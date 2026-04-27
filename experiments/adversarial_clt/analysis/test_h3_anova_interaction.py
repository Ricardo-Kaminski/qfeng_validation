"""H3 — Cross-architecture invariance (ANOVA two-way) — REFORMULADA pela Emenda 27/abr/2026.

Testa se o efeito Q-FENG (B4 vs B1) é estatisticamente invariante entre famílias
arquitetônicas de LLM, operacionalizado como NÃO-SIGNIFICÂNCIA do termo de
interação arm × model na ANOVA two-way.

H₃: F(arm × model) com p > 0.05/6 = 0.0083 (Bonferroni m=6 sobre H1-H6)

Reformulada pela emenda 27/abr/2026 (PRE_REGISTRATION.md §11.1) para alinhar
com a reivindicação editorial de agnosticismo de stack ML (canônico §7.4 nova).

Implementação:
- ANOVA two-way: D1 ~ arm + model + arm:model (statsmodels OLS, tipo II)
- Replicar para D2 e D3
- Reportar F-statistic, p-valor da interação, η² parcial
- Critério de evidência: p_interacao > 0.0083 → H3 sustentada (invariância cross-arch)
- Critério de falsificação: p_interacao ≤ 0.0083 → H3 falsificada,
  análise exploratória post-hoc sobre a natureza da interação

Semântica da decisão (pós-emenda):
  h3_supported = True  → interação NÃO significativa → efeito Q-FENG é cross-arch invariante
  h3_supported = False → interação significativa → efeito varia por arquitetura
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


ALPHA_BONFERRONI = 0.05 / 6   # m=6 hipóteses confirmatórias H1-H6


def _eta_squared(anova_table: pd.DataFrame, effect: str) -> float:
    """η² parcial: SS_effect / (SS_effect + SS_residual)."""
    ss_effect = anova_table.loc[effect, "sum_sq"]
    ss_resid = anova_table.loc["Residual", "sum_sq"]
    return ss_effect / (ss_effect + ss_resid)


def _decide_h3(p_value: float, alpha: float = ALPHA_BONFERRONI) -> dict:
    """Decisão de H3: sustentada quando p > alpha (não-significância = invariância).

    Args:
        p_value: p-valor do termo de interação arm×model
        alpha: nível de significância corrigido (padrão 0.0083)

    Returns:
        dict com h3_supported e h3_falsified
    """
    supported = p_value > alpha
    return {
        "h3_supported": supported,
        "h3_falsified": not supported,
        "interpretation": (
            "H3 sustentada — invariância cross-architecture confirmada (p > α)"
            if supported
            else "H3 falsificada — interação significativa detectada — análise exploratória requerida (p ≤ α)"
        ),
    }


def _self_test_decision_logic() -> None:
    """Smoke test: garante que H3 é sustentada quando p > alpha (não p < alpha)."""
    # Caso 1: p alto → H3 sustentada
    r = _decide_h3(p_value=0.50, alpha=ALPHA_BONFERRONI)
    assert r["h3_supported"] is True, f"Falhou: p=0.50 deveria sustentar H3, obteve {r}"
    # Caso 2: p baixo → H3 falsificada
    r = _decide_h3(p_value=0.001, alpha=ALPHA_BONFERRONI)
    assert r["h3_supported"] is False, f"Falhou: p=0.001 deveria falsificar H3, obteve {r}"
    # Caso 3: p exatamente no limiar (< alpha → falsificado)
    r = _decide_h3(p_value=ALPHA_BONFERRONI, alpha=ALPHA_BONFERRONI)
    assert r["h3_supported"] is False, f"Falhou: p=alpha deveria falsificar H3, obteve {r}"
    print(f"✓ test_h3 logic verified: p>alpha ({ALPHA_BONFERRONI:.4f}) => H3 supported (cross-arch invariance)")


def run_h3_anova(
    results_path: str | Path,
    d1_path: str | Path | None = None,
    d2_path: str | Path | None = None,
    d3_path: str | Path | None = None,
    output_path: str | Path | None = None,
) -> dict:
    """Executa ANOVA two-way (arm × model) para D1, D2, D3.

    H3 é SUSTENTADA quando p(interação) > 0.0083 (não-significância = invariância).

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
    metrics_analyzed = []

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
        model_fit = ols(formula, data=agg).fit()
        table = anova_lm(model_fit, typ=2)

        arm_row = "C(arm)"
        model_row = "C(model)"
        inter_row = "C(arm):C(model)"

        eta_arm = _eta_squared(table, arm_row)
        eta_model = _eta_squared(table, model_row)
        eta_inter = _eta_squared(table, inter_row)

        p_inter = float(table.loc[inter_row, "PR(>F)"])
        decision = _decide_h3(p_inter)

        metric_result = {
            "n_obs": int(agg.shape[0]),
            "alpha_bonferroni": ALPHA_BONFERRONI,
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
                "p": round(p_inter, 6),
                "eta2_partial": round(eta_inter, 4),
                **decision,
            },
        }
        results["h3"][metric] = metric_result
        metrics_analyzed.append(metric)
        status = "SUSTENTADA" if decision["h3_supported"] else "FALSIFICADA"
        print(
            f"  [H3] {metric.upper()}: F_inter={metric_result['interaction_arm_x_model']['F']}, "
            f"p={p_inter:.4f} {'>' if p_inter > ALPHA_BONFERRONI else '<='} {ALPHA_BONFERRONI:.4f} → H3 {status}"
        )

    # Conclusão H3: sustentada se invariância confirmada em D1 e D2 (métricas primárias)
    primary_metrics = [m for m in ("d1", "d2") if m in results["h3"]]
    h3_supported_primary = all(
        results["h3"][m]["interaction_arm_x_model"].get("h3_supported", False)
        for m in primary_metrics
    ) if primary_metrics else False

    results["conclusion"] = {
        "h3_supported": h3_supported_primary,
        "metrics_analyzed": metrics_analyzed,
        "alpha_bonferroni": ALPHA_BONFERRONI,
        "verdict": (
            "H3 SUSTENTADA: invariância cross-architecture confirmada (p > 0.0083 em D1 e D2)"
            if h3_supported_primary
            else "H3 FALSIFICADA: interação arm×model significativa detectada — análise post-hoc requerida"
        ),
    }
    print(f"\n  → {results['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H3 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANOVA two-way H3 (cross-arch invariance)")
    parser.add_argument("--d1", help="Parquet com scores D1 por job")
    parser.add_argument("--d2", help="Parquet com scores D2 por job")
    parser.add_argument("--d3", help="Parquet com scores D3 por job")
    parser.add_argument("--results", default="experiments/adversarial_clt/results/results.parquet")
    parser.add_argument("--output", default="experiments/adversarial_clt/results/h3_anova.json")
    parser.add_argument("--smoke-test", action="store_true", help="Roda self-test de lógica de decisão")
    args = parser.parse_args()

    if args.smoke_test:
        _self_test_decision_logic()
    else:
        run_h3_anova(
            results_path=args.results,
            d1_path=args.d1,
            d2_path=args.d2,
            d3_path=args.d3,
            output_path=args.output,
        )
