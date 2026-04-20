"""E2 — Deontic extraction: LLM-powered normative proposition analysis."""

from qfeng.c1_digestion.deontic.extractor import extract_deontic
from qfeng.c1_digestion.deontic.few_shots import FEW_SHOT_EXAMPLES, get_few_shots
from qfeng.c1_digestion.deontic.prompts import SYSTEM_PROMPT, render_user_prompt
from qfeng.c1_digestion.deontic.reporter import E2BatchResult, generate_e2_report

__all__ = [
    "extract_deontic",
    "E2BatchResult",
    "generate_e2_report",
    "FEW_SHOT_EXAMPLES",
    "get_few_shots",
    "SYSTEM_PROMPT",
    "render_user_prompt",
]
