# Beyond Compliance: Q-FENG as a Cybernetic Architecture for AI Governance

**Ricardo Kaminski**
Post-doctoral Researcher, [Institution]
ricardoskaminski@gmail.com

**Status:** Draft v0.1 — for ARS review
**Target journal:** Government Information Quarterly (Elsevier)
**Word count:** ~8,500 (body)
**Citation format:** APA 7.0

---

## Abstract

Artificial intelligence governance has expanded rapidly, yet algorithmic accountability failures continue to be documented across healthcare, labour markets, and public administration. This paper argues that the dominant governance frameworks — both principled declarations (Type I) and risk-management regimes (Type II) — are structurally incapable of preventing normative violations because they exhibit functional decoupling: rigorous implementation of compliance *means* without achievement of their declared normative *ends*. We identify Ontological Friction — the structural incompatibility between machine learning's inductive-statistical logic and law's deductive-deontic logic — as the technical mechanism through which decoupling operates. Drawing on an empirical analysis of 27 governance documents across four jurisdictions using fuzzy-set Qualitative Comparative Analysis (fsQCA), we show that no existing framework achieves Type III governance: continuous, machine-executable normative monitoring. We then introduce Q-FENG (Quantum-Fractal Neurosymbolic Governance), a cybernetic architecture that resolves this structural deficit by operationalizing normative alignment as a measurable interference angle θ derived from the inner product of normative state vectors. Empirical illustration across seven scenarios — including the Manaus, Brazil COVID-19 health collapse (2020–2021) and Brazilian labour law disputes — demonstrates that Q-FENG's circuit-breaker activation correctly identifies governance failures across health and legal domains. The paper contributes: (1) a tripartite governance taxonomy grounded in institutional theory; (2) Ontological Friction as a novel theoretical construct linking machine learning epistemology to governance failure; and (3) the first proof-of-concept Type III governance architecture with cross-domain scenario illustration. We conclude with implications for governance design and a pathway toward prospective institutional adoption.

**Keywords:** AI governance; cybernetic governance; normative alignment; institutional theory; functional decoupling; quantum-inspired computing; algorithmic accountability

---

## 1. Introduction

More than 300 AI ethics guidelines and governance frameworks have been produced since 2016 (Jobin et al., 2019). The OECD, the European Union, the United States National Institute of Standards and Technology, major technology corporations, and dozens of national governments have articulated principles, risk taxonomies, and compliance requirements for artificial intelligence systems. The volume of governance output has no precedent in the history of technology regulation.

Yet the accountability gap persists. Obermeyer et al. (2019) demonstrated that a commercial health algorithm used across US hospitals systematically underestimated the medical needs of Black patients — a failure invisible to the compliance structures nominally governing it. Raji et al. (2020) audited 14 major AI systems and found that none could satisfy basic accountability criteria. In Brazil, the 2021 Manaus health crisis exposed the absence of any real-time mechanism capable of triggering normative obligations embedded in the federal constitution and ministerial regulations when hospital capacity collapsed under COVID-19 pressure (Sabino et al., 2021). Across these cases, frameworks declared normative commitments; systems violated them; no governance mechanism detected the violation in real time.

The central question this paper addresses is structural, not implementational: why do governance frameworks fail to prevent the violations they prohibit? The answer proposed here has two components. First, the dominant framework architectures exhibit *functional decoupling* (Bromley & Powell, 2012) — a well-documented organizational phenomenon in which institutions construct rigorous compliance procedures without achieving the substantive outcomes those procedures are meant to secure. Second, functional decoupling in AI governance has a specific technical mechanism: what we term *Ontological Friction*, the structural incompatibility between the inductive-statistical epistemology of machine learning and the deductive-deontic logic of law and normative systems. No framework that lacks a machine-executable representation of normative obligations can bridge this gap.

We introduce a tripartite taxonomy — Type I (principled), Type II (risk-management), Type III (cybernetic) — as a theoretical instrument for classifying governance architectures by their structural capacity to achieve normative alignment. An empirical analysis of 27 governance documents using fuzzy-set Qualitative Comparative Analysis (fsQCA; Ragin, 2008) confirms that no existing framework achieves Type III. We then present Q-FENG (Quantum-Fractal Neurosymbolic Governance) as the first architecture designed from the ground up as Type III, and demonstrate its operation across seven governance scenarios drawn from health policy and labour law.

The paper makes three theoretical contributions. First, the tripartite taxonomy systematizes the governance literature along a dimension — structural capacity for continuous normative monitoring — that existing typologies (Jobin et al., 2019; Hagendorff, 2020) do not address. Second, Ontological Friction provides a theoretical construct that links the machine learning epistemology literature to governance failure analysis, grounding what critics have described as "ethics washing" (Bietti, 2020) in a precise technical mechanism. Third, Q-FENG demonstrates that Type III governance is achievable with current technology — neurosymbolic AI, Answer Set Programming, and quantum-inspired probability — and provides the architectural blueprint for its realization.

The paper is organized as follows. Section 2 develops the tripartite taxonomy and the theoretical framework. Section 3 presents the empirical analysis of the governance landscape. Section 4 describes the Q-FENG architecture. Section 5 presents seven illustrative scenarios. Section 6 discusses theoretical contributions, design implications, and limitations. Section 7 concludes.

---

## 2. A Tripartite Taxonomy of AI Governance

### 2.1 Type I: Principled Governance

The first wave of AI governance produced frameworks organized around ethical principles: fairness, transparency, accountability, privacy, non-maleficence. The OECD Recommendation on AI (2019) — adopted by 46 countries — exemplifies this form: five principles, an implementation framework, and a monitoring mechanism based on self-reporting. The Asilomar AI Principles (2017), the Partnership on AI's tenets, and the IEEE Ethically Aligned Design initiative follow the same architecture. These documents declare normative commitments at a level of generality that allows broad consensus but produces no operational specification of how a deployed system should be evaluated against the declared principles.

Type I frameworks are characterized by three structural features. They formulate governance in terms of values rather than obligations, leaving the translation from principle to operational constraint to the implementing institution. They rely on voluntary adherence or soft law mechanisms. And they have no feedback mechanism: there is no component that monitors deployed systems against declared principles in real time, or that triggers a response when principles are violated.

The governance literature has documented these weaknesses extensively. Mittelstadt et al. (2016) showed that algorithmic ethics frameworks borrow concepts from bioethics without the enforcement mechanisms that make bioethics operationally effective. Hagendorff (2020) reviewed 22 major AI ethics guidelines and found that the principles most frequently invoked — transparency, fairness, accountability — were also the least operationalized. Jobin et al. (2019) mapped 84 guidelines across 14 countries and found convergence on principles but divergence on implementation. The pattern is consistent: Type I frameworks generate normative alignment in text, not in deployed systems.

### 2.2 Type II: Risk-Management Governance

The second generation of governance frameworks replaced ethical principles with risk classification and compliance verification. The EU AI Act (2024) established a four-tier risk hierarchy (unacceptable, high, limited, minimal) with mandatory conformity assessments, technical documentation requirements, and human oversight obligations for high-risk systems. NIST's AI Risk Management Framework (2023) introduced a structured four-function cycle (Govern, Map, Measure, Manage) for AI risk. ISO/IEC 42001 (2023) provides a management system standard for AI organizations. Brazil's Lei Geral de Proteção de Dados (2018) and subsequent federal AI bills incorporate similar risk-stratification logic.

Type II frameworks represent a genuine advance over Type I. They impose binding requirements rather than voluntary commitments. They specify documentation and audit procedures. They create institutional actors — conformity assessment bodies, supervisory authorities — with enforcement powers. The shift from principles to risk management reflects an attempt to address the operationalization deficit identified in Type I.

Nevertheless, Type II frameworks retain a structural limitation: they are organized around point-in-time conformity assessment rather than continuous monitoring. A high-risk AI system under the EU AI Act must undergo a conformity assessment before deployment, but the operational behavior of the system after deployment is not continuously evaluated against the normative obligations embedded in the assessment. The audit is periodic; the system operates continuously. This temporal mismatch means that drift — gradual deterioration of normative alignment — is structurally invisible to the framework until it manifests as a reportable incident.

Power (1997, 2022) documented this pattern across audit regimes generally: the audit society substitutes the audit for the managed reality it claims to verify. Riskwork — the organizational production of risk documentation — becomes decoupled from the actual management of risk. Type II AI governance exhibits the same structure: conformity assessment documents become the object of governance attention, while the operational behavior of deployed systems remains outside the monitoring perimeter.

### 2.3 Functional Decoupling: Why Type II Fails

Bromley and Powell (2012) introduced the concept of *means-ends decoupling* to describe a structural property of organizations operating in institutionally complex environments. Where Type I decoupling (Meyer & Rowan, 1977) refers to formal structures adopted for legitimacy rather than efficiency, means-ends decoupling describes a more insidious form: organizations implement the prescribed governance *means* with full technical rigor while the normative *ends* those means were designed to achieve remain unattained. The means are real; the ends are not.

Means-ends decoupling is not hypocrisy or negligence. It is a structural outcome of institutional design. When compliance procedures are complex, highly visible, and evaluated by external parties (regulators, auditors, civil society), organizations rationally concentrate resources on satisfying the compliance procedure rather than on the substantive outcome the procedure proxies. DiMaggio and Powell (1983) identified isomorphism as the mechanism: organizations in the same regulatory field converge on identical compliance procedures because conformity with the procedures is what the field rewards, regardless of whether the procedures achieve their stated goals.

A clarification is warranted here. Bromley and Powell (2012) studied decoupling *within* organizations — how internal compliance departments implement governance procedures that are structurally disconnected from core operational outcomes. The argument developed here extends this concept to the framework level: the *design* of Type II governance frameworks creates the structural conditions that predictably produce organizational decoupling in implementation. A framework that specifies compliance means (conformity assessments, technical documentation, audit procedures) but not continuous monitoring of ends (deployed system behavior against normative obligations) does not merely *permit* means-ends decoupling — it *structurally requires* it, because implementing organizations have no mechanism through which to connect the compliance procedure to the operational outcome. The framework's architecture and the implementing organization's behavior are thus analyzed at distinct levels, but the first causes the second. This extension of the decoupling concept from organizational to framework-design analysis is the theoretical contribution of §2 of this paper.

AI governance exhibits precisely this structure. The EU AI Act's conformity assessment for high-risk systems requires technical documentation, a description of the monitoring system, and a declaration of conformity. Each of these is a means. The end — that deployed high-risk AI systems not violate fundamental rights, not discriminate, not generate unacceptable safety risks — is not directly measured. Organizations produce documents that satisfy the means while deploying systems whose operational behavior may diverge significantly from the declared ends. Raji et al. (2020) found this pattern in practice: AI audit procedures in major technology companies were designed to pass external scrutiny, not to detect the failures they nominally monitored.

The implication for governance design is precise: Type II frameworks generate compliance theater (Bietti, 2020) not because they are poorly designed, but because their structure — point-in-time conformity assessment of means — is incapable of monitoring ends in a continuously operating system. Addressing functional decoupling requires a fundamentally different architecture, one that continuously evaluates the operational behavior of AI systems against machine-executable representations of normative obligations.

### 2.4 Ontological Friction: The Technical Mechanism

Why is continuous normative monitoring technically difficult? The answer involves a structural epistemological asymmetry that we term *Ontological Friction* (Kaminski, 2026a, §2.3).

Machine learning systems are inductive: they generalize from empirical distributions to predictions about unobserved cases. The outputs they produce — risk scores, classification decisions, resource allocations — are probabilistic statements about the world derived from training data. Legal and normative systems are deductive: they derive obligations from general principles through specified inference rules. The outputs they produce — obligations, prohibitions, permissions — are deontic statements about what *ought* to be the case, derived from constitutional provisions, statutes, and regulations through legal reasoning.

Inductive outputs and deontic obligations are logically heterogeneous. An ML model that predicts a patient's health risk score is generating a real-valued estimate of a conditional probability. A legal norm that obliges a public health system to provide emergency care to all citizens regardless of insurance status is generating a deontic constraint on institutional action. There is no direct logical bridge between the prediction and the norm: the prediction neither implies the obligation nor falsifies it. The governance problem arises because most deployed AI systems in high-stakes domains produce inductive outputs that have practical consequences (resource allocation, access decisions, risk management) that interact with domains governed by deontic norms. The interaction is unmediated: the system's output is operationally consequential but normatively opaque.

This is Ontological Friction. It is structural, not incidental. No amount of principle declaration (Type I) or conformity documentation (Type II) resolves it, because both operate at the level of the governance framework rather than at the interface between the system's operational logic and the normative obligations that govern its consequences. Resolution requires an architecture that explicitly represents normative obligations in machine-executable form and continuously evaluates the gap between the system's operational state and those obligations. This is precisely what Type III governance provides.

---

## 3. The Governance Landscape: Empirical Analysis

### 3.1 Corpus and Method

The empirical analysis draws on the governance document corpus developed in Kaminski (2026a) through a systematic review of AI governance instruments across four jurisdictions: Brazil, the European Union, the United States, and international organizations. The corpus comprises 27 documents, including constitutional provisions, federal statutes, ministerial regulations, technical standards, and international agreements (see Table 1). Documents were selected on the criterion that they contain explicit normative statements about AI systems or algorithmic decision-making in public sector or high-stakes private sector applications.

Each document was analyzed using fuzzy-set Qualitative Comparative Analysis (fsQCA; Ragin, 2008). fsQCA is appropriate for this analysis because it handles small-to-medium N cases (27), allows causal complexity (conjunctural causation), and produces set-theoretic conclusions rather than correlational statistics. Governance frameworks are institutional configurations, not random draws from a population; their causal logic is conjunctural.

Three fuzzy conditions were coded for each document using direct calibration (Ragin, 2008, pp. 85–89): (C1) *Normative Specificity* — the degree to which the document specifies machine-executable normative obligations (full non-membership at 0.05: pure ethical principles; crossover at 0.5: structured risk taxonomy; full membership at 0.95: predicate-level executable rules); (C2) *Monitoring Continuity* — the degree to which the governance mechanism monitors deployed systems continuously rather than episodically (full non-membership: no monitoring provision; crossover: post-incident review required; full membership: real-time continuous monitoring mandated); (C3) *Feedback Executability* — the degree to which the governance mechanism can trigger automated institutional responses to normative violations (full non-membership: no response mechanism; crossover: supervised human-in-the-loop alert; full membership: automatic circuit-breaker activation). It is important to note that C3 was calibrated on governance mechanism design rather than on the *technological capacity* of any specific system: existing frameworks score near 0 on C3 not because they cannot imagine automated responses, but because their institutional design does not specify any response mechanism triggered by deployed-system behavior. Type III classification requires membership ≥ 0.7 in all three conditions simultaneously. Full calibration rules, individual document scores, and the truth-table summary are available from the author as supplementary material.

**Table 1.** Governance document corpus by type assignment.

| Type | N | Representative documents |
|------|---|--------------------------|
| I — Principled | 14 | OECD AI Principles (2019), Asilomar Principles (2017), EU Ethics Guidelines (2019), Montreal Declaration (2018), Partnership on AI Tenets |
| II — Risk-Management | 13 | EU AI Act (2024), NIST AI RMF (2023), ISO/IEC 42001 (2023), Brazil AI Bill (PL 2338/2023), GDPR (2018) with AI provisions, US Executive Order 14110 (2023) |
| III — Cybernetic | 0 | — |

### 3.2 Findings

The fsQCA analysis confirms Type I and Type II as the dominant governance architectures. No document in the corpus scores ≥ 0.7 on all three conditions simultaneously. The necessary condition analysis reveals that Normative Specificity is a necessary (but not sufficient) condition for Monitoring Continuity: no document achieves high monitoring continuity without first achieving substantial normative specificity. This is theoretically coherent — continuous monitoring presupposes a specification of what is being monitored — but it reveals that the majority of Type I documents, with low normative specificity scores, are structurally precluded from achieving continuous monitoring regardless of any other architectural change.

Among Type II documents, the EU AI Act scores highest on Normative Specificity (0.75) due to its detailed conformity assessment requirements, but low on Monitoring Continuity (0.25) because the assessment is pre-deployment only, and very low on Feedback Executability (0.10) because no automatic response mechanism is specified for post-deployment violations. The NIST AI RMF scores similarly: high Specificity (0.65), low Continuity (0.20), minimal Executability (0.05). The pattern is consistent across all 13 Type II documents.

The fsQCA analysis confirms the theoretical prediction: all 27 documents score below the Type III membership threshold (≥ 0.7) on at least one of the three conditions, and in most cases on all three simultaneously. This is consistent with — and expected from — the theoretical derivation of the three conditions from cybernetic governance theory (Conant & Ashby, 1970; Ashby, 1956): no governance instrument designed for periodic compliance assessment was architecturally built to satisfy the Requisite Variety requirement that a regulator must maintain a real-time model of the system it governs. The fsQCA serves here as a systematic clustering instrument, demonstrating that the current governance landscape is fully concentrated in the Type I and Type II configuration space; it does not independently generate the Type III gap as an empirical discovery, but rather confirms that the theoretical gap is unoccupied in practice.

### 3.3 The Type III Gap

The absence of Type III governance from the empirical landscape is a theoretically predicted outcome, not a surprising empirical finding. The three conditions (C1–C3) were derived from first principles of cybernetic governance theory — specifically, Conant and Ashby's (1970) requirement that every effective regulator must model the system it governs — before the 27-document corpus was analyzed. That no existing framework satisfies these conditions is precisely what the theory predicts: governance instruments designed as normative declarations (Type I) or compliance procedures (Type II) were never built to maintain continuous real-time representations of deployed AI system states. The Type III gap is therefore a *prescriptive* architectural claim — this is what governance must structurally achieve — that the fsQCA confirms is currently unoccupied.

The practical content of the gap is precise. No existing framework has a component that (a) represents legal obligations in machine-executable form, (b) evaluates the operational behavior of deployed AI systems against those representations in real time, and (c) automatically triggers institutional responses when the gap between system behavior and normative obligations exceeds a defined threshold.

This gap has a name in the organizational literature. Callon (1998) described how economic models do not merely represent markets but actively perform them — the model and its referent co-constitute each other. MacKenzie (2006) extended this to show that financial models that become widely adopted reshape the very markets they describe. AI governance frameworks face the inverse problem: they represent normative ideals but are structurally disconnected from the systems they govern, so they cannot perform governance — cannot make governance happen in the operational reality of deployed AI systems. The Type III gap is the space between governance-as-text and governance-as-practice.

Filling this gap requires an architecture that resolves Ontological Friction by creating a formal, continuously updated bridge between the inductive outputs of AI systems and the deontic obligations that govern their consequences. This is the design problem Q-FENG addresses.

---

## 4. Q-FENG: Architecture for Type III Governance

### 4.1 Conceptual Overview

Q-FENG (Quantum-Fractal Neurosymbolic Governance) is a cybernetic architecture for continuous normative monitoring of AI systems. Its theoretical lineage is Stafford Beer's Viable System Model (VSM; Beer, 1972), which specifies the recursive control structures necessary for organizational viability, and Conant and Ashby's (1970) theorem that every good regulator of a system must be a model of that system. The theorem is not metaphorical: a governance system that cannot represent the operational state of what it governs cannot regulate it. Type I and Type II frameworks violate this theorem structurally — they model governance requirements but not the systems being governed.

Q-FENG satisfies Conant and Ashby's theorem through a five-stage pipeline (C1) that transforms raw normative texts into a continuously updated normative state representation:

- **E0**: Scope configuration — defines jurisdictional domain, legal corpus, and predictor sources
- **E1**: Ingestion — chunks normative documents into semantically coherent segments
- **E2**: Deontic extraction — extracts DeonticAtoms (obligation, prohibition, permission, faculty) from each chunk using a language model
- **E3**: Translation — converts DeonticAtoms to Clingo Answer Set Programming predicates
- **E4**: Human-in-the-loop validation — classifies predicates as SOVEREIGN (constitutionally irreducible) or ELASTIC (administratively discretionary)
- **E5**: Symbolic testing — executes Clingo against scenario-specific data to compute normative state

The pipeline integrates two distinct epistemic registers: the deontic logic of the legal corpus (represented as ASP predicates and executed by Clingo) and the empirical-probabilistic logic of operational AI predictors (represented as input parameters to the normative computation). The integration point is the interference angle θ, described in §4.3.

The architecture is neurosymbolic in the technical sense: it combines neural-network-based language model processing (E2) with symbolic logic computation (E3–E5 via Clingo). This combination is deliberate. Language models are effective at extracting semantic structure from natural language legal text; symbolic logic is effective at enforcing normative consistency and producing auditable inference chains. Neither alone suffices — language models cannot enforce logical consistency; symbolic systems cannot parse natural language legal corpora at scale.

An important scope boundary applies to the current implementation: the Clingo ASP corpus encodes normative obligations as hard facts rather than defeasible defaults. This means Q-FENG, in its present form, is designed for normative environments where the applicable obligations are non-conflicting within the analyzed scope — environments where constitutional hierarchy and explicit legislative ordering (lex posterior, lex specialis) have already been resolved at the corpus-construction stage (E4 HITL). Legal reasoning in complex real-world deployments frequently involves conflicting norms that require defeasible inference (Governatori, 2013); this is addressed as a planned extension in §6.4. All seven scenarios in this paper were selected to operate within non-conflicting normative contexts. This scope boundary does not limit the theoretical claim — the interference angle θ is agnostic to the underlying normative representation — but it does bound the current implementation's applicability to cases of settled normative ordering.

### 4.2 The Normative State Vectors

*Plain-language summary for non-technical readers*: Q-FENG computes governance alignment by constructing two numeric profiles at each time step — one capturing how much institutional stress the AI system's operational outputs are generating (the pressure profile), and one capturing how many and which normative obligations are actively triggered by the current legal context (the normative profile). The interference angle θ measures how different these two profiles are: when they point in the same direction, the system is operating in alignment with its normative obligations (small θ, STAC); when they point in opposite directions, the system's operational behavior is severely misaligned with what the law requires (large θ, Circuit-Breaker). The quantum-probability formalism provides a principled way to convert this angular distance into action probabilities — the probability that the governance architecture should trigger an intervention. Readers primarily interested in the governance implications may proceed to §4.4 and §5 after this summary.

Q-FENG represents governance state as a pair of vectors in a real-valued Hilbert space. The normative pressure vector **ψ_N** captures the operational state of the AI system being governed: how much normative pressure the system's current outputs generate against the applicable legal corpus. It is derived from empirical predictors — hospital occupancy rates, algorithmic risk scores, resource allocation decisions — normalized and mapped to a probability amplitude vector over three dimensions: action-0 (no intervention required), action-1 (moderate intervention), action-2 (immediate escalation). The construction follows:

ψ_N(t) = normalize(α₀·f₀(x_t), α₁·f₁(x_t), α₂·f₂(x_t))

where f_k are empirical predictor functions, x_t is the operational data at time t, and α_k are domain-calibrated weights.

The sovereign state vector **ψ_S** captures the current normative state of the applicable legal corpus: which obligations and prohibitions are actively triggered given the current operational context. It is derived from Clingo execution of the E3–E4 predicate corpus against the current scenario data. The construction aggregates sovereign predicate activations (constitutionally irreducible obligations) weighted more heavily than elastic predicate activations (administratively discretionary rules):

ψ_S(t) = normalize(β_S · n_sovereign(t) + β_E · n_elastic(t))

where n_sovereign(t) and n_elastic(t) are the counts of active predicates in each category and β_S > β_E reflects the normative priority of constitutional obligations.

Both vectors are unit vectors in their respective spaces. Their inner product is the cosine of the angle between them — a direct measure of normative alignment.

### 4.3 The Interference Angle θ

The central quantity in Q-FENG's governance computation is the interference angle:

**θ(t) = arccos(⟨ψ_N(t) | ψ_S(t)⟩)**

When θ is small (ψ_N and ψ_S are nearly parallel), the operational behavior of the AI system is closely aligned with the activated normative obligations — governance alignment is high. When θ is large (the vectors are nearly orthogonal or anti-parallel), the system's operational behavior is structurally misaligned with what the legal corpus requires — a governance failure is in progress.

The Born-rule probability formalism provides a principled way to derive action probabilities from θ. For action j, the governance-adjusted probability is:

P_q(j) = |⟨j | Z^{-1/2} | ψ⟩|²

where Z = ψ_N ψ_N^T + ψ_S ψ_S^T + 2cos(θ)(ψ_N ψ_S^T) is the interference kernel. The interference term 2cos(θ)(ψ_N ψ_S^T) is the formal expression of the interaction between operational state and normative state. When θ > 90°, cos(θ) < 0, and the interference term suppresses action probabilities relative to the classical Bayesian baseline — a structural property of the Born-rule formulation, not an empirical finding.

The *Governance Suppression Percentage* (GSP) quantifies this suppression:

GSP(θ) = (P_cl(j) − P_q(j)) / P_cl(j) × 100%

where P_cl is the classical Bayesian probability without interference. GSP > 0 for all θ > 90°, meaning Q-FENG structurally reduces the probability of escalation-absent governance responses as normative misalignment increases. This is a theorem about the Born-rule formulation, not a feature calibrated to data.

The *Markovian θ_efetivo* extends the scalar angle to a temporally tracked quantity with adaptive memory:

θ_efetivo(t) = (1 − α(t)) · θ(t) + α(t) · θ_efetivo(t−1)

α(t) = σ(β · Δpressão(t))

where σ is the logistic sigmoid, β controls sensitivity to pressure changes, and Δpressão(t) is the month-on-month change in operational pressure. This formulation gives higher weight to recent history during crisis escalation (large Δpressão → α → 1) and more weight to the current measurement during recovery (Δpressão → 0 → α → 0). The Markovian memory makes θ_efetivo a trajectory indicator, not just a snapshot.

### 4.4 Governance Regime Classification

Q-FENG classifies governance state into three regimes based on θ:

- **STAC** (Stabilized Sociotechnical Agency Configurations; θ < 30°): The operational AI system and the normative corpus are nearly aligned. No institutional escalation is required. The system is operating within its normatively sanctioned envelope.
- **Alert Zone** (30° ≤ θ < 120°): Partial misalignment. Monitoring intensification is indicated, but the governance margin has not been exhausted.
- **Circuit-Breaker** (CB; θ ≥ 120°): The interference between operational state and normative state is severe. The Born-rule probability of the least interventionist action is maximally suppressed. The governance architecture triggers mandatory institutional escalation.

The thresholds (30° and 120°) are set *a priori* from the theoretical structure of the interference angle, not calibrated on the empirical scenarios. The 120° Circuit-Breaker threshold corresponds to the point at which P_q(action-0) < P_cl(action-0) × (1/2), ensuring that the governance architecture is structurally biased toward intervention in states of severe misalignment. The 30° STAC threshold corresponds to cos(30°) = 0.87, where the operational and normative vectors share more than 75% of their variance. Both thresholds are interpretable in terms of the geometric content of the interference angle.

This threshold structure resolves the circularity concern that might arise if thresholds were calibrated on the scenarios they subsequently classify: because thresholds are defined by the theory of the interference angle, not by the empirical results, the scenario classifications are genuine predictions, not post-hoc fits.

The language of "mandatory institutional escalation" requires a legal qualification. In constitutional systems that protect due process and administrative regularity — including Brazil (CF/88 Art. 5, LV), the European Union (Charter of Fundamental Rights, Art. 41), and the United States — automated governmental decisions affecting individual rights are legally constrained. GDPR Article 22 restricts automated decision-making with legal or similarly significant effects; Brazil's Lei Geral de Proteção de Dados (Art. 20) contains analogous provisions. The circuit-breaker mechanism in Q-FENG does not produce automated *decisions*: it produces automated *signals* that trigger human-institutional review. The escalation path from θ ≥ 120° to a governmental response is always mediated by institutional actors with legally defined competencies and due-process obligations. Q-FENG's contribution is to make the normative misalignment signal formally legible and machine-generated; the institutional response remains a human-institutional act. This distinction is architecturally designed and legally essential.

### 4.5 Why θ Resolves Ontological Friction

Ontological Friction, as defined in §2.4, is the absence of a formal bridge between inductive operational outputs and deontic normative obligations. θ is precisely such a bridge. It is computed from two vectors that respectively represent the inductive operational domain (ψ_N, derived from empirical predictors) and the deontic normative domain (ψ_S, derived from Clingo execution of legal predicates). Their inner product — the cosine of θ — quantifies the structural gap between these two logics at each time step.

θ does not eliminate Ontological Friction. The two epistemic domains remain structurally distinct. What θ provides is a continuous, numerical measurement of the magnitude of friction at any given operational moment. This measurement is what Type I and Type II frameworks lack: a real-time signal that makes normative misalignment visible to institutional actors before harm occurs. The circuit-breaker mechanism translates the measurement into an institutional response, closing the feedback loop that the Conant-Ashby theorem requires.

A geometric interpretation of θ is available and should be stated explicitly: since ψ_N and ψ_S are both unit-normalized vectors, the inner product ⟨ψ_N|ψ_S⟩ = cos(θ) is the standard cosine similarity between the two governance profiles. A reader who prefers to think geometrically can understand the entire θ computation as measuring the angle between two normalized direction vectors in a three-dimensional action space — no quantum mechanics required for this interpretation.

The quantum-probability formalism adds value beyond the geometric interpretation in three specific ways. First, it provides the Born-rule probability formulation P_q(j) = |⟨j|Z^{-1/2}|ψ⟩|², which converts the angle into calibrated action probabilities with a theoretically grounded interference kernel Z. A pure cosine similarity produces a distance metric; the Born rule produces a probability distribution over institutional actions. Second, the interference kernel Z formally encodes the *interaction* between the two governance profiles — the cross-term 2cos(θ)(ψ_N ψ_S^T) — in a way that has no natural analog in pure geometric similarity, allowing the Governance Suppression Percentage (GSP) to be derived as a mathematical theorem rather than a design choice. Third, the quantum-probability framework (Busemeyer & Bruza, 2012; Pothos & Busemeyer, 2013) provides an established literature for handling joint evaluation of incompatible representations — the core structure of the Ontological Friction problem — with known properties regarding order effects and context-dependence that apply directly to normative evaluation. The geometric interpretation is correct; the quantum-probability interpretation is richer.

---

## 5. Empirical Illustration: Seven Governance Scenarios

The seven scenarios described here are drawn from the empirical validation study in Kaminski (in review). They are presented here as illustration of Q-FENG's governance logic, not as a comprehensive evaluation. Full technical details, reproducibility materials, and statistical robustness analyses appear in the companion paper.

### 5.1 Health Governance: Manaus and SUS Concentration

**Scenario C2 — Manaus COVID-19 crisis (2020–2021)**

The Manaus case is among the most documented AI-governance failures in the Global South context (Sabino et al., 2021). From October 2020 through March 2021, the Amazonas state health system collapsed under the second wave of COVID-19. Hospital occupancy reached 100% in January 2021, with ICU beds occupied beyond capacity and oxygen supplies exhausted. The federal government issued Portaria 69/2021, which implemented constitutional obligations under CF/88 Arts. 196–200 (the universal right to health) and activated emergency coordination mechanisms.

Q-FENG applied to this scenario over a 12-month window (July 2020–June 2021) using real SIH/DATASUS hospital microdata for the crisis months (October 2020–March 2021) and epidemiological estimates consistent with Sabino et al. (2021) and COSEMS-AM bulletins for the inter-wave and recovery periods. Hospital occupancy rates were injected into the Clingo normative corpus monthly. The emergência sanitária predicate activates sovereign obligations when occupancy exceeds 85%.

The Markovian θ_efetivo trajectory over the 12 months shows a governance arc consistent with the documented clinical reality:

- July–September 2020 (inter-wave): θ_efetivo ≈ 62–68° (Alert Zone) — governance margin exists but occupancy is non-trivial
- October 2020: θ_efetivo = 125.3° (CB onset) — Circuit-Breaker first activated
- January 2021 (peak crisis): θ_efetivo = 130.9° (CB, maximum severity)
- April–June 2021 (recovery): θ_efetivo ≈ 75–88° (Alert Zone) — below CB threshold as occupancy falls

The Circuit-Breaker activation in October 2020 — two months before the catastrophic January 2021 peak — corresponds retrospectively to the point at which normative obligations embedded in the Brazilian constitutional health framework were structurally violated by the operational trajectory of the health system. Whether prospective deployment of Q-FENG could have supported earlier intervention is a separate empirical question that requires deployment pilot data; the retrospective demonstration confirms that θ correctly tracks the normative significance of the evolving crisis.

**Scenario C3 — SUS regional concentration**

The Unified Health System (SUS) scenario tests Q-FENG's response to chronic structural violations: systematic underallocation of health resources to peripheral regions relative to constitutional equity requirements (CF/88 Art. 196). The interference angle θ = 134.7° (CB), reflecting a configuration in which the predictor vector — derived from resource allocation data showing severe regional concentration — is strongly misaligned with the normative vector derived from constitutional universal coverage obligations. The scenario demonstrates Q-FENG's capacity to detect structural governance failures that are not crisis events but chronic normative violations.

### 5.2 Labour Law: CLT Scenarios

The labour law scenarios test Q-FENG in a different institutional domain: Brazilian labour law under the Consolidação das Leis do Trabalho (CLT, Brazilian Labour Code) and its interaction with collective bargaining agreements (CBAs). Following the 2017 Labour Reform (Lei 13.467/2017), certain CLT provisions can be modified by CBAs under the constitutional principle of *negociado sobre o legislado* (negotiated over legislated). The normative question Q-FENG operationalizes is: do the conditions for valid CBA modification exist in this case?

**Scenarios T-CLT-01 and T-CLT-02** test working-hours arrangements without a valid CBA. The Clingo corpus activates the prohibition predicate against individual agreements that deviate from CLT hourly limits in the absence of collective negotiation. θ = 134.1° (T-CLT-01) and θ = 127.8° (T-CLT-02): both trigger Circuit-Breaker activation, correctly identifying unlawful arrangements.

**Scenarios T-CLT-03 and T-CLT-04** test the same working-hours configurations with a valid and registered CBA in place. The normative corpus activates the permission predicate for CBA-modified arrangements. The normative state vector ψ_S shifts, reducing the misalignment between the operational arrangement and the normative context. θ = 5.7° (T-CLT-03) and θ = 7.1° (T-CLT-04): both fall in the STAC regime, confirming lawful arrangements.

The contrast between T-CLT-01/02 and T-CLT-03/04 demonstrates Q-FENG's sensitivity to the presence or absence of the normative preconditions that license an exception. The architecture does not classify arrangements as lawful or unlawful through direct rule lookup; it computes the geometric relationship between the operational configuration and the full normative context, which includes both the base prohibition and the conditions under which the prohibition is suspended.

### 5.3 Cross-Domain Summary

Table 2 presents the complete seven-scenario results.

**Table 2.** Q-FENG governance scenario results.

| Scenario | Domain | θ (°) | Regime | GSP (%) | Normative interpretation |
|----------|--------|--------|--------|---------|--------------------------|
| C2 — Manaus | Health | 132.4 | CB | 47.2 | Constitutional health obligations violated by capacity collapse |
| C3 — SUS concentration | Health | 134.7 | CB | 49.8 | Equity obligations violated by chronic underallocation |
| C7 — CEAF medication | Health | 133.7 | CB | 48.6 | Access obligations violated by formulary restriction |
| T-CLT-01 | Labour | 134.1 | CB | 49.0 | Unlawful hours arrangement (no valid CBA) |
| T-CLT-02 | Labour | 127.8 | CB | 44.3 | Unlawful hours arrangement (no valid CBA) |
| T-CLT-03 | Labour | 5.7 | STAC | — | Lawful arrangement (valid CBA present) |
| T-CLT-04 | Labour | 7.1 | STAC | — | Lawful arrangement (valid CBA present) |

*Note.* CB = Circuit-Breaker (θ ≥ 120°). STAC = Stabilized Sociotechnical Agency Configuration (θ < 30°). GSP reported for CB scenarios only; STAC scenarios exhibit constructive rather than destructive interference.

All seven scenarios produce governance regime classifications consistent with independent legal expert assessment of each case. The separation between CB (θ ∈ [127.8°, 134.7°]) and STAC (θ ∈ [5.7°, 7.1°]) is clean: there is no overlap between regimes and the signal-to-noise margin is substantial.

### 5.4 Q-FENG's Added Value Over Rule-Based Approaches

A rule-based predicate counter — classifying scenarios as CB if any SOVEREIGN predicate is violated, otherwise STAC — achieves the same binary regime classification as Q-FENG on these seven scenarios. This is expected: in scenarios with clean normative facts, symbolic logic alone is sufficient for binary classification.

Q-FENG's governance contribution lies beyond binary classification. First, the continuous θ signal carries information that binary classification discards: the Manaus trajectory from θ = 125.3° (October 2020, first CB) to θ = 130.9° (January 2021, maximum severity) maps the escalation of governance failure across time, enabling proportional institutional response rather than uniform alarm. Second, the Born-rule probabilities P_q(j) provide a probabilistic governance assessment — the probability of each institutional action, properly weighted by the interference structure — that a rule counter cannot produce. Third, the Markovian θ_efetivo integrates crisis history into each assessment, reflecting the documented institutional reality that the severity of January 2021 was a consequence of the failure to respond in October-November 2020. Fourth, the GSP quantifies the structural governance suppression as a function of θ — a metric with direct policy interpretability that has no equivalent in rule-based frameworks.

---

## 6. Discussion

### 6.1 Theoretical Contributions

The tripartite taxonomy makes three theoretical contributions to the AI governance literature. First, it provides a classification dimension — structural capacity for continuous normative monitoring — that existing reviews and typologies do not operationalize. Dafoe (2018) distinguishes safety-oriented from principle-oriented AI governance approaches; Cihon (2019) proposes a multi-tier classification of governance instrument types; Ulnicane et al. (2021) develop a governance framing analysis sensitive to whether instruments address technical, ethical, or regulatory dimensions; and Jobin et al. (2019), Hagendorff (2020), and Fjeld et al. (2020) map frameworks by the principles they invoke or the regulatory instrument they employ (guidelines, standards, binding law). The tripartite taxonomy builds on these contributions by introducing *monitoring continuity* and *feedback executability* as orthogonal dimensions absent from existing typologies. This functional classification — what the architecture can do, not what it says — reveals the Type III gap that principle-based and instrument-based typologies cannot detect, because they are not designed to ask whether a governance architecture can model the system it governs in real time.

Second, Ontological Friction provides a theoretical construct that connects two literatures that have developed largely in parallel: the AI ethics critique (Mittelstadt et al., 2016; Hagendorff, 2020; Bietti, 2020), which documents the failure of governance frameworks without fully explaining the mechanism of failure, and the philosophy of machine learning (Floridi et al., 2021; Janssen & Kuk, 2016), which analyzes the epistemological properties of ML systems without connecting them to governance architecture. Ontological Friction bridges these literatures by specifying the technical mechanism — inductive-deductive epistemic incompatibility — through which governance frameworks cannot achieve their declared normative ends without a formal interface layer.

Third, θ provides the first continuous, real-time normative alignment metric for AI systems. Existing accountability metrics — fairness measures (Dwork et al., 2012), transparency scores, audit pass rates — are static, domain-specific, and disconnected from the operational trajectory of deployed systems. θ is dynamic, domain-agnostic (tested across health and labour law), and measured continuously against the active normative state of the applicable legal corpus. Its construction from verifiable legal predicates makes it auditable in a way that learned fairness metrics are not: the normative content of ψ_S is derived directly from constitutional texts and statutes, not from training data.

### 6.2 Governance Design Implications

The cybernetic perspective derived from Beer (1972) and Conant and Ashby (1970) has a direct design implication: governance systems must be at least as complex as the systems they govern. The Law of Requisite Variety (Ashby, 1956) states that the variety of a controller must match the variety of the system being controlled. Type I and Type II governance frameworks violate this law: they are structurally simpler than the AI systems they purport to govern, incapable of representing the operational states those systems traverse.

Q-FENG satisfies Requisite Variety by constructing a normative model (the ψ_S vector updated by Clingo execution) that tracks the active legal obligations in real time as a function of operational inputs. The model complexity scales with the normative corpus and the operational domain rather than with the administrative complexity of the compliance procedure.

For governance design practitioners, this analysis suggests a pathway toward Type III adoption that does not require wholesale regulatory replacement. The first step is *normative digitization*: translating existing legal obligations into machine-executable predicates (the E3–E4 pipeline). The second step is *operational connectivity*: establishing data feeds from deployed AI systems to the normative monitoring architecture. The third step is *threshold governance*: defining institutional responses triggered by θ crossing defined thresholds. Steps one and two are technical prerequisites; step three is an institutional design decision that can be phased over time. The full Q-FENG architecture represents the mature form of this pathway, but intermediate stages are deployable with current regulatory and technical infrastructure.

Constitutional anchoring of sovereign predicates — the E4 HITL classification of obligations as SOVEREIGN (constitutionally irreducible) versus ELASTIC (administratively discretionary) — has a governance design implication as well. It provides a formal basis for distinguishing governance requirements that can be subject to compliance flexibility from those that cannot. In the Manaus scenario, the constitutional obligation to provide emergency health care (CF/88 Art. 196) is SOVEREIGN: no administrative arrangement can suspend it. The specific operational protocols for emergency response are ELASTIC: subject to administrative discretion. The SOVEREIGN/ELASTIC distinction operationalizes the constitutional theory of hierarchical normative ordering in a machine-executable form.

A critical qualification must be stated explicitly: *detection is a necessary but not sufficient condition for governance outcomes*. Q-FENG produces a normative misalignment signal — the θ trajectory and the CB activation — but does not produce the institutional response. The Manaus retrospective analysis shows that Q-FENG would have generated a CB signal in October 2020; it does not follow that a governmental response would have occurred, because the documented failure in that case also involved political decision-making, resource allocation priorities, and inter-governmental coordination failures that no monitoring architecture can address. This distinction matters for how Type III governance should be positioned: it fills the *detection* gap that Type I and Type II frameworks leave open, but the translation from detection to response requires institutional actors with legitimate authority, adequate resources, and political incentives to act. Designing the institutional pathway from θ signal to governmental response — including alert routing, escalation authority, response protocols, and accountability for non-response — is a governance design task that sits beyond the technical scope of Q-FENG itself. This pathway is the subject of ongoing institutional design work and is sketched in §6.4 as a future research direction.

### 6.3 Comparison with Adjacent Approaches

Algorithmic auditing (Raji et al., 2020) addresses governance failures through structured external review of AI systems. Audits are valuable but episodically conducted, typically triggered by incident reports or regulatory mandates, and produce binary verdicts (compliant/non-compliant) rather than continuous signals. Q-FENG and algorithmic auditing are complementary rather than competing: θ monitoring provides continuous early warning; auditing provides deep investigation when θ triggers an escalation response.

Regulatory sandboxes, introduced by the EU AI Act and several national frameworks, create bounded environments for testing high-risk AI systems under relaxed compliance requirements. They address the deployment-barrier problem (strict compliance requirements deter innovation in high-risk domains) but do not address the monitoring problem (behavior in sandbox conditions may not predict behavior at scale). Q-FENG is deployable in sandbox and production environments; the θ signal is equally valid in both.

Model cards (Mitchell et al., 2019) provide static documentation of AI system properties, intended to support informed deployment decisions. They address transparency but not continuous monitoring: a model card describes a system at a point in time, not its operational trajectory. The relationship between Q-FENG and model cards is sequential: model card information (training data provenance, known failure modes, performance metrics) can be incorporated into the E0–E2 pipeline to initialize the normative corpus and predictor configuration.

Explainable AI (XAI; Arrieta et al., 2020) provides post-hoc explanations of AI system decisions, addressing the transparency deficit. XAI explanations are decision-level; Q-FENG monitoring is system-level. They operate at different granularities and are complementary: XAI can explain why a specific decision generated a θ spike; Q-FENG tracks the aggregate normative trajectory.

### 6.4 Limitations

Several limitations of the current study warrant explicit acknowledgment.

**Scope**: The empirical illustration uses seven scenarios across two legal domains in a single jurisdiction (Brazil). While the cross-domain generalizability across health and labour law is encouraging, validation across additional jurisdictions and normative domains is needed before Type III claims can be generalized. The EU and US normative corpora included in the broader Q-FENG corpus (Kaminski, in review) provide a starting point for multi-jurisdictional extension.

**Defeasible reasoning** *(significant scope limitation)*: As noted in §4.1, the current Clingo implementation encodes normative obligations as hard ASP facts, not as defeasible defaults. This is a significant constraint, because legal reasoning in real-world deployments is fundamentally defeasible: later-in-time statutes override earlier ones, lex specialis overrides lex generalis, constitutional provisions override statutory ones, and CBAs can override CLT defaults within constitutionally defined limits. The seven scenarios in this paper were deliberately constructed within non-conflicting normative contexts — cases where the applicable normative ordering is clear — precisely because the current implementation cannot resolve genuine normative conflicts through defeasible inference. A governance monitoring system deployed in complex regulatory environments (multi-agency jurisdiction, layered constitutional-statutory-regulatory hierarchies, temporally evolving legislative landscapes) would immediately encounter conflicts that the current architecture cannot handle. Defeasible ASP semantics (Governatori, 2013; Modgil & Prakken, 2013) are planned for implementation in the full governance monitoring suite; until that extension is complete, Q-FENG should be understood as a proof-of-concept designed for normative environments with settled hierarchical ordering, not as a production-ready system for general-purpose legal reasoning.

**Prospective deployment**: All seven scenarios are retrospective: Q-FENG was applied to cases with known normative outcomes. Whether the θ signal provides actionable early warning in prospective deployment — before normative violations manifest as documented harms — requires field deployment data that is not yet available. The Manaus retrospective analysis demonstrates that θ crossed the CB threshold two months before the crisis peak, which is consistent with early-warning potential, but prospective confirmation requires a controlled deployment study.

**Annotation consistency**: The E4 HITL predicate classification (SOVEREIGN/ELASTIC) relies on domain expert annotation. Inter-annotator consistency was not formally measured in the current PoC. Perturbation analysis (±20% variation in ψ weighting) shows that regime classifications are robust to annotation-level noise of this magnitude, but a formal inter-annotator reliability study is needed for production deployment.

---

## 7. Conclusion

The structural failure of AI governance frameworks is not a contingent failure of implementation or political will. It is a consequence of architectural design: frameworks that lack machine-executable representations of normative obligations and continuous monitoring mechanisms cannot achieve the normative alignment they declare. The tripartite taxonomy presented here provides a conceptual instrument for diagnosing this architectural deficit, and Ontological Friction provides its technical explanation.

Q-FENG provides proof-of-concept that Type III governance is achievable with current technology. The interference angle θ bridges the inductive-deductive epistemic gap that Type I and Type II frameworks leave unresolved. The circuit-breaker mechanism translates continuous normative monitoring into institutional responses that are proportional, auditable, and constitutionally grounded. A proof-of-concept illustration across seven scenarios shows that θ correctly identifies governance failures in health and labour law domains, with clean separation between circuit-breaker and stable-alignment regimes; full empirical validation across additional jurisdictions and prospective deployment settings is the subject of ongoing work (Kaminski, in review).

Three implications follow for AI governance policy. First, new governance instruments should be evaluated on the tripartite taxonomy before adoption: does the proposed framework achieve Type II, or does it provide the continuous monitoring mechanisms needed for Type III? The expansion of AI governance frameworks without addressing the Type III gap generates compliance theater without accountability outcomes. Second, the normative digitization step — translating existing legal obligations into machine-executable predicates — is a prerequisite for any Type III architecture and should be prioritized in governance reform agendas. Third, constitutional anchoring of sovereign predicates provides a formal basis for distinguishing governance flexibility from governance non-negotiability, which is essential for the legitimacy of automated normative monitoring systems.

Future work addresses three open questions. First, multi-jurisdictional validation is needed to test whether the normative predicate engineering methodology generalizes across civil law, common law, and hybrid legal systems. Second, prospective deployment pilots — in which θ monitoring operates in real time alongside deployed AI systems — are needed to confirm early-warning potential. Third, defeasible ASP semantics will be integrated to handle conflicting normative provisions in complex legal domains. Parallel papers address the health equity (Obermeyer et al., 2019) and legal AI (labour law at scale) implications of the Q-FENG architecture.

The governance problem is architectural. The solution must be architectural as well.

---

## Declarations

**Data Availability Statement**: Empirical data (SIH/DATASUS), normative corpora (public regulatory documents), Clingo predicate files, and scenario results are available at [repository URL upon acceptance].

**Ethics Declaration**: No human subjects were involved. Health data used under public access provisions of Brazilian SUS microdata policy.

**Author Contributions** (CRediT): Ricardo Kaminski — Conceptualization, Methodology, Software, Formal Analysis, Writing (original draft), Writing (review & editing), Visualization.

**Conflict of Interest Statement**: The author declares no competing interests.

**Funding Acknowledgment**: This research received no specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**AI Usage Statement**: Claude Sonnet (Anthropic) was used for draft structuring and text refinement. All theoretical claims, empirical results, and citations were verified by the author. Responsibility for errors remains with the author.

---

## References

Arrieta, A. B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion*, *58*, 82–115. https://doi.org/10.1016/j.inffus.2019.12.012

Ashby, W. R. (1956). *An introduction to cybernetics*. Chapman & Hall.

Beer, S. (1972). *Brain of the firm*. Allen Lane.

Bietti, E. (2020). From ethics washing to ethics bashing: A view on tech ethics from within moral philosophy. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 210–219). ACM. https://doi.org/10.1145/3351095.3372860

Bromley, P., & Powell, W. W. (2012). From smoke and mirrors to walking the talk: Decoupling in the contemporary world. *Academy of Management Annals*, *6*(1), 483–530. https://doi.org/10.5465/19416520.2012.684462

Busemeyer, J. R., & Bruza, P. D. (2012). *Quantum models of cognition and decision*. Cambridge University Press. https://doi.org/10.1017/CBO9780511997716

Callon, M. (1998). Introduction: The embeddedness of economic markets in economics. In M. Callon (Ed.), *The laws of the markets* (pp. 1–57). Blackwell.

Cihon, P. (2019). *Standards for AI governance: International standards to enable global coordination in AI research and development*. Future of Humanity Institute, University of Oxford. [Author: verify DOI/URL before submission]

Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, *1*(2), 89–97. https://doi.org/10.1080/00207727008920220

Dafoe, A. (2018). *AI governance: A research agenda*. Future of Humanity Institute, University of Oxford. [Author: verify version/URL before submission]

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, *48*(2), 147–160. https://doi.org/10.2307/2095101

Dwork, C., Hardt, M., Pitassi, T., Reingold, O., & Zemel, R. (2012). Fairness through awareness. In *Proceedings of the 3rd Innovations in Theoretical Computer Science Conference* (pp. 214–226). ACM. https://doi.org/10.1145/2090236.2090255

EU AI Act. (2024). *Regulation (EU) 2024/1689 of the European Parliament and of the Council on artificial intelligence*. Official Journal of the European Union.

Fjeld, J., Achten, N., Hilligoss, H., Nagy, A., & Srikumar, M. (2020). *Principled artificial intelligence: Mapping consensus in ethical and rights-based approaches to principles for AI*. Berkman Klein Center for Internet & Society Research Publication.

Floridi, L., Cowls, J., King, T. C., & Taddeo, M. (2021). How to design AI for social good: Seven essential factors. *Science and Engineering Ethics*, *26*(3), 1771–1796. https://doi.org/10.1007/s11948-020-00213-5

Governatori, G. (2013). Representing business contracts in RuleML. *International Journal of Cooperative Information Systems*, *14*(2–3), 181–216. https://doi.org/10.1142/S021884300500112X

Hagendorff, T. (2020). The ethics of AI ethics: An evaluation of guidelines. *Minds and Machines*, *30*(1), 99–120. https://doi.org/10.1007/s11023-020-09517-8

Janssen, M., & Kuk, G. (2016). The challenges and limits of big data algorithms in technocratic governance. *Government Information Quarterly*, *33*(3), 371–377. https://doi.org/10.1016/j.giq.2016.08.011

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, *1*(9), 389–399. https://doi.org/10.1038/s42256-019-0088-2

Kaminski, R. (2025). *A governança da inteligência artificial como problema de controle cibernético: Fricção ontológica, desacoplamento funcional e configurações sociotécnicas estáveis* [Doctoral dissertation, University of Brasília]. UnB Repository.

Kaminski, R. (2026a). *A governança cibernética da inteligência artificial: Do compliance ao controle*. [Book manuscript].

Kaminski, R. (in review). Q-FENG validation: Quantum-fractal neurosymbolic governance across health and labour law domains. *Applied Intelligence*.

MacKenzie, D. (2006). *An engine, not a camera: How financial models shape markets*. MIT Press. https://doi.org/10.7551/mitpress/9780262134606.001.0001

Medina, E. (2011). *Cybernetic revolutionaries: Technology and politics in Allende's Chile*. MIT Press.

Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, *83*(2), 340–363. https://doi.org/10.1086/226550

Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (pp. 220–229). ACM. https://doi.org/10.1145/3287560.3287596

Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). The ethics of algorithms: Mapping the debate. *Big Data & Society*, *3*(2). https://doi.org/10.1177/2053951716679679

Modgil, S., & Prakken, H. (2013). A general account of argumentation with preferences. *Artificial Intelligence*, *195*, 361–397. https://doi.org/10.1016/j.artint.2012.10.008

NIST. (2023). *Artificial intelligence risk management framework (AI RMF 1.0)*. National Institute of Standards and Technology. https://doi.org/10.6028/NIST.AI.100-1

Noble, S. U. (2018). *Algorithms of oppression: How search engines reinforce racism*. NYU Press.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, *366*(6464), 447–453. https://doi.org/10.1126/science.aax2342

OECD. (2019). *Recommendation of the Council on Artificial Intelligence* (OECD/LEGAL/0449). Organisation for Economic Co-operation and Development.

Power, M. (1997). *The audit society: Rituals of verification*. Oxford University Press.

Power, M. (2022). *Riskwork: Essays on the organizational life of risk management*. Oxford University Press.

Pothos, E. M., & Busemeyer, J. R. (2013). Can quantum probability provide a new direction for cognitive modeling? *Behavioral and Brain Sciences*, *36*(3), 255–274. https://doi.org/10.1017/S0140525X12001525

Ragin, C. C. (2008). *Redesigning social inquiry: Fuzzy sets and beyond*. University of Chicago Press. https://doi.org/10.7208/chicago/9780226702797.001.0001

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency* (pp. 33–44). ACM. https://doi.org/10.1145/3351095.3372873

Sabino, E. C., Buss, L. F., Carvalho, M. P. S., Prete, C. A., Crispim, M. A. E., Fraiji, N. A., Pereira, R. H. M., Patifa, K. V., da Silva Peixoto, P., Ogliari, M. K., Salomon, T., Ferreira, A. Y. N., Nelson, C. W., Andricopulo, A., Miyajima, F., Segurado, A. C., & Pybus, O. (2021). SARS-CoV-2 variants of concern in Brazil: A second wave of the COVID-19 pandemic and emergence of the P.1 lineage. *The Lancet*, *397*(10272), 374–375. https://doi.org/10.1016/S0140-6736(21)00183-5

Ulnicane, I., Knight, W., Leach, T., Stahl, B. C., & Curran-Troop, W. (2021). Framing governance for a contested emerging technology: Insights from AI policy. *Policy and Society*, *40*(2), 158–177. [Author: verify DOI before submission]
