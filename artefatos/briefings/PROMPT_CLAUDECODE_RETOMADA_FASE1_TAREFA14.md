# PROMPT_CLAUDECODE_RETOMADA_FASE1_TAREFA14

**Data de gravação:** 26 de abril de 2026
**Branch:** `caminho2`
**Ponto de retomada:** Tarefa 1.4 — Validação cruzada bivariada (script criado, NÃO executado)
**Motivo da interrupção:** limite de tokens da sessão

---

## Estado das Tarefas Fase 1 BI Bivariado

| Tarefa | Status | Commit | Observações |
|--------|--------|--------|-------------|
| 1.1 — TOH UTI Manaus | ✅ CONCLUÍDA | `236a4ea` | 12 linhas, 10 confirmados, 2 estimados |
| 1.2 — SRAG Manaus | ✅ CONCLUÍDA | `96b8bb9` | **STUB** — INFLUD20/21 não disponíveis no FTP |
| 1.3 — Stub Caminho C | ✅ CONCLUÍDA | `cd465b6` | `oxigenio_unavailable.json` criado e parseável |
| 1.4 — Validação cruzada | 🔄 EM ANDAMENTO | — | Script criado, aguarda execução |
| Relatório executivo final | ⏳ PENDENTE | — | `outputs/relatorio_fase1_bi_bivariado.md` |

---

## O que foi feito nesta sessão (resumo executivo)

### Tarefa 1.1 (commit 236a4ea)
- `scripts/build_toh_uti_manaus.py` criado e executado
- `data/predictors/manaus_bi/toh_uti_manaus.parquet` gerado (12 linhas, 13 colunas)
- Bug t_mort=0 confirmado: 2678/2678 linhas MORTE=0 no SIH parquet (encoding error)
- Proxy SIH (case-mix UTI) sistematicamente menor que TOH documentado — esperado
- Sanity checks OK: jan/2021=104%, fev/2021=101% (ambos ≥ 85%)
- Dirs criados: `data/predictors/manaus_bi/raw/srag_manaus_sivep/` e `raw/boletins_fvs_am/`

### Tarefa 1.2 (commit 96b8bb9)
- FTP `ftp.datasus.gov.br/dissemin/publicos/SIVEP_Gripe/Dados/` **NÃO EXISTE**
  - FTP root encontrado em `/dissemin/publicos/` mas sem subdiretório SIVEP_Gripe
  - Fonte alternativa documentada: opendatasus.saude.gov.br/dataset/srag-2020 e srag-2021
- `scripts/download_sivep_gripe_ftp.py` criado (documentação das fontes corretas)
- `scripts/extract_srag_manaus.py` criado (com lógica stub se INFLUD ausente)
- `data/predictors/manaus_bi/srag_manaus.parquet` criado como **STUB** (12 linhas zero, `is_stub=True`)
- Schema: `year, month, competencia, n_srag_total, n_covid, n_outros, n_obitos, letalidade_pct, source, is_stub`

### Tarefa 1.3 (commit cd465b6)
- `data/predictors/manaus_bi/oxigenio_unavailable.json` criado com decisão Caminho C
- `oxigenio_manaus.parquet` **não criado** (conforme spec)
- JSON parseável, campos: `decision`, `decision_date`, `rationale`, `bi_dimensions_active`, `bi_dimensions_prospective_only`, `future_work_note`

### Tarefa 1.4 — Estado ATUAL
- `scripts/validate_bi_consistency.py` **CRIADO mas NÃO executado**
  - Usuário interrompeu antes do Bash de execução
  - Script completo, ~230 linhas
  - Importa scipy, sklearn, matplotlib
- **Outputs pendentes** (nenhum criado ainda):
  - `outputs/bi_series_normalized.png`
  - `outputs/bi_dimensional_decision.json`
  - `outputs/bi_validation_report.md`
  - `outputs/diagnostico_t_mort_zero.md`
  - `data/predictors/manaus_bi/README.md`

---

## Pré-flight da próxima sessão

1. Confirmar branch: `git rev-parse --abbrev-ref HEAD` → esperado `caminho2`
2. Confirmar último commit: `git log -3 --oneline`
   Esperado:
   ```
   cd465b6 docs(bi-fase1): stub Caminho C -- O2 prospectivo-only (Tarefa 1.3)
   96b8bb9 feat(bi-fase1): extrai SRAG Manaus 12 meses do SIVEP-Gripe (Tarefa 1.2)
   236a4ea feat(bi-fase1): consolida TOH UTI Manaus 12 meses (Tarefa 1.1)
   ```
3. Confirmar que `scripts/validate_bi_consistency.py` existe (criado nesta sessão)
4. Confirmar 7/7 corpus Clingo: `python scripts/validate_clingo_corpus.py`

---

## Próximos passos (Tarefa 1.4)

### Passo 1: Executar o script

```bash
cd C:/Workspace/academico/qfeng_validacao
PYTHONIOENCODING=utf-8 "C:/Users/ricar/miniconda3/envs/qfeng/python.exe" scripts/validate_bi_consistency.py
```

Saída esperada:
- Spearman rho: `NaN (SRAG stub)` — esperado com stub
- Pico TOH: `2021-01` (jan/2021, TOH=104%) — sanity check OK
- Vale TOH: `2020-08` (ago/2020, TOH=24%) — sanity check OK
- PCA: `indisponível (SRAG stub com variância zero)` — esperado
- weights_decision_pending: `True` (stub ativo)
- 5 outputs gerados

### Passo 2: Verificar outputs gerados

```bash
ls outputs/bi_series_normalized.png outputs/bi_dimensional_decision.json outputs/bi_validation_report.md outputs/diagnostico_t_mort_zero.md
ls data/predictors/manaus_bi/README.md
```

### Passo 3: Commit Tarefa 1.4

Arquivos a commitar (via `git add -f` para parquets/json em gitignore):
```bash
git add scripts/validate_bi_consistency.py
git add -f data/predictors/manaus_bi/README.md
```

Para outputs: verificar se `outputs/` está no .gitignore ou não antes de adicionar.

Mensagem de commit:
```
feat(bi-fase1): validação cruzada bivariada + provenance manifest (Tarefa 1.4)
```

### Passo 4: Relatório executivo final

Criar `outputs/relatorio_fase1_bi_bivariado.md` com formato do briefing (linhas 310-360 do briefing original).

Commit:
```
docs(bi-fase1): relatório executivo Fase 1 — BI bivariado finalizado
```

---

## Contexto crítico para a próxima sessão

### SRAG stub — decisão sobre download

O FTP DATASUS para SIVEP-Gripe não existe mais no caminho documentado no briefing original.
A decisão a tomar com o Ricardo:
1. Manter stub e continuar (Spearman NaN, pesos pendentes) → Fase 2 resolve com INFLUD real
2. Baixar INFLUD20/21 manualmente de opendatasus.saude.gov.br → re-executar extract_srag_manaus.py

O briefing original prevê que Spearman > 0.5 como critério de sucesso. Com stub, isso não será atingido. O relatório deve documentar claramente que o critério de sucesso da Tarefa 1.4 está **condicionado ao download dos dados reais**.

### Bug t_mort=0 (não bloqueante)

Confirmado em Tarefa 1.1: `sih_manaus_2020_2021.parquet` tem MORTE=0 em todas as 2678 linhas.
Causa provável: parquet salvo antes da conversão de rótulos Sim/Não do microdatasus.
Não afeta as séries ativas do BI (TOH e SRAG). Fix na Fase 2.

### Decisão de pesos

A priori: `w_TOH = 0.50, w_SRAG = 0.50`
`weights_decision_pending = True` enquanto SRAG stub ativo.
Quando dados reais disponíveis: se `|w_TOH_pca - 0.50| < 0.10` → confirmar 50/50.
Se ≥ 0.10 → reportar ao Ricardo antes de decidir.

### Constraint crítico do briefing (NÃO violar)

- **NÃO modificar** `manaus_sih_loader.py`
- **NÃO regenerar** Tabela 7 / Figura 3
- **NÃO atualizar** DOCX
- **NÃO fazer git push** sem confirmação explícita do Ricardo
- **NÃO criar** `oxigenio_manaus.parquet`

---

## Arquivos chave do projeto

| Arquivo | Propósito |
|---------|-----------|
| `scripts/build_toh_uti_manaus.py` | Tarefa 1.1 — extração TOH |
| `scripts/download_sivep_gripe_ftp.py` | Tarefa 1.2 — status download SRAG |
| `scripts/extract_srag_manaus.py` | Tarefa 1.2 — extração/stub SRAG |
| `scripts/validate_bi_consistency.py` | Tarefa 1.4 — validação cruzada |
| `data/predictors/manaus_bi/toh_uti_manaus.parquet` | TOH UTI 12 meses |
| `data/predictors/manaus_bi/srag_manaus.parquet` | SRAG stub |
| `data/predictors/manaus_bi/oxigenio_unavailable.json` | Caminho C stub |
| `src/qfeng/e5_symbolic/manaus_sih_loader.py` | Fonte canônica `_TOH_FVS_AM` |
| `artefatos/briefings/PROMPT_CLAUDECODE_FASE1_BI_BIVARIADO_DEFINITIVO.md` | Briefing completo Fase 1 |

---

## Ambiente

- **Python:** `C:/Users/ricar/miniconda3/envs/qfeng/python.exe` (SEMPRE usar caminho completo)
- **Conda env:** `qfeng`
- **Branch:** `caminho2`
- **PYTHONIOENCODING:** `utf-8` (necessário em todos os comandos Python no Windows)
- **git add -f:** necessário para `data/predictors/` e `*.parquet` (ambos no .gitignore)

---

*Briefing gravado ao final da sessão de 26/abr/2026, branch `caminho2`.*
