"""H2 e H4 — Wilcoxon signed-rank: cobertura predicativa (D2) e especificidade (D3).

H₂: D2(B3, m) > D2(B1, m)  AND  D2(B4, m) > D2(B1, m)  ∀m
H₄: D3(B4, m) > D3(B1, m)  ∀m

Teste: Wilcoxon signed-rank (escores contínuos 0–1, within-model, pairwise por cenário)
α_corrigido = 0,05 / 24 = 0,0021 (Bonferroni m=24)
Effect size: Cohen's d (diferença de médias / std pooled)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ALPHA_RAW = 0.05
N_COMPARISONS_BONFERRONI = 24
ALPHA_CORRECTED = ALPHA_RAW / N_COMPARISONS_BONFERRONI

VALID_MODELS = ["qwen3:14b", "phi4:14b", "gemma3:12b", "llama3.1:8b"]


def _cohens_d(scores_a: np.ndarray, scores_b: np.ndarray) -> float:
    """Cohen's d: (mean_b - mean_a) / pooled_std. Positivo = B melhora."""
    n_a, n_b = len(scores_a), len(scores_b)
    if n_a < 2 or n_b < 2:
        return float("nan")
    pooled_std = np.sqrt(
        ((n_a - 1) * scores_a.std(ddof=1) ** 2 + (n_b - 1) * scores_b.std(ddof=1) ** 2)
        / (n_a + n_b - 2)
    )
    if pooled_std == 0:
        return 0.0
    return float((scores_b.mean() - scores_a.mean()) / pooled_std)


def _wilcoxon_pairwise(
    df_a: pd.DataFrame,
    df_b: pd.DataFrame,
    score_col: str,
) -> dict:
    """Wilcoxon signed-rank entre dois braços, pareados por scenario_id."""
    merged = pd.merge(
        df_a[["scenario_id", score_col]].rename(columns={score_col: "a"}),
        df_b[["scenario_id", score_col]].rename(columns={score_col: "b"}),
        on="scenario_id",
        how="inner",
    ).dropna()

    if len(merged) < 6:
        return {"n_pairs": len(merged), "error": "pares insuficientes para Wilcoxon"}

    diffs = merged["b"].values - merged["a"].values
    if np.all(diffs == 0):
        return {
            "n_pairs": int(len(merged)),
            "stat": 0.0, "p_value": 1.0,
            "significant_bonferroni": False,
            "mean_a": round(merged["a"].mean(), 4),
            "mean_b": round(merged["b"].mean(), 4),
            "cohens_d": 0.0,
            "direction_correct": False,
        }

    stat, p_val = stats.wilcoxon(diffs, alternative="greater")
    d = _cohens_d(merged["a"].values, merged["b"].values)

    return {
        "n_pairs": int(len(merged)),
        "stat": round(float(stat), 4),
        "p_value": round(float(p_val), 6),
        "significant_bonferroni": float(p_val) < ALPHA_CORRECTED,
        "mean_a": round(float(merged["a"].mean()), 4),
        "mean_b": round(float(merged["b"].mean()), 4),
        "cohens_d": round(d, 4) if not np.isnan(d) else None,
        "direction_correct": float(merged["b"].mean()) > float(merged["a"].mean()),
    }


def run_h2_wilcoxon(
    d2_path: str | Path,
    output_path: str | Path | None = None,
) -> dict:
    """Wilcoxon H2: D2(B3/B4) > D2(B1) por modelo.

    Comparações: B1vB3, B1vB4 — esperado B3 > B1 e B4 > B1.
    """
    path = Path(d2_path)
    if not path.exists():
        raise FileNotFoundError(f"D2 parquet não encontrado: {path}")

    df = pd.read_parquet(path)
    if "arm" not in df.columns and "braco" in df.columns:
        df = df.rename(columns={"braco": "arm"})

    agg = (
        df.dropna(subset=["d2_score"])
        .groupby(["scenario_id", "arm", "model"])["d2_score"]
        .mean()
        .reset_index()
    )

    results: dict = {"h2": {}}
    comparisons = [("B1", "B3"), ("B1", "B4")]

    for arm_a, arm_b in comparisons:
        pair_key = f"{arm_a}_vs_{arm_b}"
        results["h2"][pair_key] = {}
        wins = 0

        for model in VALID_MODELS:
            df_a = agg[(agg["arm"] == arm_a) & (agg["model"] == model)]
            df_b = agg[(agg["arm"] == arm_b) & (agg["model"] == model)]
            wx = _wilcoxon_pairwise(df_a, df_b, "d2_score")
            results["h2"][pair_key][model] = wx
            if wx.get("significant_bonferroni"):
                wins += 1
            print(
                f"  [H2] {pair_key}/{model}: "
                f"p={wx.get('p_value', 'n/a')} d={wx.get('cohens_d', '?')} "
                f"dir={'✓' if wx.get('direction_correct') else '✗'}"
            )

        results["h2"][pair_key]["n_models_significant"] = wins

    # H2 corroborada se B4 > B1 em ≥ 3 modelos
    b4_wins = results["h2"].get("B1_vs_B4", {}).get("n_models_significant", 0)
    h2_corroborated = b4_wins >= 3

    results["conclusion_h2"] = {
        "h2_corroborated": h2_corroborated,
        "b4_wins_bonferroni": b4_wins,
        "verdict": (
            f"H2 CORROBORADA: D2(B4) > D2(B1) em {b4_wins}/4 modelos"
            if h2_corroborated
            else f"H2 NÃO CORROBORADA: D2(B4) > D2(B1) em {b4_wins}/4 modelos"
        ),
    }
    print(f"\n  → H2: {results['conclusion_h2']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H2 salvos em {out}")

    return results


def run_h4_wilcoxon(
    d3_path: str | Path,
    output_path: str | Path | None = None,
) -> dict:
    """Wilcoxon H4: D3(B4) > D3(B1) por modelo."""
    path = Path(d3_path)
    if not path.exists():
        raise FileNotFoundError(f"D3 parquet não encontrado: {path}")

    df = pd.read_parquet(path)
    if "arm" not in df.columns and "braco" in df.columns:
        df = df.rename(columns={"braco": "arm"})

    agg = (
        df.dropna(subset=["d3_score"])
        .groupby(["scenario_id", "arm", "model"])["d3_score"]
        .mean()
        .reset_index()
    )

    results: dict = {"h4": {"B1_vs_B4": {}}}
    wins = 0

    for model in VALID_MODELS:
        df_a = agg[(agg["arm"] == "B1") & (agg["model"] == model)]
        df_b = agg[(agg["arm"] == "B4") & (agg["model"] == model)]
        wx = _wilcoxon_pairwise(df_a, df_b, "d3_score")
        results["h4"]["B1_vs_B4"][model] = wx
        if wx.get("significant_bonferroni"):
            wins += 1
        print(
            f"  [H4] B1vB4/{model}: "
            f"p={wx.get('p_value', 'n/a')} d={wx.get('cohens_d', '?')} "
            f"dir={'✓' if wx.get('direction_correct') else '✗'}"
        )

    h4_corroborated = wins >= 3
    results["conclusion_h4"] = {
        "h4_corroborated": h4_corroborated,
        "b4_wins_bonferroni": wins,
        "verdict": (
            f"H4 CORROBORADA: D3(B4) > D3(B1) em {wins}/4 modelos"
            if h4_corroborated
            else f"H4 NÃO CORROBORADA: D3(B4) > D3(B1) em {wins}/4 modelos"
        ),
    }
    print(f"\n  → H4: {results['conclusion_h4']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H4 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wilcoxon H2 (D2) e H4 (D3)")
    parser.add_argument("--d2", help="Parquet com scores D2")
    parser.add_argument("--d3", help="Parquet com scores D3")
    parser.add_argument("--output-h2", default="experiments/adversarial_clt/results/h2_wilcoxon.json")
    parser.add_argument("--output-h4", default="experiments/adversarial_clt/results/h4_wilcoxon.json")
    args = parser.parse_args()

    if args.d2:
        run_h2_wilcoxon(d2_path=args.d2, output_path=args.output_h2)
    if args.d3:
        run_h4_wilcoxon(d3_path=args.d3, output_path=args.output_h4)
