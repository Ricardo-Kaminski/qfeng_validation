# Relatório Executivo — Fase 1 BI Bivariado Manaus
**Branch:** caminho2  
**Data:** 2026-04-26  
**Commits:** `236a4ea` (1.1) · `96b8bb9` (1.2) · `cd465b6` (1.3) · `ed0e1ce` (1.4) · *(este commit)* (Final)

---

## 1. Escopo e objetivo

A Fase 1 do Caminho 2 consolida as séries de entrada do preditor BI bivariado para Manaus 2020-2021:

- **TOH UTI** — taxa de ocupação hospitalar (UTI adulto COVID) derivada da Ficha Técnica MS/FVS-AM
- **SRAG** — síndrome respiratória aguda grave notificada via SIVEP-Gripe (INFLUD20/21)

A terceira dimensão proposta (O₂ hospitalar) foi formalmente descartada como Caminho C: sem série retrospectiva canônica disponível; prospectiva aguarda operacionalização futura.

---

## 2. Tarefas e status

| Tarefa | Descrição | Status | Commit |
|--------|-----------|--------|--------|
| 1.1 | TOH UTI Manaus — consolidação 12 meses | ✅ CONCLUÍDA | `236a4ea` |
| 1.2 | SRAG Manaus — infra extração + stub | ✅ CONCLUÍDA | `96b8bb9` |
| 1.3 | Stub Caminho C — decisão O₂ documentada | ✅ CONCLUÍDA | `cd465b6` |
| 1.4 | Validação cruzada bivariada | ✅ CONCLUÍDA | `ed0e1ce` |
| Final | Relatório executivo | ✅ CONCLUÍDA | *(este)* |

---

## 3. Resultados da Tarefa 1.4

### 3.1 Sanity checks TOH (série real, 12 meses)

| Check | Resultado | Status |
|-------|-----------|--------|
| Pico TOH jan/fev 2021 | `2021-01` — TOH = **104%** | ✅ OK |
| Vale TOH jul/ago 2020 | `2020-08` — TOH = **24%** | ✅ OK |

Os valores confirmam a narrativa epidemiológica da crise Manaus: colapso hospitalar em janeiro 2021 (acima de 100% por internações em macas e corredores) e período inter-ondas com baixa ocupação em agosto 2020.

### 3.2 Correlação de Spearman — FORMALMENTE DIFERIDA

**Status: DIFERIDA para início da Fase 2.**

A validação cruzada plena — Spearman ρ(TOH, SRAG), PCA empírica, comparação A priori vs. PCA — está condicionada à extração do SRAG SIVEP-Gripe real via `opendatasus.saude.gov.br`. O FTP DATASUS para SIVEP-Gripe estava indisponível durante a Fase 1 (migração para OpenDataSUS); o `srag_manaus.parquet` é um stub com 12 meses de zeros (`is_stub=True`).

**Critérios de sucesso não avaliados nesta fase:**
- ρ(TOH, SRAG) > 0.50
- |Δw| PCA vs. A priori < 0.10

Esses critérios permanecem como critérios de aceitação da Fase 2, Tarefa 2.x (extração SRAG real + revalidação).

### 3.3 Decisão de pesos — A priori com PCA diferida

O `bi_dimensional_decision.json` foi gravado com:

```json
{
  "weights_decision_pending": true,
  "decision_method": "apriori_only_pending_pca_validation",
  "weights_final": { "w_TOH": 0.50, "w_SRAG": 0.50 }
}
```

Os pesos finais persistidos são **w_TOH = 0.50, w_SRAG = 0.50** (paridade institucional: Ficha Técnica MS para TOH; SIVEP-Gripe para SRAG). A PCA empírica — que derivaria pesos do PC1 — será executada na Fase 2 após extração do SRAG real. O `decision_method: "apriori_only_pending_pca_validation"` garante que a Fase 2 não herde um JSON ambíguo.

---

## 4. Bug t_mort=0 — diagnóstico

### Causa raiz identificada

O campo `MORTE` no SIH/SUS é codificado como string `'Sim'/'Não'` pelo `microdatasus.process_sih()`, mas o pipeline em `manaus_sih_loader.py` aplica `pd.to_numeric(df['MORTE'], errors='coerce').fillna(0)`, que retorna NaN para strings — resultando em t_mort=0 para todos os 2.678 registros.

**Evidência:** 482 registros com `MORTE == 'Sim'` em Manaus 2020-2021 (detectados pelo `diagnostico_t_mort_zero.md`). Não era zero — era silêncio de conversão.

**Fix Fase 2 (uma linha):**
```python
df['MORTE_NUM'] = (df['MORTE'] == 'Sim').astype(int)
```
substitui `pd.to_numeric(df['MORTE'], errors='coerce').fillna(0)`.

**Implicação retroativa — item de roadmap Fase 3:**  
A Tabela 7 e a Figura 3 do canônico (`PAPER1_CANONICO.md`) foram publicadas com t_mort=0 e declaravam esse valor como achado empírico. Após o fix da Fase 2 e recálculo do θ_eff Markoviano, **Tabela 7 e Figura 3 precisam ser regeneradas na Fase 3** com t_mort ≈ 482 / 2678 ≈ 0.18 (18% de mortalidade intra-hospitalar). O texto narrativo do paper que comentava t_mort=0 como dado empírico precisará ser corrigido para refletir o achado real.

> ⚠️ **Risco Fase 3:** sem este registro, a Fase 3 poderia regenerar Tabela 7 com dados corrigidos sem revisar a narrativa textual que comentava t_mort=0 como fato — resultando em inconsistência interna no paper.

---

## 5. Artefatos gerados

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| `toh_uti_manaus.parquet` | `data/predictors/manaus_bi/` | TOH UTI 12 meses (10 confirmados + 2 estimados) |
| `srag_manaus.parquet` | `data/predictors/manaus_bi/` | SRAG stub 12 meses (zeros, is_stub=True) |
| `oxigenio_unavailable.json` | `data/predictors/manaus_bi/` | Decisão Caminho C documentada |
| `bi_dimensional_decision.json` | `outputs/` | Pesos 50/50 + decision_method + pending flag |
| `bi_series_normalized.png` | `outputs/` | Plot séries normalizadas (TOH real + SRAG stub) |
| `bi_validation_report.md` | `outputs/` | Relatório de validação cruzada com checks |
| `diagnostico_t_mort_zero.md` | `outputs/` | Diagnóstico preciso do bug t_mort |
| `README.md` | `data/predictors/manaus_bi/` | Manifesto de proveniência 12 meses |

---

## 6. Pendências explícitas para a Fase 2

1. **Extração SRAG real** — baixar INFLUD20/21 de `opendatasus.saude.gov.br` e re-executar `extract_srag_manaus.py`
2. **Revalidação cruzada** — re-executar `validate_bi_consistency.py` para calcular ρ e PCA reais
3. **Fix t_mort** — aplicar `(df['MORTE'] == 'Sim').astype(int)` em `manaus_sih_loader.py` → `manaus_bi_loader.py`
4. **Atualização JSON** — atualizar `bi_dimensional_decision.json` com pesos PCA e `decision_method: "pca_validated"`
5. **Roadmap Fase 3** — regenerar Tabela 7 e Figura 3 com t_mort corrigido; revisar narrativa do canônico

---

*Relatório gerado automaticamente ao término da Fase 1. Próxima fase: Fase 2 — Refactor `manaus_sih_loader.py` → `manaus_bi_loader.py`.*
