"""Testes para o extractor E2 — com LLM mockado."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from qfeng.c1_digestion.deontic.extractor import (
    _dict_to_atom,
    _extract_json,
    _parse_response,
    extract_deontic,
)
from qfeng.core.schemas import (
    DeonticAtom,
    DeonticModality,
    NormativeRegime,
    NormativeStrength,
    NormChunk,
)


class TestExtractDeontic:
    """Testes de extract_deontic com LLM mockado."""

    def test_extracts_single_atom(
        self,
        brasil_chunk: NormChunk,
        mock_llm_response_brasil: str,
        tmp_path: Path,
    ) -> None:
        """Deve extrair um DeonticAtom de chunk brasileiro."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = mock_llm_response_brasil

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            atoms = extract_deontic(brasil_chunk, cache_dir=tmp_path)

        assert len(atoms) == 1
        atom = atoms[0]
        assert atom.modality == DeonticModality.OBLIGATION
        assert atom.agent == "state"
        assert atom.patient == "citizen"
        assert atom.action == "guarantee_universal_healthcare_access"
        assert atom.confidence == 0.95
        assert atom.source_chunk_id == brasil_chunk.id

    def test_extracts_multiple_atoms(
        self,
        brasil_chunk: NormChunk,
        mock_llm_response_multi: str,
        tmp_path: Path,
    ) -> None:
        """Deve extrair múltiplos DeonticAtoms de um chunk."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = mock_llm_response_multi

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            atoms = extract_deontic(brasil_chunk, cache_dir=tmp_path)

        assert len(atoms) == 2
        actions = {a.action for a in atoms}
        assert "provide_healthcare" in actions
        assert "reduce_disease_risk" in actions

    def test_cache_prevents_duplicate_call(
        self,
        brasil_chunk: NormChunk,
        mock_llm_response_brasil: str,
        tmp_path: Path,
    ) -> None:
        """Segunda chamada deve usar cache, não chamar LLM."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = mock_llm_response_brasil

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response

            # Primeira chamada — chama LLM
            atoms1 = extract_deontic(brasil_chunk, cache_dir=tmp_path)
            assert mock_litellm.completion.call_count == 1

            # Segunda chamada — usa cache
            atoms2 = extract_deontic(brasil_chunk, cache_dir=tmp_path)
            assert mock_litellm.completion.call_count == 1  # não chamou de novo

        assert len(atoms1) == len(atoms2)
        assert atoms1[0].id == atoms2[0].id

    def test_cache_file_created(
        self,
        brasil_chunk: NormChunk,
        mock_llm_response_brasil: str,
        tmp_path: Path,
    ) -> None:
        """Deve criar arquivo de cache após extração."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = mock_llm_response_brasil

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            extract_deontic(brasil_chunk, cache_dir=tmp_path)

        cache_file = tmp_path / f"{brasil_chunk.id}.json"
        assert cache_file.exists()

        data = json.loads(cache_file.read_text(encoding="utf-8"))
        assert isinstance(data, list)
        assert len(data) == 1

    def test_handles_empty_response(
        self,
        brasil_chunk: NormChunk,
        tmp_path: Path,
    ) -> None:
        """Deve retornar lista vazia para resposta LLM vazia."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "[]"

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            atoms = extract_deontic(brasil_chunk, cache_dir=tmp_path)

        assert atoms == []

    def test_handles_invalid_json(
        self,
        brasil_chunk: NormChunk,
        tmp_path: Path,
    ) -> None:
        """Deve retornar lista vazia para JSON inválido."""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "This is not JSON at all"

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            atoms = extract_deontic(brasil_chunk, cache_dir=tmp_path)

        assert atoms == []

    def test_concurrent_context_in_prompt(
        self,
        brasil_chunk: NormChunk,
        mock_llm_response_brasil: str,
        tmp_path: Path,
    ) -> None:
        """Chunks concorrentes devem aparecer no prompt enviado ao LLM."""
        concurrent = NormChunk(
            id="concurrent_1",
            source="Lei 8.080/1990",
            regime=NormativeRegime.BRASIL,
            hierarchy=["Art. 2"],
            text="A saúde é um direito fundamental do ser humano.",
            language="pt-BR",
            chunk_type="principle",
        )

        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = mock_llm_response_brasil

        with patch("qfeng.c1_digestion.deontic.extractor.litellm") as mock_litellm:
            mock_litellm.completion.return_value = mock_response
            extract_deontic(
                brasil_chunk,
                cache_dir=tmp_path,
                concurrent_chunks=[concurrent],
            )

            # Verificar que o prompt contém o texto concorrente
            call_args = mock_litellm.completion.call_args
            messages = call_args.kwargs["messages"]
            user_msg = messages[1]["content"]
            assert "Lei 8.080/1990" in user_msg
            assert "Concurrent" in user_msg


class TestExtractJson:
    """Testes de extração de JSON da resposta LLM."""

    def test_plain_json(self) -> None:
        """Deve extrair JSON puro."""
        result = _extract_json('[{"key": "value"}]')
        assert json.loads(result) == [{"key": "value"}]

    def test_markdown_fenced(self) -> None:
        """Deve extrair JSON de bloco markdown."""
        result = _extract_json('```json\n[{"key": "value"}]\n```')
        assert json.loads(result) == [{"key": "value"}]

    def test_markdown_fenced_no_lang(self) -> None:
        """Deve extrair JSON de bloco markdown sem indicador de linguagem."""
        result = _extract_json('```\n[{"key": "value"}]\n```')
        assert json.loads(result) == [{"key": "value"}]

    def test_with_surrounding_text(self) -> None:
        """Deve extrair JSON com texto ao redor."""
        result = _extract_json('Here is the result:\n[{"key": "value"}]\nDone.')
        assert json.loads(result) == [{"key": "value"}]


class TestParseResponse:
    """Testes de parsing da resposta em DeonticAtoms."""

    def test_valid_response(self, brasil_chunk: NormChunk) -> None:
        """Deve parsear resposta válida em DeonticAtoms."""
        raw = json.dumps([{
            "modality": "obligation",
            "agent": "state",
            "patient": "citizen",
            "action": "provide_healthcare",
            "conditions": [],
            "threshold": None,
            "consequence": None,
            "temporality": "unconditional",
            "strength": "constitutional",
            "confidence": 0.9,
        }])
        atoms = _parse_response(raw, brasil_chunk)
        assert len(atoms) == 1
        assert atoms[0].modality == DeonticModality.OBLIGATION

    def test_invalid_modality_defaults(self, brasil_chunk: NormChunk) -> None:
        """Modalidade inválida deve defaultar para OBLIGATION."""
        raw = json.dumps([{
            "modality": "invalid_modality",
            "agent": "state",
            "patient": "citizen",
            "action": "test",
            "conditions": [],
            "threshold": None,
            "consequence": None,
            "temporality": "unconditional",
            "strength": "statutory",
            "confidence": 0.5,
        }])
        atoms = _parse_response(raw, brasil_chunk)
        assert len(atoms) == 1
        assert atoms[0].modality == DeonticModality.OBLIGATION

    def test_conditions_parsed(self, brasil_chunk: NormChunk) -> None:
        """Conditions devem ser parseadas corretamente."""
        raw = json.dumps([{
            "modality": "obligation",
            "agent": "state",
            "patient": "patient",
            "action": "provide_coverage",
            "conditions": [
                {"variable": "income_fpl", "operator": "<=", "value": "138"},
                {"variable": "age", "operator": "<", "value": "19"},
            ],
            "threshold": {"fpl": "<=138"},
            "consequence": None,
            "temporality": "when_triggered",
            "strength": "regulatory",
            "confidence": 0.9,
        }])
        atoms = _parse_response(raw, brasil_chunk)
        assert len(atoms) == 1
        assert len(atoms[0].conditions) == 2
        assert atoms[0].conditions[0].variable == "income_fpl"
        assert atoms[0].threshold == {"fpl": "<=138"}

    def test_traceability(self, brasil_chunk: NormChunk) -> None:
        """source_chunk_id deve apontar para o chunk de origem."""
        raw = json.dumps([{
            "modality": "obligation",
            "agent": "state",
            "patient": "citizen",
            "action": "test",
            "conditions": [],
            "threshold": None,
            "consequence": None,
            "temporality": "unconditional",
            "strength": "statutory",
            "confidence": 0.8,
        }])
        atoms = _parse_response(raw, brasil_chunk)
        assert atoms[0].source_chunk_id == brasil_chunk.id


class TestDictToAtom:
    """Testes de conversão dict → DeonticAtom."""

    def test_confidence_clamped(self, brasil_chunk: NormChunk) -> None:
        """Confidence deve ser clamped entre 0 e 1."""
        item = {
            "modality": "obligation",
            "agent": "state",
            "patient": "citizen",
            "action": "test",
            "confidence": 1.5,
        }
        atom = _dict_to_atom(item, brasil_chunk, 0)
        assert atom.confidence == 1.0

    def test_atom_id_deterministic(self, brasil_chunk: NormChunk) -> None:
        """Mesmo input deve gerar mesmo ID."""
        item = {
            "modality": "obligation",
            "agent": "state",
            "patient": "citizen",
            "action": "test_action",
        }
        atom1 = _dict_to_atom(item, brasil_chunk, 0)
        atom2 = _dict_to_atom(item, brasil_chunk, 0)
        assert atom1.id == atom2.id

    def test_different_index_different_id(self, brasil_chunk: NormChunk) -> None:
        """Índices diferentes devem gerar IDs diferentes."""
        item = {
            "modality": "obligation",
            "agent": "state",
            "patient": "citizen",
            "action": "test_action",
        }
        atom1 = _dict_to_atom(item, brasil_chunk, 0)
        atom2 = _dict_to_atom(item, brasil_chunk, 1)
        assert atom1.id != atom2.id
