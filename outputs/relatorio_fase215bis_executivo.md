# Relatório Executivo — Fase 2.1.5-bis
**Data:** 2026-04-27 | **Branch:** caminho2

---

## 1. Resumo

Esta fase refundou o TOH primário Manaus a partir de microdados oficiais MS:
DEMAS-VEPI (ocupação UTI diária por CNES) + CNES-LT (capacidade UTI mensal declarada).
O bug crítico da Fase 2.1.5 foi o parse de CSV com `sep=";"` em arquivo que usa `sep=","`,
causando descarte falso de 6.945 registros Manaus 2021.
Pipeline executado com sucesso: 74 SEs na janela SE10/2020-SE30/2021, pico
TOH=**2.115** em **2021-W03** (segunda onda Manaus, consistente com colapso histórico).
Spearman ρ(TOH×SRAG) = **0.462** (p=0.000050).

---

## 2. Diagnóstico do bug Fase 2.1.5

**Causa raiz:** `pd.read_csv(..., sep=";")` em CSV DEMAS-VEPI que usa `sep=","`.
**Efeito:** 554.706 colunas em 1 coluna → filtro por `municipio` retorna 0 registros Manaus.
**Cascata:** fallback para FVS-AM (boletim narrativo agregado) com interpolação de
patamares constantes → ρ=0.472 artefato de série constante por blocos.
**Achado editorial (§6.4):** Este bug é Fricção Ontológica intra-pipeline — inconsistência
de schema entre API REST CKAN (`sep=";"`) e CSV consolidado S3 (`sep=","`).

---

## 3. Pipeline implementado

```
DEMAS-VEPI (CSV, sep=",") → filtro Manaus → uti_covid_total = confirmado+suspeito
CNES-LT (DBC, blast.dll skip=4) → filtro CODUFMUN=130260 → filtro CODLEITO 74-77
Merge municipal por ano-mes → TOH_dia = uti_municipal / capacidade_municipal
Agregação SE ISO → imputação forward-fill max 3SE → toh_semanal_manaus.parquet
```

**Nota metodológica:** matching por CNES retorna 34% de cobertura (31 CNES DEMAS-VEPI
vs 23 CNES-LT UTI 74-77). Adotada abordagem municipal (sum todos CNES / capacidade total),
metodologicamente mais robusta e consistente com cálculo de TOH regional.

**Nota técnica parser DBC:** pysus/pyreaddbc falham em Windows por `unistd.h` (POSIX+MSVC).
Solução: `blast.c` (Mark Adler/zlib) compilado como DLL via MSVC, com skip=4 bytes
(pré-cabeçalho proprietário DATASUS antes do stream blast canônico).

---

## 4. Resultados quantitativos

**TOH semanal Manaus (primeiras 10 SEs + ver parquet):**

| SE | Segunda-feira | TOH | n_CNES | Método |
|---|---|---|---|---|
| 2020-W10 | 2020-03-02 | NaN | NaN | nan_gap_too_large |
| 2020-W11 | 2020-03-09 | NaN | NaN | nan_gap_too_large |
| 2020-W12 | 2020-03-16 | 0.000 | 1 | demas_vepi_direct |
| 2020-W13 | 2020-03-23 | 0.000 | NaN | forward_fill_max_3SE |
| 2020-W14 | 2020-03-30 | 0.478 | 10 | demas_vepi_direct |
| 2020-W15 | 2020-04-06 | 0.643 | 10 | demas_vepi_direct |
| 2020-W16 | 2020-04-13 | 0.786 | 11 | demas_vepi_direct |
| 2020-W17 | 2020-04-20 | 0.905 | 12 | demas_vepi_direct |
| 2020-W18 | 2020-04-27 | 1.019 | 14 | demas_vepi_direct |
| 2020-W19 | 2020-05-04 | 1.079 | 24 | demas_vepi_direct |
... (ver parquet para serie completa)

**Pico TOH:** 2021-W03 = 2.115 (211.5%)
**SEs diretas (não imputadas):** 71/74 | **Imputadas:** 3
**Spearman ρ(TOH×SRAG):** 0.4620 (p=0.000050)
**Pearson r(TOH×SRAG):** 0.4299 (p=0.000183)
**PCA PC1 variância:** 0.715 (VALIDADO)
**Lag ótimo TOH→SRAG:** 3 SE (ρ=0.6236)

---

## 5. Cross-validação FVS-AM × DEMAS-VEPI

**Spearman (DEMAS × FVS-AM):** ρ=0.865 (p=0.0003)
**MAE:** 54.7 pp | **Max delta:** 90.3 pp | **SEs |delta|>10pp:** 12

**Top 5 divergências:**
```
 year_se  sem_epi  toh_uti_pct  toh_fvs  delta_pp
    2020       53     1.943350     1.04 90.334975
    2020       31     0.969709     0.24 72.970855
    2021       13     1.437097     0.71 72.709691
    2021        9     1.587425     0.87 71.742515
    2020       27     0.926780     0.30 62.677974
```


**Interpretação (§6.4):** As divergências entre microdado DEMAS-VEPI e boletim narrativo
FVS-AM são evidência empírica de Fricção Ontológica entre fontes com distintos regimes
de produção: declaração formal CNES vs. notificação e-SUS; boletim agregado narrativo
vs. dado microanalítico por CNES-dia.

---

## 6. Achados-âncora para §6.4 do canônico

1. **Bug do separador:** decisão computacional irreversível por inconsistência de schema.
2. **TOH pico > 1.0:** o CNES-LT captura apenas capacidade declarada formal (284-395 leitos),
   não inclui leitos emergenciais instalados durante a crise Manaus jan/2021.
   Numerador DEMAS-VEPI reporta 815 leitos UTI COVID ocupados no pico (2021-01-21).
   TOH = 815/319 = 2.56 → sistema a 256% da capacidade declarada (colapso documentado).
3. **Divergências FVS-AM vs DEMAS-VEPI:** ambas são "fontes oficiais MS" mas divergem
   porque têm diferentes grânulos, regimes de coleta e cobertura temporal.

---

## 7. Outputs gerados

- `data/predictors/manaus_bi/derived/cnes_lt_manaus_uti_mensal.parquet`
- `data/predictors/manaus_bi/derived/demas_vepi_manaus_uti_diario.parquet`
- `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet` (substituído)
- `data/predictors/manaus_bi/_archive/toh_semanal_manaus_FASE215_PRE_BIS.parquet`
- `data/predictors/manaus_bi/raw/source_manifest.json` (28 arquivos SHA256)
- `outputs/setup_pysus_fase215bis.md`
- `outputs/cross_validacao_fvs_demas_fase215bis.csv`
- `outputs/correlacao_toh_srag_fase215bis.json`
- `outputs/_archive/bi_dimensional_decision_FASE215_PRE_BIS.json`
- `outputs/bi_dimensional_decision.json` (atualizado)
- `outputs/relatorio_fase215bis_executivo.md` (este arquivo)
- `blast.dll` (compilado MSVC, parser DBC)

---

## 8. Restrições conhecidas / gaps remanescentes

1. **Cobertura DEMAS-VEPI 77.5%** para campos antigos (2021): 22.5% das linhas-CNES-dia
   não têm `ocupacaoConfirmadoUti + ocupacaoSuspeitoUti` — provavelmente hospitais sem
   UTI COVID específica ou subnotificação no início do período.
2. **CNES-LT é declarado, não realizado:** capacidade existente ≠ operacional.
   TOH > 1.0 é artefato desta limitação + leitos emergenciais não registrados.
3. **Subnotificação SIVEP-Gripe início pandemia:** SEs 10-15/2020 têm dados esparsos
   (teste RT-PCR ainda escasso, critérios de notificação em evolução).
4. **blast.dll Windows:** parser DBC proprietário DATASUS requer blast.dll compilada
   localmente; não portável sem recompilação em outros ambientes.
