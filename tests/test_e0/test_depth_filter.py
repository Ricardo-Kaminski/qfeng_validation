"""Testes para _filter_chunks_by_scope() no runner E1."""

from qfeng.c1_digestion.ingestion.runner import _filter_chunks_by_scope
from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.core.schemas import NormativeRegime, NormChunk


def _make_scope(**overrides) -> ScopeConfig:
    defaults = {
        "name": "test",
        "description": "test",
        "regimes": ["brasil"],
        "documents": {"brasil": ["*"]},
        "chunk_types": ["obligation", "principle"],
        "hierarchy_depth": 3,
        "follow_cross_references": False,
        "min_chunk_chars": 40,
        "strength_filter": None,
    }
    defaults.update(overrides)
    return ScopeConfig(**defaults)


def _make_chunk(**overrides) -> NormChunk:
    defaults = {
        "id": "abc123",
        "source": "lei_8080",
        "regime": NormativeRegime.BRASIL,
        "hierarchy": ["Art. 1", "§ 2"],
        "text": "x" * 50,
        "chunk_type": "obligation",
    }
    defaults.update(overrides)
    return NormChunk(**defaults)


class TestFilterChunksByScope:
    def test_valid_chunk_passes_all_filters(self):
        scope = _make_scope()
        chunk = _make_chunk()
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_chunk_below_min_chars_discarded(self):
        scope = _make_scope(min_chunk_chars=40)
        chunk = _make_chunk(text="x" * 35)
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_chunk_at_exact_min_chars_passes(self):
        scope = _make_scope(min_chunk_chars=40)
        chunk = _make_chunk(text="x" * 40)
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_chunk_type_not_in_scope_discarded(self):
        scope = _make_scope(chunk_types=["obligation"])
        chunk = _make_chunk(chunk_type="procedure")
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_chunk_type_in_scope_passes(self):
        scope = _make_scope(chunk_types=["obligation", "principle"])
        chunk = _make_chunk(chunk_type="principle")
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_within_depth_passes(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2"])
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_at_exact_depth_passes(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2", "I"])
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_above_depth_discarded(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2", "I", "a)"])
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_empty_hierarchy_chunk_discarded(self):
        """Chunk sem hierarquia é sempre descartado (integridade estrutural)."""
        scope = _make_scope()
        chunk = _make_chunk(hierarchy=[])
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_multiple_chunks_filtered_correctly(self):
        scope = _make_scope(min_chunk_chars=40, chunk_types=["obligation"], hierarchy_depth=3)
        chunks = [
            _make_chunk(text="x" * 50, chunk_type="obligation", hierarchy=["Art. 1"]),
            _make_chunk(id="b", text="x" * 30, chunk_type="obligation", hierarchy=["Art. 1"]),
            _make_chunk(id="c", text="x" * 50, chunk_type="procedure", hierarchy=["Art. 1"]),
            _make_chunk(id="d", text="x" * 50, chunk_type="obligation",
                        hierarchy=["Art. 1", "§ 2", "I", "a)"]),
        ]
        result = _filter_chunks_by_scope(chunks, scope)
        assert len(result) == 1
        assert result[0].id == "abc123"
