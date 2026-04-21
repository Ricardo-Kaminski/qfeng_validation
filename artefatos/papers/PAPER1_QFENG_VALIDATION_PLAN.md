# Paper 1 — Q-FENG Comprehensive Validation: Section Plan

**Target:** SSRN preprint → ArXiv → Applied Intelligence (Springer) / AI & Society  
**Reviewers:** Paco Herrera (ML/XAI, Granada) · Natalia Rodrigues (AI & Law)  
**Target length:** ~15,500 words  
**Status:** PLAN APROVADO — aguardando redação

---

## Abstract (200 words — draft)

Artificial intelligence systems deployed in critical sociotechnical domains routinely generate outputs that conflict with normative constraints encoded in law, clinical protocol, and administrative regulation. Existing governance frameworks address this tension through ex-post auditing or probabilistic compliance scoring, neither of which provides formal guarantees at inference time. We present an empirical validation of Q-FENG (Quantum-Fractal Neurosymbolic Governance), a cybernetic AI architecture that operationalises normative compliance as a measurable geometric quantity — the Ontological Friction angle θ, computed as the arccosine between a Neural Evidence Vector and a Symbolic Norm Vector derived from executable Answer Set Programs. Seven scenarios across two domains and three normative regimes are evaluated: four public health scenarios (Manaus hospital collapse, SUS regional inequity, Obermeyer racial bias algorithm, and one control) and three labor-law scenarios (LLM phantom citations, hour-bank without collective agreement, and two positive controls). The Born Rule from Quantum Decision Theory provides an interference term absent from classical Bayesian mixtures, yielding a governance suppression metric (10.7–25.2% reduction in violation probability over the classical baseline) that constitutes the measurable quantum advantage. A Markovian extension with anticipatory term maps directly onto Beer's VSM System 4. Threshold robustness sweeps, Monte Carlo psi-weight sensitivity (n=500, 100% regime stability), and bootstrap confidence intervals on SIH/DATASUS microdata (n=1,526) confirm empirical validity. Limitations regarding live CEAF integration, synthetic psi-N calibration, and proof-of-concept threshold provenance are documented.

**Keywords:** AI governance; Answer Set Programming; Quantum Decision Theory; Ontological Friction; Cybernetics; VSM; Labor law; Health informatics

---

## Section Hierarchy

| # | Title | Words | Key Evidence |
|---|-------|-------|-------------|
| 1.1 | The Governance Gap in Deployed AI | 500 | EU AI Act, Obermeyer, T-CLT-01 |
| 1.2 | Q-FENG: Positioning and Contribution | 500 | WP Kaminski 2026, Beer 1979 |
| 1.3 | Paper Structure | 400 | – |
| 2.1 | Quantum Decision Theory as Governance Bridge | 700 | Busemeyer & Bruza 2012; Eq.1-4 |
| 2.2 | Answer Set Programming as Normative Motor | 700 | 17 LP files; SAT/UNSAT dual-run |
| 2.3 | Beer/VSM Cybernetic Framework | 500 | Beer 1979; theta_efetivo_manaus |
| 2.4 | Failure Taxonomy | 600 | 7 scenarios mapped |
| 3.1 | C1 Pipeline E1-E5 Overview | 400 | 5,136 DeonticAtoms, 33 docs |
| 3.2 | Psi Vector Construction | 600 | psi_builder.py; validation parquet |
| 3.3 | Clingo Dual-Run Protocol | 400 | scenario_loader.py |
| 3.4 | Manaus Time-Series Design | 400 | SIH 1,526 admissions + literature |
| 4.1 | Overview: 7 Scenarios | 300 | validation_results.parquet |
| 4.2 | C2 Manaus 2021 | 500 | theta=132.4°, CI=[126.7,131.2], GSP=16.7% |
| 4.3 | C3 SUS Regional Inequity | 400 | theta=134.7°, GSP=25.2% |
| 4.4 | C7 Obermeyer Racial Bias | 400 | theta=133.7°, n=48,784, GSP=10.7% |
| 4.5 | T-CLT-01/04 Citation Pair | 500 | 134° vs 7°, SAT/UNSAT contrastive |
| 4.6 | T-CLT-02/03 Hour Bank Pair | 400 | CB vs STAC, constructive interference |
| 4.7 | Summary Table + Taxonomy Map | 300 | Table 2 + failure_type all 7 |
| 5.1 | Threshold Robustness Sweep | 500 | threshold_robustness.parquet, 35 combos |
| 5.2 | Psi Weight Sensitivity MC | 600 | psi_sensitivity.parquet, 100% stable |
| 5.3 | Bootstrap CI Manaus | 600 | manaus_bootstrap_ci.parquet |
| 5.4 | Markovian Anticipatory Extension | 300 | theta_eff memory + gamma term |
| 6.1 | Compliance-by-Design vs Construction | 400 | EU AI Act Art. 9-11 |
| 6.2 | Comparison to SHAP/LIME XAI | 400 | Preempts Herrera "cosine similarity" |
| 6.3 | Comparison to Neurosymbolic Proposals | 400 | Garcez & Lamb 2020, ProbLog |
| 7.1 | Synthetic psi-N Calibration | 300 | psi_builder.py _PSI_N_RAW |
| 7.2 | CEAF Not Live | 200 | c1_ceaf_facts.lp stub |
| 7.3 | Threshold Provenance | 200 | PoC status declared |
| 7.4 | Single Jurisdiction / Pilot Scale | 200 | BR + USA only |
| 8.1 | Implications for AI Governance Policy | 400 | EU AI Act, failure taxonomy → policy |
| 8.2 | The Quantum Probability Interpretation | 400 | Khrennikov 2010, Busemeyer Ch.1 |
| 9 | Conclusion | 500 | 7 scenarios, future CEAF/C4/EU |
| Tables + References | ~1,400 | |
| **TOTAL** | | **~15,500** | |

---

## Equation List (11 equations, all original unless noted)

| Eq | Name | Derivation |
|----|------|-----------|
| 1 | θ = arccos(ψ_N · ψ_S) | Original, Kaminski 2026 |
| 2 | Born rule P_q(j) = (αψ_N + βψ_S)²/Z | Adapted from Busemeyer & Bruza 2012 |
| 3 | Classical baseline P_cl(j) = α²ψ_N² + β²ψ_S² | Derived for contrast |
| 4 | Interference delta Δ(j) = P_q − P_cl | Original quantum advantage term |
| 5 | Governance Suppression % = (P_cl−P_q)/P_cl × 100 | Original empirical metric |
| 6 | ASP integrity constraint template | Cited: Gelfond & Lifschitz 1988 |
| 7 | ψ_S additive construction | Original |
| 8 | Algedonic signal A(θ, n_sov, n_el, conf) | Original |
| 9 | θ_eff(t) = α(t)θ(t) + (1−α(t))θ_eff(t−1) + γE[θ(t+k)] | Original, Kaminski 2026 Eq. A10 |
| 10 | α(t) = sigmoid(β·Δpressão(t)) | Original, empirically calibrated |
| 11 | L_global = L_perf + λ_ont·max(0, −cos θ) | Original, Kaminski 2026 Eq. 3 |

---

## Figure List (7 figures)

| Fig | Title | Source |
|-----|-------|--------|
| 1 | Theta distribution — 7 scenarios, bimodal | validation_results.parquet |
| 2 | Manaus time series: theta_t + theta_eff + score_pressao | theta_efetivo_manaus.parquet |
| 3 | Born vs Classical: paired bars + GSP annotation | validation_results.parquet |
| 4 | Threshold robustness heatmap (5×7 grid) | threshold_robustness.parquet |
| 5 | Psi weight sensitivity: violin/box per scenario | psi_sensitivity.parquet |
| 6 | Markovian memory effect: shaded area theta_t vs theta_eff | theta_efetivo_manaus.parquet |
| A1 | Q-FENG pipeline architecture | docs/figuras/qfeng_pipeline_saude_v3.svg |

---

## Reviewer Attack Pre-emption Map

| Attack | Reviewer | Section | Evidence |
|--------|----------|---------|---------|
| "theta = cosine similarity" | Herrera | 2.1 + 6.2 | Eq.4 interference delta; GSP 9–25% |
| "psi weights ad hoc" | Herrera | 5.2 | 100% MC stability ±20%, max std=2.01° |
| "ASP not real legal outcomes" | Rodrigues | 2.2 + 4.5 | T-CLT-01/04 contrastive pair; CPC Art.489§1°V |
| "why quantum not Bayesian" | Both | 2.1 + 4 | Constructive/destructive asymmetry; Eq.3 vs Eq.2 |
| "thresholds ad hoc" | Herrera | 5.1 | 6/7 100% stable; T-CLT-02 fails only θ_block=130° |
| "CEAF not live" | Both | 7.2 | Honest limitation; C1 reserved |
| "single jurisdiction" | Rodrigues | 4.2/4.4 + 7.4 | BR+USA; n=1,526+48,784 |

---

## Writing Status

- [ ] Section 1 — Introduction
- [ ] Section 2 — Theoretical Foundations
- [ ] Section 3 — Architecture
- [ ] Section 4 — Empirical Validation
- [ ] Section 5 — Robustness
- [ ] Section 6 — Comparison
- [ ] Section 7 — Limitations
- [ ] Section 8 — Discussion
- [ ] Section 9 — Conclusion
- [ ] Figures (Python scripts)
- [ ] ARS review pass
