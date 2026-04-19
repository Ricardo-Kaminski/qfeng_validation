"""E1 batch runner — processa todo o corpus e gera outputs JSON + relatório.

Executa ``parse_document`` para cada arquivo do corpus,
salva chunks individuais por documento e gera relatório consolidado
com mapa de concorrências normativas (token overlap).
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

from qfeng.c1_digestion.ingestion.parser import parse_document
from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.core.schemas import NormativeRegime, NormChunk

logger = logging.getLogger(__name__)

# Extensões processáveis
_PROCESSABLE_EXTENSIONS = {".htm", ".html", ".pdf", ".md"}

# Arquivos a ignorar (READMEs, manifestos, logs)
_IGNORE_PATTERNS = {"readme", "manifest", "download_log"}

# Stopwords para token overlap (PT + EN)
_STOPWORDS = frozenset({
    "a", "o", "e", "de", "do", "da", "dos", "das", "em", "no", "na",
    "nos", "nas", "um", "uma", "para", "por", "com", "se", "que", "ou",
    "ao", "à", "às", "aos", "seu", "sua", "seus", "suas", "este",
    "esta", "esse", "essa", "aquele", "aquela", "não", "mais", "como",
    "the", "an", "of", "in", "to", "and", "or", "for", "with",
    "by", "on", "at", "from", "is", "are", "be", "was", "were",
    "shall", "may", "such", "any", "all", "each", "other", "this",
    "that", "which", "who", "its", "their", "under", "as", "it",
})


@dataclass
class E1BatchResult:
    """Resultado consolidado do batch E1."""

    total_documents: int = 0
    total_chunks: int = 0
    chunks_per_regime: dict[str, int] = field(default_factory=dict)
    chunks_per_document: dict[str, int] = field(default_factory=dict)
    chunk_type_distribution: dict[str, int] = field(default_factory=dict)
    cross_ref_count: int = 0
    concurrency_pairs: list[tuple[str, str, float]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _filter_chunks_by_scope(
    chunks: list[NormChunk],
    scope: ScopeConfig,
) -> list[NormChunk]:
    """Filtra chunks por scope: hierarquia, tipo e tamanho mínimo.

    Descarta chunks sem hierarquia (integridade estrutural, independe do scope).
    """
    result: list[NormChunk] = []
    for chunk in chunks:
        if not chunk.hierarchy:
            continue
        if len(chunk.text) < scope.min_chunk_chars:
            continue
        if chunk.chunk_type not in scope.chunk_types:
            continue
        if len(chunk.hierarchy) > scope.hierarchy_depth:
            continue
        result.append(chunk)
    return result


def run_e1_batch(
    corpus_dir: Path,
    output_dir: Path,
) -> E1BatchResult:
    """Processa todo o corpus e gera outputs JSON + relatório.

    Itera sobre todos os documentos processáveis em ``corpus_dir/``,
    organizados por regime. Salva chunks por documento e gera
    ``e1_report.md`` com estatísticas e mapa de concorrências.

    Args:
        corpus_dir: Raiz do diretório ``corpora/``.
        output_dir: Diretório de saída para JSONs e relatório.

    Returns:
        E1BatchResult com estatísticas consolidadas.
    """
    result = E1BatchResult()
    all_chunks: dict[str, list[NormChunk]] = {}  # regime -> chunks

    for regime in NormativeRegime:
        regime_dir = corpus_dir / regime.value
        if not regime_dir.exists():
            logger.warning("Diretório do regime não encontrado: %s", regime_dir)
            continue

        regime_chunks: list[NormChunk] = []
        files = _discover_files(regime_dir)

        for file_path in files:
            try:
                chunks = parse_document(file_path, regime)
            except Exception as exc:
                msg = f"Erro ao processar {file_path.name}: {exc}"
                logger.error(msg)
                result.warnings.append(msg)
                continue

            # Validar chunks
            valid_chunks: list[NormChunk] = []
            for chunk in chunks:
                if not chunk.text or len(chunk.text) < 10:
                    result.warnings.append(
                        f"Chunk com texto curto (<10 chars): {chunk.id} em {file_path.name}"
                    )
                    continue
                if not chunk.hierarchy:
                    result.warnings.append(
                        f"Chunk sem hierarquia: {chunk.id} em {file_path.name}"
                    )
                    continue
                valid_chunks.append(chunk)

            # Salvar JSON por documento
            _save_document_chunks(valid_chunks, file_path, regime, output_dir)

            result.total_documents += 1
            result.chunks_per_document[file_path.name] = len(valid_chunks)
            regime_chunks.extend(valid_chunks)

            # Contabilizar tipos
            for chunk in valid_chunks:
                result.chunk_type_distribution[chunk.chunk_type] = (
                    result.chunk_type_distribution.get(chunk.chunk_type, 0) + 1
                )
                if chunk.cross_references:
                    result.cross_ref_count += len(chunk.cross_references)

        all_chunks[regime.value] = regime_chunks
        result.chunks_per_regime[regime.value] = len(regime_chunks)
        result.total_chunks += len(regime_chunks)

    # Detecção de concorrências (token overlap)
    result.concurrency_pairs = _detect_concurrencies(all_chunks)

    # Salvar concurrency map
    concurrency_map = _build_concurrency_map(result.concurrency_pairs)
    _save_json(concurrency_map, output_dir / "concurrency_map.json")

    # Gerar relatório (com lookup de chunks para human labels)
    _generate_report(result, output_dir / "e1_report.md", all_chunks)

    logger.info(
        "E1 batch completo: %d documentos, %d chunks, %d concorrências",
        result.total_documents,
        result.total_chunks,
        len(result.concurrency_pairs),
    )
    return result


def _discover_files(directory: Path) -> list[Path]:
    """Descobre arquivos processáveis recursivamente."""
    files: list[Path] = []
    for path in sorted(directory.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in _PROCESSABLE_EXTENSIONS:
            continue
        if any(pat in path.stem.lower() for pat in _IGNORE_PATTERNS):
            continue
        files.append(path)
    return files


def _save_document_chunks(
    chunks: list[NormChunk],
    file_path: Path,
    regime: NormativeRegime,
    output_dir: Path,
) -> None:
    """Salva chunks de um documento como JSON."""
    regime_out = output_dir / regime.value
    regime_out.mkdir(parents=True, exist_ok=True)

    out_path = regime_out / f"{file_path.stem}.json"
    data = [chunk.model_dump(mode="json") for chunk in chunks]
    out_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _save_json(data: dict[str, list[str]], path: Path) -> None:
    """Salva dicionário como JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# ── Detecção de concorrências (token overlap) ────────────────────────


def _tokenize(text: str) -> set[str]:
    """Tokeniza texto em palavras significativas (sem stopwords)."""
    words = text.lower().split()
    return {
        w.strip(".,;:()[]\"'")
        for w in words
        if len(w) > 2 and w.strip(".,;:()[]\"'") not in _STOPWORDS
    }


def _detect_concurrencies(
    all_chunks: dict[str, list[NormChunk]],
    threshold: float = 0.55,
) -> list[tuple[str, str, float]]:
    """Detecta pares de chunks com sobreposição normativa via token overlap.

    Compara chunks de documentos DIFERENTES dentro do mesmo regime.
    Usa coeficiente de Jaccard sobre tokens significativos.
    Deduplica pares via frozenset.

    Args:
        all_chunks: Chunks agrupados por regime.
        threshold: Overlap mínimo de Jaccard para considerar concorrência.

    Returns:
        Lista de ``(chunk_id_a, chunk_id_b, jaccard_score)`` sem duplicatas.
    """
    seen: set[frozenset[str]] = set()
    pairs: list[tuple[str, str, float]] = []

    for _regime, chunks in all_chunks.items():
        # Agrupar por source
        by_source: dict[str, list[NormChunk]] = {}
        for chunk in chunks:
            by_source.setdefault(chunk.source, []).append(chunk)

        sources = list(by_source.keys())
        if len(sources) < 2:
            continue

        # Pré-tokenizar
        token_cache: dict[str, set[str]] = {}
        for chunk in chunks:
            token_cache[chunk.id] = _tokenize(chunk.text)

        # Comparar chunks entre fontes diferentes
        for i in range(len(sources)):
            for j in range(i + 1, len(sources)):
                for chunk_a in by_source[sources[i]]:
                    tokens_a = token_cache[chunk_a.id]
                    if len(tokens_a) < 3:
                        continue
                    for chunk_b in by_source[sources[j]]:
                        tokens_b = token_cache[chunk_b.id]
                        if len(tokens_b) < 3:
                            continue

                        pair_key = frozenset({chunk_a.id, chunk_b.id})
                        if pair_key in seen:
                            continue

                        intersection = tokens_a & tokens_b
                        union = tokens_a | tokens_b
                        if not union:
                            continue

                        jaccard = len(intersection) / len(union)
                        if jaccard >= threshold:
                            seen.add(pair_key)
                            pairs.append((chunk_a.id, chunk_b.id, round(jaccard, 3)))

    # Ordenar por score descendente
    pairs.sort(key=lambda x: x[2], reverse=True)
    return pairs


def _build_concurrency_map(
    pairs: list[tuple[str, str, float]],
) -> dict[str, list[str]]:
    """Converte pares de concorrência em mapa id → [ids concorrentes]."""
    cmap: dict[str, list[str]] = {}
    for id_a, id_b, _ in pairs:
        cmap.setdefault(id_a, []).append(id_b)
        cmap.setdefault(id_b, []).append(id_a)
    return cmap


# ── Geração de relatório ─────────────────────────────────────────────


def _generate_report(
    result: E1BatchResult,
    path: Path,
    all_chunks: dict[str, list[NormChunk]] | None = None,
) -> None:
    """Gera relatório consolidado em Markdown."""
    from qfeng.c1_digestion.ingestion.labels import human_label

    path.parent.mkdir(parents=True, exist_ok=True)

    # Construir lookup de chunks por ID para human labels
    chunk_lookup: dict[str, NormChunk] = {}
    if all_chunks:
        for chunks in all_chunks.values():
            for chunk in chunks:
                chunk_lookup[chunk.id] = chunk

    lines: list[str] = [
        "# E1 Ingestion Report",
        "",
        "## Resumo",
        "",
        f"- **Total de documentos processados:** {result.total_documents}",
        f"- **Total de chunks gerados:** {result.total_chunks}",
        f"- **Referências cruzadas detectadas:** {result.cross_ref_count}",
        f"- **Pares de concorrência normativa:** {len(result.concurrency_pairs)}",
        f"- **Alertas:** {len(result.warnings)}",
        "",
        "## Chunks por Regime",
        "",
        "| Regime | Chunks |",
        "|--------|--------|",
    ]

    for regime, count in sorted(result.chunks_per_regime.items()):
        lines.append(f"| {regime} | {count} |")

    lines.extend([
        "",
        "## Chunks por Documento",
        "",
        "| Documento | Chunks |",
        "|-----------|--------|",
    ])

    for doc, count in sorted(
        result.chunks_per_document.items(), key=lambda x: x[1], reverse=True
    ):
        lines.append(f"| {doc} | {count} |")

    lines.extend([
        "",
        "## Distribuição de chunk_type",
        "",
        "| Tipo | Quantidade |",
        "|------|-----------|",
    ])

    for ctype, count in sorted(
        result.chunk_type_distribution.items(), key=lambda x: x[1], reverse=True
    ):
        lines.append(f"| {ctype} | {count} |")

    if result.concurrency_pairs:
        lines.extend([
            "",
            "## Mapa de Concorrências Normativas",
            "",
            f"Total de pares com Jaccard >= 0.55: **{len(result.concurrency_pairs)}**",
            "",
        ])
        # Mostrar top 50 com human labels
        for id_a, id_b, score in result.concurrency_pairs[:50]:
            label_a = human_label(chunk_lookup[id_a], 60) if id_a in chunk_lookup else id_a
            label_b = human_label(chunk_lookup[id_b], 60) if id_b in chunk_lookup else id_b
            lines.extend([
                f"- **Jaccard {score:.3f}**",
                f"  - [A] {label_a}",
                f"  - [B] {label_b}",
            ])
        if len(result.concurrency_pairs) > 50:
            lines.append(
                f"\n*... e mais {len(result.concurrency_pairs) - 50} pares.*"
            )

    if result.warnings:
        lines.extend([
            "",
            "## Alertas",
            "",
        ])
        for warning in result.warnings[:100]:
            lines.append(f"- {warning}")
        if len(result.warnings) > 100:
            lines.append(f"- ... ({len(result.warnings) - 100} mais alertas)")

    path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Relatório salvo em %s", path)


# ── CLI entry point ───────────────────────────────────────────────────


def main() -> None:
    """Entry point para execução via ``python -m``."""
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="E1 — Processa corpus normativo em NormChunks"
    )
    parser.add_argument(
        "--corpus-dir",
        type=Path,
        default=Path("corpora"),
        help="Diretório raiz do corpus (default: corpora/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/e1_chunks"),
        help="Diretório de saída (default: outputs/e1_chunks/)",
    )
    args = parser.parse_args()

    result = run_e1_batch(args.corpus_dir, args.output_dir)

    print(f"\nE1 concluído: {result.total_chunks} chunks de {result.total_documents} documentos")
    for regime, count in sorted(result.chunks_per_regime.items()):
        print(f"  {regime}: {count} chunks")
    if result.concurrency_pairs:
        print(f"  Concorrências: {len(result.concurrency_pairs)} pares")
    if result.warnings:
        print(f"  Alertas: {len(result.warnings)}")


if __name__ == "__main__":
    main()
