import pandas as pd

df2 = pd.read_parquet('outputs/e5_results/theta_efetivo_manaus.parquet')
print('=== theta_efetivo_manaus ===')
print(df2.dtypes)
print()
print(df2.to_string())
print()

df1 = pd.read_parquet('outputs/e5_results/validation_results.parquet')
print('=== validation_results ===')
print(df1.dtypes)
print()
print(df1.to_string())
