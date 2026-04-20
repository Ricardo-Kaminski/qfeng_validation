"""E2 batch runner — processa chunks JSON do E1 e extrai DeonticAtoms.

Carrega NormChunks dos JSONs de saída do E1, aplica o extractor
com cache e concurrency context, e gera relatório consolidado.
"""

from __future__ import annotations

import json
import logging
import re
import subprocess
import time
from pathlib import Path

from qfeng.c1_digestion.deontic.extractor import extract_deontic
from qfeng.c1_digestion.deontic.reporter import E2BatchResult, generate_e2_report
from qfeng.core.schemas import NormChunk

logger = logging.getLogger(__name__)


def run_e2_batch(
    corpus_dir: Path,
    cache_dir: Path,
    report_path: Path,
    anchor_files: list[Path] | None = None,
    chunk_filter: re.Pattern[str] | None = None,
) -> E2BatchResult:
    """Executa extração deontica em batch sobre chunks do E1.

    Args:
        corpus_dir: Diretório com JSONs do E1 (outputs/e1_chunks/).
        cache_dir: Diretório de cache (outputs/deontic_cache/).
        report_path: Caminho para o relatório E2.
        anchor_files: Se fornecido, processa apenas estes arquivos.
            Se None, processa todos os JSONs encontrados.
        chunk_filter: Regex aplicado ao texto do chunk. Se fornecido,
            apenas chunks cujo texto faz match são processados.
            Chunks já em cache são sempre incluídos.

    Returns:
        E2BatchResult com estatísticas consolidadas.
    """
    # Descobrir arquivos a processar
    if anchor_files:
        json_files = [f for f in anchor_files if f.exists()]
        missing = [f for f in anchor_files if not f.exists()]
        for m in missing:
            logger.warning("Arquivo não encontrado: %s", m)
    else:
        json_files = sorted(corpus_dir.rglob("*.json"))
        # Excluir concurrency_map.json e outros não-chunk
        json_files = [
            f for f in json_files
            if f.name not in ("concurrency_map.json",)
        ]

    # Carregar concurrency map
    cmap_path = corpus_dir / "concurrency_map.json"
    concurrency_map: dict[str, list[str]] = {}
    if cmap_path.exists():
        concurrency_map = json.loads(cmap_path.read_text(encoding="utf-8"))

    # Carregar todos os chunks em memória para lookup de concorrentes
    all_chunks: dict[str, NormChunk] = {}
    chunks_to_process: list[NormChunk] = []

    skipped_by_filter = 0
    for json_file in json_files:
        data = json.loads(json_file.read_text(encoding="utf-8"))
        for item in data:
            chunk = NormChunk.model_validate(item)
            all_chunks[chunk.id] = chunk

            # Aplicar filtro: pular chunks que não fazem match
            # (exceto se já estão em cache — sempre incluir cacheados)
            if chunk_filter is not None:
                cache_path = cache_dir / f"{chunk.id}.json"
                if not cache_path.exists() and not chunk_filter.search(chunk.text):
                    skipped_by_filter += 1
                    continue

            chunks_to_process.append(chunk)

    if skipped_by_filter:
        logger.info("Filtro aplicado: %d chunks pulados", skipped_by_filter)

    # Contar total no corpus (todos os JSONs, não só os âncora)
    total_corpus = 0
    for f in corpus_dir.rglob("*.json"):
        if f.name == "concurrency_map.json":
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        total_corpus += len(data)

    result = E2BatchResult(total_chunks_in_corpus=total_corpus)

    logger.info(
        "E2 batch: %d chunks a processar (%d no corpus total)",
        len(chunks_to_process),
        total_corpus,
    )

    # Processar cada chunk com resiliência a crashes do Ollama
    consecutive_errors = 0
    max_consecutive_errors = 3

    for i, chunk in enumerate(chunks_to_process):
        # Verificar se já está em cache
        cache_path = cache_dir / f"{chunk.id}.json"
        from_cache = cache_path.exists()

        # Montar contexto de concorrentes
        concurrent_ids = concurrency_map.get(chunk.id, [])
        concurrent_chunks = [
            all_chunks[cid] for cid in concurrent_ids
            if cid in all_chunks
        ]

        # Extrair com retry e restart do Ollama em caso de crash
        try:
            atoms = extract_deontic(
                chunk,
                cache_dir=cache_dir,
                concurrent_chunks=concurrent_chunks if concurrent_chunks else None,
            )
            consecutive_errors = 0
        except Exception as exc:
            error_msg = str(exc)
            if "unexpectedly stopped" in error_msg or "Connection" in error_msg:
                consecutive_errors += 1
                logger.warning(
                    "Ollama crash no chunk %d/%d (%s). Reiniciando... (%d/%d)",
                    i + 1,
                    len(chunks_to_process),
                    chunk.id,
                    consecutive_errors,
                    max_consecutive_errors,
                )
                if consecutive_errors >= max_consecutive_errors:
                    logger.error(
                        "Ollama crashou %d vezes seguidas. Abortando.",
                        max_consecutive_errors,
                    )
                    break
                _restart_ollama()
                # Retry após restart
                try:
                    atoms = extract_deontic(
                        chunk,
                        cache_dir=cache_dir,
                        concurrent_chunks=concurrent_chunks if concurrent_chunks else None,
                    )
                    consecutive_errors = 0
                except Exception:
                    logger.warning("Retry falhou para chunk %s. Pulando.", chunk.id)
                    atoms = []
            else:
                logger.error("Erro inesperado no chunk %s: %s", chunk.id, exc)
                atoms = []

        result.record_extraction(chunk, atoms, from_cache=from_cache)

        if (i + 1) % 100 == 0:
            logger.info(
                "Progresso: %d/%d chunks (%d atoms, %d cache hits)",
                i + 1,
                len(chunks_to_process),
                result.total_atoms_extracted,
                result.cache_hits,
            )

    # Gerar relatório
    generate_e2_report(result, report_path)

    logger.info(
        "E2 batch completo: %d chunks → %d atoms (%d cache, %d LLM)",
        result.total_chunks_processed,
        result.total_atoms_extracted,
        result.cache_hits,
        result.llm_calls,
    )
    return result


def _restart_ollama() -> None:
    """Reinicia o servidor Ollama após crash."""
    logger.info("Reiniciando Ollama...")
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "ollama.exe"],
            capture_output=True,
            timeout=10,
        )
    except Exception:
        pass
    time.sleep(3)
    subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )
    # Aguardar o servidor ficar pronto
    time.sleep(10)
    logger.info("Ollama reiniciado.")
