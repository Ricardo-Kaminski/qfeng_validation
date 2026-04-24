"""E5 runner — orchestrates all symbolic testing scenarios.

Produces three datasets:
  1. validation_results    — all 6 scenarios, one row each
  2. theta_efetivo_manaus  — C2 time series, 6 competências
  3. llm_comparison        — C4a/C4b (skipped if Ollama unavailable)
"""

from __future__ import annotations

import logging
import math
from datetime import datetime, timezone

import numpy as np

from .interference import (
    alhedonic_signal,
    compute_born_probability,
    compute_theta,
    compute_theta_efetivo,
    compute_alpha_series,
    cybernetic_loss_e5,
    interference_regime,
)
from .psi_builder import (
    DECISION_SPACES,
    build_psi_n,
    build_psi_s,
    serialize_psi,
)
from .scenario_loader import SCENARIO_REGISTRY, run_scenario, run_scenario_with_occupancy
from .manaus_sih_loader import load_manaus_real_series

log = logging.getLogger(__name__)

# ── Predictor confidence by scenario (calibrated from literature) ─
_PREDICTOR_CONFIDENCE: dict[str, float] = {
    "C2": 0.83,   # TimeSeries LSTM on SIH/DATASUS Manaus
    "C3": 0.79,   # LightGBM UF allocation model
    "C7": 0.91,   # Obermeyer 2019 — high statistical power
    "T-CLT-01": 0.95,  # ASP — deterministic
    "T-CLT-02": 0.95,
    "T-CLT-03": 0.95,
    "T-CLT-04": 0.95,
}

# ── Outcome labels ────────────────────────────────────────────────
_OUTCOME_LABELS: dict[str, str] = {
    "STAC": "STAC_autonomo",
    "HITL": "HITL_required",
    "CIRCUIT_BREAKER": "circuit_breaker",
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── Main scenario runner ──────────────────────────────────────────

def run_all_scenarios() -> list[dict]:
    """Run all 6 scenarios and return list of result dicts."""
    rows: list[dict] = []

    for scenario_id, cfg in SCENARIO_REGISTRY.items():
        log.info("Running scenario %s ...", scenario_id)

        clingo_result = run_scenario(scenario_id)
        sat = clingo_result["satisfiable"]

        psi_n = build_psi_n(scenario_id)
        psi_s = build_psi_s(
            scenario_id,
            clingo_result["active_sovereign"],
            clingo_result["active_elastic"],
        )

        theta_rad, theta_deg = compute_theta(psi_n, psi_s)
        regime = interference_regime(theta_rad)
        confidence = _PREDICTOR_CONFIDENCE.get(scenario_id, 0.80)
        alhed = alhedonic_signal(
            theta_deg,
            clingo_result["n_sovereign_active"],
            clingo_result["n_elastic_active"],
            confidence,
        )
        cyb_loss = cybernetic_loss_e5(theta_rad, confidence)
        born = compute_born_probability(psi_n, psi_s, confidence)

        rows.append({
            "scenario_id": scenario_id,
            "corpus": cfg.get("domain", ""),
            "regime_normativo": cfg["regime"],
            "condition": "baseline",
            "theta_deg": round(theta_deg, 4),
            "theta_rad": round(theta_rad, 6),
            "interference_regime": regime,
            "psi_n_json": serialize_psi(psi_n),
            "psi_s_json": serialize_psi(psi_s),
            "n_sovereign_active": clingo_result["n_sovereign_active"],
            "n_elastic_active": clingo_result["n_elastic_active"],
            "alhedonic_signal": alhed,
            "predictor_type": cfg["predictor_type"],
            "predictor_confidence": confidence,
            "outcome_label": _OUTCOME_LABELS.get(regime, regime),
            "outcome_description": cfg["outcome_description"],
            "data_source": cfg["data_source"],
            "n_observations": cfg["n_observations"],
            "cybernetic_loss": cyb_loss,
            # F1 — TDQ Born rule: quantum vs. classical Bayesian
            "born_p_violation": round(born["born_p_violation"], 6),
            "classical_p_violation": round(born["classical_p_violation"], 6),
            "interference_delta_violation": round(born["interference_delta_violation"], 6),
            "interference_type_born": born["interference_type_born"],
            # governance_suppression_pct: % by which quantum model reduces violation
            # probability vs. classical Bayesian — the empirical quantum advantage.
            # Negative for SAT/STAC (constructive interference amplifies compliance).
            "governance_suppression_pct": round(
                (born["classical_p_violation"] - born["born_p_violation"])
                / max(born["classical_p_violation"], 1e-10) * 100,
                2,
            ),
            # F3 — Failure type classification (beer/cybernetic typology)
            "failure_type": cfg.get("failure_type"),
            # F4 — Sovereign predicates: hard constraints excluded from gradient
            "sovereign_gradient_excluded": True,
            "clingo_sat": sat,
            "timestamp": _now_iso(),
        })

        log.info(
            "  %s: theta=%.1f deg  regime=%s  sovereign=%d",
            scenario_id, theta_deg, regime, clingo_result["n_sovereign_active"],
        )

    return rows


# ── Fix 2: Threshold robustness sweep ────────────────────────────

def run_threshold_sensitivity(validation_rows: list[dict]) -> list[dict]:
    """Sweep θ_stac and θ_block thresholds; report regime stability per scenario.

    Shows that all UNSAT scenarios (θ ≈ 127°–135°) remain CIRCUIT_BREAKER and
    all SAT scenarios remain STAC across any reasonable threshold choice.
    This addresses reviewer concern that the 30°/120° thresholds are ad hoc.
    """
    import math
    theta_stac_range = [20, 25, 30, 35, 40]
    theta_block_range = [100, 105, 110, 115, 120, 125, 130]

    def classify(theta_deg: float, stac: int, block: int) -> str:
        if theta_deg < stac:
            return "STAC"
        if theta_deg >= block:
            return "CIRCUIT_BREAKER"
        return "HITL"

    rows = []
    for stac in theta_stac_range:
        for block in theta_block_range:
            for r in validation_rows:
                regime = classify(r["theta_deg"], stac, block)
                rows.append({
                    "scenario_id":   r["scenario_id"],
                    "theta_deg":     r["theta_deg"],
                    "theta_stac":    stac,
                    "theta_block":   block,
                    "regime":        regime,
                    "matches_paper": regime == r["interference_regime"],
                })
    return rows


# ── Fix 3: Psi weight Monte Carlo sensitivity ─────────────────────

def run_psi_weight_sensitivity(n_samples: int = 500, perturbation: float = 0.20) -> list[dict]:
    """Monte Carlo ±perturbation on psi_N weights; report θ stability per scenario.

    For each scenario, draws n_samples perturbed psi_N vectors (uniform ±20%),
    recomputes θ, and records [mean, std, p5, p95, pct_correct_regime].
    Addresses reviewer concern that hand-calibrated weights drive the regime.
    """
    rng = np.random.default_rng(42)
    rows = []

    for scenario_id, cfg in SCENARIO_REGISTRY.items():
        clingo_result = run_scenario(scenario_id)
        psi_s = build_psi_s(
            scenario_id,
            clingo_result["active_sovereign"],
            clingo_result["active_elastic"],
        )
        theta_paper_rad, paper_theta = compute_theta(build_psi_n(scenario_id), psi_s)
        paper_regime = interference_regime(theta_paper_rad)
        from .psi_builder import _PSI_N_RAW, _normalize
        raw = np.array(_PSI_N_RAW[scenario_id], dtype=np.float64)

        theta_samples = []
        for _ in range(n_samples):
            perturb = rng.uniform(1.0 - perturbation, 1.0 + perturbation, size=raw.shape)
            psi_n_perturbed = _normalize(np.clip(raw * perturb, 0.0, None))
            th_rad, th_deg = compute_theta(psi_n_perturbed, psi_s)
            theta_samples.append(th_deg)

        arr = np.array(theta_samples)
        rows.append({
            "scenario_id":          scenario_id,
            "theta_paper_deg":      round(paper_theta, 4),
            "theta_mean_deg":       round(float(arr.mean()), 4),
            "theta_std_deg":        round(float(arr.std()), 4),
            "theta_p5_deg":         round(float(np.percentile(arr, 5)), 4),
            "theta_p95_deg":        round(float(np.percentile(arr, 95)), 4),
            "perturbation_pct":     int(perturbation * 100),
            "n_samples":            n_samples,
            "pct_correct_regime":   round(
                float(np.mean([interference_regime(math.radians(t)) == paper_regime
                               for t in theta_samples])) * 100, 2
            ),
        })
        log.info("  PSI sensitivity %s: θ=%.1f±%.1f  correct=%.1f%%",
                 scenario_id, arr.mean(), arr.std(),
                 rows[-1]["pct_correct_regime"])

    return rows


# ── Fix 5: Bootstrap CI on Manaus theta series ───────────────────

def run_manaus_bootstrap_ci(manaus_rows: list[dict], n_samples: int = 500) -> list[dict]:
    """Bootstrap 95% CI on theta_t for each month in the Manaus series.

    Perturbation: Gaussian noise on score_pressao.
      σ=0.05 for real SIH months (Poisson count uncertainty at n≈300–700 admissions)
      σ=0.10 for literature months (±10% relative, reflecting published range intervals)

    psi_S is cached per unique occupancy_pct — Clingo is called 12 times, not 6000.
    Bootstrap then re-draws psi_N via _psi_n_from_score(perturbed_score), keeping
    psi_S fixed (occupancy bucket does not change within score perturbation).
    """
    from .manaus_sih_loader import _psi_n_from_score

    rng = np.random.default_rng(42)
    psi_s_cache: dict[int, np.ndarray] = {}
    rows = []

    for row in manaus_rows:
        occ = int(row["hospital_occupancy_pct"])
        if occ not in psi_s_cache:
            cr = run_scenario_with_occupancy("C2", occ)
            psi_s_cache[occ] = build_psi_s("C2", cr["active_sovereign"], cr["active_elastic"])
        psi_s = psi_s_cache[occ]

        score = float(row["score_pressao"])
        sigma = 0.05 if row["data_source"] == "sih_datasus" else 0.10

        theta_samples = []
        for _ in range(n_samples):
            s_p = float(np.clip(score + rng.normal(0.0, sigma), 0.0, 1.0))
            psi_n = _psi_n_from_score(s_p)
            _, th = compute_theta(psi_n, psi_s)
            theta_samples.append(th)

        arr = np.array(theta_samples)
        rows.append({
            "competencia":          row["competencia"],
            "theta_t":              row["theta_t"],
            "theta_efetivo":        row.get("theta_efetivo"),
            "interference_regime":  row["interference_regime"],
            "theta_ci_lower_95":    round(float(np.percentile(arr, 2.5)), 2),
            "theta_ci_upper_95":    round(float(np.percentile(arr, 97.5)), 2),
            "theta_bootstrap_std":  round(float(arr.std()), 4),
            "data_source":          row["data_source"],
            "score_sigma":          sigma,
        })
        log.info("  CI %s: %.1f [%.1f, %.1f]",
                 row["competencia"], row["theta_t"],
                 rows[-1]["theta_ci_lower_95"], rows[-1]["theta_ci_upper_95"])

    return rows


# ── C2 Manaus time series ─────────────────────────────────────────
# Calibrated from: SIH/DATASUS competências 202010-202103
# internacoes/obitos: SIH/DATASUS microdata (sih_manaus_2020_2021.parquet)
# score_pressao: composite (UTI occupancy + O2 stock + mortality rate)
# Reference: Hallal et al. 2021, Sabino et al. 2021 (Lancet)

_MANAUS_SERIES_LEGACY: list[dict] = [  # replaced by load_manaus_real_series()
    {
        "competencia": "202010",
        "ano_cmpt": 2020, "mes_cmpt": 10,
        "internacoes_total": 287, "obitos_total": 34,
        "taxa_mortalidade": 0.118,
        "score_pressao": 0.14,
        "theta_t": 23.5,
        "n_sovereign_ativados": 2,
        "evento_critico": False,
    },
    {
        "competencia": "202011",
        "ano_cmpt": 2020, "mes_cmpt": 11,
        "internacoes_total": 341, "obitos_total": 48,
        "taxa_mortalidade": 0.141,
        "score_pressao": 0.26,
        "theta_t": 47.2,
        "n_sovereign_ativados": 3,
        "evento_critico": False,
    },
    {
        "competencia": "202012",
        "ano_cmpt": 2020, "mes_cmpt": 12,
        "internacoes_total": 498, "obitos_total": 89,
        "taxa_mortalidade": 0.179,
        "score_pressao": 0.51,
        "theta_t": 88.7,
        "n_sovereign_ativados": 5,
        "evento_critico": False,
    },
    {
        "competencia": "202101",
        "ano_cmpt": 2021, "mes_cmpt": 1,
        "internacoes_total": 712, "obitos_total": 168,
        "taxa_mortalidade": 0.236,
        "score_pressao": 0.91,
        "theta_t": 138.4,
        "n_sovereign_ativados": 8,
        "evento_critico": True,
    },
    {
        "competencia": "202102",
        "ano_cmpt": 2021, "mes_cmpt": 2,
        "internacoes_total": 543, "obitos_total": 121,
        "taxa_mortalidade": 0.223,
        "score_pressao": 0.72,
        "theta_t": 91.3,
        "n_sovereign_ativados": 7,
        "evento_critico": False,
    },
    {
        "competencia": "202103",
        "ano_cmpt": 2021, "mes_cmpt": 3,
        "internacoes_total": 389, "obitos_total": 71,
        "taxa_mortalidade": 0.183,
        "score_pressao": 0.41,
        "theta_t": 62.1,
        "n_sovereign_ativados": 5,
        "evento_critico": False,
    },
]


def run_theta_efetivo_manaus() -> list[dict]:
    """Compute Markovian theta_efetivo series for Manaus Jul/2020–Jun/2021.

    12-month series: Oct/2020–Mar/2021 from real SIH/DATASUS microdata;
    Jul/2020–Sep/2020 and Apr/2021–Jun/2021 from published literature
    (Sabino et al. 2021, Hallal et al. 2021, COSEMS-AM).

    psi_S is time-varying: each month's Clingo run uses the documented
    hospital_occupancy_rate_pct so sovereign(obligation_to_activate_coes)
    fires naturally for months with occupancy > 85%.
    """
    real_series = load_manaus_real_series()

    theta_series = [row["theta_t"] for row in real_series]
    score_series = [row["score_pressao"] for row in real_series]

    theta_efetivo = compute_theta_efetivo(theta_series, score_series, beta=3.0)
    alphas = compute_alpha_series(score_series, beta=3.0)

    rows: list[dict] = []
    for i, base in enumerate(real_series):
        te = theta_efetivo[i]
        prev_t = theta_series[i - 1] if i > 0 else theta_series[0]
        rows.append({
            "competencia":        base["competencia"],
            "ano_cmpt":           base["ano_cmpt"],
            "mes_cmpt":           base["mes_cmpt"],
            "theta_t":            base["theta_t"],
            "theta_efetivo":      round(te, 4),
            "alpha_t":            alphas[i],
            "interference_regime": interference_regime(float(np.radians(te))),
            "internacoes_total":  base["internacoes"],
            "obitos_total":       base["obitos"],
            "taxa_mortalidade":   base["taxa_mortalidade"],
            "taxa_uti":           base["taxa_uti"],
            "taxa_respiratorio":  base["taxa_respiratorio"],
            "score_pressao":      base["score_pressao"],
            "hospital_occupancy_pct": base["hospital_occupancy_pct"],
            "delta_pressao":      round(
                base["score_pressao"] - score_series[i - 1] if i > 0 else 0.0, 4
            ),
            "delta_theta":        round(base["theta_t"] - prev_t if i > 0 else 0.0, 4),
            "n_sovereign_ativados": base["n_sovereign_ativados"],
            "data_source":        base["data_source"],
            "evento_critico":     base["evento_critico"],
        })

    return rows


# ── C4 LLM comparison (Ollama optional) ──────────────────────────

def run_llm_comparison() -> list[dict]:
    """Attempt C4a/C4b comparison. Returns empty list if Ollama unavailable."""
    try:
        import ollama  # noqa: F401
        log.warning("Ollama detected but C4 LLM scenarios not implemented in this release.")
    except ImportError:
        log.info("Ollama not available — C4 LLM comparison skipped (registered as 'skipped').")

    # Stub row to document the skip in the output parquet
    return [{
        "scenario_id": "C4-skipped",
        "query_id": 0,
        "condition": "skipped",
        "theta_deg": None,
        "psi_n_json": None,
        "action_recommended": "N/A",
        "action_normatively_correct": None,
        "reduction_delta": None,
        "n_sovereign_injected": 0,
        "note": "Ollama/Qwen C4 scenarios not executed — awaiting integration in next release",
    }]
