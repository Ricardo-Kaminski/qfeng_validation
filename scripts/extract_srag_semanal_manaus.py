"""Tarefa 2.B — SRAG semanal Manaus nativo (SIVEP-Gripe INFLUD20/21).

Extrai casos de SRAG por Semana Epidemiológica (SE) para Manaus
a partir dos arquivos INFLUD20/21 locais (dados brutos SIVEP-Gripe).

Filtros aplicados:
  - CO_MUN_RES == "130260"  (residentes de Manaus)
  - INFLUD20: SEM_NOT in 10..52  (SE 10/2020 → SE 52/2020)
  - INFLUD21: SEM_NOT in  1..30  (SE  1/2021 → SE 30/2021)

Agrega por (year, week_se):
  n_srag_total  = todos os casos SRAG Manaus na SE
  n_covid       = CLASSI_FIN == 5 (COVID-19 confirmado)
  n_outros      = CLASSI_FIN in {1,2,3,4} (outros agentes)
  n_sem_class   = sem classificação final
  n_obitos      = EVOLUCAO == 2 (todos SRAG)
  n_obitos_covid= EVOLUCAO == 2 AND CLASSI_FIN == 5

Output: data/predictors/manaus_bi/derived/srag_semanal_manaus.parquet
        outputs/source_manifest_srag.json
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd

# Paths
ROOT = Path(__file__).parents[1]
RAW_DIR = ROOT / "data/predictors/manaus_bi/raw/srag_manaus_sivep"
OUT_DIR  = ROOT / "data/predictors/manaus_bi/derived"
OUT_DIR.mkdir(parents=True, exist_ok=True)

INFLUD20 = RAW_DIR / "INFLUD20-23-03-2026.csv"
INFLUD21 = RAW_DIR / "INFLUD21-23-03-2026.csv"

MANAUS_CODE = "130260"

# Week windows (SEM_NOT is week-of-year, 1-52, no year prefix)
WINDOW = {
    2020: (10, 52),
    2021: ( 1, 30),
}

COLS_NEEDED = ["CO_MUN_RES", "SEM_NOT", "CLASSI_FIN", "EVOLUCAO"]
CHUNKSIZE = 100_000


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def _extract_one_file(path: Path, year: int) -> pd.DataFrame:
    """Lê INFLUD em chunks, filtra Manaus + janela SE, retorna DataFrame."""
    se_min, se_max = WINDOW[year]
    rows: list[dict] = []

    total_read = 0
    manaus_found = 0

    for chunk in pd.read_csv(
        path,
        sep=";",
        encoding="latin-1",
        dtype=str,
        usecols=COLS_NEEDED,
        chunksize=CHUNKSIZE,
        on_bad_lines="skip",
    ):
        total_read += len(chunk)

        # Normaliza
        chunk["CO_MUN_RES"] = chunk["CO_MUN_RES"].str.strip()
        chunk["SEM_NOT"]    = pd.to_numeric(chunk["SEM_NOT"], errors="coerce")
        chunk["CLASSI_FIN"] = pd.to_numeric(chunk["CLASSI_FIN"], errors="coerce")
        chunk["EVOLUCAO"]   = pd.to_numeric(chunk["EVOLUCAO"], errors="coerce")

        # Filtro primário: Manaus
        mask_mun = chunk["CO_MUN_RES"] == MANAUS_CODE
        sub = chunk[mask_mun].copy()
        manaus_found += len(sub)

        # Filtro temporal
        sub = sub[(sub["SEM_NOT"] >= se_min) & (sub["SEM_NOT"] <= se_max)]

        rows.append(sub)

        if total_read % 500_000 == 0:
            print(f"  {path.name}: {total_read:,} rows lidas, {manaus_found:,} Manaus até agora",
                  flush=True)

    print(f"  {path.name}: total {total_read:,} rows | Manaus na janela SE: "
          f"{sum(len(r) for r in rows):,}")

    if not rows:
        return pd.DataFrame(columns=COLS_NEEDED)
    return pd.concat(rows, ignore_index=True)


def _aggregate(df: pd.DataFrame, year: int) -> list[dict]:
    """Agrega por semana epidemiológica."""
    se_min, se_max = WINDOW[year]
    result = []
    for week in range(se_min, se_max + 1):
        wdf = df[df["SEM_NOT"] == week]
        n_total  = len(wdf)
        n_covid  = int((wdf["CLASSI_FIN"] == 5).sum())
        n_outros = int(wdf["CLASSI_FIN"].isin([1, 2, 3, 4]).sum())
        n_sem    = int(wdf["CLASSI_FIN"].isna().sum())
        n_obit   = int((wdf["EVOLUCAO"] == 2).sum())
        n_obit_c = int(((wdf["CLASSI_FIN"] == 5) & (wdf["EVOLUCAO"] == 2)).sum())
        result.append({
            "year":           year,
            "week_se":        week,
            "n_srag_total":   n_total,
            "n_covid":        n_covid,
            "n_outros":       n_outros,
            "n_sem_class":    n_sem,
            "n_obitos":       n_obit,
            "n_obitos_covid": n_obit_c,
            "letalidade_pct": round(n_obit / max(n_total, 1) * 100, 2),
            "source":         "SIVEP-Gripe INFLUD CO_MUN_RES=130260",
            "is_stub":        False,
        })
    return result


def main() -> None:
    all_rows: list[dict] = []

    for path, year in [(INFLUD20, 2020), (INFLUD21, 2021)]:
        print(f"\n=== {path.name} (ano {year}) ===")
        df = _extract_one_file(path, year)
        rows = _aggregate(df, year)
        all_rows.extend(rows)
        total_covid = sum(r["n_covid"] for r in rows)
        total_obitos = sum(r["n_obitos"] for r in rows)
        print(f"  SEs geradas: {len(rows)} | n_covid total: {total_covid} | "
              f"n_obitos: {total_obitos}")

    out = pd.DataFrame(all_rows)
    out_path = OUT_DIR / "srag_semanal_manaus.parquet"
    out.to_parquet(out_path, index=False, engine="pyarrow")
    print(f"\n✅ {out_path} — {len(out)} semanas, {out['n_covid'].sum()} casos COVID")
    print(out[["year", "week_se", "n_srag_total", "n_covid", "n_obitos", "is_stub"]].to_string())

    # Manifest com SHA256
    manifest = {
        "generated_at": pd.Timestamp.now().isoformat(),
        "output_file": str(out_path.relative_to(ROOT)),
        "total_semanas": len(out),
        "total_covid": int(out["n_covid"].sum()),
        "total_obitos": int(out["n_obitos"].sum()),
        "sources": [
            {
                "file": INFLUD20.name,
                "year": 2020,
                "se_window": list(WINDOW[2020]),
                "sha256": _sha256(INFLUD20),
                "size_bytes": INFLUD20.stat().st_size,
            },
            {
                "file": INFLUD21.name,
                "year": 2021,
                "se_window": list(WINDOW[2021]),
                "sha256": _sha256(INFLUD21),
                "size_bytes": INFLUD21.stat().st_size,
            },
        ],
        "filter": "CO_MUN_RES=130260 (Manaus)",
        "is_stub": False,
    }
    manifest_path = ROOT / "outputs/source_manifest_srag.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
