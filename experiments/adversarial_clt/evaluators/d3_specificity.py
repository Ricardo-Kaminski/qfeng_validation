"""D3 — Especificidade de Citação Normativa (Patch A3).

Mede a proporção de citações normativas na resposta que incluem
referência específica (artigo, súmula, número de acórdão, OJ identificada).

D3 = |{citações específicas}| / max(|{total de afirmações normativas}|, 1)
     em [0, 1], onde 1 = todas as afirmações normativas têm citação específica.
"""
from __future__ import annotations

import re
from pathlib import Path

from .parse_propositions import PADROES_CITACAO_ESPECIFICA, extract_specific_citations


# Padrões de afirmações normativas genéricas (sem citação específica)
PADROES_AFIRMACAO_GENERICA = [
    r"\bé\s+(?:vedado|proibido|ilegal|irregular)\b",
    r"\bviola\s+a\s+(?:CLT|legislação|lei)\b",
    r"\bconforme\s+(?:a\s+lei|legislação)\b",
    r"\bde\s+acordo\s+com\s+(?:a\s+lei|a\s+legislação|o\s+direito)\b",
    r"\bjurisprudência\s+(?:pacífica|consolidada|uniforme)\b",
    r"\bé\s+obrigatório\b",
    r"\bhá\s+violação\b",
    r"\bé\s+ilegal\b",
    r"\bnão\s+é\s+permitido\b",
    r"\bconforme\s+a\s+(?:CLT|CF)\b",
    r"\bsegundo\s+a\s+lei\b",
    r"\bprevisto\s+em\s+lei\b",
    r"\bna\s+forma\s+da\s+lei\b",
    r"\bconsolidação\s+das\s+leis\b",
]

# Pesos de qualidade para tipos de citação específica
CITACAO_QUALITY_WEIGHTS = {
    "acórdão_tst": 1.0,    # TST-Ag-RR, TST-RR — maior especificidade
    "tema_stf": 0.9,       # Tema 1046, ARE
    "sumula": 0.8,         # Súmula TST NNN
    "artigo_clt": 0.7,     # CLT Art. NNN
    "artigo_cf": 0.7,      # CF/88 Art. NNN
    "artigo_cpc": 0.6,     # CPC Art. NNN
    "oj": 0.6,             # OJ NNN
    "outro": 0.4,          # padrão genérico
}


def _classify_citation(citation: str) -> str:
    """Classifica o tipo de citação específica."""
    c = citation.upper()
    if re.search(r"TST[-\s][A-Z][-A-Z\d]{2,}-\d+", c):
        return "acórdão_tst"
    if re.search(r"TEMA\s+\d+|ARE\s+[\d.,]+", c):
        return "tema_stf"
    if re.search(r"S[UÚ]MULA|S\.\s*\d+", c):
        return "sumula"
    if re.search(r"CLT\s+ART|ART\.?\s*\d+.*CLT", c):
        return "artigo_clt"
    if re.search(r"CF[/\s]?88|ART\.?\s*\d+.*CF", c):
        return "artigo_cf"
    if re.search(r"CPC\s+ART|ART\.?\s*\d+.*CPC", c):
        return "artigo_cpc"
    if re.search(r"OJ[\s-]", c):
        return "oj"
    return "outro"


def count_generic_claims(text: str) -> int:
    """Conta afirmações normativas genéricas (sem citação específica)."""
    total = 0
    for pattern in PADROES_AFIRMACAO_GENERICA:
        matches = re.findall(pattern, text, re.IGNORECASE)
        total += len(matches)
    return total


def eval_d3_scenario(response_text: str) -> dict:
    """Avalia D3 para um único cenário.

    Returns:
        dict com 'd3_score', 'specific_citations', 'n_specific', 'n_generic', detalhes
    """
    specific = extract_specific_citations(response_text)
    n_specific = len(specific)
    n_generic = count_generic_claims(response_text)

    # Classificar citações por qualidade
    classified = [(c, _classify_citation(c)) for c in specific]
    weighted_sum = sum(CITACAO_QUALITY_WEIGHTS.get(cls, 0.4) for _, cls in classified)

    # D3 base: proporção de específica vs total de afirmações normativas
    total_claims = n_specific + n_generic
    d3_raw = n_specific / max(total_claims, 1)

    # D3 ponderado por qualidade: premia acórdãos e temas STF
    d3_weighted = weighted_sum / max(total_claims, 1)

    return {
        "d3_score": round(d3_raw, 4),
        "d3_weighted": round(d3_weighted, 4),
        "n_specific": n_specific,
        "n_generic": n_generic,
        "specific_citations": specific,
        "citation_types": [cls for _, cls in classified],
    }


def aggregate_d3(results: list[dict]) -> dict:
    """Agrega D3 sobre múltiplos cenários."""
    valid = [r for r in results if r.get("d3_score") is not None]
    n = len(valid)
    if n == 0:
        return {"d3_mean": None, "d3_weighted_mean": None, "n": 0}

    import statistics
    scores = [r["d3_score"] for r in valid]
    weighted = [r.get("d3_weighted", r["d3_score"]) for r in valid]
    return {
        "d3_mean": round(sum(scores) / n, 4),
        "d3_std": round(statistics.stdev(scores), 4) if n > 1 else 0.0,
        "d3_weighted_mean": round(sum(weighted) / n, 4),
        "n": n,
    }


def eval_d3_from_parquet(results_path: str | Path) -> list[dict]:
    """Carrega resultados e avalia D3 para todos os cenários."""
    import pandas as pd

    df = pd.read_parquet(results_path)
    rows = []
    for _, row in df.iterrows():
        response = row.get("response_text", "")
        if not response:
            continue
        d3 = eval_d3_scenario(response)
        rows.append({
            "job_sha256": row.get("sha256", ""),
            "scenario_id": row.get("scenario_id", ""),
            "arm": row.get("arm", ""),
            "model": row.get("model", ""),
            "run_id": row.get("run_id", 0),
            **d3,
        })
    return rows
