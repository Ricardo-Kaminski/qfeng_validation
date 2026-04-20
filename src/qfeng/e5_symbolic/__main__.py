"""CLI entry point for E5 Symbolic Testing.

Usage:
    python -m qfeng.e5_symbolic --output-dir outputs/e5_results
"""

from __future__ import annotations

import argparse
import logging
import pathlib
import sys

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("e5_symbolic")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Q-FENG E5 Symbolic Testing")
    parser.add_argument(
        "--output-dir",
        default="outputs/e5_results",
        help="Directory for parquet outputs (default: outputs/e5_results)",
    )
    args = parser.parse_args(argv)

    output_dir = pathlib.Path(args.output_dir)

    from .runner import (
        run_all_scenarios,
        run_theta_efetivo_manaus,
        run_llm_comparison,
        run_threshold_sensitivity,
        run_psi_weight_sensitivity,
        run_manaus_bootstrap_ci,
    )
    from .results_exporter import export_all, print_summary

    log.info("E5 Symbolic Testing — starting")

    log.info("Phase 1/6: Running scenario corpus tests ...")
    validation_rows = run_all_scenarios()

    log.info("Phase 2/6: Computing Manaus theta_efetivo time series ...")
    manaus_rows = run_theta_efetivo_manaus()

    log.info("Phase 3/6: LLM comparison (Ollama optional) ...")
    llm_rows = run_llm_comparison()

    log.info("Phase 4/6: Threshold robustness sweep ...")
    threshold_rows = run_threshold_sensitivity(validation_rows)

    log.info("Phase 5/6: Psi weight sensitivity (Monte Carlo n=500) ...")
    psi_sensitivity_rows = run_psi_weight_sensitivity()

    log.info("Phase 6/6: Manaus bootstrap CI (n=500) ...")
    manaus_ci_rows = run_manaus_bootstrap_ci(manaus_rows)

    log.info("Exporting parquets to %s ...", output_dir)
    paths = export_all(
        validation_rows, manaus_rows, llm_rows, output_dir,
        threshold_rows=threshold_rows,
        psi_sensitivity_rows=psi_sensitivity_rows,
        manaus_ci_rows=manaus_ci_rows,
    )

    print_summary(validation_rows, manaus_rows, paths)

    log.info("E5 complete.")


if __name__ == "__main__":
    main()
