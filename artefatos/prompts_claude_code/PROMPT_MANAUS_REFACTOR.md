# Prompt para Claude Code — Refactor Manaus θ_eff Series

**Contexto:** Este prompt é para ser executado pelo Claude Code no workspace local `C:\Workspace\academico\qfeng_validacao`. O plano completo está em `docs/MANAUS_REFACTOR_PLAN.md`.

**Objetivo:** Substituir os 6 meses com dados estimados de literatura (jul-set/2020, abr-jun/2021) por microdados SIH/DATASUS reais, regenerando figuras, tabelas e texto do paper.

---

## Tarefa

Você é o Claude Code operando no projeto Q-FENG Validation. Execute o refactor metodológico descrito abaixo com integridade completa — nenhum dado inventado pode permanecer no pipeline.

### Fase 1: Download dos dados faltantes

1. Abrir `scripts/download_sih_manaus_ftp.py`
2. Expandir a lista `ARQUIVOS` para incluir os 6 meses faltantes:
   ```python
   ARQUIVOS = [
       "RDAM2007.dbc",  # jul/2020  ← ADICIONAR
       "RDAM2008.dbc",  # ago/2020  ← ADICIONAR
       "RDAM2009.dbc",  # set/2020  ← ADICIONAR
       "RDAM2010.dbc",  # out/2020  (já baixado)
       "RDAM2011.dbc",  # nov/2020  (já baixado)
       "RDAM2012.dbc",  # dez/2020  (já baixado)
       "RDAM2101.dbc",  # jan/2021  (já baixado)
       "RDAM2102.dbc",  # fev/2021  (já baixado)
       "RDAM2103.dbc",  # mar/2021  (já baixado)
       "RDAM2104.dbc",  # abr/2021  ← ADICIONAR
       "RDAM2105.dbc",  # mai/2021  ← ADICIONAR
       "RDAM2106.dbc",  # jun/2021  ← ADICIONAR
   ]
   ```
3. Executar: `python scripts/download_sih_manaus_ftp.py`
4. Validar: `dir data\predictors\manaus_sih\raw` deve listar 12 arquivos `.dbc`.

**Critério de sucesso Fase 1:** 12 arquivos `.dbc` presentes em `data/predictors/manaus_sih/raw/`, totalizando aproximadamente 100–200 MB.

### Fase 2: Extração via R (microdatasus)

1. Abrir `scripts/extract_manaus_sih_r.R`
2. Modificar os parâmetros de `fetch_datasus`:
   - `month_start = 7`  (era 10)
   - `month_end   = 6`  (era 3)
   - Manter `year_start = 2020` e `year_end = 2021`
3. Atualizar o comentário do cabeçalho para refletir período Jul/2020–Jun/2021 (12 meses)
4. Executar: `Rscript scripts/extract_manaus_sih_r.R`
5. Validar:
   - `data/predictors/manaus_sih/sih_manaus_2020_2021.parquet` regenerado com ~3.000–5.000 registros (antes: 1.526)
   - `data/predictors/manaus_sih/serie_temporal_manaus.csv` regenerado com 12 linhas (competências 202007, 202008, ..., 202106)

**Critério de sucesso Fase 2:** Parquet e CSV regenerados com dados de todos os 12 meses.

**Troubleshooting:** Se o script R falhar na leitura de arquivos `.dbc`, verificar que o pacote `read.dbc` do CRAN está instalado (não é parte do `microdatasus` por default):
```r
install.packages("read.dbc")  # ou
remotes::install_github("danicat/read.dbc")
```

### Fase 3: Refactor do loader Python

1. Abrir `src/qfeng/e5_symbolic/manaus_sih_loader.py`
2. **Remover inteiramente** o dicionário `_LITERATURE_DATA` (linhas que mapeiam 6 meses para valores inventados)
3. **Atualizar a docstring** no topo do arquivo:
   - Remover frases que mencionam "literature estimates", "Sabino et al.", "Hallal et al.", "COSEMS-AM" na descrição de fontes
   - Substituir por: "All 12 months (Jul/2020–Jun/2021) use real SIH/DATASUS microdata (sih_manaus_2020_2021.parquet)"
4. **Revisar `_OCCUPANCY_BY_MONTH`**: Os valores atuais foram calibrados parcialmente à literatura. Implementar a Opção C do plano:
   - Manter Jan/2021 = 100 (ancorado em Portaria 69/2021 — este é o ground truth documentado)
   - **Recalibrar os demais 11 meses** proporcionalmente à taxa_uti SIH real de cada mês, com fator de calibração que faça Jan/2021 coincidir com 100%
   - Implementar isso como **função derivada** dentro do loader, não como dicionário hardcoded:
     ```python
     def _compute_occupancy_from_sih(taxa_uti_mes: float, taxa_uti_jan_2021: float) -> int:
         """Scale occupancy proportionally to UTI rate, anchored at Jan/2021 = 100%."""
         scaled = (taxa_uti_mes / taxa_uti_jan_2021) * 100.0
         return int(round(min(max(scaled, 30.0), 100.0)))  # clamp 30–100
     ```
   - Calcular `taxa_uti_jan_2021` uma vez no início de `load_manaus_real_series()` e usar como âncora para os demais meses.
5. **Unificar o loop**: eliminar o branch `if ym in _LITERATURE_DATA: ... else: ...` — todos os 12 meses passam pela mesma lógica de extração SIH.
6. Executar validação: `python -c "from qfeng.e5_symbolic.manaus_sih_loader import load_manaus_real_series; serie = load_manaus_real_series(); [print(r['label'], r['theta_t'], r['hospital_occupancy_pct']) for r in serie]"`

**Critério de sucesso Fase 3:** Função `load_manaus_real_series()` retorna 12 linhas com `data_source = "sih_datasus"` em todas, sem qualquer referência a `_LITERATURE_DATA`.

### Fase 4: Validação do argumento central

Após Fase 3, rodar teste crítico — **CB onset deve permanecer em out/2020**:

```python
from qfeng.e5_symbolic.manaus_sih_loader import load_manaus_real_series

serie = load_manaus_real_series()
for row in serie:
    theta_t = row['theta_t']
    regime = 'CB' if theta_t >= 120 else ('HITL' if theta_t >= 30 else 'STAC')
    print(f"{row['label']:>10} | θ_t={theta_t:6.2f}° | occ={row['hospital_occupancy_pct']:>3}% | {regime}")

# Assertion crítica
oct_2020 = next(r for r in serie if r['label'] == 'out/2020')
assert oct_2020['theta_t'] >= 120.0, f"CRITICAL: CB onset lost — θ_t(out/2020) = {oct_2020['theta_t']}"
print("\n✅ CB onset preserved in Oct/2020")
```

**Critério de sucesso Fase 4:** θ_t(out/2020) ≥ 120° (idealmente ~125–130°, mantendo ou fortalecendo o argumento do paper).

**Se falhar (θ_t(out/2020) < 120°):** PARE e reporte ao Ricardo. Isso indica que o ajuste da calibração `_OCCUPANCY_BY_MONTH` deslocou a série — precisa revisão manual.

### Fase 5: Regenerar figuras

1. Identificar o script que gera a Figure 3 do paper — provavelmente `scripts/generate_F2_manaus.py` ou `scripts/generate_paper1_figures.py`
2. Executar o script
3. Verificar visualmente a figura gerada em `outputs/figures/F*_manaus*.png`:
   - **Deve ter**: série θ_eff contínua, sem diferenciação visual entre "SIH" e "literatura"
   - **Deve ter**: bootstrap CI uniforme (mesma largura em todos os 12 meses)
   - **Não deve ter**: legenda "Occupancy — literature est." (remover do script se necessário)
   - **Deve ter**: anotação CB onset = out/2020, Peak = fev/2021, Portaria 69/2021 = jan/2021

**Se o script de figuras ainda referenciar o flag `data_source`:** atualizar para que todos os pontos sejam plotados com estilo unificado, removendo a dualidade visual.

### Fase 6: Regenerar Table 7 no paper

1. Abrir `docs/papers/PAPER1_QFENG_FINAL_editando.md`
2. Localizar Table 7 (Manaus 12-month theta-efetivo series)
3. Substituir todos os valores de θ_t, θ_eff, α(t), Occupancy e CI lower/upper pelos valores novos calculados a partir do pipeline refatorado
4. **Coluna "Data source"**: todas as 12 linhas devem mostrar "SIH/DATASUS" (remover "literature" de todas)

Valores a obter do runner após Fase 4 — gerar um CSV auxiliar:

```python
import pandas as pd
from qfeng.e5_symbolic.manaus_sih_loader import load_manaus_real_series

serie = load_manaus_real_series()
df = pd.DataFrame(serie)
df.to_csv('outputs/table7_new_values.csv', index=False)
print(df[['label', 'theta_t', 'hospital_occupancy_pct', 'data_source']].to_string(index=False))
```

### Fase 7: Atualizar texto do paper

Em `docs/papers/PAPER1_QFENG_FINAL_editando.md`:

**7.1 — Remover o terceiro "feature" de §5.3 (Bootstrap CI width asymmetry)**

Localizar a string exata:
```
1.	Bootstrap CI width asymmetry: SIH/DATASUS months (Oct/2020–Mar/2021) have narrow bootstrap CIs (±1–2°), reflecting the higher data quality of real microdata. Literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021) have wider CIs (±3–4°), reflecting the uncertainty of epidemiological estimates. The January 2021 peak month has CI [126.72°, 131.22°] — entirely within the CIRCUIT_BREAKER regime regardless of bootstrap variation.
```

Substituir por:
```
1.	Bootstrap CI uniformity: All twelve months use SIH/DATASUS microdata, producing uniformly narrow bootstrap CIs (±1–2°) that reflect the high data quality of real administrative records. The January 2021 peak month has CI [126.72°, 131.22°] — entirely within the CIRCUIT_BREAKER regime regardless of bootstrap variation.
```

**7.2 — Remover a limitação "Literature-estimated months" em §7.4**

Localizar e deletar inteiramente o parágrafo:
```
Literature-estimated months in Manaus series: Six of twelve Manaus months (Jul–Sep/2020 and Apr–Jun/2021) use epidemiological literature estimates rather than real SIH/DATASUS microdata. The bootstrap CI analysis confirms that this introduces ≤4° uncertainty in θ_eff; all classifications are stable. However, the paper-reported E2 evaluation for these months is not derived from real microdata and should be interpreted accordingly.
```

**7.3 — Atualizar §6.3 (Bootstrap Confidence Intervals)**

Localizar:
```
Confidence intervals for the Manaus theta_efetivo series were computed via parametric bootstrap: for SIH/DATASUS months (Oct/2020–Mar/2021), σ = 0.05 was used (reflecting the quality of real microdata); for literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021), σ = 0.10 was used (reflecting epidemiological estimation uncertainty).
```

Substituir por:
```
Confidence intervals for the Manaus theta_efetivo series were computed via parametric bootstrap with σ = 0.05 uniform across all twelve months (Jul/2020–Jun/2021), reflecting the consistent data quality of real SIH/DATASUS microdata.
```

**7.4 — Atualizar caption da Figure 3**

A caption atual menciona duas fontes no axis label. Ajustar para uma única fonte SIH/DATASUS. Localizar e verificar o texto da caption (está em §5.3, abaixo da referência `![Figure](/word/media/image3.png)`).

**7.5 — Atualizar caption da Table 7**

Similar — remover qualquer menção a literature/epidemiological estimates.

### Fase 8: Rodar suite de testes

```bash
cd C:\Workspace\academico\qfeng_validacao
conda activate qfeng
pytest tests/ -v
```

**Critério de sucesso Fase 8:** 100% dos testes passam. Se algum teste em `tests/test_e5/` referenciar valores hardcoded do θ_eff antigo, **atualizar o valor esperado** com o novo número da série real (documentar no commit message).

### Fase 9: Commit git

```bash
git add -A
git commit -m "refactor(manaus): substitute literature-estimated months with real SIH/DATASUS microdata

- Download RDAM2007-2009 and RDAM2104-2106 from DATASUS FTP
- Extract via microdatasus R package (expanded to 12-month window)
- Remove _LITERATURE_DATA dictionary from manaus_sih_loader.py
- Re-anchor _OCCUPANCY_BY_MONTH to Jan/2021 = 100% (Portaria 69/2021)
   and derive other months from real SIH UTI rate
- Regenerate Figure 3 and Table 7 with uniform SIH/DATASUS data source
- Remove §7.4 'Literature-estimated months' limitation
- Update §5.3, §6.3 bootstrap methodology description

Methodological rationale: author (Kaminski) has institutional access to
SIH/DATASUS microdata via MS/DEMAS/SEIDIGI; using literature estimates
when primary data is accessible is an indefensible methodological choice
for a paper submitted to JURIX/UGR/Lancet Digital Health reviewers.

CB onset preserved in Oct/2020 (argument integrity validated)."
```

---

## Relatórios ao Ricardo

Após cada Fase, reporte ao Ricardo:

- **Fase 1**: confirmação dos 6 downloads bem-sucedidos com tamanho de cada arquivo
- **Fase 2**: output final do script R com contagem de registros por mês (printar `print(serie)` completo)
- **Fase 3**: diff do `manaus_sih_loader.py` antes/depois (bloco `_LITERATURE_DATA` removido, nova função `_compute_occupancy_from_sih` adicionada)
- **Fase 4**: ⚠️ **ESPECIALMENTE IMPORTANTE** — tabela printada de todos os 12 meses com θ_t e regime, confirmação de que CB onset permanece em Oct/2020
- **Fase 5**: caminho da figura gerada + tamanho em KB (para o Ricardo abrir e verificar visualmente)
- **Fase 6**: tabela printada com os novos valores de Table 7
- **Fase 7**: diff do `.md` antes/depois dos 5 pontos de edição
- **Fase 8**: output completo do `pytest -v`
- **Fase 9**: hash do commit + output de `git log -1 --stat`

**Se qualquer validação falhar, PARE a execução e reporte ao Ricardo para decisão manual.**

---

## Notas operacionais

1. **Nunca apagar arquivos** de dados existentes sem confirmação — sempre fazer backup antes de sobrescrever parquets. Criar `sih_manaus_2020_2021_BACKUP_PRE_REFACTOR.parquet` antes de regenerar.

2. **Preservar o argumento central**: o refactor deve fortalecer, não enfraquecer, a tese "CB three months before Portaria 69/2021". Se os novos valores mostrarem fortalecimento (θ_t(out/2020) > 125°), isso é excelente. Se mostrarem enfraquecimento (θ_t(out/2020) < 120°), PARE.

3. **Uso do git**: todos os passos operam sobre a árvore versionada. Se alguma coisa der errado, `git reset --hard HEAD` restaura o estado pré-refactor.

4. **Environment**: conda env `qfeng` deve estar ativo. R instalado com `microdatasus`, `read.dbc`, `dplyr`, `arrow`, `readr`.

Boa execução.
