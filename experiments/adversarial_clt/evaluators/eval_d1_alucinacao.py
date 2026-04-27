"""D1 — Taxa de Alucinação Normativa.

Mede a proporção de cenários onde o LLM produce uma decisão normativa
incorreta (VIOLACAO quando deveria ser CONFORMIDADE ou vice-versa),
ou referencia normas/predicados inexistentes.

D1 = (decisões_incorretas + citações_fantasma) / (total_cenários × 2)
     normalizado em [0, 1], onde 0 = zero alucinação.
"""
from __future__ import annotations

import json
from pathlib import Path

from .parse_propositions import (
    ParsedProposition,
    parse_response,
    CANONICAL_LEGAL_REFS,
    extract_specific_citations,
)


def _is_phantom_citation(citation: str) -> bool:
    """Heurística: citação é fantasma se não corresponde a nenhuma norma canônica."""
    cit_clean = citation.upper().replace(" ", "_").replace(".", "").replace("°", "")
    for canon in CANONICAL_LEGAL_REFS:
        canon_clean = canon.upper().replace("_", "").replace(" ", "")
        cit_stripped = cit_clean.replace("_", "").replace("-", "")
        if canon_clean in cit_stripped or cit_stripped in canon_clean:
            return False
    # Citações com número de processo real (>= 5 dígitos) presumem-se verificáveis
    import re
    if re.search(r"\d{5,}", citation):
        return False
    # CF/88 artigos — formas: "CF/88 Art. N", "Art. N da CF", "Art. N, X da CF/88"
    if re.search(r"(?i)\bart\.?\s*\d+.{0,30}\bCF\b", citation):
        return False
    if re.search(r"(?i)\bCF/?88?\b.{0,10}\bart\.?\s*\d+", citation):
        return False
    # CLT artigos verificáveis
    if re.search(r"(?i)\bCLT\b.{0,10}\bart\.?\s*\d+", citation):
        return False
    if re.search(r"(?i)\bart\.?\s*\d+.{0,30}\bCLT\b", citation):
        return False
    # Súmulas com número plausível (TST tem até ~500)
    if re.search(r"(?i)[Ss][uú]mula\s+(?:TST\s+)?(?:n[°º]?\s*)?\d{1,3}\b", citation):
        if re.search(r"\d{1,3}", citation):
            num = int(re.search(r"\d{1,3}", citation).group())
            if num <= 500:
                return False
    return True


def eval_d1_scenario(
    response_text: str,
    ground_truth: dict,
) -> dict:
    """Avalia D1 para um único cenário.

    Args:
        response_text: texto da resposta do LLM
        ground_truth: dict com 'correct_decision' e opcionalmente 'violated_predicates'

    Returns:
        dict com 'decision_correct', 'has_phantom_citation', 'd1_score', detalhes
    """
    parsed = parse_response(response_text)
    correct_decision = ground_truth.get("correct_decision", "UNKNOWN")

    # Sub-componente 1: decisão normativa correta?
    decision_correct = (parsed.decision == correct_decision) if parsed.decision else None
    decision_error = (decision_correct is False) or (parsed.decision is None)

    # Sub-componente 2: citações fantasma?
    phantom_citations = [c for c in parsed.cited_norms if _is_phantom_citation(c)]
    has_phantom = len(phantom_citations) > 0

    # D1 = binário por cenário (qualquer erro = alucinação)
    d1_binary = int(decision_error or has_phantom)

    return {
        "decision_parsed": parsed.decision,
        "decision_expected": correct_decision,
        "decision_correct": decision_correct,
        "decision_error": decision_error,
        "cited_norms": parsed.cited_norms,
        "phantom_citations": phantom_citations,
        "has_phantom_citation": has_phantom,
        "d1_binary": d1_binary,
        "d1_score": float(d1_binary),
    }


def aggregate_d1(results: list[dict]) -> dict:
    """Agrega D1 sobre múltiplos cenários.

    Args:
        results: lista de dicts retornados por eval_d1_scenario

    Returns:
        dict com 'd1_mean', 'd1_decision_error_rate', 'd1_phantom_rate'
    """
    n = len(results)
    if n == 0:
        return {"d1_mean": None, "d1_decision_error_rate": None, "d1_phantom_rate": None, "n": 0}

    decision_errors = sum(1 for r in results if r.get("decision_error", False))
    phantom_rate = sum(1 for r in results if r.get("has_phantom_citation", False))
    d1_total = sum(r.get("d1_binary", 0) for r in results)

    return {
        "d1_mean": d1_total / n,
        "d1_decision_error_rate": decision_errors / n,
        "d1_phantom_rate": phantom_rate / n,
        "n": n,
        "n_errors": d1_total,
        "n_decision_errors": decision_errors,
        "n_phantom": phantom_rate,
    }


def eval_d1_from_parquet(results_path: str | Path, ground_truth_path: str | Path) -> list[dict]:
    """Carrega resultados e avalia D1 para todos os cenários."""
    import pandas as pd

    df = pd.read_parquet(results_path)
    with open(ground_truth_path, encoding="utf-8") as f:
        gt_data = json.load(f)

    rows = []
    for _, row in df.iterrows():
        scenario_id = row.get("scenario_id", "")
        gt = gt_data.get("by_scenario", {}).get(scenario_id, {})
        response = row.get("response_text", "")

        if not response or not gt:
            continue

        d1 = eval_d1_scenario(response, gt)
        rows.append({
            "job_sha256": row.get("sha256", ""),
            "scenario_id": scenario_id,
            "arm": row.get("arm", ""),
            "model": row.get("model", ""),
            "run_id": row.get("run_id", 0),
            **d1,
        })

    return rows
