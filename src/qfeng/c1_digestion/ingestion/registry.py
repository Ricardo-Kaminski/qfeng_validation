"""Regime-specific parsing configurations for E1 ingestion.

Each ``RegimeConfig`` bundles regex patterns, keyword lists,
and helper functions tailored to one normative regime's document format.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable

from qfeng.core.schemas import NormativeRegime


@dataclass(frozen=True)
class RegimeConfig:
    """Configuração de parsing para um regime normativo."""

    name: NormativeRegime
    language: str

    # Regex patterns — compilados
    article_pattern: re.Pattern[str]
    section_pattern: re.Pattern[str]
    subsection_patterns: list[re.Pattern[str]]
    reference_pattern: re.Pattern[str]

    # Derivação do nome-fonte a partir do filename
    source_from_filename: Callable[[str], str]

    # Palavras-chave para classificação de chunk_type
    chunk_type_keywords: dict[str, list[str]]

    # Seletores CSS para remoção do DOM
    strip_selectors: list[str] = field(default_factory=list)

    # Sinais de concorrência normativa (domínio regulatório)
    concurrency_signals: list[str] = field(default_factory=list)


def _source_brasil(filename: str) -> str:
    """Deriva nome-fonte para documentos brasileiros.

    Exemplos:
        ``lei_8080_1990`` → ``Lei 8.080/1990``
        ``CF88_completa``  → ``CF/88``
        ``portaria_1631_2015`` → ``Portaria 1.631/2015``
    """
    stem = filename.rsplit(".", maxsplit=1)[0] if "." in filename else filename

    if stem.startswith("CF88"):
        return "CF/88"
    if stem.startswith("lei_13709"):
        return "Lei 13.709/2018 (LGPD)"
    if stem.startswith("lei_13979"):
        return "Lei 13.979/2020"
    if stem.startswith("l14802"):
        return "Lei 14.802"
    if stem.startswith("pns_"):
        return "PNS 2024-2027"
    if stem.startswith("ppa_"):
        return "PPA 2024-2027"
    if stem.startswith("pl_2338"):
        return "PL 2338/2023"

    # Portarias
    if stem.startswith("portaria_consolidacao_2"):
        return "Portaria de Consolidação 2/2017"
    if stem.startswith("portaria_consolidacao_5"):
        return "Portaria de Consolidação 5/2017"
    if stem.startswith("portaria_188"):
        return "Portaria 188/2020"
    if stem.startswith("portaria_356"):
        return "Portaria 356/2020"
    if stem.startswith("portaria_454"):
        return "Portaria 454/2020"
    if stem.startswith("portaria_913"):
        return "Portaria 913/2022"
    if stem.startswith("portaria_1631"):
        return "Portaria 1.631/2015"

    # Leis genéricas: lei_NNNN_AAAA → Lei N.NNN/AAAA
    m = re.match(r"lei_(\d+)_(\d{4})", stem)
    if m:
        num = m.group(1)
        year = m.group(2)
        if len(num) >= 4:
            formatted = f"{num[:-3]}.{num[-3:]}"
        else:
            formatted = num
        return f"Lei {formatted}/{year}"

    return stem


def _source_usa(filename: str) -> str:
    """Deriva nome-fonte para documentos norte-americanos.

    Exemplos:
        ``ssa_title_xix_1902`` → ``SSA Title XIX §1902``
        ``42_cfr_part_435``    → ``42 CFR Part 435``
        ``14th_amendment``     → ``14th Amendment``
    """
    stem = filename.rsplit(".", maxsplit=1)[0] if "." in filename else filename

    m = re.match(r"ssa_title_xix_(\d+)", stem)
    if m:
        return f"SSA Title XIX §{m.group(1)}"

    m = re.match(r"42_cfr_part_(\d+)", stem)
    if m:
        return f"42 CFR Part {m.group(1)}"

    if "14th_amendment" in stem:
        return "14th Amendment"
    if "civil_rights" in stem:
        return "Civil Rights Act Title VI"

    return stem


def _source_eu(filename: str) -> str:
    """Deriva nome-fonte para documentos europeus.

    Exemplos:
        ``eu_ai_act_2024_1689``             → ``EU AI Act 2024/1689``
        ``gdpr_full``                       → ``GDPR``
        ``carta_direitos_fundamentais_ue``  → ``Carta de Direitos Fundamentais UE``
        ``pl_2338_2023``                    → ``PL 2338/2023``
    """
    stem = filename.rsplit(".", maxsplit=1)[0] if "." in filename else filename

    if "eu_ai_act" in stem:
        return "EU AI Act 2024/1689"
    if "gdpr" in stem:
        return "GDPR"
    if "carta_direitos" in stem:
        return "Carta de Direitos Fundamentais UE"
    if stem.startswith("pl_"):
        m = re.match(r"pl_(\d+)_(\d{4})", stem)
        if m:
            return f"PL {m.group(1)}/{m.group(2)}"

    return stem


# ── Configurações por regime ──────────────────────────────────────────

_BRASIL_CONFIG = RegimeConfig(
    name=NormativeRegime.BRASIL,
    language="pt-BR",
    article_pattern=re.compile(
        r"Art\.\s*(\d+)[°ºªo]?(?:-[A-Z])?\s*",
    ),
    section_pattern=re.compile(
        r"(§\s*\d+[°ºªo]?|Parágrafo\s+único)\.?\s*",
    ),
    subsection_patterns=[
        re.compile(r"^([IVXLCDM]+)\s*[-–—]\s*", re.MULTILINE),  # incisos
        re.compile(r"^([a-z])\)\s*", re.MULTILINE),               # alíneas
    ],
    reference_pattern=re.compile(
        r"(?:"
        r"(?:nos termos|conforme|de que trata|na forma|previsto|estabelecido)"
        r"[^.]{0,30}"  # até 30 chars antes do art.
        r"(?:art|Art)\.\s*(\d+[°ºªo]?)"
        r"|"
        r"(?:art|Art)\.\s*(\d+[°ºªo]?)\s*(?:desta|dessa|da|do)"
        r"|"
        r"inciso\s+([IVXLCDM]+)\s*(?:d[oa]|desta)"
        r")",
        re.IGNORECASE,
    ),
    source_from_filename=_source_brasil,
    chunk_type_keywords={
        "obligation": [
            "deve", "deverá", "obrigação", "assegurar", "garantir",
            "compete", "incumbe", "é obrigatório", "ficam obrigados",
        ],
        "definition": [
            "entende-se", "considera-se", "compreende", "abrange",
            "para efeito", "para fins", "denomina-se",
        ],
        "principle": [
            "direito", "princípio", "fundamento", "diretriz",
            "objetivo", "finalidade",
        ],
        "procedure": [
            "procedimento", "processo", "etapa", "fase",
            "tramitação", "prazo",
        ],
        "sanction": [
            "penalidade", "sanção", "infração", "multa",
            "suspensão", "cassação",
        ],
    },
    strip_selectors=["script", "style", "img", "nav", "footer", "strike"],
    concurrency_signals=[
        "saúde", "SUS", "assistência", "vigilância", "atenção básica",
        "urgência", "emergência", "leito", "UTI", "medicamento",
    ],
)

_USA_CONFIG = RegimeConfig(
    name=NormativeRegime.USA,
    language="en",
    article_pattern=re.compile(
        r"§\s*(\d+[a-z]?)",
    ),
    section_pattern=re.compile(
        r"\(([a-z])\)\s*",
    ),
    subsection_patterns=[
        re.compile(r"\((\d+)\)"),          # (1), (2)
        re.compile(r"\(([A-Z])\)"),         # (A), (B)
        re.compile(r"\(([ivxlc]+)\)"),      # (i), (ii)
    ],
    reference_pattern=re.compile(
        r"(?:section|Section|§)\s*(\d+[a-z]?(?:\([a-z0-9]+\))*)",
    ),
    source_from_filename=_source_usa,
    chunk_type_keywords={
        "obligation": [
            "shall", "must", "required to", "provide that",
            "shall be required", "shall provide",
        ],
        "definition": [
            "means", "the term", "as used in", "refers to",
            "as defined in",
        ],
        "principle": [
            "purpose", "policy", "finding", "declaration",
        ],
        "procedure": [
            "procedure", "process", "application", "determination",
            "hearing", "review",
        ],
        "sanction": [
            "penalty", "liable", "violation", "forfeiture",
            "fine", "civil money penalty",
        ],
    },
    strip_selectors=[
        "script", "style", "nav", ".modal", "#breadcrumb", "footer",
        ".navbar", "#sidebar",
    ],
    concurrency_signals=[
        "medical assistance", "eligibility", "coverage", "benefit",
        "provider", "managed care", "enrollment",
    ],
)

_EU_CONFIG = RegimeConfig(
    name=NormativeRegime.EU,
    language="en",
    article_pattern=re.compile(
        r"Article\s+(\d+)",
    ),
    section_pattern=re.compile(
        r"^(\d+)\.\s{2,}",
        re.MULTILINE,
    ),
    subsection_patterns=[
        re.compile(r"\(([a-z])\)"),  # (a), (b)
    ],
    reference_pattern=re.compile(
        r"(?:Article|paragraph|Regulation)\s+(\d+(?:\(\d+\))?)",
    ),
    source_from_filename=_source_eu,
    chunk_type_keywords={
        "obligation": [
            "shall", "shall ensure", "shall be designed",
            "shall provide", "shall establish",
        ],
        "definition": [
            "means", "shall mean", "for the purposes",
            "is defined as",
        ],
        "principle": [
            "purpose", "objective", "principle", "right",
            "dignity", "fundamental",
        ],
        "procedure": [
            "procedure", "assessment", "registration",
            "notification", "conformity",
        ],
        "sanction": [
            "penalty", "fine", "infringement", "administrative",
            "sanction",
        ],
    },
    strip_selectors=["script", "style", ".oj-separator"],
    concurrency_signals=[
        "artificial intelligence", "AI system", "high-risk",
        "deployer", "provider", "transparency", "human oversight",
    ],
)

REGIME_CONFIGS: dict[NormativeRegime, RegimeConfig] = {
    NormativeRegime.BRASIL: _BRASIL_CONFIG,
    NormativeRegime.USA: _USA_CONFIG,
    NormativeRegime.EU: _EU_CONFIG,
}
