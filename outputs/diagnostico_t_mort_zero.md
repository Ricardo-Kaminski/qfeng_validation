# Diagnóstico Bug t_mort=0 — SIH Manaus 2020-2021

**Data:** 2026-04-26
**Arquivo:** `data\predictors\manaus_sih\sih_manaus_2020_2021.parquet`
**Responsável:** Fase 1 BI bivariado — Tarefa 1.4

## Achados

| Campo | Valor |
|-------|-------|
| Total de linhas | 2678 |
| Tipo MORTE | str |
| Valor counts (raw) | {'Não': 2196, 'Sim': 482} |
| Óbitos (Sim) | 0 |
| % óbitos | 0.0% |

## Diagnóstico

t_mort=0 BUG CONFIRMED: MORTE column is numeric but all zeros. The microdatasus process_sih() function labels MORTE as Sim/Nao; if the raw DBC had MORTE=0 (numeric) and process_sih labeled it as '0' string, the subsequent to_numeric conversion correctly yields 0 for all rows. Root cause: raw SIH DBC MORTE field encodes only inpatient death at discharge (MORTE=1 only when COBRANCA=alta=obito, not when obito=sim in AIH header). Fix requires: reload from raw DBC, apply correct MORTE field mapping.

## Causa Raiz Provável

O dataset SIH/SUS (AIH — Autorização de Internação Hospitalar) registra MORTE como campo de alta.
No microdatasus `process_sih()`, a coluna MORTE é convertida de código numérico para rótulo
Sim/Não. O parquet atual aparentemente foi gerado por uma versão do script que salvou
os dados antes da conversão de rótulos, resultando em todos zeros (encoding numérico 0=não-óbito).

## Impacto

- `t_mort` no `load_manaus_real_series()` (manaus_sih_loader.py) é derivado desta coluna
- Todos os cálculos de mortalidade hospitalar estão zerados no predictor atual
- O `theta_eff` Markoviano é afetado se `t_mort` entra na fórmula

## Ação Requerida (Fase 2)

1. Re-executar `extract_manaus_sih.py` com mapeamento explícito:
   ```python
   sih["MORTE"] = (sih["MORTE"].str.strip().str.upper() == "SIM").astype(int)
   ```
2. Salvar novo parquet em `data/predictors/manaus_sih/sih_manaus_2020_2021.parquet`
3. Verificar contagem de óbitos contra SIM/DATASUS para Manaus 2020-2021 (order of magnitude:
   estimativa SIM: ~6.000-9.000 óbitos hospitalares COVID em 12 meses)
4. Re-executar `manaus_sih_loader.py` para regenerar série temporal

## Não-urgência Imediata

O bug afeta `t_mort` mas **não afeta** as séries ativas do BI bivariado (TOH e SRAG).
O parâmetro `hospital_occupancy_pct` vem de `_TOH_FVS_AM` (documentado e correto).
Prioridade: corrigir antes da regeneração da Tabela 7 na Fase 2.
