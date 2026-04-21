# Estado do PoC — Snapshot v2 — 19 abril 2026
## Verificação real do filesystem + execuções confirmadas

> ⚠️ Este documento substitui `ESTADO_19abr2026.md`, que continha estado pré-implementação.
> O estado real é significativamente mais avançado do que o snapshot anterior indicava.

---

## Estado dos módulos (verificado)

| Módulo | Pasta | Código | Fase A (pytest) | Fase B (corpus) | Aprovado |
|--------|-------|--------|----------------|-----------------|---------|
| **E0 ScopeConfig** | ❌ Ausente | ❌ | ❌ | ❌ | ❌ |
| **E1 Ingestion** | ✅ | ✅ Completo | ✅ (99 pass) | ✅ Executado | ⚠️ Pendente re-exec pós-E0 |
| **E2 Deontic** | ✅ | ✅ Completo | ✅ (99 pass) | ✅ Executado | ⚠️ Pendente aprovação |
| E3 Translation | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| E4 HITL | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| E5 Symbolic Testing | ✅ (stub) | ❌ | 🔒 | 🔒 | 🔒 |
| C1 Integration CLI | — | ❌ | 🔒 | 🔒 | 🔒 |

**Testes:** test_core 21/21 ✅ | test_e1+e2 99/99 ✅ | Total: 120/120

---

## Outputs gerados

### E1 (outputs/e1_chunks/)
- brasil/: 17 docs | eu/: 3 docs | usa/: 9 docs
- Total: 27.957 NormChunks | 347 pares de concorrência
- concurrency_map.json + e1_report.md

### E2 (outputs/deontic_cache/ + outputs/e2_report.md)
- 5.136 DeonticAtoms | confidence média 0,930 | 0 abaixo de 0,5
- Brasil: 3.206 | EU: 1.101 | USA: 829
- 3.163 arquivos JSON em cache

---

## Estado do corpus (atualizado nesta sessão)

| Regime | Status | Novos arquivos |
|--------|--------|---------------|
| Brasil | ✅ COMPLETO | portaria_69_2021.htm, portaria_197_2021.htm, portaria_268_2021.htm |
| EU | ✅ COMPLETO | — |
| USA | ✅ COMPLETO para MVP | obermeyer_2019_summary.md |

---

## Documentação acadêmica gerada (docs/)

| Arquivo | Conteúdo |
|---------|---------|
| docs/shared/corpus_preparation.md | Metodologia de construção do corpus, gap analysis, protocolo de obtenção |
| docs/shared/e2_evaluation.md | Avaliação formal do E2 (aguarda aprovação) |
| docs/shared/corpus_description.md | Atualizado com portarias e Obermeyer |
| docs/paper2_health/methodology.md | Case 2 (USA/Obermeyer) documentado |
| docs/README.md | Status table atualizado |

---

## Decisões arquiteturais confirmadas

| Decisão | Escolha | Razão |
|---------|---------|-------|
| Motor simbólico | Clingo ASP | Preserva primazia simbólica; dPASP rejeitado |
| Persistência MVP | JSON/filesystem | Neo4j fora do MVP |
| Orquestração MVP | Chamadas diretas | LangGraph fora do MVP |
| LLM backbone | litellm → claude-sonnet-4-6 | Agnóstico de provider |
| HITL interface | Jupyter Notebook | Streamlit como alternativa |
| Concorrência | concurrency_map.json externo | Preserva contrato schemas.py |
| E0 retroativo | Implementar antes de E3 | Necessário para reutilização do pipeline |

---

## Próxima sessão — Plano acordado

1. **Implementar E0** (ScopeConfig) com fluxo completo de skills:
   `superpowers:brainstorming → writing-plans → test-driven-development → executing-plans`
2. Re-executar E1 com ScopeConfig formal → Fase B E1 aprovada
3. Fase B E2 aprovada (revisão de amostra de DeonticAtoms com usuário)
4. Iniciar E3 (Translation → Clingo predicates)

---

## Alertas resolvidos (do snapshot anterior)

- ~~mempalace.yaml referencia pessoal\ em vez de academico\~~ — path real é academico/
- ~~MILA_FORM_FIELDS na raiz~~ — arquivos de outra candidatura, em artefatos/aplicacao_mila/
- ~~E1/E2 listados como stubs~~ — ambos implementados e executados com sucesso
