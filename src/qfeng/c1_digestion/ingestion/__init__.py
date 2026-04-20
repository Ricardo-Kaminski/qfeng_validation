"""E1 — Ingestion: PDF/HTML parsing, hierarchical chunking, metadata extraction."""

from qfeng.c1_digestion.ingestion.chunker import chunk_by_hierarchy
from qfeng.c1_digestion.ingestion.labels import conflict_label, human_label
from qfeng.c1_digestion.ingestion.parser import parse_document
from qfeng.c1_digestion.ingestion.registry import REGIME_CONFIGS, RegimeConfig
from qfeng.c1_digestion.ingestion.runner import run_e1_batch

__all__ = [
    "chunk_by_hierarchy",
    "conflict_label",
    "human_label",
    "parse_document",
    "run_e1_batch",
    "REGIME_CONFIGS",
    "RegimeConfig",
]
