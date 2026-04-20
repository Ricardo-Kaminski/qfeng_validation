"""E2 deontic extractor — LLM-powered extraction of DeonticAtoms from NormChunks.

Uses litellm for LLM calls with caching, exponential backoff,
and concurrency context enrichment.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import time
from pathlib import Path
from typing import Any

import litellm
from dotenv import load_dotenv

from qfeng.c1_digestion.deontic.few_shots import get_few_shots

load_dotenv()
from qfeng.c1_digestion.deontic.prompts import SYSTEM_PROMPT, render_user_prompt
from qfeng.core.schemas import (
    DeonticAtom,
    DeonticCondition,
    DeonticModality,
    NormativeStrength,
    NormChunk,
)

logger = logging.getLogger(__name__)

_DEFAULT_MODEL = "anthropic/claude-sonnet-4-20250514"
_DEFAULT_CACHE_DIR = Path("outputs/deontic_cache")
_MAX_RETRIES = 3
_BASE_BACKOFF = 2.0


def extract_deontic(
    chunk: NormChunk,
    cache_dir: Path | None = None,
    concurrent_chunks: list[NormChunk] | None = None,
    model: str | None = None,
) -> list[DeonticAtom]:
    """Extrai DeonticAtoms de um NormChunk via LLM.

    Verifica cache antes de chamar o LLM. Se o resultado já existe
    em ``cache_dir/{chunk.id}.json``, retorna diretamente.

    Args:
        chunk: NormChunk a processar.
        cache_dir: Diretório de cache. Default: ``outputs/deontic_cache/``.
        concurrent_chunks: Chunks concorrentes para enriquecer o contexto.
        model: Model ID para litellm. Default: env QFENG_LLM_MODEL.

    Returns:
        Lista de DeonticAtoms extraídos.
    """
    cache_dir = cache_dir or _DEFAULT_CACHE_DIR
    cache_path = cache_dir / f"{chunk.id}.json"

    # Cache hit
    if cache_path.exists():
        logger.debug("Cache hit: %s", chunk.id)
        return _load_cache(cache_path, chunk.id)

    # Preparar prompt
    model = model or os.environ.get("QFENG_LLM_MODEL", _DEFAULT_MODEL)
    concurrent_texts = _build_concurrent_context(concurrent_chunks)

    user_prompt = render_user_prompt(
        source=chunk.source,
        regime=chunk.regime.value,
        hierarchy=" > ".join(chunk.hierarchy),
        chunk_type=chunk.chunk_type,
        language=chunk.language,
        text=chunk.text,
        concurrent_texts=concurrent_texts,
    )

    few_shots = get_few_shots(chunk.regime.value)
    full_system = SYSTEM_PROMPT
    if few_shots:
        full_system = f"{SYSTEM_PROMPT}\n\n{few_shots}"

    # Chamar LLM com retry
    raw_response = _call_llm_with_retry(model, full_system, user_prompt)
    atoms = _parse_response(raw_response, chunk)

    # Salvar cache
    _save_cache(cache_path, atoms)

    logger.info(
        "%s (%s): %d atoms extraídos",
        chunk.source,
        " > ".join(chunk.hierarchy),
        len(atoms),
    )
    return atoms


def _call_llm_with_retry(
    model: str,
    system_prompt: str,
    user_prompt: str,
) -> str:
    """Chama o LLM com exponential backoff em caso de rate limit.

    Args:
        model: Model ID para litellm.
        system_prompt: System prompt completo (com few-shots).
        user_prompt: User prompt renderizado.

    Returns:
        Resposta do LLM como string.

    Raises:
        RuntimeError: Se todas as tentativas falharem.
    """
    for attempt in range(_MAX_RETRIES):
        try:
            temperature = float(os.environ.get("QFENG_LLM_TEMPERATURE", "0.1"))
            max_tokens = int(os.environ.get("QFENG_LLM_MAX_TOKENS", "4096"))
            response = litellm.completion(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            content = response.choices[0].message.content
            if content is None:
                msg = "LLM retornou resposta vazia"
                raise RuntimeError(msg)
            return content
        except Exception as exc:
            error_str = str(exc).lower()
            is_rate_limit = "rate" in error_str or "429" in error_str
            if is_rate_limit and attempt < _MAX_RETRIES - 1:
                wait = _BASE_BACKOFF ** (attempt + 1)
                logger.warning(
                    "Rate limit (tentativa %d/%d), aguardando %.1fs",
                    attempt + 1,
                    _MAX_RETRIES,
                    wait,
                )
                time.sleep(wait)
                continue
            raise

    msg = f"LLM falhou após {_MAX_RETRIES} tentativas"
    raise RuntimeError(msg)


def _parse_response(raw: str, chunk: NormChunk) -> list[DeonticAtom]:
    """Parseia a resposta JSON do LLM em DeonticAtoms.

    Args:
        raw: Resposta bruta do LLM (esperado: JSON array).
        chunk: NormChunk de origem (para traceability).

    Returns:
        Lista de DeonticAtoms validados.
    """
    # Extrair JSON da resposta (pode ter markdown fences)
    json_str = _extract_json(raw)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        logger.warning(
            "JSON inválido do LLM para chunk %s: %s",
            chunk.id,
            raw[:200],
        )
        return []

    if not isinstance(data, list):
        data = [data]

    atoms: list[DeonticAtom] = []
    for i, item in enumerate(data):
        try:
            atom = _dict_to_atom(item, chunk, i)
            atoms.append(atom)
        except (KeyError, ValueError) as exc:
            logger.warning(
                "Atom inválido para chunk %s (item %d): %s",
                chunk.id,
                i,
                exc,
            )

    return atoms


def _dict_to_atom(item: dict[str, Any], chunk: NormChunk, index: int) -> DeonticAtom:
    """Converte um dict da resposta LLM em DeonticAtom validado."""
    # Gerar ID determinístico
    atom_id = hashlib.sha256(
        f"{chunk.id}:{index}:{item.get('action', '')}".encode()
    ).hexdigest()[:16]

    # Parsear conditions
    conditions: list[DeonticCondition] = []
    for cond in item.get("conditions") or []:
        if isinstance(cond, dict) and "variable" in cond:
            conditions.append(DeonticCondition(
                variable=cond["variable"],
                operator=cond.get("operator", "=="),
                value=str(cond.get("value", "")),
            ))

    # Validar modality
    modality_str = item.get("modality", "obligation")
    try:
        modality = DeonticModality(modality_str)
    except ValueError:
        modality = DeonticModality.OBLIGATION

    # Validar strength
    strength_str = item.get("strength", "statutory")
    try:
        strength = NormativeStrength(strength_str)
    except ValueError:
        strength = NormativeStrength.STATUTORY

    # Validar confidence
    confidence = item.get("confidence", 0.8)
    if not isinstance(confidence, (int, float)):
        confidence = 0.8
    confidence = max(0.0, min(1.0, float(confidence)))

    return DeonticAtom(
        id=atom_id,
        source_chunk_id=chunk.id,
        modality=modality,
        agent=str(item.get("agent", "unknown")),
        patient=str(item.get("patient", "unknown")),
        action=str(item.get("action", "unknown")),
        conditions=conditions,
        threshold=item.get("threshold"),
        consequence=item.get("consequence"),
        temporality=str(item.get("temporality", "unconditional")),
        strength=strength,
        confidence=confidence,
    )


def _extract_json(text: str) -> str:
    """Extrai conteúdo JSON de texto que pode conter markdown fences."""
    # Tentar extrair de ```json ... ```
    m = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Tentar encontrar array JSON diretamente
    m = re.search(r"\[.*\]", text, re.DOTALL)
    if m:
        return m.group(0)
    return text.strip()


def _build_concurrent_context(
    concurrent_chunks: list[NormChunk] | None,
) -> list[dict[str, str]]:
    """Constrói contexto de chunks concorrentes para o prompt."""
    if not concurrent_chunks:
        return []
    return [
        {
            "source": c.source,
            "hierarchy": " > ".join(c.hierarchy),
            "text": c.text,
        }
        for c in concurrent_chunks[:3]  # Limitar a 3 para não estourar contexto
    ]


def _load_cache(path: Path, chunk_id: str) -> list[DeonticAtom]:
    """Carrega DeonticAtoms do cache JSON."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return [DeonticAtom.model_validate(item) for item in data]
    except Exception as exc:
        logger.warning("Cache corrompido para %s: %s", chunk_id, exc)
        return []


def _save_cache(path: Path, atoms: list[DeonticAtom]) -> None:
    """Salva DeonticAtoms no cache JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [atom.model_dump(mode="json") for atom in atoms]
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
