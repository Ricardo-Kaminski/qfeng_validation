"""Testes para o parser E1 — parse_document em cada regime."""

from pathlib import Path

import pytest

from qfeng.c1_digestion.ingestion.parser import parse_document
from qfeng.core.schemas import NormativeRegime, NormChunk


class TestParseBrasil:
    """Testes de parsing para documentos brasileiros."""

    def test_parse_lei_8080_returns_chunks(self, brasil_lei_8080: Path) -> None:
        """Lei 8.080/1990 deve produzir >10 NormChunks."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        assert len(chunks) > 10

    def test_parse_lei_8080_no_empty_text(self, brasil_lei_8080: Path) -> None:
        """Nenhum chunk deve ter texto vazio."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        for chunk in chunks:
            assert chunk.text.strip(), f"Chunk {chunk.id} tem texto vazio"

    def test_parse_lei_8080_no_empty_hierarchy(self, brasil_lei_8080: Path) -> None:
        """Nenhum chunk deve ter hierarquia vazia."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        for chunk in chunks:
            assert chunk.hierarchy, f"Chunk {chunk.id} tem hierarquia vazia"

    def test_parse_lei_8080_source(self, brasil_lei_8080: Path) -> None:
        """Source deve ser 'Lei 8.080/1990'."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        assert chunks[0].source == "Lei 8.080/1990"

    def test_parse_lei_8080_regime(self, brasil_lei_8080: Path) -> None:
        """Regime deve ser BRASIL."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        for chunk in chunks:
            assert chunk.regime == NormativeRegime.BRASIL

    def test_parse_lei_8080_language(self, brasil_lei_8080: Path) -> None:
        """Idioma deve ser pt-BR."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        assert chunks[0].language == "pt-BR"

    def test_parse_lei_8080_art1_present(self, brasil_lei_8080: Path) -> None:
        """Art. 1 deve estar presente nos chunks."""
        chunks = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        art1_chunks = [c for c in chunks if "Art. 1" in c.hierarchy]
        assert len(art1_chunks) > 0, "Art. 1 não encontrado"

    def test_parse_lei_8080_chunk_id_deterministic(self, brasil_lei_8080: Path) -> None:
        """Dois parses do mesmo documento devem gerar mesmos IDs."""
        chunks_a = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        chunks_b = parse_document(brasil_lei_8080, NormativeRegime.BRASIL)
        ids_a = {c.id for c in chunks_a}
        ids_b = {c.id for c in chunks_b}
        assert ids_a == ids_b

    def test_parse_pdf_brasil(self, brasil_pdf: Path) -> None:
        """PDF brasileiro deve produzir chunks."""
        if not brasil_pdf.exists():
            pytest.skip("PDF não disponível")
        chunks = parse_document(brasil_pdf, NormativeRegime.BRASIL)
        assert len(chunks) > 0


class TestParseUSA:
    """Testes de parsing para documentos norte-americanos."""

    def test_parse_ssa_1902_returns_chunks(self, usa_ssa_1902: Path) -> None:
        """SSA §1902 deve produzir >10 NormChunks."""
        chunks = parse_document(usa_ssa_1902, NormativeRegime.USA)
        assert len(chunks) > 10

    def test_parse_ssa_1902_no_empty_text(self, usa_ssa_1902: Path) -> None:
        """Nenhum chunk deve ter texto vazio."""
        chunks = parse_document(usa_ssa_1902, NormativeRegime.USA)
        for chunk in chunks:
            assert chunk.text.strip(), f"Chunk {chunk.id} tem texto vazio"

    def test_parse_ssa_1902_no_empty_hierarchy(self, usa_ssa_1902: Path) -> None:
        """Nenhum chunk deve ter hierarquia vazia."""
        chunks = parse_document(usa_ssa_1902, NormativeRegime.USA)
        for chunk in chunks:
            assert chunk.hierarchy, f"Chunk {chunk.id} tem hierarquia vazia"

    def test_parse_ssa_1902_source(self, usa_ssa_1902: Path) -> None:
        """Source deve ser 'SSA Title XIX §1902'."""
        chunks = parse_document(usa_ssa_1902, NormativeRegime.USA)
        assert chunks[0].source == "SSA Title XIX §1902"

    def test_parse_ssa_1902_language(self, usa_ssa_1902: Path) -> None:
        """Idioma deve ser en."""
        chunks = parse_document(usa_ssa_1902, NormativeRegime.USA)
        assert chunks[0].language == "en"


class TestParseEU:
    """Testes de parsing para documentos europeus."""

    def test_parse_ai_act_returns_chunks(self, eu_ai_act: Path) -> None:
        """EU AI Act deve produzir >10 NormChunks."""
        chunks = parse_document(eu_ai_act, NormativeRegime.EU)
        assert len(chunks) > 10

    def test_parse_ai_act_no_empty_text(self, eu_ai_act: Path) -> None:
        """Nenhum chunk deve ter texto vazio."""
        chunks = parse_document(eu_ai_act, NormativeRegime.EU)
        for chunk in chunks:
            assert chunk.text.strip(), f"Chunk {chunk.id} tem texto vazio"

    def test_parse_ai_act_no_empty_hierarchy(self, eu_ai_act: Path) -> None:
        """Nenhum chunk deve ter hierarquia vazia."""
        chunks = parse_document(eu_ai_act, NormativeRegime.EU)
        for chunk in chunks:
            assert chunk.hierarchy, f"Chunk {chunk.id} tem hierarquia vazia"

    def test_parse_ai_act_source(self, eu_ai_act: Path) -> None:
        """Source deve ser 'EU AI Act 2024/1689'."""
        chunks = parse_document(eu_ai_act, NormativeRegime.EU)
        assert chunks[0].source == "EU AI Act 2024/1689"

    def test_parse_ai_act_has_article_14(self, eu_ai_act: Path) -> None:
        """Article 14 (Human oversight) deve estar presente."""
        chunks = parse_document(eu_ai_act, NormativeRegime.EU)
        art14 = [c for c in chunks if "Article 14" in c.hierarchy]
        assert len(art14) > 0, "Article 14 não encontrado"


class TestParseEdgeCases:
    """Testes de edge cases."""

    def test_unsupported_extension_raises(self, tmp_path: Path) -> None:
        """Extensão não suportada deve levantar ValueError."""
        fake = tmp_path / "doc.docx"
        fake.write_text("test")
        with pytest.raises(ValueError, match="Formato não suportado"):
            parse_document(fake, NormativeRegime.BRASIL)
