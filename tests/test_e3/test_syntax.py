"""Tests for E3 validate_syntax — clingo 5.8.0 parse-level validation."""
from qfeng.c1_digestion.translation.translator import validate_syntax


class TestValidateSyntaxStandalone:
    def test_valid_obligation_rule(self) -> None:
        rule = "obligated(state, citizen, provide_healthcare)."
        assert validate_syntax(rule) is True

    def test_invalid_syntax_unclosed_paren(self) -> None:
        rule = "obligated(state, citizen, provide_healthcare"
        assert validate_syntax(rule) is False

    def test_rule_with_free_clingo_variable(self) -> None:
        rule = "obligated(state, citizen, provide_info) :-\n    count(X_0), X_0 > 0."
        assert validate_syntax(rule) is True
