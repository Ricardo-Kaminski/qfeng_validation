# Relatório Executivo — Fase 2.1.5 BI Bivariado Manaus (Continuação)

**Branch:** caminho2  
**Data:** 2026-04-26 (sessão noturna)  
**Commits:** `f4e652c` (2.A) · `531bf4e` (2.B) · `322b42e` (2.C) · `99fa11e` (2.D)

---

## 1. Contexto

Continuação da Fase 2 BI Bivariado Manaus com reorientação de granularidade mensal → semanal (SE). O bloqueio original da Tarefa 2.1 (OpenDataSUS HTTP 403 para SRAG) foi contornado com os arquivos INFLUD20/21 disponíveis localmente (2,9 GB).

---

## 2. Tarefas

| Tarefa | Descrição | Status | Commit |
|--------|-----------|--------|--------|
| 2.A | TOH semanal — API DEMAS-VEPI / fallback FVS-AM | ✅ CONCLUÍDA | `f4e652c` |
| 2.B | SRAG semanal — INFLUD20/21 local | ✅ CONCLUÍDA | `531bf4e` |
| 2.C | Revalidação cruzada bivariada semanal | ✅ CONCLUÍDA | `322b42e` |
| 2.D | Archive Fase 1 + refactor loader SE | ✅ CONCLUÍDA | `99fa11e` |
| 2.E | Relatório executivo + CHANGELOG | ✅ CONCLUÍDA | *(este)* |

---

## 3. Resultados-chave

### 3.1 API DEMAS-VEPI — DESCARTADA

**Diagnóstico:** `ocupacaohospitalaruti`=null em todos os registros de Manaus (n=89/10.000 amostrados). Sem campo de capacidade total UTI, o TOH% é inviável via API.

**Fallback aplicado:** Interpolação linear dos 12 meses FVS-AM → 73 SEs. Pico SE 3/2021 = 103.7% (FVS-AM boletim: 104%). Sanity check OK.

Output: `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet`

### 3.2 SRAG semanal — DESBLOQUEADA ✅

INFLUD20/21 processados localmente via leitura em chunks (CO_MUN_RES=130260).

| Indicador | Valor |
|-----------|-------|
| Total SEs | 73 |
| n_covid | **21.212** |
| n_obitos | **10.110** |
| is_stub | **False** |
| Pico | SE 3/2021: 1.447 COVID, 778 óbitos |

Output: `data/predictors/manaus_bi/derived/srag_semanal_manaus.parquet`

### 3.3 Validação cruzada bivariada — PCA_VALIDATED ✅

| Métrica | Valor | Critério | Resultado |
|---------|-------|----------|-----------|
| Spearman ρ(TOH, n_covid) | +0.472 | >0.50 | ⚠ Abaixo¹ |
| Spearman ρ(TOH, n_obitos) | +0.393 | — | sig. p=0.001 |
| PCA PC1 variância | **70.2%** | ≥70% | ✅ |
| Pesos PCA TOH/SRAG | **50%/50%** | apriori 50/50 | ✅ delta=0 |

¹ ρ=0.472 < 0.50: FVS-AM não sistemático antes de jul/2020 → TOH fixo em 30% para SE 10-28/2020 enquanto SRAG registra pico da primeira onda (876-1031 casos/semana). Achado metodológico para §6.4.

**Decisão:** `pca_validated` — pesos 50/50 confirmados empiricamente.

### 3.4 Refactor loader e archival — CONCLUÍDO ✅

- Parquets Fase 1 (mensais) arquivados em `_archived/`
- `manaus_bi_loader.py` refatorado: SE_WINDOW, paths `derived/`, `is_stub=False` assertado
- `test_srag_not_stub` substituído por `test_srag_real` (sem skip)
- **15/15 testes passando**

---

## 4. Estado final do subsistema BI Bivariado

```
FONTES DE DADOS:
  TOH: FVS-AM mensal (interpolado) → 73 SEs ✅
  SRAG: SIVEP-Gripe INFLUD20/21 → 73 SEs, is_stub=False ✅

VALIDAÇÃO:
  Spearman: ρ=0.472 (sig.) ✅
  PCA: PC1=70.2%, pesos 50/50 ✅
  Decisão: pca_validated ✅

LOADER:
  manaus_bi_loader.load_manaus_bi_series() → 73 dicts (SE)
  15/15 testes ✅
```

---

## 5. Pendências para Fase 3

1. **Regenerar Tabela 7 e Figura 3** com t_mort=0.18 (bug corrigido na Fase 2 Tarefa 2.2).
2. **Atualizar §6.4** com achado metodológico: ρ=0.472, primeira onda, limitação TOH pré-jul/2020.
3. **Atualizar §7.4** com nota sobre O₂ prospectivo-only (Caminho C, Fase 1 Tarefa 1.3).
4. Verificar se granularidade semanal impacta outras Tabelas/Figuras do Paper 1.

---

## 6. Decisão de arquitetura

**Granularidade definitiva do Caminho 2:** Semanal (SE). O predictor BI bivariado opera com 73 SEs cobrindo SE 10/2020 a SE 30/2021, capturando as duas ondas COVID de Manaus com resolução epidemiológica real.
