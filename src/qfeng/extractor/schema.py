"""Schema de extração de fatos Q-FENG (passthrough manual).

ScenarioExtraction: output estruturado do extrator.
render_to_asp: converte ScenarioExtraction → predicados ASP (.lp).

Operacionalização: extração executada por Claude Opus 4.7 em sessão
supervisionada (P_FASE2.0), não por chamada Anthropic API.
"""
from __future__ import annotations
from pydantic import BaseModel, Field


class FactAtom(BaseModel):
    """Um fato individual extraído do cenário."""
    predicate: str = Field(..., description="Nome do predicado ASP (snake_case)")
    args: list[str] = Field(default_factory=list, description="Argumentos do predicado")
    comment: str = Field(default="", description="Justificativa textual / source span")


class ScenarioExtraction(BaseModel):
    """Output estruturado do extrator Q-FENG para um cenário CLT.

    Operacionalização: produzido por Claude Opus 4.7 em sessão de chat
    supervisionada por especialista em Direito do Trabalho brasileiro
    (rastreabilidade humano-no-loop, alinhada com VSM).
    """
    scenario_id: str
    scenario_type: str  # e.g. "T-CLT-01", "T-CTRL-NEG"
    facts: list[FactAtom] = Field(default_factory=list)
    extraction_confidence: float = Field(..., ge=0.0, le=1.0)
    abstain: bool = Field(default=False)
    abstain_reason: str = Field(default="")

    # Rastreabilidade da extração (passthrough manual)
    extractor_model: str = Field(
        default="claude-opus-4-7-passthrough",
        description="Identificador do extrator. 'passthrough' indica execução "
                    "em sessão de chat supervisionada (não chamada API).",
    )
    extractor_session_id: str = Field(
        default="",
        description="ID da sessão de chat onde a extração foi feita "
                    "(rastreabilidade humano-no-loop).",
    )
    supervised_by: str = Field(
        default="",
        description="Identificador do especialista supervisor "
                    "(e.g., 'Ricardo da Silva Kaminski (ORCID 0000-0002-8882-9248)').",
    )

    # Compatibilidade com schema legado do Code (não usar em extração nova)
    model_used: str = Field(default="", description="DEPRECATED: usar extractor_model.")
    tokens_in: int = Field(default=0, description="Não aplicável em passthrough manual.")
    tokens_out: int = Field(default=0, description="Não aplicável em passthrough manual.")


def render_to_asp(extraction: ScenarioExtraction) -> str:
    """Converte ScenarioExtraction em predicados ASP (.lp format).

    Convenções:
      - Comentários começam com %
      - Cada fato termina com ponto
      - source_span (campo `comment` do FactAtom) aparece como comentário
        antes do fato correspondente
      - Se abstain=True, retorna apenas comentários explicativos sem fatos

    Args:
        extraction: instância validada de ScenarioExtraction

    Returns:
        Conteúdo do arquivo .lp como string UTF-8
    """
    lines: list[str] = [
        f"% Extracao Q-FENG (passthrough manual) para {extraction.scenario_id}",
        f"% Tipo: {extraction.scenario_type}",
        f"% Confianca: {extraction.extraction_confidence:.3f}",
        f"% Extractor: {extraction.extractor_model}",
    ]
    if extraction.supervised_by:
        lines.append(f"% Supervisor: {extraction.supervised_by}")
    if extraction.extractor_session_id:
        lines.append(f"% Sessao: {extraction.extractor_session_id}")
    lines.append("")

    if extraction.abstain:
        lines.append(f"% ABSTAIN: {extraction.abstain_reason}")
        return "\n".join(lines) + "\n"

    for fact in extraction.facts:
        if fact.comment:
            lines.append(f"% {fact.comment}")
        if fact.args:
            args_str = ", ".join(fact.args)
            atom = f"{fact.predicate}({args_str})."
        else:
            atom = f"{fact.predicate}."
        lines.append(atom)

    return "\n".join(lines) + "\n"
