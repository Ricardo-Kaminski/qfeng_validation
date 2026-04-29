"""H8 — Motor de interferência θ (B5) vs. ancoragem simbólica (B4) (emenda §12, 28/abr/2026).

H8a: D1(B5) != D1(B4), Wilcoxon signed-rank pareado por cenário, alpha=0.00625
H8b: D3(B5) > D3(B4), Wilcoxon signed-rank pareado por cenário, alpha=0.00625

Critério de evidência: pelo menos uma das duas hipóteses sustentada para que
H8 (família) seja considerada sustentada.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ALPHA_BONFERRONI = 0.05 / 8  # m=8 hipóteses confirmatórias pós-emenda §12
ARM_COL_CANDIDATES = ("arm", "braco")
MODEL_COL_CANDIDATES = ("model", "modelo")


def _col(df: pd.DataFrame, candidates: tuple) -> str:
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(f"Nenhuma coluna encontrada: {candidates}")


def run_h8_motor_vs_anchoring(
    d1_path: str | Path,
    d3_path: str | Path,
    output_path: str | Path | None = None,
) -> dict:
    """Wilcoxon pareado D1(B5) vs D1(B4) e D3(B5) vs D3(B4) por cenário."""
    df_d1_raw = (
        pd.read_parquet(d1_path) if str(d1_path).endswith(".parquet")
        else pd.read_csv(d1_path)
    )
    df_d3_raw = (
        pd.read_parquet(d3_path) if str(d3_path).endswith(".parquet")
        else pd.read_csv(d3_path)
    )

    arm_col_d1 = _col(df_d1_raw, ARM_COL_CANDIDATES)
    arm_col_d3 = _col(df_d3_raw, ARM_COL_CANDIDATES)

    # Normalizar nome de coluna de braço para "arm"
    df_d1 = df_d1_raw.rename(columns={arm_col_d1: "arm"})
    df_d3 = df_d3_raw.rename(columns={arm_col_d3: "arm"})

    def _pair(df: pd.DataFrame, metric_col: str) -> tuple[np.ndarray, np.ndarray]:
        """Parear B4 e B5 por (scenario_id, model, run_id)."""
        model_col = _col(df, MODEL_COL_CANDIDATES)
        df = df.rename(columns={model_col: "model"})

        df_b4 = df[df["arm"] == "B4"][["scenario_id", "model", "run_id", metric_col]]
        df_b5 = df[df["arm"] == "B5"][["scenario_id", "model", "run_id", metric_col]]

        if df_b4.empty or df_b5.empty:
            return np.array([]), np.array([])

        merged = df_b4.merge(
            df_b5,
            on=["scenario_id", "model", "run_id"],
            suffixes=("_b4", "_b5"),
        )
        return merged[f"{metric_col}_b5"].values, merged[f"{metric_col}_b4"].values

    # H8a: D1
    d1_metric = "d1_score" if "d1_score" in df_d1.columns else df_d1.columns[-1]
    d1_b5, d1_b4 = _pair(df_d1, d1_metric)

    if len(d1_b5) > 1 and not np.allclose(d1_b5, d1_b4):
        stat_h8a, p_h8a = stats.wilcoxon(d1_b5, d1_b4, alternative="two-sided")
    else:
        stat_h8a, p_h8a = float("nan"), float("nan")
    h8a_supported = bool((p_h8a < ALPHA_BONFERRONI) if not np.isnan(p_h8a) else False)

    # H8b: D3
    d3_metric = "d3_score" if "d3_score" in df_d3.columns else df_d3.columns[-1]
    d3_b5, d3_b4 = _pair(df_d3, d3_metric)

    if len(d3_b5) > 1 and not np.allclose(d3_b5, d3_b4):
        stat_h8b, p_h8b = stats.wilcoxon(d3_b5, d3_b4, alternative="greater")
    else:
        stat_h8b, p_h8b = float("nan"), float("nan")
    h8b_supported = bool((p_h8b < ALPHA_BONFERRONI) if not np.isnan(p_h8b) else False)

    h8_family_supported = bool(h8a_supported or h8b_supported)

    result = {
        "test": "H8 — Motor theta (B5) vs. ancoragem simbolica (B4)",
        "alpha_bonferroni": ALPHA_BONFERRONI,
        "n_paired_d1": int(len(d1_b5)),
        "n_paired_d3": int(len(d3_b5)),
        "h8a_d1": {
            "wilcoxon_stat": float(stat_h8a) if not np.isnan(stat_h8a) else None,
            "p_value": float(p_h8a) if not np.isnan(p_h8a) else None,
            "supported": bool(h8a_supported),
            "median_d1_b5": float(np.median(d1_b5)) if len(d1_b5) else None,
            "median_d1_b4": float(np.median(d1_b4)) if len(d1_b4) else None,
        },
        "h8b_d3": {
            "wilcoxon_stat": float(stat_h8b) if not np.isnan(stat_h8b) else None,
            "p_value": float(p_h8b) if not np.isnan(p_h8b) else None,
            "supported": bool(h8b_supported),
            "median_d3_b5": float(np.median(d3_b5)) if len(d3_b5) else None,
            "median_d3_b4": float(np.median(d3_b4)) if len(d3_b4) else None,
        },
        "h8_family_supported": h8_family_supported,
        "conclusion": {
            "verdict": "SUSTENTADA" if h8_family_supported else "FALSIFICADA",
            "h8_family_supported": h8_family_supported,
            "h8a_supported": h8a_supported,
            "h8b_supported": h8b_supported,
        },
        "interpretation": (
            "H8 sustentada — motor theta produz metricas distintas de B4"
            if h8_family_supported
            else "H8 falsificada — sem evidencia de diferenca motor theta vs ancoragem"
        ),
    }

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False, default=str)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--d1-path", required=True)
    parser.add_argument("--d3-path", required=True)
    parser.add_argument("--output-path", default=None)
    args = parser.parse_args()

    result = run_h8_motor_vs_anchoring(args.d1_path, args.d3_path, args.output_path)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
