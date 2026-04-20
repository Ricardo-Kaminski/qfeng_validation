"""Fixtures compartilhadas para testes E2."""

from __future__ import annotations

import pytest

from qfeng.core.schemas import NormativeRegime, NormChunk


@pytest.fixture()
def brasil_chunk() -> NormChunk:
    """Chunk brasileiro de exemplo (Art. 196 CF/88)."""
    return NormChunk(
        id="test_br_196",
        source="CF/88",
        regime=NormativeRegime.BRASIL,
        hierarchy=["Art. 196"],
        text=(
            "A saúde é direito de todos e dever do Estado, garantido "
            "mediante políticas sociais e econômicas que visem à redução "
            "do risco de doença e de outros agravos e ao acesso universal "
            "e igualitário às ações e serviços para sua promoção, proteção "
            "e recuperação."
        ),
        language="pt-BR",
        chunk_type="principle",
    )


@pytest.fixture()
def usa_chunk() -> NormChunk:
    """Chunk norte-americano de exemplo (SSA §1902(a)(10))."""
    return NormChunk(
        id="test_us_1902a10",
        source="SSA Title XIX §1902",
        regime=NormativeRegime.USA,
        hierarchy=["(a)", "(10)"],
        text=(
            "provide that the State plan shall include a description of "
            "the standards and methods to be used in determining eligibility "
            "for and the extent of medical assistance under the plan."
        ),
        language="en",
        chunk_type="obligation",
    )


@pytest.fixture()
def eu_chunk() -> NormChunk:
    """Chunk europeu de exemplo (AI Act Art. 14)."""
    return NormChunk(
        id="test_eu_art14",
        source="EU AI Act 2024/1689",
        regime=NormativeRegime.EU,
        hierarchy=["Article 14", "1"],
        text=(
            "High-risk AI systems shall be designed and developed in such "
            "a way, including with appropriate human-machine interface tools, "
            "that they can be effectively overseen by natural persons during "
            "the period in which they are in use."
        ),
        language="en",
        chunk_type="obligation",
    )


@pytest.fixture()
def mock_llm_response_brasil() -> str:
    """Resposta LLM simulada para chunk brasileiro."""
    return """[
  {
    "modality": "obligation",
    "agent": "state",
    "patient": "citizen",
    "action": "guarantee_universal_healthcare_access",
    "conditions": [],
    "threshold": null,
    "consequence": "mandado_seguranca",
    "temporality": "unconditional",
    "strength": "constitutional",
    "confidence": 0.95
  }
]"""


@pytest.fixture()
def mock_llm_response_multi() -> str:
    """Resposta LLM simulada com múltiplos atoms."""
    return """[
  {
    "modality": "obligation",
    "agent": "state",
    "patient": "citizen",
    "action": "provide_healthcare",
    "conditions": [],
    "threshold": null,
    "consequence": null,
    "temporality": "unconditional",
    "strength": "constitutional",
    "confidence": 0.95
  },
  {
    "modality": "obligation",
    "agent": "state",
    "patient": "citizen",
    "action": "reduce_disease_risk",
    "conditions": [],
    "threshold": null,
    "consequence": null,
    "temporality": "unconditional",
    "strength": "constitutional",
    "confidence": 0.85
  }
]"""
