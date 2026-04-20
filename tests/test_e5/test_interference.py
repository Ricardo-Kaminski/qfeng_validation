"""Unit tests for E5 interference module."""

import math

import numpy as np
import pytest

from qfeng.e5_symbolic.interference import (
    alhedonic_signal,
    compute_alpha_series,
    compute_theta,
    compute_theta_efetivo,
    cybernetic_loss_e5,
    interference_regime,
)


class TestComputeTheta:
    def test_aligned_vectors_give_zero_theta(self):
        psi_n = np.array([1.0, 0.0, 0.0])
        psi_s = np.array([1.0, 0.0, 0.0])
        theta_rad, theta_deg = compute_theta(psi_n, psi_s)
        assert theta_deg == pytest.approx(0.0, abs=0.01)

    def test_antiparallel_vectors_give_180(self):
        psi_n = np.array([1.0, 0.0, 0.0])
        psi_s = np.array([-1.0, 0.0, 0.0])
        _, theta_deg = compute_theta(psi_n, psi_s)
        assert theta_deg == pytest.approx(180.0, abs=0.01)

    def test_orthogonal_vectors_give_90(self):
        psi_n = np.array([1.0, 0.0])
        psi_s = np.array([0.0, 1.0])
        _, theta_deg = compute_theta(psi_n, psi_s)
        assert theta_deg == pytest.approx(90.0, abs=0.01)

    def test_theta_rad_and_deg_consistent(self):
        psi_n = np.array([0.8, 0.6])
        psi_s = np.array([0.6, 0.8])
        theta_rad, theta_deg = compute_theta(psi_n, psi_s)
        assert math.degrees(theta_rad) == pytest.approx(theta_deg, abs=0.001)


class TestInterferenceRegime:
    def test_stac_below_30(self):
        assert interference_regime(math.radians(5.0)) == "STAC"
        assert interference_regime(math.radians(29.9)) == "STAC"

    def test_hitl_between_30_and_120(self):
        assert interference_regime(math.radians(30.0)) == "HITL"
        assert interference_regime(math.radians(90.0)) == "HITL"
        assert interference_regime(math.radians(119.9)) == "HITL"

    def test_circuit_breaker_above_120(self):
        assert interference_regime(math.radians(120.0)) == "CIRCUIT_BREAKER"
        assert interference_regime(math.radians(135.0)) == "CIRCUIT_BREAKER"
        assert interference_regime(math.radians(175.0)) == "CIRCUIT_BREAKER"


class TestAlhedonicSignal:
    def test_returns_float_in_range(self):
        val = alhedonic_signal(90.0, 5, 3, 0.8)
        assert 0.0 <= val <= 1.0

    def test_higher_theta_gives_higher_signal(self):
        low = alhedonic_signal(10.0, 3, 2, 0.9)
        high = alhedonic_signal(150.0, 3, 2, 0.9)
        assert high > low

    def test_zero_theta_gives_low_signal(self):
        val = alhedonic_signal(0.0, 0, 0, 1.0)
        assert val < 0.15


class TestThetaEfetivo:
    def test_t0_returns_initial_theta(self):
        result = compute_theta_efetivo([45.0], [0.5])
        assert result[0] == pytest.approx(45.0)

    def test_increasing_pressure_raises_alpha(self):
        alphas = compute_alpha_series([0.1, 0.5, 0.9], beta=2.0)
        assert alphas[1] > 0.5  # delta positive → alpha > 0.5
        assert alphas[2] > 0.5

    def test_decreasing_pressure_lowers_alpha(self):
        alphas = compute_alpha_series([0.9, 0.5, 0.1], beta=2.0)
        assert alphas[1] < 0.5
        assert alphas[2] < 0.5

    def test_manaus_series_reaches_cb_jan2021(self):
        """Markovian extension with beta=3.0 reaches Circuit Breaker at jan/2021."""
        theta_series = [23.5, 47.2, 88.7, 138.4, 91.3, 62.1]
        score_series = [0.14, 0.26, 0.51, 0.91, 0.72, 0.41]
        result = compute_theta_efetivo(theta_series, score_series, beta=3.0)
        # jan/2021 (index 3) must exceed 120° (Circuit Breaker threshold)
        assert result[3] > 120.0
        # out/2020 (index 0) must be in STAC range
        assert result[0] < 30.0

    def test_memory_effect_stays_elevated_after_peak(self):
        """theta_efetivo remains elevated after crisis even as theta drops."""
        theta_series = [23.5, 47.2, 88.7, 138.4, 91.3, 62.1]
        score_series = [0.14, 0.26, 0.51, 0.91, 0.72, 0.41]
        result = compute_theta_efetivo(theta_series, score_series, beta=3.0)
        # fev/2021: theta_t=91.3 but theta_efetivo should be > 100° (memory)
        assert result[4] > 100.0
        # theta_efetivo[4] > theta_t[4] confirms memory holds
        assert result[4] > theta_series[4]


class TestCyberneticLoss:
    def test_zero_theta_gives_low_loss(self):
        loss = cybernetic_loss_e5(0.0, predictor_confidence=0.95)
        assert loss < 0.15

    def test_pi_theta_gives_high_loss(self):
        loss = cybernetic_loss_e5(math.pi, predictor_confidence=0.8)
        assert loss > 1.0

    def test_low_confidence_increases_loss(self):
        high_conf = cybernetic_loss_e5(math.radians(90), predictor_confidence=0.95)
        low_conf = cybernetic_loss_e5(math.radians(90), predictor_confidence=0.30)
        assert low_conf > high_conf
