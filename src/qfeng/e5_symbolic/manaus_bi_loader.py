"""BI bivariado loader — TOH UTI + SRAG Manaus 2020-2021.

Substitui manaus_sih_loader.py como ponto de entrada canônico para o preditor
BI bivariado do Caminho 2. Integra três fontes:

  - TOH UTI  : data/predictors/manaus_bi/toh_uti_manaus.parquet (Fase 1 Tarefa 1.1)
  - SRAG     : data/predictors/manaus_bi/srag_manaus.parquet    (stub até Fase 2 Tarefa 2.1)
  - SIH micro: data/predictors/manaus_sih/sih_manaus_2020_2021.parquet

Fix t_mort (Bug confirmado Fase 1 Tarefa 1.4):
  ANTES: pd.to_numeric(df['MORTE'], errors='coerce').fillna(0)
         → retorna NaN para strings 'Sim'/'Não' → fillna(0) zera tudo
  DEPOIS: (df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)
          → funciona com ArrowDtype str, object, e StringDtype

Resultado esperado após fix: MORTE_NUM.sum() == 482 (18% mortalidade intra-hospitalar).

Exports:
  load_manaus_bi_series()       -> list[dict]   ponto de entrada principal
  load_sih_with_fixed_tmort()   -> pd.DataFrame uso em testes de regressão
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .interference import compute_theta
from .psi_builder import _normalize, build_psi_s
from .scenario_loader import run_scenario_with_occupancy

# Paths canônicos (Fase 1 artefatos)
_BI_DIR = Path(__file__).parents[3] / "data/predictors/manaus_bi"
TOH_PATH  = _BI_DIR / "toh_uti_manaus.parquet"
SRAG_PATH = _BI_DIR / "srag_manaus.parquet"
SIH_PATH  = Path(__file__).parents[3] / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"

# CIDs COVID / insuficiência respiratória (idêntico ao manaus_sih_loader)
COVID_CIDS = {"J189", "J960", "J961", "J969", "U071", "U072", "B342"}

MONTHS_PERIOD = [
    (2020,  7), (2020,  8), (2020,  9), (2020, 10),
    (2020, 11), (2020, 12), (2021,  1), (2021,  2),
    (2021,  3), (2021,  4), (2021,  5), (2021,  6),
]


# ── Bases psi_N (copiadas do manaus_sih_loader — NÃO MODIFICAR) ─────────────
_PSI_N_BASE   = np.array([0.7, 0.2, 0.1])
_PSI_N_CRISIS = np.array([0.1, 0.3, 0.6])


def _psi_n_from_score(score: float) -> np.ndarray:
    raw = _PSI_N_BASE + score * (_PSI_N_CRISIS - _PSI_N_BASE)
    return _normalize(raw)


def load_sih_with_fixed_tmort() -> pd.DataFrame:
    """Carrega SIH parquet com MORTE_NUM corrigido.

    Fix aplicado: (df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)
    Resultado esperado: MORTE_NUM.sum() == 482

    Exposta como função pública para facilitar testes de regressão.
    """
    sih = pd.read_parquet(SIH_PATH)
    sih["ANO_CMPT"] = pd.to_numeric(sih["ANO_CMPT"], errors="coerce").fillna(0).astype(int)
    sih["MES_CMPT"] = pd.to_numeric(sih["MES_CMPT"], errors="coerce").fillna(0).astype(int)
    # Fix t_mort — funciona com ArrowDtype(str), object, StringDtype
    sih["MORTE_NUM"] = (sih["MORTE"].astype(str).str.strip() == "Sim").astype(int)
    sih["UTI_MES_TO"] = pd.to_numeric(sih["UTI_MES_TO"], errors="coerce").fillna(0).astype(float)
    return sih


def _load_toh() -> pd.DataFrame:
    """Carrega TOH UTI de toh_uti_manaus.parquet (Fase 1 Tarefa 1.1)."""
    toh = pd.read_parquet(TOH_PATH)
    toh = toh.set_index(["year", "month"])
    return toh


def _load_srag() -> pd.DataFrame:
    """Carrega SRAG de srag_manaus.parquet (stub ou real)."""
    srag = pd.read_parquet(SRAG_PATH)
    srag = srag.set_index(["year", "month"])
    return srag


def load_manaus_bi_series() -> list[dict]:
    """Retorna série bivariada de 12 meses (TOH + SRAG + métricas SIH com t_mort correto).

    Schema de cada entrada:
        label, competencia, ano_cmpt, mes_cmpt,
        internacoes, obitos, taxa_mortalidade, taxa_uti, taxa_respiratorio,
        score_pressao, hospital_occupancy_pct, toh_is_estimated,
        srag_n_covid, srag_is_stub,
        theta_t, psi_n, data_source, evento_critico

    Quando srag_is_stub=True: score_pressao usa apenas métricas SIH (fórmula original).
    Quando srag_is_stub=False (Fase 2+): SRAG normalizado será incorporado ao score.
    """
    sih  = load_sih_with_fixed_tmort()
    toh  = _load_toh()
    srag = _load_srag()

    # ── Pass 1: métricas brutas ────────────────────────────────────────────
    raw_rows: list[dict] = []
    for year, month in MONTHS_PERIOD:
        mask  = (sih["ANO_CMPT"] == year) & (sih["MES_CMPT"] == month)
        df_m  = sih[mask]
        n_int  = len(df_m)
        n_obit = int(df_m["MORTE_NUM"].sum())
        n_uti  = int((df_m["UTI_MES_TO"] > 0).sum())
        n_resp = int(df_m["DIAG_PRINC"].isin(COVID_CIDS).sum())
        denom  = max(n_int, 1)

        # TOH do parquet (Fase 1) — int para compatibilidade com Clingo
        toh_row = toh.loc[(year, month)] if (year, month) in toh.index else None
        occ_pct = int(round(toh_row["toh_uti_pct"])) if toh_row is not None else 0
        toh_estimated = bool(toh_row["is_estimated"]) if toh_row is not None else True

        # SRAG
        srag_row = srag.loc[(year, month)] if (year, month) in srag.index else None
        n_covid  = int(srag_row["n_covid"]) if srag_row is not None else 0
        is_stub  = bool(srag_row["is_stub"]) if srag_row is not None else True

        t_mort = n_obit / denom
        t_uti  = n_uti  / denom
        t_resp = n_resp / denom

        raw_rows.append({
            "year": year, "month": month,
            "internacoes":         n_int,
            "obitos":              n_obit,
            "taxa_mortalidade":    round(t_mort, 4),
            "taxa_uti":            round(t_uti,  4),
            "taxa_respiratorio":   round(t_resp,  4),
            "pressure_raw":        0.50 * t_mort + 0.30 * t_uti + 0.20 * t_resp,
            "hospital_occupancy_pct": occ_pct,
            "toh_is_estimated":    toh_estimated,
            "srag_n_covid":        n_covid,
            "srag_is_stub":        is_stub,
            "data_source":         "sih_datasus+toh_fvs_am",
        })

    # ── Pass 2: normalização de pressão ──────────────────────────────────
    pressures = [r["pressure_raw"] for r in raw_rows]
    p_min, p_max = min(pressures), max(pressures)
    p_range = max(p_max - p_min, 1e-10)

    # ── Pass 3: theta_t via Clingo ────────────────────────────────────────
    series: list[dict] = []
    for r in raw_rows:
        score   = (r["pressure_raw"] - p_min) / p_range
        psi_n   = _psi_n_from_score(float(score))
        occ_pct = r["hospital_occupancy_pct"]

        c2_result = run_scenario_with_occupancy("C2", occ_pct)
        psi_s     = build_psi_s("C2",
                                c2_result["active_sovereign"],
                                c2_result["active_elastic"])
        _, theta_t = compute_theta(psi_n, psi_s)

        label = f"{r['month']:02d}/{r['year']}"
        comp  = f"{r['year']}{r['month']:02d}"

        series.append({
            "label":                  label,
            "competencia":            comp,
            "ano_cmpt":               r["year"],
            "mes_cmpt":               r["month"],
            "internacoes":            r["internacoes"],
            "obitos":                 r["obitos"],
            "taxa_mortalidade":       r["taxa_mortalidade"],
            "taxa_uti":               r["taxa_uti"],
            "taxa_respiratorio":      r["taxa_respiratorio"],
            "score_pressao":          round(float(score), 4),
            "hospital_occupancy_pct": occ_pct,
            "toh_is_estimated":       r["toh_is_estimated"],
            "srag_n_covid":           r["srag_n_covid"],
            "srag_is_stub":           r["srag_is_stub"],
            "theta_t":                round(float(theta_t), 2),
            "psi_n":                  psi_n.tolist(),
            "n_sovereign_ativados":   c2_result["n_sovereign_active"],
            "data_source":            r["data_source"],
            "evento_critico":         occ_pct > 85,
        })

    return series
