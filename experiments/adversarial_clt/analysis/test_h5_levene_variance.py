"""H5 — Consistência cross-architecture (Levene's test).

Testa se braços B3/B4 produzem decisões mais consistentes entre modelos
diferentes do que B1/B2.

H₅: Var(D1|arm=B4) < Var(D1|arm=B1)  AND  Var(D2|arm=B4) < Var(D2|arm=B1)

Implementação:
- Para cada arm {B1, B4}: agrupa scores D1/D2 por model → 4 grupos (um por modelo)
- Levene's test de homogeneidade de variância entre os 4 modelos, dentro do arm
- H5 corroborada se B4 exibe maior homogeneidade cross-model que B1:
    → Var_entre_modelos(B4) < Var_entre_modelos(B1), OU
    → B4 passa Levene (p > 0.05) enquanto B1 falha (p < 0.05)
- Effect: razão de variâncias + Cohen's d sobre médias por modelo
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def _between_model_variance(df_arm: pd.DataFrame, score_col: str) -> float:
    """Variância das médias por modelo (cross-model consistency)."""
    means = df_arm.groupby("model")[score_col].mean()
    return float(means.var(ddof=1))


def _levene_across_models(df_arm: pd.DataFrame, score_col: str) -> tuple[float, float]:
    """Levene's test comparando variância de scores entre modelos."""
    groups = [
        grp[score_col].dropna().values
        for _, grp in df_arm.groupby("model")
    ]
    groups = [g for g in groups if len(g) >= 2]
    if len(groups) < 2:
        return float("nan"), float("nan")
    W, p = stats.levene(*groups)
    return float(W), float(p)


def _cohens_d_variance_ratio(var_b1: float, var_b4: float) -> float:
    """log-razão de variâncias: log(Var_B1 / Var_B4). Positivo = B4 mais homogêneo."""
    if var_b4 <= 0:
        return float("inf")
    return float(np.log(var_b1 / var_b4))


def run_h5_levene(
    d1_path: str | Path | None = None,
    d2_path: str | Path | None = None,
    arms_compare: tuple[str, str] = ("B1", "B4"),
    output_path: str | Path | None = None,
) -> dict:
    """Executa Levene's test para H5 em D1 e D2.

    Args:
        d1_path: parquet com colunas arm, model, d1_score por job
        d2_path: parquet com colunas arm, model, d2_score por job
        arms_compare: par de braços a comparar (baseline, intervenção)
        output_path: caminho para salvar JSON

    Returns:
        dict com resultados Levene por métrica e conclusão H5
    """
    arm_base, arm_inter = arms_compare
    results: dict = {"h5": {}, "conclusion": {}}

    for metric, path_arg in [("d1", d1_path), ("d2", d2_path)]:
        path = Path(path_arg) if path_arg else None
        if path is None or not path.exists():
            print(f"  [H5] {metric}: parquet não encontrado — ignorando")
            continue

        df = pd.read_parquet(path)
        score_col = f"{metric}_score"
        if score_col not in df.columns or "arm" not in df.columns or "model" not in df.columns:
            print(f"  [H5] {metric}: colunas ausentes — ignorando")
            continue

        df_base = df[df["arm"] == arm_base].copy()
        df_inter = df[df["arm"] == arm_inter].copy()

        if df_base.empty or df_inter.empty:
            print(f"  [H5] {metric}: arm {arm_base} ou {arm_inter} ausente — ignorando")
            continue

        # Variância entre modelos (média por modelo → var das médias)
        var_base = _between_model_variance(df_base, score_col)
        var_inter = _between_model_variance(df_inter, score_col)

        # Levene's test within each arm
        W_base, p_base = _levene_across_models(df_base, score_col)
        W_inter, p_inter = _levene_across_models(df_inter, score_col)

        log_ratio = _cohens_d_variance_ratio(var_base, var_inter)

        # Médias por modelo em cada arm
        means_base = df_base.groupby("model")[score_col].mean().to_dict()
        means_inter = df_inter.groupby("model")[score_col].mean().to_dict()

        metric_result = {
            arm_base: {
                "between_model_variance": round(var_base, 6),
                "levene_W": round(W_base, 4) if not np.isnan(W_base) else None,
                "levene_p": round(p_base, 6) if not np.isnan(p_base) else None,
                "heterogeneous_p05": p_base < 0.05 if not np.isnan(p_base) else None,
                "means_by_model": {k: round(v, 4) for k, v in means_base.items()},
            },
            arm_inter: {
                "between_model_variance": round(var_inter, 6),
                "levene_W": round(W_inter, 4) if not np.isnan(W_inter) else None,
                "levene_p": round(p_inter, 6) if not np.isnan(p_inter) else None,
                "heterogeneous_p05": p_inter < 0.05 if not np.isnan(p_inter) else None,
                "means_by_model": {k: round(v, 4) for k, v in means_inter.items()},
            },
            "log_variance_ratio": round(log_ratio, 4),
            "h5_direction_correct": var_inter < var_base,
        }
        results["h5"][metric] = metric_result

        print(
            f"  [H5] {metric.upper()}: Var({arm_base})={var_base:.4f} Var({arm_inter})={var_inter:.4f} "
            f"log_ratio={log_ratio:.4f} dir={'✓' if var_inter < var_base else '✗'}"
        )
        print(
            f"         Levene {arm_base}: W={W_base:.3f} p={p_base:.4f} | "
            f"Levene {arm_inter}: W={W_inter:.3f} p={p_inter:.4f}"
        )

    # H5 corroborada se direção correta em ao menos 1 métrica
    direction_correct = [
        results["h5"].get(m, {}).get("h5_direction_correct", False)
        for m in ("d1", "d2")
        if m in results["h5"]
    ]
    h5_corroborated = all(direction_correct) if direction_correct else False
    results["conclusion"] = {
        "h5_corroborated": h5_corroborated,
        "arms_compared": list(arms_compare),
        "alpha": 0.05,
        "verdict": (
            f"H5 CORROBORADA: {arm_inter} mais homogêneo cross-model que {arm_base} em D1 e D2"
            if h5_corroborated
            else f"H5 NÃO CORROBORADA: {arm_inter} não exibe menor variância cross-model consistentemente"
        ),
    }
    print(f"\n  → {results['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H5 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Levene H5 — variância cross-model por arm")
    parser.add_argument("--d1", help="Parquet com scores D1 por job")
    parser.add_argument("--d2", help="Parquet com scores D2 por job")
    parser.add_argument("--base-arm", default="B1", help="Braço baseline (padrão B1)")
    parser.add_argument("--inter-arm", default="B4", help="Braço intervenção (padrão B4)")
    parser.add_argument("--output", default="experiments/adversarial_clt/results/h5_levene.json")
    args = parser.parse_args()

    run_h5_levene(
        d1_path=args.d1,
        d2_path=args.d2,
        arms_compare=(args.base_arm, args.inter_arm),
        output_path=args.output,
    )
