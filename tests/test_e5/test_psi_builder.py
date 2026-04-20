"""Unit tests for E5 psi_builder module."""

import numpy as np
import pytest

from qfeng.e5_symbolic.psi_builder import (
    DECISION_SPACES,
    build_psi_n,
    build_psi_s,
)


class TestBuildPsiN:
    @pytest.mark.parametrize("scenario_id", ["C2", "C3", "C7", "T-CLT-01", "T-CLT-02", "T-CLT-03"])
    def test_psi_n_is_unit_vector(self, scenario_id):
        psi = build_psi_n(scenario_id)
        assert abs(np.linalg.norm(psi) - 1.0) < 1e-9

    @pytest.mark.parametrize("scenario_id", ["C2", "C3", "C7", "T-CLT-01", "T-CLT-02", "T-CLT-03"])
    def test_psi_n_dimension_matches_decision_space(self, scenario_id):
        psi = build_psi_n(scenario_id)
        assert len(psi) == len(DECISION_SPACES[scenario_id])

    @pytest.mark.parametrize("unsat_scenario", ["C2", "C3", "C7", "T-CLT-01", "T-CLT-02"])
    def test_psi_n_favors_violating_action_in_unsat_scenarios(self, unsat_scenario):
        """Action 0 should have highest weight in UNSAT scenarios."""
        psi = build_psi_n(unsat_scenario)
        assert psi[0] == max(psi), f"{unsat_scenario}: psi_N should favor action 0 (violating)"

    def test_t_clt_03_psi_n_favors_compliant_action(self):
        """T-CLT-03 action 0 (approve with CCT) should have highest weight."""
        psi = build_psi_n("T-CLT-03")
        assert psi[0] == max(psi)


class TestBuildPsiS:
    @pytest.mark.parametrize("scenario_id", ["C2", "C3", "C7", "T-CLT-01", "T-CLT-02", "T-CLT-03"])
    def test_psi_s_is_unit_vector_when_atoms_present(self, scenario_id):
        # Use representative sovereign atoms for each scenario
        atoms_by_scenario = {
            "C2": ["sovereign(obligation_immediate_supply_critical_inputs_oxygen)"],
            "C3": ["sovereign(obligation_to_reduce_regional_social_inequality)"],
            "C7": ["sovereign(prohibition_disparate_impact_in_federal_programs)"],
            "T-CLT-01": ["sovereign(prohibition_of_generic_precedent_citation)"],
            "T-CLT-02": ["sovereign(semester_hour_bank_requires_cct_or_act)"],
            "T-CLT-03": [],
        }
        elastic_by_scenario = {
            "T-CLT-03": ["elastic(hour_bank_with_cct_max_1_year)"],
        }
        sov = atoms_by_scenario[scenario_id]
        ela = elastic_by_scenario.get(scenario_id, [])
        psi = build_psi_s(scenario_id, sov, ela)
        assert abs(np.linalg.norm(psi) - 1.0) < 1e-9

    def test_unsat_scenarios_produce_high_theta(self):
        """Sovereign atoms blocking action 0 should produce theta > 120 with psi_N."""
        import math
        from qfeng.e5_symbolic.interference import compute_theta

        # C2: obligation blocks continue_autonomous (action 0)
        psi_n = build_psi_n("C2")
        psi_s = build_psi_s(
            "C2",
            [
                "sovereign(obligation_immediate_supply_critical_inputs_oxygen)",
                "sovereign(critical_health_system_situation_manaus)",
                "sovereign(right_to_health_as_duty_of_state)",
            ],
        )
        _, theta_deg = compute_theta(psi_n, psi_s)
        assert theta_deg > 120.0, f"C2 theta should be > 120, got {theta_deg:.1f}"

    def test_t_clt_03_produces_stac_theta(self):
        """T-CLT-03 with valid CCT elastic atoms should give theta < 30."""
        import math
        from qfeng.e5_symbolic.interference import compute_theta

        psi_n = build_psi_n("T-CLT-03")
        psi_s = build_psi_s(
            "T-CLT-03",
            ["sovereign(recognition_of_collective_bargaining)"],
            ["elastic(hour_bank_with_cct_max_1_year)", "elastic(annual_hour_bank_negotiable)"],
        )
        _, theta_deg = compute_theta(psi_n, psi_s)
        assert theta_deg < 30.0, f"T-CLT-03 theta should be < 30, got {theta_deg:.1f}"

    def test_fallback_when_no_patterns_match(self):
        """If no sovereign atoms match patterns, fallback should not crash."""
        psi = build_psi_s("C2", ["sovereign(some_unknown_predicate_xyz)"])
        assert np.linalg.norm(psi) > 0
