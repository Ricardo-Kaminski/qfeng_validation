# Q-FENG Validation

### Quantum-Fractal Neurosymbolic Governance — Anti-Hallucination Engine

> **A domain-agnostic verification layer that detects normative conflicts in AI outputs  
> using quantum interference theory and Answer Set Programming.**  
> Built with Claude Code · Brazilian Legal & Health Corpora · Clingo/ASP · dPASP-ready

[![Working Paper](https://img.shields.io/badge/SSRN-Working%20Paper-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6433122)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-yellow)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-orange)](https://claude.ai/code)

-----

## The Problem

Every AI assistant operating in regulated domains — health, law, finance, public policy — faces the same structural flaw: **it generates plausible text, not verified truth**.

A model can confidently state that:

- A workplace accident victim can be dismissed with monetary compensation *(wrong — CLT Art. 118 mandates 12-month absolute job stability)*
- A patient can be deprioritized for ICU care based on regional availability *(wrong — SUS universality principle, CF/88 Art. 196)*

This is not a prompt engineering problem. It is an architectural one. Transformers approximate; they do not verify. **Q-FENG adds the verification layer.**

-----

## What Q-FENG Does

Q-FENG sits as a **post-generation module** between any LLM and the end user. It does not modify the model. It does not use prompt injection. It formally validates every normative claim in a generated response against a structured corpus of statutes encoded as logic predicates.

```
User Query
    ↓
Any LLM (Claude / GPT / Gemini / Qwen / local)
    ↓
Generated Response
    ↓
┌──────────────────────────────────────────────┐
│              Q-FENG ENGINE                   │
│                                              │
│  1. Extract normative claims from output     │
│  2. Match claims against predicate corpus    │
│  3. Compute interference angle θ             │
│                                              │
│     θ ≈   0° → PASS   (constructive)        │
│     θ ≈  90° → REVIEW (ambiguous, HITL)     │
│     θ ≈ 180° → BLOCK  (Circuit Breaker)     │
│                                              │
│  4. Return: verified response + audit trail  │
│             norm citation + θ score          │
└──────────────────────────────────────────────┘
    ↓
Safe Output — traceable to statute
```

### The Interference Angle θ

Grounded in Quantum Decision Theory (Busemeyer & Bruza, 2012), θ measures the alignment between a neural prediction state |ψ_N⟩ and a normative constraint state |ψ_S⟩:

```
cos θ = ⟨ψ_N | ψ_S⟩ / (‖ψ_N‖ · ‖ψ_S‖)

cos θ > 0  →  constructive interference  →  claim consistent with norm
cos θ = 0  →  orthogonal                 →  ambiguous, human review
cos θ < 0  →  destructive interference  →  Circuit Breaker activated
```

### Circuit Breaker

When θ approaches 180°, the Circuit Breaker intercepts before delivery and returns the specific article violated, the nature of the conflict, and a corrected interpretation grounded in statute.

### Ontological Sovereignty

Certain predicates — constitutional rights, absolute legal protections, fundamental health guarantees — are encoded as **inviolable constraints**. The symbolic layer cannot be overridden by statistical pressure from the neural component. This is formal anti-hallucination, not prompt-based.

-----

## Two Validation Domains

The Q-FENG engine is **domain-agnostic**. The same interference architecture operates across any normative corpus. This repository contains two active validation tracks, currently developed together in the `main` branch and progressively diverging as each domain matures.

-----

### Domain 1 — Public Health (PoC: Validated ✅)

**Application:** Governance of AI-driven decisions in Brazil’s Unified Health System (SUS), validated against real DATASUS data.

**Validated cases:**

|Case                    |Description                                                   |Interference         |θ        |
|------------------------|--------------------------------------------------------------|---------------------|---------|
|C1 — Manaus 2021        |Oxygen crisis — AI system failed to detect supply collapse    |Constructive (missed)|≈ 0°     |
|C2 — ICU Regional Bias  |LightGBM model deprioritizing North/Northeast regions         |Destructive          |≈ 180°   |
|C3 — CEAF Medications   |Eligibility filter excluding legally entitled patients        |Constructive         |θ > 120° |
|C4 — θ_efetivo Markovian|Sequential consultation history extending interference horizon|Extended             |θ_efetivo|

**Corpus:** SIH/DATASUS · SINAN COVID · CNES · CF/88 Art. 196–200 · SUS portarias

**Pipeline status:**

|Stage|Description               |Status       |
|-----|--------------------------|-------------|
|E0   |Corpus ingestion          |✅ Complete   |
|E1   |Predicate extraction      |✅ Complete   |
|E2   |Embedding & classification|✅ Complete   |
|E3   |Interference validation   |✅ Complete   |
|E4   |HITL interface            |🔄 In progress|
|E5   |Audit trail generation    |🔜 Planned    |

-----

### Domain 2 — Brazilian Law (MVP: Hackathon Track 🚧)

**Application:** Anti-hallucination layer for LLM-based legal assistants operating under Brazilian statute — labor law, constitutional rights, civil and criminal code.

> 🏆 **This track is the focus of the [Built with Opus 4.7 Claude Code Hackathon](https://cerebralvalley.ai/e/built-with-4-7-hackathon) (April 21–26, 2026).** The goal is to extend the validated health PoC into a production-ready legal MVP — exposing Q-FENG as a model-agnostic API layer pluggable into any legal AI product operating in Brazil’s 1.3M+ lawyer market.

**The problem it solves:** Brazilian legal AI platforms generate responses grounded in statistical pattern-matching, not formal statute verification. There is no hallucination prevention layer in the market. Q-FENG provides it as a plug-in compliance sidecar.

**Real example — Circuit Breaker in action:**

```
Query:    "Can I dismiss an employee who had a workplace accident?"

LLM output (unverified):
    "Yes, dismissal is possible with payment of severance compensation."

Q-FENG verification:
    Claim extracted:  "dismissal + monetary compensation = sufficient"
    Norm matched:     CLT Art. 118 — estabilidade provisória 12 meses
    θ calculated:     163.4°
    cos θ:            -0.957 → DESTRUCTIVE INTERFERENCE

    ⛔ CIRCUIT BREAKER ACTIVATED
    Violation: CLT Art. 118 mandates absolute 12-month job stability
               post-accident. Monetary compensation alone is legally
               insufficient and does not substitute reinstatement.
    Corrected: Dismissal is prohibited during the stability period.
               Employer liability includes reinstatement + full wages.
```

**Legal corpus — Brazilian statutes:**

|Corpus                                          |Status       |Chunks|
|------------------------------------------------|-------------|------|
|CLT — Consolidação das Leis do Trabalho         |✅ Complete   |4,486 |
|CF/88 — Fundamental Rights (Arts. 1–17, 193–232)|✅ Complete   |—     |
|TST Súmulas — Labor Court precedents            |🔄 In progress|—     |
|Código Civil                                    |🔜 Planned    |—     |
|Código Penal                                    |🔜 Planned    |—     |
|Lei 8.213/91 — Social Security                  |🔜 Planned    |—     |
|LGPD — Data Protection                          |🔜 Planned    |—     |

**Predicate classification:**

- **RIGID** — inviolable norms: constitutional guarantees, absolute protections (Ontological Sovereignty)
- **ELASTIC** — interpretable norms: procedural rules, deadlines, jurisprudential weight

**Hackathon deliverable:** A Claude-powered legal assistant with Q-FENG running as the verification sidecar. Every response carries a θ score, a norm citation, and a conformity status (PASS / REVIEW / BLOCK).

-----

## Architecture

```
qfeng_validation/
├── src/qfeng/
│   ├── core/
│   │   ├── interference.py       # θ calculation engine (domain-agnostic)
│   │   ├── schemas.py            # Pydantic data models
│   │   └── circuit_breaker.py   # Interception + audit logic
│   ├── c1_digestion/             # Normative corpus ingestion (E1)
│   ├── c2_embedding/             # Predicate extraction — Clingo/ASP (E2)
│   ├── c3_classification/        # Rigid/Elastic classification (E3)
│   ├── c4_hitl/                  # Human-in-the-loop interface (E4)
│   └── c5_audit/                 # Audit trail + Canal de Auditoria (E5)
├── corpus/
│   ├── health/                   # SUS, DATASUS, SIH, CF/88 Art.196–200
│   └── legal/                    # CLT, CF/88, TST Súmulas
├── outputs/
│   ├── deontic_cache/            # Extracted predicates (~4,486 chunks)
│   └── interference_logs/        # θ traces per query, per domain
├── tests/
│   └── symbolic_unit_tests/      # Norm compliance test battery
└── CLAUDE.md                     # Claude Code project context
```

**Stack:**

- Language: Python 3.11
- Symbolic reasoning: **Clingo** (Answer Set Programming — Potassco)
- Architecture target: **dPASP** (differentiable Probabilistic ASP, C4AI/USP) — migration roadmap active
- LLM inference: Ollama (Qwen2.5 local) + Claude API (Opus 4.7)
- Built with: **Claude Code**
- Environment: conda `qfeng`

> **On dPASP:** The current PoC uses Clingo (classical ASP) as the symbolic solver. The Q-FENG architecture is designed for progressive migration to full dPASP — which adds learnable probabilistic weights to ASP rules, enabling normative constraints to be refined via backpropagation. This is the target for the production version.

-----

## Theoretical Foundation

|Pillar                      |Framework                                   |Reference                                 |
|----------------------------|--------------------------------------------|------------------------------------------|
|Normative conflict detection|Quantum Decision Theory (QDT)               |Busemeyer & Bruza, 2012                   |
|Symbolic reasoning          |Answer Set Programming / dPASP              |Clingo (Potassco); Cozman & Mauá, C4AI/USP|
|Governance architecture     |Viable System Model (VSM)                   |Beer, 1972                                |
|Performativity              |Callon/MacKenzie STS                        |MacKenzie, 2006                           |
|Original contribution       |θ_efetivo — Markovian interference extension|Kaminski, 2026                            |

Full formalization:
📄 **[Q-FENG: A Control Architecture for Stochastic Sociotechnical Systems](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6433122)** — SSRN, 2026

-----

## Roadmap

|Phase             |Description                                 |Status           |
|------------------|--------------------------------------------|-----------------|
|PoC Health        |Interference engine validated on SUS/DATASUS|✅ E1–E3 complete |
|PoC Legal         |CLT + CF/88 predicate extraction            |✅ E1–E2 complete |
|MVP Legal         |Claude legal assistant + Q-FENG sidecar     |🔄 Hackathon track|
|API Layer         |Model-agnostic REST API (θ + audit trail)   |🔜 Post-hackathon |
|dPASP migration   |Learnable normative weights                 |🔜 Research phase |
|Multi-jurisdiction|EU AI Act + Brazilian PL 2338/2023          |🔜 JURIX 2026     |

-----

## Getting Started

```bash
git clone https://github.com/Ricardo-Kaminski/qfeng_validation.git
cd qfeng_validation
conda activate qfeng
pip install -e ".[dev]"

# Run interference engine on a legal claim
python -m qfeng.core.interference \
  --claim "dismissal with compensation is sufficient for accident victim" \
  --corpus legal/clt

# Run full health validation pipeline
python -m qfeng.c1_digestion.run --corpus health

# Run symbolic unit tests
pytest tests/symbolic_unit_tests/
```

-----

## Author

**Ricardo da Silva Kaminski**
Senior Data Scientist · Ministry of Health of Brazil (DEMAS/SEIDIGI)
OECD AI Health Expert Group
ORCID: [0000-0002-8882-9248](https://orcid.org/0000-0002-8882-9248)

-----

## Citation

```bibtex
@misc{kaminski2026qfeng,
  title   = {Quantum-Fractal Neurosymbolic Governance (Q-FENG):
             A Control Architecture for Stochastic Sociotechnical Systems},
  author  = {Kaminski, Ricardo da Silva},
  year    = {2026},
  url     = {https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6433122}
}
```

-----

*Built with [Claude Code](https://claude.ai/code) ·
Validated on Brazilian Health & Legal Corpora ·
Clingo/ASP (Potassco) · dPASP-ready (C4AI/USP)*
