# Manaus BI Bivariado — Provenance Manifest

**Projeto:** Q-FENG Caminho 2 — BI multi-fonte
**Período:** Jul/2020 – Jun/2021 (12 meses)
**Branch:** caminho2 | **Commits:** 236a4ea (1.1), 96b8bb9 (1.2), cd465b6 (1.3)

## Dimensões ativas

| Dimensão | Arquivo | Status | Fonte primária |
|----------|---------|--------|----------------|
| TOH UTI | `toh_uti_manaus.parquet` | Ativo (10 confirmados, 2 estimados) | FVS-AM / SES-AM / Fiocruz |
| SRAG | `srag_manaus.parquet` | **STUB** (aguarda INFLUD20/21) | SIVEP-Gripe OpenDataSUS |
| O₂ supply | `oxigenio_unavailable.json` | Caminho C — prospectivo-only | — |

## TOH UTI (`toh_uti_manaus.parquet`)

Schema: `year, month, competencia, toh_uti_pct, source, source_doc, source_date,`
`is_estimated, estimation_method, raw_value_str, validation_status, tabnet_delta_pp, toh_sih_proxy_pct`

Fonte: `_TOH_FVS_AM` em `src/qfeng/e5_symbolic/manaus_sih_loader.py`
Extração: `scripts/build_toh_uti_manaus.py`
Validações: proxy SIH (case-mix UTI), sanity check jan/fev 2021 ≥85%

## SRAG Manaus (`srag_manaus.parquet`)

Schema: `year, month, competencia, n_srag_total, n_covid, n_outros, n_obitos, letalidade_pct, source, is_stub`

Extração: `scripts/extract_srag_manaus.py`
Fonte original: SIVEP-Gripe INFLUD20/21 (OpenDataSUS)
**Status: STUB** — baixar INFLUD20/21 manualmente e re-executar `extract_srag_manaus.py`
Download: opendatasus.saude.gov.br/dataset/srag-2020 e srag-2021

## Decisão O₂ — Caminho C

Arquivo: [`oxigenio_unavailable.json`](oxigenio_unavailable.json)

Decisão: sem dado retrospectivo canônico viável para O₂ Manaus 2020-2021.
BI permanece **bivariado** (TOH + SRAG). O₂ entra como limitação prospectiva no §7.4.

## Pesos do score_pressao

Decisão em [`outputs/bi_dimensional_decision.json`](../../outputs/bi_dimensional_decision.json)
A priori: w_TOH = 0.50 / w_SRAG = 0.50 (paridade institucional)
**weights_decision_pending: True** — re-executar após SRAG dados reais.

## Tabela de Provenance

| competencia | TOH source | TOH status | SRAG status |
|-------------|------------|------------|-------------|
| 2020-07 | FVS-AM/SES-AM (nota 07/ago/2020) | confirmed | STUB |
| 2020-08 | FVS-AM Boletim 18/ago/2020 | confirmed | STUB |
| 2020-09 | Fiocruz SE40-42 | estimated | STUB |
| 2020-10 | SUSAM 27/out/2020 | confirmed | STUB |
| 2020-11 | Fiocruz SE48-49 | confirmed | STUB |
| 2020-12 | SES-AM Plano Contingencia | confirmed | STUB |
| 2021-01 | FVS-AM Boletim 16/jan/2021 | confirmed | STUB |
| 2021-02 | SES-AM 04/fev/2021 | confirmed | STUB |
| 2021-03 | Fiocruz 08/mar/2021 | confirmed | STUB |
| 2021-04 | FVS-AM Boletim Risco abr/2021 | confirmed | STUB |
| 2021-05 | FVS-AM Boletim Risco mai/2021 | confirmed | STUB |
| 2021-06 | estimado por interpolação | estimated | STUB |

## Bug t_mort=0 (não bloqueante para BI)

MORTE no SIH parquet é todo zero (encoding error). Detalhes em
`outputs/diagnostico_t_mort_zero.md`. Não afeta TOH nem SRAG. Corrigir na Fase 2.
