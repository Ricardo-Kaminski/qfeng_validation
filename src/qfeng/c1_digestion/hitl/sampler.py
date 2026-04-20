"""E4 HITL — Sampler: load E3 predicates, score alhedonic conflict, stratified sample."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------

@dataclass
class HitlItem:
    atom_id: str
    chunk_id: str
    strength: str
    rule: str                           # full block including comment line
    modality: str                       # "obligated" | "prohibited" | "permitted" | "unknown"
    corpus: str
    source_doc: str                     # stem of the .lp file
    alhedonic_score: float = 0.0
    concurrent_chunks: list[str] = field(default_factory=list)
    # Enriched from E1 NormChunk — populated after sampling
    chunk_text: str = ""
    chunk_hierarchy: list[str] = field(default_factory=list)
    chunk_source_label: str = ""


# ---------------------------------------------------------------------------
# Concurrency map loader
# ---------------------------------------------------------------------------

def _load_concurrent_map(e3_dir: Path) -> dict[str, list[str]]:
    """Load concurrency_map.json from e1_chunks output (located relative to project root)."""
    # Try sibling of e3_dir's parent, then hardcoded fallback
    candidates = [
        e3_dir.parent.parent / "outputs" / "e1_chunks" / "concurrency_map.json",
        Path("outputs/e1_chunks/concurrency_map.json"),
        Path(__file__).parents[4] / "outputs" / "e1_chunks" / "concurrency_map.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


# ---------------------------------------------------------------------------
# LP file parser
# ---------------------------------------------------------------------------

_COMMENT_RE = re.compile(
    r"%\s*atom_id:\s*(\S+)\s*\|\s*chunk:\s*(\S+)\s*\|\s*strength:\s*(\S+)"
)
_MODALITY_RE = re.compile(r"^(obligated|prohibited|permitted|may)\s*\(", re.MULTILINE)


def load_predicates_from_lp(
    lp_file: Path,
    corpus: str,
    concurrent_map: dict[str, list[str]],
) -> list[HitlItem]:
    """Parse a single .lp file into a list of HitlItems.

    Each block is separated by blank lines. Blocks that have no atom_id comment
    (e.g. concurrent_facts.lp) are silently skipped.
    """
    if lp_file.name == "concurrent_facts.lp":
        return []

    text = lp_file.read_text(encoding="utf-8")
    blocks = [b.strip() for b in text.split("\n\n") if b.strip()]

    items: list[HitlItem] = []
    for block in blocks:
        m = _COMMENT_RE.search(block)
        if not m:
            continue
        atom_id, chunk_id, strength = m.group(1), m.group(2), m.group(3)

        mod_m = _MODALITY_RE.search(block)
        modality = mod_m.group(1) if mod_m else "unknown"

        concurrent_chunks = concurrent_map.get(chunk_id, [])

        items.append(
            HitlItem(
                atom_id=atom_id,
                chunk_id=chunk_id,
                strength=strength,
                rule=block,
                modality=modality,
                corpus=corpus,
                source_doc=lp_file.stem,
                concurrent_chunks=list(concurrent_chunks),
            )
        )
    return items


# ---------------------------------------------------------------------------
# Chunk text enrichment (E1 → NormChunk lookup)
# ---------------------------------------------------------------------------

def _strip_diacritics(text: str) -> str:
    """Remove diacritics and lowercase for fuzzy keyword matching."""
    import unicodedata
    nfd = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in nfd if unicodedata.category(c) != "Mn")


def _keyword_score(rule: str, chunk_text: str) -> int:
    """Count rule tokens (>=3 chars) found in chunk_text after diacritic normalisation."""
    rule_norm = _strip_diacritics(rule)
    text_norm = _strip_diacritics(chunk_text)
    tokens = re.findall(r"[a-z]{3,}", rule_norm)
    return sum(1 for t in tokens if t in text_norm)


def build_chunk_lookup(e1_dir: Path) -> dict[str, list[dict]]:
    """Read all E1 JSON files and return chunk_id||source_stem -> list[chunk_entry].

    Also indexes by source::source_stem -> list[all chunk entries] for fallback
    keyword-based lookup when chunk_ids have been regenerated (e.g. after FIX 1).
    """
    lookup: dict[str, list[dict]] = {}
    if not e1_dir.exists():
        return lookup
    for json_file in e1_dir.rglob("*.json"):
        if json_file.name.endswith("concurrency_map.json"):
            continue
        source_stem = json_file.stem
        try:
            chunks = json.loads(json_file.read_text(encoding="utf-8", errors="replace"))
            for chunk in chunks:
                cid = chunk.get("id", "")
                if not cid:
                    continue
                entry = {
                    "text": chunk.get("text", ""),
                    "hierarchy": chunk.get("hierarchy", []),
                    "source": chunk.get("source", ""),
                }
                lookup.setdefault(cid + "||" + source_stem, []).append(entry)
                lookup.setdefault("source::" + source_stem, []).append(entry)
        except Exception:
            continue
    return lookup


def enrich_with_chunk_texts(items: list[HitlItem], lookup: dict[str, list[dict]]) -> None:
    """Enrich each HitlItem with chunk_text, chunk_hierarchy, chunk_source_label.

    Lookup order:
    1. chunk_id||source_stem (exact, fast)
    2. chunk_id across any source (partial fallback)
    3. keyword scoring across all chunks for source_doc (handles stale chunk_ids
       after E1 regeneration with FIX 1 — old IDs no longer exist in new E1)
    """
    for item in items:
        key = item.chunk_id + "||" + item.source_doc
        candidates = lookup.get(key, [])

        if not candidates:
            prefix = item.chunk_id + "||"
            candidates = [entry for k, v in lookup.items() if k.startswith(prefix) for entry in v]

        if not candidates:
            # Fallback: keyword match across all chunks from the same source document
            source_candidates = lookup.get("source::" + item.source_doc, [])
            if source_candidates and item.rule:
                scored = [(c, _keyword_score(item.rule, c["text"])) for c in source_candidates]
                scored.sort(key=lambda x: x[1], reverse=True)
                best_score = scored[0][1]
                if best_score > 0:
                    candidates = [scored[0][0]]

        if not candidates:
            item.chunk_text = f"[texto do chunk nao disponivel — chunk_id: {item.chunk_id}]"
            continue

        if len(candidates) == 1:
            best = candidates[0]
        else:
            scored = [(c, _keyword_score(item.rule, c["text"])) for c in candidates]
            scored.sort(key=lambda x: x[1], reverse=True)
            best = scored[0][0]

        item.chunk_text = best["text"]
        item.chunk_hierarchy = best["hierarchy"]
        item.chunk_source_label = best["source"]


# ---------------------------------------------------------------------------
# Alhedonic score
# ---------------------------------------------------------------------------

def score_alhedonic(item: HitlItem, all_items_by_chunk: dict[str, list[HitlItem]]) -> float:
    """Compute conflict signal [0.0, 1.0] for a single HitlItem.

    Components:
      concurrent_penalty +0.4  — chunk has concurrent peers
      modality_conflict   +0.3  — peer has a different modality
      strength_mismatch   +0.2  — peer has a different strength
      low_confidence      +0.1  — strength == "operational"
    """
    score = 0.0

    peers: list[HitlItem] = []
    for cid in item.concurrent_chunks:
        peers.extend(all_items_by_chunk.get(cid, []))

    if peers:
        score += 0.4

        peer_modalities = {p.modality for p in peers}
        if peer_modalities - {item.modality}:
            score += 0.3

        peer_strengths = {p.strength for p in peers}
        if peer_strengths - {item.strength}:
            score += 0.2

    if item.strength == "operational":
        score += 0.1

    return min(score, 1.0)


# ---------------------------------------------------------------------------
# Stratified sampler
# ---------------------------------------------------------------------------

def sample_stratified(
    items: list[HitlItem],
    target: int,
    min_per_modality: int = 1,
) -> list[HitlItem]:
    """Return at most `target` items via stratified sampling per source_doc.

    Strategy:
      - Group by source_doc
      - Per doc: sort by alhedonic_score desc, guarantee min_per_modality coverage
      - base_per_doc = max(5, target // n_docs)
      - Final sort by alhedonic_score desc, trim to target
    """
    from collections import defaultdict

    by_doc: dict[str, list[HitlItem]] = defaultdict(list)
    for item in items:
        by_doc[item.source_doc].append(item)

    n_docs = len(by_doc)
    if n_docs == 0:
        return []

    base_per_doc = max(5, target // n_docs)
    selected: list[HitlItem] = []

    for doc_items in by_doc.values():
        # Sort descending by alhedonic score
        doc_items_sorted = sorted(doc_items, key=lambda x: x.alhedonic_score, reverse=True)

        # Guarantee min_per_modality coverage
        by_modality: dict[str, list[HitlItem]] = defaultdict(list)
        for it in doc_items_sorted:
            by_modality[it.modality].append(it)

        mandatory: list[HitlItem] = []
        for mod_items in by_modality.values():
            mandatory.extend(mod_items[:min_per_modality])

        mandatory_ids = {it.atom_id for it in mandatory}
        remaining = [it for it in doc_items_sorted if it.atom_id not in mandatory_ids]

        doc_sample = list(mandatory)
        needed = max(0, base_per_doc - len(doc_sample))
        doc_sample.extend(remaining[:needed])

        selected.extend(doc_sample)

    # Final sort by alhedonic_score desc, trim to target
    selected.sort(key=lambda x: x.alhedonic_score, reverse=True)
    return selected[:target]
