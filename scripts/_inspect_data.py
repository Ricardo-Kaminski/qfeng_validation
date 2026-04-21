"""Inspect real data available for psi_N computation."""
import sys
sys.path.insert(0, "C:/Workspace/academico/qfeng_validacao/src")

import pandas as pd
import pickle

print("=" * 60)
print("SIH Manaus 2020-2021")
print("=" * 60)
sih = pd.read_parquet("C:/Workspace/academico/qfeng_validacao/data/predictors/manaus_sih/sih_manaus_2020_2021.parquet")
print("Shape:", sih.shape)
print("Columns:", list(sih.columns))
print("Dtypes:")
print(sih.dtypes)
print("\nSample:")
print(sih.head(6).to_string())

print("\n" + "=" * 60)
print("CEAF — df_uf.parquet")
print("=" * 60)
df_uf = pd.read_parquet("C:/Workspace/academico/qfeng_validacao/data/predictors/ceaf_medicamentos/df_uf.parquet")
print("Shape:", df_uf.shape)
print("Columns:", list(df_uf.columns))
print("\nSample:")
print(df_uf.head(3).to_string())

print("\n" + "=" * 60)
print("CEAF — validacao_predicoes.parquet")
print("=" * 60)
val = pd.read_parquet("C:/Workspace/academico/qfeng_validacao/data/predictors/ceaf_medicamentos/validacao_predicoes.parquet")
print("Shape:", val.shape)
print("Columns:", list(val.columns))
print("\nSample:")
print(val.head(3).to_string())

print("\n" + "=" * 60)
print("CEAF — features_list.pkl")
print("=" * 60)
with open("C:/Workspace/academico/qfeng_validacao/data/predictors/ceaf_medicamentos/features_list.pkl", "rb") as f:
    feats = pickle.load(f)
print("N features:", len(feats))
print("First 10:", feats[:10])
