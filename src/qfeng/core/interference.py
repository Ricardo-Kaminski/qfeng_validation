"""Q-FENG Interference Engine — Core Mathematical Module.

Implements the Quantum Decision Theory formalism from Kaminski (2026):
- Born Rule with interference term (Eq. 2)
- Ontological Friction angle θ (Eq. 1)
- Cybernetic Loss Function with Quantum Penalty (Eq. 3)
- Markovian extension θ_eff (Eq. A10)
- Circuit Breaker decision logic

This module is DOMAIN-AGNOSTIC. It operates on normalized vectors
and produces governance decisions. It does not know whether it is
governing a health system, a market simulation, or a multi-agent
population. That separation is by design.

References:
    Kaminski, R.S. (2026). Q-FENG: Quantum-Fractal Neurosymbolic
    Governance. Working Paper. arXiv [cs.AI].

    Busemeyer, J.R. & Bruza, P.D. (2012). Quantum Models of
    Cognition and Decision. Cambridge University Press.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray

from .schemas import GovernanceDecision, InterferenceResult


# ── Constants ──────────────────────────────────────────────────────

_EPSILON = 1e-10  # Numerical stability floor


# ── Vector Operations ──────────────────────────────────────────────


def normalize(v: NDArray[np.float64]) -> NDArray[np.float64]:
    """L2-normalize a vector. Returns zero vector if norm < epsilon."""
    norm = np.linalg.norm(v)
    if norm < _EPSILON:
        return np.zeros_like(v)
    return v / norm


def compute_theta(psi_n: NDArray[np.float64], psi_s: NDArray[np.float64]) -> float:
    """Compute Ontological Friction angle θ = arccos(⟨ψ_N|ψ_S⟩).

    Args:
        psi_n: Neural Evidence Vector (normalized).
        psi_s: Symbolic Norm Vector (normalized).

    Returns:
        θ in radians ∈ [0, π].
    """
    psi_n = normalize(psi_n)
    psi_s = normalize(psi_s)
    dot = float(np.dot(psi_n, psi_s))
    # Clamp to [-1, 1] for numerical safety
    dot = max(-1.0, min(1.0, dot))
    return math.acos(dot)


# ── Born Rule with Interference ────────────────────────────────────


def born_rule(
    alpha_sq: float,
    beta_sq: float,
    theta: float,
) -> float:
    """Compute P(Action) via the Born Rule with interference term.

    P(Action) = |α|² + |β|² + 2|α||β|cos(θ)    (Eq. 2)

    Args:
        alpha_sq: |α|² — weight of neural evidence component.
        beta_sq: |β|² — weight of normative strength component.
        theta: Ontological Friction angle in radians.

    Returns:
        P(Action) ∈ [0, 2]. Values > 1 indicate constructive
        interference (amplification). Values near 0 indicate
        destructive interference (suppression).
    """
    interference_term = 2.0 * math.sqrt(alpha_sq) * math.sqrt(beta_sq) * math.cos(theta)
    p_action = alpha_sq + beta_sq + interference_term
    return max(0.0, p_action)


# ── Quantum Penalty (Loss Component) ──────────────────────────────


def quantum_penalty(theta: float) -> float:
    """Compute the Quantum Penalty term for the Cybernetic Loss Function.

    QP = max(0, −cos(θ))    (from Eq. 3)

    Activates ONLY when cos(θ) < 0 (destructive interference).
    Returns 0 when vectors are aligned (constructive interference).
    Returns up to 1.0 when θ ≈ π (maximum destructive interference).

    Args:
        theta: Ontological Friction angle in radians.

    Returns:
        Penalty value ∈ [0, 1].
    """
    return max(0.0, -math.cos(theta))


def cybernetic_loss(
    loss_perf: float,
    theta: float,
    lambda_ont: float,
    loss_fairness: float = 0.0,
    lambda_fair: float = 0.0,
) -> float:
    """Compute the full Cybernetic Loss Function.

    ℒ_Global = ℒ_Perf + λ_ont · max(0, −cos(θ)) + λ_fair · FairnessLoss
    (Eq. 3 / Eq. 6)

    Args:
        loss_perf: Task-specific performance loss.
        theta: Ontological Friction angle in radians.
        lambda_ont: Weight of ontological penalty (higher = stricter norms).
        loss_fairness: Optional fairness loss component.
        lambda_fair: Weight of fairness penalty.

    Returns:
        Total cybernetic loss value.
    """
    qp = quantum_penalty(theta)
    return loss_perf + lambda_ont * qp + lambda_fair * loss_fairness


# ── Markovian Extension: θ_eff ─────────────────────────────────────


def theta_eff(
    theta_history: list[float],
    decay_weights: list[float] | None = None,
    gamma: float = 0.0,
    theta_forecast: list[float] | None = None,
) -> float:
    """Compute the effective Ontological Friction with temporal extension.

    θ_eff(t) = Σᵢ wᵢ · θ(t−i) + γ · E[θ(t+k)]    (Eq. A10)

    First term: path dependence (historically accumulated friction).
    Second term: anticipatory governance (expected future friction).

    Args:
        theta_history: Past θ values, most recent first. [θ(t), θ(t-1), ...].
        decay_weights: Weights for past values. If None, uses exponential
            decay w_i = exp(-0.3 * i) — recent friction weighs more.
        gamma: Discount factor for future friction ∈ [0, 1].
            0 = purely reactive, 1 = maximally anticipatory.
        theta_forecast: Expected future θ values [E[θ(t+1)], E[θ(t+2)], ...].
            Typically from Monte Carlo simulation.

    Returns:
        θ_eff in radians.
    """
    if not theta_history:
        return 0.0

    # Path dependence component
    n = len(theta_history)
    if decay_weights is None:
        decay_weights = [math.exp(-0.3 * i) for i in range(n)]

    # Normalize weights
    w_sum = sum(decay_weights[:n])
    if w_sum < _EPSILON:
        return theta_history[0] if theta_history else 0.0

    path_component = sum(
        w * th for w, th in zip(decay_weights[:n], theta_history)
    ) / w_sum

    # Anticipatory component
    anticipatory_component = 0.0
    if gamma > 0 and theta_forecast:
        anticipatory_component = gamma * (sum(theta_forecast) / len(theta_forecast))

    return path_component + anticipatory_component


# ── Circuit Breaker ────────────────────────────────────────────────


@dataclass
class CircuitBreakerConfig:
    """Configuration for the Circuit Breaker decision thresholds.

    Thresholds define the governance spectrum:
        θ < theta_stac      → STAC (autonomous execution)
        theta_stac ≤ θ < theta_block → HITL (human escalation)
        θ ≥ theta_block      → BLOCK (action suppressed)

    Default values correspond to:
        STAC:  θ < 60° (cos > 0.5, strong alignment)
        HITL:  60° ≤ θ < 120° (graduated friction)
        BLOCK: θ ≥ 120° (cos < -0.5, destructive interference)
    """
    theta_stac: float = math.pi / 3        # 60° — below this: autonomous
    theta_block: float = 2 * math.pi / 3   # 120° — above this: blocked


def circuit_breaker(
    theta: float,
    config: CircuitBreakerConfig | None = None,
) -> GovernanceDecision:
    """Evaluate the Circuit Breaker decision based on θ.

    Maps the continuous θ spectrum to discrete governance actions.

    Args:
        theta: Ontological Friction angle in radians.
        config: Threshold configuration. Uses defaults if None.

    Returns:
        GovernanceDecision: STAC, HITL, or BLOCK.
    """
    if config is None:
        config = CircuitBreakerConfig()

    if theta < config.theta_stac:
        return GovernanceDecision.STAC
    elif theta < config.theta_block:
        return GovernanceDecision.HITL
    else:
        return GovernanceDecision.BLOCK


# ── Full Interference Computation ──────────────────────────────────


def compute_interference(
    psi_n: NDArray[np.float64],
    psi_s: NDArray[np.float64],
    alpha_sq: float = 0.5,
    beta_sq: float = 0.5,
    cb_config: CircuitBreakerConfig | None = None,
    theta_history: list[float] | None = None,
    gamma: float = 0.0,
    theta_forecast: list[float] | None = None,
    diagnosis_labels: list[str] | None = None,
) -> InterferenceResult:
    """Compute the full Q-FENG interference analysis.

    This is the primary entry point for governance computation.
    Takes neural and normative vectors, computes θ, evaluates
    the Born Rule, runs the Circuit Breaker, and returns a
    complete InterferenceResult.

    Args:
        psi_n: Neural Evidence Vector (will be L2-normalized).
        psi_s: Symbolic Norm Vector (will be L2-normalized).
        alpha_sq: |α|² — model confidence weight. Default 0.5.
        beta_sq: |β|² — normative strength weight. Default 0.5.
        cb_config: Circuit Breaker thresholds.
        theta_history: Past θ values for Markovian extension.
        gamma: Discount for anticipated future friction.
        theta_forecast: Expected future θ values.
        diagnosis_labels: Labels for normative dimensions that were
            tensioned (populated by the caller from dPASP predicates).

    Returns:
        InterferenceResult with all computed values and governance decision.
    """
    theta = compute_theta(psi_n, psi_s)
    cos_theta = math.cos(theta)
    interference_term = 2.0 * math.sqrt(alpha_sq) * math.sqrt(beta_sq) * cos_theta
    p_action = born_rule(alpha_sq, beta_sq, theta)
    decision = circuit_breaker(theta, cb_config)

    # Markovian extension
    t_eff: float | None = None
    if theta_history is not None:
        full_history = [theta] + theta_history
        t_eff = theta_eff(full_history, gamma=gamma, theta_forecast=theta_forecast)

    return InterferenceResult(
        theta=theta,
        theta_degrees=math.degrees(theta),
        cos_theta=cos_theta,
        p_action=p_action,
        alpha_sq=alpha_sq,
        beta_sq=beta_sq,
        interference_term=interference_term,
        decision=decision,
        diagnosis=diagnosis_labels or [],
        theta_eff=t_eff,
    )
