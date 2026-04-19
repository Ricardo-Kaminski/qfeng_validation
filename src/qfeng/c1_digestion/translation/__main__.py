"""E3 — CLI entry point.

Usage:
    python -m qfeng.c1_digestion.translation \\
        --deontic-dir outputs/deontic_cache/ \\
        --scope configs/sus_validacao.yaml \\
        --concurrency-map outputs/e1_chunks_scoped/concurrency_map.json \\
        --output-dir outputs/e3_predicates/
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path

from qfeng.c1_digestion.scope.config import load_scope
from qfeng.c1_digestion.translation.runner import run_e3_batch

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="E3 — Traduz DeonticAtoms do cache E2 em ClingoPredicates (.lp)"
    )
    parser.add_argument(
        "--deontic-dir",
        type=Path,
        default=Path("outputs/deontic_cache"),
        help="Diretório do cache E2 (default: outputs/deontic_cache/)",
    )
    parser.add_argument(
        "--scope",
        type=Path,
        required=True,
        help="Perfil YAML de escopo (ex: configs/sus_validacao.yaml)",
    )
    parser.add_argument(
        "--concurrency-map",
        type=Path,
        default=Path("outputs/e1_chunks_scoped/concurrency_map.json"),
        help="Mapa de concorrências E1 (default: outputs/e1_chunks_scoped/concurrency_map.json)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/e3_predicates"),
        help="Diretório de saída para arquivos .lp (default: outputs/e3_predicates/)",
    )
    args = parser.parse_args()

    scope = load_scope(args.scope)
    result = run_e3_batch(
        deontic_dir=args.deontic_dir,
        output_dir=args.output_dir,
        scope=scope,
        concurrency_map_path=args.concurrency_map,
    )

    logger.info("E3 concluído:")
    logger.info("  atoms processados:  %d", result.total_atoms)
    logger.info("  predicados gerados: %d", result.total_predicates)
    logger.info("  syntax_valid:       %d", result.syntax_valid)
    logger.info("  syntax_invalid:     %d", result.syntax_invalid)
    logger.info("  concurrent_facts:   %d", result.concurrent_facts)
    if result.warnings:
        logger.warning("  avisos: %d", len(result.warnings))
    for regime, count in sorted(result.predicates_per_regime.items()):
        logger.info("  %s: %d predicados", regime, count)


if __name__ == "__main__":
    main()
