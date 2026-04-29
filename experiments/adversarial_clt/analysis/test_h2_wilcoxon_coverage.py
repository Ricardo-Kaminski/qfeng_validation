"""H2: Wilcoxon pareado B3 vs B1 — cobertura jurídica (não-inferioridade, δ=-0.05).

α Bonferroni m=8: 0.00625.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

DERIVED = Path(__file__).resolve().parents[1] / "results" / "results_b1_b4_derivado.parquet"
OUTPUT_DIR = Path(__file__).resolve().parents[0] / "resultados_h1_h6"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625
MARGIN = -0.05  # margem de não-inferioridade


def run_h2() -> dict:
    df = pd.read_parquet(DERIVED)
    b1 = df[df["braco"] == "B1"][["modelo", "scenario_id", "run_id", "coverage_score"]].rename(
        columns={"coverage_score": "b1_cov"}
    )
    b3 = df[df["braco"] == "B3"][["modelo", "scenario_id", "run_id", "coverage_score"]].rename(
        columns={"coverage_score": "b3_cov"}
    )
    paired = b1.merge(b3, on=["modelo", "scenario_id", "run_id"], how="inner")
    assert len(paired) == 600

    diff = paired["b3_cov"] - paired["b1_cov"]
    shifted = diff - MARGIN  # teste H: diff > margin → shifted > 0
    stat, p_val = stats.wilcoxon(shifted, alternative="greater")

    rng = np.random.default_rng(42)
    n_boot = 10_000
    boot_medians = [
        np.median(rng.choice(diff.values, size=len(diff), replace=True))
        for _ in range(n_boot)
    ]
    ci_lo, ci_hi = float(np.percentile(boot_medians, 2.5)), float(np.percentile(boot_medians, 97.5))

    significant = p_val < ALPHA

    out = {
        "hipotese": "H2",
        "comparacao": "B3 vs B1 — cobertura jurídica (não-inferioridade Wilcoxon)",
        "n_pares": 600,
        "b1_coverage_mean": float(paired["b1_cov"].mean()),
        "b3_coverage_mean": float(paired["b3_cov"].mean()),
        "b1_coverage_median": float(paired["b1_cov"].median()),
        "b3_coverage_median": float(paired["b3_cov"].median()),
        "mean_diff_b3_minus_b1": float(diff.mean()),
        "median_diff_b3_minus_b1": float(diff.median()),
        "ci95_median_diff_bootstrap": [ci_lo, ci_hi],
        "margem_nao_inferioridade": MARGIN,
        "wilcoxon_statistic": float(stat),
        "p_value_one_sided_nao_inferioridade": float(p_val),
        "alpha_bonferroni_m8": ALPHA,
        "nao_inferioridade_demonstrada": bool(significant),
        "interpretation": (
            f"B3 cobertura média = {paired['b3_cov'].mean():.3f} vs B1 = {paired['b1_cov'].mean():.3f}. "
            f"Diferença mediana B3−B1 = {diff.median():.3f} "
            f"(IC95% bootstrap [{ci_lo:.3f}, {ci_hi:.3f}]). "
            f"Wilcoxon (H: diff > −0.05): p = {p_val:.4g}. "
            f"Não-inferioridade {'DEMONSTRADA' if significant else 'NÃO demonstrada'} "
            f"a α corrigido = 0,00625."
        ),
    }

    (OUTPUT_DIR / "h2_result.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return out


if __name__ == "__main__":
    run_h2()
