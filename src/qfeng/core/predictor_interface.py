"""Predictor interface ABC — contrato para todos os predictors Q-FENG."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class PredictionContext:
    """Contexto de entrada para qualquer predictor."""
    scenario_id: str
    regime: str
    timestamp: str
    input_data: dict[str, Any]
    active_predicates: list[str]
    system_prompt: str = ""
    extra_data: dict[str, Any] = field(default_factory=dict)


@dataclass
class PredictionResult:
    """Resultado de qualquer predictor — |psi_N>."""
    psi_n: np.ndarray
    decision_space: list[str]
    raw_output: Any
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)


class PredictorInterface(ABC):
    """Interface agnostica ao modelo preditivo."""

    @abstractmethod
    def predict(self, context: PredictionContext) -> PredictionResult:
        ...

    @abstractmethod
    def get_decision_space(self) -> list[str]:
        ...

    @abstractmethod
    def is_available(self) -> bool:
        ...

    def align_with_predicates(
        self,
        result: PredictionResult,
        active_predicates: list[str],
        predicate_weights: dict[str, float] | None = None,
    ) -> np.ndarray:
        n = len(result.psi_n)
        psi_s = np.zeros(n, dtype=np.float64)
        weights = predicate_weights or {p: 1.0 for p in active_predicates}
        decision_space = self.get_decision_space()
        for pred, weight in weights.items():
            for i, label in enumerate(decision_space):
                if any(kw in label for kw in pred.split("_")):
                    psi_s[i] += weight
        norm = np.linalg.norm(psi_s)
        if norm > 0:
            psi_s = psi_s / norm
        return psi_s


def l2_normalize(v: np.ndarray) -> np.ndarray:
    v = np.array(v, dtype=np.float64)
    norm = np.linalg.norm(v)
    if norm == 0.0:
        return np.ones(len(v), dtype=np.float64) / len(v)
    return v / norm
