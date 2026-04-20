"""Testes para o chunker E1 — chunk_by_hierarchy e utilitários."""

import hashlib

import pytest

from qfeng.c1_digestion.ingestion.chunker import (
    chunk_by_hierarchy,
    detect_chunk_type,
    extract_cross_references,
    generate_chunk_id,
)
from qfeng.c1_digestion.ingestion.registry import REGIME_CONFIGS
from qfeng.core.schemas import NormativeRegime


class TestChunkByHierarchy:
    """Testes de segmentação hierárquica por regime."""

    def test_brasil_article_split(self) -> None:
        """Texto com Art. 1 e Art. 2 deve gerar chunks separados."""
        text = (
            "Art. 1º Esta lei regula as ações e serviços de saúde.\n"
            "Art. 2º A saúde é um direito fundamental do ser humano."
        )
        chunks = chunk_by_hierarchy(text, NormativeRegime.BRASIL, "Lei Teste")
        assert len(chunks) >= 2
        labels = [c.hierarchy[0] for c in chunks]
        assert "Art. 1" in labels
        assert "Art. 2" in labels

    def test_brasil_with_paragraphs(self) -> None:
        """Art. com § deve gerar chunks separados."""
        text = (
            "Art. 5º São objetivos do SUS:\n"
            "§ 1º O primeiro parágrafo estabelece que o Estado deve garantir.\n"
            "§ 2º O segundo parágrafo define as responsabilidades."
        )
        chunks = chunk_by_hierarchy(text, NormativeRegime.BRASIL, "Lei Teste")
        assert len(chunks) >= 2

    def test_brasil_with_incisos(self) -> None:
        """Art. com incisos romanos deve gerar chunks separados."""
        text = (
            "Art. 7º As ações e serviços públicos de saúde obedecem:\n"
            "I - universalidade de acesso aos serviços de saúde;\n"
            "II - integralidade de assistência;\n"
            "III - preservação da autonomia das pessoas."
        )
        chunks = chunk_by_hierarchy(text, NormativeRegime.BRASIL, "Lei Teste")
        assert len(chunks) >= 3

    def test_usa_section_split(self) -> None:
        """Texto com (a) e (b) deve gerar chunks separados."""
        text = (
            "(a) A State plan for medical assistance must provide.\n"
            "(1) coverage for all eligible individuals.\n"
            "(2) financial participation by the State.\n"
            "(b) The Secretary shall require compliance."
        )
        chunks = chunk_by_hierarchy(text, NormativeRegime.USA, "SSA Test")
        assert len(chunks) >= 2

    def test_eu_article_split(self) -> None:
        """Texto com Article 1 e Article 2 deve gerar chunks separados."""
        text = (
            "Article 1   The purpose of this Regulation is to improve "
            "the functioning of the internal market.\n"
            "Article 2   This Regulation shall apply to providers "
            "and deployers of AI systems."
        )
        chunks = chunk_by_hierarchy(text, NormativeRegime.EU, "EU Test")
        assert len(chunks) >= 2

    def test_empty_text_returns_empty(self) -> None:
        """Texto vazio não deve gerar chunks."""
        chunks = chunk_by_hierarchy("", NormativeRegime.BRASIL, "Vazio")
        assert len(chunks) == 0

    def test_whitespace_only_returns_empty(self) -> None:
        """Texto com apenas espaços não deve gerar chunks."""
        chunks = chunk_by_hierarchy("   \n\n  ", NormativeRegime.BRASIL, "Vazio")
        assert len(chunks) == 0

    def test_no_articles_returns_single_chunk(self) -> None:
        """Texto sem artigos deve retornar um chunk único."""
        text = "Este é um texto normativo sem divisão em artigos definidos."
        chunks = chunk_by_hierarchy(text, NormativeRegime.BRASIL, "Teste")
        assert len(chunks) == 1
        assert chunks[0].hierarchy == ["Texto Integral"]

    def test_source_propagated(self) -> None:
        """O campo source deve ser propagado para todos os chunks."""
        text = "Art. 1º Teste de propagação."
        chunks = chunk_by_hierarchy(text, NormativeRegime.BRASIL, "Minha Lei")
        for chunk in chunks:
            assert chunk.source == "Minha Lei"


class TestDetectChunkType:
    """Testes de detecção de chunk_type."""

    def test_obligation_brasil(self) -> None:
        """Texto com 'deve garantir' deve ser obligation."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        assert detect_chunk_type(
            "O Estado deve garantir o acesso universal.", config
        ) == "obligation"

    def test_definition_brasil(self) -> None:
        """Texto com 'entende-se por' deve ser definition."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        assert detect_chunk_type(
            "Entende-se por vigilância sanitária um conjunto de ações.", config
        ) == "definition"

    def test_principle_brasil(self) -> None:
        """Texto com 'direito fundamental' deve ser principle."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        assert detect_chunk_type(
            "A saúde é um direito fundamental do ser humano.", config
        ) == "principle"

    def test_obligation_usa(self) -> None:
        """Texto com 'shall provide' deve ser obligation."""
        config = REGIME_CONFIGS[NormativeRegime.USA]
        assert detect_chunk_type(
            "The State shall provide coverage for all individuals.", config
        ) == "obligation"

    def test_definition_usa(self) -> None:
        """Texto com 'means' deve ser definition."""
        config = REGIME_CONFIGS[NormativeRegime.USA]
        assert detect_chunk_type(
            "The term medical assistance means payment of services.", config
        ) == "definition"

    def test_obligation_eu(self) -> None:
        """Texto com 'shall ensure' deve ser obligation."""
        config = REGIME_CONFIGS[NormativeRegime.EU]
        assert detect_chunk_type(
            "Providers shall ensure that high-risk AI systems have human oversight.",
            config,
        ) == "obligation"


class TestExtractCrossReferences:
    """Testes de extração de referências cruzadas."""

    def test_brasil_nos_termos(self) -> None:
        """'nos termos do art. 196' deve detectar referência."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        refs = extract_cross_references(
            "nos termos do art. 196 da Constituição Federal", config
        )
        assert "196" in refs

    def test_brasil_conforme_disposto(self) -> None:
        """'conforme disposto no art. 7' deve detectar referência."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        refs = extract_cross_references(
            "conforme disposto no art. 7 desta lei", config
        )
        assert "7" in refs

    def test_usa_section_reference(self) -> None:
        """'section 1396b' deve detectar referência."""
        config = REGIME_CONFIGS[NormativeRegime.USA]
        refs = extract_cross_references(
            "pursuant to section 1396b of this title", config
        )
        assert any("1396b" in r for r in refs)

    def test_eu_article_reference(self) -> None:
        """'Article 14' deve detectar referência."""
        config = REGIME_CONFIGS[NormativeRegime.EU]
        refs = extract_cross_references(
            "in accordance with Article 14 of this Regulation", config
        )
        assert "14" in refs

    def test_no_references(self) -> None:
        """Texto sem referências deve retornar lista vazia."""
        config = REGIME_CONFIGS[NormativeRegime.BRASIL]
        refs = extract_cross_references("Texto simples sem referências.", config)
        assert refs == []


class TestGenerateChunkId:
    """Testes de geração de ID determinístico."""

    def test_deterministic(self) -> None:
        """Mesmos inputs devem gerar mesmo ID."""
        id1 = generate_chunk_id("Lei 8.080/1990", ["Art. 1"])
        id2 = generate_chunk_id("Lei 8.080/1990", ["Art. 1"])
        assert id1 == id2

    def test_different_inputs_different_ids(self) -> None:
        """Inputs diferentes devem gerar IDs diferentes."""
        id1 = generate_chunk_id("Lei 8.080/1990", ["Art. 1"])
        id2 = generate_chunk_id("Lei 8.080/1990", ["Art. 2"])
        assert id1 != id2

    def test_hash_length(self) -> None:
        """ID deve ter 16 caracteres hexadecimais."""
        chunk_id = generate_chunk_id("Teste", ["Art. 1"])
        assert len(chunk_id) == 16
        assert all(c in "0123456789abcdef" for c in chunk_id)

    def test_matches_manual_hash(self) -> None:
        """ID deve corresponder ao hash SHA-256 manual."""
        source = "Lei 8.080/1990"
        hierarchy = ["Art. 1"]
        raw = f"{source}:Art. 1"
        expected = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
        assert generate_chunk_id(source, hierarchy) == expected
