"""H1 — McNemar emparelhado: efeito de ancoragem sobre alucinação (D1).

H₁: D1(B4, m) < D1(B1, m)  ∀m ∈ {qwen3:14b, phi4:14b, gemma3:12b, llama3.1:8b}

D1 é binária por cenário: 0=sem alucinação, 1=com alucinação.
McNemar testa se a proporção de mudanças B1→B4 e B4→B1 é simétrica.
α_corrigido = 0,05 / 24 = 0,0021 (Bonferroni m=24 comparações).

Effect size: Cohen's h = 2*arcsin(sqrt(p_B4)) - 2*arcsin(sqrt(p_B1))
  |h| > 0.2 = pequeno, > 0.5 = médio, > 0.8 = grande
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


ALPHA_RAW = 0.05
N_COMPARISONS_BONFERRONI = 24  # 6 pairwise × 4 modelos
ALPHA_CORRECTED = ALPHA_RAW / N_COMPARISONS_BONFERRONI

VALID_MODELS = ["qwen3:14b", "phi4:14b", "gemma3:12b", "llama3.1:8b"]
VALID_ARMS = ["B1", "B2", "B3", "B4"]


def _cohens_h(p1: float, p2: float) -> float:
    """Cohen's h para diferença de proporções."""
    return 2 * np.arcsin(np.sqrt(p1)) - 2 * np.arcsin(np.sqrt(p2))


def _mcnemar_pairwise(
    df_a: pd.DataFrame, df_b: pd.DataFrame, score_col: str = "d1_score"
) -> dict:
    """McNemar emparelhado entre dois braços para D1 binária.

    Pareia por scenario_id. Cada par (a, b) é um cenário:
      n00 = B1=0, B4=0 (ambos sem erro)
      n01 = B1=0, B4=1 (B4 piorou)
      n10 = B1=1, B4=0 (B4 melhorou — direção esperada)
      n11 = B1=1, B4=1 (ambos com erro)
    """
    merged = pd.merge(
        df_a[["scenario_id", score_col]].rename(columns={score_col: "a"}),
        df_b[["scenario_id", score_col]].rename(columns={score_col: "b"}),
        on="scenario_id",
        how="inner",
    )
    if merged.empty:
        return {"n_pairs": 0, "error": "sem pares"}

    a_bin = (merged["a"] > 0.5).astype(int)
    b_bin = (merged["b"] > 0.5).astype(int)

    n00 = int(((a_bin == 0) & (b_bin == 0)).sum())
    n01 = int(((a_bin == 0) & (b_bin == 1)).sum())  # intervenção piorou
    n10 = int(((a_bin == 1) & (b_bin == 0)).sum())  # intervenção melhorou
    n11 = int(((a_bin == 1) & (b_bin == 1)).sum())

    p_a = float(a_bin.mean())
    p_b = float(b_bin.mean())
    h = _cohens_h(p_a, p_b)

    if n01 + n10 == 0:
        chi2, p_val = 0.0, 1.0
    else:
        # McNemar: chi2 = (n10 - n01)^2 / (n10 + n01)
        chi2 = (n10 - n01) ** 2 / (n10 + n01)
        p_val = float(1 - stats.chi2.cdf(chi2, df=1))

    return {
        "n_pairs": int(len(merged)),
        "n00": n00, "n01": n01, "n10": n10, "n11": n11,
        "p_arm_a": round(p_a, 4),
        "p_arm_b": round(p_b, 4),
        "chi2": round(chi2, 4),
        "p_value": round(p_val, 6),
        "significant_bonferroni": p_val < ALPHA_CORRECTED,
        "cohens_h": round(h, 4),
        "direction_correct": p_b < p_a,  # intervenção reduz alucinação
    }


def run_h1_mcnemar(
    d1_path: str | Path,
    arm_pairs: list[tuple[str, str]] | None = None,
    output_path: str | Path | None = None,
) -> dict:
    """Executa McNemar emparelhado para H1 em todos os modelos e pares de braços.

    Args:
        d1_path: parquet com colunas scenario_id, arm, model, run_id, d1_score
        arm_pairs: pares a comparar (padrão: todos os pairwise entre B1..B4)
        output_path: caminho para salvar JSON

    Returns:
        dict com resultados McNemar por (arm_pair, model) e conclusão H1
    """
    path = Path(d1_path)
    if not path.exists():
        raise FileNotFoundError(f"D1 parquet não encontrado: {path}")

    df = pd.read_parquet(path)
    if "arm" not in df.columns and "braco" in df.columns:
        df = df.rename(columns={"braco": "arm"})

    # Agregar: média por (scenario_id, arm, model) entre run_ids
    agg = (
        df.dropna(subset=["d1_score"])
        .groupby(["scenario_id", "arm", "model"])["d1_score"]
        .mean()
        .reset_index()
    )

    if arm_pairs is None:
        arms = sorted(agg["arm"].unique())
        arm_pairs = [(a, b) for i, a in enumerate(arms) for b in arms[i+1:]]

    results: dict = {"h1": {}, "conclusion": {}}
    n_significant = 0
    n_h1_primary_direction = 0  # B4 < B1

    for arm_a, arm_b in arm_pairs:
        pair_key = f"{arm_a}_vs_{arm_b}"
        results["h1"][pair_key] = {}

        for model in VALID_MODELS:
            df_a = agg[(agg["arm"] == arm_a) & (agg["model"] == model)]
            df_b = agg[(agg["arm"] == arm_b) & (agg["model"] == model)]

            mc = _mcnemar_pairwise(df_a, df_b, "d1_score")
            results["h1"][pair_key][model] = mc

            sig = mc.get("significant_bonferroni", False)
            if sig:
                n_significant += 1
                print(
                    f"  [H1] {pair_key} / {model}: "
                    f"p={mc.get('p_value'):.4f} h={mc.get('cohens_h'):.3f} ★SIGNIFICATIVO"
                )
            else:
                print(
                    f"  [H1] {pair_key} / {model}: "
                    f"p={mc.get('p_value', 'n/a'):.4f} h={mc.get('cohens_h', 0):.3f}"
                )

        # Verifica H1 primária: B4 < B1 em ao menos 3 de 4 modelos
        if arm_a == "B1" and arm_b == "B4":
            directions = [
                results["h1"][pair_key][m].get("direction_correct", False)
                for m in VALID_MODELS
                if m in results["h1"][pair_key]
            ]
            n_h1_primary_direction = sum(directions)

    # Conclusão H1: corroborada se B4 < B1 em ao menos 3 modelos (p < 0,0021)
    b1_vs_b4 = results["h1"].get("B1_vs_B4", {})
    b4_wins = sum(
        1 for m in VALID_MODELS
        if b1_vs_b4.get(m, {}).get("significant_bonferroni", False)
        and b1_vs_b4.get(m, {}).get("direction_correct", False)
    )
    h1_corroborated = b4_wins >= 3

    results["conclusion"] = {
        "h1_corroborated": h1_corroborated,
        "b4_wins_bonferroni": b4_wins,
        "n_models_direction_correct": n_h1_primary_direction,
        "alpha_raw": ALPHA_RAW,
        "alpha_corrected": ALPHA_CORRECTED,
        "n_comparisons": N_COMPARISONS_BONFERRONI,
        "verdict": (
            f"H1 CORROBORADA: B4 < B1 em D1 para {b4_wins}/4 modelos (p < {ALPHA_CORRECTED})"
            if h1_corroborated
            else f"H1 NÃO CORROBORADA: B4 < B1 em apenas {b4_wins}/4 modelos com Bonferroni"
        ),
    }
    print(f"\n  → {results['conclusion']['verdict']}")

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Resultados H1 salvos em {out}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="McNemar H1 — efeito de ancoragem D1")
    parser.add_argument("--d1", required=True, help="Parquet com scores D1 por job")
    parser.add_argument("--output", default="experiments/adversarial_clt/results/h1_mcnemar.json")
    args = parser.parse_args()

    run_h1_mcnemar(d1_path=args.d1, output_path=args.output)
