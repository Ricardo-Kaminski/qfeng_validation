"""Testes para labels.py — human_label e conflict_label."""

from qfeng.c1_digestion.ingestion.labels import conflict_label, human_label
from qfeng.core.schemas import NormativeRegime, NormChunk


def _make_chunk(
    source: str = "CF/88",
    hierarchy: list[str] | None = None,
    text: str = "A saúde é direito de todos.",
) -> NormChunk:
    """Helper para criar chunks de teste."""
    return NormChunk(
        id="test_id",
        source=source,
        regime=NormativeRegime.BRASIL,
        hierarchy=hierarchy or ["Art. 196"],
        text=text,
        language="pt-BR",
    )


class TestHumanLabel:
    """Testes de human_label."""

    def test_basic_format(self) -> None:
        """Label deve conter source, hierarchy e preview."""
        chunk = _make_chunk()
        label = human_label(chunk)
        assert "CF/88" in label
        assert "Art. 196" in label
        assert "A saúde é direito de todos." in label

    def test_truncates_long_text(self) -> None:
        """Texto longo deve ser truncado com '...'."""
        chunk = _make_chunk(text="A" * 200)
        label = human_label(chunk, text_preview=50)
        assert label.endswith("...")
        assert len(label) < 200

    def test_short_text_no_ellipsis(self) -> None:
        """Texto curto não deve ter '...'."""
        chunk = _make_chunk(text="Curto.")
        label = human_label(chunk)
        assert not label.endswith("...")

    def test_multi_level_hierarchy(self) -> None:
        """Hierarquia multi-nível deve ser concatenada."""
        chunk = _make_chunk(hierarchy=["Art. 7", "§ 1", "I"])
        label = human_label(chunk)
        assert "Art. 7 § 1 I" in label

    def test_custom_preview_length(self) -> None:
        """text_preview deve controlar o tamanho."""
        chunk = _make_chunk(text="Abcdefghij" * 10)
        label_20 = human_label(chunk, text_preview=20)
        label_50 = human_label(chunk, text_preview=50)
        assert len(label_20) < len(label_50)


class TestConflictLabel:
    """Testes de conflict_label."""

    def test_basic_format(self) -> None:
        """Conflict label deve conter ambos os chunks e o score."""
        chunk_a = _make_chunk(source="CF/88")
        chunk_b = _make_chunk(source="Lei 8.080/1990")
        label = conflict_label(chunk_a, chunk_b, 0.857)
        assert "Jaccard 0.857" in label
        assert "[A]" in label
        assert "[B]" in label
        assert "CF/88" in label
        assert "Lei 8.080/1990" in label

    def test_multiline(self) -> None:
        """Conflict label deve ser multi-linha."""
        chunk_a = _make_chunk()
        chunk_b = _make_chunk()
        label = conflict_label(chunk_a, chunk_b, 0.5)
        assert label.count("\n") == 2
