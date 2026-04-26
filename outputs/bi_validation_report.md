# BI Bivariado Manaus — Relatório de Validação Cruzada

**Data:** 2026-04-26
**Branch:** caminho2
**Commits Tarefa 1.1–1.3:** 236a4ea / 96b8bb9 / cd465b6

## 1. Séries Ativas

| Série | Meses | Confirmados | Estimados | Stub | Fonte primária |
|-------|-------|-------------|-----------|------|----------------|
| TOH UTI | 12 | 10 | 2 | Não | FVS-AM / SES-AM / Fiocruz |
| SRAG Manaus | 12 | 0 | 0 | **Sim** | SIVEP-Gripe INFLUD20/21 (pendente) |

**SRAG stub ativo** — INFLUD20/21 não baixados (FTP DATASUS migrado para OpenDataSUS).
Fonte: opendatasus.saude.gov.br/dataset/srag-2020 e srag-2021.

## 2. Correlação de Spearman

| Par | ρ | Esperado | Status |
|-----|---|----------|--------|
| TOH vs SRAG | NaN (SRAG stub) | > 0.50 | PENDENTE (stub) |

## 3. Sanity Checks — Pico e Vale

| Check | Resultado | Status |
|-------|-----------|--------|
| Pico TOH em jan/fev 2021 | 2021-01 | OK |
| Vale TOH em jul/ago 2020 | 2020-08 | OK |

## 4. Outliers (|z| > 2.5)

SRAG: serie constante (stub), z-score indeterminado

## 5. PCA Empírica (sanity check de pesos)

**Indisponível** — SRAG stub com variância zero.

## 6. Decisão Final de Pesos

| Método | w_TOH | w_SRAG |
|--------|-------|--------|
| A priori (ficha técnica MS) | 0.5 | 0.5 |
| PCA empírica | N/A (stub) | N/A (stub) |
| **Decisão final** | **0.5** | **0.5** |

**weights_decision_pending:** True
**Método:** apriori_only_stub_srag

> Rationale: Pesos a priori 50/50 refletem paridade institucional entre TOH UTI (ficha técnica
> MS) e SRAG (vigilância epidemiológica oficial SIVEP-Gripe). PCA empírica como sanity check;
> divergência tolerada até |Δw|<0.10. Decisão final após SRAG dados reais.

## 7. Diagnóstico Bug t_mort=0

**Resultado:** t_mort=0 BUG CONFIRMED: MORTE column is numeric but all zeros. The microdatasus process_sih() function labels MORTE as Sim/Nao; if the raw DBC had MORTE=0 (numeric) and process_sih labeled it as '0' string, the subsequent to_numeric conversion correctly yields 0 for all rows. Root cause: raw SIH DBC MORTE field encodes only inpatient death at discharge (MORTE=1 only when COBRANCA=alta=obito, not when obito=sim in AIH header). Fix requires: reload from raw DBC, apply correct MORTE field mapping.

Detalhes completos em `outputs/diagnostico_t_mort_zero.md`.

## 8. Recomendações para Fase 2

1. **Baixar INFLUD20/21** de opendatasus.saude.gov.br e re-executar `extract_srag_manaus.py`
2. **Re-executar este script** para calcular Spearman real e validar |Δw| PCA
3. **Corrigir bug t_mort=0** no SIH parquet antes da regeneração da Tabela 7
4. **Confirmar pesos finais** (atualmente pendentes) após SRAG dados reais
