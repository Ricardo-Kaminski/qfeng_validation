"""Entry point para ``python -m qfeng.c1_digestion.deontic``."""

from __future__ import annotations

import argparse
import logging
import re
from pathlib import Path

from qfeng.c1_digestion.deontic.batch import run_e2_batch

# Keywords do case Manaus — filtra portarias de consolidação
MANAUS_CASE_KEYWORDS = [
    # Oxigênio e insumos críticos
    "oxigênio", "oxigenio", "insumo crítico", "gases medicinais",
    # UTI e leitos críticos
    "uti", "terapia intensiva", "leito de retaguarda", "leitos de uti",
    # Urgência e emergência
    "urgência e emergência", "SAMU", "UPA", "pronto-socorro",
    "rede de urgência", "porta de entrada",
    # Vigilância e epidemiologia
    "vigilância epidemiológica", "vigilância em saúde",
    "notificação compulsória", "ESPIN", "COES",
    "emergência em saúde pública",
    # Gestão hospitalar e regulação
    "regulação de leitos", "central de regulação", "gestão hospitalar",
    "capacidade instalada", "taxa de ocupação",
    # Responsabilização
    "responsabilização", "auditoria", "prestação de contas",
    # Logística
    "logística de distribuição", "cadeia de suprimento",
    # Atenção especializada
    "atenção especializada", "alta complexidade", "média complexidade",
    # Indicadores e monitoramento
    "indicador de desempenho", "monitoramento",
    "alerta epidemiológico", "sinal de alerta",
]


def main() -> None:
    """CLI para execução do batch E2."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="E2 — Extração deontica de NormChunks via LLM"
    )
    parser.add_argument(
        "--corpus-dir",
        type=Path,
        default=Path("outputs/e1_chunks"),
        help="Diretório com JSONs do E1 (default: outputs/e1_chunks/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/deontic_cache"),
        help="Diretório de cache (default: outputs/deontic_cache/)",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("outputs/e2_report.md"),
        help="Caminho para o relatório (default: outputs/e2_report.md)",
    )
    parser.add_argument(
        "--anchor-only",
        action="store_true",
        help="Processar apenas documentos-âncora",
    )
    parser.add_argument(
        "--filter-manaus",
        action="store_true",
        help="Filtrar portarias por keywords do case Manaus",
    )
    parser.add_argument(
        "--files",
        nargs="*",
        type=Path,
        help="Arquivos JSON específicos a processar",
    )
    args = parser.parse_args()

    anchor_files = args.files
    if args.anchor_only and not anchor_files:
        anchor_files = [
            args.corpus_dir / "brasil" / "lei_8080_1990.json",
            args.corpus_dir / "brasil" / "CF88_completa.json",
            args.corpus_dir / "brasil" / "lei_13709_2018.json",
            args.corpus_dir / "eu" / "eu_ai_act_2024_1689.json",
            args.corpus_dir / "usa" / "ssa_title_xix_1902.json",
        ]

    chunk_filter = None
    if args.filter_manaus:
        chunk_filter = re.compile(
            "|".join(re.escape(k) for k in MANAUS_CASE_KEYWORDS),
            re.IGNORECASE,
        )

    result = run_e2_batch(
        corpus_dir=args.corpus_dir,
        cache_dir=args.output_dir,
        report_path=args.report,
        anchor_files=anchor_files,
        chunk_filter=chunk_filter,
    )

    print(f"\nE2 concluído: {result.total_atoms_extracted} atoms "
          f"de {result.total_chunks_processed} chunks")
    print(f"  Cache hits: {result.cache_hits}")
    print(f"  LLM calls: {result.llm_calls}")
    print(f"  Chunks com 0 atoms: {len(result.zero_atom_chunks)}")
    if result.low_confidence_atoms:
        print(f"  Alertas (confidence < 0.5): {len(result.low_confidence_atoms)}")
    print(f"\nRelatório: {args.report}")


main()
