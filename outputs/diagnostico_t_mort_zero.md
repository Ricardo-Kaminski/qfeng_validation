# Diagnóstico Bug t_mort=0 — SIH Manaus 2020-2021

**Data original:** 2026-04-26 (Fase 1 BI bivariado — Tarefa 1.4)
**Revisão semântica:** 2026-04-26 (Fase 2 — Tarefa 2.4 — alinhamento causa raiz e nota SIH vs SIM)
**Arquivo:** `data/predictors/manaus_sih/sih_manaus_2020_2021.parquet`

## Achados

| Campo | Valor |
|-------|-------|
| Total de linhas | 2678 |
| Tipo MORTE (raw parquet) | str (ArrowDtype) |
| Valor counts (raw) | `{'Não': 2196, 'Sim': 482}` |
| Óbitos (Sim) após `pd.to_numeric()` | **0** ← bug |
| Óbitos (Sim) após fix correto | **482** |
| % óbitos SIH (fix) | 18,0% |

## Diagnóstico

Bug confirmado — t_mort=0 é silêncio de conversão, não dado faltante.

O parquet `data/predictors/manaus_sih/sih_manaus_2020_2021.parquet` está correto:
contém 482 registros com `MORTE == 'Sim'` (string) e 2196 com `MORTE == 'Não'`,
codificação consistente com o output esperado de `microdatasus.process_sih()`.

O bug está no consumidor: `manaus_sih_loader.py` aplica
`pd.to_numeric(df['MORTE'], errors='coerce').fillna(0)`,
que retorna NaN para strings `'Sim'/'Não'` — em especial porque a coluna tem
dtype ArrowDtype (`str`), não `object`, então a guarda `dtype == object` falha
silenciosamente e cai no branch `pd.to_numeric()`. O parquet não precisa ser
re-extraído; o fix é uma linha no loader.

## Causa Raiz

Cadeia: `process_sih()` produz `MORTE: str ∈ {'Sim', 'Não'}` (ArrowDtype) →
`manaus_sih_loader.py` aplica `pd.to_numeric()` esperando códigos numéricos
do AIH bruto (1/0) → NaN para strings → `.fillna(0)` mascara silenciosamente.

O fix de uma linha `(df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)`
preserva o parquet existente e elimina a cadeia de conversão silenciosa.

## Impacto

- `t_mort` derivado desta coluna estava zerado em todas as execuções anteriores
- `theta_eff` Markoviano afetado nos cálculos que usam `t_mort` como entrada
- Tabela 7 e Figura 3 do canônico precisam ser regeneradas na Fase 3 (ver abaixo)

## Ação Requerida (aplicada em Fase 2 — Tarefa 2.2)

1. **Fix aplicado** em `manaus_bi_loader.py` (novo loader canônico):

   ANTES (bug em `manaus_sih_loader.py`):
   ```python
   sih["MORTE"] = pd.to_numeric(sih["MORTE"], errors="coerce").fillna(0).astype(int)
   ```

   DEPOIS (fix em `manaus_bi_loader.py`):
   ```python
   sih["MORTE_NUM"] = (sih["MORTE"].astype(str).str.strip() == "Sim").astype(int)
   ```

2. **Não re-extrair o parquet** — está correto (482 'Sim', 2196 'Não').

3. **Teste de regressão** em `tests/test_manaus_bi_loader.py`:
   ```python
   def test_t_mort_fix(sih):
       assert sih["MORTE_NUM"].sum() == 482
   ```

4. **Recálculo do θ_eff e regeneração de Tabela 7 e Figura 3** são item da Fase 3,
   após estabilização do loader na Fase 2.

## Nota — Discrepância SIH vs SIM (não é problema)

Estimativas SIM apontam ~6.000–9.000 óbitos hospitalares COVID em Manaus 2020–2021.
O SIH registra apenas 482 óbitos em 2.678 internações nesta janela. A discrepância
é esperada e reflete diferença de denominadores:

- **SIM** (Sistema de Informações sobre Mortalidade) registra todos os óbitos por COVID,
  incluindo: óbitos comunitários, óbitos em estabelecimentos não-AIH (UPAs, hospitais
  privados sem AIH paga, unidades de campanha), óbitos em transferência interhospitalar.

- **SIH** registra apenas internações com AIH paga (rede SUS contratada), com
  `MORTE='Sim'` no campo de alta da AIH. Excluem-se óbitos em UPA/PS antes da AIH,
  óbitos em rede privada, e óbitos pós-alta.

O ratio 482/2678 ≈ 18% é consistente com letalidade hospitalar COVID reportada na
literatura para Manaus (15–25% UTI, 10–15% enfermaria). Nenhuma ação corretiva
é necessária; esta nota existe para evitar que leitores futuros interpretem a
diferença como subnotificação no parquet SIH.

## Pendência Fase 3

Regenerar Tabela 7 e Figura 3 do canônico com `t_mort ≈ 0.18` (482/2678), em substituição
ao valor `t_mort = 0.0` publicado nas versões da Fase 1. Revisar também a narrativa textual
do paper que comentava t_mort=0 como achado empírico.
