"""Tarefa 1.1 — Extrai _TOH_FVS_AM e constrói toh_uti_manaus.parquet.

Importa programaticamente o dict _TOH_FVS_AM do loader canônico e anota
cada mês com metadados de proveniência, estimativa, validação e proxy SIH.
"""

import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from qfeng.e5_symbolic.manaus_sih_loader import _TOH_FVS_AM  # noqa: E402

# ---------------------------------------------------------------------------
# Metadados de proveniência por mês (extraídos dos comentários do loader)
# ---------------------------------------------------------------------------
_METADATA: dict[tuple[int, int], dict] = {
    (2020,  7): {
        "source":            "FVS-AM/SES-AM",
        "source_doc":        "FVS-AM/SES-AM nota tecnica 07/ago/2020",
        "source_date":       "2020-08-07",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "49/165 leitos = 29.7%",
    },
    (2020,  8): {
        "source":            "FVS-AM",
        "source_doc":        "FVS-AM Boletim COVID-19 18/ago/2020",
        "source_date":       "2020-08-18",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "24.4% (58 pacientes UTI, pub+priv)",
    },
    (2020,  9): {
        "source":            "Fiocruz Observatorio Covid-19",
        "source_doc":        "Fiocruz Observatorio Covid-19 SE40-42",
        "source_date":       "2020-10-18",
        "is_estimated":      True,
        "estimation_method": "Fiocruz SE range (abaixo de 60%; estimado 45% interondas)",
        "raw_value_str":     "abaixo de 60% — estimado 45%",
    },
    (2020, 10): {
        "source":            "SUSAM/Amazonas Atual",
        "source_doc":        "SUSAM/Amazonas Atual 27/out/2020",
        "source_date":       "2020-10-27",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "~82% (80/223 leitos UTI)",
    },
    (2020, 11): {
        "source":            "Fiocruz Observatorio Covid-19",
        "source_doc":        "Fiocruz Observatorio SE48-49",
        "source_date":       "2020-12-07",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "76% em 7/dez (representativo nov)",
    },
    (2020, 12): {
        "source":            "SES-AM",
        "source_doc":        "SES-AM Plano Contingencia 3a fase",
        "source_date":       "2020-12-25",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     ">92% em 25/dez/2020",
    },
    (2021,  1): {
        "source":            "FVS-AM",
        "source_doc":        "FVS-AM Boletim COVID-19 16/jan/2021",
        "source_date":       "2021-01-16",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "103.69% UTI publica (colapso documentado)",
    },
    (2021,  2): {
        "source":            "SES-AM",
        "source_doc":        "SES-AM Nota Tecnica 04/fev/2021",
        "source_date":       "2021-02-04",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "366/379 UTI publicas adulto = 101%",
    },
    (2021,  3): {
        "source":            "Fiocruz Observatorio Covid-19",
        "source_doc":        "Fiocruz Observatorio 08/mar/2021",
        "source_date":       "2021-03-08",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "87% (zona critica)",
    },
    (2021,  4): {
        "source":            "FVS-AM",
        "source_doc":        "FVS-AM Boletim de Risco abr/2021",
        "source_date":       "2021-04-28",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "74.5% (19/abr) a 67.77% (28/abr) — media 71%",
    },
    (2021,  5): {
        "source":            "FVS-AM",
        "source_doc":        "FVS-AM Boletim de Risco mai/2021",
        "source_date":       "2021-05-31",
        "is_estimated":      False,
        "estimation_method": None,
        "raw_value_str":     "68.9-70.68% — media 70%",
    },
    (2021,  6): {
        "source":            "FVS-AM (estimado)",
        "source_doc":        "Estimado por interpolacao linear pos-pico mai/2021",
        "source_date":       "2021-06-30",
        "is_estimated":      True,
        "estimation_method": "linear_interpolation (queda progressiva pos-pico)",
        "raw_value_str":     "estimado ~70%",
    },
}

# ---------------------------------------------------------------------------
# Proxy SIH: proporção de internações com UTI_MES_TO > 0 por mês
# ---------------------------------------------------------------------------
SIH_PATH = PROJECT_ROOT / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"

def _compute_sih_proxy() -> dict[tuple[int, int], float | None]:
    if not SIH_PATH.exists():
        print(f"[WARN] SIH parquet nao encontrado em {SIH_PATH} — proxy sera None")
        return {}
    sih = pd.read_parquet(SIH_PATH)
    sih["ANO_CMPT"] = pd.to_numeric(sih["ANO_CMPT"], errors="coerce").fillna(0).astype(int)
    sih["MES_CMPT"] = pd.to_numeric(sih["MES_CMPT"], errors="coerce").fillna(0).astype(int)
    sih["UTI_MES_TO"] = pd.to_numeric(sih["UTI_MES_TO"], errors="coerce").fillna(0).astype(float)
    proxies: dict[tuple[int, int], float | None] = {}
    for (y, m) in _TOH_FVS_AM:
        mask = (sih["ANO_CMPT"] == y) & (sih["MES_CMPT"] == m)
        month_rows = sih[mask]
        if len(month_rows) == 0:
            proxies[(y, m)] = None
        else:
            pct_uti = (month_rows["UTI_MES_TO"] > 0).sum() / len(month_rows) * 100
            proxies[(y, m)] = round(float(pct_uti), 2)
    return proxies


# ---------------------------------------------------------------------------
# Diagnóstico t_mort=0
# ---------------------------------------------------------------------------
def _diagnose_t_mort(sih: pd.DataFrame | None) -> dict:
    if sih is None:
        return {"status": "sih_not_loaded"}
    if "MORTE" not in sih.columns:
        return {"status": "column_MORTE_absent"}
    sih_copy = sih.copy()
    if sih_copy["MORTE"].dtype == object:
        sih_copy["MORTE"] = (sih_copy["MORTE"].str.strip() == "Sim").astype(int)
    else:
        sih_copy["MORTE"] = pd.to_numeric(sih_copy["MORTE"], errors="coerce").fillna(0).astype(int)
    total = len(sih_copy)
    n_morte = int(sih_copy["MORTE"].sum())
    pct_morte = round(n_morte / total * 100, 2) if total > 0 else 0.0
    zeros_in_t_mort = int((sih_copy["MORTE"] == 0).sum())
    return {
        "total_rows": total,
        "n_morte_sim": n_morte,
        "pct_morte": pct_morte,
        "n_morte_zero": zeros_in_t_mort,
        "diagnosis": (
            "t_mort=0 BUG CONFIRMED: MORTE column all-zero (encoding error)"
            if n_morte == 0
            else f"OK: {n_morte}/{total} ({pct_morte}%) mortes registradas"
        ),
    }


# ---------------------------------------------------------------------------
# Construção do DataFrame
# ---------------------------------------------------------------------------
def build_toh_parquet(output_path: Path) -> pd.DataFrame:
    sih_proxy = _compute_sih_proxy()
    sih_df = pd.read_parquet(SIH_PATH) if SIH_PATH.exists() else None

    rows = []
    for (y, m), toh_pct in sorted(_TOH_FVS_AM.items()):
        meta = _METADATA[(y, m)]
        proxy = sih_proxy.get((y, m))
        delta_pp: float | None = None
        if proxy is not None:
            # tabnet_delta_pp: magnitude da diferença entre proxy SIH e TOH documentado
            # Negativo = proxy subestima; positivo = proxy superestima
            delta_pp = round(proxy - float(toh_pct), 2)

        rows.append({
            "year":              y,
            "month":             m,
            "competencia":       f"{y}-{m:02d}",
            "toh_uti_pct":       float(toh_pct),
            "source":            meta["source"],
            "source_doc":        meta["source_doc"],
            "source_date":       meta["source_date"],
            "is_estimated":      meta["is_estimated"],
            "estimation_method": meta["estimation_method"],
            "raw_value_str":     meta["raw_value_str"],
            "validation_status": "estimated" if meta["is_estimated"] else "confirmed",
            "tabnet_delta_pp":   delta_pp,
            "toh_sih_proxy_pct": proxy,
        })

    df = pd.DataFrame(rows)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    return df, sih_df


# ---------------------------------------------------------------------------
# Relatório de saída
# ---------------------------------------------------------------------------
def main() -> None:
    out_dir = PROJECT_ROOT / "data/predictors/manaus_bi"
    out_path = out_dir / "toh_uti_manaus.parquet"

    print("=== Tarefa 1.1 — TOH UTI Manaus ===")
    print(f"Fonte: {len(_TOH_FVS_AM)} meses importados de _TOH_FVS_AM")

    df, sih_df = build_toh_parquet(out_path)

    print(f"\nParquet salvo em: {out_path}")
    print(f"Linhas: {len(df)} | Colunas: {list(df.columns)}")
    print("\n--- TOH UTI por mes ---")
    for _, row in df.iterrows():
        est_flag = " [estimado]" if row["is_estimated"] else ""
        proxy_str = f"  proxy_SIH={row['toh_sih_proxy_pct']:.1f}% (delta={row['tabnet_delta_pp']:+.1f}pp)" if row["toh_sih_proxy_pct"] is not None else "  proxy_SIH=N/A"
        print(f"  {row['competencia']}: TOH={row['toh_uti_pct']:.0f}%{est_flag}{proxy_str}  [{row['source']}]")

    estimated_count = int(df["is_estimated"].sum())
    confirmed_count = len(df) - estimated_count
    print(f"\nValidacao: {confirmed_count} confirmados / {estimated_count} estimados")
    print("Meses estimados:", list(df[df["is_estimated"]]["competencia"]))

    # Diagnóstico t_mort=0
    print("\n--- Diagnóstico t_mort=0 ---")
    diag = _diagnose_t_mort(sih_df)
    for k, v in diag.items():
        print(f"  {k}: {v}")

    # Sanity check: TOH > 85 em jan/fev 2021
    jan21 = df[(df["year"] == 2021) & (df["month"] == 1)]["toh_uti_pct"].values
    feb21 = df[(df["year"] == 2021) & (df["month"] == 2)]["toh_uti_pct"].values
    assert len(jan21) == 1 and jan21[0] >= 85, f"FAIL: jan/2021 TOH={jan21}"
    assert len(feb21) == 1 and feb21[0] >= 85, f"FAIL: fev/2021 TOH={feb21}"
    print("\nSanity checks OK: jan/2021 >= 85% e fev/2021 >= 85%")
    print("Tarefa 1.1 CONCLUIDA.")


if __name__ == "__main__":
    main()
