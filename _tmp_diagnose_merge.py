"""Diagnostica mismatch CNES entre numerador e denominador."""
import sys, pandas as pd
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DERIVED = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\derived"

num = pd.read_parquet(f"{DERIVED}/demas_vepi_manaus_uti_diario.parquet")
den = pd.read_parquet(f"{DERIVED}/cnes_lt_manaus_uti_mensal.parquet")

num["data"] = pd.to_datetime(num["data"])
num["ano_mes"] = num["data"].dt.strftime("%Y-%m")

print("=== NUMERADOR (DEMAS-VEPI 2021) ===")
num21 = num[num["data"].dt.year == 2021]
cnes_num = sorted(num21["cnes"].unique())
print(f"N CNES unicos: {len(cnes_num)}")
print(f"Exemplos CNES (primeiro 15): {cnes_num[:15]}")
print(f"Len CNES[0]: {len(cnes_num[0]) if cnes_num else 'N/A'}")

print("\n=== DENOMINADOR (CNES-LT jan/2021) ===")
den21 = den[den["ano_mes"] == "2021-01"]
cnes_den = sorted(den21["cnes"].unique())
print(f"N CNES unicos jan/2021: {len(cnes_den)}")
print(f"Exemplos CNES (todos): {cnes_den}")
print(f"Len CNES[0]: {len(cnes_den[0]) if cnes_den else 'N/A'}")

print("\n=== INTERSECAO ===")
s_num = set(cnes_num)
s_den = set(cnes_den)
inter = s_num & s_den
print(f"CNES em ambos: {len(inter)}")
print(f"CNES so no num: {len(s_num - s_den)}")
print(f"CNES so no den: {len(s_den - s_num)}")

# Tentar match com zero-padding
cnes_num_7 = {c.zfill(7) for c in cnes_num}
cnes_den_7 = {c.zfill(7) for c in cnes_den}
inter7 = cnes_num_7 & cnes_den_7
print(f"\nApos zfill(7) — CNES em ambos: {len(inter7)}")

# Mostrar exemplos do que nao casa
in_num_not_den = sorted(s_num - s_den)[:10]
print(f"\nCNES no num mas nao no den: {in_num_not_den}")

in_den_not_num = sorted(s_den - s_num)
print(f"CNES no den mas nao no num: {in_den_not_num}")

# Verificar capacidade total mensal sem matching por CNES
print("\n=== CAPACIDADE TOTAL MANAUS (ignorando CNES matching) ===")
cap_total = den.groupby("ano_mes")["qt_uti_existente_total"].sum()
print(cap_total.to_string())
