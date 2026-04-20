"""Core data schemas for Q-FENG.

All regime-agnostic data structures. These schemas define the
contracts between pipeline stages — every module communicates
through these types.
"""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


# ── Enums ──────────────────────────────────────────────────────────


class DeonticModality(StrEnum):
    """Hohfeldian deontic modalities."""
    OBLIGATION = "obligation"
    PROHIBITION = "prohibition"
    PERMISSION = "permission"
    FACULTY = "faculty"


class NormativeStrength(StrEnum):
    """Hierarchical strength of normative source."""
    CONSTITUTIONAL = "constitutional"
    STATUTORY = "statutory"
    REGULATORY = "regulatory"
    OPERATIONAL = "operational"


class SovereigntyClass(StrEnum):
    """Predicate sovereignty classification — the core normative decision."""
    SOVEREIGN = "sovereign"   # excluded from gradient, axiom
    ELASTIC = "elastic"       # subject to optimization


class GovernanceDecision(StrEnum):
    """Circuit Breaker output."""
    STAC = "stac"             # Stabilized — execute
    HITL = "hitl"             # Escalate to human
    BLOCK = "block"           # Block action


class NormativeRegime(StrEnum):
    """Supported normative regimes."""
    BRASIL = "brasil"
    USA = "usa"
    EU = "eu"


# ── E1: Ingestion schemas ──────────────────────────────────────────


class NormChunk(BaseModel):
    """A minimal unit of normative text, parsed and structured.

    Each chunk should contain exactly one normative proposition —
    something that can generate one or a few deontic predicates.
    """
    id: str = Field(description="Deterministic hash of source + hierarchy")
    source: str = Field(description="e.g. 'CF/88', 'SSA_Title_XIX', 'EU_AI_Act'")
    regime: NormativeRegime
    hierarchy: list[str] = Field(
        description="Structural path: ['Art. 196', 'caput'] or ['Title XIX', 'Sec. 1902', '(a)(10)']"
    )
    text: str = Field(description="Original normative text, verbatim")
    language: str = Field(default="pt-BR", description="ISO language code")
    effective_date: str | None = Field(default=None, description="Date norm took effect")
    cross_references: list[str] = Field(
        default_factory=list,
        description="References to other articles/norms"
    )
    chunk_type: str = Field(
        default="obligation",
        description="principle | obligation | definition | procedure | sanction"
    )


# ── E2: Deontic extraction schemas ────────────────────────────────


class DeonticCondition(BaseModel):
    """A single condition that gates a deontic atom."""
    variable: str = Field(description="e.g. 'icu_occupancy', 'income', 'risk_class'")
    operator: str = Field(description=">, >=, <, <=, ==, !=, in")
    value: str = Field(description="Threshold value or category")


class DeonticAtom(BaseModel):
    """The fundamental unit of deontic extraction.

    Represents one normative proposition extracted from a NormChunk
    by the LLM-powered deontic extractor. Each atom maps to one
    or a few Clingo predicates.
    """
    id: str = Field(description="Unique identifier")
    source_chunk_id: str = Field(description="Traceability to NormChunk")
    modality: DeonticModality
    agent: str = Field(description="Who bears the obligation: 'state', 'deployer', 'provider'")
    patient: str = Field(description="Who/what is affected: 'citizen', 'patient', 'system'")
    action: str = Field(description="Mandated/prohibited action: 'provide_healthcare'")
    conditions: list[DeonticCondition] = Field(default_factory=list)
    threshold: dict[str, Any] | None = Field(
        default=None,
        description="Numeric thresholds: {'rate': '>0.80', 'income': '<=138%FPL'}"
    )
    consequence: str | None = Field(
        default=None,
        description="What happens on violation: 'mandado_seguranca', 'penalty', 'audit'"
    )
    temporality: str = Field(
        default="unconditional",
        description="unconditional | when_triggered | periodic | anticipatory"
    )
    strength: NormativeStrength = Field(default=NormativeStrength.STATUTORY)
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0,
        description="LLM confidence in extraction quality"
    )


# ── E3/E4: Predicate schemas ──────────────────────────────────────


class ClingoPredicate(BaseModel):
    """A single Clingo/dPASP predicate, generated and validated."""
    id: str
    rule: str = Field(description="The .lp rule text")
    source_atom_id: str = Field(description="Traceability to DeonticAtom")
    source_chunk_id: str = Field(description="Traceability to NormChunk")
    sovereignty: SovereigntyClass | None = Field(
        default=None,
        description="Set during HITL validation"
    )
    sovereignty_justification: str | None = Field(default=None)
    syntax_valid: bool = Field(default=False)
    validated_by: str | None = Field(default=None)
    validated_at: datetime | None = Field(default=None)
    version: int = Field(default=1)


# ── E5: Test schemas ──────────────────────────────────────────────


class SymbolicTest(BaseModel):
    """A unit test for a normative predicate."""
    id: str
    description: str
    setup_facts: list[str] = Field(description="Ground facts for the test scenario")
    expected_true: list[str] = Field(
        default_factory=list,
        description="Atoms that must be in the answer set"
    )
    expected_false: list[str] = Field(
        default_factory=list,
        description="Atoms that must NOT be in the answer set"
    )
    target_predicates: list[str] = Field(
        description="Which predicate IDs this test covers"
    )


# ── C2: Inference & Governance schemas ────────────────────────────


class InferenceOutput(BaseModel):
    """Model-agnostic output from any S1 model.

    This is the universal contract: any model (XGBoost, LSTM, LLM,
    CNN) that wants to be governed by Q-FENG must produce this.
    """
    model_id: str
    model_type: str = Field(description="llm | predictive | prescriptive | simulation")
    prediction: list[float] = Field(description="Normalized output vector")
    confidence: float = Field(ge=0.0, le=1.0)
    features_used: list[str] = Field(default_factory=list)
    context: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.now)


class InterferenceResult(BaseModel):
    """Output of the Quantum Interference Calculator."""
    theta: float = Field(description="Ontological Friction angle in radians")
    theta_degrees: float = Field(description="θ in degrees for readability")
    cos_theta: float
    p_action: float = Field(description="P(Action) via Born Rule with interference")
    alpha_sq: float = Field(description="|α|² — model confidence component")
    beta_sq: float = Field(description="|β|² — normative strength component")
    interference_term: float = Field(description="2|α||β|cos(θ)")
    decision: GovernanceDecision
    diagnosis: list[str] = Field(
        default_factory=list,
        description="Which predicates were tensioned and by what margin"
    )
    theta_eff: float | None = Field(
        default=None,
        description="Markovian extension θ_eff if temporal data available"
    )
