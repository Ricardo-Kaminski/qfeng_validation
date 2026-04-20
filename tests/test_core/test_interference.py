"""Tests for Q-FENG core interference engine."""

from __future__ import annotations

import math

import numpy as np
import pytest

from qfeng.core.interference import (
    CircuitBreakerConfig,
    born_rule,
    circuit_breaker,
    compute_interference,
    compute_theta,
    cybernetic_loss,
    normalize,
    quantum_penalty,
    theta_eff,
)
from qfeng.core.schemas import GovernanceDecision


# ── normalize ──────────────────────────────────────────────────────

class TestNormalize:
    def test_unit_vector_unchanged(self) -> None:
        v = np.array([1.0, 0.0, 0.0])
        result = normalize(v)
        np.testing.assert_array_almost_equal(result, v)

    def test_scales_to_unit_norm(self) -> None:
        v = np.array([3.0, 4.0])
        result = normalize(v)
        assert abs(np.linalg.norm(result) - 1.0) < 1e-10

    def test_zero_vector_returns_zero(self) -> None:
        v = np.array([0.0, 0.0, 0.0])
        result = normalize(v)
        np.testing.assert_array_equal(result, v)


# ── compute_theta ──────────────────────────────────────────────────

class TestComputeTheta:
    def test_identical_vectors_theta_zero(self) -> None:
        """Constructive interference: aligned vectors → θ ≈ 0."""
        v = np.array([1.0, 0.0, 0.0])
        theta = compute_theta(v, v)
        assert abs(theta) < 1e-10

    def test_orthogonal_vectors_theta_pi_half(self) -> None:
        """Neutral: orthogonal vectors → θ = π/2."""
        v1 = np.array([1.0, 0.0])
        v2 = np.array([0.0, 1.0])
        theta = compute_theta(v1, v2)
        assert abs(theta - math.pi / 2) < 1e-10

    def test_opposite_vectors_theta_pi(self) -> None:
        """Destructive interference: anti-aligned → θ ≈ π."""
        v1 = np.array([1.0, 0.0])
        v2 = np.array([-1.0, 0.0])
        theta = compute_theta(v1, v2)
        assert abs(theta - math.pi) < 1e-10

    def test_theta_range_always_0_to_pi(self) -> None:
        """θ is always in [0, π] regardless of input."""
        rng = np.random.default_rng(42)
        for _ in range(100):
            v1 = rng.standard_normal(10)
            v2 = rng.standard_normal(10)
            theta = compute_theta(v1, v2)
            assert 0.0 <= theta <= math.pi + 1e-10

    def test_unnormalized_vectors_still_work(self) -> None:
        """Vectors are normalized internally."""
        v1 = np.array([100.0, 0.0])
        v2 = np.array([0.0, 0.001])
        theta = compute_theta(v1, v2)
        assert abs(theta - math.pi / 2) < 1e-10


# ── born_rule ──────────────────────────────────────────────────────

class TestBornRule:
    def test_constructive_amplifies(self) -> None:
        """θ=0, equal weights → P = 0.5 + 0.5 + 2*0.5 = 2.0."""
        p = born_rule(0.5, 0.5, 0.0)
        assert abs(p - 2.0) < 1e-10

    def test_destructive_suppresses(self) -> None:
        """θ=π, equal weights → P = 0.5 + 0.5 - 2*0.5 = 0.0."""
        p = born_rule(0.5, 0.5, math.pi)
        assert abs(p) < 1e-10

    def test_orthogonal_no_interference(self) -> None:
        """θ=π/2, cos=0 → P = |α|² + |β|² (no interference term)."""
        p = born_rule(0.5, 0.5, math.pi / 2)
        assert abs(p - 1.0) < 1e-10

    def test_never_negative(self) -> None:
        """P(Action) is clamped to ≥ 0."""
        p = born_rule(0.1, 0.1, math.pi)
        assert p >= 0.0

    def test_asymmetric_weights(self) -> None:
        """When α dominates, P is less affected by destructive interference."""
        p = born_rule(0.9, 0.1, math.pi)
        # 0.9 + 0.1 - 2*sqrt(0.9)*sqrt(0.1) = 1.0 - 0.6 = 0.4
        assert p > 0.0


# ── quantum_penalty ────────────────────────────────────────────────

class TestQuantumPenalty:
    def test_zero_when_constructive(self) -> None:
        assert quantum_penalty(0.0) == 0.0

    def test_zero_at_orthogonal(self) -> None:
        assert abs(quantum_penalty(math.pi / 2)) < 1e-10

    def test_max_at_pi(self) -> None:
        assert abs(quantum_penalty(math.pi) - 1.0) < 1e-10

    def test_activates_past_pi_half(self) -> None:
        """Penalty activates only when cos(θ) < 0, i.e. θ > π/2."""
        assert quantum_penalty(math.pi / 3) == 0.0  # 60°, cos > 0
        assert quantum_penalty(2 * math.pi / 3) > 0.0  # 120°, cos < 0


# ── cybernetic_loss ────────────────────────────────────────────────

class TestCyberneticLoss:
    def test_no_penalty_when_aligned(self) -> None:
        loss = cybernetic_loss(loss_perf=0.5, theta=0.0, lambda_ont=10.0)
        assert abs(loss - 0.5) < 1e-10

    def test_penalty_adds_when_destructive(self) -> None:
        loss = cybernetic_loss(loss_perf=0.5, theta=math.pi, lambda_ont=1.0)
        assert abs(loss - 1.5) < 1e-10  # 0.5 + 1.0 * 1.0

    def test_lambda_scales_penalty(self) -> None:
        loss_low = cybernetic_loss(loss_perf=0.0, theta=math.pi, lambda_ont=1.0)
        loss_high = cybernetic_loss(loss_perf=0.0, theta=math.pi, lambda_ont=10.0)
        assert abs(loss_high / loss_low - 10.0) < 1e-10

    def test_fairness_term(self) -> None:
        loss = cybernetic_loss(
            loss_perf=0.1, theta=0.0, lambda_ont=1.0,
            loss_fairness=0.3, lambda_fair=2.0,
        )
        assert abs(loss - 0.7) < 1e-10  # 0.1 + 0 + 2.0*0.3


# ── circuit_breaker ────────────────────────────────────────────────
