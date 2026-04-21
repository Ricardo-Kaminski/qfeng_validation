"""
extract_manaus_sih_python.py
============================
Extração SIH/SUS Manaus via PySUS (Python)
Caso C2 — Q-FENG PoC: Crise de Oxigênio Manaus 2021

Instalação:
    pip install pysus pandas pyarrow

Uso:
    python scripts/extract_manaus_sih_python.py

Saída:
    data/predictors/manaus_sih/sih_manaus_2020_2021.parquet
    data/predictors/manaus_sih/serie_temporal_manaus.parquet
    data/predictors/manaus_sih/serie_temporal_manaus.csv
"""
from __future__ import annotations
import logging
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "data" / "predictors" / "manaus_sih"
MANAUS_IBGE = "130260"
PERIODOS = [(2020,10),(2020,11),(2020,12),(2021,1),(2021,2),(2021,3)]
CIDS_PREFIX = {"J96", "J18", "U07"}


def extrair() -> pd.DataFrame:
    try:
        from pysus.ftp.databases.sih import SIH
    except ImportError:
        raise ImportError("Execute: pip install pysus")

    sih = SIH().load()
    dfs = []
    for year, month in PERIODOS:
        log.info(f"Baixando SIH-RD AM {year}/{month:02d}...")
        try:
            files = sih.get_files("RD", uf="AM", year=year, month=month)
            parquets = sih.download(files)
            df = parquets.to_dataframe()
            log.info(f"  {len(df):,} registros")
            dfs.append(df)
        except Exception as e:
            log.error(f"  Erro {year}/{month:02d}: {e}")

    df_raw = pd.concat(dfs, ignore_index=True)
    df_manaus = df_raw[df_raw["MUNIC_RES"].astype(str) == MANAUS_IBGE].copy()
    df_cid = df_manaus[
        df_manaus["DIAG_PRINC"].str[:3].str.upper().isin(CIDS_PREFIX)
    ].copy()
    df_cid["COMPETENCIA"] = (
        df_cid["ANO_CMPT"].astype(str) +
        df_cid["MES_CMPT"].astype(str).str.zfill(2)
    )
    log.info(f"Total filtrado: {len(df_cid):,} registros Manaus + J96/J18/U07")
    return df_cid


def agregar_serie(df: pd.DataFrame) -> pd.DataFrame:
    df["MORTE_N"] = pd.to_numeric(df["MORTE"], errors="coerce").fillna(0)
    df["UTI_D"] = pd.to_numeric(df.get("UTI_MES_TO", 0), errors="coerce").fillna(0)
    serie = df.groupby("COMPETENCIA").agg(
        internacoes_total=("DIAG_PRINC","count"),
        obitos=("MORTE_N","sum"),
        dias_uti=("UTI_D","sum"),
        internacoes_j96=("DIAG_PRINC", lambda x: x.str[:3].str.upper().eq("J96").sum()),
        internacoes_u07=("DIAG_PRINC", lambda x: x.str[:3].str.upper().eq("U07").sum()),
    ).reset_index()
    serie["taxa_mortalidade"] = serie["obitos"] / serie["internacoes_total"]
    serie["COMPETENCIA_DT"] = pd.to_datetime(serie["COMPETENCIA"], format="%Y%m")
    return serie.sort_values("COMPETENCIA_DT")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = extrair()
    df.to_parquet(OUTPUT_DIR / "sih_manaus_2020_2021.parquet", index=False)
    serie = agregar_serie(df)
    serie.to_parquet(OUTPUT_DIR / "serie_temporal_manaus.parquet", index=False)
    serie.to_csv(OUTPUT_DIR / "serie_temporal_manaus.csv", index=False)
    log.info("Concluído. Arquivos em data/predictors/manaus_sih/")
    log.info(serie[["COMPETENCIA","internacoes_total","obitos","taxa_mortalidade"]].to_string(index=False))


if __name__ == "__main__":
    main()
