"""Integration tests for E5 scenario_loader — requires corpora_clingo files."""

import pytest

from qfeng.e5_symbolic.scenario_loader import SCENARIO_REGISTRY, run_scenario


@pytest.mark.parametrize("scenario_id,expected_sat", [
    ("C2", False),
    ("C3", False),
    ("C7", False),
    ("T-CLT-01", False),
    ("T-CLT-02", False),
    ("T-CLT-03", True),
])
def test_scenario_sat_unsat(scenario_id, expected_sat):
    """Full-program Clingo run must match expected SAT/UNSAT for each scenario."""
    result = run_scenario(scenario_id)
    assert result["satisfiable"] == expected_sat, (
        f"{scenario_id}: expected {'SAT' if expected_sat else 'UNSAT'}, "
        f"got {'SAT' if result['satisfiable'] else 'UNSAT'}"
    )


@pytest.mark.parametrize("scenario_id", list(SCENARIO_REGISTRY.keys()))
def test_relaxed_run_yields_sovereign_atoms(scenario_id):
    """Relaxed run must always yield at least one sovereign() atom."""
    result = run_scenario(scenario_id)
    assert result["n_sovereign_active"] > 0, (
        f"{scenario_id}: relaxed run produced no sovereign atoms"
    )


def test_t_clt_03_has_elastic_atoms():
    """T-CLT-03 SAT case must derive elastic hour_bank predicates."""
    result = run_scenario("T-CLT-03")
    elastic_names = [a.lower() for a in result["active_elastic"]]
    assert any("hour_bank" in a for a in elastic_names), (
        f"T-CLT-03: expected elastic hour_bank atom, got {result['active_elastic']}"
    )


def test_c2_has_obligation_sovereign():
    """C2 must derive sovereign(obligation_immediate_supply_critical_inputs_oxygen)."""
    result = run_scenario("C2")
    sov_lower = [a.lower() for a in result["active_sovereign"]]
    assert any("obligation_immediate_supply" in a for a in sov_lower), (
        f"C2: missing obligation_immediate_supply sovereign atom"
    )
