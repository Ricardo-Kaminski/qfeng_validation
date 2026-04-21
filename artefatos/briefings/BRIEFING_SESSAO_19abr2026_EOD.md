# BRIEFING — Sessão 19 abr 2026 (EOD)
# =====================================
# Para: próxima sessão Claude.ai + Claude Code
# Status: fim de dia, tudo commitado

---

## Estado dos módulos

| Módulo | Status | Notas |
|--------|--------|-------|
| E0 ScopeConfig | ✅ COMPLETO | 152 testes, Fase B aprovada |
| E1 Ingestion | ✅ COMPLETO | 24.111 chunks sus_validacao |
| E2 Deontic | ✅ COMPLETO | 5.136 DeonticAtoms, cache em outputs/deontic_cache/ |
| E3 Translation | 🔄 EM IMPLEMENTAÇÃO | writing-plans em andamento, NÃO concluído |
| E4 HITL | 🔒 BLOQUEADO | aguarda E3 |
| E5 Symbolic Testing | 🔒 BLOQUEADO | aguarda E4 |

---

## E3 — estado exato ao encerrar

Design aprovado:
- Abordagem 1: template-based puro, zero LLM
- Opção B: condições viram corpo de regra Clingo
- patient=null/unknown → OMITIR do predicado (não usar "none")
- Sovereignty default: elastic (E4 classifica)

Arquivos a criar:
  src/qfeng/c1_digestion/translation/
    translator.py   — atom_to_predicate(DeonticAtom) → ClingoPredicate
    templates.py    — MODALITY_TEMPLATES dict Jinja2
    runner.py       — batch E2 cache → outputs/e3_predicates/
    __main__.py     — CLI --scope --deontic-dir --output-dir
  tests/test_e3/
    test_translator.py  (12 casos)
    test_runner.py
    test_syntax.py      (validação clingo.Control().add())

Output: outputs/e3_predicates/{regime}/{source}.lp
        outputs/e3_predicates/concurrent_facts.lp

Validação: clingo 5.8.0 API Python

---

## Ambiente

- conda activate qfeng  (SEMPRE antes de qualquer comando)
- Python 3.11.15 ✅
- QFENG_LLM_MODEL=ollama/qwen2.5:14b
- QFENG_LLM_MAX_TOKENS=2048

---

## Corpus disponível

### Saúde (sus_validacao) — COMPLETO
  corpora/brasil/ (20 docs) + eu/ (3) + usa/ (10) = 33 docs

### Trabalhista (advocacia_trabalhista) — COMPLETO
  corpora/brasil_trabalhista/
    constitucional/CF88_art7_xiii_xvi.htm     1.41 MB
    legislacao/clt_completa.htm               3.15 MB
    legislacao/lei_13467_2017_reforma.htm     172 KB
    jurisprudencia/livro_jurisprudencia_tst.pdf  3.33 MB
  configs/advocacia_trabalhista.yaml — criado e testado (4 docs selecionados)

### Dados empíricos

CEAF medicamentos (data/predictors/ceaf_medicamentos/):
  model_pharma_sota_v1.pkl + forecast_t12_final.parquet + séries — PRONTO

Manaus SIH (data/predictors/manaus_sih/raw/):
  RDAM2010.dbc a RDAM2103.dbc — 6 arquivos .dbc baixados, 6 MB
  PENDENTE: converter .dbc → parquet (script: scripts/converter_dbc_manaus.R)
  Fazer na segunda após resetar senha DATASUS

---

## Specs disponíveis

docs/superpowers/specs/
  2026-04-19-e0-scope-config-design.md      — E0 completo
  2026-04-19-predictor-interface-design.md  — 3 predictors (LightGBM, TimeSeries, Ollama)
  2026-04-19-paper2-legal-spec.md           — Paper 2 jurídico + Mata v. Avianca

---

## Dois papers

Paper 1 — Lancet Digital Health
  Domínio: saúde (SUS/Medicaid/EU AI Act)
  Corpus: sus_validacao
  Casos: Manaus 2021 (θ≈0) + concentração regional (θ≈π) + CEAF medicamentos
  Predictor: LightGBM CEAF + TimeSeries SIH

Paper 2 — AI & Law / JURIX
  Domínio: jurídico (CLT + TST)
  Corpus: advocacia_trabalhista
  Âncora empírica: Mata v. Avianca, 678 F.Supp.3d 443 (S.D.N.Y. 2023)
  Casos: T-CLT-01 a T-CLT-04 (citação fantasma, distorção súmula, elástico, θ_efetivo)
  Predictor: OllamaQwenPredictor (Qwen 2.5 14B)

---

## Próximas ações (segunda-feira)

1. claude code: conda activate qfeng → continuar E3 executing-plans
2. Ricardo: converter .dbc Manaus via R (scripts/converter_dbc_manaus.R)
3. Ricardo: resetar senha DATASUS → validar/complementar dados SIH se necessário
4. Após E3 Fase B aprovada: iniciar E4 HITL + predictor_interface.py

---

## Decisões arquiteturais canônicas (NÃO reverter)

- Motor simbólico: Clingo ASP puro (dPASP rejeitado)
- Persistência MVP: JSON/filesystem (Neo4j fora)
- LLM backend: ollama/qwen2.5:14b local (zero custo API)
- Concurrency map: externo ao schemas.py
- E3: template-based puro, sem LLM
- ScopeConfig: regimes válidos = {brasil, eu, usa, brasil_trabalhista}
- patient null → omitir do predicado Clingo
