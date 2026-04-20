# Q-FENG Validation

### Quantum-Fractal Neurosymbolic Governance — Legal Engine

> **Anti-hallucination infrastructure for LLMs operating in normative contexts.**  
> Built with Claude Code · Brazilian Legal Corpus · Clingo/dPASP · Quantum Interference Theory

[![Working Paper](https://img.shields.io/badge/SSRN-Working%20Paper-blue)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6433122)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-yellow)](https://python.org)

-----

## The Problem

Every legal AI assistant today — regardless of the underlying model — operates by **probabilistic generation**: it produces plausible text about statutes, but has no formal mechanism to verify consistency with the actual normative corpus. Legal hallucination is not an engineering bug. It is a structural consequence of the transformer architecture.

A model can confidently state that monetary compensation is sufficient for wrongful termination of an injured worker — and be completely wrong under CLT Art. 118, which mandates absolute 12-month job stability. No prompt engineering fixes this. The model doesn’t *know* the law; it *approximates* it.

**Q-FENG solves this at the architectural level.**

-----

## How It Works

Q-FENG sits as a **post-generation verification layer** between any LLM and the end user. It does not modify the LLM. It does not use prompt injection. It operates as an independent module that formally validates every normative claim in a generated response.

```
User Query
    ↓
LLM (Claude / GPT / Gemini / local model)
    ↓
Generated Response
    ↓
┌─────────────────────────────────────┐
│         Q-FENG ENGINE               │
│                                     │
│  1. Extract normative claims        │
│  2. Compute interference angle θ    │
│     between claim and statute       │
│  3. Classify:                       │
│     θ ≈ 0°   → PASS (consistent)   │
│     θ ≈ 90°  → REVIEW (ambiguous)  │
│     θ ≈ 180° → BLOCK (violation)   │
│  4. Generate audit trail            │
└─────────────────────────────────────┘
    ↓
Verified Response + Norm Citation + θ Score
```

### The Interference Angle θ

Borrowed from quantum decision theory (Busemeyer & Bruza, 2012), θ measures the **alignment between a neural prediction state |ψ_N⟩ and a normative constraint state |ψ_S⟩**:

```
cos θ = ⟨ψ_N | ψ_S⟩ / (‖ψ_N‖ · ‖ψ_S⟩‖)
```

- **cos θ > 0** (θ < 90°): constructive interference — claim aligns with statute
- **cos θ = 0** (θ = 90°): orthogonal — ambiguous zone, human review required
- **cos θ < 0** (θ > 90°): destructive interference — Circuit Breaker activates

### The Circuit Breaker

A hard-stop mechanism triggered when θ approaches 180°. It intercepts the response before delivery and returns:

- The specific article/statute violated
- The nature of the conflict
- A corrected normative interpretation

### Ontological Sovereignty

Certain predicates — constitutional rights, absolute legal protections — are encoded as **inviolable constraints** in the dPASP layer. These cannot be overridden by gradient pressure from the neural component, regardless of training data distribution. This is formal anti-hallucination, not prompt-based.

-----

## Legal Corpus

The current validation corpus covers Brazilian federal legislation, formalized as Clingo then dPASP (differentiable Probabilistic Answer Set Programming) predicates:

|Corpus                                              |Status       |Chunks|Coverage           |
|----------------------------------------------------|-------------|------|-------------------|
|CLT — Consolidação das Leis do Trabalho             |✅ Complete   |4,486 |Full text          |
|CF/88 — Constituição Federal (Direitos Fundamentais)|✅ Complete   |—     |Arts. 1–17, 193–232|
|TST Súmulas (jurisprudência)                        |🔄 In progress|—     |—                  |
|Código Civil                                        |🔜 Planned    |—     |—                  |
|Código Penal                                        |🔜 Planned    |—     |—                  |
|Lei 8.213/91 — Previdência Social                   |🔜 Planned    |—     |—                  |

**Predicate classification:**

- **RIGID** — inviolable norms (constitutional rights, absolute protections)
- **ELASTIC** — interpretable norms (procedural rules, administrative deadlines)

-----

## Real Example: Circuit Breaker in Action

**Query:** “Can I dismiss an employee who had a workplace accident?”

**LLM response (unverified):** “Yes, dismissal is possible with payment of severance compensation.”

**Q-FENG verification:**

```
Claim extracted: "dismissal possible with monetary compensation"
Norm matched:    CLT Art. 118 — estabilidade provisória 12 meses pós-acidente
θ calculated:    163.4°
cos θ:           -0.957 → DESTRUCTIVE INTERFERENCE

⛔ CIRCUIT BREAKER ACTIVATED
Violation: CLT Art. 118 — injured worker holds absolute 12-month job stability.
Monetary compensation alone does not satisfy this requirement.
Corrected guidance: dismissal is legally prohibited during stability period.
```

-----

## Architecture

```
qfeng_validation/
├── src/qfeng/
│   ├── core/
│   │   ├── interference.py      # θ calculation engine
│   │   ├── schemas.py           # Pydantic data models
│   │   └── circuit_breaker.py   # Interception logic
│   ├── c1_digestion/            # Normative corpus ingestion (E1)
│   ├── c2_embedding/            # dPASP predicate extraction (E2)
│   ├── c3_classification/       # Rigid/Elastic classification (E3)
│   ├── c4_hitl/                 # Human-in-the-loop interface (E4)
│   └── c5_audit/                # Audit trail generation (E5)
├── outputs/
│   ├── deontic_cache/           # Extracted predicates (cached)
│   └── interference_logs/       # θ traces per query
├── tests/
└── CLAUDE.md                    # Claude Code context
```

**Stack:** Python 3.11 · Ollama (Qwen2.5) · 
Clingo/ASP (Potassco) — dPASP-ready architecture · Claude Code · conda

-----

## Theoretical Foundation

Q-FENG synthesizes four research traditions:

|Pillar                      |Framework                               |Key Reference          |
|----------------------------|----------------------------------------|-----------------------|
|Symbolic reasoning          |dPASP — differentiable Probabilistic ASP|Cozman & Mauá, C4AI/USP|
|Normative conflict detection|Quantum Decision Theory (QDT)           |Busemeyer & Bruza, 2012|
|Governance architecture     |Viable System Model (VSM)               |Beer, 1972             |
|Institutional performativity|Callon/MacKenzie STS                    |MacKenzie, 2006        |

Full formalization in the working paper:  
📄 **[Q-FENG: A Control Architecture for Stochastic Sociotechnical Systems](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6433122)** — SSRN, 2026

-----

## Getting Started

```bash
# Clone and setup
git clone https://github.com/Ricardo-Kaminski/qfeng_validation.git
cd qfeng_validation
conda activate qfeng

# Install dependencies
pip install -e ".[dev]"

# Run interference engine on a sample claim
python -m qfeng.core.interference --claim "dismissal with compensation is sufficient" \
                                   --corpus clt

# Run full validation pipeline
python -m qfeng.c1_digestion.run --corpus clt
```

-----

## Status

This repository contains the **academic validation PoC** for the Q-FENG framework, currently being extended into a production MVP as part of the **Built with Opus 4.7 Claude Code Hackathon** (April–May 2026).

The MVP will expose Q-FENG as a model-agnostic API layer — pluggable into any LLM-based legal assistant.

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

*Built with [Claude Code](https://claude.ai/code) · Brazilian Legal Corpus · dPASP (C4AI/USP)*
