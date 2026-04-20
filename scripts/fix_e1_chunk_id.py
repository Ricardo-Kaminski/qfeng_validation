"""Aplica 3 fixes estruturais ao E1 antes de regenerar."""
import pathlib
import py_compile
import re

ROOT = pathlib.Path(__file__).parents[1]
CHUNKER = ROOT / "src" / "qfeng" / "c1_digestion" / "ingestion" / "chunker.py"
PARSER  = ROOT / "src" / "qfeng" / "c1_digestion" / "ingestion" / "parser.py"

# ── FIX 1a: generate_chunk_id — assinatura + corpo ───────────────────────
chunker = CHUNKER.read_text(encoding="utf-8")

# Substituir apenas o corpo funcional (não depende do docstring)
OLD_BODY = (
    '    hierarchy_path = ":".join(hierarchy)\n'
    '    raw = f"{source}:{hierarchy_path}"\n'
    '    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]'
)
NEW_BODY = (
    '    hierarchy_path = ":".join(hierarchy)\n'
    '    text_snippet = text[:200].strip() if text else ""\n'
    '    raw = f"{source}:{hierarchy_path}:{text_snippet}"\n'
    '    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]'
)
assert OLD_BODY in chunker, f"ERRO: corpo generate_chunk_id nao encontrado"
chunker = chunker.replace(OLD_BODY, NEW_BODY)

# Atualizar assinatura
OLD_SIG = "def generate_chunk_id(source: str, hierarchy: list[str]) -> str:"
NEW_SIG = 'def generate_chunk_id(source: str, hierarchy: list[str], text: str = "") -> str:'
assert OLD_SIG in chunker, "ERRO: assinatura generate_chunk_id nao encontrada"
chunker = chunker.replace(OLD_SIG, NEW_SIG)

# FIX 1b: _make_chunk passa text=
OLD_MAKE = "        id=generate_chunk_id(source, hierarchy),"
NEW_MAKE = "        id=generate_chunk_id(source, hierarchy, text),"
assert OLD_MAKE in chunker, "ERRO: _make_chunk nao encontrado"
chunker = chunker.replace(OLD_MAKE, NEW_MAKE)

CHUNKER.write_text(chunker, encoding="utf-8")
py_compile.compile(str(CHUNKER), doraise=True)
print("FIX 1 OK: generate_chunk_id inclui text snippet")

# ── FIX 3: _read_html normaliza NFC ─────────────────────────────────────
parser = PARSER.read_text(encoding="utf-8")

OLD_READ = (
    '    try:\n'
    '        return path.read_text(encoding="utf-8")\n'
    '    except UnicodeDecodeError:\n'
    '        logger.warning("Fallback para latin-1: %s", path.name)\n'
    '        return path.read_text(encoding="latin-1")'
)
NEW_READ = (
    '    import unicodedata\n'
    '    try:\n'
    '        text = path.read_text(encoding="utf-8")\n'
    '    except UnicodeDecodeError:\n'
    '        logger.warning("Fallback para latin-1: %s", path.name)\n'
    '        text = path.read_text(encoding="latin-1")\n'
    '    return unicodedata.normalize("NFC", text)'
)
assert OLD_READ in parser, "ERRO: _read_html body nao encontrado"
parser = parser.replace(OLD_READ, NEW_READ)
print("FIX 3 OK: _read_html normaliza NFC")

# ── FIX 2: _parse_pdf usa blocks+sort ───────────────────────────────────
OLD_PDF_BODY = (
    '    doc = fitz.open(str(path))\n'
    '    pages: list[str] = []\n'
    '    for page in doc:\n'
    '        text = page.get_text()\n'
    '        # Limpar headers/footers repetidos (linhas curtas no in'
)
# find and replace the whole function body
pdf_start = parser.index('    doc = fitz.open(str(path))\n    pages: list[str] = []\n    for page in doc:\n        text = page.get_text()')
pdf_end = parser.index('\n    chunks = chunk_by_hierarchy(full_text, regime, source)\n    logger.info("%s: %d chunks extra', pdf_start) + 1

OLD_PDF = parser[pdf_start:pdf_end]

NEW_PDF_BODY = (
    '    import unicodedata\n'
    '    doc = fitz.open(str(path))\n'
    '    pages: list[str] = []\n'
    '    for page in doc:\n'
    '        blocks = page.get_text("blocks", sort=True)\n'
    '        text_parts: list[str] = []\n'
    '        for block in blocks:\n'
    '            if block[6] == 0:  # tipo 0 = texto\n'
    '                t = block[4].strip()\n'
    '                if len(t) > 3:\n'
    '                    text_parts.append(t)\n'
    '        pages.append("\\n".join(text_parts))\n'
    '    doc.close()\n\n'
    '    full_text = "\\n\\n".join(pages)\n'
    '    full_text = unicodedata.normalize("NFC", full_text)\n'
    '    full_text = _clean_text(full_text)\n\n'
    '    if not full_text:\n'
    '        logger.warning("%s: PDF sem texto extraivel", source)\n'
    '        return []\n\n'
)

# find the full old pdf body (from doc = fitz... to the last line before chunks = ...)
# Use a different approach: find the whole function and replace it
OLD_PDF_FUNC = '''\
def _parse_pdf(
    path: Path,
    config: RegimeConfig,
    source: str,
    regime: NormativeRegime,
) -> list[NormChunk]:'''

pdf_func_start = parser.index(OLD_PDF_FUNC)
# find next def after this
next_def = parser.index('\ndef _parse_markdown', pdf_func_start)
old_func = parser[pdf_func_start:next_def]

new_func = '''\
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
        pages.append("\\n".join(text_parts))
    doc.close()

    full_text = "\\n\\n".join(pages)
    full_text = unicodedata.normalize("NFC", full_text)
    full_text = _clean_text(full_text)

    if not full_text:
        logger.warning("%s: PDF sem texto extraivel", source)
        return []

    chunks = chunk_by_hierarchy(full_text, regime, source)
    logger.info("%s: %d chunks extraidos (PDF)", source, len(chunks))
    return chunks

'''

parser = parser.replace(old_func, new_func)
print("FIX 2 OK: _parse_pdf usa blocks+NFC")

# ── FIX 1c: todas as chamadas generate_chunk_id em parser.py ─────────────
# Usar regex para encontrar generate_chunk_id(source, X) sem text= e adicionar text=VAR
# Estratégia: após cada NormChunk( com id=generate_chunk_id, extrair text=VAR do mesmo bloco
# e inserir o text= na chamada.
# Abordagem simples e robusta: localizar cada NormChunk( ... ) bloco e fazer substituição

def add_text_arg(src: str) -> tuple[str, int]:
    """Substitui generate_chunk_id(source, X) por generate_chunk_id(source, X, text_var)
    usando o valor text=VAR do mesmo NormChunk() bloco."""
    count = 0
    # Padrão: id=generate_chunk_id(source, EXPR), dentro de um NormChunk(
    # Logo após (ou próximo), haverá text=VAR,
    # Fazemos match do bloco NormChunk( ... ) e extraímos text=VAR
    pattern = re.compile(
        r'(NormChunk\(.*?id=generate_chunk_id\((source,\s*[^)]+?)\))'
        r'(.*?text=(\w+),)',
        re.DOTALL,
    )
    def replacer(m):
        nonlocal count
        full = m.group(0)
        norm_chunk_part = m.group(1)
        gen_args = m.group(2)
        after = m.group(3)
        text_var = m.group(4)
        # Already has text arg?
        if re.search(r'generate_chunk_id\(' + re.escape(gen_args) + r',\s*\w+\)', norm_chunk_part):
            return full
        new_norm_chunk = norm_chunk_part.replace(
            f'generate_chunk_id({gen_args})',
            f'generate_chunk_id({gen_args}, {text_var})',
        )
        count += 1
        return new_norm_chunk + after

    result = pattern.sub(replacer, src)
    return result, count

parser, n = add_text_arg(parser)
print(f"FIX 1c: {n} chamadas generate_chunk_id atualizadas em parser.py")

# Verificar chamadas restantes sem text= (não deveria haver nenhuma em NormChunk)
remaining = re.findall(
    r'NormChunk\(.*?id=generate_chunk_id\(source,\s*[^\)]+\)(?!\s*,\s*\w)',
    parser,
    re.DOTALL,
)
if remaining:
    print(f"  AVISO: {len(remaining)} chamadas ainda sem text=")
else:
    print("  Todas as chamadas dentro de NormChunk() atualizadas.")

PARSER.write_text(parser, encoding="utf-8")
py_compile.compile(str(PARSER), doraise=True)
print("parser.py syntax OK")

print()
print("=== 3 FIXES APLICADOS COM SUCESSO ===")
