"""E4 HITL — Exporter: generate .lp files separated by SOVEREIGN/ELASTIC class."""
from __future__ import annotations

import json
from pathlib import Path


def export_classified_lp(
    sample_path: Path,
    cache_path: Path,
    output_dir: Path,
) -> dict[str, int]:
    """Export classified predicates into sovereign/ and elastic/ subdirectories.

    Args:
        sample_path: path to the sample JSON file (from --action sample)
        cache_path:  path to the decisions JSON cache (from classifier)
        output_dir:  root output directory (e.g. outputs/)

    Returns:
        dict with counts: {"sovereign": N, "elastic": N}
    """
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    cache: dict[str, dict] = {}
    if cache_path.exists():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))

    by_class: dict[str, dict[str, dict[str, list[str]]]] = {
        "sovereign": {},
        "elastic": {},
    }

    for pred in sample:
        dec = cache.get(pred["id"])
        if not dec:
            continue
        classification = dec["classification"].lower()
        if classification not in by_class:
            continue  # "skip" entries are not exported

        regime = pred.get("corpus", "brasil")
        doc = pred.get("source_doc", "unknown")
        by_class[classification].setdefault(regime, {}).setdefault(doc, []).append(pred["rule"])

    stats: dict[str, int] = {"sovereign": 0, "elastic": 0}

    for cls, regimes in by_class.items():
        for regime, docs in regimes.items():
            regime_dir = output_dir / f"e4_{cls}" / regime
            regime_dir.mkdir(parents=True, exist_ok=True)
            for doc, rules in docs.items():
                out_file = regime_dir / f"{doc}.lp"
                out_file.write_text("\n\n".join(rules), encoding="utf-8")
                stats[cls] += len(rules)

    return stats
