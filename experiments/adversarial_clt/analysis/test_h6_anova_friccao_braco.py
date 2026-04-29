"""H6: ANOVA two-way friccao_categoria × braco + post-hoc Tukey por categoria.

α Bonferroni m=8: 0.00625.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

DERIVED = Path(__file__).resolve().parents[1] / "results" / "results_b1_b4_derivado.parquet"
OUTPUT_DIR = Path(__file__).resolve().parents[0] / "resultados_h1_h6"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ALPHA = 0.00625


def _tukey_to_list(tukey) -> list[dict]:
    rows = []
    data = tukey._results_table.data[1:]
    for row in data:
        rows.append({
            "group1": str(row[0]),
            "group2": str(row[1]),
            "meandiff": float(row[2]),
            "p_adj": float(row[3]),
            "lower": float(row[4]),
            "upper": float(row[5]),
            "reject": bool(row[6]),
        })
    return rows


def run_h6() -> dict:
    df = pd.read_parquet(DERIVED)

    # Remover categoria 'test' (n=1) e NaN
    df["friccao_categoria"] = df["friccao_categoria"].astype(str).replace("nan", "")
    df_clean = df[~df["friccao_categoria"].isin(["test", "", "nan"])].copy()

    # ANOVA two-way
    model = ols(
        "hallucination_flag ~ C(friccao_categoria) * C(braco)",
        data=df_clean,
    ).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    # Eta² parcial
    ss_res = anova_table.loc["Residual", "sum_sq"]
    eta_sq = {
        idx: float(row["sum_sq"] / (row["sum_sq"] + ss_res))
        for idx, row in anova_table.iterrows()
        if idx != "Residual"
    }

    # Taxa de alucinação por (friccao, braco) — tabela descritiva
    rate_by_cat = (
        df_clean.groupby(["friccao_categoria", "braco"])["hallucination_flag"]
        .mean()
        .unstack()
        .round(3)
        .to_dict()
    )

    # Tukey HSD por categoria
    tukey_results: dict[str, dict] = {}
    for cat in sorted(str(c) for c in df_clean["friccao_categoria"].unique()):
        sub = df_clean[df_clean["friccao_categoria"] == cat]
        if sub["braco"].nunique() < 2:
            continue
        try:
            tukey = pairwise_tukeyhsd(sub["hallucination_flag"], sub["braco"], alpha=0.05)
            tukey_results[cat] = {
                "n": int(len(sub)),
                "n_by_braco": sub["braco"].value_counts().to_dict(),
                "mean_by_braco": sub.groupby("braco")["hallucination_flag"].mean().round(4).to_dict(),
                "comparisons": _tukey_to_list(tukey),
            }
        except Exception as exc:
            tukey_results[cat] = {"error": str(exc)}

    interacao_sig = bool(anova_table.loc["C(friccao_categoria):C(braco)", "PR(>F)"] < ALPHA)

    out = {
        "hipotese": "H6",
        "comparacao": "Interação friccao_categoria × braco para hallucination_flag",
        "n_total": int(len(df_clean)),
        "anova_two_way": {
            "F_friccao": float(anova_table.loc["C(friccao_categoria)", "F"]),
            "p_friccao": float(anova_table.loc["C(friccao_categoria)", "PR(>F)"]),
            "F_braco": float(anova_table.loc["C(braco)", "F"]),
            "p_braco": float(anova_table.loc["C(braco)", "PR(>F)"]),
            "F_interacao": float(anova_table.loc["C(friccao_categoria):C(braco)", "F"]),
            "p_interacao": float(anova_table.loc["C(friccao_categoria):C(braco)", "PR(>F)"]),
            "eta_sq_partial": eta_sq,
        },
        "rate_by_friccao_braco": rate_by_cat,
        "alpha_bonferroni_m8": ALPHA,
        "interacao_significativa": interacao_sig,
        "tukey_por_categoria": tukey_results,
        "interpretation": (
            f"ANOVA two-way: F_interação={anova_table.loc['C(friccao_categoria):C(braco)', 'F']:.2f}, "
            f"p={anova_table.loc['C(friccao_categoria):C(braco)', 'PR(>F)']:.4g} "
            f"({'significativo' if interacao_sig else 'NÃO significativo'} a α=0.00625). "
            f"F_braço={anova_table.loc['C(braco)', 'F']:.2f}, "
            f"p_braço={anova_table.loc['C(braco)', 'PR(>F)']:.4g}. "
            f"Efeito principal braço η²={eta_sq.get('C(braco)',0):.3f}."
        ),
    }

    (OUTPUT_DIR / "h6_result.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False, default=str), encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k != "tukey_por_categoria"}, indent=2, ensure_ascii=False, default=str))
    print(f"\nTukey por categoria: {list(tukey_results.keys())}")
    return out


if __name__ == "__main__":
    run_h6()
