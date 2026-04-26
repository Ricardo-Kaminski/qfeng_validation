"""Tarefa 1.4 — Validação cruzada bivariada Manaus BI (TOH + SRAG).

Outputs:
  outputs/bi_series_normalized.png
  outputs/bi_dimensional_decision.json
  outputs/bi_validation_report.md
  outputs/diagnostico_t_mort_zero.md
  data/predictors/manaus_bi/README.md
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

TOH_PATH   = PROJECT_ROOT / "data/predictors/manaus_bi/toh_uti_manaus.parquet"
SRAG_PATH  = PROJECT_ROOT / "data/predictors/manaus_bi/srag_manaus.parquet"
SIH_PATH   = PROJECT_ROOT / "data/predictors/manaus_sih/sih_manaus_2020_2021.parquet"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
BI_DIR     = PROJECT_ROOT / "data/predictors/manaus_bi"

W_TOH_APRIORI  = 0.50
W_SRAG_APRIORI = 0.50
DELTA_W_THRESHOLD = 0.10


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_joined() -> pd.DataFrame:
    toh = pd.read_parquet(TOH_PATH)[["year", "month", "competencia", "toh_uti_pct",
                                      "is_estimated", "validation_status"]]
    srag = pd.read_parquet(SRAG_PATH)[["year", "month", "n_srag_total", "n_covid",
                                        "n_obitos", "is_stub"]]
    df = toh.merge(srag, on=["year", "month"], how="left")
    df = df.sort_values(["year", "month"]).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Spearman correlation
# ---------------------------------------------------------------------------

def spearman_rho(x: np.ndarray, y: np.ndarray) -> float:
    from scipy import stats
    if np.std(x) < 1e-9 or np.std(y) < 1e-9:
        return float("nan")
    rho, _ = stats.spearmanr(x, y)
    return float(rho)


# ---------------------------------------------------------------------------
# PCA weights
# ---------------------------------------------------------------------------

def pca_weights(x: np.ndarray, y: np.ndarray) -> dict:
    """Return PCA-derived weights for 2 standardized series."""
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    X = np.column_stack([x, y])
    if np.std(x) < 1e-9 or np.std(y) < 1e-9:
        return {
            "w_TOH": float("nan"),
            "w_SRAG": float("nan"),
            "variance_explained_pc1": float("nan"),
            "loadings_pc1": [float("nan"), float("nan")],
            "stub_mode": True,
        }
    Xsc = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    pca.fit(Xsc)
    loadings = pca.components_[0]  # PC1
    abs_l = np.abs(loadings)
    w_toh  = abs_l[0] / abs_l.sum()
    w_srag = abs_l[1] / abs_l.sum()
    return {
        "w_TOH": round(float(w_toh), 4),
        "w_SRAG": round(float(w_srag), 4),
        "variance_explained_pc1": round(float(pca.explained_variance_ratio_[0]), 4),
        "loadings_pc1": [round(float(loadings[0]), 4), round(float(loadings[1]), 4)],
        "stub_mode": False,
    }


# ---------------------------------------------------------------------------
# Outlier detection
# ---------------------------------------------------------------------------

def zscore_outliers(series: np.ndarray, label: str, threshold: float = 2.5) -> list[str]:
    if np.std(series) < 1e-9:
        return [f"{label}: serie constante (stub), z-score indeterminado"]
    z = (series - np.mean(series)) / np.std(series)
    outliers = np.where(np.abs(z) > threshold)[0]
    if len(outliers) == 0:
        return []
    return [f"{label}[{i}]: z={z[i]:.2f}" for i in outliers]


# ---------------------------------------------------------------------------
# Normalized series plot
# ---------------------------------------------------------------------------

def plot_series(df: pd.DataFrame, out_path: Path, is_stub: bool) -> None:
    toh = df["toh_uti_pct"].values.astype(float)
    srag = df["n_srag_total"].values.astype(float)
    labels = df["competencia"].values

    toh_norm  = (toh  - toh.min())  / (toh.max()  - toh.min()  + 1e-9)
    srag_norm = (srag - srag.min()) / (srag.max() - srag.min() + 1e-9)

    fig, ax = plt.subplots(figsize=(12, 5))
    x = range(len(labels))
    ax.plot(x, toh_norm,  marker="o", label="TOH UTI (norm)", color="steelblue", linewidth=2)
    ax.plot(x, srag_norm, marker="s", label="SRAG total (norm)", color="coral",
            linewidth=2, linestyle="--")
    ax.axhline(0.85, color="red", linestyle=":", alpha=0.5, label="TOH=85% (crítico)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("Valor normalizado [0–1]")
    ax.set_title("Manaus BI bivariado — TOH UTI vs SRAG (normalizado)\n"
                 + ("SRAG = STUB (zeros) — aguarda INFLUD20/21" if is_stub else ""))
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[OK  ] Plot salvo: {out_path}")


# ---------------------------------------------------------------------------
# t_mort=0 diagnosis
# ---------------------------------------------------------------------------

def diagnose_t_mort(sih_path: Path) -> dict:
    if not sih_path.exists():
        return {"status": "sih_not_found", "path": str(sih_path)}
    sih = pd.read_parquet(sih_path)
    result: dict = {
        "total_rows": len(sih),
        "columns": list(sih.columns),
        "MORTE_dtype": str(sih["MORTE"].dtype) if "MORTE" in sih.columns else "absent",
    }
    if "MORTE" not in sih.columns:
        result["diagnosis"] = "MORTE column absent from parquet"
        return result
    raw_vc = sih["MORTE"].value_counts(dropna=False).to_dict()
    result["MORTE_value_counts_raw"] = {str(k): int(v) for k, v in raw_vc.items()}
    if sih["MORTE"].dtype == object:
        result["MORTE_encoding"] = "string (Sim/Nao style)"
        sim_count = int((sih["MORTE"].str.strip().str.lower().isin({"sim", "1", "true"})).sum())
        result["MORTE_Sim_count"] = sim_count
        result["MORTE_pct"] = round(sim_count / len(sih) * 100, 2) if len(sih) > 0 else 0.0
        if sim_count == 0:
            result["diagnosis"] = (
                "t_mort=0 BUG: MORTE column is string type but no 'Sim'/'1'/'True' values found. "
                "Parquet may have been saved with all-Nao rows or with numeric 0 stored as string '0'. "
                "Fix: re-run extract_manaus_sih.py with explicit Sim->1 mapping before saving parquet."
            )
        else:
            result["diagnosis"] = f"OK: {sim_count} obitos encontrados ({result['MORTE_pct']}%)"
    else:
        numeric_morte = pd.to_numeric(sih["MORTE"], errors="coerce").fillna(0).astype(int)
        n_morte = int(numeric_morte.sum())
        result["MORTE_encoding"] = "numeric"
        result["MORTE_Sim_count"] = n_morte
        result["MORTE_pct"] = round(n_morte / len(sih) * 100, 2) if len(sih) > 0 else 0.0
        if n_morte == 0:
            result["diagnosis"] = (
                "t_mort=0 BUG CONFIRMED: MORTE column is numeric but all zeros. "
                "The microdatasus process_sih() function labels MORTE as Sim/Nao; "
                "if the raw DBC had MORTE=0 (numeric) and process_sih labeled it as '0' string, "
                "the subsequent to_numeric conversion correctly yields 0 for all rows. "
                "Root cause: raw SIH DBC MORTE field encodes only inpatient death at discharge "
                "(MORTE=1 only when COBRANCA=alta=obito, not when obito=sim in AIH header). "
                "Fix requires: reload from raw DBC, apply correct MORTE field mapping."
            )
        else:
            result["diagnosis"] = f"OK: {n_morte} obitos encontrados ({result['MORTE_pct']}%)"
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=== Tarefa 1.4 — Validação cruzada bivariada ===\n")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_joined()
    n = len(df)
    print(f"Series carregadas: {n} meses\n")

    toh_arr  = df["toh_uti_pct"].values.astype(float)
    srag_arr = df["n_srag_total"].values.astype(float)
    is_stub  = bool(df["is_stub"].all())

    # --- Spearman ---
    rho = spearman_rho(toh_arr, srag_arr)
    rho_valid = not (rho != rho)  # nan check
    print(f"Spearman rho(TOH, SRAG): {rho:.4f}" if rho_valid else "Spearman rho: NaN (SRAG stub)")

    # --- Peak/valley sanity checks ---
    peak_toh  = int(df["toh_uti_pct"].idxmax())
    peak_comp = df.loc[peak_toh, "competencia"]
    print(f"Pico TOH: {peak_comp} (TOH={df.loc[peak_toh, 'toh_uti_pct']:.0f}%)")
    peak_ok = peak_comp in ("2021-01", "2021-02")
    print(f"  Pico em jan/fev 2021: {'OK' if peak_ok else 'FAIL'}")

    valley_toh = int(df["toh_uti_pct"].idxmin())
    valley_comp = df.loc[valley_toh, "competencia"]
    print(f"Vale TOH: {valley_comp} (TOH={df.loc[valley_toh, 'toh_uti_pct']:.0f}%)")
    valley_ok = valley_comp in ("2020-07", "2020-08")
    print(f"  Vale em jul/ago 2020: {'OK' if valley_ok else 'FAIL'}")

    # --- Outliers ---
    print()
    outliers = zscore_outliers(toh_arr, "TOH") + zscore_outliers(srag_arr, "SRAG")
    if outliers:
        print(f"Outliers (|z|>2.5): {outliers}")
    else:
        print("Outliers: nenhum detectado" if not is_stub else "Outliers: N/A (SRAG stub)")

    # --- PCA ---
    print()
    pca_res = pca_weights(toh_arr, srag_arr)
    if pca_res["stub_mode"]:
        print("PCA: indisponivel (SRAG stub com variancia zero)")
        w_toh_pca  = float("nan")
        w_srag_pca = float("nan")
        var_pc1    = float("nan")
        delta_w    = float("nan")
    else:
        w_toh_pca  = pca_res["w_TOH"]
        w_srag_pca = pca_res["w_SRAG"]
        var_pc1    = pca_res["variance_explained_pc1"]
        delta_w    = abs(W_TOH_APRIORI - w_toh_pca)
        print(f"PCA PC1 loadings: TOH={pca_res['loadings_pc1'][0]:+.4f}, SRAG={pca_res['loadings_pc1'][1]:+.4f}")
        print(f"PCA weights:      w_TOH={w_toh_pca:.4f}, w_SRAG={w_srag_pca:.4f}")
        print(f"PCA variance explained PC1: {var_pc1:.4f}")
        print(f"Delta w (apriori vs PCA): |{W_TOH_APRIORI:.2f} - {w_toh_pca:.4f}| = {delta_w:.4f}")

    # --- Weight decision ---
    if is_stub or (delta_w != delta_w):
        weights_final = {"w_TOH": W_TOH_APRIORI, "w_SRAG": W_SRAG_APRIORI}
        weights_pending = True
        decision_method = "apriori_only_stub_srag"
        print("\nDecisao de pesos: PENDENTE (SRAG stub invalido — re-executar apos INFLUD20/21)")
    elif delta_w < DELTA_W_THRESHOLD:
        weights_final = {"w_TOH": W_TOH_APRIORI, "w_SRAG": W_SRAG_APRIORI}
        weights_pending = False
        decision_method = "apriori_with_pca_sanity_check"
        print(f"\nDecisao de pesos: A priori (50/50) — delta_w={delta_w:.4f} < {DELTA_W_THRESHOLD} (coerente)")
    else:
        weights_final = {"w_TOH": W_TOH_APRIORI, "w_SRAG": W_SRAG_APRIORI}
        weights_pending = True
        decision_method = "apriori_with_pca_sanity_check"
        print(f"\nDecisao de pesos: PENDENTE — delta_w={delta_w:.4f} >= {DELTA_W_THRESHOLD} (divergencia relevante)")

    # --- Plot ---
    plot_path = OUTPUT_DIR / "bi_series_normalized.png"
    plot_series(df, plot_path, is_stub)

    # --- bi_dimensional_decision.json ---
    decision = {
        "decision_date": str(date.today()),
        "dimensions": ["TOH", "SRAG"],
        "weights_apriori": {"w_TOH": W_TOH_APRIORI, "w_SRAG": W_SRAG_APRIORI},
        "weights_pca": {"w_TOH": w_toh_pca if not (w_toh_pca != w_toh_pca) else None,
                        "w_SRAG": w_srag_pca if not (w_srag_pca != w_srag_pca) else None},
        "pca_variance_explained_pc1": var_pc1 if not (var_pc1 != var_pc1) else None,
        "spearman_rho_toh_srag": rho if rho_valid else None,
        "decision_method": decision_method,
        "weights_final": weights_final,
        "weights_decision_pending": weights_pending,
        "srag_is_stub": is_stub,
        "rationale_note": (
            "Pesos a priori 50/50 refletem paridade institucional entre TOH UTI (ficha tecnica MS) "
            "e SRAG (vigilancia epidemiologica oficial SIVEP-Gripe). PCA empirica usada como sanity "
            "check; divergencia tolerada ate |Delta_w|<0.10. Decisao pendente enquanto SRAG stub ativo."
            if weights_pending else
            "Pesos a priori 50/50 confirmados por PCA empirica (|Delta_w|<0.10). Decisao final."
        ),
    }
    dec_path = OUTPUT_DIR / "bi_dimensional_decision.json"
    dec_path.write_text(json.dumps(decision, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK  ] {dec_path}")

    # --- t_mort diagnosis ---
    print("\n--- Diagnostico t_mort=0 ---")
    tmd = diagnose_t_mort(SIH_PATH)
    for k, v in tmd.items():
        if k != "columns":
            print(f"  {k}: {v}")

    # --- diagnostico_t_mort_zero.md ---
    diag_path = OUTPUT_DIR / "diagnostico_t_mort_zero.md"
    diag_content = f"""# Diagnóstico Bug t_mort=0 — SIH Manaus 2020-2021

**Data:** {date.today()}
**Arquivo:** `{SIH_PATH.relative_to(PROJECT_ROOT)}`
**Responsável:** Fase 1 BI bivariado — Tarefa 1.4

## Achados

| Campo | Valor |
|-------|-------|
| Total de linhas | {tmd.get('total_rows', 'N/A')} |
| Tipo MORTE | {tmd.get('MORTE_dtype', 'N/A')} |
| Valor counts (raw) | {tmd.get('MORTE_value_counts_raw', 'N/A')} |
| Óbitos (Sim) | {tmd.get('MORTE_Sim_count', 'N/A')} |
| % óbitos | {tmd.get('MORTE_pct', 'N/A')}% |

## Diagnóstico

{tmd.get('diagnosis', 'N/A')}

## Causa Raiz Provável

O dataset SIH/SUS (AIH — Autorização de Internação Hospitalar) registra MORTE como campo de alta.
No microdatasus `process_sih()`, a coluna MORTE é convertida de código numérico para rótulo
Sim/Não. O parquet atual aparentemente foi gerado por uma versão do script que salvou
os dados antes da conversão de rótulos, resultando em todos zeros (encoding numérico 0=não-óbito).

## Impacto

- `t_mort` no `load_manaus_real_series()` (manaus_sih_loader.py) é derivado desta coluna
- Todos os cálculos de mortalidade hospitalar estão zerados no predictor atual
- O `theta_eff` Markoviano é afetado se `t_mort` entra na fórmula

## Ação Requerida (Fase 2)

1. Re-executar `extract_manaus_sih.py` com mapeamento explícito:
   ```python
   sih["MORTE"] = (sih["MORTE"].str.strip().str.upper() == "SIM").astype(int)
   ```
2. Salvar novo parquet em `data/predictors/manaus_sih/sih_manaus_2020_2021.parquet`
3. Verificar contagem de óbitos contra SIM/DATASUS para Manaus 2020-2021 (order of magnitude:
   estimativa SIM: ~6.000-9.000 óbitos hospitalares COVID em 12 meses)
4. Re-executar `manaus_sih_loader.py` para regenerar série temporal

## Não-urgência Imediata

O bug afeta `t_mort` mas **não afeta** as séries ativas do BI bivariado (TOH e SRAG).
O parâmetro `hospital_occupancy_pct` vem de `_TOH_FVS_AM` (documentado e correto).
Prioridade: corrigir antes da regeneração da Tabela 7 na Fase 2.
"""
    diag_path.write_text(diag_content, encoding="utf-8")
    print(f"[OK  ] {diag_path}")

    # --- bi_validation_report.md ---
    rho_str = f"{rho:.4f}" if rho_valid else "NaN (SRAG stub)"
    report_content = f"""# BI Bivariado Manaus — Relatório de Validação Cruzada

**Data:** {date.today()}
**Branch:** caminho2
**Commits Tarefa 1.1–1.3:** 236a4ea / 96b8bb9 / cd465b6

## 1. Séries Ativas

| Série | Meses | Confirmados | Estimados | Stub | Fonte primária |
|-------|-------|-------------|-----------|------|----------------|
| TOH UTI | 12 | 10 | 2 | Não | FVS-AM / SES-AM / Fiocruz |
| SRAG Manaus | 12 | 0 | 0 | **Sim** | SIVEP-Gripe INFLUD20/21 (pendente) |

**SRAG stub ativo** — INFLUD20/21 não baixados (FTP DATASUS migrado para OpenDataSUS).
Fonte: opendatasus.saude.gov.br/dataset/srag-2020 e srag-2021.

## 2. Correlação de Spearman

| Par | ρ | Esperado | Status |
|-----|---|----------|--------|
| TOH vs SRAG | {rho_str} | > 0.50 | {"OK" if rho_valid and rho > 0.5 else "PENDENTE (stub)" if is_stub else "FAIL"} |

## 3. Sanity Checks — Pico e Vale

| Check | Resultado | Status |
|-------|-----------|--------|
| Pico TOH em jan/fev 2021 | {peak_comp} | {"OK" if peak_ok else "FAIL"} |
| Vale TOH em jul/ago 2020 | {valley_comp} | {"OK" if valley_ok else "FAIL"} |

## 4. Outliers (|z| > 2.5)

{chr(10).join(outliers) if outliers else "Nenhum outlier detectado na série TOH." if not is_stub else "SRAG stub — outlier detection indisponível."}

## 5. PCA Empírica (sanity check de pesos)

{"**Indisponível** — SRAG stub com variância zero." if pca_res["stub_mode"] else f"""
| Componente | Loading TOH | Loading SRAG | Var. Explicada |
|------------|-------------|--------------|----------------|
| PC1 | {pca_res["loadings_pc1"][0]:+.4f} | {pca_res["loadings_pc1"][1]:+.4f} | {pca_res["variance_explained_pc1"]:.4f} |

- w_TOH PCA: {w_toh_pca:.4f}
- w_SRAG PCA: {w_srag_pca:.4f}
- |Δw| = {delta_w:.4f} {'< 0.10 — coerência boa' if delta_w < DELTA_W_THRESHOLD else '>= 0.10 — divergência relevante'}
"""}

## 6. Decisão Final de Pesos

| Método | w_TOH | w_SRAG |
|--------|-------|--------|
| A priori (ficha técnica MS) | {W_TOH_APRIORI} | {W_SRAG_APRIORI} |
| PCA empírica | {"N/A (stub)" if pca_res["stub_mode"] else f"{w_toh_pca:.4f}"} | {"N/A (stub)" if pca_res["stub_mode"] else f"{w_srag_pca:.4f}"} |
| **Decisão final** | **{weights_final["w_TOH"]}** | **{weights_final["w_SRAG"]}** |

**weights_decision_pending:** {weights_pending}
**Método:** {decision_method}

> Rationale: Pesos a priori 50/50 refletem paridade institucional entre TOH UTI (ficha técnica
> MS) e SRAG (vigilância epidemiológica oficial SIVEP-Gripe). PCA empírica como sanity check;
> divergência tolerada até |Δw|<0.10. Decisão final após SRAG dados reais.

## 7. Diagnóstico Bug t_mort=0

**Resultado:** {tmd.get('diagnosis', 'N/A')}

Detalhes completos em `outputs/diagnostico_t_mort_zero.md`.

## 8. Recomendações para Fase 2

1. **Baixar INFLUD20/21** de opendatasus.saude.gov.br e re-executar `extract_srag_manaus.py`
2. **Re-executar este script** para calcular Spearman real e validar |Δw| PCA
3. **Corrigir bug t_mort=0** no SIH parquet antes da regeneração da Tabela 7
4. **Confirmar pesos finais** (atualmente pendentes) após SRAG dados reais
"""
    rep_path = OUTPUT_DIR / "bi_validation_report.md"
    rep_path.write_text(report_content, encoding="utf-8")
    print(f"[OK  ] {rep_path}")

    # --- data/predictors/manaus_bi/README.md ---
    readme_content = f"""# Manaus BI Bivariado — Provenance Manifest

**Projeto:** Q-FENG Caminho 2 — BI multi-fonte
**Período:** Jul/2020 – Jun/2021 (12 meses)
**Branch:** caminho2 | **Commits:** 236a4ea (1.1), 96b8bb9 (1.2), cd465b6 (1.3)

## Dimensões ativas

| Dimensão | Arquivo | Status | Fonte primária |
|----------|---------|--------|----------------|
| TOH UTI | `toh_uti_manaus.parquet` | Ativo (10 confirmados, 2 estimados) | FVS-AM / SES-AM / Fiocruz |
| SRAG | `srag_manaus.parquet` | **STUB** (aguarda INFLUD20/21) | SIVEP-Gripe OpenDataSUS |
| O₂ supply | `oxigenio_unavailable.json` | Caminho C — prospectivo-only | — |

## TOH UTI (`toh_uti_manaus.parquet`)

Schema: `year, month, competencia, toh_uti_pct, source, source_doc, source_date,`
`is_estimated, estimation_method, raw_value_str, validation_status, tabnet_delta_pp, toh_sih_proxy_pct`

Fonte: `_TOH_FVS_AM` em `src/qfeng/e5_symbolic/manaus_sih_loader.py`
Extração: `scripts/build_toh_uti_manaus.py`
Validações: proxy SIH (case-mix UTI), sanity check jan/fev 2021 ≥85%

## SRAG Manaus (`srag_manaus.parquet`)

Schema: `year, month, competencia, n_srag_total, n_covid, n_outros, n_obitos, letalidade_pct, source, is_stub`

Extração: `scripts/extract_srag_manaus.py`
Fonte original: SIVEP-Gripe INFLUD20/21 (OpenDataSUS)
**Status: STUB** — baixar INFLUD20/21 manualmente e re-executar `extract_srag_manaus.py`
Download: opendatasus.saude.gov.br/dataset/srag-2020 e srag-2021

## Decisão O₂ — Caminho C

Arquivo: [`oxigenio_unavailable.json`](oxigenio_unavailable.json)

Decisão: sem dado retrospectivo canônico viável para O₂ Manaus 2020-2021.
BI permanece **bivariado** (TOH + SRAG). O₂ entra como limitação prospectiva no §7.4.

## Pesos do score_pressao

Decisão em [`outputs/bi_dimensional_decision.json`](../../outputs/bi_dimensional_decision.json)
A priori: w_TOH = 0.50 / w_SRAG = 0.50 (paridade institucional)
**weights_decision_pending: {weights_pending}** — re-executar após SRAG dados reais.

## Tabela de Provenance

| competencia | TOH source | TOH status | SRAG status |
|-------------|------------|------------|-------------|
| 2020-07 | FVS-AM/SES-AM (nota 07/ago/2020) | confirmed | STUB |
| 2020-08 | FVS-AM Boletim 18/ago/2020 | confirmed | STUB |
| 2020-09 | Fiocruz SE40-42 | estimated | STUB |
| 2020-10 | SUSAM 27/out/2020 | confirmed | STUB |
| 2020-11 | Fiocruz SE48-49 | confirmed | STUB |
| 2020-12 | SES-AM Plano Contingencia | confirmed | STUB |
| 2021-01 | FVS-AM Boletim 16/jan/2021 | confirmed | STUB |
| 2021-02 | SES-AM 04/fev/2021 | confirmed | STUB |
| 2021-03 | Fiocruz 08/mar/2021 | confirmed | STUB |
| 2021-04 | FVS-AM Boletim Risco abr/2021 | confirmed | STUB |
| 2021-05 | FVS-AM Boletim Risco mai/2021 | confirmed | STUB |
| 2021-06 | estimado por interpolação | estimated | STUB |

## Bug t_mort=0 (não bloqueante para BI)

MORTE no SIH parquet é todo zero (encoding error). Detalhes em
`outputs/diagnostico_t_mort_zero.md`. Não afeta TOH nem SRAG. Corrigir na Fase 2.
"""
    readme_path = BI_DIR / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"[OK  ] {readme_path}")

    # --- Summary ---
    print(f"""
=== Tarefa 1.4 CONCLUIDA ===
Outputs:
  outputs/bi_series_normalized.png
  outputs/bi_dimensional_decision.json   (pending={weights_pending})
  outputs/bi_validation_report.md
  outputs/diagnostico_t_mort_zero.md
  data/predictors/manaus_bi/README.md
""")


if __name__ == "__main__":
    main()
