"""Verify each pattern in _SCENARIO_PREDICATE_MAP matches ≥1 active atom per scenario.

Guards against silent zero-weight rows in psi_S (audit C-5).
"""

import pytest

from qfeng.e5_symbolic.psi_builder import _SCENARIO_PREDICATE_MAP
from qfeng.e5_symbolic.scenario_loader import run_scenario


@pytest.fixture(scope="module")
def active_atoms_by_scenario():
    result = {}
    for scenario_id in _SCENARIO_PREDICATE_MAP:
        data = run_scenario(scenario_id)
        atoms = [a.lower() for a in data["active_sovereign"]] + [
            a.lower() for a in data["active_elastic"]
        ]
        result[scenario_id] = atoms
    return result


@pytest.mark.parametrize(
    "scenario_id,pattern",
    [
        (sid, pattern)
        for sid, pattern_map in _SCENARIO_PREDICATE_MAP.items()
        for pattern in pattern_map
    ],
)
def test_pattern_matches_at_least_one_atom(
    scenario_id, pattern, active_atoms_by_scenario
):
    atoms = active_atoms_by_scenario[scenario_id]
    matching = [a for a in atoms if pattern in a]
    assert matching, (
        f"Pattern '{pattern}' in scenario '{scenario_id}' matched 0 atoms.\n"
        f"Active atoms: {atoms}"
    )
