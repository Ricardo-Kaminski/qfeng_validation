"""H5: Variabilidade intra-(modelo, cenário) — Levene + bootstrap overlap.

H5a: Levene — B3 tem menor variância que B1 e B2
H5b: Bootstrap — fração de (modelo, cenário) com IC95% B3 e B1 sem sobreposição
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


def bootstrap_ci(values: np.ndarray, n: int = 10_000, ci: float = 0.95, seed: int = 42) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    boots = rng.choice(values, size=(n, len(values)), replace=True).mean(axis=1)
    lo = float(np.percentile(boots, (1 - ci) / 2 * 100))
    hi = float(np.percentile(boots, (1 + ci) / 2 * 100))
    return lo, hi


def run_h5() -> dict:
    df = pd.read_parquet(DERIVED)

    # H5a: Levene — variância intra-(modelo, cenário, braço)
    var_intra = (
        df.groupby(["braco", "modelo", "scenario_id"])["hallucination_flag"]
        .var(ddof=1)
        .reset_index()
        .rename(columns={"hallucination_flag": "var_hall"})
    )

    b1_vars = var_intra[var_intra["braco"] == "B1"]["var_hall"].dropna().values
    b2_vars = var_intra[var_intra["braco"] == "B2"]["var_hall"].dropna().values
    b3_vars = var_intra[var_intra["braco"] == "B3"]["var_hall"].dropna().values
    b4_vars = var_intra[var_intra["braco"] == "B4"]["var_hall"].dropna().values

    stat_b3_b1, p_b3_b1 = stats.levene(b3_vars, b1_vars, center="median")
    stat_b3_b2, p_b3_b2 = stats.levene(b3_vars, b2_vars, center="median")
    stat_b3_b4, p_b3_b4 = stats.levene(b3_vars, b4_vars, center="median")

    # H5b: Bootstrap overlap por (modelo, cenário)
    overlap_b3_b1: list[dict] = []
    b13 = df[df["braco"].isin(["B1", "B3"])]
    for (modelo, scenario_id), grp in b13.groupby(["modelo", "scenario_id"]):
        b1_v = grp[grp["braco"] == "B1"]["hallucination_flag"].values
        b3_v = grp[grp["braco"] == "B3"]["hallucination_flag"].values
        if len(b1_v) < 2 or len(b3_v) < 2:
            continue
        ci_b1 = bootstrap_ci(b1_v.astype(float))
        ci_b3 = bootstrap_ci(b3_v.astype(float))
        no_overlap = (ci_b3[1] < ci_b1[0]) or (ci_b1[1] < ci_b3[0])
        overlap_b3_b1.append({
            "modelo": modelo,
            "scenario_id": scenario_id,
            "ci_b1": list(ci_b1),
            "ci_b3": list(ci_b3),
            "no_overlap": bool(no_overlap),
        })

    n_pairs = len(overlap_b3_b1)
    n_no_overlap = sum(1 for o in overlap_b3_b1 if o["no_overlap"])
    frac_no_overlap = n_no_overlap / n_pairs if n_pairs > 0 else 0.0

    out = {
        "hipotese": "H5",
        "comparacao": "Variabilidade intra-(modelo, cenário): B3 vs B1/B2/B4",
        "h5a_levene": {
            "var_b1_mean": float(np.mean(b1_vars)),
            "var_b2_mean": float(np.mean(b2_vars)),
            "var_b3_mean": float(np.mean(b3_vars)),
            "var_b4_mean": float(np.mean(b4_vars)),
            "b3_vs_b1": {
                "statistic": float(stat_b3_b1),
                "p_value": float(p_b3_b1),
                "significant": bool(p_b3_b1 < ALPHA),
                "b3_menor_var": bool(np.mean(b3_vars) < np.mean(b1_vars)),
            },
            "b3_vs_b2": {
                "statistic": float(stat_b3_b2),
                "p_value": float(p_b3_b2),
                "significant": bool(p_b3_b2 < ALPHA),
                "b3_menor_var": bool(np.mean(b3_vars) < np.mean(b2_vars)),
            },
            "b3_vs_b4": {
                "statistic": float(stat_b3_b4),
                "p_value": float(p_b3_b4),
                "significant": bool(p_b3_b4 < ALPHA),
            },
        },
        "h5b_bootstrap_overlap": {
            "n_pares_modelo_cenario": n_pairs,
            "n_no_overlap": n_no_overlap,
            "frac_no_overlap_b3_b1": float(frac_no_overlap),
            "interpretation": (
                f"IC95%(B3) e IC95%(B1) sem sobreposição em "
                f"{frac_no_overlap*100:.1f}% dos {n_pairs} pares (modelo, cenário)."
            ),
        },
        "alpha_bonferroni_m8": ALPHA,
        "interpretation": (
            f"Var intra média: B1={np.mean(b1_vars):.4f}, B2={np.mean(b2_vars):.4f}, "
            f"B3={np.mean(b3_vars):.4f}, B4={np.mean(b4_vars):.4f}. "
            f"Levene B3 vs B1: p={p_b3_b1:.4g} "
            f"({'sig.' if p_b3_b1 < ALPHA else 'n.s.'}). "
            f"Bootstrap overlap: B3/B1 sem sobreposição em {frac_no_overlap*100:.1f}% dos pares."
        ),
    }

    (OUTPUT_DIR / "h5_result.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    # Salva breakdown completo separado (pode ser grande)
    (OUTPUT_DIR / "h5_bootstrap_pairs.json").write_text(
        json.dumps(overlap_b3_b1, indent=1, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k != "h5b_bootstrap_overlap"}, indent=2, ensure_ascii=False))
    print(f"\nh5b bootstrap: {n_no_overlap}/{n_pairs} pares sem sobreposição "
          f"({frac_no_overlap*100:.1f}%)")
    return out


if __name__ == "__main__":
    run_h5()
