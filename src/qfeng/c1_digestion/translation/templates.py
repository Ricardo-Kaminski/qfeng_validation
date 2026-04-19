"""E3 — Clingo rule templates and condition translation."""
from __future__ import annotations

from qfeng.core.schemas import DeonticCondition, DeonticModality

_PREDICATE_NAME: dict[DeonticModality, str] = {
    DeonticModality.OBLIGATION:  "obligated",
    DeonticModality.PROHIBITION: "prohibited",
    DeonticModality.PERMISSION:  "permitted",
    DeonticModality.FACULTY:     "permitted",
}


def _normalize(s: str) -> str:
    """Normalize string to Clingo-safe snake_case atom."""
    return s.lower().replace("-", "_").replace(" ", "_")


def modality_to_predicate_name(modality: DeonticModality) -> str:
    return _PREDICATE_NAME[modality]


def condition_to_clingo(cond: DeonticCondition, idx: int) -> str:
    raise NotImplementedError


def build_rule(
    name: str,
    agent: str,
    patient: str,
    action: str,
    conditions: list[str],
) -> str:
    raise NotImplementedError
