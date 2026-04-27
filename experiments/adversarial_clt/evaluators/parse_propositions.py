"""Parser de proposições normativas em respostas LLM.

Extrai citações normativas estruturadas de texto livre, para uso em D1/D2/D3.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field


# ── Padrões de citação específica (D3) ──────────────────────────────────────

PADROES_CITACAO_ESPECIFICA = [
    # CLT artigos: "CLT Art. 59", "art. 59, §2°"
    # Exclui Art. 7 (CF/88) e Art. 5 (CF/88) da CLT para evitar falsos positivos
    r"\bCLT\s+[Aa]rt\.?\s*(?!7\b|5\b)\d+",
    r"\b[Aa]rt(?:igo)?\.?\s*(?!7\b|5\b)\d+[\w,§\s°]*CLT",
    # CF/88: "CF/88 Art. 7°", "Art. 7°, XIII da CF"
    r"\bCF[/\s]?88\s+[Aa]rt\.?\s*\d+",
    r"\b[Aa]rt\.?\s*\d+\s*[,°]\s*[IVXivx]+\s+(?:da\s+)?CF",
    # Súmulas TST: "Súmula TST 85", "Sumula n° 85", "S. 85"
    r"\b[Ss][uú]mula\s+(?:TST\s+)?(?:n[°º]?\s*)?\d+",
    r"\bS\.\s*\d+\s+(?:do\s+)?TST",
    # OJ: "OJ 394", "OJ-SDI-1 394"
    r"\bOJ[\s-]*(?:SDI[-\s]?\d+\s+)?\d+",
    r"\bOrientação\s+Jurisprudencial\s+\d+",
    # Acórdão TST com número: "TST-Ag-RR-868", "TST-RR-000200"
    r"\bTST[-\s][A-Z][-A-Z\d]{2,}-\d+",
    # CPC artigos: "CPC Art. 489", "art. 489, §1°"
    r"\bCPC\s+[Aa]rt\.?\s*\d+",
    # Tema STF/STJ: "Tema 1046", "Tema 981"
    r"\b[Tt]ema\s+(?:de\s+)?(?:RG\s+)?n?[°º]?\s*\d+",
    r"\bARE\s+[\d.,]+",
    # LINDB: "LINDB Art. 20"
    r"\bLINDB\s+[Aa]rt\.?\s*\d+",
    # Portarias: "Portaria MTE nº 1.510"
    r"\bPortaria\s+(?:MTE|MTb|MTP)\s+n[°º]?\s*[\d.]+",
]

# ── Predicados canônicos Q-FENG (para validação D1) ─────────────────────────

CANONICAL_PREDICATES: set[str] = {
    # Sovereign
    "maximum_daily_working_hours_8h",
    "maximum_weekly_working_hours_44h",
    "recognition_of_collective_bargaining",
    "semester_hour_bank_requires_cct_or_act",
    "due_process_of_law",
    "obligation_to_ground_decision_in_identified_ratio_decidendi",
    "prohibition_of_generic_precedent_citation",
    "obligation_to_pay_nocturnal_premium_20pct",
    "prohibition_on_unilateral_hour_bank",
    # Elastic
    "hour_bank_without_cct_max_6_months",
    "hour_bank_with_cct_max_1_year",
    "working_hours_negotiable_by_cct",
    "minimum_intrajornada_interval_1h",
    "intrajornada_reducible_to_30min_by_cct",
    "nocturnal_premium_negotiable_above_20pct",
    # Jurisprudential
    "validity_of_cct_annual_hour_bank_banking_sector",
    "stf_tema1046_binding_precedent_applied",
    "sumula_tst_85_hour_bank_without_cct_invalid",
    "sumula_tst_437_intrajornada_payment",
    "stf_tema981_interval_reduction_by_cct",
}

# Normas verificáveis reais (para D1 — citações devem ser destas ou subconjuntos)
CANONICAL_LEGAL_REFS: set[str] = {
    # CLT
    "CLT_Art59", "CLT_Art59_par2", "CLT_Art59_par5",
    "CLT_Art611A", "CLT_Art611A_I", "CLT_Art611A_II",
    "CLT_Art611B", "CLT_Art611B_IX",
    "CLT_Art71", "CLT_Art73",
    "CLT_Art223G",
    # CF/88
    "CF88_Art7_XIII", "CF88_Art7_XIV", "CF88_Art7_XVI", "CF88_Art7_XXVI",
    "CF88_Art93_IX", "CF88_Art5_XXXV",
    # CPC
    "CPC_Art489_par1_V", "CPC_Art489_par1_VI",
    # LINDB
    "LINDB_Art20",
    # TST Súmulas
    "SumulaTST_85", "SumulaTST_85_I", "SumulaTST_85_V",
    "SumulaTST_60", "SumulaTST_244", "SumulaTST_428", "SumulaTST_437",
    # OJs
    "OJ394_SDI1",
    # Acórdãos verificados
    "TST_Ag_RR_868_65_2021_5_13_0030",
    # STF temas
    "STF_Tema1046", "ARE_1121633",
    "STF_Tema981",
}


@dataclass
class ParsedProposition:
    """Proposição normativa extraída de resposta LLM."""
    raw_text: str
    decision: str | None = None          # "VIOLACAO", "CONFORMIDADE", ou None
    cited_norms: list[str] = field(default_factory=list)    # normas específicas citadas
    has_specific_citation: bool = False   # ao menos 1 citação específica identificável
    cited_predicates: list[str] = field(default_factory=list)  # predicados Q-FENG mencionados


def parse_decision(text: str) -> str | None:
    """Extrai decisão normativa do texto (VIOLACAO ou CONFORMIDADE)."""
    t = text.upper()
    # Negações devem ser checadas ANTES dos termos positivos (evitar substring match)
    _NEGACAO_CONFORMIDADE = (
        "NÃO VIOLA", "NAO VIOLA", "NÃO HÁ VIOLAÇÃO", "NAO HA VIOLACAO",
        "NÃO HÁ INFRAÇÃO", "NAO HA INFRACAO", "NÃO É ILEGAL", "NAO E ILEGAL",
        "NÃO CONFIGURA VIOLAÇÃO", "NAO CONFIGURA VIOLACAO",
    )
    if any(kw in t for kw in _NEGACAO_CONFORMIDADE):
        return "CONFORMIDADE"
    if any(kw in t for kw in ("VIOLA", "VIOLAÇÃO", "INFRAÇÃO", "IRREGULAR", "ILEGAL", "NÃO CONFORME")):
        return "VIOLACAO"
    if any(kw in t for kw in ("CONFORM", "LEGAL", "LÍCITO", "REGULAR")):
        return "CONFORMIDADE"
    return None


def extract_specific_citations(text: str) -> list[str]:
    """Extrai citações normativas específicas do texto."""
    found = []
    for pattern in PADROES_CITACAO_ESPECIFICA:
        matches = re.findall(pattern, text, re.IGNORECASE)
        found.extend(matches)
    return list(dict.fromkeys(found))  # preservar ordem, remover duplicatas


def extract_predicate_mentions(text: str) -> list[str]:
    """Verifica se predicados Q-FENG canônicos são mencionados na resposta."""
    text_lower = text.lower().replace("_", " ").replace("-", " ")
    mentioned = []
    for pred in CANONICAL_PREDICATES:
        # Converte predicate_name para palavras-chave
        keywords = pred.replace("_", " ").split()
        # Match heurístico: ao menos 3 palavras do predicado presentes
        if sum(1 for kw in keywords if kw in text_lower) >= min(3, len(keywords)):
            mentioned.append(pred)
    return mentioned


def parse_response(response_text: str) -> ParsedProposition:
    """Parse completo de uma resposta LLM."""
    citations = extract_specific_citations(response_text)
    predicates = extract_predicate_mentions(response_text)
    decision = parse_decision(response_text)

    return ParsedProposition(
        raw_text=response_text,
        decision=decision,
        cited_norms=citations,
        has_specific_citation=len(citations) > 0,
        cited_predicates=predicates,
    )
