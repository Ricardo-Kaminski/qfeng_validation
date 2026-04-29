# P_FASE1.5b — Ajuste para passthrough manual

**Data:** 29/abr/2026
**Sessão:** chat Opus 4.7 (continuação da sessão de redesenho B3/B4/B5)
**Origem:** o Claude Code, ao executar a P_FASE1, leu a versão **inicial** do briefing `PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md` (que ainda especificava cliente Anthropic API). O ajuste in-place do briefing para passthrough manual foi sincronizado **depois** da execução, gerando divergência. A P_FASE1.5b corrige a divergência sem refazer a P_FASE1 inteira.

## Contexto

A **Decisão 2** do Ricardo (29/abr/2026) migrou a operacionalização do extrator de fatos de "Claude Sonnet via Anthropic API com cache" para "passthrough manual via Claude Opus 4.7 em sessão supervisionada". Justificativa: ausência de créditos API + ganho epistemológico de rastro humano-no-loop verificável (alinhado com VSM, Pineau et al. 2021 sobre reprodutibilidade em sistemas neurosimbólicos).

O briefing P_FASE1 foi ajustado in-place para refletir esta decisão (P1.5 reescrita; P1.6, P1.7 ajustadas), mas o Code processou a versão pré-ajuste. Resultado:

```
src/qfeng/extractor/
├── __init__.py            # Importa claude_extractor (não funcional sem `anthropic`)
├── cache.py               # Funcional, mas com bug: parents[4] aponta para fora do projeto
├── claude_extractor.py    # ❌ Cliente Anthropic API — não será usado
├── prompt_template.md     # ❌ Template de prompt API — substituído pelo Apêndice A do P_FASE2.0
├── schema.py              # Funcional, mas sem campos de rastreabilidade humano-no-loop
└── __pycache__/
```

## Operações executadas

### 1. Arquivamento

`claude_extractor.py` e `prompt_template.md` movidos para `src/qfeng/extractor/_archive_pre_passthrough/` com `README.md` explicativo. Política: arquivar (não deletar) para auditoria forense + reprodutibilidade futura caso créditos API sejam repostos.

### 2. Reescrita de `__init__.py`

Removidas importações de `claude_extractor` (`extract_facts`, `extract_facts_batch`). Pacote público agora exporta apenas:

- `FactAtom`, `ScenarioExtraction`, `render_to_asp` (de `schema.py`)
- `get_cached_facts`, `store_cached_facts`, `cache_status` (de `cache.py`)

Docstring atualizado com decisão arquitetônica e referência ao `_archive_pre_passthrough/README.md`.

### 3. Extensão de `schema.py`

Adicionados três campos a `ScenarioExtraction` para rastreabilidade humano-no-loop:

- `extractor_model: str = "claude-opus-4-7-passthrough"` (default identifica operacionalização)
- `extractor_session_id: str = ""` (preenchido pela sessão de chat)
- `supervised_by: str = ""` (especialista supervisor, e.g., Ricardo + ORCID)

Mantidos campos legados (`model_used`, `tokens_in`, `tokens_out`) com docstring DEPRECATED para compatibilidade.

`render_to_asp` atualizado para incluir `% Supervisor:` e `% Sessao:` nos comentários do `.lp` quando preenchidos.

### 4. Correção de bug em `cache.py`

`parents[4]` apontava para `C:\Workspace\academico\` (fora do projeto). Estrutura real:

```
src/qfeng/extractor/cache.py
   parents[0] = src/qfeng/extractor
   parents[1] = src/qfeng
   parents[2] = src
   parents[3] = qfeng_validacao  ← workspace root
```

Corrigido para `parents[3]`. Pasta errada (`C:\Workspace\academico\corpora_clingo\`) removida via `rmdir /S /Q`.

### 5. Smoke test

Validações executadas com sucesso:

- Imports do pacote público passam
- `extract_facts` (do claude_extractor arquivado) **não** mais exposto (correto)
- `cache_status` aponta para `C:\Workspace\academico\qfeng_validacao\corpora_clingo\extracted_facts` (correto)
- Render ASP normal e abstain produzem output esperado, com cabeçalhos de rastreabilidade
- Round-trip cache (store → get → cleanup) funciona

## Estado pós-correção

```
src/qfeng/extractor/
├── __init__.py            # Reescrito: 4 símbolos públicos (sem claude_extractor)
├── cache.py               # Corrigido parents[3]
├── schema.py              # Estendido com extractor_session_id, supervised_by, extractor_model
├── _archive_pre_passthrough/
│   ├── README.md          # Explica arquivamento
│   ├── claude_extractor.py
│   └── prompt_template.md
└── __pycache__/
```

## Próximo passo

P_FASE2.0 (extração manual via passthrough) executável agora conforme `artefatos/briefings/PROTOCOLO_P_FASE2_0_EXTRACAO_MANUAL_PASSTHROUGH.md`. Cache aponta para o caminho correto, schema tem campos de rastreabilidade, `__init__` não importa código quebrado.

## Commit

```
frente2-p-fase1-5b: ajuste passthrough manual (arquiva claude_extractor + corrige parents)
```

Mudanças isoladas em `src/qfeng/extractor/*` e `artefatos/notas_metodologicas/P_FASE1_5b_*.md`. Não tocar em outras pendências de `git status` (B5.9, dashboards, briefings antigos) — escopo cirúrgico.
