# Prompt para Claude Code — Caminho 2, Fase 1: Levantamento BI multi-fonte Manaus

**Contexto:** Este prompt opera no workspace local `C:\Workspace\academico\qfeng_validacao` (conda env `qfeng`). O plano operacional completo está em `artefatos/briefings/RELATORIO_CAMINHO2_BI_MULTIFONTE.md`.

**Objetivo da Fase 1:** Levantar três séries primárias institucionalmente canônicas para Manaus jul/2020-jun/2021, persisti-las em parquets bem documentados, e validar consistência cruzada antes do refactor do pipeline (Fase 2).

**Pré-requisitos:**
- Conda env `qfeng` ativo.
- Acesso DEMAS/SEIDIGI a SIVEP-Gripe (autor confirmou).
- Acesso público a TabNet DATASUS (`http://www2.datasus.gov.br/DATASUS/index.php?area=0901`).
- Decisão Fase 0 sobre dimensão O₂ (trivariado vs bivariado): **a confirmar antes de iniciar**.

---

## Estrutura de diretórios a criar

```
data/predictors/manaus_bi/
├── README.md                      # Provenance manifest (Fase 1.4)
├── raw/                           # Dados brutos baixados
│   ├── srag_manaus_sivep/         # CSVs SIVEP-Gripe filtrados
│   └── boletins_fvs_am/           # PDFs/screenshots dos boletins (referência)
├── toh_uti_manaus.parquet         # Output Fase 1.1
├── srag_manaus.parquet            # Output Fase 1.2
└── oxigenio_manaus.parquet        # Output Fase 1.3 (se aplicável)
```

---

## Tarefa 1.1 — Validação e consolidação de TOH UTI Manaus

### Input
- Dicionário existente `_TOH_FVS_AM` em `src/qfeng/e5_symbolic/manaus_sih_loader.py` (lines ~73-103).
- TabNet DATASUS para validação cruzada (acesso público).

### Procedimento

1. Extrair `_TOH_FVS_AM` para `data/predictors/manaus_bi/toh_uti_manaus.parquet` com schema:
   ```python
   {
     "year": int, "month": int, "competencia": str (YYYYMM),
     "toh_uti_pct": float, 
     "source": str (FVS-AM / Fiocruz / SES-AM / TabNet),
     "source_doc": str (referência primária),
     "source_date": str (data do boletim),
     "is_estimated": bool,
     "estimation_method": str (NULL se is_estimated=False),
     "validation_status": str (canonical / cross_validated / interpolated),
   }
   ```

2. Preencher meses canônicos (todos os 8 meses com fonte FVS-AM/Fiocruz/SES-AM diretamente documentada): `is_estimated=False, validation_status="canonical"`.

3. Para os 4 meses estimados (set/2020 = 45%, abr/2021 = 71%, mai/2021 = 70%, jun/2021 = 70%):
   - Tentar buscar valor canônico via TabNet (tabulação por município/competência/leitos UTI).
   - Se TabNet retornar valor: marcar `validation_status="cross_validated"` com diferença ≤ 5pp aceitável; senão registrar valor TabNet substituindo o estimado.
   - Se TabNet não retornar valor: manter estimativa atual com `is_estimated=True, validation_status="interpolated"` e documentar metodologia.

4. Adicionar coluna de checagem secundária: TOH derivado de SIH (`taxa_uti × fator_calibrador`) para sanity-check — não substitui o TOH canônico, só serve como sanity check.

### Critério de sucesso 1.1
- 12 linhas no parquet, todas com `source` preenchida.
- ≥ 8 meses com `validation_status ∈ {canonical, cross_validated}`.
- Documentação de fonte primária (referência ao boletim/decreto) por linha.

### Saída
- `data/predictors/manaus_bi/toh_uti_manaus.parquet`
- Summary impresso no terminal: `competencia | toh_uti_pct | source | validation_status`

---

## Tarefa 1.2 — Extração de série SRAG Manaus (SIVEP-Gripe)

### Input
- FTP DATASUS: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIVEP_Gripe/Dados/`
  - `INFLUD20.csv` (~ 800MB, dados 2020 Brasil inteiro)
  - `INFLUD21.csv` (~ 1.2GB, dados 2021 Brasil inteiro)

### Procedimento

1. Criar `scripts/download_sivep_gripe_ftp.py`:
   ```python
   """Download INFLUD20.csv e INFLUD21.csv do FTP DATASUS para data/predictors/manaus_bi/raw/srag_manaus_sivep/."""
   ```

2. Criar `scripts/extract_srag_manaus.py`:
   ```python
   """Filtra SIVEP-Gripe Brasil por:
     - CO_MUN_RES = 130260 (Manaus, código IBGE 6 dígitos)
     - DT_NOTIFIC entre 2020-07-01 e 2021-06-30
     - CLASSI_FIN ∈ {5, 4} (5=COVID confirmado; 4=SRAG outras causas, separar)
   Agrega por (year, month):
     - srag_cases (notificações)
     - srag_covid_cases (CLASSI_FIN=5)
     - srag_uti_admissions (UTI=1)
     - srag_obito (EVOLUCAO=2)
     - srag_obito_pct (srag_obito / srag_cases)
     - srag_growth_rate (logaritmo da razão entre mês t e mês t-1)
   Persiste em data/predictors/manaus_bi/srag_manaus.parquet.
   """
   ```

3. Schema do parquet:
   ```python
   {
     "year": int, "month": int, "competencia": str,
     "srag_cases": int, "srag_covid_cases": int,
     "srag_uti_admissions": int, "srag_obito": int,
     "srag_obito_pct": float, "srag_growth_rate": float,
     "srag_cases_norm": float (min-max na janela 12 meses),
     "source": str ("SIVEP-Gripe DATASUS"),
     "source_url": str,
     "extraction_date": str,
   }
   ```

4. Validar com TabNet (`SIVEP-Gripe / Tabulação Manaus / 2020-2021 / SRAG por mês`) — diferença ≤ 5% aceitável.

### Critério de sucesso 1.2
- Parquet com 12 linhas, uma por (ano, mês).
- jan/2021 deve ter `srag_cases` em pico claro (literatura: Sabino et al. 2021 reporta ~10x crescimento out-jan).
- ago/2020 deve ter `srag_cases` em vale claro (interondas).
- `srag_growth_rate(jan/2021) > 0` significativo.

### Saída
- `data/predictors/manaus_bi/srag_manaus.parquet`
- Summary: `competencia | srag_cases | srag_covid_cases | srag_growth_rate`
- Validação cruzada vs TabNet — relatório `outputs/validacao_srag_tabnet.md`

---

## Tarefa 1.3 — Cobertura de O₂ medicinal Manaus (a confirmar viabilidade)

### Decisão prévia (Fase 0)

Antes de Tarefa 1.3, autor deve confirmar qual caminho viável:

- **Caminho A:** SCTIE/MS empenhos de O₂ medicinal Manaus 2020-2021 acessíveis via DEMAS/SEIDIGI (preferencial).
- **Caminho B:** CNES-LT (capacidade declarada de leitos UTI) como proxy estrutural de demanda de O₂.
- **Caminho C (fallback):** apenas indicador qualitativo via news indexing — **NÃO compõe ψ_N, fica em discussão narrativa**.

### Caminho A (preferencial)

1. Acessar base SCTIE/MS empenhos para CNPJ Hospitais Manaus jul/2020-jun/2021.
2. Filtrar por categoria "Oxigênio medicinal" (descrição do empenho ou código SIASG).
3. Computar:
   - `volume_m3_empenho_mes` (volume contratado por mês)
   - `dias_cobertura_estimada = volume / consumo_diario_estimado` (baseado em leitos UTI ativos × consumo médio leito-dia)
4. Persistir em `data/predictors/manaus_bi/oxigenio_manaus.parquet`.

### Caminho B (fallback estrutural)

1. Baixar CNES-LT mensal Manaus 2020-2021 (FTP DATASUS).
2. Extrair leitos UTI ativos (códigos 74, 75, 76, 77).
3. Computar `capacidade_o2_proxy = leitos_uti × 50_kg_o2_dia` (consumo médio documentado em literatura crítica).
4. Persistir como proxy estrutural com `source="CNES-LT proxy"`.

### Schema (qualquer caminho)

```python
{
  "year": int, "month": int, "competencia": str,
  "supply_indicator_value": float,
  "supply_indicator_unit": str (m³ / kg / leitos-equivalente),
  "days_coverage_proxy": float,
  "coverage_norm": float (min-max),
  "source": str (SCTIE-empenho / CNES-LT-proxy / qualitative-news),
  "observability_class": str (primary-administrative / structural-proxy / qualitative),
  "is_complete_for_psi_n": bool,
}
```

### Critério de sucesso 1.3
- Se Caminho A: 12 linhas com `observability_class="primary-administrative"`.
- Se Caminho B: 12 linhas com `observability_class="structural-proxy"`, declaração de proxy explícita.
- Se Caminho C: parquet vazio com `is_complete_for_psi_n=False`; trivariado fica bivariado, declarado em §7.4.

### Saída
- `data/predictors/manaus_bi/oxigenio_manaus.parquet` (ou flag `unavailable.json` se C)
- Decisão final BI: `outputs/bi_dimensional_decision.json` registrando trivariado vs bivariado

---

## Tarefa 1.4 — Validação cruzada e provenance manifest

### Procedimento

1. Criar `data/predictors/manaus_bi/README.md` documentando:
   - Cada série (TOH, SRAG, O₂ se aplicável)
   - Fontes primárias por mês
   - Metodologia de extração
   - Validações cruzadas executadas
   - Limitações conhecidas

2. Criar `scripts/validate_bi_consistency.py` que:
   - Carrega os 3 parquets (ou 2 se bivariado)
   - Plota as séries normalizadas no mesmo gráfico
   - Identifica visualmente: peak conjunto em jan/2021, vale conjunto em ago/2020
   - Calcula correlação Spearman entre as séries (esperar ρ > 0.6 para TOH-SRAG; ρ pode ser negativo para O₂-coverage vs TOH)

3. Executar e gerar `outputs/bi_validation_report.md` com:
   - Sanity checks visuais
   - Matriz de correlação
   - Diagnóstico de outliers
   - Recomendação de pesos w_TOH, w_SRAG, w_O2 baseada em PCA
   - Decisão final: pesos a priori (autor) ou pesos PCA (estatísticos)

### Critério de sucesso 1.4
- README.md completo e auditável.
- Validação cruzada com correlação ρ(TOH, SRAG) > 0.5 confirmando que ambas refletem a mesma realidade subjacente.
- Identificação de pesos finais para Fase 2.

### Saída
- `data/predictors/manaus_bi/README.md`
- `outputs/bi_validation_report.md`
- `outputs/bi_dimensional_decision.json` com pesos finais

---

## Validação geral Fase 1 — checklist antes de avançar para Fase 2

- [ ] `data/predictors/manaus_bi/toh_uti_manaus.parquet` existe e tem 12 linhas válidas
- [ ] `data/predictors/manaus_bi/srag_manaus.parquet` existe e tem 12 linhas válidas
- [ ] `data/predictors/manaus_bi/oxigenio_manaus.parquet` existe (trivariado) OU `unavailable.json` existe (bivariado)
- [ ] `data/predictors/manaus_bi/README.md` documenta provenance completa
- [ ] `outputs/bi_validation_report.md` mostra correlação esperada entre séries
- [ ] `outputs/bi_dimensional_decision.json` registra pesos finais e decisão tri/bi
- [ ] Bug `t_mort = 0` investigado (pode ser tratado em Fase 2, mas registrar diagnóstico aqui)
- [ ] CHANGELOG.md atualizado com Fase 1 concluída

---

## O que NÃO fazer na Fase 1

- NÃO modificar `manaus_sih_loader.py` ainda — refactor é Fase 2.
- NÃO regenerar Tabela 7 ou Figura 3 — outputs são Fase 3.
- NÃO atualizar o paper DOCX — atualização é Fase 4 (sessão de chat de revisão).
- NÃO fazer commit final de Fase 1 antes de validação completa do checklist.

---

## Ao final da Fase 1

Reporte ao autor:

```
✅ Fase 1 — Levantamento BI multi-fonte concluído.

Decisão dimensional: [TRIVARIADO / BIVARIADO]
Fontes consolidadas:
  - TOH UTI: [n] meses canônicos, [n] cross-validated, [n] interpolados
  - SRAG (SIVEP-Gripe): 12 meses, total [N] casos COVID-confirmados
  - O₂: [Caminho A primary-administrative / Caminho B structural-proxy / N/A]

Correlação Spearman:
  - ρ(TOH, SRAG) = [valor]
  - ρ(TOH, O₂_inverse) = [valor]  # se trivariado
  - ρ(SRAG, O₂_inverse) = [valor]  # se trivariado

Pesos recomendados para Fase 2:
  - w_TOH = [valor]
  - w_SRAG = [valor]
  - w_O2 = [valor]  # se trivariado

Bug t_mort=0: [diagnóstico inicial]

Próxima ação: Fase 2 — Refactor manaus_sih_loader.py → manaus_bi_loader.py
Aguardando aprovação do autor para iniciar Fase 2.
```

---

*Fim do prompt Fase 1.*
