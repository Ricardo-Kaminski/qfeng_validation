"""Tests for Q-FENG core interference engine.

Validates the mathematical formalism from Kaminski (2026):
- Born Rule with interference (Eq. 2)
- θ computation and boundary conditions
- Circuit Breaker decision logic
- Cybernetic Loss Function (Eq. 3)
- Markovian extension θ_eff (Eq. A10)
"""

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
