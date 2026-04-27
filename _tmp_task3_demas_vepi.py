"""
Tarefa 3 — Pipeline numerador: DEMAS-VEPI -> UTI diario COVID Manaus.
CRITICO: sep="," (bug Fase 2.1.5 usava sep=";").
"""
import sys, os
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW_DIR  = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\raw\api_demas_vepi"
OUT_PATH = r"C:\Workspace\academico\qfeng_validacao\data\predictors\manaus_bi\derived\demas_vepi_manaus_uti_diario.parquet"

NUMERIC_COLS = [
    "ocupacaoConfirmadoUti", "ocupacaoSuspeitoUti",
    "ocupacaoConfirmadoCli", "ocupacaoSuspeitoCli",
    "saidaConfirmadaObitos", "saidaSuspeitaObitos",
]

files = [
    ("esus-vepi.LeitoOcupacao_2020.csv", 2020),
    ("esus-vepi.LeitoOcupacao_2021.csv", 2021),
]

all_daily = []

for fname, ano in files:
    fpath = os.path.join(RAW_DIR, fname)
    fsize = os.path.getsize(fpath) / 1e6
    print(f"\n{'='*60}")
    print(f"Lendo {fname} ({fsize:.0f} MB)...")

    # CRITICO: sep="," (bug Fase 2.1.5 usava sep=";")
    df = pd.read_csv(fpath, sep=",", dtype=str, low_memory=False)
    print(f"Shape total: {df.shape}")
    print(f"Colunas[0:5]: {list(df.columns[:5])}")

    # Validar schema (primeira coluna pode ser '' ou 'Unnamed: 0' dependendo do pandas)
    expected_cols_2_5 = ['_id', 'dataNotificacao', 'cnes', 'ocupacaoSuspeitoCli']
    actual_cols_2_5   = list(df.columns[1:5])
    schema_ok = actual_cols_2_5 == expected_cols_2_5 and len(df.columns) >= 20
    print(f"Schema check: {'OK' if schema_ok else 'DIVERGENTE'}")
    print(f"  Cols[0:5]: {list(df.columns[:5])}")
    if not schema_ok:
        print(f"  PARANDO: esperado {expected_cols_2_5}, obtido {actual_cols_2_5}, ncols={len(df.columns)}")
        sys.exit(1)

    # Filtrar Manaus
    manaus = df[df["municipio"].fillna("").str.contains("Manaus", case=False, na=False)].copy()
    n_manaus = len(manaus)
    print(f"Registros Manaus: {n_manaus} (de {len(df)})")
    if ano == 2021 and not (6800 <= n_manaus <= 7100):
        print(f"  AVISO: esperado ~6945, obtido {n_manaus}")

    # Cast numerico
    for col in NUMERIC_COLS:
        if col in manaus.columns:
            manaus[col] = pd.to_numeric(manaus[col], errors="coerce")

    # Numerador
    uti_cols = [c for c in ["ocupacaoConfirmadoUti","ocupacaoSuspeitoUti"] if c in manaus.columns]
    manaus["uti_covid_total"] = manaus[uti_cols].sum(axis=1, min_count=1)
    coverage = manaus["uti_covid_total"].notna().mean()
    print(f"Cobertura uti_covid_total nao-null: {coverage:.1%}")

    # Parse temporal
    manaus["dt"] = pd.to_datetime(manaus["dataNotificacao"], errors="coerce", utc=True)
    manaus["dt"] = manaus["dt"].dt.tz_convert("America/Manaus")
    manaus["data"] = manaus["dt"].dt.date

    # CNES como string
    manaus["cnes"] = manaus["cnes"].fillna("").str.strip()

    # Colunas opcionais de obitos
    if "saidaConfirmadaObitos" not in manaus.columns:
        manaus["saidaConfirmadaObitos"] = float("nan")
    if "saidaSuspeitaObitos" not in manaus.columns:
        manaus["saidaSuspeitaObitos"] = float("nan")

    # Agregacao diaria por CNES
    diario = manaus.groupby(["data","cnes"]).agg(
        uti_covid_total_max=("uti_covid_total","max"),
        uti_covid_total_mean=("uti_covid_total","mean"),
        n_registros_dia=("dt","count"),
        obitos_confirmado_max=("saidaConfirmadaObitos","max"),
        obitos_suspeito_max=("saidaSuspeitaObitos","max"),
    ).reset_index()
    diario["source_file"] = fname

    print(f"CNES distintos: {manaus['cnes'].nunique()}")
    print(f"Shape diario: {diario.shape}")
    pico = manaus.groupby(manaus["dt"].dt.to_period("M"))["uti_covid_total"].sum()
    print(f"Top 3 meses UTI total: {pico.nlargest(3).to_dict()}")

    all_daily.append(diario)

# Concatenar
df_out = pd.concat(all_daily, ignore_index=True)
df_out["data"] = pd.to_datetime(df_out["data"])

col_order = ["data","cnes","uti_covid_total_max","uti_covid_total_mean",
             "n_registros_dia","obitos_confirmado_max","obitos_suspeito_max","source_file"]
df_out = df_out[col_order]

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
df_out.to_parquet(OUT_PATH, index=False)
print(f"\nSalvo: {OUT_PATH}  shape={df_out.shape}")

# Sanity checks (usando parquet salvo)
dc = pd.read_parquet(OUT_PATH)
dc["data"] = pd.to_datetime(dc["data"])

print("\n=== SANITY CHECKS ===")
n_2021 = len(dc[dc["data"].dt.year==2021])
c_2021 = dc[dc["data"].dt.year==2021]["cnes"].nunique()
print(f"Linhas diarias-CNES 2021: {n_2021}  (probe forense: ~esperado ~6945 registros Manaus, daily pode ser maior/menor por CNES)")
print(f"CNES distintos 2021: {c_2021}  (esperado ~31)")

cov = dc["uti_covid_total_max"].notna().mean()
print(f"Cobertura uti_covid_total_max nao-null: {cov:.1%}  (esperado ~77%)")

by_month = dc.groupby(dc["data"].dt.to_period("M"))["uti_covid_total_max"].sum()
top3 = by_month.nlargest(3)
print(f"Top 3 meses por UTI max-sum: {top3.to_dict()}")
pico_mes = str(by_month.idxmax())
pico_ok = pico_mes in ["2021-01","2021-02","2021-03","2021-04"]
print(f"Pico em jan-abr/2021: {'OK' if pico_ok else 'VERIFICAR'} ({pico_mes})")

max_val = dc["uti_covid_total_max"].max()
print(f"Max uti_covid_total_max: {max_val}  (plausivel <= 250)")

all_ok = cov > 0.5 and pico_ok
print(f"\nRESULTADO: {'PASSOU' if all_ok else 'VERIFICAR'}")
