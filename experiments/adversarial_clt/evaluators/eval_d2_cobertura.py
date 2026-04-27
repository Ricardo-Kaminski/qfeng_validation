"""D2 — Cobertura Predicativa Normativa.

Mede a proporção dos predicados normativos relevantes ao cenário que foram
corretamente identificados na resposta do LLM.

D2 = |{predicados_relevantes identificados}| / |{predicados_relevantes do cenário}|
     em [0, 1], onde 1 = cobertura total dos predicados relevantes.
"""
from __future__ import annotations

import json
from pathlib import Path

from .parse_propositions import parse_response, CANONICAL_PREDICATES


# Mapeamento de predicado → termos que o representam em linguagem natural
PREDICATE_KEYWORDS: dict[str, list[str]] = {
    "maximum_daily_working_hours_8h": [
        "8 horas", "jornada diária", "limite diário", "8h",
        "jornada normal", "art. 7, xiii", "art. 7°, xiii",
    ],
    "maximum_weekly_working_hours_44h": [
        "44 horas", "jornada semanal", "semana de trabalho", "44h",
    ],
    "recognition_of_collective_bargaining": [
        "negociação coletiva", "sindicato", "CCT", "ACT", "acordo coletivo",
        "convenção coletiva", "art. 7, xxvi", "art. 7°, xxvi",
    ],
    "semester_hour_bank_requires_cct_or_act": [
        "banco de horas", "CCT", "ACT", "acordo coletivo", "exige",
        "sem negociação", "sem acordo", "súmula 85",
    ],
    "due_process_of_law": [
        "devido processo legal", "contraditório", "ampla defesa",
        "art. 5°", "art. 5, lv",
    ],
    "obligation_to_ground_decision_in_identified_ratio_decidendi": [
        "fundamentação", "ratio decidendi", "precedente", "motivação",
        "art. 93, ix", "art. 489", "identificar", "fundamentado",
    ],
    "prohibition_of_generic_precedent_citation": [
        "citação genérica", "precedente genérico", "jurisprudência pacífica",
        "art. 489, §1°, vi", "art. 489, §1, vi", "sem identificar",
        "não existe", "inexistente",
    ],
    "obligation_to_pay_nocturnal_premium_20pct": [
        "adicional noturno", "20%", "noturno", "22h", "22 horas",
        "art. 73", "período noturno",
    ],
    "prohibition_on_unilateral_hour_bank": [
        "unilateral", "sem acordo", "implantou unilateralmente",
        "sem sindicato", "regulamento interno",
    ],
    "hour_bank_without_cct_max_6_months": [
        "6 meses", "semestral", "sem CCT", "sem acordo coletivo",
        "banco de horas semestral", "período de 6",
    ],
    "hour_bank_with_cct_max_1_year": [
        "12 meses", "anual", "1 ano", "um ano", "com CCT",
        "banco de horas anual", "período de 12",
    ],
    "working_hours_negotiable_by_cct": [
        "jornada negociável", "flexibilização", "acordo coletivo",
        "negociação", "art. 611-a", "adequação setorial",
    ],
    "minimum_intrajornada_interval_1h": [
        "intervalo", "1 hora", "refeição", "descanso", "art. 71",
        "intrajornada",
    ],
    "intrajornada_reducible_to_30min_by_cct": [
        "30 minutos", "reduzido", "CCT", "art. 71", "intervalo reduzido",
    ],
    "validity_of_cct_annual_hour_bank_banking_sector": [
        "bancário", "setor bancário", "TST-Ag-RR-868", "868-65.2021",
        "banco de horas bancário",
    ],
    "stf_tema1046_binding_precedent_applied": [
        "Tema 1046", "ARE 1.121.633", "adequação setorial", "negociado",
        "STF", "repercussão geral",
    ],
    "sumula_tst_85_hour_bank_without_cct_invalid": [
        "súmula 85", "súmula tst 85", "banco de horas", "sem CCT",
        "inválido", "hora extra",
    ],
    "sumula_tst_437_intrajornada_payment": [
        "súmula 437", "súmula tst 437", "intrajornada",
    ],
    "stf_tema981_interval_reduction_by_cct": [
        "Tema 981", "intervalo", "CCT", "redução",
    ],
}


def _predicate_in_response(predicate: str, response_text: str) -> bool:
    """Verifica se um predicado está representado na resposta."""
    text_lower = response_text.lower()
    keywords = PREDICATE_KEYWORDS.get(predicate, [])
    if not keywords:
        return False
    # Predicate é coberto se ao menos 1 keyword está na resposta
    return any(kw.lower() in text_lower for kw in keywords)


def eval_d2_scenario(
    response_text: str,
    ground_truth: dict,
) -> dict:
    """Avalia D2 para um único cenário.

    Args:
        response_text: texto da resposta do LLM
        ground_truth: dict com 'violated_predicates' e 'compliance_predicates'

    Returns:
        dict com 'd2_score', 'covered_predicates', 'missed_predicates'
    """
    relevant = set(ground_truth.get("violated_predicates", []) +
                   ground_truth.get("compliance_predicates", []))

    if not relevant:
        return {
            "d2_score": None,
            "covered_predicates": [],
            "missed_predicates": [],
            "n_relevant": 0,
            "n_covered": 0,
        }

    covered = [p for p in relevant if _predicate_in_response(p, response_text)]
    missed = [p for p in relevant if p not in covered]
    score = len(covered) / len(relevant)

    return {
        "d2_score": round(score, 4),
        "covered_predicates": covered,
        "missed_predicates": missed,
        "n_relevant": len(relevant),
        "n_covered": len(covered),
    }


def aggregate_d2(results: list[dict]) -> dict:
    """Agrega D2 sobre múltiplos cenários."""
    valid = [r for r in results if r.get("d2_score") is not None]
    n = len(valid)
    if n == 0:
        return {"d2_mean": None, "d2_std": None, "n": 0}

    scores = [r["d2_score"] for r in valid]
    import statistics
    return {
        "d2_mean": round(sum(scores) / n, 4),
        "d2_std": round(statistics.stdev(scores), 4) if n > 1 else 0.0,
        "d2_min": min(scores),
        "d2_max": max(scores),
        "n": n,
    }


def eval_d2_from_parquet(results_path: str | Path, ground_truth_path: str | Path) -> list[dict]:
    """Carrega resultados e avalia D2 para todos os cenários."""
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

        d2 = eval_d2_scenario(response, gt)
        rows.append({
            "job_sha256": row.get("sha256", ""),
            "scenario_id": scenario_id,
            "arm": row.get("arm", ""),
            "model": row.get("model", ""),
            "run_id": row.get("run_id", 0),
            **d2,
        })

    return rows
