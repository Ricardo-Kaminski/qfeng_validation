# Arquivamento `claude_extractor.py` + `prompt_template.md`

**Data:** 29/abr/2026
**Razão:** decisão arquitetônica final na sessão de 29/abr/2026 — extração de fatos será executada por **passthrough manual** (Claude Opus 4.7 em sessão de chat supervisionada pelo Ricardo, com Desktop Commander), **não** por chamada à Anthropic API.

## Origem

Os arquivos `claude_extractor.py` (cliente Anthropic API) e `prompt_template.md` (template com placeholders `[VOCABULARY_INJECTED_HERE]`, `[SCENARIO_TEXT_INJECTED_HERE]`, etc.) foram criados pelo Claude Code durante a execução da P_FASE1, seguindo a versão **inicial** do briefing `PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md`.

A versão final do briefing — ajustada in-place pela sessão chat (Opus 4.7) imediatamente após a Decisão 2 do Ricardo migrar de "Claude Sonnet via API" para "passthrough manual via Claude Opus 4.7" — removeu a especificação destes dois arquivos. O ajuste foi sincronizado **depois** do Code já ter executado a P1.5, gerando esta divergência.

## Status atual

- **`claude_extractor.py`** importa `anthropic` (não instalado em `qfeng` env) e chama `client.messages.create(model="claude-sonnet-4-6", ...)`. **Não funcional** no estado atual e **não será usado**.
- **`prompt_template.md`** é uma referência útil mas não é mais necessária — o protocolo `PROTOCOLO_P_FASE2_0_EXTRACAO_MANUAL_PASSTHROUGH.md` (Apêndice A) contém a versão atualizada do framing cognitivo da extração.

## Por que arquivar e não deletar

1. Auditoria forense — preserva o caminho completo de decisões editoriais da Frente 2.
2. Reprodutibilidade — se créditos API forem repostos no futuro e for desejável paralelizar a extração via API, este código serve de base.
3. Política de transparência — o paper documenta a operacionalização real, e o histórico arquivado permite verificar a divergência entre o briefing inicial e a operacionalização final.

## Estado pós-arquivamento

```
src/qfeng/extractor/
├── __init__.py           # Reescrito: sem importações de claude_extractor
├── cache.py              # Mantido (criado pelo Code, funcional)
├── schema.py             # Estendido: + extractor_session_id, + extractor_model com default 'claude-opus-4-7-passthrough'
├── _archive_pre_passthrough/
│   ├── README.md         # Este documento
│   ├── claude_extractor.py
│   └── prompt_template.md
```

## Operacionalização efetiva

A extração será executada conforme `artefatos/briefings/PROTOCOLO_P_FASE2_0_EXTRACAO_MANUAL_PASSTHROUGH.md`:
- Sessão de chat com Claude Opus 4.7 + Ricardo + Desktop Commander
- Output: `corpora_clingo/extracted_facts/{scenario_id}.lp` + `{scenario_id}_meta.json`
- Persistência via Desktop Commander, validação Pydantic em memória
- Sem dependência de `anthropic` package, sem variável `ANTHROPIC_API_KEY`

---

**Não restaurar** estes arquivos do arquivo sem revisão da decisão metodológica.
