# P1.5 — Setup do Extrator Claude Sonnet

**Data:** 29/abr/2026

## Estrutura criada

```
src/qfeng/extractor/
├── __init__.py           ← exports públicos
├── schema.py             ← ScenarioExtraction (Pydantic v2) + render_to_asp
├── cache.py              ← store/get/status (idempotente, sem TTL)
├── prompt_template.md    ← instrução para Claude Sonnet
└── claude_extractor.py   ← extract_facts + extract_facts_batch

corpora_clingo/extracted_facts/
└── .gitkeep              ← diretório vazio (fatos extraídos em P_FASE2)
```

## Decisão arquitetônica

Extrator como componente Q-FENG dedicado, não como função inline do runner.
Claude Sonnet (`claude-sonnet-4-6`) via Anthropic API, escolhido por:
- Structured output confiável (JSON schema via Pydantic)
- Independência do modelo do braço (Qwen/Phi/Gemma/Llama não extraem fatos)
- Custo proporcional: ~50 cenários × ~1K tokens ≈ $0.05 total

## Modelo Claude

String exata de model_id: `claude-sonnet-4-6`

## Política de cache

- Um arquivo `.lp` por `scenario_id` em `corpora_clingo/extracted_facts/`
- Um arquivo `_meta.json` correspondente com tokens, latência, confiança
- Sem TTL — fatos são estáveis (o cenário não muda entre sessões)
- `skip_cached=True` por padrão em `extract_facts_batch`

## Variável de ambiente

`ANTHROPIC_API_KEY` — adicionada ao `.env` como placeholder.
Preencher com chave real antes de P_FASE2.

## Verificação

```
OK: extractor module importa, cache vazio.
OK: schema + render funcionam.
anthropic 0.97.0 instalado em env qfeng.
```

## Não chamado ainda

A primeira chamada real à API ocorrerá em P_FASE2.
P_FASE1.5 apenas monta a estrutura.
