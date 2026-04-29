"""Schema de extração de fatos para Q-FENG extrator Claude Sonnet.

ScenarioExtraction: output estruturado do extrator.
render_to_asp: converte ScenarioExtraction → predicados ASP (.lp).
"""
from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field


class FactAtom(BaseModel):
    """Um fato individual extraído do cenário."""
    predicate: str = Field(..., description="Nome do predicado ASP (snake_case)")
    args: list[str] = Field(default_factory=list, description="Argumentos do predicado")
    comment: str = Field(default="", description="Justificativa textual da extração")


class ScenarioExtraction(BaseModel):
    """Output estruturado do extrator Claude Sonnet para um cenário CLT."""
    scenario_id: str
    scenario_type: str  # e.g. "T-CLT-01"
    facts: list[FactAtom] = Field(default_factory=list)
    extraction_confidence: float = Field(..., ge=0.0, le=1.0)
    abstain: bool = Field(default=False)
    abstain_reason: str = Field(default="")
    model_used: str = Field(default="")
    tokens_in: int = Field(default=0)
    tokens_out: int = Field(default=0)


def render_to_asp(extraction: ScenarioExtraction) -> str:
    """Converte ScenarioExtraction em predicados ASP (.lp format).

    Se abstain=True, retorna comentário explicativo sem predicados.
    """
    lines: list[str] = [
        f"% scenario_id: {extraction.scenario_id}",
        f"% scenario_type: {extraction.scenario_type}",
        f"% extraction_confidence: {extraction.extraction_confidence:.3f}",
        f"% model: {extraction.model_used}",
        "",
    ]

    if extraction.abstain:
        lines.append(f"% ABSTAIN: {extraction.abstain_reason}")
        return "\n".join(lines)

    for fact in extraction.facts:
        if fact.args:
            args_str = ", ".join(fact.args)
            atom = f"{fact.predicate}({args_str})."
        else:
            atom = f"{fact.predicate}."
        if fact.comment:
            lines.append(f"% {fact.comment}")
        lines.append(atom)

    return "\n".join(lines)
