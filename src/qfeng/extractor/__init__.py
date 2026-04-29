"""Q-FENG Extrator: cenário texto → predicados ASP via Claude Sonnet.

Componente da pipeline B3-novo e B4-novo. Primeira chamada real em P_FASE2.
"""
from qfeng.extractor.claude_extractor import extract_facts, extract_facts_batch
from qfeng.extractor.cache import get_cached_facts, store_cached_facts, cache_status
from qfeng.extractor.schema import ScenarioExtraction, FactAtom, render_to_asp

__all__ = [
    "extract_facts",
    "extract_facts_batch",
    "get_cached_facts",
    "store_cached_facts",
    "cache_status",
    "ScenarioExtraction",
    "FactAtom",
    "render_to_asp",
]
