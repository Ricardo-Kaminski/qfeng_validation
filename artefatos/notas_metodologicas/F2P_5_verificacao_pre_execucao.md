# F2P.5 — Verificação Forense Pré-Execução Frente 2

**Data:** 27/abr/2026, ~19h UTC-3
**Branch:** caminho2
**Auditoria realizada ANTES de qualquer chamada LLM**

---

## Checklist de Integridade

| # | Item | Status |
|---|------|--------|
| 1 | SHA pré-registro original (`4c24e14`) preservado | ✅ |
| 2 | SHA emenda (`6d2f8ae`) registrada no §11.0 do pré-registro | ✅ |
| 3 | `test_h3_anova_interaction.py` reformulado: `p > 0.0083 → H3 supported` | ✅ |
| 4 | Smoke test H3 decisão invertida passa | ✅ `p>alpha (0.0083) => H3 supported` |
| 5 | `test_h5_bootstrap_overlap.py` criado paralelo ao Levene | ✅ |
| 6 | Smoke test H5b sintético passa (6/6 pares sobrepostos) | ✅ |
| 7 | `run_confirmatory_analysis.py` lista 7 hipóteses (H1-H6 + H5b) | ✅ |
| 8 | `results/raw_responses/` pristine — 0 arquivos | ✅ |
| 9 | Emenda §11 commitada antes de qualquer chamada LLM | ✅ |
| 10 | `evaluators/`, `scenarios/`, `prompts/`, `runners/` intocados pela emenda | ✅ |

---

## Cadeia de Commits da Emenda

```
4c24e14  frente2-a4: pre-registro OSF-style (ANTES de qualquer execucao LLM)
6d2f8ae  frente2-emenda: alinhamento estatistico-editorial H3+H5b pre-execucao
46e1f12  frente2-emenda: registrar SHA da emenda na secao 11.0
```

---

## Sumário das Mudanças

- **H3 reformulada:** `p > 0.05/6 = 0.0083` → H3 sustentada (cross-arch invariance).
  Direção única e falsificável; semântica alinhada ao agnosticismo de stack ML.

- **H5b adicionada:** bootstrap IC95% percentile pareado por cenário (1.000 iter).
  Critério: ≥5/6 pares de arquiteturas com ICs sobrepostos → H5b sustentada.
  H5 (Levene) preservada como análise complementar.

- **7 hipóteses confirmatórias:** H1, H2, H3, H4, H5 (complementar), H5b (primário), H6.

---

## Status: ✅ Pronto para `run_full_experiment.py` (Task 10)

Despacho autorizado apenas com confirmação explícita do autor.
