import pandas as pd

df = pd.read_parquet('outputs/e5_results/validation_results.parquet')
print('=== validation_results ===')
print(df.to_string())
print()

df2 = pd.read_parquet('outputs/e5_results/theta_efetivo_manaus.parquet')
print('=== theta_efetivo_manaus ===')
print(df2.to_string())
print()

df3 = pd.read_parquet('outputs/e5_results/threshold_robustness.parquet')
print('=== threshold_robustness (head) ===')
print(df3.head(20).to_string())
print()

df4 = pd.read_parquet('outputs/e5_results/psi_sensitivity.parquet')
print('=== psi_sensitivity ===')
print(df4.to_string())
print()

df5 = pd.read_parquet('outputs/e5_results/manaus_bootstrap_ci.parquet')
print('=== manaus_bootstrap_ci ===')
print(df5.to_string())
