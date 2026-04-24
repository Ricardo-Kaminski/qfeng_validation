"""Fase 6: Generate outputs/table7_new_values.csv from refactored pipeline."""
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ts = pd.read_parquet(PROJECT_ROOT / "outputs/e5_results/theta_efetivo_manaus.parquet")
ci = pd.read_parquet(PROJECT_ROOT / "outputs/e5_results/manaus_bootstrap_ci.parquet")

df = ts.merge(ci[["competencia", "theta_ci_lower_95", "theta_ci_upper_95"]], on="competencia", how="left")

# Round for display
for col in ["theta_t", "theta_efetivo", "alpha_t", "theta_ci_lower_95", "theta_ci_upper_95", "score_pressao"]:
    if col in df.columns:
        df[col] = df[col].round(2)

out = PROJECT_ROOT / "outputs" / "table7_new_values.csv"
df.to_csv(out, index=False)
print(f"Saved: {out}")
print()
print(df[["competencia", "theta_t", "theta_efetivo", "alpha_t",
          "hospital_occupancy_pct", "theta_ci_lower_95", "theta_ci_upper_95",
          "interference_regime", "data_source"]].to_string(index=False))
