"""Computes real Manaus theta_t series from SIH/DATASUS 2020-2021.

12-month series: Jul/2020–Jun/2021
  All 12 months use real SIH/DATASUS microdata
  (sih_manaus_2020_2021.parquet, ~2,678 admissions, DIAG_PRINC ∈ J96/J18/U07).

Hospital occupancy is derived proportionally from real SIH UTI rates,
anchored at Jan/2021 = 100% (ground truth: Portaria MS 69/2021).

psi_S is TIME-VARYING: each month's Clingo run injects the documented
hospital_occupancy_rate_pct for that month. The emergencia_sanitaria.lp
threshold (R > 85) activates sovereign(obligation_to_activate_coes)
only during the crisis peak, so CB emerges from the normative structure
without manual weight calibration.
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

# Jan/2021 = 100% occupancy is ground truth (Portaria MS 69/2021, "all ICU beds occupied")
_JAN2021_OCCUPANCY_ANCHOR = 100

# Crisis pressure → autonomous operation preference mapping.
_PSI_N_BASE   = np.array([0.50, 0.30, 0.20], dtype=np.float64)
_PSI_N_CRISIS = np.array([0.93, 0.04, 0.03], dtype=np.float64)


def _psi_n_from_score(score: float) -> np.ndarray:
    """Interpolate psi_N between baseline and peak-crisis vectors."""
    raw = _PSI_N_BASE + score * (_PSI_N_CRISIS - _PSI_N_BASE)
    return _normalize(raw)


def _compute_occupancy_from_sih(taxa_uti_mes: float, taxa_uti_jan_2021: float) -> int:
    """Scale occupancy proportionally to UTI rate, anchored at Jan/2021 = 100%."""
    if taxa_uti_jan_2021 <= 0:
        return 50  # fallback if anchor is zero
    scaled = (taxa_uti_mes / taxa_uti_jan_2021) * 100.0
    return int(round(min(max(scaled, 30.0), 100.0)))  # clamp 30–100


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

    Each row contains:
        label, competencia, ano_cmpt, mes_cmpt,
        internacoes, obitos, taxa_mortalidade, taxa_uti, taxa_respiratorio,
        score_pressao, hospital_occupancy_pct, theta_t, psi_n,
        data_source, evento_critico
    """
    sih = _load_and_clean_sih()

    # ── Pass 0: pre-compute UTI rates for all months (occupancy derivation) ───
    uti_by_month: dict[tuple[int, int], float] = {}
    for year, month, _ in MONTHS_PERIOD:
        mask = (sih["ANO_CMPT"] == year) & (sih["MES_CMPT"] == month)
        df_m = sih[mask]
        denom = max(len(df_m), 1)
        uti_by_month[(year, month)] = int((df_m["UTI_MES_TO"] > 0).sum()) / denom

    taxa_uti_jan_2021 = max(uti_by_month.get((2021, 1), 1e-6), 1e-6)

    # ── Pass 1: collect raw metrics for all 12 months (all SIH/DATASUS) ───────
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

    # ── Pass 2: min-max normalize across the full 12-month window ────────────
    pressures = [r["pressure_raw"] for r in raw_rows]
    p_min, p_max = min(pressures), max(pressures)
    p_range = max(p_max - p_min, 1e-10)

    # ── Pass 3: time-varying psi_S via monthly Clingo runs ───────────────────
    series: list[dict] = []
    for r in raw_rows:
        score = (r["pressure_raw"] - p_min) / p_range
        psi_n = _psi_n_from_score(float(score))

        ym = (r["year"], r["month"])
        if ym == (2021, 1):
            occ_pct = _JAN2021_OCCUPANCY_ANCHOR
        else:
            occ_pct = _compute_occupancy_from_sih(uti_by_month[ym], taxa_uti_jan_2021)

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
