"""Cache idempotente para fatos extraídos por cenário.

Política: um arquivo por scenario_id em corpora_clingo/extracted_facts/.
Sem TTL — fatos extraídos são estáveis (o cenário não muda).
Cache-hit retorna o .lp existente sem chamar a API.
"""
from __future__ import annotations
import json
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parents[4] / "corpora_clingo" / "extracted_facts"
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _lp_path(scenario_id: str) -> Path:
    safe = scenario_id.replace("/", "_").replace("\\", "_")
    return CACHE_DIR / f"{safe}.lp"


def _meta_path(scenario_id: str) -> Path:
    safe = scenario_id.replace("/", "_").replace("\\", "_")
    return CACHE_DIR / f"{safe}_meta.json"


def get_cached_facts(scenario_id: str) -> str | None:
    """Retorna conteúdo .lp se cache existir, None caso contrário."""
    p = _lp_path(scenario_id)
    return p.read_text(encoding="utf-8") if p.exists() else None


def store_cached_facts(scenario_id: str, facts_lp: str, meta: dict) -> None:
    """Persiste fatos .lp e metadados no cache."""
    _lp_path(scenario_id).write_text(facts_lp, encoding="utf-8")
    _meta_path(scenario_id).write_text(
        json.dumps(meta, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def cache_status() -> dict:
    """Retorna estatísticas do cache atual."""
    lp_files = list(CACHE_DIR.glob("*.lp"))
    return {
        "cache_dir": str(CACHE_DIR),
        "n_cached": len(lp_files),
        "scenario_ids": [f.stem for f in lp_files],
    }
