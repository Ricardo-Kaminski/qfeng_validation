# BRIEFING DE PONTE — Sessão 19-20 abr 2026
# ============================================
# De: chat Claude.ai "pos doc" (sessão longa 19 abr)
# Para: próximo chat Claude.ai + Claude Code
# Gerado em: 20 abr 2026 (manhã)
# Workspace: C:\Workspace\academico\qfeng_validacao

---

## CONTEXTO GERAL

Ricardo da Silva Kaminski — pesquisador sênior, DEMAS/SEIDIGI Ministério da Saúde,
OECD AI Health Expert Group. Projeto: validação empírica do Q-FENG (Quantum-Fractal
Neurosymbolic Governance) — arquitetura de governança cibernética de IA.

Dois outputs acadêmicos em desenvolvimento:
- Paper 1 — Lancet Digital Health: domínio saúde (SUS/Medicaid/EU AI Act)
- Paper 2 — AI & Law / JURIX: domínio jurídico (CLT + TST, âncora: Mata v. Avianca)

Referência canônica WP:
KAMINSKI, R.S. Q-FENG: SSRN 6433122 | DOI: 10.2139/ssrn.6433122

---

## ESTADO DO PIPELINE C1 (estado real ao encerrar sessão)

| Módulo | Status | Detalhe |
|--------|--------|---------|
| E0 ScopeConfig | ✅ COMPLETO | 152→176 testes verdes |
| E1 Saúde | ✅ COMPLETO | 24.111 chunks, sus_validacao |
| E1 Trabalhista | ✅ COMPLETO | 4.486 chunks, advocacia_trabalhista |
| E2 Saúde | ✅ COMPLETO | 5.136 DeonticAtoms, cache em outputs/deontic_cache/ |
| E2 Trabalhista | 🔄 EM EXECUÇÃO | rodando via Claude Code CLI ao encerrar |
| E3 Saúde | ✅ COMPLETO | 2.529/2.530 válidos (99.96%), outputs/e3_predicates/ |
| E3 Trabalhista | 🔒 BLOQUEADO | aguarda E2 trabalhista |
| E4 HITL | 🔒 BLOQUEADO | aguarda E3 saúde aprovado formalmente |
| E5 Symbolic Testing | 🔒 BLOQUEADO | aguarda E4 |

### E3 Saúde — detalhes do resultado aprovado
```
outputs/e3_predicates/
  brasil/  — 1.063 predicados (CF88, Lei 8080, portarias Manaus, PL2338...)
  eu/      — 951 predicados  (EU AI Act: 906, GDPR: 23, Carta: 22)
  usa/     — 516 predicados  (SSA 1902: 379, CFR 435: 55, 1903: 27...)
  concurrent_facts.lp — 329 fatos
Total: 2.530 predicados | 2.529 válidos | 1 inválido
```

### E2 Trabalhista — estado ao encerrar
Iniciado com:
```
python -m qfeng.c1_digestion.deontic.runner \
    --chunks-dir outputs/e1_chunks_trabalhista/ \
    --scope configs/advocacia_trabalhista.yaml \
    --output-dir outputs/deontic_cache_trabalhista/
QFENG_LLM_MODEL=claude-sonnet-4-6  (Max plan, sem custo extra)
```
Verificar status ao iniciar próxima sessão.

---

## CORPUS DISPONÍVEL

### Saúde (sus_validacao) — COMPLETO
```
corpora/brasil/    — 20 docs (CF88, Lei 8080/8142/8689/13709/13979,
                    portarias Manaus 2021, consolidações, PPA, PNS, PL2338)
corpora/eu/        — 3 docs (EU AI Act, GDPR, Carta Direitos)
corpora/usa/       — 10 docs (14ª Emenda, Civil Rights, SSA XIX, 42 CFR,
                    Obermeyer 2019 summary)
```

### Trabalhista (advocacia_trabalhista) — COMPLETO
```
corpora/brasil_trabalhista/
  constitucional/CF88_art7_xiii_xvi.htm     1.41 MB
  legislacao/clt_completa.htm               3.15 MB
  legislacao/lei_13467_2017_reforma.htm     172 KB
  jurisprudencia/livro_jurisprudencia_tst.pdf  3.33 MB
configs/advocacia_trabalhista.yaml          ✅ criado e testado
```

### Dados Empíricos
```
data/predictors/ceaf_medicamentos/    — PRONTO
  model_pharma_sota_v1.pkl + forecast_t12_final.parquet + séries (46 MB)
  Fonte: F:\proj\IADAF (projeto IADAF/LightGBM/CEAF)

data/predictors/manaus_sih/raw/       — .dbc BAIXADOS, conversão pendente
  RDAM2010.dbc → RDAM2103.dbc (6 arquivos, 6 MB)
  PENDENTE: Rscript scripts/converter_dbc_manaus.R
  (requer: install.packages("read.dbc"); pode falhar — alternativa: TabNet manual)
```

---

## AMBIENTE E CONFIGURAÇÃO

```
conda activate qfeng          ← OBRIGATÓRIO antes de qualquer comando
Python: 3.11.15
Clingo: 5.8.0

.env atual:
  QFENG_LLM_MODEL=claude-sonnet-4-6    ← para E2 trabalhista (Max plan)
  QFENG_LLM_MAX_TOKENS=4096

Billing:
  Claude Max plan — Claude + Claude Code compartilham mesmo pool de uso
  0% usage = pool resetou (reseta a cada 5h)
  SEM créditos de API separados necessários enquanto dentro do limite Max
```

---

## PRÓXIMAS AÇÕES IMEDIATAS

### 1. Verificar E2 trabalhista (primeira coisa)
```bash
conda activate qfeng
# Verificar se terminou:
ls outputs/deontic_cache_trabalhista/ | wc -l
# Esperado: ~4.000-5.000 arquivos JSON
# Se ainda rodando: aguardar
# Se concluído: reportar total de atoms e confidence média
```

### 2. Após E2 trabalhista concluído → E3 trabalhista
```bash
python -m qfeng.c1_digestion.translation \
    --deontic-dir outputs/deontic_cache_trabalhista/ \
    --scope configs/advocacia_trabalhista.yaml \
    --concurrency-map outputs/e1_chunks_trabalhista/concurrency_map.json \
    --output-dir outputs/e3_predicates_trabalhista/
```

### 3. E4 HITL — iniciar brainstorming
O E3 saúde está aprovado (99.96% válidos). O E4 pode iniciar em paralelo.
Ler spec: docs/superpowers/specs/ (não há spec E4 ainda — criar)

E4 Goal: classificar predicados como SOVEREIGN ou ELASTIC via interface HITL.
Decisão pendente: Jupyter Notebook ou Streamlit para interface HITL?

### 4. Dados SIH Manaus (quando possível)
```r
# Tentar converter os .dbc:
Rscript scripts/converter_dbc_manaus.R
# Se falhar: baixar via TabNet manualmente
# URL: http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/qruf.def
```

---

## DECISÕES ARQUITETURAIS CANÔNICAS (NÃO reverter)

| Decisão | Escolha |
|---------|---------|
| Motor simbólico | Clingo ASP puro (dPASP rejeitado) |
| Persistência MVP | JSON/filesystem (Neo4j fora) |
| LLM E2 saúde | claude-sonnet-4-6 via Max (cache existente, não re-executar) |
| LLM E2 trabalhista | claude-sonnet-4-6 via Max |
| LLM E5 predictor | Qwen 2.5 14B via Ollama (agente de decisão nos cenários) |
| Concurrency map | Externo ao schemas.py |
| E3 | Template-based puro, sem LLM |
| patient null | Omitir do predicado Clingo (não usar "none") |
| ScopeConfig regimes | {brasil, eu, usa, brasil_trabalhista} |
| _REGIME_ALIAS | {"brasil_trabalhista": "brasil"} no runner (sem modificar schemas.py) |

---

## SPECS E DOCUMENTAÇÃO

```
docs/superpowers/specs/
  2026-04-19-e0-scope-config-design.md      — E0 (completo)
  2026-04-19-predictor-interface-design.md  — 3 predictors ABC + implementações
  2026-04-19-paper2-legal-spec.md           — Paper 2 jurídico completo
  2026-04-19-e3-translation-design.md       — E3 (completo, commitado)

artefatos/briefings/
  BRIEFING_PONTE_producao_academica.md      — ponte com projeto do livro
  BRIEFING_SESSAO_19abr2026_EOD.md          — briefing EOD da sessão anterior
  BRIEFING_SESSAO_19-20abr2026.md           — ESTE ARQUIVO
```

---

## CENÁRIOS E5 DEFINIDOS

### Paper 1 — Saúde
- C1: CEAF medicamentos (LightGBM IADAF) — falha de execução θ≈0
- C2: Manaus 2021 (TimeSeries SIH) — falha de execução θ>120°
- C3: Concentração regional SUS (LightGBM) — falha constitucional θ≈π
- C4a/b/c: Qwen LLM sem/com predicados + θ_efetivo markoviano

### Paper 2 — Jurídico
- T-CLT-01: Citação fantasma (Mata v. Avianca) — falha constitucional θ≈π
- T-CLT-02: Distorção Súmula TST 85 — falha de execução θ>120°
- T-CLT-03: Banco de horas com CCT — predicado elástico correto θ<30°
- T-CLT-04: θ_efetivo markoviano — sequência 8 consultas rescisão trabalhista

---

## NOTAS IMPORTANTES

1. O briefing de ponte com o projeto do livro está em:
   artefatos/briefings/BRIEFING_PONTE_producao_academica.md
   Lê-lo para contexto sobre o Cap. 7, os casos SUS e a posição do PoC
   em relação à demonstração contrafactual do livro.

2. O projeto do livro está em:
   C:\Workspace\academico\govern_ai_paper\livro_final\KAMINSKI_livro_versão_final.docx

3. A frente de advocacia (Paper 2) é Contexto B — PoC acadêmico.
   O produto comercial com Omar Kaminski é trabalho separado futuro.

4. BitNet b1.58 (Microsoft): identificado como extensão futura interessante
   para E5 (testar se compliance-by-construction funciona com modelos ternários).
   NÃO priorizar no MVP.

5. Senha DATASUS venceu — resetar segunda para acesso institucional às bases
   SIH, SIA, CNES com maior granularidade.
