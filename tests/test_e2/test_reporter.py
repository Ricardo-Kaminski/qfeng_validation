"""Testes para o reporter E2."""

from pathlib import Path

from qfeng.c1_digestion.deontic.reporter import E2BatchResult, generate_e2_report
from qfeng.core.schemas import (
    DeonticAtom,
    DeonticModality,
    NormativeRegime,
    NormativeStrength,
    NormChunk,
)


def _make_chunk(chunk_id: str = "c1", regime: str = "brasil") -> NormChunk:
    """Helper para criar chunk de teste."""
    return NormChunk(
        id=chunk_id,
        source="CF/88",
        regime=NormativeRegime(regime),
        hierarchy=["Art. 196"],
        text="A saúde é direito de todos e dever do Estado.",
        language="pt-BR",
        chunk_type="principle",
    )


def _make_atom(
    atom_id: str = "a1",
    chunk_id: str = "c1",
    confidence: float = 0.9,
    modality: DeonticModality = DeonticModality.OBLIGATION,
) -> DeonticAtom:
    """Helper para criar atom de teste."""
    return DeonticAtom(
        id=atom_id,
        source_chunk_id=chunk_id,
        modality=modality,
        agent="state",
        patient="citizen",
        action="provide_healthcare",
        confidence=confidence,
        strength=NormativeStrength.CONSTITUTIONAL,
    )


class TestE2BatchResult:
    """Testes do dataclass E2BatchResult."""

    def test_record_extraction_counts(self) -> None:
        """record_extraction deve atualizar contadores."""
        result = E2BatchResult(total_chunks_in_corpus=10)
        chunk = _make_chunk()
        atoms = [_make_atom()]

        result.record_extraction(chunk, atoms, from_cache=False)

        assert result.total_chunks_processed == 1
        assert result.total_atoms_extracted == 1
        assert result.llm_calls == 1
        assert result.cache_hits == 0

    def test_record_cache_hit(self) -> None:
        """from_cache=True deve incrementar cache_hits."""
        result = E2BatchResult()
        chunk = _make_chunk()
        atoms = [_make_atom()]

        result.record_extraction(chunk, atoms, from_cache=True)

        assert result.cache_hits == 1
        assert result.llm_calls == 0

    def test_record_zero_atoms(self) -> None:
        """Chunks sem atoms devem ir para zero_atom_chunks."""
        result = E2BatchResult()
        chunk = _make_chunk()

        result.record_extraction(chunk, [], from_cache=False)

        assert len(result.zero_atom_chunks) == 1
        assert result.zero_atom_chunks[0].id == "c1"

    def test_record_low_confidence(self) -> None:
        """Atoms com confidence < 0.5 devem ir para alertas."""
        result = E2BatchResult()
        chunk = _make_chunk()
        atom = _make_atom(confidence=0.3)

        result.record_extraction(chunk, [atom], from_cache=False)

        assert len(result.low_confidence_atoms) == 1

    def test_modality_distribution(self) -> None:
        """Distribuição de modality deve ser contabilizada."""
        result = E2BatchResult()
        chunk = _make_chunk()
        atoms = [
            _make_atom("a1", modality=DeonticModality.OBLIGATION),
            _make_atom("a2", modality=DeonticModality.PROHIBITION),
            _make_atom("a3", modality=DeonticModality.OBLIGATION),
        ]

        result.record_extraction(chunk, atoms, from_cache=False)

        assert result.modality_distribution["obligation"] == 2
        assert result.modality_distribution["prohibition"] == 1

    def test_samples_limited_to_3(self) -> None:
        """Amostras por regime devem ser limitadas a 3."""
        result = E2BatchResult()
        for i in range(5):
            chunk = _make_chunk(f"c{i}")
            atom = _make_atom(f"a{i}", f"c{i}")
            result.record_extraction(chunk, [atom], from_cache=False)

        assert len(result.sample_atoms["brasil"]) == 3

    def test_confidence_values_collected(self) -> None:
        """Valores de confidence devem ser coletados para métricas."""
        result = E2BatchResult()
        chunk = _make_chunk()
        atoms = [
            _make_atom("a1", confidence=0.9),
            _make_atom("a2", confidence=0.7),
        ]

        result.record_extraction(chunk, atoms, from_cache=False)

        assert len(result.confidence_values) == 2
        assert 0.9 in result.confidence_values


class TestGenerateE2Report:
    """Testes de geração do relatório E2."""

    def test_report_file_created(self, tmp_path: Path) -> None:
        """Deve criar arquivo de relatório."""
        result = E2BatchResult(total_chunks_in_corpus=10)
        path = tmp_path / "e2_report.md"

        generate_e2_report(result, path)

        assert path.exists()

    def test_report_contains_sections(self, tmp_path: Path) -> None:
        """Relatório deve conter todas as seções esperadas."""
        result = E2BatchResult(total_chunks_in_corpus=100)
        chunk = _make_chunk()
        atoms = [_make_atom(confidence=0.9)]
        result.record_extraction(chunk, atoms, from_cache=False)

        path = tmp_path / "e2_report.md"
        generate_e2_report(result, path)

        content = path.read_text(encoding="utf-8")
        assert "## Resumo" in content
        assert "## DeonticAtoms por Regime" in content
        assert "## Distribuição de Modality" in content
        assert "## Métricas de Confidence" in content
        assert "## Amostras de DeonticAtoms" in content

    def test_report_with_zero_atoms(self, tmp_path: Path) -> None:
        """Relatório deve listar chunks com 0 atoms."""
        result = E2BatchResult()
        chunk = _make_chunk()
        result.record_extraction(chunk, [], from_cache=False)

        path = tmp_path / "e2_report.md"
        generate_e2_report(result, path)

        content = path.read_text(encoding="utf-8")
        assert "Chunks com 0 DeonticAtoms" in content
        assert "CF/88" in content

    def test_report_with_low_confidence(self, tmp_path: Path) -> None:
        """Relatório deve listar alertas de low confidence."""
        result = E2BatchResult()
        chunk = _make_chunk()
        atom = _make_atom(confidence=0.3)
        result.record_extraction(chunk, [atom], from_cache=False)

        path = tmp_path / "e2_report.md"
        generate_e2_report(result, path)

        content = path.read_text(encoding="utf-8")
        assert "Confidence < 0.5" in content

    def test_report_empty_result(self, tmp_path: Path) -> None:
        """Relatório com resultado vazio não deve falhar."""
        result = E2BatchResult()
        path = tmp_path / "e2_report.md"

        generate_e2_report(result, path)

        assert path.exists()
        content = path.read_text(encoding="utf-8")
        assert "Sem dados de confidence" in content
