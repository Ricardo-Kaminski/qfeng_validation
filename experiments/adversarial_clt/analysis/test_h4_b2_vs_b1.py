"""H4: B2 (RAG isolado) vs B1 — alucinação (McNemar) + cobertura (Wilcoxon não-inf.).

H4a: McNemar — B2 reduz alucinação vs B1
H4b: Wilcoxon — B2 não-inferior a B1 em cobertura
α Bonferroni m=8: 0.00625.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.contingency_tables import mcnemar

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

DERIVED = Path(__file__).resolve().parents[1] / "results" / "results_b1_b4_derivado.parquet"
OUTPUT_DIR = Path(__file__).resolve().parents[0] / "resultados_h1_h6"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625
MARGIN = -0.05


def run_h4() -> tuple[dict, dict]:
    df = pd.read_parquet(DERIVED)
    b1 = df[df["braco"] == "B1"][["modelo", "scenario_id", "run_id", "hallucination_flag", "coverage_score"]].rename(
        columns={"hallucination_flag": "b1_hall", "coverage_score": "b1_cov"}
    )
    b2 = df[df["braco"] == "B2"][["modelo", "scenario_id", "run_id", "hallucination_flag", "coverage_score"]].rename(
        columns={"hallucination_flag": "b2_hall", "coverage_score": "b2_cov"}
    )
    paired = b1.merge(b2, on=["modelo", "scenario_id", "run_id"], how="inner")
    assert len(paired) == 600

    # H4a: McNemar (alucinação)
    n_00 = int(((paired["b2_hall"] == 0) & (paired["b1_hall"] == 0)).sum())
    n_01 = int(((paired["b2_hall"] == 0) & (paired["b1_hall"] == 1)).sum())
    n_10 = int(((paired["b2_hall"] == 1) & (paired["b1_hall"] == 0)).sum())
    n_11 = int(((paired["b2_hall"] == 1) & (paired["b1_hall"] == 1)).sum())
    table = [[n_00, n_01], [n_10, n_11]]
    res_mc = mcnemar(table, exact=True)
    direction_b2_reduces = n_01 > n_10
    p_mc_1s = res_mc.pvalue / 2 if direction_b2_reduces else 1.0 - res_mc.pvalue / 2
    odds_ratio = n_01 / n_10 if n_10 > 0 else float("inf")

    # Compare to B3 for context (re-load B3)
    b3 = df[df["braco"] == "B3"][["modelo", "scenario_id", "run_id", "hallucination_flag"]].rename(
        columns={"hallucination_flag": "b3_hall"}
    )
    paired_b3 = paired.merge(b3, on=["modelo", "scenario_id", "run_id"], how="inner")
    b3_rate = float(paired_b3["b3_hall"].mean())

    h4a = {
        "hipotese": "H4a",
        "comparacao": "B2 vs B1 — taxa de alucinação (McNemar)",
        "n_pares": 600,
        "tabela_2x2": {"n_00": n_00, "n_01": n_01, "n_10": n_10, "n_11": n_11},
        "b1_hall_rate": float(paired["b1_hall"].mean()),
        "b2_hall_rate": float(paired["b2_hall"].mean()),
        "b3_hall_rate_context": b3_rate,
        "reducao_absoluta_pp": float((paired["b1_hall"].mean() - paired["b2_hall"].mean()) * 100),
        "odds_ratio_discordancia": float(odds_ratio),
        "p_value_two_sided": float(res_mc.pvalue),
        "p_value_one_sided": float(p_mc_1s),
        "direction_b2_reduces": bool(direction_b2_reduces),
        "alpha_bonferroni_m8": ALPHA,
        "significant_at_alpha_corrected": bool(p_mc_1s < ALPHA),
        "interpretation": (
            f"B2 hall_rate={paired['b2_hall'].mean()*100:.1f}% vs B1={paired['b1_hall'].mean()*100:.1f}%. "
            f"B2 {'aumentou' if not direction_b2_reduces else 'reduziu'} alucinação. "
            f"p_unicaudal={p_mc_1s:.4g} "
            f"({'significativo' if p_mc_1s < ALPHA else 'NÃO significativo'} a α=0.00625). "
            f"Comparação: B3={b3_rate*100:.1f}% — ancoragem simbólica supera RAG isolado."
        ),
    }

    # H4b: Wilcoxon (cobertura)
    diff_cov = paired["b2_cov"] - paired["b1_cov"]
    shifted = diff_cov - MARGIN
    stat_w, p_w = stats.wilcoxon(shifted, alternative="greater")
    rng = np.random.default_rng(42)
    boot_medians = [np.median(rng.choice(diff_cov.values, len(diff_cov), True)) for _ in range(10_000)]
    ci_lo, ci_hi = float(np.percentile(boot_medians, 2.5)), float(np.percentile(boot_medians, 97.5))

    h4b = {
        "hipotese": "H4b",
        "comparacao": "B2 vs B1 — cobertura jurídica (Wilcoxon não-inferioridade)",
        "n_pares": 600,
        "b1_coverage_mean": float(paired["b1_cov"].mean()),
        "b2_coverage_mean": float(paired["b2_cov"].mean()),
        "mean_diff_b2_minus_b1": float(diff_cov.mean()),
        "median_diff_b2_minus_b1": float(diff_cov.median()),
        "ci95_median_diff_bootstrap": [ci_lo, ci_hi],
        "margem_nao_inferioridade": MARGIN,
        "wilcoxon_statistic": float(stat_w),
        "p_value_one_sided": float(p_w),
        "alpha_bonferroni_m8": ALPHA,
        "nao_inferioridade_demonstrada": bool(p_w < ALPHA),
        "interpretation": (
            f"B2 cobertura={paired['b2_cov'].mean():.3f} vs B1={paired['b1_cov'].mean():.3f}. "
            f"Dif mediana={diff_cov.median():.3f} (IC95% [{ci_lo:.3f},{ci_hi:.3f}]). "
            f"Wilcoxon p={p_w:.4g}. "
            f"Não-inferioridade {'DEMONSTRADA' if p_w < ALPHA else 'NÃO demonstrada'}."
        ),
    }

    (OUTPUT_DIR / "h4a_mcnemar_result.json").write_text(
        json.dumps(h4a, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUTPUT_DIR / "h4b_wilcoxon_result.json").write_text(
        json.dumps(h4b, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print("=== H4a ===")
    print(json.dumps(h4a, indent=2, ensure_ascii=False))
    print("\n=== H4b ===")
    print(json.dumps(h4b, indent=2, ensure_ascii=False))
    return h4a, h4b


if __name__ == "__main__":
    run_h4()
