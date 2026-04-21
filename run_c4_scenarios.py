"""Run C4a/C4b LLM scenarios and update llm_comparison.parquet.

Usage:
    python run_c4_scenarios.py
"""

import sys
import logging
import pathlib

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("c4_runner")

import pandas as pd
import numpy as np

OUTPUT_DIR = pathlib.Path("C:/Workspace/academico/qfeng_validacao/outputs/e5_results")
OUTPUT_PATH = OUTPUT_DIR / "llm_comparison.parquet"

sys.path.insert(0, "C:/Workspace/academico/qfeng_validacao/src")

from qfeng.e5_symbolic.c4_llm_runner import (
    run_c4,
    C4_ACTIONS,
    NORMATIVELY_CORRECT_ACTIONS,
)


def main():
    log.info("=" * 60)
    log.info("C4 LLM Scenarios — Qwen2.5:14b via Ollama")
    log.info("=" * 60)

    rows = run_c4()

    df = pd.DataFrame(rows)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False, engine="pyarrow")
    size_kb = OUTPUT_PATH.stat().st_size / 1024
    log.info("Saved %s (%d rows, %.1f KB)", OUTPUT_PATH.name, len(df), size_kb)

    # ── Summary report ────────────────────────────────────────────
    c4a = df[df["scenario_id"] == "C4a"]
    c4b = df[df["scenario_id"] == "C4b"]

    print()
    print("=" * 60)
    print("C4 RESULTS — THETA PER QUERY")
    print("=" * 60)
    print(f"{'Q':>2}  {'theta_C4a':>10} {'action_C4a':<22} {'correct_a':>9}  |"
          f"  {'theta_C4b':>10} {'action_C4b':<22} {'correct_b':>9}  delta")
    print("-" * 100)

    corrections = []
    for qid in range(1, 9):
        row_a = c4a[c4a["query_id"] == qid].iloc[0] if not c4a[c4a["query_id"] == qid].empty else None
        row_b = c4b[c4b["query_id"] == qid].iloc[0] if not c4b[c4b["query_id"] == qid].empty else None
        if row_a is None or row_b is None:
            continue
        delta = row_b["reduction_delta"]
        delta_str = f"{delta:+.1f}" if delta is not None else "N/A"
        corrected = (not row_a["action_normatively_correct"]) and row_b["action_normatively_correct"]
        flag = " <-- CORRECTED" if corrected else ""
        if corrected:
            corrections.append(qid)
        print(
            f"{qid:>2}  {row_a['theta_deg']:>10.1f} {row_a['action_recommended']:<22} "
            f"{'Yes' if row_a['action_normatively_correct'] else 'No':>9}  |"
            f"  {row_b['theta_deg']:>10.1f} {row_b['action_recommended']:<22} "
            f"{'Yes' if row_b['action_normatively_correct'] else 'No':>9}  {delta_str}{flag}"
        )

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    mean_4a = c4a["theta_deg"].mean()
    mean_4b = c4b["theta_deg"].mean()
    mean_delta = c4b["reduction_delta"].dropna().mean()

    correct_4a = c4a["action_normatively_correct"].sum()
    correct_4b = c4b["action_normatively_correct"].sum()

    print(f"  theta medio C4a:          {mean_4a:.1f} deg")
    print(f"  theta medio C4b:          {mean_4b:.1f} deg")
    print(f"  reduction_delta medio:    {mean_delta:+.1f} deg")
    print(f"  actions corretas C4a:     {correct_4a}/8")
    print(f"  actions corretas C4b:     {correct_4b}/8")
    print(f"  queries corrigidas C4a->C4b: {corrections}")
    print()
    print(f"  Parquet: {OUTPUT_PATH.name}  ({size_kb:.1f} KB, {len(df)} rows)")
    print()


if __name__ == "__main__":
    main()
