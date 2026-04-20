"""Testes para detecção de concorrência normativa (token overlap)."""

from qfeng.c1_digestion.ingestion.runner import _detect_concurrencies, _tokenize
from qfeng.core.schemas import NormChunk, NormativeRegime


def _make_chunk(
    chunk_id: str,
    source: str,
    text: str,
    regime: NormativeRegime = NormativeRegime.BRASIL,
) -> NormChunk:
    """Helper para criar chunks sintéticos."""
    return NormChunk(
        id=chunk_id,
        source=source,
        regime=regime,
        hierarchy=["Art. 1"],
        text=text,
        language="pt-BR",
    )


class TestTokenize:
    """Testes da função de tokenização."""

    def test_removes_stopwords(self) -> None:
        """Stopwords devem ser removidas."""
        tokens = _tokenize("o Estado deve garantir a saúde")
        assert "o" not in tokens
        assert "a" not in tokens
        assert "saúde" in tokens

    def test_lowercases(self) -> None:
        """Tokens devem ser lowercase."""
        tokens = _tokenize("Estado DEVE Garantir")
        assert "estado" in tokens
        assert "deve" in tokens

    def test_strips_punctuation(self) -> None:
        """Pontuação deve ser removida dos tokens."""
        tokens = _tokenize("saúde, educação; moradia.")
        assert "saúde" in tokens
        assert "educação" in tokens

    def test_short_words_excluded(self) -> None:
        """Palavras com 2 ou menos caracteres devem ser excluídas."""
        tokens = _tokenize("um de os as")
        assert len(tokens) == 0


class TestDetectConcurrencies:
    """Testes de detecção de concorrência por Jaccard."""

    def test_identical_text_different_sources(self) -> None:
        """Chunks com texto idêntico de fontes diferentes devem ser concorrentes."""
        text = "O Estado deve garantir acesso universal aos serviços de saúde"
        chunks = {
            "brasil": [
                _make_chunk("a1", "CF/88", text),
                _make_chunk("a2", "Lei 8.080/1990", text),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.55)
        assert len(pairs) > 0
        assert pairs[0][2] >= 0.55

    def test_same_source_no_concurrency(self) -> None:
        """Chunks da mesma fonte não devem ser comparados."""
        text = "O Estado deve garantir acesso universal"
        chunks = {
            "brasil": [
                _make_chunk("a1", "CF/88", text),
                _make_chunk("a2", "CF/88", text + " adicional"),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.35)
        assert len(pairs) == 0

    def test_unrelated_text_no_concurrency(self) -> None:
        """Chunks com texto completamente diferente não devem ser concorrentes."""
        chunks = {
            "brasil": [
                _make_chunk("a1", "CF/88", "O direito à saúde é garantido"),
                _make_chunk("a2", "Lei 8.080/1990", "A penalidade aplicável será multa"),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.55)
        assert len(pairs) == 0

    def test_partial_overlap(self) -> None:
        """Chunks com sobreposição parcial devem ser detectados se acima do threshold."""
        chunks = {
            "brasil": [
                _make_chunk(
                    "a1", "CF/88",
                    "O Estado deve garantir acesso universal e igualitário "
                    "aos serviços de saúde pública e assistência médica"
                ),
                _make_chunk(
                    "a2", "Lei 8.080/1990",
                    "Compete ao Estado garantir acesso universal e igualitário "
                    "aos serviços do Sistema Único de Saúde"
                ),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.30)
        assert len(pairs) > 0

    def test_cross_regime_not_compared(self) -> None:
        """Chunks de regimes diferentes não devem ser comparados entre si."""
        text = "The State shall ensure universal access to healthcare"
        chunks = {
            "brasil": [_make_chunk("a1", "CF/88", text, NormativeRegime.BRASIL)],
            "usa": [_make_chunk("a2", "SSA", text, NormativeRegime.USA)],
        }
        pairs = _detect_concurrencies(chunks, threshold=0.35)
        assert len(pairs) == 0

    def test_no_duplicate_pairs(self) -> None:
        """Mesmo par não deve aparecer mais de uma vez."""
        text = "O Estado deve garantir acesso universal aos serviços de saúde"
        chunks = {
            "brasil": [
                _make_chunk("a1", "CF/88", text),
                _make_chunk("a2", "Lei 8.080/1990", text),
                _make_chunk("a3", "Lei 8.142/1990", text),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.55)
        pair_keys = [frozenset({p[0], p[1]}) for p in pairs]
        assert len(pair_keys) == len(set(pair_keys)), "Pares duplicados encontrados"

    def test_short_text_excluded(self) -> None:
        """Chunks com menos de 3 tokens significativos devem ser ignorados."""
        chunks = {
            "brasil": [
                _make_chunk("a1", "CF/88", "saúde"),
                _make_chunk("a2", "Lei 8.080/1990", "saúde"),
            ]
        }
        pairs = _detect_concurrencies(chunks, threshold=0.01)
        assert len(pairs) == 0
