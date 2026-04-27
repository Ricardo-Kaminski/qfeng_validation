"""H3 — Interação arm × model (ANOVA two-way).

Testa se existe efeito de interação estatisticamente significativo entre
braço experimental (arm) e modelo (model) sobre D1, D2, D3.

H₃: F(arm × model) com p < 0,05 para ao menos uma métrica {D1, D2, D3}

Critério de sucesso: p < 0,05 na interação (não aplica Bonferroni — único teste global).
Saída: tabela ANOVA completa + η² parcial para cada fator.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def _eta_squared(anova_table: pd.DataFrame, effect: str) -> float:
    """η² parcial: SS_effect / (SS_effect + SS_residual)."""
    ss_effect = anova_table.loc[effect, "sum_sq"]
    ss_resid = anova_table.loc["Residual", "sum_sq"]
    return ss_effect / (ss_effect + ss_resid)


def run_h3_anova(
    results_path: str | Path,
    d1_path: str | Path | None = None,
    d2_path: str | Path | None = None,
    d3_path: str | Path | None = None,
    output_path: str | Path | None = None,
) -> dict:
    """Executa ANOVA two-way (arm × model) para D1, D2, D3.

    Args:
        results_path: parquet com colunas scenario_id, arm, model, run_id, response_text
        d1_path: parquet com d1_score por job (opcional — usa results_path se None)
        d2_path: parquet com d2_score por job (opcional)
        d3_path: parquet com d3_score por job (opcional)
        output_path: caminho para salvar JSON com resultados

    Returns:
        dict com resultados ANOVA por métrica e conclusão H3
    """
    try:
        from statsmodels.formula.api import ols
        from statsmodels.stats.anova import anova_lm
    except ImportError:
        raise ImportError("statsmodels obrigatório: pip install statsmodels")

    results: dict = {"h3": {}, "conclusion": {}}
    metrics_found = []

    for metric, path_arg in [("d1", d1_path), ("d2", d2_path), ("d3", d3_path)]:
        path = Path(path_arg) if path_arg else None
        if path is None or not path.exists():
            print(f"  [H3] {metric}: parquet não encontrado — ignorando")
            continue

        df = pd.read_parquet(path)
        score_col = f"{metric}_score"
        if score_col not in df.columns:
            print(f"  [H3] {metric}: coluna '{score_col}' ausente — ignorando")
            continue

        # Agregar por (scenario_id, arm, model) → média entre run_ids
        agg = (
            df.dropna(subset=[score_col])
            .groupby(["scenario_id", "arm", "model"])[score_col]
            .mean()
            .reset_index()
        )

        if agg.shape[0] < 8:
            print(f"  [H3] {metric}: dados insuficientes (n={agg.shape[0]}) — ignorando")
            continue

        formula = f"{score_col} ~ C(arm) + C(model) + C(arm):C(model)"
        model = ols(formula, data=agg).fit()
        table = anova_lm(model, typ=2)

        arm_row = "C(arm)"
        model_row = "C(model)"
        inter_row = "C(arm):C(model)"

        eta_arm = _eta_squared(table, arm_row)
        eta_model = _eta_squared(table, model_row)
        eta_inter = _eta_squared(table, inter_row)

        metric_result = {
            "n_obs": int(agg.shape[0]),
            "arm": {
                "F": round(float(table.loc[arm_row, "F"]), 4),
                "p": round(float(table.loc[arm_row, "PR(>F)"]), 6),
                "eta2_partial": round(eta_arm, 4),
            },
            "model": {
                "F": round(float(table.loc[model_row, "F"]), 4),
                "p": round(float(table.loc[model_row, "PR(>F)"]), 6),
                "eta2_partial": round(eta_model, 4),
            },
            "interaction_arm_x_model": {
                "F": round(float(table.loc[inter_row, "F"]), 4),
                "p": round(float(table.loc[inter_row, "PR(>F)"]), 6),
                "eta2_partial": round(eta_inter, 4),
                "significant_p05": float(table.loc[inter_row, "PR(>F)"]) < 0.05,
            },
        }
        results["h3"][metric] = metric_result
        metrics_found.append(metric)
        print(
            f"  [H3] {metric.upper()}: F_inter={metric_result['interaction_arm_x_model']['F']}, "
            f"p={metric_result['interaction_arm_x_model']['p']:.4f}, "
            f"η²={metric_result['interaction_arm_x_model']['eta2_partial']:.4f}"
        )

    # Conclusão H3: interação significativa em ao menos 1 métrica
    any_significant = any(
        results["h3"].get(m, {}).get("interaction_arm_x_model", {}).get("significant_p05", False)
        for m in metrics_found
    )
    results["conclusion"]["h3_corroborated"] = any_significant
    results["conclusion"]["metrics_analyzed"] = metrics_found
    results["conclusion"]["alpha"] = 0.05
    results["conclusion"]["verdict"] = (
        "H3 CORROBORADA: interação arm×model significativa em ao menos 1 métrica"
        if any_significant
        else "H3 NÃO CORROBORADA: ausência de interação significativa em todas as métricas"
    )
    print(f"\n  → {results['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H3 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANOVA two-way H3 (arm × model)")
    parser.add_argument("--d1", help="Parquet com scores D1 por job")
    parser.add_argument("--d2", help="Parquet com scores D2 por job")
    parser.add_argument("--d3", help="Parquet com scores D3 por job")
    parser.add_argument("--results", default="experiments/adversarial_clt/results/results.parquet")
    parser.add_argument("--output", default="experiments/adversarial_clt/results/h3_anova.json")
    args = parser.parse_args()

    run_h3_anova(
        results_path=args.results,
        d1_path=args.d1,
        d2_path=args.d2,
        d3_path=args.d3,
        output_path=args.output,
    )
