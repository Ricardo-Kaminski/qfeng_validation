# CLAUDE.md — Q-FENG C1 Implementation Plan

---

## 🔴 AMBIENTE PYTHON — EXECUTAR ANTES DE QUALQUER COMANDO

**NUNCA usar o conda base. SEMPRE ativar o ambiente dedicado `qfeng`.**

```powershell
# Verificar se o ambiente existe
conda env list

# Se 'qfeng' existir — ativar:
conda activate qfeng

# Se NÃO existir — criar e instalar:
conda create -n qfeng python=3.11 -y
conda activate qfeng
pip install -e ".[dev]"
pip install pysus pandas pyarrow requests beautifulsoup4 lxml
```

**Checklist obrigatório a cada inicialização:**
1. `conda activate qfeng`
2. `python --version` → deve ser 3.11+
3. `python -c "import clingo; print(clingo.__version__)"` → deve ser 5.8.0
4. Só então executar qualquer comando do pipeline

> ⚠️ Se qualquer `pip install` for necessário durante a sessão:
> verificar PRIMEIRO que o ambiente `qfeng` está ativo.
> NUNCA instalar pacotes no conda base.

---

## ⚡ INICIALIZAÇÃO — MemPalace (executar SEMPRE ao abrir o projeto)

Este projeto usa **MemPalace** para orientar Claude Code sobre a estrutura entre sessões.
O `mempalace.yaml` na raiz mapeia todas as "salas" de conhecimento do projeto.

### 1. Carregar o MemPalace

```powershell
Get-Content C:\Workspace\academico\qfeng_validacao\mempalace.yaml
```

| Sala                  | Conteúdo                                                    |
|-----------------------|-------------------------------------------------------------|
| `core_engine`         | schemas.py + interference.py — **NÃO modificar**           |
| `c1_pipeline`         | Módulos E0→E5 (E0/E1/E2 completos, E3 em implementação)    |
| `corpora_brasil`      | CF/88, Lei 8.080, portarias SUS, portarias Manaus 2021      |
| `corpora_eu`          | EU AI Act, GDPR, Carta de Direitos                          |
| `corpora_usa`         | Medicaid/SSA Title XIX, CFR 42, Obermeyer 2019              |
| `corpora_trabalhista` | CLT jornada/rescisão, Lei 13.467, Súmulas TST               |
| `data_predictors`     | CEAF/LightGBM (F:\proj\IADAF copiado), Manaus SIH (a obter)|
| `test_suites`         | pytest test_core + test_e0→e5 (152 testes passando)         |
| `configuration`       | pyproject.toml, CLAUDE.md, CORPUS_MANIFEST                  |
| `scripts`             | download_corpus_trabalhista.py, extract_manaus_sih_*.py/R   |

### 2. LightRAG

> ⚠️ O vault do Obsidian contém documentos pessoais gerais, **não** os referenciais
> teóricos do Q-FENG. Não usar `query_rag` para contexto teórico neste projeto.
> O LightRAG é infraestrutura futura — ignorar por ora.

---

## Project Context

Q-FENG (Quantum-Fractal Neurosymbolic Governance) is a cybernetic AI architecture for
monitoring and evaluation of public policies. This repository implements the **empirical
validation** across **dois domínios e dois papers**:

- **Paper 1 — Lancet Digital Health**: infraestrutura crítica de saúde (SUS/Medicaid/EU AI Act)
- **Paper 2 — AI & Law / JURIX**: raciocínio jurídico assistido por LLM (CLT + TST, âncora: Mata v. Avianca)

The C1 pipeline transforms raw normative documents into executable Clingo/dPASP
predicates through stages E0→E5. **O mesmo core serve os dois domínios** — o que muda
é o ScopeConfig e o corpus.

## Current State (19 abr 2026)

| Módulo | Status | Observação |
|--------|--------|------------|
| E0 ScopeConfig | ✅ COMPLETO | 152 testes, Fase B aprovada |
| E1 Ingestion | ✅ COMPLETO | 24.111 chunks (sus_validacao) |
| E2 Deontic | ✅ COMPLETO | 5.136 DeonticAtoms, cache em outputs/deontic_cache/ |
| E3 Translation | 🔄 EM IMPLEMENTAÇÃO | Abordagem 1 (template-based) aprovada |
| E4 HITL | 🔒 BLOQUEADO | aguarda E3 |
| E5 Symbolic Testing | 🔒 BLOQUEADO | aguarda E4 |

**LLM Backend:** `ollama/qwen2.5:14b` (local, zero custo API)
**Configuração:** `.env` — `QFENG_LLM_MODEL=ollama/qwen2.5:14b`, `QFENG_LLM_MAX_TOKENS=2048`

**Corpus:**
- `sus_validacao`: Brasil (20 docs) + EU (3) + USA (10) = 33 docs ✅
- `advocacia_trabalhista`: a construir após E3 (`scripts/download_corpus_trabalhista.py`)

## Architecture Constraints

- **Clingo ASP puro**: motor simbólico, sem dPASP
- **Neo4j**: NOT in MVP — use JSON/filesystem para persistência
- **LangGraph**: NOT in MVP — chamadas diretas ao pipeline
- **litellm via Ollama**: LLM backbone para E2 (qwen2.5:14b local)
- **schemas.py é contrato** — módulos comunicam APENAS por esses tipos, NÃO MODIFICAR
- **Concurrency map externo**: `outputs/e1_chunks/concurrency_map.json`

---

## ⚠️ REGRA DE PROGRESSÃO — LER ANTES DE QUALQUER COISA

**Cada módulo tem DUAS fases obrigatórias antes de avançar:**

1. **FASE A — Implementação + Testes**: código escrito, `pytest` verde
2. **FASE B — Execução Real**: módulo rodado contra o corpus real com o `ScopeConfig`
   ativo, outputs inspecionados e validados pelo usuário

**Nunca avançar para o próximo módulo sem a aprovação explícita do usuário após a Fase B.**
O módulo só está concluído quando o usuário disser **"pode avançar"**.

---

## Implementation Plan — Execute in Order

### MODULE 0: E0 ✅ COMPLETO

### MODULE 1: E1 ✅ COMPLETO

### MODULE 2: E2 ✅ COMPLETO

---

### MODULE 3: E3 — Translation 🔄 EM IMPLEMENTAÇÃO

**Goal:** DeonticAtom → ClingoPredicate (.lp). Template-based puro (Abordagem 1 aprovada).

**Decisão de design aprovada:**
- Opção B: condições como predicados Clingo com corpo de regra
- Condições `==` → predicado unário
- Condições `>`, `<` → aritmética Clingo
- Strings ambíguas → comentário estruturado
- Sovereignty default: `elastic` (E4 HITL classifica soberano/elástico)

**Mapeamento modality → Clingo:**
```prolog
% obligation (sem condições)
obligated(agent, action).

% obligation (com condições)
obligated(agent, action) :- condition_predicate(X), X > threshold.

% prohibition
:- permitted(agent, action).

% permission
permitted(agent, action) :- condition_predicate.

% faculty
may(agent, action) :- condition_predicate.

% meta-fatos de concorrência
concurrent(atom_id_1, atom_id_2).
```

**Arquivos a criar:**
```
src/qfeng/c1_digestion/translation/
  __init__.py (já existe stub)
  translator.py     (translate_atom: DeonticAtom → ClingoPredicate)
  templates.py      (MODALITY_TEMPLATES: dict de templates Jinja2)
  runner.py         (run_e3_batch: DeonticAtoms + scope → outputs/clingo_rules/)
tests/test_e3/
  test_translator.py
  test_templates.py
  test_runner.py
```

---

### MODULE 4: E4 — Validation (HITL)
> 🔒 BLOQUEADO — inicia após E3 Fase B aprovada

### MODULE 5: E5 — Symbolic Testing
> 🔒 BLOQUEADO — inicia após E4 Fase B aprovada

**Cenários definidos:**
- Saúde: Manaus 2021 (θ≈0), concentração regional SUS (θ≈π), CEAF medicamentos
- Jurídico: T-CLT-01 a T-CLT-04 (âncora: Mata v. Avianca)
- LLM: C4a/C4b/C4c com OllamaQwenPredictor (θ_efetivo markoviano)

### MODULE 6: C1 Pipeline Integration
> 🔒 BLOQUEADO — inicia após E5 Fase B aprovada

---

## Coding Standards

- Python 3.11+, type hints em tudo
- Pydantic v2 — usar schemas de `core/schemas.py`, NÃO criar tipos paralelos
- `ruff check` e `mypy --strict` devem passar
- UTF-8 em tudo, diacríticos PT obrigatórios
- Sem `print()` — usar `rich.console.Console` ou `logging`
- Testes com pytest + fixtures

## Key Schemas (core/schemas.py — NÃO MODIFICAR)

```
NormChunk         → E1 output
DeonticAtom       → E2 output
ClingoPredicate   → E3 output
SymbolicTest      → E5 input
InterferenceResult→ C2 output (futuro)
```

## What NOT to Build

- Neo4j, LangGraph, Web UI, Docker (fora do MVP)
- C2/C3/C4 (fases futuras)
- Modificações em core/schemas.py

---

## Specs disponíveis (docs/superpowers/specs/)

| Arquivo | Conteúdo |
|---------|---------|
| `2026-04-19-e0-scope-config-design.md` | Spec E0 completo |
| `2026-04-19-predictor-interface-design.md` | ABC + 3 predictors (LightGBM, TimeSeries, Ollama) |
| `2026-04-19-paper2-legal-spec.md` | Paper 2 jurídico — CLT + Mata v. Avianca |

---

## FORMAÇÃO ACADÊMICA — REFERÊNCIA CANÔNICA (atualizado 13/abr/2026)

1. **Ph.D. Social Sciences (Comparative Studies)** — UnB | 2019–2025 (concluído)
2. **Master in Data Science & AI** — NUCLIO Digital School, Spain | 2022–2023 (concluído)
3. **M.Sc. in Sociology** — UFC | 2012–2014 (é M.Sc., NUNCA M.A.)
4. **Spec. Applied AI Engineering** — UNIPDS | Em andamento (360h, MEC) — SEPARADO do NUCLIO
5. **Spec. Intelligent Solutions Architecture** — PUC-PR | Em andamento
6. **B.Sc. in AI Sciences** — UNIBF | Em andamento (1º semestre)
7. **B.Sc. in Social Sciences** — UFC | 2004–2010 (é UFC, NÃO UNIBF; é B.Sc., NÃO B.A.)
8. **Law (6 semestres)** — UNIVALI, Itajaí/SC | 1994–1998
9. **Physics (2 semestres, base STEM)** — UFSC | 1999–2000

### ERROS FREQUENTES A EVITAR:
- NUCLIO e UNIPDS são cursos SEPARADOS
- Sociologia UFC é M.Sc., não M.A.
- Social Sciences UFC é B.Sc., não B.A.
- UNIBF é B.Sc. AI Sciences (em andamento), NÃO Social Sciences
- Ricardo NÃO é coautor do relatório OECD 2024 — é MEMBRO do AIHEG

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)

---

## Arquivos canônicos — agents: use ONLY these

### Paper 1 (JURIX 2026)
- **Canônico**: `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`
- Todos os outros `.docx` e `.md` em `docs/papers/` foram removidos (versões superseded).
- Para regenerar o `.md` a partir do canônico: `python scripts/extract_docx_to_md.py`

### Paper 2
- `docs/papers/PAPER2_GOVERNANCE_QFENG.md`

### Scripts ativos (pipeline reproduzível)
```
scripts/download_*.py          ← aquisição de corpus e dados
scripts/extract_*.py           ← extração SIH/DATASUS e docx→md
scripts/_run_e5*.py            ← execução E5 e validação
scripts/_fase*.py              ← validação fases 4/6
scripts/generate_*.py          ← geração de figuras e paper APA7
scripts/figures/               ← figura F1
scripts/monitor_e2.py          ← monitoramento E2
scripts/write_hitl_app.py      ← app HITL
```

### Scripts NÃO existentes (foram one-off, já removidos)
- `apply_*.py` — patches já aplicados ao paper e corpus
- `_inspect_*.py`, `_diagnose_*.py`, `_check_*.py` — diagnósticos de sessão
- `fix_*.py`, `patch_*.py` — correções pontuais já aplicadas

### Artefatos relevantes
- `artefatos/briefings/RELATORIO_AUDITORIA_ARS.md` — relatório completo de auditoria pré-submissão
- `artefatos/briefings/AUDIT_PHASE0_LOG.md` — log de verificações externas (F0-1, F0-2)
- `artefatos/briefings/BRIEFING_CORPUS_CLINGO_*.md` — documentação técnica do corpus

### Corpus Clingo (fonte da verdade normativa)
```
corpora_clingo/brasil/         ← CF/88, SUS, CLT, CPC, Manaus ESPIN
corpora_clingo/eu/             ← EU AI Act, GDPR
corpora_clingo/usa/            ← Medicaid/SSA, Civil Rights 14th Amendment
corpora_clingo/scenarios/      ← facts files por cenário (C2, C7, T-CLT-01..04)
```
