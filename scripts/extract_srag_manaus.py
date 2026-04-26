"""Extrai serie SRAG Manaus (12 meses) do SIVEP-Gripe INFLUD20/21.

Filtragem:
  CO_MUN_RES == "130260" (Manaus, IBGE)
  CLASSI_FIN in {"5", "4"}  (COVID-19 + SRAG nao-especificada)
  DT_SIN_PRI em 2020-07-01 a 2021-06-30

Saida: data/predictors/manaus_bi/srag_manaus.parquet
  Schema: year, month, competencia, n_srag_total, n_covid, n_outros,
          n_obitos, letalidade_pct, source, is_stub
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).parents[1]
RAW_DIR = PROJECT_ROOT / "data/predictors/manaus_bi/raw/srag_manaus_sivep"
OUTPUT_PATH = PROJECT_ROOT / "data/predictors/manaus_bi/srag_manaus.parquet"

MUNICIPIO_MANAUS = "130260"
START_DATE = pd.Timestamp("2020-07-01")
END_DATE   = pd.Timestamp("2021-06-30")
CLASSI_COVID   = "5"
CLASSI_OUTROS  = "4"

# Months in the series
COMPETENCIAS = [
    (2020,  7), (2020,  8), (2020,  9), (2020, 10), (2020, 11), (2020, 12),
    (2021,  1), (2021,  2), (2021,  3), (2021,  4), (2021,  5), (2021,  6),
]


def _find_influd(year_tag: str) -> Path | None:
    candidates = list(RAW_DIR.glob(f"INFLUD{year_tag}*.csv"))
    return candidates[0] if candidates else None


def _load_influd(path: Path) -> pd.DataFrame:
    """Load INFLUD CSV, handling encoding and separator variations."""
    for enc in ("latin-1", "utf-8", "cp1252"):
        for sep in (";", ","):
            try:
                df = pd.read_csv(path, encoding=enc, sep=sep, low_memory=False,
                                 dtype=str)
                if len(df.columns) > 5:
                    print(f"  Lido: {path.name}  enc={enc} sep='{sep}'  {len(df)} linhas, {len(df.columns)} colunas")
                    return df
            except Exception:
                continue
    raise RuntimeError(f"Nao foi possivel ler {path}")


def _parse_date(series: pd.Series) -> pd.Series:
    for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
        try:
            return pd.to_datetime(series, format=fmt, errors="coerce")
        except Exception:
            continue
    return pd.to_datetime(series, infer_datetime_format=True, errors="coerce")


def extract_from_files() -> pd.DataFrame:
    """Attempt extraction from downloaded INFLUD CSV files."""
    f20 = _find_influd("20")
    f21 = _find_influd("21")
    if not f20 or not f21:
        return None

    parts = []
    for path in [f20, f21]:
        df = _load_influd(path)
        # Filter municipality
        mun_col = next((c for c in df.columns if "CO_MUN_RES" in c.upper()), None)
        if mun_col is None:
            print(f"  [WARN] Coluna CO_MUN_RES nao encontrada em {path.name}")
            continue
        df = df[df[mun_col].str.strip().str.startswith("130260")]
        print(f"  Manaus: {len(df)} linhas em {path.name}")
        parts.append(df)

    if not parts:
        return None

    raw = pd.concat(parts, ignore_index=True)

    # Date column
    date_col = next((c for c in raw.columns if c.upper() in ("DT_SIN_PRI", "DT_NOTIFIC")), None)
    if date_col is None:
        print("[WARN] Coluna de data nao encontrada — usando DT_NOTIFIC fallback")
        date_col = raw.columns[0]
    raw["_date"] = _parse_date(raw[date_col])
    raw = raw[(raw["_date"] >= START_DATE) & (raw["_date"] <= END_DATE)]
    print(f"  Apos filtro de data (jul/2020-jun/2021): {len(raw)} linhas")

    # CLASSI_FIN
    classi_col = next((c for c in raw.columns if "CLASSI_FIN" in c.upper()), None)
    if classi_col:
        raw = raw[raw[classi_col].str.strip().isin({CLASSI_COVID, CLASSI_OUTROS})]
        print(f"  Apos filtro CLASSI_FIN 4/5: {len(raw)} linhas")

    # EVOLUCAO (obitos = "2")
    evol_col = next((c for c in raw.columns if "EVOLUCAO" in c.upper()), None)
    obito_mask = (raw[evol_col].str.strip() == "2") if evol_col else pd.Series(False, index=raw.index)
    raw["_obito"] = obito_mask.astype(int)

    covid_mask = (raw[classi_col].str.strip() == CLASSI_COVID) if classi_col else pd.Series(False, index=raw.index)
    raw["_covid"] = covid_mask.astype(int)

    # Monthly aggregation
    raw["year"]  = raw["_date"].dt.year
    raw["month"] = raw["_date"].dt.month
    grp = raw.groupby(["year", "month"]).agg(
        n_srag_total=("_covid", "count"),
        n_covid=("_covid", "sum"),
        n_obitos=("_obito", "sum"),
    ).reset_index()
    grp["n_outros"] = grp["n_srag_total"] - grp["n_covid"]
    grp["letalidade_pct"] = np.where(
        grp["n_srag_total"] > 0,
        (grp["n_obitos"] / grp["n_srag_total"] * 100).round(2),
        0.0
    )
    return grp


def build_stub() -> pd.DataFrame:
    """Build stub parquet with zero-count rows when source files are unavailable."""
    rows = []
    for y, m in COMPETENCIAS:
        rows.append({
            "year": y, "month": m,
            "competencia": f"{y}-{m:02d}",
            "n_srag_total": 0,
            "n_covid": 0,
            "n_outros": 0,
            "n_obitos": 0,
            "letalidade_pct": 0.0,
            "source": "STUB — INFLUD20/21 nao baixados",
            "is_stub": True,
        })
    return pd.DataFrame(rows)


def main() -> None:
    print("=== Tarefa 1.2 — Extracao SRAG Manaus ===")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    grp = extract_from_files()
    if grp is not None:
        # Merge with full competencia list to ensure 12 rows
        base = pd.DataFrame(COMPETENCIAS, columns=["year", "month"])
        grp = base.merge(grp, on=["year", "month"], how="left").fillna(0)
        grp["competencia"] = grp.apply(lambda r: f"{int(r['year'])}-{int(r['month']):02d}", axis=1)
        for col in ["n_srag_total", "n_covid", "n_outros", "n_obitos"]:
            grp[col] = grp[col].astype(int)
        grp["source"] = "SIVEP-Gripe INFLUD20/21 (OpenDataSUS)"
        grp["is_stub"] = False
        stub_mode = False
    else:
        print("[STUB] Arquivos INFLUD20/21 nao encontrados — criando stub de 12 linhas zeros")
        print("       Execute download_sivep_gripe_ftp.py e re-execute este script")
        grp = build_stub()
        stub_mode = True

    grp = grp[["year", "month", "competencia", "n_srag_total", "n_covid",
               "n_outros", "n_obitos", "letalidade_pct", "source", "is_stub"]]
    grp.to_parquet(OUTPUT_PATH, index=False)
    print(f"\nParquet salvo: {OUTPUT_PATH}")
    print(f"Linhas: {len(grp)} | is_stub={stub_mode}")
    print("\n--- Serie SRAG Manaus ---")
    for _, row in grp.iterrows():
        stub_flag = " [STUB]" if row["is_stub"] else ""
        print(f"  {row['competencia']}: total={row['n_srag_total']:>4}  covid={row['n_covid']:>4}  obitos={row['n_obitos']:>3}  let={row['letalidade_pct']:.1f}%{stub_flag}")
    if stub_mode:
        print("\nATENCAO: stub ativo — Spearman(TOH,SRAG) sera 0.0 (invalido)")
        print("Baixe INFLUD20/21 de opendatasus.saude.gov.br e re-execute para dados reais")
    else:
        print("\nTarefa 1.2 CONCLUIDA com dados reais.")


if __name__ == "__main__":
    main()
