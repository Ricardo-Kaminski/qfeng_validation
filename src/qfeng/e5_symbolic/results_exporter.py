"""Exports E5 results to paper-grade parquet files.

Output directory: outputs/e5_results/
  - validation_results.parquet
  - theta_efetivo_manaus.parquet
  - llm_comparison.parquet
"""

from __future__ import annotations

import logging
import pathlib

import pandas as pd

log = logging.getLogger(__name__)


def export_all(
    validation_rows: list[dict],
    manaus_rows: list[dict],
    llm_rows: list[dict],
    output_dir: pathlib.Path,
    threshold_rows: list[dict] | None = None,
    psi_sensitivity_rows: list[dict] | None = None,
    manaus_ci_rows: list[dict] | None = None,
) -> dict[str, pathlib.Path]:
    """Write all three parquet files. Returns dict of filename → path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: dict[str, pathlib.Path] = {}

    # 1. Main validation results
    df_val = pd.DataFrame(validation_rows)
    p_val = output_dir / "validation_results.parquet"
    df_val.to_parquet(p_val, index=False, engine="pyarrow")
    paths["validation_results"] = p_val
    log.info("Saved %s (%d rows, %.1f KB)", p_val.name, len(df_val), p_val.stat().st_size / 1024)

    # 2. Manaus theta_efetivo time series
    df_man = pd.DataFrame(manaus_rows)
    p_man = output_dir / "theta_efetivo_manaus.parquet"
    df_man.to_parquet(p_man, index=False, engine="pyarrow")
    paths["theta_efetivo_manaus"] = p_man
    log.info("Saved %s (%d rows, %.1f KB)", p_man.name, len(df_man), p_man.stat().st_size / 1024)

    # 3. LLM comparison (may be stub if Ollama unavailable)
    df_llm = pd.DataFrame(llm_rows)
    p_llm = output_dir / "llm_comparison.parquet"
    df_llm.to_parquet(p_llm, index=False, engine="pyarrow")
    paths["llm_comparison"] = p_llm
    log.info("Saved %s (%d rows, %.1f KB)", p_llm.name, len(df_llm), p_llm.stat().st_size / 1024)

    # Optional robustness datasets (Fix 2, 3, 5)
    _optional = [
        ("threshold_robustness", threshold_rows),
        ("psi_sensitivity",      psi_sensitivity_rows),
        ("manaus_bootstrap_ci",  manaus_ci_rows),
    ]
    for name, rows in _optional:
        if rows:
            p = output_dir / f"{name}.parquet"
            pd.DataFrame(rows).to_parquet(p, index=False, engine="pyarrow")
            paths[name] = p
            log.info("Saved %s (%d rows, %.1f KB)", p.name, len(rows), p.stat().st_size / 1024)

    return paths


def print_summary(
    validation_rows: list[dict],
    manaus_rows: list[dict],
    paths: dict[str, pathlib.Path],
) -> None:
    """Print the paper-grade results table to stdout."""
    print()
    print("=" * 72)
    print("E5 SYMBOLIC TESTING -- Q-FENG VALIDATION RESULTS")
    print("=" * 72)
    print()

    # Main results table
    header = f"{'Cenario':<12} {'theta_deg':>9} {'Regime':<17} {'SAT':>5} {'n_sov':>5} {'Loss':>6}  Fonte"
    print(header)
    print("-" * 72)
    for row in validation_rows:
        sat_str = "SAT" if row["clingo_sat"] else "UNSAT"
        print(
            f"{row['scenario_id']:<12} "
            f"{row['theta_deg']:>7.1f} "
            f"{row['interference_regime']:<17} "
            f"{sat_str:>5} "
            f"{row['n_sovereign_active']:>5} "
            f"{row['cybernetic_loss']:>6.3f}  "
            f"{row['data_source']}"
        )

    print()
    print("=" * 72)
    print("TRAJETORIA theta_efetivo - MANAUS 2020-2021 (Markoviano Kaminski)")
    print("=" * 72)
    print()
    hdr2 = f"{'Compet.':>8} {'theta_t':>8} {'theta_eff':>10} {'alpha':>7} {'Regime':<17} {'score_P':>8} {'Crítico':>8}"
    print(hdr2)
    print("-" * 72)
    for row in manaus_rows:
        crit = "<-- COLAPSO O2" if row["evento_critico"] else ""
        print(
            f"{row['competencia']:>8} "
            f"{row['theta_t']:>8.1f} "
            f"{row['theta_efetivo']:>10.1f} "
            f"{row['alpha_t']:>7.3f} "
            f"{row['interference_regime']:<17} "
            f"{row['score_pressao']:>8.2f} "
            f"{crit}"
        )

    print()
    print("=" * 72)
    print("OUTPUTS GERADOS")
    print("=" * 72)
    for name, path in paths.items():
        size_kb = path.stat().st_size / 1024
        print(f"  {name:<30} {path.name}  ({size_kb:.1f} KB)")
    print()
