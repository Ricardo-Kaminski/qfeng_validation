"""Tarefa 2.C — Revalidacao cruzada bivariada semanal TOH x SRAG.

Inputs:
  data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet (73 SEs)
  data/predictors/manaus_bi/derived/srag_semanal_manaus.parquet (73 SEs)

Analises:
  1. Spearman rho: TOH x n_covid, TOH x n_obitos, TOH x taxa_crescimento_covid
  2. PCA 2D normalizado: variancia explicada por componente
  3. Decisao de pesos: |delta_w| < 0.10 -> pca_validated; else pca_divergent
  4. Deteccao de lag: correlacao com offset de 1-4 semanas
  5. Relatorio em outputs/relatorio_validacao_semanal.md

Output principal:
  outputs/bi_dimensional_decision_semanal.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).parents[1]
DERIVED = ROOT / "data/predictors/manaus_bi/derived"

APRIORI_TOH  = 0.50
APRIORI_SRAG = 0.50
DELTA_THRESHOLD = 0.10


def load_data() -> pd.DataFrame:
    toh  = pd.read_parquet(DERIVED / "toh_semanal_manaus.parquet")
    srag = pd.read_parquet(DERIVED / "srag_semanal_manaus.parquet")

    merged = toh.merge(srag, on=["year", "week_se"], suffixes=("_toh", "_srag"))

    # Taxa de crescimento semanal de COVID (%)
    merged = merged.sort_values(["year", "week_se"]).reset_index(drop=True)
    merged["covid_prev"] = merged["n_covid"].shift(1).fillna(1)
    merged["covid_growth"] = ((merged["n_covid"] - merged["covid_prev"]) /
                              merged["covid_prev"].clip(lower=1) * 100)

    return merged


def spearman_analysis(df: pd.DataFrame) -> dict:
    """Spearman rho entre TOH e tres indicadores SRAG."""
    results = {}
    pairs = [
        ("n_covid",    "Casos COVID"),
        ("n_obitos",   "Obitos SRAG"),
        ("covid_growth","Taxa crescimento COVID (%)"),
    ]
    for col, label in pairs:
        rho, pval = stats.spearmanr(df["toh_uti_pct"], df[col], nan_policy="omit")
        results[col] = {
            "label":   label,
            "rho":     round(float(rho),  4),
            "pval":    round(float(pval), 4),
            "signif":  pval < 0.05,
        }
        print(f"  Spearman rho(TOH, {label}): {rho:+.4f}  p={pval:.4f}"
              f"  {'*' if pval < 0.05 else ''}")
    return results


def spearman_lag(df: pd.DataFrame, max_lag: int = 4) -> dict:
    """Rho com diferentes lags (semanas de atraso TOH -> SRAG)."""
    lags = {}
    for lag in range(0, max_lag + 1):
        toh_lagged = df["toh_uti_pct"].shift(lag)
        mask = toh_lagged.notna()
        rho, pval = stats.spearmanr(toh_lagged[mask], df["n_covid"][mask])
        lags[f"lag_{lag}"] = {"rho": round(float(rho), 4), "pval": round(float(pval), 4)}
        print(f"  lag={lag:+d} semanas: rho={rho:+.4f}  p={pval:.4f}")
    return lags


def pca_analysis(df: pd.DataFrame) -> dict:
    """PCA 2D normalizado sobre TOH e n_covid."""
    X = df[["toh_uti_pct", "n_covid"]].dropna().values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    pca.fit(X_scaled)

    loadings = pca.components_  # shape (2, 2)
    var_exp   = pca.explained_variance_ratio_

    pc1_toh_loading  = abs(loadings[0, 0])
    pc1_srag_loading = abs(loadings[0, 1])
    total = pc1_toh_loading + pc1_srag_loading

    w_toh  = round(pc1_toh_loading  / total, 4)
    w_srag = round(pc1_srag_loading / total, 4)

    delta_toh  = abs(w_toh  - APRIORI_TOH)
    delta_srag = abs(w_srag - APRIORI_SRAG)

    print(f"  PC1 variancia explicada: {var_exp[0]:.1%}")
    print(f"  PC1 loadings: TOH={loadings[0,0]:+.4f}  SRAG={loadings[0,1]:+.4f}")
    print(f"  Pesos PCA: TOH={w_toh:.4f}  SRAG={w_srag:.4f}")
    print(f"  Delta vs apriori 50/50: |dTOH|={delta_toh:.4f}  |dSRAG|={delta_srag:.4f}")

    return {
        "pc1_var_explained":  round(float(var_exp[0]), 4),
        "pc2_var_explained":  round(float(var_exp[1]), 4),
        "pc1_loading_toh":    round(float(loadings[0, 0]), 4),
        "pc1_loading_srag":   round(float(loadings[0, 1]), 4),
        "w_toh_pca":          w_toh,
        "w_srag_pca":         w_srag,
        "delta_toh":          round(delta_toh, 4),
        "delta_srag":         round(delta_srag, 4),
    }


def weight_decision(pca_res: dict) -> dict:
    delta_toh  = pca_res["delta_toh"]
    delta_srag = pca_res["delta_srag"]
    max_delta  = max(delta_toh, delta_srag)

    if max_delta < DELTA_THRESHOLD:
        method = "pca_validated"
        w_toh  = pca_res["w_toh_pca"]
        w_srag = pca_res["w_srag_pca"]
        note = ("PCA confirma pesos proximos ao apriori 50/50. "
                "Diferenca max={:.4f} < {:.2f}.").format(max_delta, DELTA_THRESHOLD)
    else:
        method = "pca_divergent_pending_author"
        w_toh  = APRIORI_TOH
        w_srag = APRIORI_SRAG
        note = ("PCA sugere pesos diferentes do apriori (delta_max={:.4f} >= {:.2f}). "
                "Mantido 50/50 apriori ate decisao do autor.").format(max_delta, DELTA_THRESHOLD)

    print(f"  Decisao: {method}")
    print(f"  Pesos finais: TOH={w_toh:.4f}  SRAG={w_srag:.4f}")
    return {
        "decision_method":     method,
        "w_toh":               w_toh,
        "w_srag":              w_srag,
        "weights_decision_pending": method != "pca_validated",
        "note":                note,
    }


def build_report(df: pd.DataFrame, spearman: dict, lag: dict,
                 pca_res: dict, decision: dict) -> str:
    lines = [
        "# Relatorio Validacao Cruzada Bivariada Semanal",
        "",
        "**Branch:** caminho2  ",
        "**Data:** 2026-04-26  ",
        "**Granularidade:** Semana Epidemiologica (SE)  ",
        "",
        "## 1. Dataset",
        "",
        f"- Semanas: {len(df)} (SE 10/2020 - SE 30/2021)",
        f"- TOH: interpolado FVS-AM mensal (is_estimated=True para todas SEs)",
        f"- SRAG: SIVEP-Gripe INFLUD20/21, CO_MUN_RES=130260, is_stub=False",
        f"- n_covid total: {int(df['n_covid'].sum())}",
        f"- n_obitos total: {int(df['n_obitos'].sum())}",
        "",
        "## 2. Correlacao de Spearman (TOH x SRAG)",
        "",
        "| Indicador | rho | p-valor | Significativo |",
        "|-----------|-----|---------|---------------|",
    ]
    for col, res in spearman.items():
        sig = "Sim *" if res["signif"] else "Nao"
        lines.append(f"| {res['label']} | {res['rho']:+.4f} | {res['pval']:.4f} | {sig} |")

    lines += [
        "",
        "## 3. Analise de Lag (semanas de atraso TOH -> n_covid)",
        "",
        "| Lag | rho | p-valor |",
        "|-----|-----|---------|",
    ]
    for lag_key, res in lag.items():
        lag_n = lag_key.replace("lag_", "")
        lines.append(f"| {lag_n} sem | {res['rho']:+.4f} | {res['pval']:.4f} |")

    pc1_var = pca_res["pc1_var_explained"]
    lines += [
        "",
        "## 4. PCA Bivariado",
        "",
        f"- PC1 variancia explicada: {pc1_var:.1%}",
        f"- PC1 loading TOH: {pca_res['pc1_loading_toh']:+.4f}",
        f"- PC1 loading SRAG: {pca_res['pc1_loading_srag']:+.4f}",
        f"- Pesos PCA-derivados: TOH={pca_res['w_toh_pca']:.4f} / SRAG={pca_res['w_srag_pca']:.4f}",
        "",
        "## 5. Decisao de Pesos",
        "",
        f"- Metodo: `{decision['decision_method']}`",
        f"- Pesos finais: TOH={decision['w_toh']} / SRAG={decision['w_srag']}",
        f"- Pendente: {decision['weights_decision_pending']}",
        f"- Nota: {decision['note']}",
        "",
        "## 6. Interpretacao Epidemiologica",
        "",
        "### Primeira onda (SE 10-28/2020)",
        "TOH fixo em 30% (FVS-AM nao registrou sistematicamente antes de jul/2020).",
        "SRAG mostra pico massivo em SE 15-17/2020 (876-1031 casos/semana).",
        "Correlacao nulo neste periodo - esperado, limitacao de cobertura TOH.",
        "",
        "### Segunda onda (SE 49/2020 - SE 10/2021)",
        "Ambas variaveis crescem em paralelo: TOH 84% -> 104%, SRAG 284 -> 1607/semana.",
        "Pico sincronizado SE 3/2021: TOH=103.7%, n_covid=1.447.",
        "Correlacao estrutural esperada para predictor C2.",
    ]
    return "\n".join(lines)


def main() -> None:
    print("Carregando dados semanais...")
    df = load_data()
    print(f"  {len(df)} semanas mescladas")
    print(f"  Colunas: {list(df.columns)}")

    print("\n--- Spearman rho ---")
    spearman = spearman_analysis(df)

    print("\n--- Analise de Lag (TOH -> SRAG, 0-4 semanas) ---")
    lag = spearman_lag(df)

    print("\n--- PCA 2D ---")
    pca_res = pca_analysis(df)

    print("\n--- Decisao de Pesos ---")
    decision = weight_decision(pca_res)

    # Salva JSON de decisao
    out_json = {
        "generated_at":        pd.Timestamp.now().isoformat(),
        "granularidade":       "semanal_SE",
        "n_semanas":           len(df),
        "janela":              "SE 10/2020 - SE 30/2021",
        "spearman":            spearman,
        "lag_analysis":        lag,
        "pca":                 pca_res,
        "decision":            decision,
        "apriori":             {"w_toh": APRIORI_TOH, "w_srag": APRIORI_SRAG},
        "delta_threshold":     DELTA_THRESHOLD,
    }
    json_path = ROOT / "outputs/bi_dimensional_decision_semanal.json"

    def _to_serializable(obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        return obj

    def _fix_dict(d):
        if isinstance(d, dict):
            return {k: _fix_dict(v) for k, v in d.items()}
        if isinstance(d, list):
            return [_fix_dict(v) for v in d]
        return _to_serializable(d)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(_fix_dict(out_json), f, ensure_ascii=False, indent=2)
    print(f"\nDecisao JSON: {json_path}")

    # Relatorio markdown
    report = build_report(df, spearman, lag, pca_res, decision)
    report_path = ROOT / "outputs/relatorio_validacao_semanal.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Relatorio: {report_path}")


if __name__ == "__main__":
    main()
