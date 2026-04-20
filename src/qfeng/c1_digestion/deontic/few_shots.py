"""Few-shot examples for E2 deontic extraction.

Manually crafted examples per regime showing the expected
input (NormChunk text) and output (DeonticAtom JSON) format.
These are injected into the LLM prompt to guide extraction quality.

NOTE: Kept to 1 example per regime (3 total) to minimize context
size for local LLM inference (~800 tokens vs ~3200 with full set).
"""

from __future__ import annotations

# ── Brasil / SUS ──────────────────────────────────────────────────────

BRASIL_EXAMPLES: list[dict[str, str]] = [
    {
        "input": (
            "Source: CF/88, Hierarchy: Art. 196\n"
            "Text: A saúde é direito de todos e dever do Estado, garantido "
            "mediante políticas sociais e econômicas que visem à redução do "
            "risco de doença e de outros agravos e ao acesso universal e "
            "igualitário às ações e serviços para sua promoção, proteção e "
            "recuperação."
        ),
        "output": """[
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
]""",
    },
]

# ── USA / Medicaid ────────────────────────────────────────────────────

USA_EXAMPLES: list[dict[str, str]] = [
    {
        "input": (
            "Source: 42 CFR Part 435, Hierarchy: § 435.110, (a)\n"
            "Text: The agency must provide Medicaid to individuals under "
            "age 19 whose family income is at or below 138 percent of the "
            "Federal poverty level."
        ),
        "output": """[
  {
    "modality": "obligation",
    "agent": "state_medicaid_agency",
    "patient": "individual_under_19",
    "action": "provide_medicaid_coverage",
    "conditions": [
      {"variable": "age", "operator": "<", "value": "19"},
      {"variable": "family_income_fpl_pct", "operator": "<=", "value": "138"}
    ],
    "threshold": {"fpl_percentage": "<=138"},
    "consequence": "federal_compliance_violation",
    "temporality": "unconditional",
    "strength": "regulatory",
    "confidence": 0.95
  }
]""",
    },
]

# ── EU / AI Act ───────────────────────────────────────────────────────

EU_EXAMPLES: list[dict[str, str]] = [
    {
        "input": (
            "Source: EU AI Act 2024/1689, Hierarchy: Article 14, 1\n"
            "Text: High-risk AI systems shall be designed and developed in "
            "such a way, including with appropriate human-machine interface "
            "tools, that they can be effectively overseen by natural persons "
            "during the period in which they are in use."
        ),
        "output": """[
  {
    "modality": "obligation",
    "agent": "provider",
    "patient": "ai_system",
    "action": "design_for_human_oversight",
    "conditions": [
      {"variable": "risk_class", "operator": "==", "value": "high"}
    ],
    "threshold": null,
    "consequence": "non_conformity_procedure",
    "temporality": "unconditional",
    "strength": "statutory",
    "confidence": 0.95
  }
]""",
    },
]

# ── Lookup por regime ─────────────────────────────────────────────────

FEW_SHOT_EXAMPLES: dict[str, list[dict[str, str]]] = {
    "brasil": BRASIL_EXAMPLES,
    "usa": USA_EXAMPLES,
    "eu": EU_EXAMPLES,
}


def get_few_shots(regime: str) -> str:
    """Formata os few-shot examples de um regime para inclusão no prompt.

    Args:
        regime: O regime normativo (brasil, usa, eu).

    Returns:
        String formatada com os exemplos input/output.
    """
    examples = FEW_SHOT_EXAMPLES.get(regime, [])
    if not examples:
        return ""

    parts: list[str] = ["## Few-shot Examples\n"]
    for i, ex in enumerate(examples, 1):
        parts.append(f"### Example {i}")
        parts.append(f"**Input:**\n{ex['input']}\n")
        parts.append(f"**Expected Output:**\n```json\n{ex['output']}\n```\n")

    return "\n".join(parts)
