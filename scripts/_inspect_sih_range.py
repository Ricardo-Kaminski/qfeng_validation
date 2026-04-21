"""Check available months in SIH and pre-crisis baseline stats."""
import sys
sys.path.insert(0, "C:/Workspace/academico/qfeng_validacao/src")
import pandas as pd
import numpy as np

sih = pd.read_parquet(
    "C:/Workspace/academico/qfeng_validacao/data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"
)
sih["ANO_CMPT"]  = sih["ANO_CMPT"].astype(int)
sih["MES_CMPT"]  = sih["MES_CMPT"].astype(int)
sih["MORTE"]     = pd.to_numeric(sih["MORTE"],     errors="coerce").fillna(0).astype(int)
sih["UTI_MES_TO"]= pd.to_numeric(sih["UTI_MES_TO"],errors="coerce").fillna(0)

COVID_CIDS = {"J189", "J960", "J961", "J969", "U071", "U072", "B342"}

print("Available year/month combinations (sorted):")
months = sorted(sih.groupby(["ANO_CMPT","MES_CMPT"]).size().reset_index().values.tolist())
for y, m, n in months:
    df_m = sih[(sih["ANO_CMPT"]==y) & (sih["MES_CMPT"]==m)]
    n_int  = len(df_m)
    n_obit = int(df_m["MORTE"].sum())
    n_resp = int(df_m["DIAG_PRINC"].isin(COVID_CIDS).sum())
    n_uti  = int((df_m["UTI_MES_TO"]>0).sum())
    t_mort = n_obit/max(n_int,1)
    t_resp = n_resp/max(n_int,1)
    t_uti  = n_uti/max(n_int,1)
    print(f"  {y}/{m:02d}: n={n_int:4d}  obitos={n_obit:3d}  t_mort={t_mort:.3f}  t_resp={t_resp:.3f}  t_uti={t_uti:.3f}")
