"""Extrator de fatos jurídicos via Claude Sonnet (Anthropic API).

Componente Q-FENG: converte cenário texto → predicados ASP para Clingo.
Cache idempotente: uma extração por scenario_id, sem TTL.

IMPORTANTE: não chamar a API em P_FASE1. Primeira chamada real em P_FASE2.
"""
from __future__ import annotations
import json
import os
import time
from pathlib import Path

from qfeng.extractor.cache import get_cached_facts, store_cached_facts
from qfeng.extractor.schema import FactAtom, ScenarioExtraction, render_to_asp

MODEL_ID = "claude-sonnet-4-6"
PROMPT_TEMPLATE_PATH = Path(__file__).parent / "prompt_template.md"

# Vocabulário de predicados por tipo de cenário (expandir em P_FASE2)
PREDICATE_VOCABULARY: dict[str, list[str]] = {
    "T-CLT-01": [
        "cita_sumula(N)",
        "fundamentacao_completa(bool)",
        "menciona_precedente_generico(bool)",
        "aborda_todos_argumentos(bool)",
        "acordao_id(id)",
    ],
    "T-CLT-02": [
        "aviso_previo_proporcional(bool)",
        "tempo_servico_anos(N)",
        "dispensa_sem_justa_causa(bool)",
        "indenizacao_calculada_corretamente(bool)",
    ],
    "T-CLT-03": [
        "horas_extras_registradas(bool)",
        "banco_horas_valido(bool)",
        "acordo_coletivo_presente(bool)",
        "intervalo_intrajornada_respeitado(bool)",
    ],
    "T-CLT-04": [
        "equiparacao_salarial_pleiteada(bool)",
        "identidade_funcional(bool)",
        "mesmo_empregador(bool)",
        "simultaneidade_comprovada(bool)",
    ],
}


def _load_prompt_template(scenario_type: str, scenario_text: str) -> str:
    template = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    vocab = PREDICATE_VOCABULARY.get(scenario_type, [])
    vocab_str = "\n".join(f"- `{p}`" for p in vocab) if vocab else "(nenhum vocabulário definido)"
    return (
        template
        .replace("{{scenario_type}}", scenario_type)
        .replace("{{predicate_vocabulary}}", vocab_str)
        .replace("{{scenario_text}}", scenario_text)
    )


def extract_facts(
    scenario_id: str,
    scenario_text: str,
    scenario_type: str,
    skip_cache: bool = False,
) -> tuple[ScenarioExtraction, str]:
    """Extrai fatos ASP de um cenário usando Claude Sonnet.

    Returns:
        (ScenarioExtraction, facts_lp): objeto estruturado e string .lp.

    Cache-hit: retorna fatos do cache sem chamar a API.
    """
    if not skip_cache:
        cached = get_cached_facts(scenario_id)
        if cached is not None:
            # Reconstruct minimal ScenarioExtraction from cached .lp
            extraction = ScenarioExtraction(
                scenario_id=scenario_id,
                scenario_type=scenario_type,
                facts=[],
                extraction_confidence=1.0,
                abstain=False,
                model_used="(from_cache)",
            )
            return extraction, cached

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY não definida. "
            "Adicionar ao .env antes de chamar o extrator."
        )

    # Lazy import — anthropic só é necessário em chamadas reais
    import anthropic  # noqa: PLC0415

    client = anthropic.Anthropic(api_key=api_key)
    prompt = _load_prompt_template(scenario_type, scenario_text)

    t0 = time.monotonic()
    response = client.messages.create(
        model=MODEL_ID,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    latency_ms = int((time.monotonic() - t0) * 1000)

    raw_text = response.content[0].text.strip()

    # Parse JSON response
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude retornou JSON inválido: {e}\nRaw: {raw_text[:500]}") from e

    facts = [
        FactAtom(
            predicate=f["predicate"],
            args=f.get("args", []),
            comment=f.get("comment", ""),
        )
        for f in data.get("facts", [])
    ]

    extraction = ScenarioExtraction(
        scenario_id=scenario_id,
        scenario_type=scenario_type,
        facts=facts,
        extraction_confidence=float(data.get("extraction_confidence", 0.5)),
        abstain=bool(data.get("abstain", False)),
        abstain_reason=data.get("abstain_reason", ""),
        model_used=MODEL_ID,
        tokens_in=response.usage.input_tokens,
        tokens_out=response.usage.output_tokens,
    )

    facts_lp = render_to_asp(extraction)

    meta = {
        "scenario_id": scenario_id,
        "scenario_type": scenario_type,
        "model": MODEL_ID,
        "latency_ms": latency_ms,
        "tokens_in": extraction.tokens_in,
        "tokens_out": extraction.tokens_out,
        "abstain": extraction.abstain,
        "confidence": extraction.extraction_confidence,
    }
    store_cached_facts(scenario_id, facts_lp, meta)

    return extraction, facts_lp


def extract_facts_batch(
    scenarios: list[dict],
    skip_cached: bool = True,
) -> dict[str, str]:
    """Extrai fatos para lista de cenários. Retorna {scenario_id: facts_lp}."""
    results: dict[str, str] = {}
    for s in scenarios:
        sid = s["scenario_id"]
        if skip_cached and get_cached_facts(sid) is not None:
            results[sid] = get_cached_facts(sid)  # type: ignore[assignment]
            continue
        _, facts_lp = extract_facts(sid, s["scenario_text"], s["scenario_type"])
        results[sid] = facts_lp
    return results
