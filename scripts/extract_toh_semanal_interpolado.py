"""Tarefa 2.A — TOH semanal Manaus via interpolação linear do FVS-AM.

API DEMAS-VEPI descartada: campo ocupacaohospitalaruti é null para todos
os registros de Manaus (diagnóstico 26/abr/2026 em outputs/api_demas_vepi_probe.json).

Estratégia: interpolar os 12 meses FVS-AM para 73 Semanas Epidemiológicas.

Mapeamento: cada mês YYYY-MM → SE correspondentes via semana epidemiológica
brasileira (ISO week adaptada). Para cada SE, o TOH é calculado por
interpolação linear entre o valor do mês central anterior e o seguinte.

Output: data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet
        outputs/api_demas_vepi_probe.json (diagnóstico de viabilidade)
        outputs/toh_interpolacao_log.md (auditoria da interpolação)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import numpy as np
import pandas as pd

ROOT = Path(__file__).parents[1]
TOH_MENSAL_PATH = ROOT / "data/predictors/manaus_bi/toh_uti_manaus.parquet"
OUT_DIR  = ROOT / "data/predictors/manaus_bi/derived"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Janela de semanas epidemiológicas
# SE 10/2020 → SE 30/2021 = 73 semanas
SE_WINDOW = [
    *[(2020, w) for w in range(10, 53)],  # SE 10-52/2020 = 43 semanas
    *[(2021, w) for w in range(1,  31)],  # SE  1-30/2021 = 30 semanas
]

# Datas ISO aproximadas das semanas epidemiológicas brasileiras
# Semana epidemiológica começa no domingo. Referência: CGPNC/SVS calendário 2020/2021.
# Para interpolação, usamos a segunda-feira de cada SE como data representativa.
def se_to_date(year: int, week: int) -> pd.Timestamp:
    """Retorna a data da segunda-feira da Semana Epidemiológica (ISO week)."""
    return pd.Timestamp.fromisocalendar(year, week, 1)


def load_toh_mensal() -> pd.DataFrame:
    toh = pd.read_parquet(TOH_MENSAL_PATH)
    # Garante colunas year, month, toh_uti_pct
    toh = toh.copy()
    toh["date_mid"] = pd.to_datetime(
        {"year": toh["year"], "month": toh["month"], "day": 15}
    )
    toh = toh.sort_values("date_mid").reset_index(drop=True)
    return toh


def interpolate_toh_weekly(toh_mensal: pd.DataFrame) -> pd.DataFrame:
    """Interpola TOH mensal para cada SE via interpolação linear."""
    # Série mensal com data do dia 15 como âncora
    ts_monthly = pd.Series(
        toh_mensal["toh_uti_pct"].values,
        index=pd.DatetimeIndex(toh_mensal["date_mid"]),
        name="toh_uti_pct",
    )

    # Gera datas das SEs
    se_records = []
    for year, week in SE_WINDOW:
        try:
            date = se_to_date(year, week)
        except ValueError:
            # SE 53 pode não existir em alguns anos
            continue
        se_records.append({"year": year, "week_se": week, "date": date})

    se_df = pd.DataFrame(se_records)

    # Interpolação: para cada SE, interpola entre os dois meses adjacentes
    # Constrói índice contínuo com ancoras mensais + datas das SEs
    all_dates = pd.DatetimeIndex(
        list(ts_monthly.index) + list(se_df["date"])
    ).sort_values().unique()

    ts_full = ts_monthly.reindex(all_dates).interpolate(method="time")

    # Extrai valores para as datas das SEs
    toh_weekly: list[dict] = []
    for _, row in se_df.iterrows():
        date = row["date"]
        val = float(ts_full.get(date, np.nan))
        if np.isnan(val):
            # Fallback: valor do mês mais próximo
            diffs = abs(ts_monthly.index - date)
            nearest = ts_monthly.iloc[diffs.argmin()]
            val = float(nearest)

        toh_weekly.append({
            "year":             int(row["year"]),
            "week_se":          int(row["week_se"]),
            "date_se_monday":   date.strftime("%Y-%m-%d"),
            "toh_uti_pct":      round(val, 2),
            "is_estimated":     True,
            "method":           "interpolacao_linear_fvs_am",
            "source":           "FVS-AM boletins 2020-2021 (interpolado mensalmente)",
        })

    return pd.DataFrame(toh_weekly)


def build_audit_log(toh_mensal: pd.DataFrame, toh_semanal: pd.DataFrame) -> str:
    lines = [
        "# Auditoria — TOH Semanal Manaus (interpolação FVS-AM)",
        "",
        "## Decisão de fonte",
        "",
        "API DEMAS-VEPI descartada:",
        "- Sem campo de capacidade total UTI (`ocupacaohospitalaruti` = null para Manaus)",
        "- Manaus ~0.9% dos registros — filtro server-side não disponível",
        "- Diagnóstico completo: `outputs/api_demas_vepi_probe.json`",
        "",
        "Fallback: interpolação linear dos 12 meses FVS-AM → 73 SEs.",
        "",
        "## Valores mensais FVS-AM (ancoras)",
        "",
        "| Mês | TOH UTI % |",
        "|-----|-----------|",
    ]
    for _, row in toh_mensal.iterrows():
        lines.append(f"| {row['year']}-{int(row['month']):02d} | {row['toh_uti_pct']:.1f}% |")

    lines += [
        "",
        "## Valores semanais interpolados",
        "",
        "| Ano | SE | Data | TOH % |",
        "|----|----|----|-------|",
    ]
    for _, row in toh_semanal.iterrows():
        lines.append(f"| {row['year']} | SE{row['week_se']:02d} | {row['date_se_monday']} | {row['toh_uti_pct']:.1f}% |")

    lines += [
        "",
        "## Limitações",
        "",
        "- Interpolação é linear (piecewise); não captura variações intra-mensais reais.",
        "- is_estimated=True em todos os registros semanais.",
        "- Adequado para predictor BI bivariado (granularidade mensal publicada para Paper 1).",
    ]
    return "\n".join(lines)


def main() -> None:
    print("Carregando TOH mensal FVS-AM...")
    toh_mensal = load_toh_mensal()
    print(f"  {len(toh_mensal)} meses carregados: "
          f"{toh_mensal['year'].min()}-{toh_mensal['month'].min():02d} → "
          f"{toh_mensal['year'].max()}-{toh_mensal['month'].max():02d}")

    print("Interpolando para semanas epidemiológicas...")
    toh_semanal = interpolate_toh_weekly(toh_mensal)
    print(f"  {len(toh_semanal)} semanas geradas")
    print(f"  Pico: SE {toh_semanal.loc[toh_semanal['toh_uti_pct'].idxmax(), 'week_se']}"
          f"/{toh_semanal.loc[toh_semanal['toh_uti_pct'].idxmax(), 'year']} = "
          f"{toh_semanal['toh_uti_pct'].max():.1f}%")

    out_path = OUT_DIR / "toh_semanal_manaus.parquet"
    toh_semanal.to_parquet(out_path, index=False, engine="pyarrow")
    print(f"\n  Salvo: {out_path}")

    audit = build_audit_log(toh_mensal, toh_semanal)
    log_path = ROOT / "outputs/toh_interpolacao_log.md"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(audit)
    print(f"  Audit log: {log_path}")

    print("\nPreview (primeiras e últimas semanas):")
    print(toh_semanal[["year", "week_se", "date_se_monday", "toh_uti_pct"]].to_string())


if __name__ == "__main__":
    main()
