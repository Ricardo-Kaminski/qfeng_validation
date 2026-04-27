"""
Tarefa 4 — Juncao numerador x denominador -> TOH semanal real Manaus.
Abordagem municipal: soma de todos CNES por dia / capacidade mensal total Manaus.
Janela editorial: SE 10/2020 a SE 30/2021 (~73 SEs).

Nota metodologica: merge por CNES retornaria apenas 34% de cobertura porque
DEMAS-VEPI reporta 31 CNES (incluindo leitos emergenciais nao declarados em CNES-LT)
enquanto CNES-LT tem apenas 23 CNES com UTI adulto (74-77) formalmente declarados.
A agregacao municipal e mais robusta e consistente com calculo de TOH regional.
"""
import sys, os, shutil
import pandas as pd
import numpy as np
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DERIVED = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\derived"
ARCHIVE = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\_archive"
NUM_PATH = os.path.join(DERIVED, "demas_vepi_manaus_uti_diario.parquet")
DEN_PATH = os.path.join(DERIVED, "cnes_lt_manaus_uti_mensal.parquet")
OUT_PATH = os.path.join(DERIVED, "toh_semanal_manaus.parquet")
BAK_PATH = os.path.join(ARCHIVE, "toh_semanal_manaus_FASE215_PRE_BIS.parquet")

os.makedirs(ARCHIVE, exist_ok=True)
if os.path.exists(OUT_PATH) and not os.path.exists(BAK_PATH):
    shutil.copy(OUT_PATH, BAK_PATH)
    print(f"Backup: {BAK_PATH}")
else:
    print("Backup ja existe ou nao ha parquet anterior")

# ---------- 1. Ler parquets ----------
num = pd.read_parquet(NUM_PATH)
den = pd.read_parquet(DEN_PATH)
num["data"] = pd.to_datetime(num["data"])
den["competencia"] = pd.to_datetime(den["competencia"])

# Nota sobre matching por CNES
num["ano_mes"] = num["data"].dt.strftime("%Y-%m")
n_match = num.merge(den[["ano_mes","cnes"]], on=["ano_mes","cnes"])
print(f"Nota: matching por CNES = {len(n_match)/len(num):.1%} ({len(n_match)}/{len(num)})")
print(f"Usando abordagem municipal: sum(todos CNES) por dia / capacidade_total_mes")

# ---------- 2. Numerador municipal diario ----------
# Sum de uti_covid_total_max por dia, todos os CNES Manaus
mun_dia = num.groupby("data").agg(
    uti_covid_municipal=("uti_covid_total_max", "sum"),
    n_cnes_ativos=("cnes", "nunique"),
    n_registros=("n_registros_dia", "sum"),
).reset_index()
mun_dia["ano_mes"] = mun_dia["data"].dt.strftime("%Y-%m")
print(f"\nNumerador municipal: {len(mun_dia)} dias")
print(f"Pico uti_covid_municipal: {mun_dia['uti_covid_municipal'].max():.0f} em {mun_dia.loc[mun_dia['uti_covid_municipal'].idxmax(),'data'].date()}")

# ---------- 3. Denominador municipal mensal ----------
cap_mensal = den.groupby("ano_mes")["qt_uti_existente_total"].sum().reset_index()
cap_mensal.columns = ["ano_mes", "capacidade_municipal"]
print(f"\nDenominador municipal: {len(cap_mensal)} meses")
print(f"Range capacidade: {cap_mensal['capacidade_municipal'].min()} - {cap_mensal['capacidade_municipal'].max()} leitos")

# ---------- 4. Merge por mes ----------
merged = mun_dia.merge(cap_mensal, on="ano_mes", how="left")
cov_den = merged["capacidade_municipal"].notna().mean()
print(f"Cobertura denominador: {cov_den:.1%}")
merged = merged[merged["capacidade_municipal"].fillna(0) > 0].copy()
merged["toh_dia"] = merged["uti_covid_municipal"] / merged["capacidade_municipal"]
print(f"\nPico toh_dia: {merged['toh_dia'].max():.3f} em {merged.loc[merged['toh_dia'].idxmax(),'data'].date()}")

# ---------- 5. Agregacao SE epidemiologica ----------
merged["dt"] = pd.to_datetime(merged["data"])
iso = merged["dt"].dt.isocalendar()
merged["year_se"] = iso.year.astype(int)
merged["sem_epi"]  = iso.week.astype(int)

semanal = merged.groupby(["year_se","sem_epi"]).agg(
    toh_uti_pct=("toh_dia","mean"),
    uti_ocupada_covid_media_se=("uti_covid_municipal","mean"),
    uti_ocupada_covid_pico_se=("uti_covid_municipal","max"),
    capacidade_uti_total_mes=("capacidade_municipal","mean"),
    n_cnes_ativos=("n_cnes_ativos","max"),
    n_dias_com_dado=("data","count"),
).reset_index()

def monday_of_isoweek(year, week):
    return pd.Timestamp.fromisocalendar(int(year), int(week), 1)

semanal["date_se_monday"] = semanal.apply(
    lambda r: monday_of_isoweek(r["year_se"], r["sem_epi"]), axis=1)

# ---------- 6. Filtro janela + SEs esperadas ----------
all_se = []
for yr, wk in [(2020,w) for w in range(10,54)] + [(2021,w) for w in range(1,31)]:
    try:
        monday = monday_of_isoweek(yr, wk)
        all_se.append({"year_se": yr, "sem_epi": wk, "date_se_monday": monday})
    except ValueError:
        pass
df_all_se = pd.DataFrame(all_se)

semanal = df_all_se.merge(semanal, on=["year_se","sem_epi","date_se_monday"], how="left")
semanal = semanal.sort_values(["year_se","sem_epi"]).reset_index(drop=True)
print(f"\nSEs na janela: {len(semanal)}")

# ---------- 7. Imputacao forward-fill max 3 SE ----------
semanal["is_imputed"] = semanal["n_dias_com_dado"].isna() | (semanal["n_dias_com_dado"] < 3)

toh_vals = semanal["toh_uti_pct"].values.copy()
consec = 0
for i in range(len(toh_vals)):
    if np.isnan(toh_vals[i]):
        if consec < 3 and i > 0 and not np.isnan(toh_vals[i-1]):
            toh_vals[i] = toh_vals[i-1]
        consec += 1
    else:
        consec = 0
semanal["toh_uti_pct"] = toh_vals

def classify_method(row):
    if pd.isna(row["n_dias_com_dado"]) or row["n_dias_com_dado"] < 1:
        return "nan_gap_too_large" if pd.isna(row["toh_uti_pct"]) else "forward_fill_max_3SE"
    elif row["n_dias_com_dado"] < 3:
        return "forward_fill_max_3SE"
    return "demas_vepi_direct"

semanal["method"] = semanal.apply(classify_method, axis=1)
semanal["source"] = "demas_vepi_local_microdado_v2026.04"

for col in ["n_dias_com_dado","n_cnes_ativos","capacidade_uti_total_mes",
            "uti_ocupada_covid_media_se","uti_ocupada_covid_pico_se"]:
    if col not in semanal.columns:
        semanal[col] = np.nan

col_order = ["year_se","sem_epi","date_se_monday","toh_uti_pct","n_cnes_ativos",
             "capacidade_uti_total_mes","uti_ocupada_covid_media_se",
             "uti_ocupada_covid_pico_se","n_dias_com_dado","is_imputed","method","source"]
semanal = semanal[col_order]
semanal.to_parquet(OUT_PATH, index=False)
print(f"Salvo: {OUT_PATH}  shape={semanal.shape}")

# ---------- Sanity checks ----------
print("\n=== SANITY CHECKS ===")
n_se = len(semanal)
s1 = 71 <= n_se <= 75
print(f"73 SEs (+-2): {'OK' if s1 else 'FALHA'} ({n_se})")

pico_row = semanal.dropna(subset=["toh_uti_pct"]).nlargest(1,"toh_uti_pct").iloc[0]
pico_yr, pico_wk, pico_val = int(pico_row.year_se), int(pico_row.sem_epi), pico_row.toh_uti_pct
s2 = (pico_yr == 2021 and 1 <= pico_wk <= 8)
print(f"Pico SE {pico_yr}-W{pico_wk:02d}: TOH={pico_val:.3f}  {'OK (SE01-08/2021)' if s2 else 'VERIFICAR'}")

s3 = 0.65 <= pico_val <= 1.50
print(f"Valor pico plausivel (0.65-1.50): {'OK' if s3 else f'VERIFICAR ({pico_val:.3f})'}")

n_direct = (semanal["method"]=="demas_vepi_direct").sum()
n_imp    = semanal["is_imputed"].sum()
s4 = n_direct >= 60
print(f"SEs diretas >= 60: {'OK' if s4 else 'VERIFICAR'} ({n_direct})")
print(f"SEs imputadas: {n_imp}")

early_toh = semanal[(semanal["year_se"]==2020)&(semanal["sem_epi"].between(10,15))]["toh_uti_pct"].dropna()
early_ok = len(early_toh) > 0 and early_toh.mean() > 0
print(f"TOH SE 10-15/2020 > 0: {'OK' if early_ok else 'VERIFICAR'} (mean={early_toh.mean():.3f})")

# Top 5
print(f"\nTop 5 SEs por TOH:")
top5 = semanal.dropna(subset=["toh_uti_pct"]).nlargest(5,"toh_uti_pct")[
    ["year_se","sem_epi","date_se_monday","toh_uti_pct","n_cnes_ativos","is_imputed"]]
for _,r in top5.iterrows():
    print(f"  {int(r.year_se)}-W{int(r.sem_epi):02d} ({r.date_se_monday.date()}): TOH={r.toh_uti_pct:.3f}  n_cnes={r.n_cnes_ativos}  imp={r.is_imputed}")

# Curva ASCII
print(f"\nCurva ASCII TOH:")
vals = semanal["toh_uti_pct"].fillna(0).values
vmax = vals.max()
chars = " ._-=+*#@"
line = "".join(chars[int((v/vmax)*(len(chars)-1))] if vmax>0 else " " for v in vals)
print(f"  [{line}]")
print(f"  SE10/2020{'':<42}SE30/2021")

all_ok = s1 and s2 and (pico_val < 1.50) and s4
print(f"\nRESULTADO: {'PASSOU' if all_ok else 'VERIFICAR'}")
