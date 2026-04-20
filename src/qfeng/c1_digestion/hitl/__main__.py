"""E4 HITL — CLI entry point.

Usage:
    conda run -n qfeng python -m qfeng.c1_digestion.hitl --action sample --corpus sus_validacao
    conda run -n qfeng python -m qfeng.c1_digestion.hitl --action review --corpus sus_validacao
    conda run -n qfeng python -m qfeng.c1_digestion.hitl --action export --corpus sus_validacao
    conda run -n qfeng python -m qfeng.c1_digestion.hitl --action report --corpus sus_validacao
"""
from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

# Force UTF-8 output to survive conda run on Windows cp1252 terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from rich.console import Console
from rich.table import Table

console = Console(highlight=False)

from qfeng.c1_digestion.hitl.exporter import export_classified_lp
from qfeng.c1_digestion.hitl.sampler import (
    HitlItem,
    _load_concurrent_map,
    build_chunk_lookup,
    enrich_with_chunk_texts,
    load_predicates_from_lp,
    sample_stratified,
    score_alhedonic,
)

# ---------------------------------------------------------------------------
# Project root (3 parents up from this file)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parents[4]

CORPUS_CONFIG: dict[str, dict] = {
    "sus_validacao": {
        "e3_dir": PROJECT_ROOT / "outputs" / "e3_predicates",
        "e1_dir": PROJECT_ROOT / "outputs" / "e1_chunks_scoped",
        "session_dir": PROJECT_ROOT / "outputs" / "hitl_session" / "sus_validacao",
        "samples_dir": PROJECT_ROOT / "data" / "hitl" / "samples",
        "cache_dir": PROJECT_ROOT / "data" / "hitl" / "hitl_cache",
        "target": 990,
    },
    "advocacia_trabalhista": {
        "e3_dir": PROJECT_ROOT / "outputs" / "e3_predicates_trabalhista",
        "e1_dir": PROJECT_ROOT / "outputs" / "e1_chunks_trabalhista",
        "session_dir": PROJECT_ROOT / "outputs" / "hitl_session" / "advocacia_trabalhista",
        "samples_dir": PROJECT_ROOT / "data" / "hitl" / "samples",
        "cache_dir": PROJECT_ROOT / "data" / "hitl" / "hitl_cache",
        "target": 160,
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _item_to_dict(item: HitlItem) -> dict:
    d = asdict(item)
    d["id"] = d.pop("atom_id")  # use "id" as key for compatibility with app.py
    return d


def _load_all_predicates(corpus: str) -> list[HitlItem]:
    cfg = CORPUS_CONFIG[corpus]
    e3_dir: Path = cfg["e3_dir"]
    concurrent_map = _load_concurrent_map(e3_dir)

    all_items: list[HitlItem] = []
    lp_files = sorted(e3_dir.rglob("*.lp"))
    console.print(f"[bold]Corpus:[/bold] {corpus} — {len(lp_files)} .lp files found in {e3_dir}")

    for lp_file in lp_files:
        items = load_predicates_from_lp(lp_file, corpus=corpus, concurrent_map=concurrent_map)
        all_items.extend(items)

    console.print(f"Loaded [green]{len(all_items)}[/green] predicates total")

    # Enrich with original NormChunk text and hierarchy from E1
    e1_dir: Path = cfg.get("e1_dir", Path("nonexistent"))
    chunk_lookup = build_chunk_lookup(e1_dir)
    enrich_with_chunk_texts(all_items, chunk_lookup)
    enriched = sum(1 for it in all_items if it.chunk_text)
    console.print(f"  Chunks enriched with E1 text: [cyan]{enriched}[/cyan] / {len(all_items)}")

    return all_items


def _score_all(items: list[HitlItem]) -> None:
    """Score alhedonic in-place on all items."""
    from collections import defaultdict

    by_chunk: dict[str, list[HitlItem]] = defaultdict(list)
    for item in items:
        by_chunk[item.chunk_id].append(item)

    for item in items:
        item.alhedonic_score = score_alhedonic(item, by_chunk)


# ---------------------------------------------------------------------------
# Actions
# ---------------------------------------------------------------------------

def action_sample(corpus: str) -> None:
    cfg = CORPUS_CONFIG[corpus]
    target: int = cfg["target"]
    samples_dir: Path = cfg["samples_dir"]
    samples_dir.mkdir(parents=True, exist_ok=True)
    sample_path = samples_dir / f"{corpus}_sample.json"

    all_items = _load_all_predicates(corpus)
    _score_all(all_items)

    sampled = sample_stratified(all_items, target=target, min_per_modality=1)

    # Serialize
    records = [_item_to_dict(it) for it in sampled]
    sample_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    # Report
    modality_counts = Counter(it.modality for it in sampled)
    source_doc_counts = Counter(it.source_doc for it in sampled)
    high_signal = sum(1 for it in sampled if it.alhedonic_score > 0.5)

    console.print(f"\n[bold green]Sample saved:[/bold green] {sample_path}")
    console.print(f"  Total sampled:        [cyan]{len(sampled)}[/cyan]")
    console.print(f"  High alhedonic (>0.5): [yellow]{high_signal}[/yellow]")

    table = Table(title="Modality distribution", show_header=True)
    table.add_column("Modality", style="cyan")
    table.add_column("Count", justify="right")
    for mod, cnt in sorted(modality_counts.items()):
        table.add_row(mod, str(cnt))
    console.print(table)

    table2 = Table(title="Predicates per source_doc", show_header=True)
    table2.add_column("Source doc", style="cyan")
    table2.add_column("Count", justify="right")
    for doc, cnt in sorted(source_doc_counts.items(), key=lambda x: -x[1]):
        table2.add_row(doc, str(cnt))
    console.print(table2)


def action_review(corpus: str) -> None:
    app_path = Path(__file__).parent / "app.py"
    console.print(f"Launching Streamlit for corpus=[cyan]{corpus}[/cyan]")
    subprocess.run(
        [
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--", f"--corpus={corpus}",
        ],
        check=False,
    )


def action_export(corpus: str) -> None:
    cfg = CORPUS_CONFIG[corpus]
    samples_dir: Path = cfg["samples_dir"]
    cache_dir: Path = cfg["cache_dir"]

    sample_path = samples_dir / f"{corpus}_sample.json"
    cache_path = cache_dir / f"{corpus}_decisions.json"

    if not sample_path.exists():
        console.print(f"[red]Sample not found:[/red] {sample_path}")
        console.print("Run --action sample first.")
        sys.exit(1)

    stats = export_classified_lp(sample_path, cache_path, PROJECT_ROOT / "outputs")
    console.print(f"[bold green]Export complete:[/bold green] {stats}")


def action_report(corpus: str) -> None:
    cfg = CORPUS_CONFIG[corpus]
    samples_dir: Path = cfg["samples_dir"]
    cache_dir: Path = cfg["cache_dir"]

    sample_path = samples_dir / f"{corpus}_sample.json"
    cache_path = cache_dir / f"{corpus}_decisions.json"

    if not sample_path.exists():
        console.print(f"[red]Sample not found.[/red] Run --action sample first.")
        sys.exit(1)

    sample: list[dict] = json.loads(sample_path.read_text(encoding="utf-8"))
    cache: dict[str, dict] = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    total = len(sample)
    reviewed = len(cache)
    sovereign = sum(1 for v in cache.values() if v["classification"] == "SOVEREIGN")
    elastic = sum(1 for v in cache.values() if v["classification"] == "ELASTIC")
    skipped = sum(1 for v in cache.values() if v["classification"] == "SKIP")

    # Breakdown by doc
    by_doc: dict[str, Counter] = {}
    for pred in sample:
        dec = cache.get(pred["id"])
        if dec:
            doc = pred.get("source_doc", "unknown")
            if doc not in by_doc:
                by_doc[doc] = Counter()
            by_doc[doc][dec["classification"]] += 1

    console.print(f"\n[bold]E4 HITL Report — {corpus}[/bold]")
    console.print(f"  Total sample:  {total}")
    console.print(f"  Reviewed:      {reviewed}")
    console.print(f"  Remaining:     {total - reviewed}")
    console.print(f"  SOVEREIGN:     {sovereign}")
    console.print(f"  ELASTIC:       {elastic}")
    console.print(f"  SKIP:          {skipped}")

    if reviewed > 0:
        sov_pct = 100 * sovereign / reviewed
        console.print(f"  SOVEREIGN %:   {sov_pct:.1f}%")

    table = Table(title="Breakdown by document", show_header=True)
    table.add_column("Document", style="cyan")
    table.add_column("SOVEREIGN", justify="right", style="green")
    table.add_column("ELASTIC", justify="right", style="blue")
    table.add_column("SKIP", justify="right", style="yellow")
    for doc, cnts in sorted(by_doc.items()):
        table.add_row(doc, str(cnts["SOVEREIGN"]), str(cnts["ELASTIC"]), str(cnts["SKIP"]))
    console.print(table)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Q-FENG E4 HITL")
    parser.add_argument(
        "--action",
        choices=["sample", "review", "export", "report"],
        required=True,
    )
    parser.add_argument(
        "--corpus",
        choices=list(CORPUS_CONFIG.keys()),
        required=True,
    )
    args = parser.parse_args()

    dispatch = {
        "sample": action_sample,
        "review": action_review,
        "export": action_export,
        "report": action_report,
    }
    dispatch[args.action](args.corpus)


if __name__ == "__main__":
    main()
