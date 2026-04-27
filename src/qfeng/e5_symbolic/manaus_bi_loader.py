"""BI bivariado loader — TOH UTI + SRAG Manaus 2020-2021 (granularidade semanal SE).

Substitui manaus_sih_loader.py como ponto de entrada canônico para o preditor
BI bivariado do Caminho 2. Integra três fontes:

  - TOH semanal : data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet
                  74 SEs raw (Fase 2.1.5-bis); série ativa = 70 SEs via SE_INICIO_SERIE_FRENTE1.
                  Exportado em percentual (0–211.5), pico SE 03/2021 = 211.5%.
  - SRAG semanal: data/predictors/manaus_bi/derived/srag_semanal_manaus.parquet
                  73 SEs, SIVEP-Gripe INFLUD20/21, is_stub=False. Fase 2 Tarefa 2.B.
  - SIH micro   : data/predictors/manaus_sih/sih_manaus_2020_2021.parquet
                  Usado para métricas mensais (t_mort, t_uti, t_resp) mapeadas à SE.

Fix t_mort (Bug confirmado Fase 1 Tarefa 1.4):
  ANTES: pd.to_numeric(df['MORTE'], errors='coerce').fillna(0)
         → retorna NaN para strings 'Sim'/'Não' → fillna(0) zera tudo
  DEPOIS: (df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)

Resultado esperado após fix: MORTE_NUM.sum() == 482 (18% mortalidade intra-hospitalar).

Exports:
  load_manaus_bi_series()       -> list[dict]   ponto de entrada principal (73 SEs)
  load_sih_with_fixed_tmort()   -> pd.DataFrame uso em testes de regressão
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .interference import compute_theta
from .psi_builder import _normalize, build_psi_s
from .scenario_loader import run_scenario_with_occupancy

# Paths canônicos — Fase 2 derived/ (granularidade semanal)
_BI_DIR   = Path(__file__).parents[3] / "data/predictors/manaus_bi"
TOH_PATH  = _BI_DIR / "derived/toh_semanal_manaus.parquet"
SRAG_PATH = _BI_DIR / "derived/srag_semanal_manaus.parquet"
SIH_PATH  = Path(__file__).parents[3] / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"

# CIDs COVID / insuficiência respiratória (idêntico ao manaus_sih_loader)
COVID_CIDS = {"J189", "J960", "J961", "J969", "U071", "U072", "B342"}

# Janela de semanas epidemiológicas (SE 10/2020 → SE 30/2021 = 73 SEs)
SE_WINDOW = [
    *[(2020, w) for w in range(10, 54)],   # SE 10-53/2020 = 44 SEs (2020 tem 53 semanas ISO)
    *[(2021, w) for w in range(1,  31)],   # SE  1-30/2021 = 30 SEs
]  # = 74 SEs raw — alinhado com toh_semanal_manaus.parquet (Fase 2.1.5-bis)

# Opção 2 (27/abr/2026): exclui SE 10-13/2020 (TOH=0, consolidação tardia DEMAS-VEPI)
# Série ativa: SE 14/2020 → SE 30/2021 = 70 SEs
SE_INICIO_SERIE_FRENTE1: int = 202014

# Para mapeamento SE → mês (métricas SIH mensais)
_MONTHS_PERIOD = [
    (2020,  7), (2020,  8), (2020,  9), (2020, 10),
    (2020, 11), (2020, 12), (2021,  1), (2021,  2),
    (2021,  3), (2021,  4), (2021,  5), (2021,  6),
]

# Bases psi_N — idênticas ao manaus_sih_loader (NÃO MODIFICAR — contrato matemático Q-FENG)
# ATENÇÃO: valores anteriores [0.7,0.2,0.1]/[0.1,0.3,0.6] eram incorretos;
# causavam inversão: θ↑ em score=0, θ↓ em score=1 (oposto à hipótese de antecipação).
_PSI_N_BASE   = np.array([0.50, 0.30, 0.20], dtype=np.float64)
_PSI_N_CRISIS = np.array([0.93, 0.04, 0.03], dtype=np.float64)


def _psi_n_from_score(score: float) -> np.ndarray:
    raw = _PSI_N_BASE + score * (_PSI_N_CRISIS - _PSI_N_BASE)
    return _normalize(raw)


def _se_to_month(year: int, week: int) -> tuple[int, int]:
    """Mapeia (year, week_se) → (year, month) para lookup de métricas SIH."""
    try:
        date = pd.Timestamp.fromisocalendar(year, week, 1)
    except ValueError:
        # SE 53 em anos sem 53 semanas → usa última SE do ano
        date = pd.Timestamp(f"{year}-12-28")
    return date.year, date.month


def load_sih_with_fixed_tmort() -> pd.DataFrame:
    """Carrega SIH parquet com MORTE_NUM corrigido.

    Fix aplicado: (df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)
    Resultado esperado: MORTE_NUM.sum() == 482
    """
    sih = pd.read_parquet(SIH_PATH)
    sih["ANO_CMPT"] = pd.to_numeric(sih["ANO_CMPT"], errors="coerce").fillna(0).astype(int)
    sih["MES_CMPT"] = pd.to_numeric(sih["MES_CMPT"], errors="coerce").fillna(0).astype(int)
    # Fix t_mort — funciona com ArrowDtype(str), object, StringDtype
    sih["MORTE_NUM"] = (sih["MORTE"].astype(str).str.strip() == "Sim").astype(int)
    sih["UTI_MES_TO"] = pd.to_numeric(sih["UTI_MES_TO"], errors="coerce").fillna(0).astype(float)
    return sih


def _load_toh() -> pd.DataFrame:
    """Carrega TOH semanal de derived/toh_semanal_manaus.parquet (Fase 2.1.5-bis DEMAS-VEPI).

    Parquet usa year_se/sem_epi (Task 4 schema); renomeados para year/week_se
    para compatibilidade com SE_WINDOW.
    toh_uti_pct está em fração (0–2.12); convertido para percentual (×100)
    em load_manaus_bi_series() — Contrato reprodutibilidade Zenodo: unidade = %.
    """
    toh = pd.read_parquet(TOH_PATH)
    toh = toh.rename(columns={"year_se": "year", "sem_epi": "week_se"})
    toh = toh.set_index(["year", "week_se"])
    return toh


def _load_srag() -> pd.DataFrame:
    """Carrega SRAG semanal de derived/srag_semanal_manaus.parquet (Fase 2 Tarefa 2.B).

    Valida is_stub=False — dados reais SIVEP-Gripe INFLUD20/21.
    """
    srag = pd.read_parquet(SRAG_PATH)
    assert not srag["is_stub"].any(), (
        "srag_semanal_manaus.parquet contém is_stub=True. "
        "Use o arquivo em derived/ (Tarefa 2.B), não o stub da Fase 1."
    )
    srag = srag.set_index(["year", "week_se"])
    return srag


def _build_sih_monthly_metrics(sih: pd.DataFrame) -> dict[tuple[int, int], dict]:
    """Pré-computa métricas mensais do SIH para mapeamento a SEs."""
    metrics: dict[tuple[int, int], dict] = {}
    for year, month in _MONTHS_PERIOD:
        mask  = (sih["ANO_CMPT"] == year) & (sih["MES_CMPT"] == month)
        df_m  = sih[mask]
        n_int  = len(df_m)
        n_obit = int(df_m["MORTE_NUM"].sum())
        n_uti  = int((df_m["UTI_MES_TO"] > 0).sum())
        n_resp = int(df_m["DIAG_PRINC"].isin(COVID_CIDS).sum())
        denom  = max(n_int, 1)
        metrics[(year, month)] = {
            "internacoes":       n_int,
            "obitos":            n_obit,
            "taxa_mortalidade":  round(n_obit / denom, 4),
            "taxa_uti":          round(n_uti  / denom, 4),
            "taxa_respiratorio": round(n_resp / denom, 4),
        }
    return metrics


def load_manaus_bi_series() -> list[dict]:
    """Retorna série bivariada de 70 SEs (SE 14/2020 → SE 30/2021).

    Opção 2 (27/abr/2026): série truncada em SE_INICIO_SERIE_FRENTE1=202014,
    excluindo 4 SEs com TOH=0 por consolidação tardia DEMAS-VEPI (202010-202013).

    Schema de cada entrada:
        label, competencia, year, week_se, month_sih,
        internacoes, obitos, taxa_mortalidade, taxa_uti, taxa_respiratorio,
        score_pressao, hospital_occupancy_pct, toh_is_estimated,
        srag_n_covid, srag_is_stub,
        theta_t, psi_n, data_source, evento_critico

    score_pressao usa métricas mensais SIH mapeadas ao mês da SE.
    TOH e SRAG são semanais (is_stub=False garantido).
    """
    sih  = load_sih_with_fixed_tmort()
    toh  = _load_toh()
    srag = _load_srag()
    sih_metrics = _build_sih_monthly_metrics(sih)

    # Aplica corte Opção 2: exclui SEs < SE_INICIO_SERIE_FRENTE1
    active_window = [
        (y, w) for (y, w) in SE_WINDOW if y * 100 + w >= SE_INICIO_SERIE_FRENTE1
    ]

    # ── Pass 1: métricas brutas por SE ───────────────────────────────────
    raw_rows: list[dict] = []
    for year, week in active_window:
        # Mapeia SE → mês para lookup de métricas SIH mensais
        sih_year, sih_month = _se_to_month(year, week)
        month_key = (sih_year, sih_month)
        # Cai para o mês mais próximo disponível se fora do range
        if month_key not in sih_metrics:
            closest = min(_MONTHS_PERIOD, key=lambda m: abs(m[0]*12+m[1] - sih_year*12-sih_month))
            month_key = closest
        m = sih_metrics[month_key]

        # TOH semanal
        toh_row = toh.loc[(year, week)] if (year, week) in toh.index else None
        # ×100: toh_uti_pct é fração (0–2.12); hospital_occupancy_pct exportado em % (0–211.5)
        # Guard NaN: SEs iniciais (SE 10-22/2020) têm toh_uti_pct=NaN (sem dados DEMAS-VEPI)
        toh_val = toh_row["toh_uti_pct"] if toh_row is not None else float("nan")
        occ_pct = int(round(toh_val * 100)) if (toh_row is not None and not np.isnan(toh_val)) else 0
        toh_estimated = bool(toh_row["is_imputed"]) if toh_row is not None else True

        # SRAG semanal
        srag_row = srag.loc[(year, week)] if (year, week) in srag.index else None
        n_covid  = int(srag_row["n_covid"])  if srag_row is not None else 0
        is_stub  = False  # garantido por _load_srag()

        pressure_raw = (0.50 * m["taxa_mortalidade"]
                        + 0.30 * m["taxa_uti"]
                        + 0.20 * m["taxa_respiratorio"])

        raw_rows.append({
            "year": year, "week": week,
            "month_sih":           month_key[1],
            "internacoes":         m["internacoes"],
            "obitos":              m["obitos"],
            "taxa_mortalidade":    m["taxa_mortalidade"],
            "taxa_uti":            m["taxa_uti"],
            "taxa_respiratorio":   m["taxa_respiratorio"],
            "pressure_raw":        pressure_raw,
            "hospital_occupancy_pct": occ_pct,
            "toh_is_estimated":    toh_estimated,
            "srag_n_covid":        n_covid,
            "srag_is_stub":        is_stub,
            "data_source":         "sih_datasus+toh_demas_vepi_semanal+srag_sivep",
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

        year, week = r["year"], r["week"]
        label = f"SE{week:02d}/{year}"
        comp  = f"{year}{week:02d}"

        series.append({
            "label":                  label,
            "competencia":            comp,
            "year":                   year,
            "week_se":                week,
            "month_sih":              r["month_sih"],
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
