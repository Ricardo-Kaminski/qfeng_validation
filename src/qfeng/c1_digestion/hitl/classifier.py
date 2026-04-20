"""E4 HITL — Classifier: decision cache for SOVEREIGN/ELASTIC classification."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class HITLDecision:
    predicate_id: str
    classification: str       # "SOVEREIGN" | "ELASTIC" | "SKIP"
    alhedonic_signal: float
    reviewer_note: str = ""
    session_ts: str = ""


class DecisionCache:
    """Persistent JSON cache for HITL decisions with resume support."""

    def __init__(self, cache_path: Path) -> None:
        self.path = cache_path
        self._data: dict[str, dict] = {}
        if cache_path.exists():
            self._data = json.loads(cache_path.read_text(encoding="utf-8"))

    def save(self, decision: HITLDecision) -> None:
        self._data[decision.predicate_id] = {
            "classification": decision.classification,
            "alhedonic_signal": decision.alhedonic_signal,
            "reviewer_note": decision.reviewer_note,
            "session_ts": decision.session_ts,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def get(self, predicate_id: str) -> dict | None:
        return self._data.get(predicate_id)

    def completed_ids(self) -> set[str]:
        return set(self._data.keys())

    def stats(self) -> dict:
        total = len(self._data)
        sovereign = sum(1 for v in self._data.values() if v["classification"] == "SOVEREIGN")
        elastic = sum(1 for v in self._data.values() if v["classification"] == "ELASTIC")
        skipped = sum(1 for v in self._data.values() if v["classification"] == "SKIP")
        return {
            "total": total,
            "sovereign": sovereign,
            "elastic": elastic,
            "skipped": skipped,
        }
    def remove(self, predicate_id: str) -> None:
        """Remove a decision from the cache (allows re-classification)."""
        if predicate_id in self._data:
            del self._data[predicate_id]
            self.path.write_text(
                json.dumps(self._data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

    def last_decisions(self, n: int = 10) -> list[tuple[str, dict]]:
        """Return last n decisions as (predicate_id, decision_dict) pairs."""
        items = list(self._data.items())
        return items[-n:][::-1]  # most recent first

