"""E1 document parser — extracts NormChunks from HTML/PDF normative documents.

Uses DOM-based parsing (BeautifulSoup) for HTML with regime-specific
strategies, and PyMuPDF for PDF. Falls back to text-based chunking
when DOM structure is insufficient.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

import warnings

import fitz  # PyMuPDF
from bs4 import BeautifulSoup, NavigableString, Tag, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

from qfeng.c1_digestion.ingestion.chunker import (
    chunk_by_hierarchy,
    detect_chunk_type,
    extract_cross_references,
    generate_chunk_id,
)
from qfeng.c1_digestion.ingestion.registry import REGIME_CONFIGS, RegimeConfig
from qfeng.core.schemas import NormChunk, NormativeRegime

logger = logging.getLogger(__name__)


def parse_document(path: Path, regime: NormativeRegime) -> list[NormChunk]:
    """Faz o parse de um documento normativo em NormChunks.

    Detecta o formato pelo sufixo do arquivo e delega ao parser
    apropriado (HTML, PDF ou Markdown).

    Args:
        path: Caminho para o arquivo.
        regime: Regime normativo do documento.

    Returns:
        Lista de NormChunks extraídos.

    Raises:
        ValueError: Se o formato não for suportado.
    """
    config = REGIME_CONFIGS[regime]
    suffix = path.suffix.lower()
    source = config.source_from_filename(path.name)

    if suffix in (".htm", ".html"):
        return _parse_html(path, regime, config, source)
    if suffix == ".pdf":
        return _parse_pdf(path, config, source, regime)
    if suffix == ".md":
        return _parse_markdown(path, config, source, regime)

    msg = f"Formato não suportado: {suffix} ({path.name})"
    raise ValueError(msg)


# ── HTML parsing ──────────────────────────────────────────────────────


def _read_html(path: Path) -> str:
    """Lê arquivo HTML tentando UTF-8 e fallback para latin-1."""
    import unicodedata
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.warning("Fallback para latin-1: %s", path.name)
        text = path.read_text(encoding="latin-1")
    return unicodedata.normalize("NFC", text)


def _parse_html(
    path: Path,
    regime: NormativeRegime,
    config: RegimeConfig,
    source: str,
) -> list[NormChunk]:
    """Dispatcher para parser HTML regime-específico."""
    html = _read_html(path)
    # EU docs são XHTML — usar lxml-xml evita warning
    parser = "lxml-xml" if regime == NormativeRegime.EU else "lxml"
    soup = BeautifulSoup(html, parser)

    # Strip elementos indesejados
    for selector in config.strip_selectors:
        for el in soup.select(selector):
            el.decompose()

    match regime:
        case NormativeRegime.BRASIL:
            return _parse_brasil_html(soup, config, source)
        case NormativeRegime.USA:
            return _parse_usa_html(soup, config, source)
        case NormativeRegime.EU:
            return _parse_eu_html(soup, config, source)


def _clean_text(text: str) -> str:
    """Normaliza espaços e remove quebras desnecessárias."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ── Brasil HTML Parser ────────────────────────────────────────────────


_BRASIL_ANCHOR_RE = re.compile(
    r"^art(\d+[a-zA-Z]?)"       # art7, art6a, art6A
    r"(?:§(\d+)|([piIVXLCDM]+))?$"  # §1, p (parágrafo único), incisos
)

_BRASIL_AMENDMENT_RE = re.compile(
    r"\((?:Redação|Incluído|Revogado|Vide|Regulamento)"
    r".*?(?:\)|$)",
    re.DOTALL | re.IGNORECASE,
)

_BRASIL_STRUCTURAL_RE = re.compile(
    r"^(TÍTULO|CAPÍTULO|SEÇÃO|SUBSEÇÃO|DISPOSIÇÃO|LIVRO|PARTE)\b",
    re.IGNORECASE,
)


def _parse_brasil_html(
    soup: BeautifulSoup,
    config: RegimeConfig,
    source: str,
) -> list[NormChunk]:
    """Parser para legislação brasileira (Planalto.gov.br)."""
    chunks: list[NormChunk] = []
    current_structural: list[str] = []

    for p_tag in soup.find_all("p"):
        text = _clean_text(p_tag.get_text())
        if not text or len(text) < 5:
            continue

        # Detectar cabeçalhos estruturais (TÍTULO, CAPÍTULO, etc.)
        if _BRASIL_STRUCTURAL_RE.match(text):
            # Atualizar contexto estrutural
            _update_structural_context(current_structural, text)
            continue

        # Detectar artigos via <a name="...">
        anchor = p_tag.find("a", attrs={"name": True})
        hierarchy = _brasil_hierarchy_from_anchor(anchor, text)

        if not hierarchy:
            continue

        # Limpar referências de emenda do texto
        clean = _BRASIL_AMENDMENT_RE.sub("", text).strip()
        clean = _clean_text(clean)

        if not clean or len(clean) < 10:
            continue

        chunks.append(NormChunk(
            id=generate_chunk_id(source, hierarchy, clean),
            source=source,
            regime=NormativeRegime.BRASIL,
            hierarchy=hierarchy,
            text=clean,
            language=config.language,
            cross_references=extract_cross_references(clean, config),
            chunk_type=detect_chunk_type(clean, config),
        ))

    logger.info("%s: %d chunks extraídos", source, len(chunks))
    return chunks


def _brasil_hierarchy_from_anchor(
    anchor: Tag | NavigableString | None,
    text: str,
) -> list[str]:
    """Extrai hierarquia do anchor name ou do texto do parágrafo."""
    if anchor is not None and isinstance(anchor, Tag):
        name = anchor.get("name", "")
        if isinstance(name, list):
            name = name[0] if name else ""

        # art1, art2§1, art3p, art5i, etc.
        if name.startswith("art"):
            return _parse_brasil_anchor_name(name, text)

    # Fallback: detectar Art. N no texto
    m = re.match(r"Art\.\s*(\d+[°ºªo]?(?:-[A-Z])?)\s*", text)
    if m:
        art_label = f"Art. {m.group(1)}"
        # Verificar se tem § ou Parágrafo único
        if "Parágrafo único" in text:
            return [art_label, "Parágrafo único"]
        return [art_label]

    # Parágrafo avulso com §
    m = re.match(r"§\s*(\d+)[°ºª]?\s*", text)
    if m:
        return [f"§ {m.group(1)}"]

    # Inciso (I -, II -, etc.) isolado — sem contexto de artigo
    m = re.match(r"^([IVXLCDM]+)\s*[-–—]\s*", text)
    if m:
        return [m.group(1)]

    return []


def _parse_brasil_anchor_name(name: str, text: str) -> list[str]:
    """Converte anchor name do Planalto em hierarquia.

    Exemplos:
        ``art1``    → ``["Art. 1"]``
        ``art2§1``  → ``["Art. 2", "§ 1"]``
        ``art3p``   → ``["Art. 3", "Parágrafo único"]``
    """
    # Extrair número do artigo
    m = re.match(r"art(\d+[a-zA-Z]?)", name)
    if not m:
        return []

    art_num = m.group(1)
    art_label = f"Art. {art_num}"
    rest = name[m.end():]

    if not rest:
        return [art_label]

    # § seguido de número
    m_sec = re.match(r"[§](\d+)", rest)
    if m_sec:
        return [art_label, f"§ {m_sec.group(1)}"]

    # "p" = Parágrafo único
    if rest == "p":
        return [art_label, "Parágrafo único"]

    # Incisos (i, ii, etc. ou letras de alínea a, b, c)
    if rest and rest[0].islower() and len(rest) <= 2:
        return [art_label, rest]

    return [art_label]


def _update_structural_context(context: list[str], header: str) -> None:
    """Atualiza o contexto estrutural (TÍTULO, CAPÍTULO, etc.)."""
    # Determinar nível
    levels = ["TÍTULO", "CAPÍTULO", "SEÇÃO", "SUBSEÇÃO"]
    header_upper = header.upper()
    for i, level in enumerate(levels):
        if header_upper.startswith(level):
            # Truncar contexto no nível correto
            context[:] = context[:i]
            context.append(header)
            return
    context.append(header)


# ── USA HTML Parser ───────────────────────────────────────────────────


def _parse_usa_html(
    soup: BeautifulSoup,
    config: RegimeConfig,
    source: str,
) -> list[NormChunk]:
    """Parser para legislação norte-americana (Cornell LII + eCFR)."""
    chunks: list[NormChunk] = []

    # Detectar formato: eCFR usa div.section com h4[data-hierarchy-metadata]
    ecfr_sections = soup.find_all(
        "div", class_="section", id=re.compile(r"^\d+\.\d+")
    )
    if ecfr_sections:
        return _parse_usa_ecfr(soup, ecfr_sections, config, source)

    # Cornell LII: buscar container principal
    content_div = soup.find("div", class_="tab-pane active")
    if content_div is None:
        content_div = soup.find("body")
    if content_div is None:
        logger.warning("%s: nenhum container de conteúdo encontrado", source)
        return chunks

    # Processar subsection (a), (b), etc.
    subsections = content_div.find_all(
        "div", class_=re.compile(r"subsection")
    )
    if subsections:
        for subsec in subsections:
            _parse_usa_subsection(subsec, [], config, source, chunks)
    else:
        # Sem subsections — tentar paragraphs diretamente
        paragraphs = content_div.find_all(
            "div", class_=re.compile(r"paragraph")
        )
        for para in paragraphs:
            _parse_usa_paragraph(para, [], config, source, chunks)

    # Fallback: detectar h2/h3 "Section N." (documentos constitucionais)
    if not chunks:
        section_headers = content_div.find_all(
            re.compile(r"^h[23]$"),
            string=re.compile(r"Section\s+\d+", re.IGNORECASE),
        )
        if section_headers:
            for i, h in enumerate(section_headers):
                label = _clean_text(h.get_text())
                # Coletar texto entre este header e o próximo
                text_parts: list[str] = []
                for sibling in h.next_siblings:
                    if isinstance(sibling, Tag) and sibling.name in ("h2", "h3"):
                        break
                    if isinstance(sibling, Tag):
                        text_parts.append(_clean_text(sibling.get_text()))
                text = " ".join(text_parts)
                if text and len(text) >= 10:
                    hierarchy = [label]
                    chunks.append(NormChunk(
                        id=generate_chunk_id(source, hierarchy, text),
                        source=source,
                        regime=NormativeRegime.USA,
                        hierarchy=hierarchy,
                        text=text,
                        language=config.language,
                        cross_references=extract_cross_references(text, config),
                        chunk_type=detect_chunk_type(text, config),
                    ))

    # Se ainda nada, fallback para chunker de texto
    if not chunks:
        text = _clean_text(content_div.get_text())
        if text:
            chunks = chunk_by_hierarchy(text, NormativeRegime.USA, source)

    logger.info("%s: %d chunks extraídos", source, len(chunks))
    return chunks


def _parse_usa_ecfr(
    soup: BeautifulSoup,
    sections: list[Tag],
    config: RegimeConfig,
    source: str,
) -> list[NormChunk]:
    """Parser para documentos eCFR (42 CFR Parts)."""
    chunks: list[NormChunk] = []

    for section in sections:
        sec_id = section.get("id", "")
        h4 = section.find("h4")
        sec_label = f"§ {sec_id}" if sec_id else "§"
        if h4:
            sec_label = _clean_text(h4.get_text())

        # Parágrafos com indentação (a), (b), etc.
        paras = section.find_all(
            "p", class_=re.compile(r"indent")
        )
        if paras:
            for p in paras:
                # Extrair label do span.paragraph-hierarchy
                span = p.find("span", class_="paragraph-hierarchy")
                para_label = _clean_text(span.get_text()) if span else ""
                hierarchy = [sec_label]
                if para_label:
                    hierarchy.append(para_label)

                text = _clean_text(p.get_text())
                if text and len(text) >= 10:
                    chunks.append(NormChunk(
                        id=generate_chunk_id(source, hierarchy, text),
                        source=source,
                        regime=NormativeRegime.USA,
                        hierarchy=hierarchy,
                        text=text,
                        language=config.language,
                        cross_references=extract_cross_references(text, config),
                        chunk_type=detect_chunk_type(text, config),
                    ))
        else:
            # Seção sem parágrafos indentados — texto direto
            text = _clean_text(section.get_text())
            if text and len(text) >= 10:
                chunks.append(NormChunk(
                    id=generate_chunk_id(source, [sec_label], text),
                    source=source,
                    regime=NormativeRegime.USA,
                    hierarchy=[sec_label],
                    text=text,
                    language=config.language,
                    cross_references=extract_cross_references(text, config),
                    chunk_type=detect_chunk_type(text, config),
                ))

    logger.info("%s: %d chunks extraídos (eCFR)", source, len(chunks))
    return chunks


def _parse_usa_subsection(
    element: Tag,
    parent_hierarchy: list[str],
    config: RegimeConfig,
    source: str,
    chunks: list[NormChunk],
) -> None:
    """Processa recursivamente uma subsection do Cornell LII."""
    # Extrair label
    num_span = element.find("span", class_="num", recursive=False)
    label = ""
    if num_span:
        label = _clean_text(num_span.get_text())

    hierarchy = [*parent_hierarchy, label] if label else parent_hierarchy

    # Procurar filhos estruturais
    child_paragraphs = element.find_all(
        "div", class_=re.compile(r"paragraph"), recursive=False
    )
    if child_paragraphs:
        # Capturar chapeau text se existir
        chapeau = element.find("span", class_="chapeau", recursive=False)
        if chapeau:
            chapeau_text = _clean_text(chapeau.get_text())
            if chapeau_text and len(chapeau_text) > 10:
                chunks.append(NormChunk(
                    id=generate_chunk_id(source, [*hierarchy, "chapeau"], chapeau_text),
                    source=source,
                    regime=NormativeRegime.USA,
                    hierarchy=[*hierarchy, "chapeau"],
                    text=chapeau_text,
                    language=config.language,
                    cross_references=extract_cross_references(chapeau_text, config),
                    chunk_type=detect_chunk_type(chapeau_text, config),
                ))

        for para in child_paragraphs:
            _parse_usa_paragraph(para, hierarchy, config, source, chunks)
    else:
        # Nó folha — extrair texto
        text = _usa_extract_content(element)
        if text and len(text) >= 10:
            chunks.append(NormChunk(
                id=generate_chunk_id(source, hierarchy, text),
                source=source,
                regime=NormativeRegime.USA,
                hierarchy=hierarchy,
                text=text,
                language=config.language,
                cross_references=extract_cross_references(text, config),
                chunk_type=detect_chunk_type(text, config),
            ))


def _parse_usa_paragraph(
    element: Tag,
    parent_hierarchy: list[str],
    config: RegimeConfig,
    source: str,
    chunks: list[NormChunk],
) -> None:
    """Processa um paragraph do Cornell LII, recursivamente."""
    num_span = element.find("span", class_="num", recursive=False)
    label = ""
    if num_span:
        label = _clean_text(num_span.get_text())

    hierarchy = [*parent_hierarchy, label] if label else parent_hierarchy

    # Procurar filhos (subparagraph, clause)
    children = element.find_all(
        "div",
        class_=re.compile(r"subparagraph|clause"),
        recursive=False,
    )
    if children:
        # Capturar chapeau
        chapeau = element.find("span", class_="chapeau", recursive=False)
        if chapeau:
            chapeau_text = _clean_text(chapeau.get_text())
            if chapeau_text and len(chapeau_text) > 10:
                chunks.append(NormChunk(
                    id=generate_chunk_id(source, [*hierarchy, "chapeau"], chapeau_text),
                    source=source,
                    regime=NormativeRegime.USA,
                    hierarchy=[*hierarchy, "chapeau"],
                    text=chapeau_text,
                    language=config.language,
                    cross_references=extract_cross_references(chapeau_text, config),
                    chunk_type=detect_chunk_type(chapeau_text, config),
                ))

        for child in children:
            _parse_usa_paragraph(child, hierarchy, config, source, chunks)
    else:
        text = _usa_extract_content(element)
        if text and len(text) >= 10:
            chunks.append(NormChunk(
                id=generate_chunk_id(source, hierarchy, text),
                source=source,
                regime=NormativeRegime.USA,
                hierarchy=hierarchy,
                text=text,
                language=config.language,
                cross_references=extract_cross_references(text, config),
                chunk_type=detect_chunk_type(text, config),
            ))


def _usa_extract_content(element: Tag) -> str:
    """Extrai texto de conteúdo de um elemento USA, limpando definições inline."""
    content_div = element.find("div", class_="content")
    if content_div:
        return _clean_text(content_div.get_text())
    # Fallback: texto direto (excluindo sub-elementos estruturais)
    texts: list[str] = []
    for child in element.children:
        if isinstance(child, NavigableString):
            texts.append(str(child))
        elif isinstance(child, Tag) and child.get("class") not in [
            ["paragraph"], ["subparagraph"], ["clause"],
        ]:
            texts.append(child.get_text())
    return _clean_text(" ".join(texts))


# ── EU HTML Parser ────────────────────────────────────────────────────


def _parse_eu_html(
    soup: BeautifulSoup,
    config: RegimeConfig,
    source: str,
) -> list[NormChunk]:
    """Parser para legislação europeia (EUR-Lex)."""
    chunks: list[NormChunk] = []

    # Processar artigos
    articles = soup.find_all("div", class_="eli-subdivision", id=re.compile(r"^art_\d+$"))
    for art_div in articles:
        _parse_eu_article(art_div, config, source, chunks)

    # Se não encontrou artigos com id="art_N", fallback para text chunker
    if not chunks:
        text = _clean_text(soup.get_text())
        if text:
            chunks = chunk_by_hierarchy(text, NormativeRegime.EU, source)

    logger.info("%s: %d chunks extraídos", source, len(chunks))
    return chunks


def _parse_eu_article(
    art_div: Tag,
    config: RegimeConfig,
    source: str,
    chunks: list[NormChunk],
) -> None:
    """Processa um artigo do EUR-Lex."""
    # Extrair número e título do artigo
    title_p = art_div.find("p", class_="oj-ti-art")
    art_label = _clean_text(title_p.get_text()) if title_p else "Article"

    # Subtitle
    subtitle_p = art_div.find("p", class_="oj-sti-art")
    art_title = _clean_text(subtitle_p.get_text()) if subtitle_p else ""

    # Parágrafos numerados (id="NNN.NNN")
    numbered_divs = art_div.find_all(
        "div", id=re.compile(r"^\d{3}\.\d{3}$")
    )

    if numbered_divs:
        for ndiv in numbered_divs:
            div_id = ndiv.get("id", "")
            # Extrair número do parágrafo do id (e.g., "001.002" → "2")
            para_num = str(int(div_id.split(".")[1])) if "." in str(div_id) else ""
            hierarchy = [art_label, para_num] if para_num else [art_label]

            # Extrair texto do parágrafo
            para_text_parts: list[str] = []

            # Texto direto em <p class="oj-normal">
            for p in ndiv.find_all("p", class_="oj-normal", recursive=False):
                para_text_parts.append(_clean_text(p.get_text()))

            # Sub-pontos em tabelas (a), (b), etc.
            tables = ndiv.find_all("table", recursive=False)
            for table in tables:
                rows = table.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) >= 2:
                        point_label = _clean_text(cells[0].get_text())
                        point_text = _clean_text(cells[1].get_text())
                        if point_text:
                            sub_hierarchy = [*hierarchy, point_label]
                            chunks.append(NormChunk(
                                id=generate_chunk_id(source, sub_hierarchy, point_text),
                                source=source,
                                regime=NormativeRegime.EU,
                                hierarchy=sub_hierarchy,
                                text=point_text,
                                language=config.language,
                                cross_references=extract_cross_references(
                                    point_text, config
                                ),
                                chunk_type=detect_chunk_type(point_text, config),
                            ))

            # Texto do parágrafo (excluindo sub-pontos já processados)
            para_text = " ".join(para_text_parts)
            if para_text and len(para_text) >= 10:
                chunks.append(NormChunk(
                    id=generate_chunk_id(source, hierarchy, para_text),
                    source=source,
                    regime=NormativeRegime.EU,
                    hierarchy=hierarchy,
                    text=para_text,
                    language=config.language,
                    cross_references=extract_cross_references(para_text, config),
                    chunk_type=detect_chunk_type(para_text, config),
                ))
    else:
        # Artigo sem parágrafos numerados — texto direto
        text_parts: list[str] = []
        for p in art_div.find_all("p", class_="oj-normal"):
            text_parts.append(_clean_text(p.get_text()))
        text = " ".join(text_parts)
        if text and len(text) >= 10:
            hierarchy = [art_label]
            chunks.append(NormChunk(
                id=generate_chunk_id(source, hierarchy, text),
                source=source,
                regime=NormativeRegime.EU,
                hierarchy=hierarchy,
                text=text,
                language=config.language,
                cross_references=extract_cross_references(text, config),
                chunk_type=detect_chunk_type(text, config),
            ))


# ── PDF parsing ───────────────────────────────────────────────────────


def _parse_pdf(
    path: Path,
    config: RegimeConfig,
    source: str,
    regime: NormativeRegime,
) -> list[NormChunk]:
    """Extrai texto de PDF via PyMuPDF e delega ao chunker.

    Usa get_text("blocks", sort=True) para preservar ordem e unicode.
    """
    import unicodedata
    doc = fitz.open(str(path))
    pages: list[str] = []
    for page in doc:
        blocks = page.get_text("blocks", sort=True)
        text_parts: list[str] = []
        for block in blocks:
            if block[6] == 0:  # tipo 0 = texto (nao imagem)
                t = block[4].strip()
                if len(t) > 3:
                    text_parts.append(t)
        pages.append("\n".join(text_parts))
    doc.close()

    full_text = "\n\n".join(pages)
    full_text = unicodedata.normalize("NFC", full_text)
    full_text = _clean_text(full_text)

    if not full_text:
        logger.warning("%s: PDF sem texto extraivel", source)
        return []

    chunks = chunk_by_hierarchy(full_text, regime, source)
    logger.info("%s: %d chunks extraidos (PDF)", source, len(chunks))
    return chunks


def _parse_markdown(
    path: Path,
    config: RegimeConfig,
    source: str,
    regime: NormativeRegime,
) -> list[NormChunk]:
    """Extrai chunks de Markdown dividindo por headers.

    Headers ``##`` definem nível 1 e ``###`` definem nível 2.
    Cada bloco de texto sob um header gera um chunk.
    """
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        logger.warning("%s: Markdown vazio", source)
        return []

    chunks: list[NormChunk] = []
    # Encontrar todos os headers e suas posições
    headers = list(_MD_HEADER_RE.finditer(text))

    if not headers:
        # Sem headers — bloco único
        clean = _clean_text(text)
        if clean and len(clean) >= 10:
            chunks.append(NormChunk(
                id=generate_chunk_id(source, ["Texto Integral"], clean),
                source=source,
                regime=regime,
                hierarchy=["Texto Integral"],
                text=clean,
                language=config.language,
                cross_references=extract_cross_references(clean, config),
                chunk_type=detect_chunk_type(clean, config),
            ))
        return chunks

    # Construir hierarquia a partir dos headers
    current_h2 = ""
    for i, match in enumerate(headers):
        level = len(match.group(1))  # número de #
        title = match.group(2).strip()

        # Rastrear contexto hierárquico
        if level <= 2:
            current_h2 = title

        # Extrair conteúdo entre este header e o próximo
        start = match.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        content = text[start:end].strip()

        # Pular separadores (---) e conteúdo vazio
        content = re.sub(r"^-{3,}\s*$", "", content, flags=re.MULTILINE).strip()
        if not content or len(content) < 10:
            continue

        # Construir hierarquia
        if level <= 2:
            hierarchy = [title]
        else:
            hierarchy = [current_h2, title] if current_h2 else [title]

        # Dividir conteúdo em parágrafos significativos
        paragraphs = [
            p.strip() for p in content.split("\n\n")
            if p.strip() and len(p.strip()) >= 10
        ]

        if len(paragraphs) <= 1:
            # Um parágrafo ou tabela — chunk único para esta seção
            clean = _clean_text(content)
            if clean:
                chunks.append(NormChunk(
                    id=generate_chunk_id(source, hierarchy, clean),
                    source=source,
                    regime=regime,
                    hierarchy=hierarchy,
                    text=clean,
                    language=config.language,
                    cross_references=extract_cross_references(clean, config),
                    chunk_type=detect_chunk_type(clean, config),
                ))
        else:
            # Múltiplos parágrafos — chunk por parágrafo
            for j, para in enumerate(paragraphs):
                clean = _clean_text(para)
                if clean and len(clean) >= 10:
                    para_hierarchy = [*hierarchy, str(j + 1)]
                    chunks.append(NormChunk(
                        id=generate_chunk_id(source, para_hierarchy, clean),
                        source=source,
                        regime=regime,
                        hierarchy=para_hierarchy,
                        text=clean,
                        language=config.language,
                        cross_references=extract_cross_references(clean, config),
                        chunk_type=detect_chunk_type(clean, config),
                    ))

    logger.info("%s: %d chunks extraídos (Markdown)", source, len(chunks))
    return chunks
