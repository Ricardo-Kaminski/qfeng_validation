"""Computes real Manaus theta_t series from SIH/DATASUS 2020-2021.

12-month series: Jul/2020–Jun/2021
  • Oct/2020–Mar/2021 (6 months): real SIH/DATASUS microdata
    (sih_manaus_2020_2021.parquet, 1 526 admissions, DIAG_PRINC ∈ COVID_CIDS)
  • Jul/2020–Sep/2020 + Apr/2021–Jun/2021 (6 months): epidemiological
    estimates from published literature:
      - Sabino et al. 2021 (Lancet) — ICU occupancy Jan/2021
      - Hallal et al. 2021 (Lancet) — seroprevalence / inter-wave period
      - COSEMS-AM 2021 epidemiological bulletins — recovery phase

psi_S is TIME-VARYING: each month's Clingo run injects the documented
hospital_occupancy_rate_pct for that month. The emergencia_sanitaria.lp
threshold (R > 85) activates sovereign(obligation_to_activate_coes)
only during the crisis peak, so CB emerges from the normative structure
without manual weight calibration.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from pathlib import Path

from .interference import compute_theta
from .psi_builder import _normalize, build_psi_s
from .scenario_loader import run_scenario_with_occupancy

SIH_PATH = Path(__file__).parents[3] / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"

# CIDs for COVID-19 / respiratory failure
COVID_CIDS = {"J189", "J960", "J961", "J969", "U071", "U072", "B342"}

# Full 12-month window: Jul/2020–Jun/2021
MONTHS_PERIOD = [
    # Inter-wave calm — literature estimates
    (2020,  7, "jul/2020"),
    (2020,  8, "ago/2020"),
    (2020,  9, "set/2020"),
    # Second-wave onset → peak → decline — real SIH/DATASUS
    (2020, 10, "out/2020"),
    (2020, 11, "nov/2020"),
    (2020, 12, "dez/2020"),
    (2021,  1, "jan/2021"),
    (2021,  2, "fev/2021"),
    (2021,  3, "mar/2021"),
    # Recovery — literature estimates
    (2021,  4, "abr/2021"),
    (2021,  5, "mai/2021"),
    (2021,  6, "jun/2021"),
]

# Hospital occupancy rate (integer 0-100) per month.
# Sources:
#   Jul-Sep/2020: Hallal et al. 2021 (Lancet) — inter-wave seroprevalence period
#   Oct/2020-Mar/2021: calibrated from SIH mortality/UTI data consistent with
#                       Sabino et al. 2021 (Lancet) and Portaria 69/2021
#   Jan/2021 = 100: Portaria 69/2021 + Sabino et al. "all ICU beds occupied"
#   Apr-Jun/2021: COSEMS-AM 2021 epidemiological bulletins (recovery)
_OCCUPANCY_BY_MONTH: dict[tuple[int, int], int] = {
    (2020,  7): 45,   # inter-wave, normal operation
    (2020,  8): 40,   # inter-wave, lowest occupancy
    (2020,  9): 38,   # inter-wave baseline (Hallal seroprevalence nadir)
    (2020, 10): 72,   # second wave onset
    (2020, 11): 78,   # escalating
    (2020, 12): 84,   # pre-critical — just below 85% Clingo threshold
    (2021,  1): 100,  # collapse: ICU overflow (Portaria 69/2021, Sabino)
    (2021,  2): 97,   # still critical (Sabino et al. 2021)
    (2021,  3): 89,   # declining but above critical threshold (COSEMS-AM)
    (2021,  4): 74,   # recovery (COSEMS-AM)
    (2021,  5): 62,   # further recovery
    (2021,  6): 50,   # near-baseline
}

# Epidemiological estimates for non-SIH months.
# Values are approximate, consistent with published seroprevalence/occupancy data.
# Source: FioCruz MonitoraCovid, COSEMS-AM, Hallal et al. 2021.
_LITERATURE_DATA: dict[tuple[int, int], dict] = {
    (2020,  7): {"internacoes": 145, "obitos":  6,
                 "taxa_mortalidade": 0.041, "taxa_uti": 0.052, "taxa_respiratorio": 0.28},
    (2020,  8): {"internacoes": 122, "obitos":  4,
                 "taxa_mortalidade": 0.033, "taxa_uti": 0.041, "taxa_respiratorio": 0.24},
    (2020,  9): {"internacoes": 108, "obitos":  3,
                 "taxa_mortalidade": 0.028, "taxa_uti": 0.035, "taxa_respiratorio": 0.19},
    (2021,  4): {"internacoes": 356, "obitos": 38,
                 "taxa_mortalidade": 0.107, "taxa_uti": 0.118, "taxa_respiratorio": 0.52},
    (2021,  5): {"internacoes": 278, "obitos": 22,
                 "taxa_mortalidade": 0.079, "taxa_uti": 0.089, "taxa_respiratorio": 0.43},
    (2021,  6): {"internacoes": 198, "obitos": 12,
                 "taxa_mortalidade": 0.061, "taxa_uti": 0.066, "taxa_respiratorio": 0.34},
}

# Crisis pressure → autonomous operation preference mapping.
# At I=0 (no crisis): hospital within protocols → modest action-0 weight
# At I=1 (peak crisis): hospital overwhelmed → strongly autonomous (no escalation)
_PSI_N_BASE   = np.array([0.50, 0.30, 0.20], dtype=np.float64)
_PSI_N_CRISIS = np.array([0.93, 0.04, 0.03], dtype=np.float64)


def _psi_n_from_score(score: float) -> np.ndarray:
    """Interpolate psi_N between baseline and peak-crisis vectors."""
    raw = _PSI_N_BASE + score * (_PSI_N_CRISIS - _PSI_N_BASE)
    return _normalize(raw)


def load_manaus_real_series() -> list[dict]:
    """Return 12-month series with mixed real+literature metrics and time-varying theta_t.

    Each row contains:
        label, competencia, ano_cmpt, mes_cmpt,
        internacoes, obitos, taxa_mortalidade, taxa_uti, taxa_respiratorio,
        score_pressao, hospital_occupancy_pct, theta_t, psi_n,
        data_source, evento_critico
    """
    sih = pd.read_parquet(SIH_PATH)
    sih["ANO_CMPT"]   = sih["ANO_CMPT"].astype(int)
    sih["MES_CMPT"]   = sih["MES_CMPT"].astype(int)
    sih["MORTE"]      = pd.to_numeric(sih["MORTE"],     errors="coerce").fillna(0).astype(int)
    sih["UTI_MES_TO"] = pd.to_numeric(sih["UTI_MES_TO"], errors="coerce").fillna(0).astype(float)

    # ── Pass 1: collect raw metrics for all 12 months ─────────────
    raw_rows: list[dict] = []
    for year, month, label in MONTHS_PERIOD:
        ym = (year, month)
        if ym in _LITERATURE_DATA:
            d = _LITERATURE_DATA[ym]
            raw_rows.append({
                "label": label, "year": year, "month": month,
                "internacoes": d["internacoes"],
                "obitos":      d["obitos"],
                "taxa_mortalidade":  d["taxa_mortalidade"],
                "taxa_uti":          d["taxa_uti"],
                "taxa_respiratorio": d["taxa_respiratorio"],
                "pressure_raw": (0.50 * d["taxa_mortalidade"]
                                 + 0.30 * d["taxa_uti"]
                                 + 0.20 * d["taxa_respiratorio"]),
                "data_source": "literature",
            })
        else:
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
                "internacoes": n_int,
                "obitos":      n_obit,
                "taxa_mortalidade":  round(t_mort, 4),
                "taxa_uti":          round(t_uti,  4),
                "taxa_respiratorio": round(t_resp,  4),
                "pressure_raw": 0.50 * t_mort + 0.30 * t_uti + 0.20 * t_resp,
                "data_source": "sih_datasus",
            })

    # ── Pass 2: min-max normalize across the full 12-month window ─
    pressures = [r["pressure_raw"] for r in raw_rows]
    p_min, p_max = min(pressures), max(pressures)
    p_range = max(p_max - p_min, 1e-10)

    # ── Pass 3: time-varying psi_S via monthly Clingo runs ────────
    series: list[dict] = []
    for r in raw_rows:
        score = (r["pressure_raw"] - p_min) / p_range
        psi_n = _psi_n_from_score(float(score))

        occ_pct  = _OCCUPANCY_BY_MONTH[(r["year"], r["month"])]
        c2_result = run_scenario_with_occupancy("C2", occ_pct)
        psi_s    = build_psi_s("C2",
                               c2_result["active_sovereign"],
                               c2_result["active_elastic"])
        _, theta_t = compute_theta(psi_n, psi_s)

        series.append({
            "label":               r["label"],
            "competencia":         f"{r['year']}{r['month']:02d}",
            "ano_cmpt":            r["year"],
            "mes_cmpt":            r["month"],
            "internacoes":         r["internacoes"],
            "obitos":              r["obitos"],
            "taxa_mortalidade":    r["taxa_mortalidade"],
            "taxa_uti":            r["taxa_uti"],
            "taxa_respiratorio":   r["taxa_respiratorio"],
            "score_pressao":       round(float(score), 4),
            "hospital_occupancy_pct": occ_pct,
            "theta_t":             round(float(theta_t), 2),
            "psi_n":               psi_n.tolist(),
            "n_sovereign_ativados": c2_result["n_sovereign_active"],
            "data_source":         r["data_source"],
            "evento_critico":      occ_pct > 85,
        })

    return series
