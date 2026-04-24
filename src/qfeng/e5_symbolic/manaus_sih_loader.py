"""Computes real Manaus theta_t series from SIH/DATASUS 2020-2021.

12-month series: Jul/2020–Jun/2021
  All 12 months use real SIH/DATASUS microdata
  (sih_manaus_2020_2021.parquet, ~2,678 admissions, DIAG_PRINC in J96/J18/U07).

Hospital occupancy (TOH UTI COVID SUS Manaus) is sourced from published
institutional bulletins — FVS-AM Boletim COVID-19 (Secretaria de Estado de
Saúde do Amazonas / Fundacao de Vigilancia em Saude) and Observatorio
Covid-19 Fiocruz — which report daily/weekly ICU bed occupancy using the
canonical TOH formula (pacientes-dia / leitos-dia operacionais) × 100.
See _TOH_FVS_AM for per-month values and primary sources.

Values above 100% (Jan-Feb/2021) reflect documented over-capacity operation
during the crisis peak, consistent with ANS E-EFI-01 guidance that TOH > 100%
occurs when hospitals operate with extra beds beyond the cadastral count.

psi_S is TIME-VARYING: each month's Clingo run injects the documented
hospital_occupancy_pct for that month. The emergencia_sanitaria.lp
threshold (R > 85) activates sovereign(obligation_to_activate_coes)
only during the crisis peak (Dec/2020–Mar/2021), so CB emerges from
the normative structure without manual weight calibration.

Primary sources for Portaria references in this module:
  - ICU collapse Jan/2021: FVS-AM Boletim COVID-19, 16 jan 2021
    (103.69% UTI publica); SES-AM requisicao compulsoria 14/fev/2021
  - Emergency decrees: Decreto AM 43.269/2021 (4/jan); Decreto AM 43.303/2021
    (23/jan); Decreto AM 43.360/2021 (4/fev, calamidade publica estadual)
  - Portaria GM/MS 69/2021 (18/jan): institui obrigatoriedade de registro de
    aplicacao de vacinas — documento de data-reporting, NAO declaracao de
    colapso hospitalar; NAO usar como ancora de ocupacao UTI.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .interference import compute_theta
from .psi_builder import _normalize, build_psi_s
from .scenario_loader import run_scenario_with_occupancy

SIH_PATH = Path(__file__).parents[3] / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"

# CIDs for COVID-19 / respiratory failure
COVID_CIDS = {"J189", "J960", "J961", "J969", "U071", "U072", "B342"}

# Full 12-month window: Jul/2020–Jun/2021
MONTHS_PERIOD = [
    (2020,  7, "jul/2020"),
    (2020,  8, "ago/2020"),
    (2020,  9, "set/2020"),
    (2020, 10, "out/2020"),
    (2020, 11, "nov/2020"),
    (2020, 12, "dez/2020"),
    (2021,  1, "jan/2021"),
    (2021,  2, "fev/2021"),
    (2021,  3, "mar/2021"),
    (2021,  4, "abr/2021"),
    (2021,  5, "mai/2021"),
    (2021,  6, "jun/2021"),
]

# TOH UTI COVID SUS Manaus — valores documentados por fontes institucionais primarias.
# Formula canonica MS/ANS: TOH = (pacientes-dia / leitos-dia operacionais) x 100.
# Valores acima de 100% em jan-fev/2021 refletem operacao em sobre-capacidade
# documentada (ANS E-EFI-01; FVS-AM Boletim COVID-19 16/jan/2021: 103.69%).
#
# Fontes por mes:
#   Jul/2020: FVS-AM/SES-AM nota 7/ago/2020; 49/165 leitos = 29.7%
#   Ago/2020: FVS-AM Boletim 18/ago/2020; 24.4% (58 pacientes UTI, pub+priv)
#   Set/2020: Fiocruz Observatorio Covid-19 SE40-42; abaixo de 60%, fora de
#             zona de alerta (estimado 45%; interondas)
#   Out/2020: SUSAM/Amazonas Atual 27/out/2020; ~82% (80/223 leitos UTI)
#   Nov/2020: Fiocruz Observatorio SE48-49; 76% em 7/dez (representativo nov)
#   Dez/2020: SES-AM Plano Contingencia 3a fase; >92% em 25/dez/2020
#   Jan/2021: FVS-AM Boletim 16/jan/2021; 103.69% UTI publica (colapso)
#   Fev/2021: SES-AM 4/fev/2021; 366/379 UTI publicas = 101% (adulto)
#   Mar/2021: Fiocruz Observatorio 8/mar/2021; 87% (zona critica)
#   Abr/2021: FVS-AM Boletim de Risco; 74.5% (19/abr) a 67.77% (28/abr) = media 71%
#   Mai/2021: FVS-AM Boletim de Risco; 68.9-70.68% = media 70%
#   Jun/2021: Estimado por interpolacao; queda progressiva pos-pico = ~70%
_TOH_FVS_AM: dict[tuple[int, int], int] = {
    (2020,  7):  30,
    (2020,  8):  24,
    (2020,  9):  45,   # estimado; abaixo de 60%, fora zona alerta Fiocruz
    (2020, 10):  82,
    (2020, 11):  76,
    (2020, 12):  92,
    (2021,  1): 104,   # FVS-AM 16/jan: 103.69%; arredondado; >100% documentado
    (2021,  2): 101,   # SES-AM 4/fev: 366/379 UTI publicas adulto
    (2021,  3):  87,
    (2021,  4):  71,   # media 74.5% (19/abr) e 67.77% (28/abr)
    (2021,  5):  70,
    (2021,  6):  70,   # estimado
}

# Crisis pressure → autonomous operation preference mapping.
_PSI_N_BASE   = np.array([0.50, 0.30, 0.20], dtype=np.float64)
_PSI_N_CRISIS = np.array([0.93, 0.04, 0.03], dtype=np.float64)


def _psi_n_from_score(score: float) -> np.ndarray:
    """Interpolate psi_N between baseline and peak-crisis vectors."""
    raw = _PSI_N_BASE + score * (_PSI_N_CRISIS - _PSI_N_BASE)
    return _normalize(raw)


def _load_and_clean_sih() -> pd.DataFrame:
    """Load parquet and normalise column types produced by microdatasus process_sih()."""
    sih = pd.read_parquet(SIH_PATH)
    # ANO_CMPT / MES_CMPT are stored as numeric strings after process_sih
    sih["ANO_CMPT"] = pd.to_numeric(sih["ANO_CMPT"], errors="coerce").fillna(0).astype(int)
    sih["MES_CMPT"] = pd.to_numeric(sih["MES_CMPT"], errors="coerce").fillna(0).astype(int)
    # MORTE is stored as 'Sim'/'Não' after process_sih labelling
    if sih["MORTE"].dtype == object:
        sih["MORTE"] = (sih["MORTE"].str.strip() == "Sim").astype(int)
    else:
        sih["MORTE"] = pd.to_numeric(sih["MORTE"], errors="coerce").fillna(0).astype(int)
    # UTI_MES_TO is stored as numeric string
    sih["UTI_MES_TO"] = pd.to_numeric(sih["UTI_MES_TO"], errors="coerce").fillna(0).astype(float)
    return sih


def load_manaus_real_series() -> list[dict]:
    """Return 12-month series with real SIH/DATASUS metrics and time-varying theta_t.

    Hospital occupancy (hospital_occupancy_pct) is sourced from _TOH_FVS_AM —
    documented TOH UTI COVID SUS Manaus values from FVS-AM/Fiocruz institutional
    bulletins — NOT derived from the SIH UTI rate proxy, which measures case-mix
    (proportion of admissions that used ICU), not bed occupancy.

    Each row contains:
        label, competencia, ano_cmpt, mes_cmpt,
        internacoes, obitos, taxa_mortalidade, taxa_uti, taxa_respiratorio,
        score_pressao, hospital_occupancy_pct, theta_t, psi_n,
        data_source, evento_critico
    """
    sih = _load_and_clean_sih()

    # ── Pass 1: collect raw metrics for all 12 months ────────────────────────
    raw_rows: list[dict] = []
    for year, month, label in MONTHS_PERIOD:
        mask = (sih["ANO_CMPT"] == year) & (sih["MES_CMPT"] == month)
        df_m  = sih[mask]
        n_int  = len(df_m)
        n_obit = int(df_m["MORTE"].sum())
        n_uti  = int((df_m["UTI_MES_TO"] > 0).sum())
        n_resp = int(df_m["DIAG_PRINC"].isin(COVID_CIDS).sum())
        denom  = max(n_int, 1)
        t_mort = n_obit / denom
        t_uti  = n_uti  / denom
        t_resp = n_resp / denom
        raw_rows.append({
            "label": label, "year": year, "month": month,
            "internacoes":         n_int,
            "obitos":              n_obit,
            "taxa_mortalidade":    round(t_mort, 4),
            "taxa_uti":            round(t_uti,  4),
            "taxa_respiratorio":   round(t_resp,  4),
            "pressure_raw": 0.50 * t_mort + 0.30 * t_uti + 0.20 * t_resp,
            "data_source": "sih_datasus",
        })

    # ── Pass 2: min-max normalize pressure across the full 12-month window ───
    pressures = [r["pressure_raw"] for r in raw_rows]
    p_min, p_max = min(pressures), max(pressures)
    p_range = max(p_max - p_min, 1e-10)

    # ── Pass 3: time-varying psi_S via monthly Clingo runs ───────────────────
    series: list[dict] = []
    for r in raw_rows:
        score = (r["pressure_raw"] - p_min) / p_range
        psi_n = _psi_n_from_score(float(score))

        ym = (r["year"], r["month"])
        occ_pct = _TOH_FVS_AM[ym]

        c2_result = run_scenario_with_occupancy("C2", occ_pct)
        psi_s     = build_psi_s("C2",
                                c2_result["active_sovereign"],
                                c2_result["active_elastic"])
        _, theta_t = compute_theta(psi_n, psi_s)

        series.append({
            "label":                  r["label"],
            "competencia":            f"{r['year']}{r['month']:02d}",
            "ano_cmpt":               r["year"],
            "mes_cmpt":               r["month"],
            "internacoes":            r["internacoes"],
            "obitos":                 r["obitos"],
            "taxa_mortalidade":       r["taxa_mortalidade"],
            "taxa_uti":               r["taxa_uti"],
            "taxa_respiratorio":      r["taxa_respiratorio"],
            "score_pressao":          round(float(score), 4),
            "hospital_occupancy_pct": occ_pct,
            "theta_t":                round(float(theta_t), 2),
            "psi_n":                  psi_n.tolist(),
            "n_sovereign_ativados":   c2_result["n_sovereign_active"],
            "data_source":            r["data_source"],
            "evento_critico":         occ_pct > 85,
        })

    return series
