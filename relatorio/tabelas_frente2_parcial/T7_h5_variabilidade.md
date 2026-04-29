# T7 — H5: Variabilidade Intra-(Modelo, Cenário): Levene + Bootstrap

## H5a — Teste de Levene

| Comparação | Var. média B3 | Var. média outro braço | Estatística Levene | p-value | Sig.? | B3 menor variância? |
| ---------- | ------------- | ---------------------- | ------------------ | ------- | ----- | ------------------- |
| B3 vs B1 | 0.028 | 0.080 | 18.376 | 2.277e-05 * | Sim * | Sim |
| B3 vs B2 | 0.028 | 0.062 | 8.707 | 3.357e-03 * | Sim * | Sim |
| B3 vs B4 | 0.028 | 0.005 | 10.536 | 1.270e-03 * | Sim * | Não |

## H5b — Sobreposição de IC95% (Bootstrap)

| N pares (modelo, cenário) | Sem sobreposição IC95% | Fração sem sobreposição | Interpretação |
| ------------------------- | ---------------------- | ----------------------- | ------------- |
| 200 | 11 | 5.5% | IC95%(B3) e IC95%(B1) sem sobreposição em 5.5% dos 200 pares (modelo, cenário). |

**Interpretação geral:** Var intra média: B1=0.0800, B2=0.0617, B3=0.0283, B4=0.0050. Levene B3 vs B1: p=2.277e-05 (sig.). Bootstrap overlap: B3/B1 sem sobreposição em 5.5% dos pares.
