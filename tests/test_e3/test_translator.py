"""Unit tests for E3 translator — atom_to_predicate."""
from __future__ import annotations

import pytest

from qfeng.c1_digestion.translation.templates import (
    _normalize,
    build_rule,
    condition_to_clingo,
    modality_to_predicate_name,
)
from qfeng.c1_digestion.translation.translator import atom_to_predicate, validate_syntax
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


class TestValidateSyntax:
    def test_valid_fact(self) -> None:
        assert validate_syntax("obligated(state, citizen, provide_healthcare).") is True

    def test_valid_rule_with_body(self) -> None:
        rule = "permitted(a, b, c) :-\n    use_cases(high_risk)."
        assert validate_syntax(rule) is True

    def test_invalid_syntax(self) -> None:
        assert validate_syntax("obligated(state, UNCLOSED") is False


class TestAtomToPredicate:
    def _make_atom(
        self,
        *,
        modality: DeonticModality = DeonticModality.OBLIGATION,
        agent: str = "state",
        patient: str = "citizen",
        action: str = "provide_healthcare",
        conditions: list[DeonticCondition] | None = None,
        strength: NormativeStrength = NormativeStrength.STATUTORY,
        atom_id: str = "abc123",
        chunk_id: str = "chunk456",
    ) -> DeonticAtom:
        return DeonticAtom(
            id=atom_id,
            source_chunk_id=chunk_id,
            modality=modality,
            agent=agent,
            patient=patient,
            action=action,
            conditions=conditions or [],
            strength=strength,
            confidence=0.9,
        )

    def test_obligation_no_conditions(self) -> None:
        atom = self._make_atom()
        pred = atom_to_predicate(atom)
        assert "obligated(state, citizen, provide_healthcare)." in pred.rule

    def test_obligation_with_gt_condition(self) -> None:
        atom = self._make_atom(
            conditions=[DeonticCondition(variable="count", operator=">", value="0")]
        )
        pred = atom_to_predicate(atom)
        assert "obligated(state, citizen, provide_healthcare) :-" in pred.rule
        assert "count(X_0), X_0 > 0" in pred.rule

    def test_faculty_maps_to_permitted(self) -> None:
        atom = self._make_atom(modality=DeonticModality.FACULTY)
        pred = atom_to_predicate(atom)
        assert "permitted(" in pred.rule

    def test_permission_with_eq_string_condition(self) -> None:
        atom = self._make_atom(
            modality=DeonticModality.PERMISSION,
            conditions=[DeonticCondition(variable="use_cases", operator="==",
                                         value="high_risk_ai_systems")],
        )
        pred = atom_to_predicate(atom)
        assert "permitted(" in pred.rule
        assert "use_cases(high_risk_ai_systems)" in pred.rule

    def test_prohibition(self) -> None:
        atom = self._make_atom(modality=DeonticModality.PROHIBITION)
        pred = atom_to_predicate(atom)
        assert "prohibited(" in pred.rule

    def test_patient_none_becomes_atom_none(self) -> None:
        atom = self._make_atom(patient="None")
        pred = atom_to_predicate(atom)
        assert ", none, " in pred.rule

    def test_multiple_conditions(self) -> None:
        atom = self._make_atom(conditions=[
            DeonticCondition(variable="rate", operator=">=", value="80"),
            DeonticCondition(variable="status", operator="==", value="active"),
        ])
        pred = atom_to_predicate(atom)
        assert "rate(X_0), X_0 >= 80" in pred.rule
        assert "status(active)" in pred.rule

    def test_traceability_comment_atom_id(self) -> None:
        atom = self._make_atom(atom_id="ea9646908e4d3ea2", chunk_id="003bd71d0f5d3a8c")
        pred = atom_to_predicate(atom)
        assert "% atom_id: ea9646908e4d3ea2" in pred.rule
        assert "chunk: 003bd71d0f5d3a8c" in pred.rule

    def test_strength_in_comment(self) -> None:
        atom = self._make_atom(strength=NormativeStrength.STATUTORY)
        pred = atom_to_predicate(atom)
        assert "strength: statutory" in pred.rule

    def test_syntax_valid_true_for_valid_atom(self) -> None:
        atom = self._make_atom()
        pred = atom_to_predicate(atom)
        assert pred.syntax_valid is True

    def test_source_atom_id_set(self) -> None:
        atom = self._make_atom(atom_id="myatom")
        pred = atom_to_predicate(atom)
        assert pred.source_atom_id == "myatom"
        assert pred.id == "myatom"

    def test_source_chunk_id_set(self) -> None:
        atom = self._make_atom(chunk_id="mychunk")
        pred = atom_to_predicate(atom)
        assert pred.source_chunk_id == "mychunk"
