"""Unit tests for E3 translator — atom_to_predicate."""
from __future__ import annotations

import pytest

from qfeng.c1_digestion.translation.templates import (
    _normalize,
    build_rule,
    condition_to_clingo,
    modality_to_predicate_name,
)
from qfeng.core.schemas import (
    DeonticAtom,
    DeonticCondition,
    DeonticModality,
    NormativeStrength,
)


class TestNormalize:
    def test_hyphen_to_underscore(self) -> None:
        assert _normalize("high-risk_ai_systems") == "high_risk_ai_systems"

    def test_space_to_underscore(self) -> None:
        assert _normalize("state agency") == "state_agency"

    def test_already_snake(self) -> None:
        assert _normalize("state_agency") == "state_agency"

    def test_lowercase(self) -> None:
        assert _normalize("Municipality") == "municipality"

    def test_mixed(self) -> None:
        assert _normalize("High-Risk AI") == "high_risk_ai"


class TestModalityToPredicateName:
    def test_obligation(self) -> None:
        assert modality_to_predicate_name(DeonticModality.OBLIGATION) == "obligated"

    def test_prohibition(self) -> None:
        assert modality_to_predicate_name(DeonticModality.PROHIBITION) == "prohibited"

    def test_permission(self) -> None:
        assert modality_to_predicate_name(DeonticModality.PERMISSION) == "permitted"

    def test_faculty(self) -> None:
        assert modality_to_predicate_name(DeonticModality.FACULTY) == "permitted"
