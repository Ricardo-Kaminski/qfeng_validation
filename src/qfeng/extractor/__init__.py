"""Q-FENG Symbolic Facts Extractor (passthrough manual).

Componente arquitetonico Q-FENG responsavel por converter scenario_text em
fatos ASP grounded. A extracao em si eh executada por Claude Opus 4.7 em
sessao de chat supervisionada (P_FASE2.0); este modulo apenas:

    (a) define o schema Pydantic do output esperado (schema.py);
    (b) prove cache idempotente por scenario_id (cache.py);
    (c) traduz JSON -> ASP (.lp) deterministicamente (render_to_asp em schema.py).

Cache:  corpora_clingo/extracted_facts/{scenario_id}.lp
        corpora_clingo/extracted_facts/{scenario_id}_meta.json

Documentado no paper como componente da arquitetura sob avaliacao (nao como
capacidade dos modelos comparados Qwen/Phi-4/Gemma/Llama).

Historico: o cliente Anthropic API original (claude_extractor.py) e o
prompt_template.md foram arquivados em _archive_pre_passthrough/ apos
mudanca arquitetonica para passthrough manual (Decisao 2, 29/abr/2026).
Veja _archive_pre_passthrough/README.md para detalhes.
"""
from qfeng.extractor.cache import get_cached_facts, store_cached_facts, cache_status
from qfeng.extractor.schema import (
    FactAtom,
    ScenarioExtraction,
    render_to_asp,
)

__all__ = [
    "FactAtom",
    "ScenarioExtraction",
    "render_to_asp",
    "get_cached_facts",
    "store_cached_facts",
    "cache_status",
]
