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


class TestConditionToClingo:
    def test_eq_string_value(self) -> None:
        cond = DeonticCondition(variable="use_cases", operator="==", value="high_risk_ai_systems")
        assert condition_to_clingo(cond, 0) == "use_cases(high_risk_ai_systems)"

    def test_eq_string_normalizes_value(self) -> None:
        cond = DeonticCondition(variable="use_cases", operator="==", value="high-risk_ai_systems")
        assert condition_to_clingo(cond, 0) == "use_cases(high_risk_ai_systems)"

    def test_gt_numeric(self) -> None:
        cond = DeonticCondition(variable="inconsistent_submissions", operator=">", value="0")
        assert condition_to_clingo(cond, 0) == "inconsistent_submissions(X_0), X_0 > 0"

    def test_lt_numeric(self) -> None:
        cond = DeonticCondition(variable="rate", operator="<", value="80")
        assert condition_to_clingo(cond, 0) == "rate(X_0), X_0 < 80"

    def test_gte_numeric(self) -> None:
        cond = DeonticCondition(variable="coverage", operator=">=", value="138")
        assert condition_to_clingo(cond, 0) == "coverage(X_0), X_0 >= 138"

    def test_lte_numeric(self) -> None:
        cond = DeonticCondition(variable="bed_ratio", operator="<=", value="2")
        assert condition_to_clingo(cond, 0) == "bed_ratio(X_0), X_0 <= 2"

    def test_neq_numeric(self) -> None:
        cond = DeonticCondition(variable="inconsistencies", operator="!=", value="0")
        assert condition_to_clingo(cond, 0) == "inconsistencies(X_0), X_0 != 0"

    def test_variable_index_increments(self) -> None:
        cond = DeonticCondition(variable="count", operator=">", value="5")
        result_idx1 = condition_to_clingo(cond, 1)
        assert "X_1" in result_idx1

    def test_eq_numeric_value(self) -> None:
        cond = DeonticCondition(variable="count", operator="==", value="5")
        assert condition_to_clingo(cond, 0) == "count(5)"


class TestBuildRule:
    def test_fact_no_conditions(self) -> None:
        result = build_rule("obligated", "state", "citizen", "provide_healthcare", [])
        assert result == "obligated(state, citizen, provide_healthcare)."

    def test_rule_with_one_condition(self) -> None:
        result = build_rule(
            "permitted", "commission", "none", "adopt_acts",
            ["use_cases(high_risk_ai_systems)"],
        )
        assert result == (
            "permitted(commission, none, adopt_acts) :-\n"
            "    use_cases(high_risk_ai_systems)."
        )

    def test_rule_with_two_conditions(self) -> None:
        result = build_rule(
            "obligated", "state", "citizen", "pay",
            ["income(X_0), X_0 <= 138", "status(eligible)"],
        )
        assert result == (
            "obligated(state, citizen, pay) :-\n"
            "    income(X_0), X_0 <= 138,\n"
            "    status(eligible)."
        )

    def test_patient_none_atom(self) -> None:
        result = build_rule("permitted", "municipality", "none", "organize_districts", [])
        assert result == "permitted(municipality, none, organize_districts)."
