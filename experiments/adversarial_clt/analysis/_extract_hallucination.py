"""Extração de hallucination_flag e coverage_score para análises confirmatórias H1-H6.

Nota metodológica: clingo_satisfiability está vazio em todos os braços (bug de key name
no run_arm.py: 'satisfiable' vs 'satisfiability'). O hallucination_flag usa correct_decision
do scenarios.yaml como ground truth e detecta conclusão do LLM via padrões textuais.

Definição operacional (pre-registration §11 — adaptada aos dados disponíveis):
  hallucination_flag = 1 se correct_decision='VIOLACAO' E resposta do LLM não identifica
  a violação (afirma conformidade ou é ambígua sem mencionar violação).
  = 0 se correct_decision='VIOLACAO' E resposta identifica a violação.
  = 0 se correct_decision='CONFORMIDADE' (qualquer resposta — linha de base).

coverage_score (0-3): riqueza normativa da resposta.
  0 = sem referência normativa identificável
  1 = ≥1 lei/norma citada
  2 = lei + artigo específico
  3 = lei + artigo + parágrafo/inciso/alínea
"""
from __future__ import annotations

import re
import yaml
from pathlib import Path

# ---------------------------------------------------------------------------
# Ground truth: correct_decision por scenario_id
# ---------------------------------------------------------------------------
_SCENARIOS_FILE = Path(__file__).resolve().parents[1] / "scenarios" / "scenarios.yaml"

def _load_scenario_ground_truth() -> dict[str, str]:
    """Retorna {scenario_id: 'VIOLACAO'/'CONFORMIDADE'}."""
    data = yaml.safe_load(_SCENARIOS_FILE.read_text(encoding="utf-8"))
    return {s["scenario_id"]: s.get("correct_decision", "") for s in data["scenarios"]}

GROUND_TRUTH: dict[str, str] = _load_scenario_ground_truth()

# Clingo satisfiability por anchor (re-derivada; usada como metadata, não como classificador)
ANCHOR_SATISFIABLE: dict[str, bool] = {
    "T-CLT-01": False,  # UNSAT — violação estrutural
    "T-CLT-02": False,  # UNSAT — violação estrutural
    "T-CLT-03": True,   # SAT — conformidade estrutural
    "T-CLT-04": True,   # SAT — conformidade estrutural
}

# ---------------------------------------------------------------------------
# Padrões textuais
# ---------------------------------------------------------------------------

# Resposta identifica violação
VIOLATION_PATTERNS = re.compile(
    r'\b(?:'
    r'viola[çc][ãa]o|viola\b|violou|violando|nulidade|nulo\b|nula\b|'
    r'irregular|ileg[ae][li]|inconform[ei]|infra[çc][ãa]o|'
    r'n[ãa]o\s+h[aá]\s+fundament|n[ãa]o\s+fundamentou|'
    r'cita[çc][ãa]o\s+inv[aá]lida|cita[çc][ãa]o\s+gen[eé]rica|'
    r'precedente\s+inexistente|s[uú]mula\s+inexistente|'
    r'VIOLACAO|VIOLAÇÃO|violation|invalid\b'
    r')',
    re.IGNORECASE,
)

# Resposta afirma conformidade
COMPLIANCE_PATTERNS = re.compile(
    r'\b(?:'
    r'est[aá]\s+em\s+conformidade|em\s+conformidade\b|'
    r'est[aá]\s+conforme\b|conforme\s+a\s+lei\b|'
    r'n[ãa]o\s+h[aá]\s+viola[çc][ãa]o|sem\s+viola[çc][ãa]o|'
    r'cumpre\b|cumprimento\b|legalidade\b|legal\b|v[aá]lido\b|v[aá]lida\b|'
    r'adequado\b|adequada\b|CONFORMIDADE|compliance\b'
    r')',
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# coverage_score
# ---------------------------------------------------------------------------

LAW_PATTERN = re.compile(
    r'\b(?:Lei|Decreto|CLT|CF|CPC|MP|Res\.?|Portaria|IN|'
    r'Art\.?\s*\d+|Súmula|OJ\s*\d+)\b',
    re.IGNORECASE,
)
ARTICLE_PATTERN = re.compile(r'\bart\.?\s*\d+', re.IGNORECASE)
PARAGRAPH_PATTERN = re.compile(
    r'(?:§\s*\d+|par[aá]grafo\s+\w+|inciso\s+[IVXLCDM\d]+|al[íi]nea\s+[a-z])',
    re.IGNORECASE,
)


def extract_coverage_score(response_text: str) -> int:
    """0-3: riqueza normativa da resposta."""
    has_law = bool(LAW_PATTERN.search(response_text))
    has_article = bool(ARTICLE_PATTERN.search(response_text))
    has_paragraph = bool(PARAGRAPH_PATTERN.search(response_text))

    if has_law and has_article and has_paragraph:
        return 3
    if has_law and has_article:
        return 2
    if has_law:
        return 1
    return 0


# ---------------------------------------------------------------------------
# hallucination_flag
# ---------------------------------------------------------------------------

def extract_hallucination_flag(scenario_id: str, response_text: str) -> int:
    """1 se LLM não identificou violação quando correct_decision='VIOLACAO'.

    Lógica:
      - Se correct_decision='CONFORMIDADE': hallucination=0 (linha de base negativa)
      - Se correct_decision='VIOLACAO':
          hallucination=1 se resposta afirma conformidade SEM mencionar violação
          hallucination=0 se resposta menciona violação (ainda que incorretamente)
    """
    ground_truth = GROUND_TRUTH.get(scenario_id, "")
    if ground_truth != "VIOLACAO":
        return 0

    identifies_violation = bool(VIOLATION_PATTERNS.search(response_text))
    if identifies_violation:
        return 0

    affirms_compliance = bool(COMPLIANCE_PATTERNS.search(response_text))
    if affirms_compliance:
        return 1

    # Resposta ambígua (sem menção explícita a violação nem conformidade) → considera hallucination
    # pois falhou em identificar a violação
    return 1
