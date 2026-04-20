"""Tests for E4 HITL sampler module."""
from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from qfeng.c1_digestion.hitl.sampler import (
    HitlItem,
    load_predicates_from_lp,
    sample_stratified,
    score_alhedonic,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def lp_blocks() -> str:
    return textwrap.dedent("""\
        % atom_id: abc001 | chunk: chunk001 | strength: constitutional
        obligated(state, citizen, provide_healthcare).

        % atom_id: abc002 | chunk: chunk002 | strength: statutory
        prohibited(employer, employee, discriminate_by_race).

        % atom_id: abc003 | chunk: chunk003 | strength: operational
        permitted(authority, public, access_data).

        % atom_id: abc004 | chunk: chunk001 | strength: constitutional
        obligated(state, worker, guarantee_minimum_wage).
    """)


@pytest.fixture
def lp_file(tmp_path: Path, lp_blocks: str) -> Path:
    f = tmp_path / "test_doc.lp"
    f.write_text(lp_blocks, encoding="utf-8")
    return f


@pytest.fixture
def concurrent_lp(tmp_path: Path) -> Path:
    f = tmp_path / "concurrent_facts.lp"
    f.write_text("% concurrent_facts.lp — gerado do concurrency_map.json\nconcurrent(chunk001, chunk002).\n")
    return f


# ---------------------------------------------------------------------------
# load_predicates_from_lp
# ---------------------------------------------------------------------------

class TestLoadPredicatesFromLp:
    def test_skips_concurrent_facts(self, concurrent_lp: Path) -> None:
        items = load_predicates_from_lp(concurrent_lp, corpus="test", concurrent_map={})
        assert items == []

    def test_parses_obligated_modality(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        obligated = [it for it in items if it.modality == "obligated"]
        assert len(obligated) == 2

    def test_parses_prohibited_modality(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        prohibited = [it for it in items if it.modality == "prohibited"]
        assert len(prohibited) == 1

    def test_parses_permitted_modality(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        permitted = [it for it in items if it.modality == "permitted"]
        assert len(permitted) == 1

    def test_extracts_atom_id(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        ids = {it.atom_id for it in items}
        assert "abc001" in ids
        assert "abc002" in ids

    def test_extracts_chunk_id(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        chunk_ids = {it.chunk_id for it in items}
        assert "chunk001" in chunk_ids

    def test_extracts_strength(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        item = next(it for it in items if it.atom_id == "abc001")
        assert item.strength == "constitutional"

    def test_rule_contains_comment(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        item = next(it for it in items if it.atom_id == "abc001")
        assert "% atom_id:" in item.rule

    def test_source_doc_is_stem(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        assert all(it.source_doc == "test_doc" for it in items)

    def test_corpus_field_set(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="mytest", concurrent_map={})
        assert all(it.corpus == "mytest" for it in items)

    def test_concurrent_chunks_populated(self, lp_file: Path) -> None:
        concurrent_map = {"chunk001": ["chunk999", "chunk888"]}
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map=concurrent_map)
        item = next(it for it in items if it.chunk_id == "chunk001")
        assert "chunk999" in item.concurrent_chunks

    def test_no_concurrent_chunks_when_map_empty(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        assert all(it.concurrent_chunks == [] for it in items)

    def test_unknown_modality_fallback(self, tmp_path: Path) -> None:
        f = tmp_path / "weird.lp"
        f.write_text(
            "% atom_id: zz001 | chunk: cX | strength: statutory\n"
            "norm(state, public, do_something).\n",
            encoding="utf-8",
        )
        items = load_predicates_from_lp(f, corpus="test", concurrent_map={})
        assert items[0].modality == "unknown"

    def test_returns_correct_count(self, lp_file: Path) -> None:
        items = load_predicates_from_lp(lp_file, corpus="test", concurrent_map={})
        assert len(items) == 4


# ---------------------------------------------------------------------------
# score_alhedonic
# ---------------------------------------------------------------------------

class TestScoreAlhedonic:
    def _make_item(
        self,
        atom_id: str = "a1",
        chunk_id: str = "c1",
        strength: str = "statutory",
        modality: str = "obligated",
        concurrent_chunks: list[str] | None = None,
    ) -> HitlItem:
        return HitlItem(
            atom_id=atom_id,
            chunk_id=chunk_id,
            strength=strength,
            rule="obligated(x, y, z).",
            modality=modality,
            corpus="test",
            source_doc="doc",
            concurrent_chunks=concurrent_chunks or [],
        )

    def test_zero_score_no_peers_no_operational(self) -> None:
        item = self._make_item()
        assert score_alhedonic(item, {}) == pytest.approx(0.0)

    def test_low_confidence_adds_0_1(self) -> None:
        item = self._make_item(strength="operational")
        assert score_alhedonic(item, {}) == pytest.approx(0.1)

    def test_concurrent_penalty_0_4(self) -> None:
        item = self._make_item(chunk_id="c1", concurrent_chunks=["c2"])
        peer = self._make_item(atom_id="a2", chunk_id="c2", modality="obligated", strength="statutory")
        assert score_alhedonic(item, {"c2": [peer]}) == pytest.approx(0.4)

    def test_modality_conflict_adds_0_3(self) -> None:
        item = self._make_item(chunk_id="c1", modality="obligated", concurrent_chunks=["c2"])
        peer = self._make_item(atom_id="a2", chunk_id="c2", modality="prohibited", strength="statutory")
        score = score_alhedonic(item, {"c2": [peer]})
        assert score == pytest.approx(0.7)  # 0.4 + 0.3

    def test_strength_mismatch_adds_0_2(self) -> None:
        item = self._make_item(chunk_id="c1", strength="constitutional", modality="obligated", concurrent_chunks=["c2"])
        peer = self._make_item(atom_id="a2", chunk_id="c2", strength="operational", modality="obligated")
        score = score_alhedonic(item, {"c2": [peer]})
        assert score == pytest.approx(0.6)  # 0.4 + 0.2

    def test_max_score_capped_at_1_0(self) -> None:
        item = self._make_item(
            chunk_id="c1", strength="operational", modality="obligated", concurrent_chunks=["c2"]
        )
        peer = self._make_item(
            atom_id="a2", chunk_id="c2", strength="constitutional", modality="prohibited"
        )
        score = score_alhedonic(item, {"c2": [peer]})
        assert score == pytest.approx(1.0)

    def test_full_components_without_cap(self) -> None:
        # 0.4 + 0.3 + 0.2 + 0.1 = 1.0 — should not exceed 1.0
        item = self._make_item(
            chunk_id="c1", strength="operational", modality="obligated", concurrent_chunks=["c2"]
        )
        peer = self._make_item(
            atom_id="a2", chunk_id="c2", strength="constitutional", modality="prohibited"
        )
        score = score_alhedonic(item, {"c2": [peer]})
        assert 0.0 <= score <= 1.0


# ---------------------------------------------------------------------------
# sample_stratified
# ---------------------------------------------------------------------------

class TestSampleStratified:
    def _make_items(self, n: int, source_doc: str = "doc1", modality: str = "obligated") -> list[HitlItem]:
        return [
            HitlItem(
                atom_id=f"a{i}",
                chunk_id=f"c{i}",
                strength="statutory",
                rule=f"obligated(x, y, z{i}).",
                modality=modality,
                corpus="test",
                source_doc=source_doc,
                alhedonic_score=float(i) / n,
            )
            for i in range(n)
        ]

    def test_respects_target(self) -> None:
        items = self._make_items(100)
        sampled = sample_stratified(items, target=10)
        assert len(sampled) <= 10

    def test_returns_all_when_fewer_than_target(self) -> None:
        items = self._make_items(3)
        sampled = sample_stratified(items, target=100)
        assert len(sampled) == 3

    def test_empty_input(self) -> None:
        assert sample_stratified([], target=10) == []

    def test_min_per_modality_coverage(self) -> None:
        items_obl = self._make_items(10, modality="obligated")
        items_proh = self._make_items(10, modality="prohibited")
        all_items = items_obl + items_proh
        sampled = sample_stratified(all_items, target=50, min_per_modality=2)
        modalities = {it.modality for it in sampled}
        assert "obligated" in modalities
        assert "prohibited" in modalities

    def test_sorted_by_alhedonic_desc(self) -> None:
        items = self._make_items(20)
        sampled = sample_stratified(items, target=5)
        scores = [it.alhedonic_score for it in sampled]
        assert scores == sorted(scores, reverse=True)

    def test_multi_doc_coverage(self) -> None:
        items = self._make_items(20, source_doc="doc1") + self._make_items(20, source_doc="doc2")
        sampled = sample_stratified(items, target=20)
        docs = {it.source_doc for it in sampled}
        assert "doc1" in docs
        assert "doc2" in docs

    def test_no_duplicate_atom_ids(self) -> None:
        items = self._make_items(50)
        sampled = sample_stratified(items, target=20)
        ids = [it.atom_id for it in sampled]
        assert len(ids) == len(set(ids))
