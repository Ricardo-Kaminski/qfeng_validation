# OP2.1 — Auditoria de impacto pré-Opção 2

**Data:** 27/abr/2026 | **Branch:** caminho2

## Achados

| Item | Valor |
|------|-------|
| Total SEs (pré-OP2) | 74 |
| SEs com TOH=0 | 4 |
| Competências afetadas | 202010, 202011, 202012, 202013 |
| θ_efetivo nas 4 SEs | 115,27° (inicialização Markoviana) |
| Regime nas 4 SEs | HITL (todas) |
| Primeira SE em CB | 202037 (SE 37/2020) |
| CB em SEs removidas? | Não |

## Impacto esperado pós-OP2

| Métrica | Pré-OP2 | Pós-OP2 |
|---------|---------|---------|
| n SEs | 74 | 70 |
| HITL | 48 | 44 |
| CB | 26 | 26 (preservado) |
| ΔSE_HITL | 46 | 42 |
| ΔSE_CB_estável | 19 | 19 (preservado) |

## Conclusão

As 4 SEs descartadas têm TOH=0 por consolidação tardia do DEMAS-VEPI e
θ_efetivo artefatual (115,27° = valor de inicialização, sem ancoragem operacional real).
A primeira ativação CB (SE 37/2020) está 23 SEs após o início da série canônica —
não é afetada pelo truncamento.
