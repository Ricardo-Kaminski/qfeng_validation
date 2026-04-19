"""E3 — Batch runner: deontic cache → Clingo .lp files."""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.c1_digestion.translation.translator import atom_to_predicate
from qfeng.core.schemas import ClingoPredicate, DeonticAtom

logger = logging.getLogger(__name__)


@dataclass
class E3BatchResult:
    total_atoms: int = 0
    total_predicates: int = 0
    syntax_valid: int = 0
    syntax_invalid: int = 0
    predicates_per_regime: dict[str, int] = field(default_factory=dict)
    concurrent_facts: int = 0
    warnings: list[str] = field(default_factory=list)


def _build_chunk_lookup(e1_dir: Path, scope: ScopeConfig) -> dict[str, tuple[str, str]]:
    """Return {chunk_id: (regime, source_stem)} from E1 output JSONs."""
    lookup: dict[str, tuple[str, str]] = {}
    for regime in scope.regimes:
        regime_dir = e1_dir / regime
        if not regime_dir.exists():
            continue
        for json_file in sorted(regime_dir.glob("*.json")):
            try:
                chunks = json.loads(json_file.read_text(encoding="utf-8"))
            except Exception as exc:
                logger.warning("Falha ao ler E1 JSON %s: %s", json_file.name, exc)
                continue
            for chunk in chunks:
                lookup[chunk["id"]] = (regime, json_file.stem)
    return lookup


def run_e3_batch(
    deontic_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,
    concurrency_map_path: Path,
) -> E3BatchResult:
    """Translate all DeonticAtoms in the E2 cache to ClingoPredicates.

    Args:
        deontic_dir: outputs/deontic_cache/ — each file is {chunk_id}.json
        output_dir: outputs/e3_predicates/ — per-regime .lp files written here
        scope: ScopeConfig — only regimes in scope.regimes are processed
        concurrency_map_path: outputs/e1_chunks_scoped/concurrency_map.json
            The parent directory is used as the E1 output root for chunk lookup.
    """
    result = E3BatchResult()
    e1_dir = concurrency_map_path.parent

    chunk_lookup = _build_chunk_lookup(e1_dir, scope)

    by_file: dict[tuple[str, str], list[ClingoPredicate]] = {}

    for cache_file in sorted(deontic_dir.glob("*.json")):
        try:
            raw_atoms = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception as exc:
            msg = f"Falha ao ler cache {cache_file.name}: {exc}"
            logger.warning(msg)
            result.warnings.append(msg)
            continue

        atoms = [DeonticAtom.model_validate(a) for a in raw_atoms]

        for atom in atoms:
            result.total_atoms += 1
            key = chunk_lookup.get(atom.source_chunk_id)
            if key is None:
                continue
            regime, source_stem = key

            pred = atom_to_predicate(atom)
            result.total_predicates += 1
            if pred.syntax_valid:
                result.syntax_valid += 1
            else:
                result.syntax_invalid += 1
                msg = f"syntax_invalid: atom {atom.id} (chunk {atom.source_chunk_id})"
                logger.warning(msg)
                result.warnings.append(msg)

            result.predicates_per_regime[regime] = (
                result.predicates_per_regime.get(regime, 0) + 1
            )
            by_file.setdefault((regime, source_stem), []).append(pred)

    output_dir.mkdir(parents=True, exist_ok=True)
    for (regime, source_stem), preds in sorted(by_file.items()):
        regime_dir = output_dir / regime
        regime_dir.mkdir(parents=True, exist_ok=True)
        lp_path = regime_dir / f"{source_stem}.lp"
        lp_path.write_text(
            "\n\n".join(p.rule for p in preds),
            encoding="utf-8",
        )
        logger.info("Escrito: %s (%d predicados)", lp_path, len(preds))

    conc_map: dict[str, list[str]] = json.loads(
        concurrency_map_path.read_text(encoding="utf-8")
    )
    seen: set[frozenset[str]] = set()
    facts: list[str] = []
    for chunk_a, neighbors in conc_map.items():
        for chunk_b in neighbors:
            pair: frozenset[str] = frozenset({chunk_a, chunk_b})
            if pair not in seen:
                seen.add(pair)
                facts.append(f"concurrent({chunk_a}, {chunk_b}).")

    conc_lp = output_dir / "concurrent_facts.lp"
    header = "% concurrent_facts.lp — gerado do concurrency_map.json\n"
    conc_lp.write_text(header + "\n".join(facts), encoding="utf-8")
    result.concurrent_facts = len(facts)

    logger.info(
        "E3 batch: %d atoms → %d predicados | valid=%d invalid=%d | conc=%d",
        result.total_atoms, result.total_predicates,
        result.syntax_valid, result.syntax_invalid, result.concurrent_facts,
    )
    return result
