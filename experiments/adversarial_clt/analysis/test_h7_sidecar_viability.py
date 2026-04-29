"""H7 — Governance sidecar viability (emenda §12, 28/abr/2026).

Testa se o overhead operacional do motor Q-FENG é menor que 5% do tempo total
da chamada, em mediana, para todos os 4 modelos LLM testados.

H₇: mediana(overhead_qfeng_ms) / mediana(latency_ms) < 0.05 ∀ modelo

overhead_qfeng_ms = t_clingo_ms + t_psi_build_ms + t_theta_compute_ms
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

THRESHOLD_VIABILITY = 0.05  # 5%
ARM_COL_CANDIDATES = ("arm", "braco")
MODEL_COL_CANDIDATES = ("model", "modelo")


def _col(df: pd.DataFrame, candidates: tuple) -> str:
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(f"Nenhuma coluna encontrada: {candidates}")


def run_h7_sidecar_viability(
    results_parquet: str | Path,
    output_path: str | Path | None = None,
) -> dict:
    """Computa overhead Q-FENG por modelo e verifica H7."""
    df = pd.read_parquet(results_parquet)
    arm_col = _col(df, ARM_COL_CANDIDATES)
    model_col = _col(df, MODEL_COL_CANDIDATES)

    df_b5 = df[df[arm_col] == "B5"].copy()

    if df_b5.empty:
        result = {
            "test": "H7 — Governance sidecar viability",
            "threshold": THRESHOLD_VIABILITY,
            "by_model": [],
            "h7_supported": None,
            "interpretation": "Sem dados B5 — executar B5 primeiro",
        }
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
        return result

    df_b5["overhead_qfeng_ms"] = (
        df_b5["t_clingo_ms"].fillna(0)
        + df_b5["t_psi_build_ms"].fillna(0)
        + df_b5["t_theta_compute_ms"].fillna(0)
    )

    by_model = (
        df_b5.groupby(model_col)
        .agg(
            n=("latency_ms", "size"),
            median_overhead_ms=("overhead_qfeng_ms", "median"),
            median_latency_ms=("latency_ms", "median"),
            median_t_clingo_ms=("t_clingo_ms", "median"),
            median_t_psi_build_ms=("t_psi_build_ms", "median"),
            median_t_theta_compute_ms=("t_theta_compute_ms", "median"),
            median_t_llm_ms=("t_llm_ms", "median"),
        )
        .reset_index()
    )
    by_model["overhead_ratio"] = (
        by_model["median_overhead_ms"] / by_model["median_latency_ms"]
    )
    by_model["h7_viable"] = by_model["overhead_ratio"] < THRESHOLD_VIABILITY

    h7_supported = bool(by_model["h7_viable"].all())

    result = {
        "test": "H7 — Governance sidecar viability",
        "threshold": THRESHOLD_VIABILITY,
        "by_model": by_model.to_dict(orient="records"),
        "h7_supported": h7_supported,
        "conclusion": {
            "verdict": "SUSTENTADA" if h7_supported else "FALSIFICADA",
            "h7_supported": h7_supported,
        },
        "interpretation": (
            "H7 sustentada — overhead Q-FENG < 5% do tempo total em todos os modelos; "
            "viabilidade do governance sidecar empiricamente sustentada"
            if h7_supported
            else "H7 falsificada — em ao menos um modelo, overhead Q-FENG >= 5%"
        ),
    }

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False, default=str)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-parquet", required=True)
    parser.add_argument("--output-path", default=None)
    args = parser.parse_args()

    result = run_h7_sidecar_viability(args.results_parquet, args.output_path)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
