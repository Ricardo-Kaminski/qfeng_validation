# Q-FENG Validation — Academic Documentation

Documentação técnica e acadêmica acumulada durante a validação empírica do Q-FENG.
Serve de base para dois papers derivados.

## Estrutura

```
docs/
  README.md                     ← este arquivo
  paper1_ai_engineering/        ← Paper 1: engenharia de IA / ciência de dados
    methodology.md              ← metodologia técnica acumulada
    results.md                  ← resultados por etapa (E1→E5)
    related_work.md             ← literatura relacionada
    figures/                    ← diagramas, tabelas, gráficos
  paper2_health/                ← Paper 2: saúde digital / Lancet Digital
    methodology.md
    results.md
    related_work.md
    figures/
  shared/                       ← conteúdo compartilhado entre os dois papers
    corpus_description.md       ← descrição formal do corpus normativo (atualizado 19/abr)
    corpus_preparation.md       ← metodologia de construção e gap analysis do corpus ✨
    e1_evaluation.md            ← avaliação formal do E1 ✅ APROVADO
    e2_evaluation.md            ← avaliação formal do E2 ⚠️ aguarda aprovação ✨
    architecture.md             ← descrição da arquitetura Q-FENG
```

## Status por etapa

| Etapa | Status | Documentado |
|-------|--------|-------------|
| Corpus | ✅ Completo para MVP | ✅ corpus_description.md + corpus_preparation.md |
| E0 ScopeConfig | 🔨 Em implementação | — |
| E1 Ingestion | ✅ Executado | ✅ e1_evaluation.md (aprovação formal pendente re-exec pós-E0) |
| E2 Deontic Extraction | ✅ Executado | ✅ e2_evaluation.md (aprovação formal pendente) |
| E3 Translation | 🔒 Bloqueado | — |
| E4 Validation (HITL) | 🔒 Bloqueado | — |
| E5 Symbolic Testing | 🔒 Bloqueado | — |

## Última atualização: 19 abril 2026

Sessão de curadoria: corpus Brasil completado (portarias 69/197/268/2021),
corpus USA empirical criado (obermeyer_2019_summary.md). Decisão: implementar
E0 ScopeConfig antes de avançar para E3.
