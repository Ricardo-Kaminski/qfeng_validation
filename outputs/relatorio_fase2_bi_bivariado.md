# Relatório Executivo — Fase 2 BI Bivariado Manaus

**Branch:** caminho2  
**Data:** 2026-04-26  
**Commits:** `8edbb0f` (2.1-abort) · `7c77081` (2.2) · `3f9d449` (2.4) · *(este commit)* (2.5)

---

## 1. Escopo

Acoplamento de três objetivos: (a) substituir stub SRAG por dados reais SIVEP-Gripe;
(b) refactor `manaus_sih_loader.py` → `manaus_bi_loader.py` integrando TOH + SRAG + fix t_mort;
(c) revalidação cruzada bivariada plena.

---

## 2. Tarefas

| Tarefa | Descrição | Status | Commit |
|--------|-----------|--------|--------|
| 2.1 | SRAG real SIVEP-Gripe | ⚠️ ABORTADA | `8edbb0f` |
| 2.2 | Refactor loader + fix t_mort | ✅ CONCLUÍDA | `7c77081` |
| 2.3 | Revalidação cruzada bivariada | ⏳ DIFERIDA (depende 2.1) | — |
| 2.4 | Correção retroativa diagnóstico | ✅ CONCLUÍDA | `3f9d449` |
| 2.5 | Relatório executivo | ✅ CONCLUÍDA | *(este)* |

---

## 3. Resultados-chave

### 3.1 SRAG real (SIVEP-Gripe) — ABORTADA

**Diagnóstico de rede:**
- OpenDataSUS S3: `HTTP 403 Forbidden` em ambas as URLs INFLUD20/21
- Parsing HTML OpenDataSUS: 0 links CSV encontrados (requer JS/autenticação?)
- FTP DATASUS: conexão OK (anônima), mas `/dissemin/publicos/SIVEP_Gripe/` → `550 path not found`

`srag_manaus.parquet` permanece STUB (`is_stub=True`, `n_covid=0`).  
Diagnóstico completo em `outputs/sivep_gripe_unavailable.md`.

### 3.2 Validação cruzada plena — DIFERIDA

Tarefa 2.3 depende de SRAG real (Tarefa 2.1). Diferida para quando OpenDataSUS ou FTP DATASUS ficarem acessíveis.

Critérios de aceitação ainda pendentes: ρ(TOH, SRAG) > 0.50, PCA PC1 variance > 0.70.

### 3.3 Decisão de pesos — sem alteração

`bi_dimensional_decision.json` permanece com `decision_method: "apriori_only_pending_pca_validation"`,
`weights_decision_pending: true`, pesos 50/50.

### 3.4 Fix t_mort — APLICADO ✅

**Bug identificado na Fase 1:** `pd.to_numeric('Sim', errors='coerce')` retorna NaN para
ArrowDtype `str` → `.fillna(0)` zera todos os óbitos.

**Fix aplicado em `manaus_bi_loader.py`:**
```python
sih["MORTE_NUM"] = (sih["MORTE"].astype(str).str.strip() == "Sim").astype(int)
```

| Métrica | Antes (bug) | Depois (fix) |
|---------|-------------|-------------|
| `MORTE_NUM.sum()` | 0 | **482** |
| t_mort global | 0.0 | **0.180** (18%) |
| Faixa esperada (literatura) | — | 15–25% UTI COVID ✅ |

**Teste de regressão:** `test_t_mort_fix` em `tests/test_manaus_bi_loader.py` — PASSED.

### 3.5 Refactor loader — APLICADO ✅

| Aspecto | Antes | Depois |
|---------|-------|--------|
| Arquivo | `manaus_sih_loader.py` | `manaus_bi_loader.py` |
| TOH fonte | dict `_TOH_FVS_AM` (hardcoded) | `toh_uti_manaus.parquet` (Fase 1) |
| SRAG | ausente | `srag_manaus.parquet` (stub/real) |
| t_mort | bugado (=0) | correto (=482/2678≈0.18) |
| Export principal | `load_manaus_real_series()` | `load_manaus_bi_series()` |
| Status antigo | ativo | DEPRECATED (auditoria forense) |

**Testes:** 10 passed, 1 skipped (srag_not_stub aguarda extração real).

### 3.6 Diagnóstico t_mort — CORRIGIDO ✅

`diagnostico_t_mort_zero.md` revisado (Tarefa 2.4):
- Causa raiz corrigida: bug no loader (pd.to_numeric), não no parquet (que está correto)
- "Reload from raw DBC" removido — parquet não precisa ser re-extraído
- Nova seção "Nota — Discrepância SIH vs SIM" esclarece diferença de denominadores

---

## 4. Pendências para Fase 3

1. **Desbloquear Tarefa 2.1** — verificar acesso ao OpenDataSUS/FTP em outra sessão ou rede.  
   Alternativas a discutir com o autor: reagendar, TabNet manual, proxy SIH, ou Caminho C definitivo.

2. **Tarefa 2.3** — revalidação cruzada com SRAG real (Spearman ρ, PCA, atualização JSON).

3. **Regenerar Tabela 7 e Figura 3** do canônico com t_mort=0.18 (era=0.0).  
   Revisar narrativa textual que comentava t_mort=0 como achado empírico.

4. **Atualizar §7.4** do canônico com nota sobre O₂ prospectivo-only (decisão Caminho C, Fase 1).

---

## 5. Próxima ação

**Aguardando decisão do autor** sobre paliativos para Tarefa 2.1 (SRAG SIVEP-Gripe).

Após desbloqueio e conclusão de 2.1/2.3:  
Fase 3 — Regeneração de Tabela 7 e Figura 3 do canônico com `load_manaus_bi_series()` + t_mort corrigido.
