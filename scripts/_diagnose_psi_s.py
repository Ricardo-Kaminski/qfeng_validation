"""Diagnose whether occupancy actually changes Clingo psi_S output."""
import sys
sys.path.insert(0, 'src')

from qfeng.e5_symbolic.scenario_loader import run_scenario_with_occupancy
from qfeng.e5_symbolic.psi_builder import build_psi_s

test_occupancies = [30, 45, 76, 82, 85, 86, 92, 104]

print(f"{'occ%':>6} | {'n_sov':>5} | {'n_ela':>5} | {'active_sovereign (first 3)'}")
print("-" * 70)
for occ in test_occupancies:
    r = run_scenario_with_occupancy("C2", occ)
    psi_s = build_psi_s("C2", r["active_sovereign"], r["active_elastic"])
    sov_preview = list(r["active_sovereign"])[:3]
    print(f"{occ:>6} | {r['n_sovereign_active']:>5} | {len(r['active_elastic']):>5} | {sov_preview}")
    if occ in (82, 86):
        print(f"         psi_s = {psi_s.round(4)}")
