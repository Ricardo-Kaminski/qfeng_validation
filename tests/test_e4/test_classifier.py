"""Tests for E4 HITL classifier module."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from qfeng.c1_digestion.hitl.classifier import DecisionCache, HITLDecision


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def cache_path(tmp_path: Path) -> Path:
    return tmp_path / "decisions.json"


@pytest.fixture
def cache(cache_path: Path) -> DecisionCache:
    return DecisionCache(cache_path)


@pytest.fixture
def decision() -> HITLDecision:
    return HITLDecision(
        predicate_id="abc001",
        classification="SOVEREIGN",
        alhedonic_signal=0.7,
        reviewer_note="constitutional norm",
        session_ts="2026-04-19T00:00:00+00:00",
    )


# ---------------------------------------------------------------------------
# HITLDecision dataclass
# ---------------------------------------------------------------------------

class TestHITLDecision:
    def test_fields(self, decision: HITLDecision) -> None:
        assert decision.predicate_id == "abc001"
        assert decision.classification == "SOVEREIGN"
        assert decision.alhedonic_signal == pytest.approx(0.7)

    def test_defaults(self) -> None:
        d = HITLDecision(predicate_id="x", classification="ELASTIC", alhedonic_signal=0.0)
        assert d.reviewer_note == ""
        assert d.session_ts == ""


# ---------------------------------------------------------------------------
# DecisionCache
# ---------------------------------------------------------------------------

class TestDecisionCache:
    def test_empty_on_new_path(self, cache: DecisionCache) -> None:
        assert cache.completed_ids() == set()

    def test_save_creates_file(self, cache: DecisionCache, cache_path: Path, decision: HITLDecision) -> None:
        cache.save(decision)
        assert cache_path.exists()

    def test_save_and_get(self, cache: DecisionCache, decision: HITLDecision) -> None:
        cache.save(decision)
        result = cache.get("abc001")
        assert result is not None
        assert result["classification"] == "SOVEREIGN"

    def test_get_returns_none_for_missing(self, cache: DecisionCache) -> None:
        assert cache.get("nonexistent") is None

    def test_completed_ids_updated(self, cache: DecisionCache, decision: HITLDecision) -> None:
        cache.save(decision)
        assert "abc001" in cache.completed_ids()

    def test_multiple_saves(self, cache: DecisionCache) -> None:
        cache.save(HITLDecision("a1", "SOVEREIGN", 0.8))
        cache.save(HITLDecision("a2", "ELASTIC", 0.2))
        cache.save(HITLDecision("a3", "SKIP", 0.0))
        assert len(cache.completed_ids()) == 3

    def test_stats_counts_correctly(self, cache: DecisionCache) -> None:
        cache.save(HITLDecision("a1", "SOVEREIGN", 0.8))
        cache.save(HITLDecision("a2", "SOVEREIGN", 0.7))
        cache.save(HITLDecision("a3", "ELASTIC", 0.2))
        cache.save(HITLDecision("a4", "SKIP", 0.0))
        stats = cache.stats()
        assert stats["sovereign"] == 2
        assert stats["elastic"] == 1
        assert stats["skipped"] == 1
        assert stats["total"] == 4

    def test_persists_to_disk(self, cache_path: Path, decision: HITLDecision) -> None:
        cache1 = DecisionCache(cache_path)
        cache1.save(decision)
        # Load fresh from disk
        cache2 = DecisionCache(cache_path)
        assert "abc001" in cache2.completed_ids()

    def test_json_is_valid_utf8(self, cache: DecisionCache, cache_path: Path) -> None:
        cache.save(HITLDecision("x1", "SOVEREIGN", 0.5, reviewer_note="Proteção constitucional"))
        data = json.loads(cache_path.read_text(encoding="utf-8"))
        assert data["x1"]["reviewer_note"] == "Proteção constitucional"

    def test_overwrite_existing_decision(self, cache: DecisionCache) -> None:
        cache.save(HITLDecision("a1", "SOVEREIGN", 0.8))
        cache.save(HITLDecision("a1", "ELASTIC", 0.3))
        result = cache.get("a1")
        assert result is not None
        assert result["classification"] == "ELASTIC"

    def test_stats_empty_cache(self, cache: DecisionCache) -> None:
        stats = cache.stats()
        assert stats["total"] == 0
        assert stats["sovereign"] == 0
        assert stats["elastic"] == 0
