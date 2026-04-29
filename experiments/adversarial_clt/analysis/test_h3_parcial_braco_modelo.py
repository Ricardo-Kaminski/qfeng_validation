"""H3 parcial: ANOVA two-way braço × modelo — B1-B4 apenas.

Status: PARCIAL — análise final com B5 incluído será executada em B5.10.
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


def run_h3_parcial() -> dict:
    df = pd.read_parquet(DERIVED)

    model = ols("hallucination_flag ~ C(braco) * C(modelo)", data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    ss_res = anova_table.loc["Residual", "sum_sq"]
    eta_sq = {
        idx: float(row["sum_sq"] / (row["sum_sq"] + ss_res))
        for idx, row in anova_table.iterrows()
        if idx != "Residual"
    }

    interacao_sig = bool(anova_table.loc["C(braco):C(modelo)", "PR(>F)"] < ALPHA)

    # Tukey pairwise por braço
    tukey_braco = pairwise_tukeyhsd(df["hallucination_flag"], df["braco"], alpha=0.05)
    tukey_modelo = pairwise_tukeyhsd(df["hallucination_flag"], df["modelo"], alpha=0.05)

    def tukey_to_list(tukey) -> list[dict]:
        rows = []
        for row in tukey._results_table.data[1:]:
            rows.append({
                "group1": str(row[0]),
                "group2": str(row[1]),
                "meandiff": float(row[2]),
                "p_adj": float(row[3]),
                "reject": bool(row[6]),
            })
        return rows

    # Taxa por (braço, modelo)
    rate_table = (
        df.groupby(["braco", "modelo"])["hallucination_flag"]
        .mean()
        .unstack()
        .round(3)
        .to_dict()
    )

    out = {
        "hipotese": "H3",
        "status": "parcial_b1_b4_apenas",
        "nota": "Análise final com B5 incluído será executada em B5.10 após B5=600/600.",
        "comparacao": "ANOVA two-way braço × modelo — taxa de alucinação (B1-B4)",
        "n_total": int(len(df)),
        "anova_two_way": {
            "F_braco": float(anova_table.loc["C(braco)", "F"]),
            "p_braco": float(anova_table.loc["C(braco)", "PR(>F)"]),
            "F_modelo": float(anova_table.loc["C(modelo)", "F"]),
            "p_modelo": float(anova_table.loc["C(modelo)", "PR(>F)"]),
            "F_interacao": float(anova_table.loc["C(braco):C(modelo)", "F"]),
            "p_interacao": float(anova_table.loc["C(braco):C(modelo)", "PR(>F)"]),
            "eta_sq_partial": eta_sq,
        },
        "rate_by_braco_modelo": rate_table,
        "tukey_braco": tukey_to_list(tukey_braco),
        "tukey_modelo": tukey_to_list(tukey_modelo),
        "alpha_bonferroni_m8": ALPHA,
        "interacao_braco_modelo_significativa": interacao_sig,
        "interpretation": (
            f"ANOVA two-way (B1-B4): F_braço={anova_table.loc['C(braco)', 'F']:.2f} "
            f"(p={anova_table.loc['C(braco)', 'PR(>F)']:.4g}), "
            f"F_modelo={anova_table.loc['C(modelo)', 'F']:.2f} "
            f"(p={anova_table.loc['C(modelo)', 'PR(>F)']:.4g}), "
            f"F_interação={anova_table.loc['C(braco):C(modelo)', 'F']:.2f} "
            f"(p={anova_table.loc['C(braco):C(modelo)', 'PR(>F)']:.4g}, "
            f"{'sig.' if interacao_sig else 'n.s.'} a α=0.00625). "
            f"η²_braço={eta_sq.get('C(braco)',0):.3f}. "
            f"PARCIAL: requer B5 para análise final."
        ),
    }

    (OUTPUT_DIR / "h3_parcial_result.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False, default=str), encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in out.items() if k not in ("tukey_braco", "tukey_modelo")}, indent=2, ensure_ascii=False, default=str))
    return out


if __name__ == "__main__":
    run_h3_parcial()
