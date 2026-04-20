"""Patch sampler.py: replace build_chunk_lookup + enrich_with_chunk_texts with
collision-safe, keyword-matching versions."""
import pathlib

TARGET = pathlib.Path(__file__).parents[1] / "src" / "qfeng" / "c1_digestion" / "hitl" / "sampler.py"
src = TARGET.read_text(encoding="utf-8")

# ── locate and cut the two functions ──────────────────────────────────────

START_MARKER = "def build_chunk_lookup(e1_dir: Path)"
END_MARKER = "# ---------------------------------------------------------------------------\n# Alhedonic score"

start = src.index(START_MARKER)
end = src.index(END_MARKER)

# ── replacement block ─────────────────────────────────────────────────────

NEW_BLOCK = '''\
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

    Large consolidated documents (e.g. portaria_consolidacao_5_2017) contain
    many sections from different annexed portarias that share the same hierarchy
    label (e.g. 'Art. 5') and therefore the same chunk_id.  Storing a *list*
    instead of a single entry avoids the last-write-wins collision bug.
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
                key = cid + "||" + source_stem
                entry = {
                    "text": chunk.get("text", ""),
                    "hierarchy": chunk.get("hierarchy", []),
                    "source": chunk.get("source", ""),
                }
                lookup.setdefault(key, []).append(entry)
        except Exception:
            continue
    return lookup


def enrich_with_chunk_texts(items: list[HitlItem], lookup: dict[str, list[dict]]) -> None:
    """Enrich each HitlItem with chunk_text, chunk_hierarchy, chunk_source_label.

    When multiple E1 chunks share the same chunk_id (ID collision in consolidated
    documents), picks the candidate whose text best matches the predicate rule via
    keyword scoring.  Falls back to the first candidate when scoring is tied.
    """
    for item in items:
        key = item.chunk_id + "||" + item.source_doc
        candidates = lookup.get(key, [])

        if not candidates:
            # fallback: try chunk_id across any source_doc
            prefix = item.chunk_id + "||"
            candidates = [entry for k, v in lookup.items() if k.startswith(prefix) for entry in v]

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


'''

patched = src[:start] + NEW_BLOCK + src[end:]
TARGET.write_text(patched, encoding="utf-8")
print(f"Patched: {TARGET}")

# verify syntax
import py_compile
py_compile.compile(str(TARGET), doraise=True)
print("Syntax OK")
