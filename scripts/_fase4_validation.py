"""Fase 4: CB onset validation — all 12 months table + critical assertion."""
from qfeng.e5_symbolic.manaus_sih_loader import load_manaus_real_series

serie = load_manaus_real_series()
for row in serie:
    theta_t = row["theta_t"]
    regime = "CB" if theta_t >= 120 else ("HITL" if theta_t >= 30 else "STAC")
    print(f"{row['label']:>10} | theta_t={theta_t:6.2f} | occ={row['hospital_occupancy_pct']:>3}% | {regime}")

oct_2020 = next(r for r in serie if r["label"] == "out/2020")
assert oct_2020["theta_t"] >= 120.0, f"CRITICAL: CB onset lost — theta_t(out/2020) = {oct_2020['theta_t']}"
print()
print("CB onset preserved in Oct/2020")
print(f"theta_t(out/2020) = {oct_2020['theta_t']}")
