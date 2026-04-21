# Artefatos — Q-FENG Validação
**Estrutura de suporte ao desenvolvimento via Claude Code + Claude.ai**

---

## Propósito desta pasta

Centraliza prompts, briefings e referências que articulam o trabalho entre:
- **Claude Code** (terminal) — implementação de código, execução de testes, debug
- **Claude.ai chat** (projeto "pos doc") — análise teórica, revisão de outputs, decisões arquiteturais

---

## Estrutura de subpastas

```
artefatos/
├── README.md                          ← este arquivo
├── BRIEFING_PONTE_producao_academica.md  ← contexto do livro/papers para este projeto
│
├── prompts_claude_code/               ← prompts prontos para colar no Claude Code
│   ├── 00_inicializacao.md            ← prompt de inicialização (executar SEMPRE)
│   ├── E0_scope_config.md             ← prompt para implementar MODULE 0
│   ├── E1_ingestion.md                ← prompt para implementar MODULE 1
│   ├── E2_deontic.md                  ← (bloqueado até E1 aprovado)
│   ├── E3_translation.md              ← (bloqueado até E2 aprovado)
│   ├── E4_hitl.md                     ← (bloqueado até E3 aprovado)
│   └── E5_symbolic_testing.md         ← (bloqueado até E4 aprovado)
│
├── referencias_teoricas/              ← excertos e fichas do WP Q-FENG para uso no código
│   ├── qfeng_arquitetura_resumo.md    ← resumo dos 3 níveis + 5 canais
│   ├── tipologia_falhas.md            ← execução vs constitucional
│   └── clingo_predicates_spec.md      ← especificação dos predicados Clingo
│
└── estado_poc/                        ← snapshots do estado do PoC por sessão
    └── ESTADO_19abr2026.md            ← estado atual mapeado
```

---

## Fluxo de trabalho recomendado

1. **Abrir Claude Code** no diretório `C:\Workspace\academico\qfeng_validacao`
2. **Colar o prompt** de `artefatos/prompts_claude_code/00_inicializacao.md`
3. **Selecionar o módulo** a implementar e colar o prompt correspondente
4. **Trazer outputs** (relatórios, erros, dúvidas arquiteturais) para o chat Claude.ai
5. **Decisões de design** tomadas no chat → documentadas em `estado_poc/`
6. **Atualizar estado** após cada sessão produtiva

---

## Estado atual dos módulos (19/abr/2026)

| Módulo | Status | Fase A | Fase B |
|--------|--------|--------|--------|
| E0 — Scope Config | ⚠️ Pendente verificação | ? | ❌ |
| E1 — Ingestion | ⚠️ Stubs apenas | ❌ | ❌ |
| E2 — Deontic | 🔒 Bloqueado | ❌ | ❌ |
| E3 — Translation | 🔒 Bloqueado | ❌ | ❌ |
| E4 — HITL | 🔒 Bloqueado | ❌ | ❌ |
| E5 — Symbolic Testing | 🔒 Bloqueado | ❌ | ❌ |
| C1 — Integração | 🔒 Bloqueado | ❌ | ❌ |
