# Estado do PoC — Snapshot 19 abril 2026
## Gerado via mapeamento do filesystem + leitura do CLAUDE.md

---

## Localização do workspace

```
C:\Workspace\academico\qfeng_validacao\   ← workspace real (não pessoal\)
```

---

## Estrutura verificada em 19/abr/2026

```
qfeng_validacao/
├── CLAUDE.md                    ✅ Plano completo E0→E5 + regras de progressão
├── mempalace.yaml               ✅ Mapa de salas
├── pyproject.toml               ✅ Dependências configuradas
├── README.md                    ✅
├── .env / .env.example          ✅ (litellm API keys)
├── .gitignore                   ✅
│
├── src/qfeng/
│   ├── core/
│   │   ├── schemas.py           ✅ DONE — NÃO MODIFICAR
│   │   └── interference.py      ✅ DONE — NÃO MODIFICAR
│   └── c1_digestion/
│       ├── deontic/             ⚠️ Só __init__.py (stub)
│       ├── ingestion/           ⚠️ Só __init__.py (stub)
│       ├── testing/             ⚠️ Só __init__.py (stub)
│       ├── translation/         ⚠️ Só __init__.py (stub)
│       └── validation/          ⚠️ Só __init__.py (stub)
│       ⚠️ AUSENTE: scope/       ← E0 não implementado
│
├── corpora/
│   ├── CORPUS_MANIFEST.md       ✅
│   ├── brasil/                  ✅ Documentos baixados
│   ├── eu/                      ✅ Documentos baixados
│   └── usa/                     ✅ Documentos baixados
│
├── tests/
│   ├── test_core/               ✅ Completo
│   ├── test_e1/ → test_e5/      ⚠️ Vazios (só __init__.py)
│   ⚠️ AUSENTE: test_e0/         ← a criar junto com E0
│
├── outputs/                     ⚠️ Vazio (nenhuma execução real)
├── scripts/                     (utilitários de download)
│
└── artefatos/                   ✅ Criado nesta sessão
    ├── README.md
    ├── BRIEFING_PONTE_producao_academica.md
    ├── prompts_claude_code/
    │   ├── 00_inicializacao.md
    │   ├── E0_scope_config.md
    │   ├── E1_ingestion.md
    │   └── E2_E5_bloqueados.md
    ├── referencias_teoricas/
    │   ├── qfeng_arquitetura_resumo.md
    │   ├── tipologia_falhas.md
    │   └── clingo_predicates_spec.md
    └── estado_poc/
        └── ESTADO_19abr2026.md  ← este arquivo
```

---

## Estado dos módulos

| Módulo | Pasta existe? | Código? | Fase A (pytest) | Fase B (corpus real) | Aprovado? |
|--------|--------------|---------|-----------------|----------------------|-----------|
| **E0 ScopeConfig** | ❌ Ausente | ❌ | ❌ | ❌ | ❌ |
| **E1 Ingestion** | ✅ (stub) | ❌ | ❌ | ❌ | ❌ |
| E2 Deontic | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| E3 Translation | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| E4 HITL | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| E5 Symbolic Testing | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| C1 Integration | — | ❌ | 🔒 | 🔒 | 🔒 |

**Próximo passo imediato: implementar E0 (ScopeConfig)**
Prompt: `artefatos/prompts_claude_code/E0_scope_config.md`

---

## Corpora disponíveis (a verificar no Claude Code)

Manifesto em `corpora/CORPUS_MANIFEST.md` — verificar quais arquivos existem
de fato em cada subpasta antes de configurar sus_validacao.yaml.

Regimes esperados: brasil/, eu/, usa/

---

## Decisões arquiteturais canônicas

| Decisão | Escolha | Razão |
|---------|---------|-------|
| Motor simbólico | **Clingo ASP** | Preserva primazia simbólica |
| ~~dPASP~~ | Rejeitado | Inverte controle (neural sobre simbólico) |
| Persistência MVP | JSON/filesystem | Neo4j fora do MVP |
| Orquestração MVP | Chamadas diretas | LangGraph fora do MVP |
| LLM backbone | litellm (agnóstico) | claude-sonnet-4-6 por default |
| HITL interface | Jupyter Notebook | Streamlit como alternativa |
| Concorrência | concurrency_map.json externo | Preserva contrato de schemas.py |

---

## Alertas e pendências

- ⚠️ `mempalace.yaml` referencia `C:\Workspace\pessoal\qfeng_validacao` — verificar se precisa atualizar para path real `C:\Workspace\academico\qfeng_validacao`
- ⚠️ MILA_FORM_FIELDS.md e MILA_FORM_FIELDS_FINAL.md na raiz — arquivos de outra candidatura; não são parte do PoC, podem ser movidos para artefatos/ ou ignorados
- ⚠️ Verificar se `test_core/` passa com `pytest tests/test_core/ -v` antes de iniciar E0

---

## Próxima sessão recomendada

1. Abrir Claude Code em `C:\Workspace\academico\qfeng_validacao`
2. Colar `artefatos/prompts_claude_code/00_inicializacao.md`
3. Verificar estado real (pytest test_core, listar corpora)
4. Colar `artefatos/prompts_claude_code/E0_scope_config.md`
5. Implementar E0 Fase A (código + testes)
6. Reportar no chat Claude.ai para decisão sobre Fase B
