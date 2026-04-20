"""Hierarchical chunking of normative text into NormChunk objects.

Splits raw extracted text by article → section → subsection using
regime-specific regex patterns from the registry. Also provides
shared utilities for chunk_type detection and cross-reference extraction.
"""

from __future__ import annotations

import hashlib
import re

from qfeng.c1_digestion.ingestion.registry import REGIME_CONFIGS, RegimeConfig
from qfeng.core.schemas import NormativeRegime, NormChunk


def chunk_by_hierarchy(
    raw_text: str,
    regime: NormativeRegime,
    source: str,
) -> list[NormChunk]:
    """Divide texto normativo bruto em NormChunks hierárquicos.

    Aplica regex patterns do regime para segmentar por artigo,
    parágrafo/seção e inciso/alínea.

    Args:
        raw_text: Texto normativo extraído (sem HTML).
        regime: Regime normativo do documento.
        source: Nome-fonte do documento (e.g. ``Lei 8.080/1990``).

    Returns:
        Lista de NormChunks, um por proposição normativa.
    """
    config = REGIME_CONFIGS[regime]
    chunks: list[NormChunk] = []

    # Nível 1: artigos
    articles = _split_by_pattern(raw_text, config.article_pattern, "Art.")

    if not articles:
        # Sem artigos — tentar seções como nível primário
        sections = _split_by_pattern(raw_text, config.section_pattern, "")
        if sections:
            for sec_label, sec_text in sections:
                _chunk_with_subsections(
                    sec_text, [sec_label], source, regime, config, chunks
                )
        else:
            # Sem estrutura — bloco único
            text = raw_text.strip()
            if text:
                chunks.append(
                    _make_chunk(text, ["Texto Integral"], source, regime, config)
                )
        return chunks

    for art_label, art_text in articles:
        # Nível 2: seções (§, Parágrafo único)
        sections = _split_by_pattern(art_text, config.section_pattern, "")
        if not sections:
            # Artigo sem § — tentar subdivisões diretamente (incisos)
            _chunk_with_subsections(
                art_text, [art_label], source, regime, config, chunks
            )
            continue

        for sec_label, sec_text in sections:
            hierarchy = [art_label]
            if sec_label:
                hierarchy.append(sec_label)
            _chunk_with_subsections(
                sec_text, hierarchy, source, regime, config, chunks
            )

    return chunks


def detect_chunk_type(text: str, config: RegimeConfig) -> str:
    """Classifica o tipo de um chunk normativo por keyword scoring.

    Busca palavras-chave no texto e retorna o tipo com maior
    pontuação. Em caso de empate, prioriza: obligation > definition >
    principle > procedure > sanction.

    Args:
        text: Texto do chunk.
        config: Configuração do regime.

    Returns:
        Tipo do chunk: ``principle``, ``obligation``, ``definition``,
        ``procedure`` ou ``sanction``.
    """
    text_lower = text.lower()
    priority = ["obligation", "definition", "principle", "procedure", "sanction"]

    best_type = "obligation"
    best_score = 0

    for chunk_type in priority:
        keywords = config.chunk_type_keywords.get(chunk_type, [])
        score = sum(1 for kw in keywords if kw.lower() in text_lower)
        if score > best_score:
            best_score = score
            best_type = chunk_type

    return best_type


def extract_cross_references(text: str, config: RegimeConfig) -> list[str]:
    """Extrai referências cruzadas do texto normativo.

    Usa o ``reference_pattern`` do regime para encontrar menções
    a outros artigos, seções ou normas.

    Args:
        text: Texto do chunk.
        config: Configuração do regime.

    Returns:
        Lista de referências encontradas (e.g. ``["art. 196", "art. 2"]``).
    """
    matches = config.reference_pattern.findall(text)
    # Deduplica preservando ordem
    # findall pode retornar strings ou tuples (múltiplos grupos de captura)
    seen: set[str] = set()
    refs: list[str] = []
    for m in matches:
        if isinstance(m, tuple):
            # Múltiplos grupos — pegar o primeiro não-vazio
            ref = next((g.strip() for g in m if g.strip()), "")
        else:
            ref = m.strip()
        if ref and ref not in seen:
            seen.add(ref)
            refs.append(ref)
    return refs


def generate_chunk_id(source: str, hierarchy: list[str], text: str = "") -> str:
    """Gera ID determinístico para um chunk.

    Args:
        source: Nome-fonte do documento.
        hierarchy: Caminho hierárquico do chunk.

    Returns:
        Hash SHA-256 truncado em 16 caracteres.
    """
    hierarchy_path = ":".join(hierarchy)
    text_snippet = text[:200].strip() if text else ""
    raw = f"{source}:{hierarchy_path}:{text_snippet}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


# ── Funções internas ──────────────────────────────────────────────────


def _chunk_with_subsections(
    text: str,
    hierarchy: list[str],
    source: str,
    regime: NormativeRegime,
    config: RegimeConfig,
    chunks: list[NormChunk],
) -> None:
    """Tenta dividir texto em subdivisões; se não houver, cria chunk único."""
    subsections = _split_subsections(text, config)
    if subsections:
        for sub_label, sub_text in subsections:
            sub_text = sub_text.strip()
            if sub_text:
                chunks.append(
                    _make_chunk(
                        sub_text, [*hierarchy, sub_label], source, regime, config
                    )
                )
    else:
        text = text.strip()
        if text:
            chunks.append(_make_chunk(text, hierarchy, source, regime, config))


def _make_chunk(
    text: str,
    hierarchy: list[str],
    source: str,
    regime: NormativeRegime,
    config: RegimeConfig,
) -> NormChunk:
    """Constrói um NormChunk com metadados derivados."""
    return NormChunk(
        id=generate_chunk_id(source, hierarchy, text),
        source=source,
        regime=regime,
        hierarchy=hierarchy,
        text=text,
        language=config.language,
        cross_references=extract_cross_references(text, config),
        chunk_type=detect_chunk_type(text, config),
    )


def _split_by_pattern(
    text: str,
    pattern: re.Pattern[str],
    prefix: str,
) -> list[tuple[str, str]]:
    """Divide texto usando um regex, retornando pares (label, conteúdo).

    O label é construído a partir do grupo capturado pelo regex,
    prefixado com ``prefix`` (e.g. ``"Art."``).

    Args:
        text: Texto a dividir.
        pattern: Regex com pelo menos um grupo de captura.
        prefix: Prefixo para o label (e.g. ``"Art."``).

    Returns:
        Lista de ``(label, conteúdo)`` para cada seção encontrada.
    """
    splits: list[tuple[str, str]] = []
    matches = list(pattern.finditer(text))
    if not matches:
        return splits

    for i, m in enumerate(matches):
        label_num = m.group(1) if m.lastindex and m.lastindex >= 1 else m.group(0)
        label = f"{prefix} {label_num}".strip() if prefix else label_num.strip()

        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()

        if content:
            splits.append((label, content))

    return splits


def _split_subsections(
    text: str,
    config: RegimeConfig,
) -> list[tuple[str, str]]:
    """Tenta dividir texto em subdivisões usando os patterns do regime.

    Aplica cada nível de ``subsection_patterns`` em ordem. Retorna
    os resultados do primeiro nível que produzir splits.

    Args:
        text: Texto a subdividir.
        config: Configuração do regime.

    Returns:
        Lista de ``(label, conteúdo)`` ou lista vazia se não houver subdivisões.
    """
    for pattern in config.subsection_patterns:
        splits = _split_by_pattern(text, pattern, "")
        if splits:
            return splits
    return []
