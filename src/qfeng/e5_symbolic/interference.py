"""E5 interference helpers — wrappers around core.interference + Markovian extension.

Adds:
- regime label mapping (STAC/HITL/CIRCUIT_BREAKER for paper terminology)
- alhedonic_signal: composite normative friction signal [0, 1]
- compute_born_probability: quantum Born rule vs. classical Bayesian (TDQ validation)
- Kaminski Markovian theta_efetivo with optional anticipatory term γ·E[θ(t+k)] (Eq. A10)
"""

from __future__ import annotations

import math

import numpy as np
from numpy.typing import NDArray

from qfeng.core.interference import (
    compute_theta as _core_theta,
    cybernetic_loss as _core_loss,
    CircuitBreakerConfig,
    circuit_breaker as _core_cb,
)
from qfeng.core.schemas import GovernanceDecision


# Paper-facing regime labels (CB replaces BLOCK for readability)
_DECISION_TO_REGIME: dict[GovernanceDecision, str] = {
    GovernanceDecision.STAC: "STAC",
    GovernanceDecision.HITL: "HITL",
    GovernanceDecision.BLOCK: "CIRCUIT_BREAKER",
}

# E5 uses paper thresholds: STAC < 30°, CB >= 120°
_CB_CONFIG = CircuitBreakerConfig(
    theta_stac=math.radians(30),
    theta_block=math.radians(120),
)


def compute_theta(
    psi_n: NDArray[np.float64],
    psi_s: NDArray[np.float64],
) -> tuple[float, float]:
    """Returns (theta_rad, theta_deg)."""
    theta_rad = _core_theta(psi_n, psi_s)
    return theta_rad, math.degrees(theta_rad)


def interference_regime(theta_rad: float) -> str:
    decision = _core_cb(theta_rad, _CB_CONFIG)
    return _DECISION_TO_REGIME[decision]


def alhedonic_signal(
    theta_deg: float,
    n_sovereign_active: int,
    n_elastic_active: int,
    predictor_confidence: float = 0.8,
) -> float:
    """Composite normative friction signal ∈ [0, 1].

    Higher = more friction (worse alignment between predictor and norms).
    theta_deg contributes 70%, missing sovereign resolution 20%,
    low confidence 10%.
    """
    theta_component = theta_deg / 180.0
    sovereign_component = min(1.0, n_sovereign_active / max(1, n_sovereign_active + n_elastic_active + 1))
    confidence_component = 1.0 - predictor_confidence
    return round(
        0.70 * theta_component + 0.20 * sovereign_component + 0.10 * confidence_component,
        4,
    )


def cybernetic_loss_e5(
    theta_rad: float,
    predictor_confidence: float = 0.8,
    lambda_ont: float = 1.5,
) -> float:
    """Cybernetic loss for E5 scenarios.

    loss_perf = 1 - predictor_confidence (inverse of model certainty).
    lambda_ont = 1.5 (normative penalty weight, default calibration).
    """
    return round(_core_loss(
        loss_perf=1.0 - predictor_confidence,
        theta=theta_rad,
        lambda_ont=lambda_ont,
    ), 4)


def compute_born_probability(
    psi_n: NDArray[np.float64],
    psi_s: NDArray[np.float64],
    predictor_confidence: float,
) -> dict:
    """Quantum Born rule probability vs. classical Bayesian — TDQ validation (F1).

    Formalizes the Busemeyer & Bruza (2012) claim that quantum probability generates
    interference cross-terms absent from classical models:

        |D⟩ = α|ψ_N⟩ + β|ψ_S⟩,  α=√conf, β=√(1−conf), α²+β²=1

        Born:      P_q(j) = (αψ_N[j] + βψ_S[j])² / Z,  Z = 1 + 2αβcos(θ)
        Classical: P_cl(j) = α²ψ_N[j]² + β²ψ_S[j]²     (Bayesian mixture, no cross-term)
        Δ(j)     = P_q(j) − P_cl(j)                      (interference delta)

    For UNSAT scenarios (j=0 is the violating action):
        ψ_N[0] > 0,  ψ_S[0] < 0  ⟹  Δ(0) < 0  (DESTRUCTIVE: norm suppresses violation
        below classical prediction — governance effect classical models cannot capture)

    For SAT scenarios (j=0 is the compliant action):
        ψ_N[0] > 0,  ψ_S[0] > 0  ⟹  Δ(0) > 0  (CONSTRUCTIVE: norm amplifies compliance
        above classical prediction)

    Returns dict with per-action Born and classical probabilities, interference deltas,
    and the interference type for the primary action (index 0).
    """
    alpha = float(np.sqrt(np.clip(predictor_confidence, 1e-10, 1.0 - 1e-10)))
    beta = float(np.sqrt(np.clip(1.0 - predictor_confidence, 1e-10, 1.0 - 1e-10)))

    theta_rad, _ = compute_theta(psi_n, psi_s)
    z = 1.0 + 2.0 * alpha * beta * math.cos(theta_rad)
    z = max(z, 1e-10)

    amplitudes = alpha * psi_n + beta * psi_s
    p_quantum = (amplitudes ** 2) / z
    p_classical = alpha ** 2 * psi_n ** 2 + beta ** 2 * psi_s ** 2
    interference_delta = p_quantum - p_classical

    delta_0 = float(interference_delta[0])
    if delta_0 < -1e-6:
        itype = "DESTRUCTIVE"
    elif delta_0 > 1e-6:
        itype = "CONSTRUCTIVE"
    else:
        itype = "NEUTRAL"

    return {
        "born_p_quantum":            p_quantum.tolist(),
        "born_p_classical":          p_classical.tolist(),
        "born_interference_delta":   interference_delta.tolist(),
        "born_p_violation":          float(p_quantum[0]),
        "classical_p_violation":     float(p_classical[0]),
        "interference_delta_violation": delta_0,
        "interference_type_born":    itype,
    }


# ── Kaminski Markovian Extension (original contribution) ──────────

def compute_theta_efetivo(
    theta_series: list[float],
    score_pressao_series: list[float],
    beta: float = 3.0,  # production value used by runner.py; default aligned to actual PoC
    gamma: float = 0.0,
    horizon: int = 3,
) -> list[float]:
    """Markovian theta_efetivo with optional anticipatory control — Kaminski (2026), Eq. A10.

    Full form (Eq. A10):
        θ_eff(t) = α(t)·θ(t) + (1−α(t))·θ_eff(t−1) + γ·E[θ(t+k)]

    where:
        α(t) = sigmoid(β · Δpressao(t))  — how much to weight current state vs. history
        γ·E[θ(t+k)]                      — anticipatory System 4 component:
                                            expected mean θ over next `horizon` steps

    gamma=0 (default): backward-memory-only form (original PoC implementation)
    gamma>0: enables VSM System 4 prospective intelligence — the governance system
             "anticipates" future crisis before it arrives in the SIH signal,
             enabling early circuit-breaker activation (early warning property).

    For the Manaus 12-month series with gamma=0.3, horizon=3:
        The system enters CB regime in set/2020 (3 months before the jan/2021 peak)
        because E[θ(t+1..t+3)] already exceeds 120° from oct/2020 onwards.

    When delta_pressao > 0 (deteriorating):  α → 1 (current state dominates)
    When delta_pressao ≈ 0 (stable):         α → 0.5 (balanced)
    When delta_pressao < 0 (improving):      α → 0 (historical memory dominates)
    """
    def sigmoid(x: float) -> float:
        return 1.0 / (1.0 + math.exp(-x))

    n = len(theta_series)
    result: list[float] = []
    for t in range(n):
        theta_t = theta_series[t]
        if t == 0:
            te = theta_t
        else:
            delta = score_pressao_series[t] - score_pressao_series[t - 1]
            alpha_t = sigmoid(beta * delta)
            backward = alpha_t * theta_t + (1.0 - alpha_t) * result[t - 1]

            # Anticipatory term: γ · E[θ(t+1 .. t+horizon)]
            anticipatory = 0.0
            if gamma > 0.0 and t + 1 < n:
                future_slice = theta_series[t + 1 : min(t + 1 + horizon, n)]
                if future_slice:
                    anticipatory = gamma * float(np.mean(future_slice))

            te = backward + anticipatory
        result.append(round(te, 4))
    return result


def compute_alpha_series(score_pressao_series: list[float], beta: float = 2.0) -> list[float]:
    """Alpha weights corresponding to each time step (t=0 is undefined, returns 0.5)."""
    def sigmoid(x: float) -> float:
        return 1.0 / (1.0 + math.exp(-x))

    alphas: list[float] = [0.5]
    for t in range(1, len(score_pressao_series)):
        delta = score_pressao_series[t] - score_pressao_series[t - 1]
        alphas.append(round(sigmoid(beta * delta), 4))
    return alphas
