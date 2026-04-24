"""Run E5 and print summary of theta values and regimes for Phase 5 check."""
import sys
sys.path.insert(0, "src")
from qfeng.e5_symbolic.runner import run_all_scenarios

results = run_all_scenarios()
print("\n=== E5 PHASE 5 SUMMARY ===")
for r in results:
    sat = "SAT" if r["interference_regime"] == "STAC" else "UNSAT/HITL"
    print(f"  {r['scenario_id']:12s} theta={r['theta_deg']:6.2f}  {r['interference_regime']:20s}  {sat}")
print(f"\nTotal scenarios: {len(results)}")
cb = sum(1 for r in results if r["interference_regime"] == "CIRCUIT_BREAKER")
stac = sum(1 for r in results if r["interference_regime"] == "STAC")
hitl = sum(1 for r in results if r["interference_regime"] == "HITL")
print(f"  CIRCUIT_BREAKER: {cb}  STAC: {stac}  HITL: {hitl}")
