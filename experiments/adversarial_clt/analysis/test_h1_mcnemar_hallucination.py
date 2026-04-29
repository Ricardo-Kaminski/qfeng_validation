"""H1: McNemar pareado B3 vs B1 — taxa de alucinação.

Pareamento por (modelo, scenario_id, run_id).
Teste unicaudal: B3 reduz alucinação (b > c esperado).
α Bonferroni m=8: 0.00625.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
from statsmodels.stats.contingency_tables import mcnemar

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

DERIVED = Path(__file__).resolve().parents[1] / "results" / "results_b1_b4_derivado.parquet"
OUTPUT_DIR = Path(__file__).resolve().parents[0] / "resultados_h1_h6"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625


def run_h1() -> dict:
    df = pd.read_parquet(DERIVED)
    b1 = df[df["braco"] == "B1"][["modelo", "scenario_id", "run_id", "hallucination_flag"]].rename(
        columns={"hallucination_flag": "b1_hall"}
    )
    b3 = df[df["braco"] == "B3"][["modelo", "scenario_id", "run_id", "hallucination_flag"]].rename(
        columns={"hallucination_flag": "b3_hall"}
    )
    paired = b1.merge(b3, on=["modelo", "scenario_id", "run_id"], how="inner")
    assert len(paired) == 600, f"Esperado 600 pares, encontrou {len(paired)}"

    n_00 = int(((paired["b3_hall"] == 0) & (paired["b1_hall"] == 0)).sum())
    n_01 = int(((paired["b3_hall"] == 0) & (paired["b1_hall"] == 1)).sum())  # b: B1 alucina, B3 não
    n_10 = int(((paired["b3_hall"] == 1) & (paired["b1_hall"] == 0)).sum())  # c: B3 alucina, B1 não
    n_11 = int(((paired["b3_hall"] == 1) & (paired["b1_hall"] == 1)).sum())

    assert n_00 + n_01 + n_10 + n_11 == 600

    table = [[n_00, n_01], [n_10, n_11]]
    result = mcnemar(table, exact=True)

    direction_correct = n_01 > n_10  # b > c: B3 melhora
    p_one_sided = result.pvalue / 2 if direction_correct else 1.0 - result.pvalue / 2
    odds_ratio = n_01 / n_10 if n_10 > 0 else float("inf")
    significant = p_one_sided < ALPHA

    # Breakdown por modelo
    breakdown = []
    for modelo in sorted(paired["modelo"].unique()):
        sub = paired[paired["modelo"] == modelo]
        n01_m = int(((sub["b3_hall"] == 0) & (sub["b1_hall"] == 1)).sum())
        n10_m = int(((sub["b3_hall"] == 1) & (sub["b1_hall"] == 0)).sum())
        n00_m = int(((sub["b3_hall"] == 0) & (sub["b1_hall"] == 0)).sum())
        n11_m = int(((sub["b3_hall"] == 1) & (sub["b1_hall"] == 1)).sum())
        table_m = [[n00_m, n01_m], [n10_m, n11_m]]
        res_m = mcnemar(table_m, exact=True)
        dir_m = n01_m > n10_m
        p1_m = res_m.pvalue / 2 if dir_m else 1.0 - res_m.pvalue / 2
        breakdown.append({
            "modelo": modelo,
            "n_pares": int(len(sub)),
            "b1_hall_rate": float(sub["b1_hall"].mean()),
            "b3_hall_rate": float(sub["b3_hall"].mean()),
            "n_00": n00_m, "n_01": n01_m, "n_10": n10_m, "n_11": n11_m,
            "odds_ratio": float(n01_m / n10_m) if n10_m > 0 else None,
            "p_one_sided": float(p1_m),
            "significant": bool(p1_m < ALPHA),
        })

    out = {
        "hipotese": "H1",
        "comparacao": "B3 vs B1 — taxa de alucinação (McNemar pareado)",
        "n_pares": 600,
        "tabela_2x2": {"n_00": n_00, "n_01": n_01, "n_10": n_10, "n_11": n_11},
        "b1_hall_rate": float(paired["b1_hall"].mean()),
        "b3_hall_rate": float(paired["b3_hall"].mean()),
        "reducao_absoluta_pp": float((paired["b1_hall"].mean() - paired["b3_hall"].mean()) * 100),
        "odds_ratio_discordancia": float(odds_ratio),
        "mcnemar_statistic": float(result.statistic) if result.statistic is not None else None,
        "p_value_two_sided": float(result.pvalue),
        "p_value_one_sided": float(p_one_sided),
        "direction_correct": bool(direction_correct),
        "alpha_bonferroni_m8": ALPHA,
        "significant_at_alpha_corrected": bool(significant),
        "interpretation": (
            f"B3 reduz alucinação em {(paired['b1_hall'].mean() - paired['b3_hall'].mean())*100:.1f} pp "
            f"(de {paired['b1_hall'].mean()*100:.1f}% para {paired['b3_hall'].mean()*100:.1f}%). "
            f"McNemar exato: p_unicaudal = {p_one_sided:.4g} "
            f"({'significativo' if significant else 'NÃO significativo'} a α corrigido = 0,00625). "
            f"OR discordância = {odds_ratio:.2f}."
        ),
    }

    (OUTPUT_DIR / "h1_result.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUTPUT_DIR / "h1_breakdown_por_modelo.json").write_text(
        json.dumps(breakdown, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return out


if __name__ == "__main__":
    run_h1()
