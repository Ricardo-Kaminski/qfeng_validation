# Appendix — The Q-FENG Normative Corpus: Architecture, Audit Methodology, and Engineering of Sovereignty Classification

This appendix presents the full architecture and audit methodology of the Q-FENG normative corpus implemented as Clingo Answer Set Programming (ASP) facts, rules, and integrity constraints. The corpus is the symbolic substrate from which the normative state vector ψ_S is constructed in stage E5 of the C1 pipeline (§4.5), and consequently the formal grounding of the interference angle θ that operationalizes Ontological Friction as a continuous, computable scalar (§3.1, §3.2).

The appendix is organized as follows. Section A.1 introduces the three-layer normative topology that mirrors the formal hierarchy of Brazilian positive law. Section A.2 specifies the dual-classification scheme (SOVEREIGN/ELASTIC) that defines the legal weight of each predicate. Section A.3 catalogs the active scenario set after the April 2026 audit cycle. Section A.4 presents the canonical normative anchors per scenario in tabular form. Section A.5 reports the audit methodology and discusses the dogmatically dense cases — those in which engineering decisions navigated genuine tensions between textual fidelity, methodological robustness, and computational operability. Section A.6 reports validation results across all seven active scenarios. Section A.7 acknowledges limitations and identifies future work.

---

## A.1 Three-Layer Normative Topology

The corpus is organized in three hierarchically nested layers that mirror the formal stratification of Brazilian positive law (Kelsen 1934; Bobbio 1960). The same architectural principle extends to other jurisdictions in the corpus (EU AI Act, GDPR; US 14th Amendment, Title VI, 42 CFR), with appropriate substitution of the constitutional, statutory, and regulatory primary sources.

**Layer 1 — Constitutional (`brasil/constitucional/`).** The uppermost layer encodes the petreous clauses (CF/88 Art. 60 §4°), foundational principles of the Republic (Art. 1°), fundamental objectives (Art. 3°), fundamental rights and guarantees (Art. 5°), and the common federative competence in health (Art. 23 II, added in the April 2026 audit). Predicates at this layer are classified `sovereign/1` either in the strict petreous sense (entrenched against constitutional amendment under Art. 60 §4°) or in the structuring sense (constitutional norms that ground the operational stratum of the federation, even if not formally entrenched). The distinction between the two senses is documented in inline comments per predicate, following the doctrinal divergence between Mendes (entrenchment of structuring principles is doctrinally defensible) and José Afonso da Silva (only the formally listed clauses of Art. 60 §4° qualify). For the Q-FENG project, the sovereign classification is operational — meaning "irreducible by the immediately subordinate regulatory layer" — and not strictly formal-petreous; this engineering choice is explicit in the corpus headers.

**Layer 2 — Statutory and regulatory.** The intermediate layer encodes legislation enacted by the National Congress and regulatory instruments of executive agencies. For the Brazilian health domain, this includes Lei 8080/1990 (Lei Orgânica da Saúde, including Arts. 2°, 6°, 7°, 15) in `brasil/saude/sus_direito_saude.lp`, Lei 13.979/2020 (COVID-19 emergency framework) and the relevant ministerial portarias and the Decreto AM 43.303/2021 in `brasil/emergencia_manaus/emergencia_sanitaria.lp`. For the procedural domain, CF/88 Art. 93 IX, CPC Art. 489 §1° I-VI, and LINDB Art. 20 (Lei 13.655/2018) are encoded in `brasil/processual/cpc_fundamentacao.lp`. For the labor domain, CF/88 Art. 7° articles, CLT Arts. 59, 59-B, 611-A, 611-B, 818, the consolidated Súmulas TST (notably 85), and OJ SDI-1 233 are encoded in `brasil/trabalhista/clt_direitos_trabalhistas.lp`. Predicates at this layer are classified `sovereign/1` when they are constitutionally anchored (typically through dual-anchoring — see §A.5.4 on Audit LAW-BR-05) and `elastic/1` when they are modulable by infralegal regulatory instruments (e.g., portarias, normative resolutions).

**Layer 3 — Scenarios (`scenarios/`).** The bottom layer encodes factual instances that invoke predicates from Layers 1 and 2 and provide the operational facts (hospital occupancy rates, hour-bank periods, decisions issued, citations used) that activate constraints and trigger the SAT/UNSAT verdict. Each scenario is a self-contained `.lp` file that declares its `constitutional_basis/1`, `statutory_basis/1`, `regulatory_basis/1`, `jurisprudential_basis/1` ground truths and the operational facts of the case under evaluation. The separation between scenarios and the upper layers ensures that scenario instantiation cannot fabricate facts that contradict positive law — the upper layers are immutable from the scenario perspective.

The hierarchical separation is methodologically important because it implements the Kelsenian normative hierarchy operationally: integrity constraints triggered at the constitutional layer cannot be overridden by predicates from infralegal layers, and scenario instantiations cannot instantiate facts that contradict what is positively encoded in superior layers. This is a structural property of the architecture, not merely a convention — it is enforced by the closed-world semantics of Clingo and by the explicit dependency graph among the `.lp` files.


---

## A.2 Dual-Classification Scheme: SOVEREIGN vs. ELASTIC

Each predicate in the corpus is classified into one of two normative weight categories. This classification is the formal operationalization of the legal hierarchy described informally in compliance frameworks but rarely formalized.

**SOVEREIGN predicates** encode normative content that is legally irreducible by the immediately subordinate layer. The classification carries operational consequences: violation of a sovereign predicate by an algorithmic decision triggers the Circuit Breaker (θ ≥ 120°) regardless of the predictor's confidence. Examples include: `dignity_of_human_person` (CF/88 Art. 1° III), `right_to_health_as_duty_of_state` (CF/88 Art. 196), `prohibition_of_discrimination_by_race_origin_color` (CF/88 Art. 3° IV), `obligation_to_ground_decision_in_identified_ratio_decidendi` (CPC Art. 489 §1° V), `prohibition_negotiation_reducing_health_safety` (dual-anchored on CLT Art. 611-B XVII and CF/88 Art. 7° XXII).

**ELASTIC predicates** encode normative content that is modulable by infralegal regulatory instruments — typically ministerial portarias, normative resolutions, or technical fichas. They define the configurable parameters of the regime within statutory bounds. Examples include: `organization_by_complexity_level` (Lei 8080/1990 Art. 7° XI — implementation modulable by Ministry of Health regulation), `working_hours_negotiable_by_cct` (CLT Art. 611-A I — negotiable by collective bargaining within constitutional limits), `burden_of_proof_redistribution_with_motivation` (CLT Art. 818 §1° — judicially modulable provided the redistribution is motivated under CPC Art. 489).

The dual classification is performed during the E4 stage of the C1 pipeline (§4.4), where human reviewers classify each LLM-extracted ClingoPredicate as SOVEREIGN or ELASTIC according to a calibrated protocol. For the saúde scope, all 537 predicates were reviewed in Phase B (April 2026); for the trabalhista scope, the predicates covering working hours, collective bargaining agreements, and TST jurisprudence were classified in the same HITL pass (145 predicates).

The thermodynamic analogy that motivates this classification is rendered explicit in Diagram 8 of the main paper. The normative state space is framed as a free-energy landscape: sovereign predicates define the ground-state energy minimum (the constitutionally mandated configuration); elastic predicates constitute the thermal bath of regulatorily calibratable parameters. The Circuit Breaker threshold corresponds to the energy barrier that the predictor cannot cross without explicit governance intervention.

---

## A.3 Active Scenario Set

The April 2026 audit cycle consolidated the canonical set of validation scenarios. One scenario, **C1 (CEAF Medicamentos)** — originally a LightGBM-based prediction of medication shortage in the Brazilian *Componente Especializado da Assistência Farmacêutica* — was deprecated from the active set. The LightGBM predictor remains operational as an engineering artifact, but the corresponding scenario was determined not to belong to the canonical set of symbolic validation cases for Q-FENG. The deprecated facts file was preserved in `corpora_clingo/_deprecated/c1_ceaf_facts.lp` with explanatory header for historical traceability and as a reference for "paths not taken" in the methodological discussion. The normative coverage that grounded C1 — Lei 8080/1990 Art. 6° I d (right to integral pharmaceutical assistance) — was retained in `sus_direito_saude.lp` as a sovereign predicate of broad applicability to future health scenarios involving medication continuity.

The active scenario set comprises seven cases distributed across two normative domains and three jurisdictions:

| Scenario | Domain | Jurisdiction | Expected regime | Failure type |
|---|---|---|---|---|
| **C2** Manaus 2021 hospital collapse | Health | Brazil | UNSAT (CIRCUIT_BREAKER, θ ~ 132°) | execution_absent_channel |
| **C3** SUS regional concentration | Health | Brazil | UNSAT (CIRCUIT_BREAKER, θ ~ 134°) | constitutional |
| **C7** Obermeyer Medicaid bias | Health | USA | UNSAT (CIRCUIT_BREAKER, θ ~ 134°) | constitutional |
| **T-CLT-01** Mata v. Avianca / phantom citation | Labor | Brazil | UNSAT (CIRCUIT_BREAKER, θ ~ 134°) | execution_inertia |
| **T-CLT-02** Hour-bank without CCT (8 months) | Labor | Brazil | UNSAT (CIRCUIT_BREAKER, θ ~ 128°) | execution_absent_channel |
| **T-CLT-03** Hour-bank with CCT (10 months, control) | Labor | Brazil | SAT (STAC, θ ~ 6°) | — |
| **T-CLT-04** Grounded citation (positive control) | Labor | Brazil | SAT (STAC, θ ~ 7°) | — |

The seven scenarios collectively instantiate all four failure types defined in §3.5 of the main paper: constitutional failure (the sovereign predicate is absent from the system's operational layer — C3, C7), execution_absent_channel (the sovereign predicate is present but the execution channel is structurally missing — C2, T-CLT-02), execution_inertia (the sovereign predicate is invoked falsely or without proper grounding — T-CLT-01), and STAC (positive controls — T-CLT-03, T-CLT-04).

---

## A.4 Canonical Normative Anchors per Scenario

Table A.4.1 below enumerates the constitutional, statutory, regulatory, and jurisprudential anchors invoked by each active scenario. The complete formalization is in the corresponding scenario `.lp` file under `corpora_clingo/scenarios/`.

### Table A.4.1 — Normative Anchors Per Scenario

| Scenario | Constitutional anchors | Statutory anchors | Regulatory anchors | Jurisprudential anchors |
|---|---|---|---|---|
| **C2** | CF/88 Art. 196 (3 nuclei); Art. 197; Art. 198 II/III; Art. 200 II; Art. 23 II | Lei 8080/1990 Arts. 2°, 6°, 7° I/II/IV, 15 I; Lei 13.979/2020 Arts. 3° I/II/VII/VIII/§7°, 10 | Portaria GM/MS 188/2020 (ESPIN); 356/2020; 454/2020; 197/2021; 79/2021; Decreto AM 43.303/2021 | — |
| **C3** | CF/88 Art. 196 (3 nuclei); Art. 198; Art. 3° III | Lei 8080/1990 Art. 7° I, IV | — | — |
| **C7** | 14th Amendment §1 EPC | Civil Rights Act 1964 Title VI §601 (42 U.S.C. §2000d); Title VI Regulations | 42 CFR §435.4; §440.230(c) | — |
| **T-CLT-01** | CF/88 Art. 93 IX; Art. 5° XXXV | CPC Art. 489 §1° V/VI; LINDB Art. 20 | — | — |
| **T-CLT-02** | CF/88 Art. 7° XIII, XVI | CLT Art. 59 §2, §5; Art. 611-B IX | — | Súmula TST 85 I, V |
| **T-CLT-03** | CF/88 Art. 7° XIII, XXVI | CLT Art. 59 §2; Art. 611-A I, II | — | — |
| **T-CLT-04** | CF/88 Art. 93 IX; Art. 5° XXXV; Art. 7° XXVI | CPC Art. 489 §1° V/VI; LINDB Art. 20; CLT Art. 59 §2; Art. 611-A I | — | TST-Ag-RR-868-65.2021.5.13.0030 |

The asymmetric distribution — C2 has the densest anchor set, C3 has only constitutional and statutory anchors, T-CLT-04 (positive control) has the only verifiable jurisprudential anchor — reflects the substantive structure of each scenario. C2's density encodes the federalism-emergency-protocol cascade specific to Manaus 2021; C3's parsimony reflects that the regional concentration violation is structural-constitutional, not contingent on specific regulatory instruments; T-CLT-04's jurisprudential anchor is the verifiable real precedent that distinguishes it from T-CLT-01 (phantom citation).


---

## A.5 Audit Methodology and Discussion of Dogmatically Significant Cases

### A.5.1 Methodology

The April 2026 audit cycle was conducted in two phases. Phase 1 (semantic audit, in dedicated Opus 4.7 chat sessions) systematically reviewed all `.lp` files of the Brazilian sub-corpus against the canonical legal text of CF/88, Lei 8080/1990, Lei 13.979/2020, the relevant ministerial portarias, the Decreto AM 43.303/2021, CLT, the consolidated TST jurisprudence, and the relevant CPC and LINDB articles. Pendencies were classified into four categories: (A) structural gaps with epistemic impact on active scenarios; (B) anti-patterns of normative engineering; (C) typological coverage gaps; (D) constraint refinements. Phase 2 (operational application, by Claude Code local with OpusPlan) applied the patches produced in Phase 1 with explicit dogmatic checkpoint approval at the close of Block 1 (constitutional gaps). The full audit consolidated 14 numbered audits, 5 of which are new in this cycle (C-5, LAW-BR-05 through LAW-BR-09); the remaining audits had been previously registered and were re-validated within the systematic scope.

The sections below develop in greater depth the audits that involved dogmatically dense decisions — those in which normative engineering had to navigate genuine tensions between textual fidelity, methodological robustness, and computational operability.

### A.5.2 Audit C-5 — Decomposition of CF/88 Art. 196 and Epistemological Grounding of Path 2

CF/88 Art. 196 establishes: *"Health is a right of all and a duty of the State, guaranteed through social and economic policies aimed at reducing the risk of disease and other harms and at universal and equal access to actions and services for its promotion, protection, and recovery."*

Systematic legal interpretation recognizes three distinct normative nuclei in this provision: (i) **right-duty** (the dual subjective-objective structure: right of all / duty of the State); (ii) **reduction of risk of disease and other harms** through social and economic policies; (iii) **universal and equal access** to health actions and services. The original `.lp` implementation collapsed these three nuclei into two clauses sharing the same key `constitutional_basis("CF88_Art196")` — one for the right-duty, one for universal access. The second nucleus (risk reduction) remained implicit but unidentified.

This collapse was specifically problematic for **Path 2 (multi-source BI)**, which reconstructs the Manaus predictor by combining ICU occupancy rate (TOH) + severe acute respiratory syndrome incidence (SRAG) + oxygen logistics as a multivariate time series. The epistemic defense of the BI is: these three series jointly measure "risk of disease and other harms" precisely in the sense of the second nucleus of Art. 196 — TOH measures the risk of healthcare saturation, SRAG measures the risk of severe epidemiological progression, and oxygen logistics measures the risk of therapeutic-logistical breakdown. Without the autonomous predicate `obligation_reduce_disease_risk_via_social_economic_policies`, the defense would have to rest on free interpretation of the constitutional text — fragile under reviewer scrutiny.

After the audit applied the decomposition, the argument acquires structure: the BI predictor is a computational instrument for measuring compliance with the second nucleus of Art. 196 — a direct relation between constitutional text and technical architecture. This is the most robust way to defend the methodological choice of Path 2 before constitutional or public health reviewers.

### A.5.3 Audit C-4 — The Portaria 69/2021 and the Documentary Granularity Problem

The previous version of `emergencia_sanitaria.lp` invoked `regulatory_basis("Portaria69_2021")` as one of the regulatory sources of the C2 Manaus scenario. Documentary audit revealed that GM/MS Portaria 69/2021 concerns vaccine registration in the SI-PNI (Information System of the National Immunization Program) — not hospital calamity nor obligations of supply provision.

This audit is particularly instructive because it illustrates a **characteristic failure mode of LLM-assisted normative extraction pipelines**: the extraction model (E2 of the Q-FENG pipeline, based on Qwen 2.5 few-shots) returned Portaria 69/2021 as a relevant artifact because it appears in contexts close to "COVID-19" and "Manaus" in the training corpus (vaccination registration during the pandemic, Amazonian territory). **Thematic** relevance was captured, but **deontic** relevance (the portaria does not establish an obligation relevant to the scenario) was not. The correction substituted `Decreto AM 43.303/2021` — the effective normative instrument declaring state-level public calamity in Amazonas on January 23, 2021.

This is precisely the function of the **HITL Sovereignty Classification (E4)** stage in the Q-FENG pipeline: not as a decorative phase, but as an indispensable semantic-juridical filter. LLM-extracted predicates must be validated against the actual deontic content of the normative instrument, not merely against thematic co-occurrence. Audit C-4 provides the paradigmatic case that methodologically justifies the systematic human review effort across the 537 health predicates and 145 labor predicates sampled.

### A.5.4 Audits F0-1 / C-6 — Phantom TST Citation and the Hallucination Problem in the Positive Control

The previous version of T-CLT-04 (positive control) invoked the precedent `TST-RR-000200-50.2019.5.02.0020`. Audit revealed that this case number was **fabricated** — it does not exist in the TST database. The fabrication was generated during an earlier prototyping phase in which the goal was to find a plausible precedent for the control, and the hallucination passed initial validation because the format (TST-RR-NNN-NN.AAAA.5.UF.NNNN) is syntactically valid.

The correction (Audit C-6) substituted the precedent with **TST-Ag-RR-868-65.2021.5.13.0030** — a real ruling of the 2nd Panel of the TST, published in DEJT on December 6, 2023, addressing a banking-sector collective bargaining agreement articulated with STF Theme 1046 (ARE 1.121.633). This is the actual precedent that dogmatically grounds the positive control of T-CLT-04 (well-grounded decision with verifiable precedent and identified ratio decidendi).

This audit has an **especially critical** dimension because T-CLT-04 is the **positive control** of the experiment. If the positive control is instantiated with a fabricated precedent, the falsifiability of the entire Q-FENG framework is compromised: how does one distinguish a genuine SAT scenario from a SAT scenario that merely appears valid because the hallucination went undetected? Audit F0-1 documents the detection protocol (cross-reference with public TST databases plus case number verification), and C-6 documents the substitution. The combination ensures that the positive control is **falsifiable and auditable** — a property essential to any system of scientific validation.

The methodological lesson is direct: LLM hallucinations are not restricted to obvious contexts (citations in free-form text); they can appear in syntactically valid structures (well-formatted case numbers) that pass through regex filters but not through existence verification. For Q-FENG and for any NeSy pipeline operating on a juridical corpus, **citation hallucination detection requires systematic cross-reference against authoritative public databases**, not merely syntactic validation.

### A.5.5 Audit LAW-BR-05 — Dual Anchoring and the Problem of Petreous Sustained by Infraconstitutional Norm

The previous version of `clt_direitos_trabalhistas.lp` declared:

```prolog
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII").
```

This formulation has a dogmatic fragility: `sovereign/1` here is asserted from a single statutory anchor (an infraconstitutional norm). But an infraconstitutional norm is not entrenched by itself — it can be revoked or modified by another infraconstitutional norm. The "petreous-fortress" required by the strong-sense classification `sovereign/1` requires constitutional anchoring.

The correction (LAW-BR-05) applies **dual anchoring**:

```prolog
sovereign(prohibition_negotiation_reducing_health_safety) :-
    statutory_basis("CLT_Art611B_XVII"),
    constitutional_basis("CF88_Art7_XXII").
```

CF/88 Art. 7° XXII establishes "reduction of risks inherent to work, through health, hygiene, and safety norms." The combination `CLT_Art611B_XVII ∧ CF88_Art7_XXII` produces a formal chain: the infraconstitutional norm (Art. 611-B XVII) is shielded as petreous because it sustains a right that has explicit constitutional anchoring (Art. 7° XXII). The chain cannot be broken by the ordinary legislator — any revocation of Art. 611-B XVII would leave Art. 7° XXII intact, and the latter would still provide a constitutional basis for the prohibition.

This is the computational version of Kelsenian reasoning: the sovereignty of an inferior-hierarchy norm is only stable if there is anchoring in a superior-hierarchy norm. The corpus engineering must reflect this structure — it is not enough to declare `sovereign/1` mechanically; one must ensure that the chain of foundation reaches a constitutional norm. LAW-BR-05 institutes this pattern and opens space for other apparent-petreous predicates to be reviewed under the same criterion.

### A.5.6 Audit LAW-BR-08 — Operational Thresholds and the Interface Between Law and Empirical Data

The predicates `hospital_capacity_critical :- hospital_occupancy_rate_pct(R), R > 85` and `oxygen_supply_critical :- oxygen_days_remaining(D), D < 3` define **quantitative thresholds** that trigger normative derivations. The problem is: where do these numbers come from?

This is one of the most delicate tensions in any NeSy system applied to law: the formal normative text (CF/88, Lei 8080, Lei 13.979) rarely specifies numerical thresholds; what specifies them are the **technical infralegal instruments** (technical fichas, portarias, best-practice manuals) and the **specialized technical literature**. The corpus must document that chain of foundation so that the thresholds do not appear arbitrary.

LAW-BR-08 implements this documentation:

- **TOH > 85%:** anchored in the **Technical Indicator Sheet for Hospital Care of the Brazilian Ministry of Health** (TOH UTI), prepared by the General Coordination of Hospital Care / DAHU / SAES / MS. There is convergence with the critical Brazilian literature (AMIB — Brazilian Association of Intensive Medicine) which classifies TOH > 85% as operational saturation — a state in which ICU bed waiting time grows non-linearly and mortality from inadequate prioritization increases significantly. The author of Q-FENG is also the author of the Ministry of Health technical sheet, which provides direct institutional anchoring.

- **Oxygen days < 3:** anchored in the **operational precedent of Manaus 2021**. White Martins notified the Ministry of Health on January 14, 2021, that it would be unable to replenish stock within 24-48 hours, configuring an operational point of no return. The threshold of 3 days establishes a minimum lead-time window for triggering emergency requisition (Lei 13.979/2020 Art. 3° VII) or logistical reorganization (air transport, patient redirection).

Additionally, the oxygen threshold was parameterized as a configurable fact: `oxygen_critical_threshold_days(3).` This allows adjustment without modifying the logical predicate — if in another scenario (e.g., another federative unit, another type of input) the canonical threshold differs, only the fact needs to be altered. The separation between **logical predicate** (rule) and **parametric fact** (value) is good normative engineering: it makes the code auditable and adaptable without losing documentary grounding.

The broader lesson of LAW-BR-08 is: **a normative corpus operating on empirical data must document the provenance of its thresholds** with the same rigor as it documents the provenance of its predicates. The law-data interface is where NeSy systems most often fail silently, because the human reader automatically assumes that "obvious" thresholds (85%, 3 days) reflect technical consensus — when in fact they reflect specific institutional decisions that need to be made explicit to be auditable.


---

## A.6 Validation Results

The post-audit corpus was validated through two complementary procedures.

**Per-file syntax check.** Every `.lp` file in `corpora_clingo/` was independently validated via `clingo --syntax-check`. All files passed: `cf88_principios_fundamentais.lp`, `sus_direito_saude.lp`, `emergencia_sanitaria.lp`, `cpc_fundamentacao.lp`, `clt_direitos_trabalhistas.lp`, the seven scenario files in `scenarios/`, and the deprecated `_deprecated/c1_ceaf_facts.lp` (preserved for traceability).

**Integrated per-scenario validation.** The script `scripts/validate_clingo_corpus.py` executes each active scenario by loading the canonical set of `.lp` files it invokes and comparing the resulting Clingo answer-set semantics against the expected SAT/UNSAT regime:

```
========================================================================
INTEGRATED VALIDATION OF Q-FENG CLINGO CORPUS — 26/Apr/2026
========================================================================

[OK] C2_Manaus:                       UNSAT  (expected: UNSAT)
[OK] C3_Concentracao:                 UNSAT  (expected: UNSAT)
[OK] C7_Obermeyer:                    UNSAT  (expected: UNSAT)
[OK] T_CLT_01_Mata_Avianca:           UNSAT  (expected: UNSAT)
[OK] T_CLT_02_Sumula85_Distorcida:    UNSAT  (expected: UNSAT)
[OK] T_CLT_03_Banco_Horas_CCT:        SAT    (expected: SAT)
[OK] T_CLT_04_Citacao_Fundamentada:   SAT    (expected: SAT)

========================================================================
ALL 7 SCENARIOS SUCCESSFULLY VALIDATED.
========================================================================
```

**Zero regressions** were introduced by the audit corrections. Circuit-breaker scenarios remain UNSAT (constraints triggering correctly), and positive controls remain SAT (elastic predicates satisfied without violating sovereign constraints). The audit thus increases the dogmatic robustness of the corpus while preserving its operational behavior — the substantive content of the corrections is in the documentary anchoring, the dual-anchoring patterns, the typological coverage, and the explicit thresholds, not in the SAT/UNSAT verdicts themselves.


---

## A.7 Limitations and Future Work

### A.7.1 Defeasibility

The current corpus encodes obligations as hard ASP facts. The Q-FENG framework defers the formal treatment of defeasibility — exceptions, hierarchical priority among norms, the strong/weak distinction of permissions (Governatori, Olivieri, Rotolo, and Scannapieco 2013) — to the full governance suite. This limitation is methodologically deliberate at the proof-of-concept stage: hard ASP semantics is sufficient to demonstrate that Ontological Friction can be operationalized as a continuous scalar over a normative state space, and the binary SAT/UNSAT verdicts of the seven canonical scenarios suffice to validate the four failure types of §3.5. For the production version of Q-FENG, integration with defeasible deontic logic is necessary, and is identified in §7.4 of the main paper as a priority direction for the next development cycle.

### A.7.2 Norm-Norm Conflict Arbitration

When two sovereign predicates collide (e.g., right to work versus worker health, or right to health versus budgetary principle), the current corpus does not provide an arbitration mechanism — Clingo would simply return UNSAT. This is acceptable for the seven canonical scenarios, where the failure modes are designed to invoke a single dominant constraint. For scenarios of greater normative complexity, the implementation of arbitration rules (lex posterior, lex specialis, principled balancing) is necessary. The metanormative governance layer (S5) of Q-FENG, which operates over multiple jurisdictions, will require this arbitration mechanism by design.

### A.7.3 English Translation of the Corpus

The bulk of the corpus content is in Portuguese — most predicate identifiers are in English, but the inline doctrinal notes and comments are in Portuguese. For the international submission of Paper 1 (target venues JURIX, AI & Law, JAIR — international audience) and for the S5 layer of Q-FENG (multi-jurisdictional metanormative governance), a careful translation of the comments and doctrinal notes is necessary. Preliminary estimate: 6-12 months as a preparatory research line.

### A.7.4 EU and USA Sub-Corpus Audit

The files `eu/ai_act/eu_ai_act_obligations.lp`, `eu/gdpr/gdpr_data_protection.lp`, `usa/civil_rights/civil_rights_14th.lp`, and `usa/medicaid/medicaid_access.lp` were **outside the scope** of the April 2026 audit, which focused on the Brazilian sub-corpus. A systematic semantic audit of analogous depth is to be conducted on these files before the international submission of Paper 1. The audit is planned to be executed in parallel-silent mode to Path 2 (multi-source BI), with results re-incorporated at the output regeneration phase. The USA sub-corpus audit additionally includes a re-review of `c7_obermeyer_facts.lp` against Obermeyer et al. (2019, Table 2), confirming the 28.8 percentage-point gap reported in the canonical scenario.

### A.7.5 Expanded TST Jurisprudence Coverage

The implemented jurisprudential basis covers TST Súmulas 85 and OJ SDI-1 233, which are sufficient for the four canonical labor scenarios (T-CLT-01 through T-CLT-04). The broader TST jurisprudential base — Súmulas 90 (night-shift premium), 366 (residual minutes), 423 (continuous shifts), OJ SDI-1 297, OJ SDI-1 308, among others — is not yet implemented. Progressive expansion is planned as additional scenarios are instantiated in the labor domain.

### A.7.6 Reproducibility

The full audit cycle, including the validation script, the patches applied, and the consolidated CHANGELOG, is preserved in branch `caminho2` of the public repository at `github.com/Ricardo-Kaminski/qfeng_validation`. The principal commit of this audit cycle is `49808c4`. To reproduce the validation, after cloning the repository and activating the conda environment `qfeng`:

```bash
git checkout caminho2
git log -1 --oneline       # should show 49808c4 or descendant
conda activate qfeng
python scripts/validate_clingo_corpus.py
```

Expected output: `ALL 7 SCENARIOS SUCCESSFULLY VALIDATED.`

---

*End of Appendix.*

*Document produced in Opus 4.7 chat session and recorded by Claude Code local in `docs/papers/paper1/_apendices/apendice_corpus_clingo.md` on 26/Apr/2026, branch `caminho2`.*
