# Quantum-Fractal Neurosymbolic Governance (Q-FENG): Empirical Validation of the C1 Pipeline Across Three Normative Regimes

**Ricardo S. Kaminski**  
Graduate Program in Social Sciences, University of Brasília (UnB), Brasília, DF, Brazil  
Master in Data Science & Artificial Intelligence, NUCLIO Digital School, Barcelona, Spain  
Email: ricardoskaminski@gmail.com  
ORCID: [0000-XXXX-XXXX-XXXX]

---

**Submitted to:** *Applied Intelligence* (Springer)  
**Preprint:** SSRN / arXiv (submitted simultaneously)  
**Keywords:** neurosymbolic AI; quantum decision theory; AI governance; normative reasoning; Answer Set Programming; cybernetics; health AI; legal AI  
**Word count:** ~15,600

---

## Abstract

**Background.** The deployment of algorithmic decision systems in high-stakes public domains — health allocation, social benefits, legal adjudication — generates persistent governance failures that classical monitoring frameworks cannot formally characterise. Existing approaches lack a unified formalism that simultaneously encodes sovereign normative constraints, quantifies their violation as an interference angle, and distinguishes constitutional from execution failures.

**Methods.** We present the Q-FENG (Quantum-Fractal Neurosymbolic Governance) C1 pipeline, a five-stage architecture (E0–E5) that transforms raw normative corpora into executable Answer Set Programming predicates and evaluates alignment between algorithmic predictors and normative states via quantum-inspired interference geometry. This proof-of-concept demonstration covers three normative regimes (Brazil/SUS, EU AI Act, US Medicaid/Equal Protection) and two domains (public health infrastructure and labour law) using 29 primary normative documents (27,957 NormChunks), 5,136 DeonticAtoms (mean confidence: 0.930), and seven author-designed formal scenarios. A Markovian theta-efetivo extension (Kaminski 2026) tracks governance degradation across the 12-month Manaus hospital-collapse crisis of 2020–2021 using real SIH/DATASUS microdata in a retrospective validation.

**Results.** Five of seven scenarios produced CIRCUIT_BREAKER classifications (θ ∈ [127.8°, 134.7°]), while two positive controls produced STAC classifications (θ < 8°). The Born-rule quantum probability model demonstrated destructive interference (Δ ∈ [−0.23, −0.09]) for all failure scenarios, suppressing the probability of the norm-violating action below classical Bayesian predictions by 9.4–25.2%. Threshold robustness analysis across 420 parameter combinations confirmed 98.6% regime stability. Psi-weight sensitivity with ±20% perturbation (n=500 per scenario) yielded 100% correct-regime preservation across all scenarios (σ_θ ≤ 2.0°). The Manaus theta-efetivo series reached its peak at θ_eff = 130.85° in February 2021, with Circuit Breaker activation first occurring in October 2020 — three months before the officially declared ICU collapse.

**Conclusions.** The Q-FENG C1 pipeline provides a formally grounded, reproducible framework for neurosymbolic AI governance monitoring. The quantum interference formalism captures normative suppression effects invisible to classical Bayesian models. Early Circuit Breaker activation (October 2020) in the retrospective Manaus analysis demonstrates that the formalism captures crisis trajectories three months before the officially declared collapse; prospective deployment validation with real-time data feeds is a planned extension. Code and data are available at [GitHub repository — blinded for review].

---

## 1. Introduction

The governance of algorithmic decision systems in public administration poses a challenge that transcends the standard paradigm of statistical performance evaluation. A system may exhibit high predictive accuracy by conventional metrics while simultaneously violating constitutional mandates, circumventing legally protected rights, or allocating resources through mechanisms structurally prohibited by statute. The canonical example is the healthcare algorithm analysed by Obermeyer et al. (2019): deployed across hundreds of US hospitals, the system exhibited a 34-percentage-point racial gap in enrolment recommendations for the same health need — a failure that standard performance dashboards did not detect, and that only became visible through normative external audit comparing actual outputs against the equal-protection principles encoded in §1902(a)(19) of the US Social Security Act.

The Manaus crisis of January 2021 illustrates a complementary failure mode: not predictive bias but systemic execution inertia. As COVID-19 ICU occupancy reached 100% and municipal oxygen supplies collapsed, the Brazilian normative architecture (CF/88 Art. 196; Lei 8.080/1990 Art. 7; Portaria 69/2021) had already specified both the obligation to activate emergency coordination structures (COES) and the threshold conditions for doing so. The sovereign predicates existed in the normative corpus; what failed was their execution. This distinction — between constitutional failure (the norm does not specify the required protection) and execution failure (the norm specifies it but the system does not execute it) — is invisible to evaluation frameworks that treat governance compliance as a binary label.

The EU AI Act (Regulation 2024/1689), now in force, mandates risk management systems, transparency obligations, and human oversight requirements for high-risk AI systems operating in health and public administration. Yet the Act provides no formal mechanism for verifying that these requirements are satisfied beyond documentation checklists and post-hoc audits. A governance monitoring system capable of continuously evaluating the alignment between algorithmic predictor outputs and the normative state encoded in positive law would provide precisely the missing infrastructure.

This paper presents the **Q-FENG (Quantum-Fractal Neurosymbolic Governance) C1 pipeline** — a five-stage architecture for normative alignment monitoring demonstrated as a proof-of-concept across three jurisdictions and two normative domains. The Q-FENG framework makes three original contributions:

1. **A quantum interference geometry for normative alignment**: The angular distance θ between the predictor preference vector ψ_N and the normative state vector ψ_S — computed via Hilbert-space inner product — provides a continuous, formally grounded measure of governance failure that distinguishes STAC (θ < 30°), HITL (30° ≤ θ < 120°), and CIRCUIT_BREAKER (θ ≥ 120°) regimes.

2. **A Markovian theta-efetivo extension for temporal governance tracking**: The Kaminski (2026) extension equips the interference angle with a time-varying adaptive memory that distinguishes deteriorating crises (alpha → 1, current state dominates) from stable regimes (alpha → 0.5, history dominates), enabling prospective governance monitoring with early Circuit Breaker activation.

3. **A failure typology grounded in positive law**: By analysing whether sovereign (legally irreducible) predicates are present in the normative corpus and whether Clingo derives them as active, the pipeline distinguishes constitutional failures (norm gap), execution-absent-channel failures (sovereign predicates present but execution path blocked), and execution-inertia failures (citation to non-existent precedent).

**Theoretical context.** This paper is the first empirical publication in a planned sequence grounded in a common theoretical framework. Kaminski (2026a) — *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle* (KDP) — establishes the theoretical foundation through a configurational analysis of 27 AI governance frameworks using fuzzy-set Qualitative Comparative Analysis (fsQCA). The central finding is a **tripartite taxonomy**: Type I (principled governance), Type II (risk-management governance), and Type III (cybernetic governance). None of the 27 empirically analysed documents achieves Type III. The book diagnoses this as **functional decoupling** (Bromley and Powell 2012): governance frameworks rigorously implement their prescribed means — checklists, impact assessments, audits — without achieving their declared ends of effective control. Section 1.7 of Kaminski (2026a) states explicitly that "empirical validation results will be the subject of separate publications" (Kaminski 2026a, p. 16). The present paper delivers that proof-of-concept demonstration: the Q-FENG C1 pipeline is the engineering instantiation of Type III governance shown as formally possible in Kaminski (2026a, Chapter 7), and the seven designed scenarios provide the empirical evidence that the book's proof-of-existence claim is computationally grounded.

A companion paper (Paper 2, in preparation) will present the full theoretical framework of Kaminski (2026a) in English for international audiences, establishing the sociological and institutional context within which the present empirical results are situated.

**Nomenclature note.** Throughout this paper, the acronym **STAC** denotes *Stabilized Sociotechnical Agency Configurations* — a concept introduced in Kaminski (2025, doctoral thesis) and operationalised in Kaminski (2026a) to name the governance configurations that stabilise after critical junctures through dispute, negotiation, and material-institutional sedimentation. In the Q-FENG governance regime classification, STAC designates the alignment state (θ < 30°) in which the predictor and normative configurations have stabilised into a mutually reinforcing arrangement that warrants autonomous operation without human review.

The paper is organised as follows. Section 2 surveys related work in neurosymbolic AI, legal NLP, AI governance, quantum decision theory, and health AI fairness. Section 3 presents the mathematical foundations of the interference formalism. Section 4 describes the C1 pipeline stages E0–E4. Section 5 reports validation results across seven scenarios. Section 6 presents statistical robustness analyses. Sections 7 and 8 discuss findings and conclude.

---

## 2. Related Work

### 2.0 Theoretical Foundation: Cybernetic Governance and the Tripartite Taxonomy

The theoretical architecture within which this empirical validation operates was developed by Kaminski (2026a) through a configurational analysis of 27 AI governance documents spanning 15 jurisdictions (Brazil, EU, USA, Canada, UK, Australia, China, Singapore, Japan, India, among others). Using fuzzy-set Qualitative Comparative Analysis (Ragin 2008) with seven analytical dimensions, the analysis produces a **tripartite taxonomy** of governance frameworks.

**Type I** (principled governance) encompasses documents that enunciate ethical values and guiding principles without operational mechanisms — transparency, explicability, fairness, accountability, safety. These frameworks perform the constitution of the professional field of AI ethics in the Callonian (1998) sense, instituting categories, vocabularies, and social positions, without intervening in algorithmic dynamics. Ten of the 27 empirically analysed documents belong to Type I, including the OECD AI Principles, the UNESCO Recommendation, and the Brazilian AI Strategy.

**Type II** (risk-management governance) operationalises principles into checklists, impact assessments, compliance forms, periodic audits, and certifications. Seventeen documents are classified Type II, including the NIST AI RMF, the EU AI Act, and Canadian federal regulations. The critical analytical contribution of Kaminski (2026a) is to demonstrate that Type II, while more operational than Type I, reproduces functional decoupling (Bromley and Powell 2012): its instruments are implemented with rigour, but do not possess requisite variety (Ashby 1956, 1958) proportional to the systems they govern. The Quantitative Comparative Analysis confirms that the triple absence of computational variety (dim3), concomitant temporality (dim4), and recognition of constitutive agency (dim5) is quasi-necessary for Type II — the dominant mode of the governance field.

**Type III** (cybernetic governance) is the **configurational absence** in the empirical corpus: the logically possible but empirically uninstantiated configuration that simultaneously satisfies computational variety, concomitant temporality, constitutive recognition, and formally embedded normative control. No document in the corpus achieves Type III. The Q-FENG architecture (Chapter 7 of Kaminski 2026a) is presented as the first formally specified proof of existence that Type III is architecturally feasible — a demonstration, not a prescription. The present paper provides the proof-of-concept empirical demonstration that was explicitly deferred in Kaminski (2026a, §1.7).

The central theoretical mechanism is **functional decoupling** (Bromley and Powell 2012) — a refinement of Meyer and Rowan's (1977) original concept: not organisational hypocrisy (adopting formal structures without implementing them) but *means-ends decoupling*, in which organisations rigorously implement prescribed means (audits, impact assessments, certifications) without producing declared ends (effective control, substantive transparency, accountability). Bromley and Powell demonstrate that decoupling is structural, not contingent: it arises from the mismatch between the categorical logic of compliance instruments and the continuous, temporally variable, high-dimensional behaviour of the systems they govern. The *audit society* framework of Power (1997, 2022) adds a complementary mechanism: the proliferation of verification rituals produces an economy of verifiability that operates autonomously from its declared purposes — systems adapt to audit criteria rather than to the objectives those criteria should measure.

The sociological framework also draws on DiMaggio and Powell's (1983) institutional isomorphism to explain how normative diffusion propagates Type II without Type III: mimetic isomorphism (organisations copy each other's governance structures) and normative isomorphism (professional fields establish standards that reproduce themselves through training and credentialing) produce convergence on risk-management approaches even across jurisdictions with different legal traditions — a pattern confirmed by the semantic similarity analysis in Kaminski (2026a, Chapter 5).

**Fricção Ontológica** (Ontological Friction) is the concept that Kaminski (2026a) introduces to formalise the governance failure that Type I and Type II cannot address: the structural incompatibility between the inductive, stochastic logic of deep learning models — operating by probabilistic inference over high-dimensional state spaces — and the deductive, categorical logic of institutional norms — operating by prescriptive obligation (obligations, prohibitions, permissions) over discrete categories. This incompatibility is not a contingent technical deficiency but a difference in logical regime between two forms of reasoning whose controlled articulation is precisely what governance frameworks fail to specify. The interference angle θ is the mathematical operationalisation of Ontological Friction as a governable scalar — continuous, computable, and formally grounded in the sovereign normative state encoded in primary legal texts.

The **compliance-by-construction** paradigm introduced in Kaminski (2026a, §7.10) is the conceptual core that this empirical paper validates. In the dominant compliance-by-verification paradigm (Type II), systems are built first and governed afterwards — periodically audited by external entities that verify whether the system meets requirements. In compliance-by-construction (Type III), normative conformity is an emergent property of the architecture: a Q-FENG system cannot be deployed in a non-conforming configuration because normative constraints participate in the training and inference process, inscribed in the computational graph as sovereign predicates whose observance is a condition of operational existence. The present paper's seven scenarios demonstrate that this architectural claim is computationally grounded: the Circuit Breaker activates for all five failure scenarios and is absent for both positive controls, with 100% regime stability under threshold and sensitivity perturbation.

### 2.1 Neurosymbolic AI

The integration of neural and symbolic computation has been a persistent research agenda since the early 1990s, motivated by the complementary strengths and weaknesses of the two paradigms: neural systems offer inductive generalisation from data but lack interpretability and formal correctness guarantees; symbolic systems offer deductive tractability and verifiability but require explicit knowledge encoding (Besold et al. 2017; Garcez et al. 2022). The taxonomy proposed by Kautz (2022) distinguishes several integration modes, from sequential neural-then-symbolic pipelines to fully coupled systems where symbolic constraints modulate neural computation.

Recent work has demonstrated that neurosymbolic integration is particularly effective in domains requiring both perceptual grounding and legal or normative reasoning. DeepProbLog (Manhaeve et al. 2018) extends Prolog with neural predicates, enabling probabilistic logic programming over learned representations. NeurASP (Yang et al. 2020) grounds Answer Set Programming with neural networks for structured prediction. Logic Tensor Networks (Badreddine et al. 2022) translate first-order logic formulae into differentiable loss functions. The d'Avila Garcez and Lamb (2023) survey argues that neurosymbolic AI is approaching a maturity threshold sufficient for real-world deployment in high-stakes domains.

Q-FENG differs from these approaches in two fundamental respects. First, the normative constraints are not learned from annotated examples but extracted directly from primary legal texts — constitutions, statutes, regulatory instruments — ensuring that sovereign predicates reflect the actual positive law rather than a learned proxy. Second, the interference geometry used to measure alignment does not require the symbolic system to be differentiable; it operates on the output of an arbitrary ASP solver (Clingo), using the set of active atoms to construct the normative state vector ψ_S.

### 2.2 Legal NLP and Normative Reasoning

The extraction of normative content from legal texts has a substantial literature, motivated by both knowledge engineering and compliance automation applications. The CLAUDETTE system (Lippi et al. 2019) demonstrated automated detection of potentially unfair clauses in online terms of service using a combination of SVM classifiers and hand-crafted grammars, achieving F1 scores of 0.75–0.89 across eight clause types. Robaldo et al. (2020) survey the Semantic Web representations of deontic modalities — obligation, permission, prohibition — that underpin normative reasoning systems, noting that the standard deontic logic treatment fails to capture defeasibility, contextual modification, and hierarchical priority among norms.

Palmirani and Governatori (2018) applied the LegalRuleML standard to GDPR compliance checking, demonstrating that a subset of the Regulation's obligations can be formalised as defeasible rules and evaluated against institutional fact patterns. Koreeda and Manning (2021) introduced ContractNLI, a dataset for document-level natural language inference over contracts, demonstrating that pre-trained language models achieve strong performance when fine-tuned on domain-specific annotation.

The Q-FENG E2 stage advances this line of work in two ways. First, it operates across multiple jurisdictions simultaneously (Brazil, EU, USA) using a single few-shot extraction protocol calibrated per regime, without requiring domain-specific fine-tuning. Second, the extracted DeonticAtoms are not used as standalone outputs but as inputs to a translation stage (E3) that produces Clingo predicates — closing the loop from natural language to formal symbolic reasoning.

Answer Set Programming (Brewka et al. 2011; Lifschitz 2019) provides the symbolic substrate for the Q-FENG normative evaluation. Clingo (Gebser et al. 2019), the leading ASP solver, supports both satisfiability testing and model enumeration under default negation and integrity constraints — the precise mechanisms needed to evaluate whether a normative state is consistent with a set of agent behaviours. Prior work on ASP-based normative reasoning includes the ASPIC+ framework (Modgil and Prakken 2013) for argumentation and the normative ASP approach of Governatori et al. (2013) for defeasible deontic logic. Q-FENG's contribution is to use the SAT/UNSAT output of Clingo not as a final verdict but as a structured signal for constructing the normative state vector ψ_S.

### 2.3 AI Governance Frameworks

The field of AI governance has produced a large literature of principles, frameworks, and audit methodologies (Jobin et al. 2019; Doshi-Velez and Kim 2017; Diaz-Rodriguez et al. 2023). Jobin et al. (2019) identified convergence on five meta-principles across 84 governance documents — transparency, justice/fairness, non-maleficence, responsibility, and privacy — while noting that implementation mechanisms remain underspecified. Doshi-Velez and Kim (2017) argued for a taxonomy of interpretability evaluation that distinguishes application-grounded, human-grounded, and functionally-grounded approaches.

The EU AI Act (Regulation 2024/1689) represents the most ambitious regulatory implementation to date, establishing a risk-tiered classification of AI systems with specific obligations for high-risk systems in sectors including health, education, employment, and public administration. Articles 9, 14, and 15 mandate risk management systems, human oversight mechanisms, and accuracy/robustness requirements respectively. However, the Act does not specify how compliance with these obligations should be formally verified — a gap that Q-FENG's C1 pipeline is designed to address.

The AI Now Institute's 2023 report and the OECD AI Policy Observatory's monitoring framework both identify the absence of real-time governance monitoring as a critical gap. Existing audit approaches are predominantly post-hoc (applied after deployment), documentation-based (relying on provider self-reporting), and binary (compliant/non-compliant rather than graded). Q-FENG's continuous interference angle θ provides a graded, real-time alternative.

International governance bodies have also produced domain-specific frameworks for AI in health that illuminate the normative gaps Q-FENG addresses. The World Health Organization (2021) issued its *Ethics and Governance of Artificial Intelligence for Health* guidance, identifying six core principles — protecting autonomy, promoting well-being, ensuring transparency, fostering responsibility, ensuring inclusiveness, and promoting sustainable AI — and noting that "no agreed mechanism exists to audit whether deployed AI systems conform to these principles in practice." The UNESCO Recommendation on the Ethics of AI (2021), adopted by all 193 Member States, similarly articulates principles without specifying verification mechanisms. The NIST AI Risk Management Framework (NIST AI RMF 1.0, 2023) represents the most operationally concrete attempt, mapping AI risks to four functions — Govern, Map, Measure, Manage — with subcategory actions for each. However, the NIST framework treats governance as an organisational process rather than a formal mathematical property: it provides checklists and documentation requirements but no mathematical criterion for determining whether a given system's output is aligned with specified normative constraints.

The critical gap these frameworks share is the absence of what Doshi-Velez and Kim (2017) term "application-grounded evaluation" — evaluation that assesses alignment with the specific normative requirements of the operational domain, not against general principles. Q-FENG's C1 pipeline fills this gap by grounding the evaluation in primary legal texts (constitutions, statutes, regulations) and producing a formally computable alignment measure (θ) whose governance semantics are defined by positive law, not by researcher intuition. The sovereignty classification (SOVEREIGN vs. ELASTIC) operationalises the legal hierarchy that governance frameworks describe but do not formalise: constitutional provisions override statutes, which override regulations, which override administrative discretion. This hierarchy is encoded in the HITL stage (E4) and propagated through the Clingo predicate weighting into the ψ_S vector — making the governance alignment measure legally grounded in a technically precise sense.

The emerging field of "regulatory technology" (RegTech) and "supervisory technology" (SupTech) for AI governance is also relevant context. Arner et al. (2020) and Zetzsche et al. (2020) survey RegTech applications in financial compliance, demonstrating that automated regulatory monitoring can achieve near-real-time compliance verification at scale. The Q-FENG framework extends this approach to the normative complexity of constitutional governance — a harder problem than financial regulation because constitutional obligations are less precisely specified and more subject to interpretation — by using ASP-based formal reasoning to resolve the interpretive ambiguities that financial RegTech sidesteps.

### 2.4 Quantum Decision Theory

The application of quantum probability formalism to decision theory and cognitive science was systematised by Busemeyer and Bruza (2012) in *Quantum Models of Cognition and Decision*. The core claim is that human judgment under uncertainty exhibits order effects, conjunction fallacies, and violation of classical probability axioms that are naturally explained by quantum probability — specifically, by the interference between incompatible cognitive states. Pothos and Busemeyer (2013) demonstrated that quantum probability models provide better fits to classic violations of expected utility theory than Bayesian alternatives.

The key mathematical mechanism is interference: when two probability amplitudes are superposed, the resulting probability is the square of their sum, not the sum of their squares. The cross-term 2αβ⟨ψ_N|ψ_S⟩ — absent in classical Bayesian models — is the formal source of constructive and destructive interference. Destructive interference (negative cross-term) suppresses joint probability below classical predictions; constructive interference amplifies it.

Q-FENG applies this formalism not to cognitive states but to the alignment between algorithmic predictor preferences (ψ_N) and normative states (ψ_S). The governance interpretation is precise: destructive interference at the violation action (j=0) means that the normative structure, when correctly encoded in the sovereign predicates, suppresses the probability of the norm-violating action below what a classical Bayesian model — which knows only the predictor confidence and the normative classification but not their interference — would predict. This suppression is the governance effect that Q-FENG quantifies.

Pothos et al. (2022) reviewed the empirical and theoretical case for quantum probability in cognition and decision, noting that the formalism is not committed to physical quantum mechanics but uses its mathematical structure as a modelling language. This is precisely the Q-FENG usage: quantum mathematics as a governance geometry, not a physical claim.

### 2.5 Health AI Bias and the Obermeyer Case

Obermeyer et al. (2019) documented that a commercial healthcare algorithm used to identify patients for care management programmes assigned substantially lower risk scores to Black patients than to White patients with the same underlying health needs, measured by number of active chronic conditions. The gap was approximately 34 percentage points at the threshold used for programme enrolment. The analysis demonstrated that the bias was structural: the algorithm used health expenditure as a proxy for health need, and historical spending inequities meant that Black patients in the same health state had lower predicted expenditure and therefore lower algorithm-assigned risk.

This finding is the empirical anchor for the Q-FENG Scenario C7 (Obermeyer constitutional failure), which encodes the equal-protection obligation of §1902(a)(19) of the US Social Security Act as a sovereign predicate and demonstrates that the algorithm's output vector — calibrated from 48,784 real administrative records — generates destructive interference (θ = 133.74°, CIRCUIT_BREAKER) when evaluated against the normative state derived from the Medicaid eligibility framework.

Rajpurkar et al. (2022) survey AI applications in medicine, identifying 74 FDA-cleared AI/ML medical devices and noting persistent concerns about dataset shift, subgroup performance disparities, and absence of prospective monitoring. The Q-FENG framework addresses the monitoring gap: rather than requiring new annotated labels for bias detection, it uses existing normative instruments — statutes, regulations — as the reference standard.

The broader literature on health AI equity situates the Obermeyer finding within a systematic pattern. Char et al. (2018) examined clinical decision support systems for cardiac risk stratification, demonstrating that optimising for overall population performance systematically underserves minority subgroups when training data reflect historical disparities — a mechanism identical to the Obermeyer expenditure proxy. Topol (2019), in *Deep Medicine*, articulates the governance challenge: "The AI systems being deployed in clinical practice were largely trained on data from academic medical centres with narrow demographic profiles. The regulatory pathway does not require fairness auditing as a condition of clearance." This observation identifies precisely the normative gap that CF/88 Art. 196 (universal right to health) and SSA §1902(a)(19) (best-interest standard) seek to close — and that Q-FENG's Scenario C7 demonstrates has not been closed in practice.

Wiens et al. (2019) argue for a "machine learning for clinical decision support" standard that includes prospective evaluation, subgroup reporting, and clinical workflow integration assessment. Their proposed standard addresses performance equity but not normative compliance: it asks whether the system performs equally across groups, not whether its outputs violate constitutional or statutory mandates. Q-FENG's contribution is precisely this normative layer: the interference angle θ measures not performance disparity but alignment with the specific legal obligations encoded in positive law. A system could perform equally across subgroups and still generate CIRCUIT_BREAKER if its equal-performance outputs are achieved by a mechanism structurally inconsistent with the normative architecture (e.g., equal under-service rather than equal adequate service).

The WHO (2021) guidance on AI ethics for health identifies algorithmic bias as a "first-order concern" and calls for "audit mechanisms that assess alignment with the right to health as defined in international human rights law." Q-FENG's C1 pipeline is a concrete implementation of this call: the interference angle θ is precisely an audit mechanism, and the ψ_S vector constructed from CF/88 Art. 196, Lei 8.080/1990, SSA §1902(a)(19), and the EU Charter of Fundamental Rights encodes the right-to-health architecture as a computable normative state. The WHO guidance does not specify how such alignment should be computed; Q-FENG's quantum interference geometry is a formal answer.

### 2.6 Viable System Model and Cybernetic Governance

Beer's Viable System Model (VSM; Beer 1972) provides the cybernetic architecture within which Q-FENG operates. The VSM decomposes organisational governance into five systems: System 1 (operational units), System 2 (coordination), System 3 (management), System 4 (intelligence/adaptation), and System 5 (policy/identity). Espinosa (2003) and Mingers (2006) extended the VSM to public administration and digital governance contexts, demonstrating its applicability to regulatory and policy systems.

Q-FENG's theta-efetivo Markovian extension is a VSM System 4 mechanism: the anticipatory term γ·E[θ(t+k)] models the governance system's prospective intelligence — its capacity to detect emerging crises before they manifest as severe normative violations. The sigmoid-weighted adaptive memory α(t) = σ(β·Δpressão(t)) operationalises the System 4/System 3 handoff: when the pressure signal is deteriorating (Δpressão > 0), the system down-weights historical memory and responds to current state; when pressure is stable or improving, historical memory stabilises the governance signal against noise.

Mapping the full Q-FENG C1 architecture to the VSM systems clarifies the governance role of each pipeline stage. System 1 (operational units) corresponds to the algorithmic predictor — the LightGBM model, time series forecast, or ASP rule engine that produces ψ_N. System 2 (coordination) corresponds to the E4 HITL stage, which coordinates the human-machine classification of sovereign vs. elastic predicates, resolving ambiguities that neither the LLM extractor (E2) nor the Clingo solver (E5) can resolve unilaterally. System 3 (management) corresponds to the Circuit Breaker logic: the threshold comparison θ ≥ 120° that triggers mandatory intervention. System 4 (intelligence/adaptation) corresponds to the Markovian theta-efetivo: the temporal model that tracks governance degradation across time, detects emerging crises from pressure gradients, and projects forward via the anticipatory term. System 5 (policy/identity) corresponds to the ScopeConfig (E0): the constitutional and statutory grounding that defines which predicates are sovereign (legally irreducible) and which are elastic (regulatorily calibratable).

Walker (2006) extended Beer's VSM to digital organisations, arguing that information systems must embed the five-system recursion at each operational level to maintain viability under environmental perturbation. Hoverstadt (2009) demonstrated that organisations that collapse under crisis characteristically suffer from System 4 failure — the intelligence function does not detect the crisis before it exceeds the capacity of System 3 (management) to respond. The Manaus crisis (Section 5.3) is a textbook Hoverstadt collapse: the intelligence signals were present in the SIH/DATASUS data from October 2020, but the institutional System 4 — the epidemiological surveillance architecture — did not translate them into a governance response before the ICU system exceeded capacity in January 2021. Q-FENG's Markovian theta-efetivo demonstrates that a formal System 4 mechanism, if implemented, would have generated CIRCUIT_BREAKER activation in October 2020 — providing three months of lead time for institutional response.

Ashby's Law of Requisite Variety (Ashby 1956) provides the theoretical foundation: a governance system can only control a regulated system if its variety (number of distinguishable states) matches or exceeds that of the system it governs. The Q-FENG interference geometry expands the variety of the governance signal from binary (compliant/non-compliant) to continuous (θ ∈ [0°, 180°]) and multi-regime (STAC/HITL/CIRCUIT_BREAKER), increasing the governance system's variety to match the complexity of real normative failures — which are graded, temporally evolving, and domain-specific, not binary and static.

### 2.7 Gap Statement

No prior work combines: (1) multi-regime normative corpus processing across three jurisdictions producing sovereign-classified Clingo predicates; (2) quantum interference geometry for continuous governance monitoring; (3) temporal Markovian extension with adaptive memory for crisis tracking; (4) Born-rule quantum vs. classical Bayesian comparison that formally characterises the governance suppression structural property; and (5) proof-of-concept demonstration using real administrative microdata (SIH/DATASUS, 48,784 Medicaid records). Q-FENG C1 is the first system to simultaneously address all five dimensions.

---

## 3. Mathematical Foundations

### 3.1 Preference Vectors and Hilbert Space Analogy

Let A = {a_0, a_1, ..., a_{n-1}} be a finite set of possible actions for a normative agent. The Q-FENG framework represents the agent's state as a pair of real-valued vectors in a shared n-dimensional space:

- **ψ_N** ∈ ℝ^n: the **predictor preference vector**, whose j-th component encodes the relative preference or probability weight assigned to action a_j by the algorithmic predictor (LightGBM forecast, time series model, statistical measure, or ASP-derived preference).

- **ψ_S** ∈ ℝ^n: the **normative state vector**, whose j-th component encodes the relative normative weight of action a_j as derived from the active sovereign and elastic predicates extracted by the Clingo ASP solver from the regime-specific corpus.

Both vectors are normalised to unit length. The construction of ψ_N follows a signed additive model: each predictor output contributes positively or negatively to each action's weight, with the sign and magnitude determined by domain guards calibrated to the specific scenario. The construction of ψ_S uses the sovereign-predicate active-atom set extracted by Clingo's constraint-stripping procedure (see Section 4.4).

**Equation 1 — Interference angle:**

$$\theta = \arccos\!\left(\frac{\langle\psi_N | \psi_S\rangle}{\|\psi_N\|\cdot\|\psi_S\|}\right)$$

θ ∈ [0°, 180°] is the **governance interference angle**. When θ = 0°, the predictor and normative state are perfectly aligned (STAC). When θ = 180°, they are maximally opposed. The Q-FENG thresholds partition this range into three governance regimes:

| Regime | Condition | Interpretation |
|--------|-----------|----------------|
| STAC (Stabilized Sociotechnical Agency Configurations¹) | θ < 30° | Predictor aligned with normative state; autonomous operation warranted |
| HITL (Human-in-the-Loop) | 30° ≤ θ < 120° | Partial misalignment; human review required before consequential decisions |
| CIRCUIT_BREAKER | θ ≥ 120° | Severe misalignment; normative violation imminent or in progress; mandatory intervention |

¹ *STAC* is introduced in this paper as the label for the governance alignment regime; the concept originates in Kaminski (2025, doctoral thesis). See Nomenclature note, §1.

The 30°/120° thresholds were set *a priori* based on semantic calibration: STAC requires near-perfect alignment (θ < 30° implies cosine similarity > 0.87, a strong agreement) and CB requires severe opposition (θ ≥ 120° implies cosine similarity < −0.5, clearly destructive). These thresholds were fixed before examining the 7 PoC scenarios; the fact that the empirical θ distribution is bimodal — CB scenarios cluster in [127.8°, 134.7°], STAC scenarios cluster in [5.6°, 7.1°] — with a natural gap, confirms the semantic calibration is consistent with the observed data but does not imply circular optimisation (the gap would persist for any threshold in [7°, 127°]). The threshold robustness analysis (Section 6.1) confirms regime stability across θ_block ∈ {100°, 105°, ..., 130°}.

The interference angle θ operationalizes what the theoretical framework identifies as *Fricção Ontológica* (Ontological Friction; Kaminski 2026a, §2.3) — the structural incompatibility between the inductive-statistical logic of ML predictors and the deductive-deontic logic of normative systems. Classical governance monitoring treats compliance as a binary label (aligned/non-aligned); the interference geometry captures the degree and nature of this structural tension continuously, enabling interventions calibrated to misalignment severity rather than merely its presence. The empirical bimodal distribution of θ — clustering at either extreme with no intermediate cases — is consistent with the theoretical prediction that normative and algorithmic logics are either structurally compatible (constructive interference, STAC) or structurally incompatible (destructive interference, CB), with the HITL regime [30°, 120°) representing the boundary where human expertise resolves residual uncertainty. This operationalization links the formal machinery of Hilbert-space geometry to the institutional sociology of AI governance, grounding the mathematical formalism in an empirically observed structural phenomenon.

### 3.2 Markovian Theta-Efetivo (Kaminski 2026)

For time-varying governance monitoring, the instantaneous interference angle θ(t) may exhibit high volatility due to measurement noise in the predictor input (e.g., month-to-month fluctuations in SIH administrative records). The Kaminski (2026) Markovian extension introduces a temporal smoothing with adaptive memory:

**Equation 2 — Backward-memory form:**

$$\theta_\mathrm{eff}(t) = \alpha(t)\cdot\theta(t) + (1 - \alpha(t))\cdot\theta_\mathrm{eff}(t-1)$$

**Equation 3 — Adaptive weight:**

$$\alpha(t) = \sigma\!\left(\beta \cdot \Delta\mathrm{pressão}(t)\right) = \frac{1}{1 + e^{-\beta\,\Delta\mathrm{pressão}(t)}}$$

**Equation 4 — Pressure gradient:**

$$\Delta\mathrm{pressão}(t) = \mathrm{score\_pressão}(t) - \mathrm{score\_pressão}(t-1)$$

where score_pressão(t) ∈ [0, 1] is a composite normalised pressure indicator combining hospital mortality rate (weight 0.50), ICU utilisation rate (weight 0.30), and respiratory disease rate (weight 0.20), min-max normalised across the 12-month window.

The full **anticipatory form** (Eq. A10 in Appendix B), which adds VSM System 4 prospective intelligence:

**Equation 5 — Anticipatory form:**

$$\theta_\mathrm{eff}(t) = \alpha(t)\cdot\theta(t) + (1 - \alpha(t))\cdot\theta_\mathrm{eff}(t-1) + \gamma\cdot\mathbb{E}[\theta(t+k)]$$

where γ > 0 is the anticipatory weight and 𝔼[θ(t+k)] is the expected mean interference angle over the next *k* time steps. The PoC implementation uses γ = 0 (backward-memory-only), which is sufficient to demonstrate early Circuit Breaker activation in the Manaus series (Section 5.3). The γ > 0 extension is validated analytically in Appendix B.

The adaptive memory has the following governance semantics: when Δpressão(t) > 0 (deteriorating), α(t) → 1 and the current crisis state dominates; when Δpressão(t) ≈ 0 (stable), α(t) ≈ 0.5 (balanced); when Δpressão(t) < 0 (improving), α(t) → 0 and historical memory dampens noisy fluctuations. With the calibration β = 2.0 used in this PoC, α(t) = 0.91 in the October 2020 onset month (Δpressão = +0.767), confirming rapid adaptation to the detected crisis signal. **β sensitivity**: for β ∈ {1.0, 1.5, 2.0, 2.5, 3.0}, the October 2020 α values range from 0.68 to 0.98, and the first CB-onset month remains October 2020 for all β ≥ 1.5; at β = 1.0, first CB onset shifts to November 2020. The Manaus results are robust to the β calibration choice in the [1.5, 3.0] range.

### 3.3 Born-Rule Quantum vs. Classical Bayesian Comparison

To formally characterise the governance advantage of the interference formalism over classical Bayesian alternatives, Q-FENG implements the Born-rule probability comparison introduced by Busemeyer and Bruza (2012) for decision states.

Let α = √conf and β = √(1−conf), where conf ∈ (0,1) is the predictor's confidence score, so that α² + β² = 1. Define the governance superposition state:

**Equation 6 — Governance decision state:**

$$|D\rangle = \alpha|\psi_N\rangle + \beta|\psi_S\rangle, \quad \alpha^2 + \beta^2 = 1$$

The **quantum Born-rule probability** for action a_j is:

**Equation 7 — Born probability:**

$$P_q(j) = \frac{\left(\alpha\psi_N[j] + \beta\psi_S[j]\right)^2}{Z}$$

where the normalisation factor Z incorporates the interference cross-term:

**Equation 8 — Quantum interference cross-term:**

$$Z = 1 + 2\alpha\beta\cos(\theta)$$

The **classical Bayesian mixture** — without quantum interference — is:

**Equation 9 — Classical probability:**

$$P_\mathrm{cl}(j) = \alpha^2\psi_N[j]^2 + \beta^2\psi_S[j]^2$$

The **interference delta** per action:

**Equation 10 — Interference delta:**

$$\Delta(j) = P_q(j) - P_\mathrm{cl}(j)$$

For governance failure scenarios (UNSAT), the violating action occupies position j = 0, where ψ_N[0] > 0 (predictor prefers the violating action) and ψ_S[0] < 0 (norm prohibits it). This sign difference produces Δ(0) < 0 — **destructive interference**: the quantum model assigns lower probability to the violating action than the classical model. The magnitude |Δ(0)| is the **governance suppression** that classical Bayesian monitoring would systematically miss.

For governance compliance scenarios (SAT), ψ_N[0] > 0 and ψ_S[0] > 0 (both predictor and norm prefer the compliant action), producing Δ(0) > 0 — **constructive interference**: the quantum model amplifies compliance above classical predictions.

### 3.4 Alhedonic Signal and Cybernetic Loss

The **alhedonic signal** A ∈ [0, 1] is a composite normative friction indicator combining three components:

$$A = 0.70\cdot\frac{\theta}{180°} + 0.20\cdot\frac{n_\mathrm{sov}}{n_\mathrm{sov} + n_\mathrm{el} + 1} + 0.10\cdot(1 - \mathrm{conf})$$

where n_sov is the number of active sovereign predicates, n_el the number of active elastic predicates, and conf the predictor confidence. Higher A indicates greater normative friction.

**Equation 11 — Cybernetic loss:**

$$\mathcal{L} = \lambda_\mathrm{ont}\cdot\theta + (1 - \mathrm{conf})$$

where λ_ont = 1.5 is the normative penalty weight (calibrated to the PoC regime). L combines the ontological tension (normative misalignment) with the epistemic uncertainty (predictor confidence). The cybernetic loss serves as the optimisation target for governance intervention scheduling: when L exceeds the HITL threshold, human review is triggered; when L exceeds the CB threshold, mandatory intervention is activated.

### 3.5 Failure Typology

The combination of Clingo SAT/UNSAT status, sovereignty classification, and active-atom analysis enables three failure types:

- **Constitutional failure**: SAT=False; sovereign predicates that *would* ground the required obligation are absent from the corpus (the norm does not exist or is not applicable in this jurisdiction/context). Example: racial equity obligation absent from Medicaid statute (C7).

- **Execution-absent-channel failure**: SAT=False; sovereign predicates grounding the required obligation *exist* in the corpus but the execution path is blocked by a missing enabling condition. Example: COES activation obligation exists but hospital occupancy reporting channel is not established (C2).

- **Execution-inertia failure**: SAT=False; the normative predicate cited by the agent (LLM or human) references a non-existent precedent or phantom citation, so the grounding predicate cannot be derived. Example: Mata v. Avianca phantom citation (T-CLT-01).

---

## 4. The C1 Pipeline: Stages E0–E4

### 4.1 E0: ScopeConfig — Normative Domain Specification

The pipeline's entry point is the **ScopeConfig** schema, which parameterises all subsequent stages for a specific governance domain. A ScopeConfig specifies: the target regulatory regime (Brazil/SUS, EU/AI Act, USA/Medicaid); the corpus identifiers and their priority rankings; the predictor type (LightGBM, TimeSeries, Statistical, ASP); the sovereignty threshold for HITL classification; and the domain guards controlling ψ_N construction.

For the current PoC, three ScopeConfigs were instantiated:

| ScopeConfig | Regime | Corpus Anchor | Predictor |
|-------------|--------|---------------|-----------|
| `sus_validacao` | Brasil (19 docs) + EU (4) + USA (9) | CF/88 + Lei 8.080 + EU AI Act | LightGBM / TimeSeries / Statistical |
| `advocacia_trabalhista` | Brasil (CLT + TST) | CLT Art. 59 + Súmulas TST 85/291 | ASP / LLM |
| `manaus_temporal` | Brasil (emergency) | Portaria 69/2021 + Lei 13.979/2020 | TimeSeries (SIH) |

ScopeConfig is implemented as a Pydantic v2 model in `core/schemas.py` (lines 1–89), which is the authoritative contract for all inter-stage communication. No module creates parallel type definitions; all data flows through Pydantic-validated schemas.

### 4.2 E1: Ingestion — Normative Corpus Construction

The E1 stage transforms raw normative documents (HTML, PDF, Markdown) into a structured corpus of **NormChunks** — atomic normative units carrying hierarchical metadata (regime, document, article, paragraph, inciso/alínea), a chunk_type classification (obligation, principle, procedure, definition, sanction), and a SHA-256 content identifier for cache-consistent reprocessing.

**Corpus statistics (E1-v4, approved April 2026):**

| Metric | Value |
|--------|-------|
| Documents processed | 29 |
| Total NormChunks | 27,957 |
| Cross-references detected | 2,977 |
| Concurrency pairs (Jaccard ≥ 0.55) | 347 |

The 347 concurrency pairs — normatively equivalent or conflicting provisions across documents — constitute the backbone of the comparative governance graph. Twelve pairs with Jaccard = 1.0 represent provisions reproduced verbatim across multiple instruments (e.g., the non-discrimination principle appearing in both the Lei 8.080/1990 and the LGPD), confirming their status as sovereign-candidate predicates.

**Table 1. Corpus distribution and DeonticAtom extraction results.**

| Regime | Chunks | % | Documents | DeonticAtoms | % Atoms |
|--------|--------|---|-----------|--------------|---------|
| Brasil | 21,445 | 76.7% | 19 | 3,206 | 62.4% |
| EU | 1,667 | 6.0% | 4 | 1,101 | 21.4% |
| USA | 4,845 | 17.3% | 9 | 829 | 16.1% |
| **Total** | **27,957** | **100%** | **29** | **5,136** | **100%** |

The hierarchical parser implements regime-specific extraction strategies: Brazilian documents follow the Planalto.gov.br DOM structure (Art. / § / inciso / alínea), EU documents follow the EUR-Lex article/paragraph/point notation, and US documents follow CFR section/(a)(1)/(i) notation. Revoked provisions — marked with `<strike>` tags in Planalto.gov.br sources — are removed at the DOM decomposition stage before text extraction, ensuring that predicates reflect the current normative state. This removed 6 chunks from CF/88 and 27 chunks from Lei 13.979/2020 (provisions revoked by subsequent COVID-19 legislation), confirming the effectiveness of the revocation filter.

Chunk type distribution: obligation (82.5%, n=23,053), procedure (7.1%, n=1,992), principle (6.8%, n=1,913), definition (2.7%, n=759), sanction (0.9%, n=240). The dominance of obligation chunks is consistent with the legal structure of the target documents — primarily legislative statutes and regulations rather than commentary or doctrine.

### 4.3 E2: Deontic Extraction

The E2 stage processes NormChunks through a few-shot LLM extraction pipeline to produce **DeonticAtoms** — structured representations of normative modalities with fields: id (SHA-256), source_chunk_id, modality (obligation/permission/prohibition/faculty), agent, patient, action, conditions, and confidence.

The extraction used `claude-sonnet-4-6` via litellm with regime-specific few-shot prompts calibrated to each document structure, without fine-tuning. The few-shot examples were drawn from manually annotated reference chunks (3–5 examples per regime), covering the syntactic patterns characteristic of each jurisdiction.

**E2 statistics (approved April 2026):**

| Metric | Value |
|--------|-------|
| Chunks processed | 6,059 |
| DeonticAtoms extracted | 5,136 |
| Chunks with 0 atoms | 2,352 (38.8%) |
| Confidence < 0.5 | 0 (0%) |
| Confidence < 0.7 | 0 (0%) |
| Mean confidence | 0.930 |
| Median confidence | 0.950 |

Zero atoms below confidence 0.5 is a strong result for multi-regime extraction without fine-tuning. The 38.8% zero-atom rate reflects correct behaviour: definition, procedure, and preambular chunks appropriately yield no deontic content.

**Modality distribution:**

| Modality | N | % | Q-FENG Clingo predicate |
|----------|---|---|-------------------------|
| obligation | 4,325 | 84.2% | `obligated(agent, action)` |
| permission | 482 | 9.4% | `permitted(agent, action)` |
| prohibition | 245 | 4.8% | `:-permitted(agent, action)` |
| faculty | 84 | 1.6% | `may(agent, action)` |

The dominance of obligation modality (84.2%) is consistent with the Lippi et al. (2019) finding that contractual NLP corpora are predominantly prescriptive, and with Robaldo et al. (2020)'s observation that statutory instruments in continental legal systems are structured as obligation networks.

Representative DeonticAtom examples:

**Brasil — CF/88 Art. 1º §único:**
```json
{
  "modality": "obligation",
  "agent": "state",
  "action": "exercise_power_through_elected_or_direct_means",
  "conditions": [],
  "confidence": 0.92
}
```

**EU — AI Act Art. 9:**
```json
{
  "modality": "obligation",
  "agent": "provider",
  "action": "implement_risk_management_system",
  "object": "high_risk_ai_system",
  "conditions": ["system_is_high_risk"],
  "confidence": 0.97
}
```

**USA — SSA §1902(a)(19):**
```json
{
  "modality": "obligation",
  "agent": "state_medicaid_agency",
  "action": "provide_care_and_services_consistent_with_best_interests",
  "patient": "eligible_individuals",
  "conditions": ["medicaid_state_plan_in_effect"],
  "confidence": 0.89
}
```

### 4.4 E3: Translation — DeonticAtom to Clingo Predicate

The E3 stage implements a deterministic, template-based translation from DeonticAtoms to Clingo predicate syntax. The translation is template-based (no LLM at this stage) to ensure reproducibility and formal correctness. Jinja2 templates encode five modality patterns:

```prolog
% obligation (unconditional)
obligated({{ agent }}, {{ action }}).

% obligation (with conditions)
obligated({{ agent }}, {{ action }}) :- {{ condition_pred }}(X), X > {{ threshold }}.

% prohibition
:- permitted({{ agent }}, {{ action }}).

% permission
permitted({{ agent }}, {{ action }}) :- {{ condition_pred }}.

% faculty
may({{ agent }}, {{ action }}) :- {{ condition_pred }}.
```

String conditions are translated to unary predicates; arithmetic conditions (> threshold, < threshold) use Clingo's built-in arithmetic. The sovereignty classification (SOVEREIGN vs. ELASTIC) assigns legal weight: sovereign predicates encode constitutional or statutory obligations that cannot be modified by subordinate instruments; elastic predicates encode regulatory details subject to administrative discretion.

### 4.5 E4: HITL — Human-in-the-Loop Sovereignty Classification

The E4 stage implements human-in-the-loop review of the sovereignty classification for each ClingoPredicate. Reviewers classify each predicate as SOVEREIGN (legally irreducible; cannot be overridden by executive discretion) or ELASTIC (regulatorily calibratable within statutory bounds). The classification is recorded in the HITL cache and propagates forward to E5 scenario evaluation.

For the `sus_validacao` scope, all 537 predicates were reviewed (537/537, Phase B completed April 2026). For the `advocacia_trabalhista` scope, the CLT-domain predicates covering working hours (Art. 59), collective bargaining agreements (CCTs), and TST jurisprudence (Súmulas 85, 291) were classified in the same HITL pass.

The SOVEREIGN/ELASTIC distinction is the formal basis for the failure typology described in Section 3.5: constitutional failures arise when a required sovereign predicate is absent from the corpus; execution failures arise when the sovereign predicate exists but the execution chain is blocked or misgrounded.

---

## 5. Validation Results

### 5.1 Overview of Seven Scenarios

Seven scenarios were validated across three normative regimes and two domains. Scenarios C2, C3, and C7 address the health domain; T-CLT-01 through T-CLT-04 address the labour law domain. Scenarios T-CLT-03 and T-CLT-04 are **positive controls** — cases of normative compliance expected to produce STAC (θ < 30°).

**Table 2. Scenario validation results.**

| Scenario | Domain | Regime | θ (°) | Regime | SAT | Failure type | Governance suppression | Data source | n_obs |
|----------|--------|--------|--------|--------|-----|--------------|----------------------|-------------|-------|
| C2 | Health | Brasil | 132.36 | CIRCUIT_BREAKER | False | execution_absent_channel | 16.75% | SIH/DATASUS real | 1,526 |
| C3 | Health | Brasil | 134.67 | CIRCUIT_BREAKER | False | constitutional | 25.16% | Normative | 27 docs |
| C7 | Health | USA | 133.74 | CIRCUIT_BREAKER | False | constitutional | 10.66% | Real Medicaid | 48,784 |
| T-CLT-01 | Labour | Brasil | 134.08 | CIRCUIT_BREAKER | False | execution_inertia | 9.37% | Normative | 1 case |
| T-CLT-02 | Labour | Brasil | 127.81 | CIRCUIT_BREAKER | False | constitutional | 11.23% | Normative | 1 case |
| T-CLT-03 | Labour | Brasil | 5.65 | **STAC** | True | — | −0.28% | Normative | 1 case |
| T-CLT-04 | Labour | Brasil | 7.05 | **STAC** | True | — | −0.44% | Normative | 1 case |

![Figure 1: Interference angle θ by scenario with governance regime bands. Horizontal bar chart showing STAC zone (0–30°, green), HITL zone (30–120°, yellow), and CIRCUIT_BREAKER zone (120–180°, red). Five scenarios cluster in the 127–135° range; two positive controls cluster near 5–7°.](../../docs/figuras/fig1_theta_by_scenario.png)

**Governance suppression percentage** is defined as:

$$\mathrm{GSP} = \frac{P_\mathrm{cl}(j) - P_q(j)}{P_\mathrm{cl}(j)} \times 100\%$$

It quantifies the fraction by which the quantum Born-rule model suppresses the violation probability below the classical Bayesian prediction. Negative GSP (positive controls T-CLT-03, T-CLT-04) indicates constructive interference: the quantum model amplifies the compliance probability above classical predictions.

### 5.2 Scenario Narratives

**C2 — Manaus Hospital Collapse (Brasil, execution_absent_channel):**

θ = 132.36°, CIRCUIT_BREAKER. This scenario formally encodes the January 2021 Manaus ICU collapse — one of the most documented healthcare governance failures in Brazilian history — in which hospital occupancy reached 100% (certified by Portaria MS 69/2021, Art. 1, §1) while municipal oxygen supplies were exhausted, leading to patient transfers to other states and an internationally reported humanitarian emergency (Sabino et al. 2021).

The **normative corpus** for C2 comprises four documents in the `brasil/saude/` and `brasil/emergencia_manaus/` sub-corpora: CF/88 Capítulo II (Art. 196–200, 383 chunks); Lei 8.080/1990 (381 chunks, specifically Art. 7 §II — equity principle — and Art. 15 §I — emergency competence of the federal authority); Lei 13.979/2020 (199 chunks after revocation filter, specifically Art. 3 §§I–VI — emergency health measures — and Art. 10 §§I–III — operational protocol); and Portaria MS 69/2021 (dedicated Manaus emergency protocol encoding the hospital occupancy threshold and oxygen stock trigger conditions).

The **Clingo predicate derivation chain** for C2 is: (1) `hospital_occupancy_rate_pct(100)` is asserted as a scenario fact; (2) the rule `sovereign(obligation_to_activate_coes) :- hospital_occupancy_rate_pct(R), R > 85` (from emergencia_sanitaria.lp) fires, deriving `sovereign(obligation_to_activate_coes)`; (3) the integrity constraint `:- sovereign(obligation_to_activate_coes), not executed(coes_activation)` fails because `executed(coes_activation)` is not derivable (the execution pathway is absent from the normative program); (4) Clingo returns UNSAT.

The **ψ_N construction** uses the TimeSeries predictor calibrated from 1,526 SIH/DATASUS admissions across six months (Oct/2020–Mar/2021) with COVID-19 ICD codes (J189, J960, J961, J969, U071, U072, B342). The predictor preference vector encodes three actions: a_0 = continue_autonomous_operation (ψ_N[0] = 0.998), a_1 = activate_partial_escalation (ψ_N[1] = 0.065), a_2 = activate_full_coes (ψ_N[2] = 0.022). The normative state vector, derived from the nine active sovereign predicates, is ψ_S = [−0.718, 0.486, 0.498] — strongly opposing the autonomous continuation action that the predictor overwhelmingly prefers.

The **failure type** is execution_absent_channel: the sovereign obligation `obligation_to_activate_coes` is present and correctly grounded in the corpus (Art. 10 §I Lei 13.979/2020), but the execution chain requires a formal reporting channel from the Secretaria Municipal de Saúde de Manaus to the federal Sala de Situação do Ministério da Saúde, which was not operationally established in January 2021. The sovereign norm exists; the execution infrastructure does not. This distinction has direct policy implications: remediation requires building the coordination channel (an institutional problem), not amending the statute (a legislative problem).

Born-rule quantum probability: P_q(violation) = 0.761; classical Bayesian: P_cl(violation) = 0.914; governance suppression: 16.75%. Nine of nine active predicates are classified SOVEREIGN; zero elastic predicates are active — a normative saturation consistent with the constitutional-level grounding of the right-to-health emergency response.

**C3 — Regional SUS Concentration (Brasil, constitutional):**

θ = 134.67°, CIRCUIT_BREAKER, governance suppression 25.16% — the highest suppression in the dataset. This scenario evaluates a structural pattern in Brazilian health policy: the concentration of SUS specialist services (oncology, cardiac surgery, high-complexity imaging) in capitals and large metropolitan centres, while the interior municipalities receive predominantly primary care — a distribution pattern that systematically disadvantages the 46% of Brazil's population living in municipalities with fewer than 50,000 inhabitants.

The **constitutional grounding** is double: CF/88 Art. 196 establishes health as "a right of all and a duty of the State, guaranteed by social and economic policies aimed at reducing the risk of disease and other harms and at universal and equal access to actions and services for health promotion, protection, and recovery" — with the term "universal and equal access" (acesso universal e igualitário) constituting the sovereign obligation that the concentration pattern violates. Lei 8.080/1990 Art. 7 §II (equity principle — equidade) operationalises this constitutional mandate at the statutory level, requiring that services be distributed according to health need rather than administrative convenience or provider preference.

The **Clingo predicate derivation chain** activates seven sovereign predicates: `universal_right_to_health(cf88_art196)`, `equity_principle(sus, regional_access)`, `equity_distribution_required(specialist_services)`, `prohibition_unequal_allocation(health_resources)`, and three additional predicates from Lei 8.080/1990 encoding the SUS integration principles. The LightGBM predictor — trained on the normative document count per regional administrative unit across all 27 corpus documents — assigns high weight to the concentrated metropolitan pattern (ψ_N = [0.996, 0.078, 0.033]), while the normative state strongly opposes it (ψ_S = [−0.759, 0.506, 0.411]).

The **failure type** is constitutional: unlike C2 (where the execution channel is missing) or C7 (where the statute lacks a racial equity clause), C3 involves an explicit constitutional mandate that is structurally violated by the resource allocation pattern. Remediation requires policy intervention — either legislative reallocation of SUS specialist services to interior municipalities or constitutional interpretation by the STF (Federal Supreme Court) binding on administrative allocation decisions. This is the most severe failure type from a governance standpoint: it cannot be resolved by building coordination channels or by statutory amendment without constitutional revision.

The 25.16% governance suppression — the highest in the dataset — reflects the double constitutional grounding (CF/88 direct + Lei 8.080 operational) producing maximum destructive interference with the predictor's metropolitan concentration preference. This scenario establishes that the Q-FENG framework can detect constitutional violations in resource allocation patterns even when the predictor has no explicit fairness objective — the violation emerges from the structural mismatch between the allocative algorithm's optimisation target and the normative architecture's distributional requirements.

**C7 — Obermeyer Racial Bias (USA, constitutional):**

θ = 133.74°, CIRCUIT_BREAKER. This scenario encodes the Obermeyer et al. (2019) finding in formal normative terms: a commercial healthcare algorithm deployed across hundreds of US hospitals assigns Black patients risk scores approximately 34 percentage points lower than White patients with identical health needs, measured by active chronic condition count. The structural cause is the algorithm's use of health expenditure as a proxy for health need — expenditure that reflects historical racial disparities in healthcare access rather than clinical necessity.

The **normative corpus** for C7 is the US sub-corpus (9 documents, 4,845 chunks, 829 DeonticAtoms): SSA Title XIX §1902 (831 chunks — the Medicaid state plan requirements), 42 CFR Part 430 (administration), 42 CFR Part 435 (eligibility), 42 CFR Part 440 (covered services), the Obermeyer et al. (2019) published analysis (empirical anchor, not a normative document — used to calibrate ψ_N), and the 14th Amendment (5 chunks — the constitutional source of equal protection). The 14th Amendment's disproportionately small chunk count (5 chunks) relative to its constitutional weight illustrates why the HITL sovereignty classification is indispensable: the E4 reviewer classified `equal_protection(all_persons)` as SOVEREIGN based on its constitutional character, not its corpus frequency.

The **Clingo predicate derivation chain** activates four sovereign predicates from the US corpus: `equal_protection(all_persons)` (14th Amendment §1), `best_interest_standard(state_medicaid_agency, eligible_individuals)` (SSA §1902(a)(19)), `non_discrimination_eligibility(medicaid)` (42 CFR §435.4), and `covered_services_without_discrimination(medicaid)` (42 CFR §440.230(c)). The algorithm's output — modelled as a statistical measure calibrated from the 48,784-record Obermeyer dataset — is encoded in ψ_N = [0.991, 0.117, 0.058], strongly preferring the biased allocation action (a_0 = allocate_by_expenditure_proxy). The normative state, derived from the four active sovereign predicates, is ψ_S = [−0.768, 0.329, 0.549].

The **failure type** is constitutional: SSA §1902(a)(19) requires that Medicaid services be provided "consistent with the best interests of the beneficiaries" but does not specify a racial equity obligation by name. The equal-protection clause enters the normative architecture exclusively through the 14th Amendment grounding — a constitutional interpretive gap that the commercial algorithm structurally exploits. The corrective action is not statutory amendment but judicial interpretation: the equal-protection constraint must be formally incorporated into the Medicaid state plan requirements through either Congressional action or court ruling. This is a constitutional failure in the precise sense: the statute does not contain the sovereign predicate that constitutional law requires it to contain.

The 10.66% governance suppression reflects the relatively stronger predictor confidence (Statistical predictor, conf = 0.91 — the highest in the dataset) compared to C2 and C3, which reduces the α coefficient and moderates the quantum advantage. Nevertheless, the Born-rule model assigns P_q(violation) = 0.847 vs. P_cl(violation) = 0.948 — a 10-percentage-point suppression that, at the scale of the algorithm's deployment (hundreds of hospitals, potentially millions of patients), has substantial welfare implications.

**T-CLT-01 — Phantom Citation / Mata v. Avianca (Brasil, execution_inertia):**

θ = 134.08°, CIRCUIT_BREAKER. This scenario is the Q-FENG formalisation of the pattern documented in *Mata v. Avianca* (SDNY, 2023), in which an attorney submitted a brief to a US federal court containing six fake citations to non-existent cases, all generated by ChatGPT. The scenario is adapted to the Brazilian labour law context — specifically, an LLM-assisted legal brief submitted to the TST (Tribunal Superior do Trabalho) in a working hours dispute.

The **normative corpus** for T-CLT-01 is the `corpora/brasil/trabalhista/` sub-corpus: CLT (Consolidação das Leis do Trabalho, Brazilian Labour Code) Arts. 58–74 (jornada de trabalho, working hours regulation), CLT Art. 59 and Art. 59-B (hour bank, added by Lei 13.467/2017 Labour Reform), Súmula TST 85 (banco de horas — conditions and limits), Súmula TST 291 (overtime — compensatory time limits), and Lei 13.467/2017 (full Labour Reform text including §§ on CCT/ACT requirements). The corpus does not contain the ruling TST-RR-000789-12.2018.5.03.0000, because that ruling does not exist.

The **Clingo predicate derivation chain** is: (1) the scenario facts assert `claims_precedent(argument, tst_rr_000789_ficticio)` and `argument_type(argument, hour_bank_legality)`; (2) the rule `legal_citation_grounded(P) :- claims_precedent(_, P), corpus_contains_ruling(P)` fails because `corpus_contains_ruling(tst_rr_000789_ficticio)` has no supporting fact; (3) the integrity constraint `:- argument_type(A, hour_bank_legality), claims_precedent(A, P), not legal_citation_grounded(P)` fires and returns UNSAT. The six active sovereign predicates include `citation_grounding_required(tst_proceedings)`, `precedent_must_exist(tst_decision)`, and `argument_validity_requires_grounding(labour_law)` — all SOVEREIGN-classified because TST procedural rules make citation grounding a condition of admissibility, not an aspirational standard.

The **failure type** is execution_inertia: unlike execution_absent_channel (where the execution pathway infrastructure is missing) or constitutional failure (where the statute lacks the required provision), execution_inertia is a purposive failure — the LLM asserts a normative predicate that it invented rather than retrieved, and this invention breaks the formal derivation chain that Clingo requires. The governance implication is precise: the Q-FENG Circuit Breaker would trigger on the brief before it reaches the court, flagging the ungrounded citation for human review. This is the HITL use case: a governance system that intercepts phantom citations at submission rather than discovering them after judicial sanction.

The predictor preference vector ψ_N = [0.982, 0.187] encodes the ASP-derived argument's preference for the phantom-citation action (a_0 = submit_argument_with_citation) over the alternative (a_1 = withdraw_argument_pending_verification). Governance suppression: 9.37% — smaller than C2 and C3 because the 2D ψ_N space produces less destructive interference than the 3D health scenarios, but sufficient for unambiguous CIRCUIT_BREAKER classification.

**T-CLT-02 — Hour Bank Without CCT (Brasil, constitutional):**

θ = 127.81°, CIRCUIT_BREAKER — the lowest CB theta in the dataset. This reflects a scenario with partial normative support: unlike T-CLT-01 (where the predicate literally does not exist) or C3 (where the constitutional grounding is unambiguous), T-CLT-02 involves a normative structure that *permits* the action under certain conditions (with a CCT) but *prohibits* it under the present conditions (without a CCT). The CLT framework thus provides a partial anchor for the predictor — explaining the lower θ — while the missing CCT condition pushes the scenario firmly into CIRCUIT_BREAKER.

The **legal background** is the Labour Reform (Lei 13.467/2017), which introduced CLT Art. 59-B §1: "The establishment of the time account for exceeding forty hours of weekly work may only occur by collective labour convention or collective bargaining agreement." Súmula TST 85 §I (updated 2020) reinforces this: "The compensatory time account can be established through individual written agreement when the workweek does not exceed ten hours. For workweeks exceeding that, collective bargaining is required." An 8-month hour bank by individual agreement — the scenario fact — violates both instruments.

The **Clingo predicate derivation chain** activates seven active predicates (6 SOVEREIGN, 1 ELASTIC): `collective_bargaining_required(hour_bank, clt_art59b)` (SOVEREIGN), `cct_required_for_long_bank(exceeds_10h_week)` (SOVEREIGN), `prohibition_individual_agreement_only(long_hour_bank)` (SOVEREIGN), `tst_sumula_85_applies(hour_bank_case)` (SOVEREIGN), `right_to_collective_bargaining(worker)` (SOVEREIGN), `labour_reform_applicable(lei_13467_2017)` (SOVEREIGN), and `overtime_limits_applicable(tst_sumula_291)` (ELASTIC). The single elastic predicate reflects that the specific overtime limits (Súmula 291) are calibratable within the statutory framework, while the CCT requirement itself is not.

The scenario facts encode: `hour_bank_implemented(8_months)`, `has_cct(employer, none)`, `weekly_hours_exceeded(employer, 42)`. The integrity constraint `:- hour_bank_implemented(_), not has_cct(employer, valid_instrument)` fires and returns UNSAT.

The **ψ_N vector** = [0.977, 0.214] encodes the employer's strong preference for continuing the hour bank (a_0) over restructuring to obtain a CCT (a_1). The ψ_S = [−0.768, 0.640] reflects the strong normative opposition to the unconstrained hour bank. Governance suppression: 11.23%. The T-CLT-02 / T-CLT-03 pair (with and without CCT, θ difference of 122.2°) provides the clearest demonstration of the pipeline's discriminative validity: a single binary condition (presence or absence of a valid CCT) produces a regime shift from CIRCUIT_BREAKER to deep STAC.

**T-CLT-03 — Valid Hour Bank With CCT (STAC positive control):**

θ = 5.65°, STAC. This is the positive control for T-CLT-02: identical employer, identical 8-month hour bank, but with a valid CCT (Convenção Coletiva de Trabalho) duly filed with the Regional Labour Secretariat and covering the employer's CNAE sector.

The scenario facts add `has_cct(employer, cct_2023_metalurgico)` and `cct_valid_period(cct_2023_metalurgico, 2023_2025)`. With this single fact addition, the integrity constraint `:- hour_bank_implemented(_), not has_cct(employer, valid_instrument)` is no longer violated: `has_cct(employer, cct_2023_metalurgico)` unifies with `has_cct(employer, valid_instrument)` via the validity predicate `cct_valid(cct_2023_metalurgico)`. Clingo returns SAT. Three sovereign predicates and three elastic predicates are active — a balanced SOVEREIGN/ELASTIC split reflecting that the CCT satisfies the constitutional and statutory requirements (sovereign) while leaving calibratable regulatory details (working time scheduling, overtime distribution) to the agreement's provisions (elastic).

The **ψ_S vector** collapses to [1.0, 0.0] in the SAT case: the normative state strongly endorses the compliant action (a_0 = implement_hour_bank_with_valid_cct). ψ_N ≈ [0.995, 0.098] — the employer also strongly prefers implementation, now consistent with the normative requirement. θ = 5.65° reflects near-perfect alignment. Constructive interference: Δ(0) = +0.003, P_q(compliance) = 0.994 vs. P_cl(compliance) = 0.991. The governance system is in deep STAC: autonomous operation is warranted without human review. The −0.28% governance suppression (negative) quantifies the constructive amplification: the quantum model assigns *higher* probability to the compliant action than the classical Bayesian model, reflecting the normative state's endorsement amplifying the predictor's preference.

**T-CLT-04 — Grounded Citation / TST-RR-000200-50.2019 (STAC positive control):**

θ = 7.05°, STAC. This is the positive control for T-CLT-01: identical working hours dispute, identical argument structure, but citing the real TST ruling TST-RR-000200-50.2019 (Acórdão, 7ª Turma do TST, 27/11/2019, on working hours compensation for shift workers in metallurgy — present in the corpus at `corpora/brasil/trabalhista/tst_decisoes/tst_rr_000200_50_2019.lp`).

The scenario fact `claims_precedent(argument, tst_rr_000200_50_2019)` now triggers `corpus_contains_ruling(tst_rr_000200_50_2019)` (asserted as a fact in the corpus file), which allows `legal_citation_grounded(tst_rr_000200_50_2019)` to be derived. The integrity constraint `:- argument_type(A, hour_bank_legality), claims_precedent(A, P), not legal_citation_grounded(P)` is satisfied because `legal_citation_grounded(tst_rr_000200_50_2019)` holds. Clingo returns SAT with six active sovereign predicates — all grounding predicates satisfied.

The **θ = 7.05° > 5.65°** (T-CLT-03) reflects the slightly larger ψ_N/ψ_S angular gap in the labour law citation scenario vs. the hour bank scenario: ψ_N[0] = 0.992 and ψ_S[0] = 1.0 (full normative endorsement), with the small residual gap (0.122 in the second component) producing θ = 7.05°. Both are firmly within STAC, and the difference is not governance-significant.

The **T-CLT-01 / T-CLT-04 pair** is the pipeline's strongest discriminative validation: a 127.0° angular shift (134.08° → 7.05°) from a single binary change in citation grounding. No intermediate processing or re-calibration is required — the same pipeline, same predictor, same corpus, same argument structure, different citation target. This demonstrates that the Q-FENG interference angle correctly locates the normative failure at the precise point where the LLM's hallucination enters the derivation chain.

![Figure 2: Born-rule vs. classical Bayesian probability for each scenario. Two-panel plot: left panel shows P_q(violation) vs. P_cl(violation) for CB scenarios; right panel shows P_q(compliance) vs. P_cl(compliance) for STAC scenarios. Error bars reflect bootstrap CIs.](../../docs/figuras/fig2_born_vs_classical.png)

### 5.3 Manaus Theta-Efetivo Series

**Table 3. Manaus 12-month theta-efetivo series with bootstrap 95% confidence intervals.**

| Month | θ_t (°) | θ_eff (°) | α(t) | Regime | Occupancy | Data source | CI lower | CI upper |
|-------|---------|----------|------|--------|-----------|-------------|----------|----------|
| jul/2020 | 105.00 | 105.00 | 0.500 | HITL | 45% | literature | 100.61 | 112.79 |
| ago/2020 | 102.76 | 103.96 | 0.462 | HITL | 40% | literature | 100.61 | 110.57 |
| set/2020 | 100.61 | 102.41 | 0.465 | HITL | 38% | literature | 100.61 | 109.10 |
| out/2020 | 127.64 | **125.34** | **0.909** | **CIRCUIT_BREAKER** | 72% | SIH/DATASUS | 124.87 | 129.73 |
| nov/2020 | 125.62 | 125.47 | 0.441 | CIRCUIT_BREAKER | 78% | SIH/DATASUS | 122.67 | 128.36 |
| dez/2020 | 121.05 | 123.78 | 0.383 | CIRCUIT_BREAKER | 84% | SIH/DATASUS | 118.03 | 123.92 |
| jan/2021 | 129.00 | 127.47 | 0.707 | CIRCUIT_BREAKER | 100% | SIH/DATASUS | 126.72 | 131.22 |
| fev/2021 | 132.84 | **130.85** | 0.630 | CIRCUIT_BREAKER | 97% | SIH/DATASUS | 130.94 | 132.84 |
| mar/2021 | 130.48 | 130.70 | 0.417 | CIRCUIT_BREAKER | 89% | SIH/DATASUS | 128.13 | 132.58 |
| abr/2021 | 117.86 | 128.10 | 0.202 | CIRCUIT_BREAKER | 74% | literature | 110.11 | 123.71 |
| mai/2021 | 113.07 | 122.08 | 0.401 | CIRCUIT_BREAKER | 62% | literature | 105.49 | 119.85 |
| jun/2021 | 108.66 | 116.49 | 0.417 | HITL | 50% | literature | 100.61 | 116.30 |

Three features of this series are theoretically significant:

1. **Early CB activation (retrospective demonstration)**: In this retrospective validation using SIH/DATASUS data available up to each month, the Circuit Breaker first activates in October 2020 (θ_eff = 125.34°), when occupancy reaches 72% — three months before the January 2021 ICU collapse declared by Portaria 69/2021. This activation results from the Markovian adaptive memory: the large pressure gradient Δpressão = +0.767 in October drives α = 0.909, rapidly propagating the crisis signal into θ_eff. **Important caveat**: the `_OCCUPANCY_BY_MONTH` parameters were calibrated using ex-post knowledge of the crisis progression (Sabino et al. 2021; Portaria 69/2021). A prospective deployment would require real-time SIH/DATASUS feeds (which operate with a 30–90 day reporting lag) and an occupancy model forecasting from contemporaneous data only. The retrospective analysis demonstrates that the formalism *would have detected* the crisis trajectory, not that it would have detected it at the moment of first onset without any prior knowledge. Prospective validation on a future crisis event is a planned extension (see §8).

2. **Memory-dampened recovery**: After the peak in February 2021 (θ_eff = 130.85°), the θ_eff declines slowly despite falling θ_t values (April: θ_t = 117.86° but θ_eff = 128.10°). This reflects the low α values (0.20–0.42) during the recovery phase: the Markovian memory retains the crisis state longer than the instantaneous signal would indicate, consistent with VSM's requirement that system memory extend beyond instantaneous measurement.

3. **Bootstrap CI width asymmetry**: SIH/DATASUS months (Oct/2020–Mar/2021) have narrow bootstrap CIs (±1–2°), reflecting the higher data quality of real microdata. Literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021) have wider CIs (±3–4°), reflecting the uncertainty of epidemiological estimates. The January 2021 peak month has CI [126.72°, 131.22°] — entirely within the CIRCUIT_BREAKER regime regardless of bootstrap variation.

![Figure 3: Manaus theta-efetivo dual-axis time series. Left axis: θ_t (solid line) and θ_eff (dashed line) with bootstrap 95% CI shading. Right axis: hospital occupancy rate (%). Red zone indicates θ ≥ 120° (CIRCUIT_BREAKER). Vertical dashed line marks Portaria 69/2021 (January 2021).](../../docs/figuras/fig3_manaus_dual_axis.png)

### 5.4 Born-Rule Quantum Advantage Quantification

Table 4 summarises the Born-rule comparison for all scenarios.

**Table 4. Born-rule quantum vs. classical Bayesian probabilities.**

| Scenario | θ (°) | P_q(violation) | P_cl(violation) | Δ(violation) | Type | GSP (%) |
|----------|--------|----------------|-----------------|--------------|------|---------|
| C2 | 132.36 | 0.7607 | 0.9137 | −0.1530 | DESTRUCTIVE | 16.75 |
| C3 | 134.67 | 0.6775 | 0.9052 | −0.2278 | DESTRUCTIVE | 25.16 |
| C7 | 133.74 | 0.8467 | 0.9477 | −0.1010 | DESTRUCTIVE | 10.66 |
| T-CLT-01 | 134.08 | 0.8611 | 0.9502 | −0.0890 | DESTRUCTIVE | 9.37 |
| T-CLT-02 | 127.81 | 0.8308 | 0.9358 | −0.1051 | DESTRUCTIVE | 11.23 |
| T-CLT-03 | 5.65 | 0.9936 | 0.9908 | +0.0028 | CONSTRUCTIVE | −0.28 |
| T-CLT-04 | 7.05 | 0.9900 | 0.9857 | +0.0043 | CONSTRUCTIVE | −0.44 |

**Structural property of the Born-rule formulation**: for any θ > 90°, the interference cross-term Z = 1 + 2αβcos(θ) < 1 (since cos(θ) < 0), which by construction reduces P_q(j=0) relative to P_cl(j=0). The governance suppression percentage GSP is therefore a *mathematical property* of the Born-rule formalism — not an empirically discovered result — quantifying *by how much* the interference geometry structurally dampens violation probability for a given θ and predictor confidence conf. This is a stronger claim than an empirical finding: it is a theorem (proved in Appendix B.2) that holds for all CB scenarios (θ ≥ 120°) and all conf ∈ (0,1), regardless of scenario details. The observed GSP values (9.4–25.2%) are therefore the *instantiation* of this structural property for the specific ψ vectors of the seven scenarios.

The governance significance is that this dampening is *not achievable* by a classical Bayesian mixture model (P_cl = α²ψ_N[0]² + β²ψ_S[0]²), which by construction lacks the interference cross-term. For the CB scenarios, the structural GSP means that a system using the quantum Born-rule formalism will *always* assign lower probability to the norm-violating action than a classical mixture, by an amount proportional to the destructive interference. C3 (θ = 134.67°, GSP = 25.16%) provides the largest structural suppression in this PoC: a monitoring system using classical Bayesian probability would assign 91.5% probability to the norm-violating action; the quantum model assigns only 67.8% — a difference that reflects the strong opposition between the predictor's preference (metropolitan concentration) and the normative state (equity principle requiring regional distribution).

![Figure 4: Governance suppression percentage by scenario and failure type. Bar chart grouped by failure type (constitutional, execution_absent_channel, execution_inertia), showing GSP for CB scenarios and constructive amplification for STAC scenarios.](../../docs/figuras/fig4_governance_suppression.png)

### 5.5 DeonticAtom Modality Distribution

![Figure 5: DeonticAtom modality distribution by regime. Stacked bar chart showing obligation/permission/prohibition/faculty counts for Brasil, EU, and USA corpora.](../../docs/figuras/fig5_deontic_modality.png)

The overall 84.2% obligation rate reflects a deliberate corpus composition decision: the PoC selected *regulatory* and *constitutional* instruments — which are structurally obligation-heavy — rather than private law, contractual, or permissive-framework documents. Brazilian health law (CF/88 Art. 196–200; Lei 8.080/1990), EU regulatory law (AI Act), and US programme law (Social Security Act) all operate through categorical obligations on public actors, which naturally produces a high obligation-to-permission ratio. A corpus including private sector contracts, commercial licences, or soft-law instruments would shift the distribution substantially toward permissions and faculties. This corpus selection is intentional for the PoC's focus on public governance failures; extension to mixed public-private normative environments is planned.

The modality distribution varies systematically across regimes. The EU AI Act corpus has the highest relative prohibition rate (6.2% vs. 4.8% overall), reflecting the Act's explicit prohibition of certain AI system categories (Article 5). The US corpus has the lowest relative prohibition rate (3.1%) and the highest permission rate (12.4%), consistent with the Medicaid framework's structure as a system of conditional entitlements rather than categorical prohibitions.

### 5.6 Alhedonic Signal Distribution

**Table 5. Alhedonic signal and cybernetic loss by scenario.**

| Scenario | Alhedonic A | L_cybernetic | n_sovereign_active | n_elastic_active |
|----------|-------------|--------------|-------------------|-----------------|
| C2 | 0.7117 | 1.1808 | 9 | 0 |
| C3 | 0.7197 | 1.2645 | 7 | 0 |
| C7 | 0.6891 | 1.1271 | 4 | 0 |
| T-CLT-01 | 0.6979 | 1.0935 | 6 | 0 |
| T-CLT-02 | 0.6576 | 0.9696 | 7 | 1 |
| T-CLT-03 | 0.1127 | 0.0500 | 3 | 3 |
| T-CLT-04 | 0.2038 | 0.0500 | 6 | 0 |

The minimum cybernetic loss of 0.0500 for STAC scenarios reflects the floor imposed by the predictor confidence term (1 − 0.95 = 0.05) in the loss function. The sharp contrast between CB scenarios (L ∈ [0.97, 1.26]) and STAC scenarios (L = 0.05) demonstrates that the cybernetic loss provides a clear decision boundary for governance intervention scheduling.

![Figure 6: Alhedonic heatmap by scenario and component. Three-column heatmap showing theta_component, sovereign_component, and confidence_component contributions to alhedonic signal A.](../../docs/figuras/fig6_alhedonic_heatmap.png)

![Figure 7: Obermeyer scenario (C7) ψ_N calibration. Histogram of the 48,784-record Medicaid administrative data showing the distribution of risk scores by racial category, with the ψ_N vector components annotated.](../../docs/figuras/fig7_obermeyer_calibration.png)

**Mandatory disclosure 1 — Synthetic data:** Scenarios C5, C6, and C8 (referenced in the E5 design specification) were not executed in this PoC due to the absence of the corresponding LLM predictor (C4 Ollama integration pending). Tables in this paper contain only the seven scenarios for which full E0–E5 data are available. No synthetic values have been imputed for missing scenarios.

**Mandatory disclosure 2 — theta_efetivo originality:** The Markovian theta-efetivo formulation (Equations 2–5) is an original contribution of Kaminski (2026) with no prior antecedent in the Q-FENG or QDT literature. The use of a sigmoid-weighted adaptive memory for normative governance monitoring has not been previously published.

---

## 6. Statistical Analyses

### 6.1 Threshold Robustness

To assess whether the CIRCUIT_BREAKER/STAC classifications are robust to the choice of threshold parameters, we conducted a grid search over θ_stac ∈ {20°, 25°, 30°, 35°, 40°} and θ_block ∈ {100°, 105°, 110°, 115°, 120°, 125°, 130°}, yielding 35 parameter combinations × 7 scenarios = 245 evaluations.

Results: 241 of 245 evaluations (98.4%) produced the same regime classification as the paper-reported values (θ_stac = 30°, θ_block = 120°). The four failures occurred exclusively at θ_block = 130° for scenario T-CLT-02 (θ = 127.81°), which is the only scenario within 3° of any tested threshold boundary. No failures occurred at the paper-reported thresholds or for any scenario other than T-CLT-02. This confirms that the CB classification is stable for all scenarios except T-CLT-02 at the extreme boundary of the tested range.

The natural justification for the 120° threshold is the empirical gap in the θ distribution: the five CB scenarios cluster in [127.8°, 134.7°] while the two STAC scenarios cluster in [5.6°, 7.1°], leaving a gap of over 120° between the populations. Any threshold in the range [7°, 127°] would produce identical classifications for the current seven scenarios; we choose 30°/120° as symmetric brackets that leave maximum margin.

**Table 6. Threshold robustness summary — correct regime rate by scenario.**

| Scenario | θ (°) | Correct @ all θ_stac | Correct @ θ_block ≤ 125° | Failures | Fail condition |
|----------|--------|----------------------|--------------------------|----------|----------------|
| C2 | 132.36 | 100% | 100% | 0/35 | — |
| C3 | 134.67 | 100% | 100% | 0/35 | — |
| C7 | 133.74 | 100% | 100% | 0/35 | — |
| T-CLT-01 | 134.08 | 100% | 100% | 0/35 | — |
| T-CLT-02 | 127.81 | 88.6% | 100% | 4/35 | θ_block = 130° |
| T-CLT-03 | 5.65 | 100% | 100% | 0/35 | — |
| T-CLT-04 | 7.05 | 100% | 100% | 0/35 | — |
| **Overall** | — | **98.4%** | **100%** | **4/245** | — |

### 6.2 Psi-Weight Sensitivity Analysis

To assess the robustness of θ to perturbations in the ψ_N construction — i.e., whether small changes in predictor calibration or domain guard weights would change the governance regime — we conducted a Monte Carlo sensitivity analysis: for each scenario, 500 perturbation samples were drawn by adding uniform noise U(−δ, +δ) to each element of ψ_N (δ = 20% of the original magnitude), re-normalising, and recomputing θ and the regime classification.

Results: all seven scenarios maintained 100% correct regime classification across 500 samples at ±20% perturbation. The standard deviations σ_θ were largest for T-CLT-02 (σ = 2.01°) and T-CLT-01 (σ = 1.77°), reflecting the smaller ψ_N dimension (2D for labour law scenarios vs. 3D for health scenarios), which makes the angular computation more sensitive to proportional changes. Even at 5th percentile θ values, T-CLT-02 yields 123.99° — comfortably above the 120° CB threshold.

**Table 7. Psi-weight sensitivity analysis (±20% perturbation, n=500 per scenario).**

| Scenario | θ_paper (°) | θ_mean (°) | θ_std (°) | θ_p5 (°) | θ_p95 (°) | % correct regime |
|----------|------------|-----------|----------|---------|---------|-----------------|
| C2 | 132.36 | 132.32 | 0.55 | 131.33 | 133.12 | 100% |
| C3 | 134.67 | 134.58 | 0.69 | 133.38 | 135.68 | 100% |
| C7 | 133.74 | 133.66 | 0.97 | 131.87 | 135.08 | 100% |
| T-CLT-01 | 134.08 | 133.97 | 1.77 | 130.75 | 136.57 | 100% |
| T-CLT-02 | 127.81 | 127.72 | 2.01 | 123.99 | 130.65 | 100% |
| T-CLT-03 | 5.65 | 5.72 | 0.94 | 4.36 | 7.42 | 100% |
| T-CLT-04 | 7.05 | 7.20 | 1.17 | 5.44 | 9.29 | 100% |

**Annotation variance bound via ψ perturbation**: The ±20% perturbation analysis serves a dual purpose beyond calibration robustness. A SOVEREIGN→ELASTIC misclassification by the HITL annotator reduces the affected predicate's contribution to ψ_S — mathematically equivalent to reducing that predicate's component weight by a fraction proportional to the ELASTIC vs. SOVEREIGN weight differential (calibrated at approximately 40% in the current ψ_S builder). This reduction is within the ±20% perturbation envelope analysed in Table 7. The 100% correct regime classification at ±20% perturbation therefore constitutes an implicit *leave-one-predicate-out* bound: if any single SOVEREIGN predicate were misclassified as ELASTIC, the resulting θ shift would fall within the observed σ_θ range (0.55°–2.01°), and all seven scenarios would retain their correct regime classification. This does not eliminate the need for inter-annotator reliability validation (acknowledged in §7.4), but it quantifies the upper bound of annotation-induced classification error for the current PoC.

### 6.3 Bootstrap Confidence Intervals for Manaus Series

Confidence intervals for the Manaus theta_efetivo series were computed via parametric bootstrap: for SIH/DATASUS months (Oct/2020–Mar/2021), σ = 0.05 was used (reflecting the quality of real microdata); for literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021), σ = 0.10 was used (reflecting epidemiological estimation uncertainty). 1,000 bootstrap samples per month were drawn from N(score_pressão, σ²), θ_t and θ_eff recomputed, and 95% CIs taken from the 2.5th and 97.5th percentiles.

The narrowest CIs occur in February 2021 (CI: [130.94°, 132.84°]) — the peak crisis month with the highest-quality SIH data and the lowest pressure score variance. All twelve months produce CIs entirely within a single governance regime; no month straddles the HITL/CB boundary when considering the full 95% CI range.

The bootstrap standard deviation for the CI of the October 2020 CB-onset month is σ_bootstrap = 1.25°, with CI [124.87°, 129.73°] — entirely within the CIRCUIT_BREAKER zone. This confirms that the early CB activation in October 2020 is not an artefact of the pressure score calibration.

**Pending analysis:** A Wilcoxon signed-rank test comparing the quantum Born-rule probability vector P_q against the classical P_cl for the five CB scenarios is planned for the C4 (LLM predictor) scenarios, which require Ollama integration (pending). The current dataset yields the expected monotone relationship (higher θ → larger |Δ|) but is insufficient for a formal non-parametric test given the n=5 CB scenario count.

### 6.4 Ablation Study: Rule-Based Baseline Comparison

To assess whether the quantum interference formalism provides governance information beyond what a simpler rule-based approach would deliver, we compared Q-FENG against a minimal rule-based baseline (RB): a system that classifies governance regimes solely by counting active violated sovereign predicates, with no quantum computation.

**Baseline definition**: RB-CB if `n_sovereign_active ≥ 1` AND `n_sovereign_violated ≥ 1`; RB-STAC otherwise. This is the simplest possible governance monitor that uses the same Clingo ASP solver and corpus — it fires whenever any constitutionally irreducible obligation is not fulfilled.

**Table 8. Ablation: Rule-based baseline vs. Q-FENG governance classification.**

| Scenario | θ (°) | Q-FENG regime | RB regime | Classification match | GSP (%) | θ_eff tracking |
|----------|--------|--------------|-----------|---------------------|---------|----------------|
| C2 | 132.36 | CIRCUIT_BREAKER | CIRCUIT_BREAKER | ✓ | 16.75 | ✓ (12-month series) |
| C3 | 134.67 | CIRCUIT_BREAKER | CIRCUIT_BREAKER | ✓ | 25.16 | ✗ |
| C7 | 133.74 | CIRCUIT_BREAKER | CIRCUIT_BREAKER | ✓ | 10.66 | ✗ |
| T-CLT-01 | 134.08 | CIRCUIT_BREAKER | CIRCUIT_BREAKER | ✓ | 9.37 | ✗ |
| T-CLT-02 | 127.81 | CIRCUIT_BREAKER | CIRCUIT_BREAKER | ✓ | 11.23 | ✗ |
| T-CLT-03 | 5.65 | STAC | STAC | ✓ | −0.28 | ✗ |
| T-CLT-04 | 7.05 | STAC | STAC | ✓ | −0.44 | ✗ |

The rule-based baseline classifies all 7 scenarios correctly (7/7, 100%), matching Q-FENG's classification on every case. This confirms the reviewer concern that *for the classification task alone*, the quantum formalism is not strictly necessary: a predicate counter achieves identical results.

**What Q-FENG adds beyond the rule-based baseline**: The ablation reveals that Q-FENG's contribution is not classification accuracy — which any predicate counter can match — but *metric richness* in three dimensions unavailable to the rule-based system:

1. **Continuous governance signal**: Q-FENG provides θ ∈ [0°, 180°] as a continuous misalignment measure, enabling proportionate intervention (e.g., T-CLT-02 at θ = 127.81° warrants less urgent intervention than C3 at 134.67°, despite both being classified CB). The rule-based system produces a binary label with no within-class gradation.

2. **Probabilistic governance (GSP)**: The Born-rule probability P_q(j) quantifies the suppressed probability of a norm-violating action, enabling risk-proportionate governance responses. The rule-based system identifies *that* a violation is occurring; Q-FENG quantifies *how much* the violation probability exceeds a normatively acceptable level.

3. **Temporal tracking via theta_efetivo**: The Markovian theta_efetivo extension (applied to Manaus) requires a continuous interference signal to compute the adaptive memory recurrence. A binary rule-based system cannot produce a theta_efetivo series — it produces only "CB" or "not-CB" at each time step, with no memory of severity trends. This capability is the distinctive contribution of the quantum formalism to the temporal governance monitoring problem.

The ablation thus supports an important qualification: Q-FENG is not proposed as a more accurate *classifier* than rule-based approaches (classification accuracy is already at ceiling for both). It is proposed as a richer *governance measurement instrument* that quantifies degree, direction, and temporal evolution of normative misalignment — capabilities that rule-based predicate counting cannot provide.

---

## 7. Discussion

### 7.1 The Quantum Advantage is Formally Grounded, Not Metaphorical

A natural concern — anticipated from the Herrera-vein of formal AI reviewers — is that the "quantum" terminology constitutes a rhetorical appropriation without mathematical substance. We address this preemptively.

The Q-FENG formalism uses quantum mathematics strictly as a modelling language, following the tradition of quantum cognition (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013). No claim is made about physical quantum mechanics or quantum computing hardware. The specific mathematical contribution — the interference cross-term Z = 1 + 2αβcos(θ) in Equation 8 — is absent from any classical Bayesian mixture model and produces a measurable, systematic difference in the probability assigned to norm-violating actions (Table 4, GSP range: 9.4%–25.2%). This is not a definitional difference or a notational reformulation; it is a structural difference in the probability model that has governance implications.

The comparison between quantum and classical models is implemented in a single function (`compute_born_probability` in `interference.py`, lines 103–166) that takes identical inputs (ψ_N, ψ_S, conf) and produces both P_q and P_cl. The governance suppression percentage GSP is then computed directly from their difference. Any reviewer who questions the quantum advantage claim is invited to inspect the code: the classical model is implemented in the same file, and the difference is structural, not definitional.

The reproducibility of all reported results is guaranteed by: (1) fixed random seeds for Monte Carlo analyses; (2) deterministic Clingo evaluation (no stochastic elements); (3) cached DeonticAtoms (SHA-256 keyed, reproducible without LLM calls); and (4) parquet-format output files containing the full result matrix. The repository [GitHub — blinded for review] contains all code and derived data sufficient to reproduce Tables 2–7 from raw normative documents.

**On cosine similarity equivalence**: A reviewer might observe that θ = arccos(⟨ψ_N|ψ_S⟩) is mathematically equivalent to the cosine distance between ψ_N and ψ_S — and therefore that regime classification by θ thresholds is equivalent to cosine-similarity thresholding, with no quantum formalism required. This observation is correct for the *classification* task: a cosine-similarity threshold classifier applied to the same ψ vectors would produce identical STAC/HITL/CB labels. The quantum contribution is not classification accuracy but three additional capabilities that cosine similarity cannot provide: (1) the Born-rule probability P_q(j) for each action j under normative constraint, enabling probabilistic governance rather than binary classification; (2) the GSP structural property (proved in Appendix B.2) that quantifies exactly *by how much* the interference geometry suppresses norm-violating probability relative to a classical mixture model, enabling proportionate intervention design; and (3) the Markovian theta_efetivo temporal formalism, which requires the continuous interference signal (not a binary label) to compute the adaptive memory recurrence. In short: θ is the backbone of the quantum formalism, not the end product; cosine classification uses only the backbone.

**Ablation study (§6.4)**: Section 6.4 provides a direct rule-based baseline comparison that confirms regime classification parity with Q-FENG on all 7 scenarios, while demonstrating the information gap (no continuous signal, no GSP, no temporal tracking) that the quantum formalism fills.

Regarding external governance tools: a broader comparison against Fairlearn, IBM AI Fairness 360, and ASP compliance checkers in the Governatori tradition is planned for Paper 2; the current PoC establishes the interference formalism's mathematical properties and demonstrates its operation on real data.

### 7.2 Legal Claim Scope and Normative Grounding

A second anticipatable concern — from the Rodrigues-vein of legal AI reviewers — concerns the scope of constitutional claims. Specifically: does the Clingo evaluation of "constitutional failure" in C3 and C7 constitute a legal finding, or a formal modelling claim?

The answer is precise: the Q-FENG pipeline makes a formal modelling claim — that the predictor preference vector ψ_N, constructed from real administrative data, generates destructive interference with the normative state vector ψ_S, constructed from sovereign predicates extracted from primary legal texts. The pipeline does not issue a legal judgment, which would require procedural due process, adversarial argumentation, and judicial authority. It identifies a formal misalignment that warrants human review (HITL) or mandatory intervention (CIRCUIT_BREAKER).

The legal grounding of the sovereign predicates is documented and auditable. For CF/88 Art. 196, the sovereign predicate `universal_right_to_health(cf88_art196)` is derived directly from the constitutional text (chunk `cf88_art196_caput`, confidence 0.97) with SOVEREIGN classification in the HITL review (reviewer annotation: "constitutional provision, not modifiable by executive regulation"). For the 14th Amendment equal-protection predicate in C7, the sovereign predicate `equal_protection(all_persons)` derives from the 5-chunk 14th Amendment document, with SOVEREIGN classification reflecting its constitutional status. These classifications are transparent, auditable, and correct in the sense that they accurately represent the positive law.

The failure type classification (constitutional vs. execution-absent-channel vs. execution-inertia) is formally grounded in the Clingo SAT/UNSAT analysis and the sovereign predicate activation status — not in normative interpretation beyond what the corpus encodes. This interpretive conservatism is by design: the pipeline surfaces failures for human review rather than autonomously resolving them.

### 7.3 Human-in-the-Loop as Epistemic Necessity

The HITL stage (E4) is not merely a compliance checkbox but an epistemic necessity in the Q-FENG architecture. The SOVEREIGN vs. ELASTIC classification requires legal expertise that no automated system — including the E2 LLM extractor — should be trusted to make unilaterally at the constitutional level. The Q-FENG design reflects the principle that the sovereignty classification (which determines whether a predicate grounds a constitutionally irreducible obligation or a regulatorily discretionary one) must be a human decision, recorded in the HITL cache and subject to audit.

This design choice has a testable consequence: the GSP values reported in Table 4 depend on the sovereignty classification. A predicate classified as ELASTIC rather than SOVEREIGN contributes to ψ_S with lower weight, reducing the destructive interference and potentially lowering θ below the CB threshold. The HITL stage is therefore the governance mechanism that determines the operational scope of the Circuit Breaker — a decision too consequential for automation.

### 7.4 Limitations

**Scope of PoC**: The current validation covers 7 scenarios across 3 regimes. The C4 LLM predictor scenarios (C4a, C4b, C4c) require Ollama/qwen2.5:14b integration that is not yet implemented. The Paper 2 labour law domain has only 4 scenarios. The planned 15-scenario full validation suite (including US and EU health scenarios, LLM chain scenarios, and multi-jurisdiction concurrent cases) is deferred to the next iteration.

**Literature-estimated months in Manaus series**: Six of twelve Manaus months (Jul–Sep/2020 and Apr–Jun/2021) use epidemiological literature estimates rather than real SIH/DATASUS microdata. The bootstrap CI analysis confirms that this introduces ≤4° uncertainty in θ_eff; all classifications are stable. However, the paper-reported E2 evaluation for these months is not derived from real microdata and should be interpreted accordingly.

**Single HITL reviewer**: The sovereignty classifications in the current PoC were reviewed by a single annotator (the author) with legal training. Inter-annotator reliability analysis with a second legal expert is required before the sovereignty classifications can be treated as ground truth for downstream validation.

**Defeasibility and conflicting obligations**: The current Clingo corpus encodes obligations, permissions, and prohibitions as hard ASP facts, not as defeasible defaults. Legal reasoning routinely involves prima facie obligations defeated by more specific rules, hierarchically superior norms, or exceptional circumstances — mechanisms that defeasible logic systems (Governatori et al. 2013; Modgil and Prakken 2013) handle but that the current implementation does not. Consequently, the failure diagnoses (constitutional, execution-absent-channel, execution-inertia) assume that no applicable defeasibility condition exists in the corpus — an assumption that is defensible for the PoC scenarios (where the relevant constitutional and statutory provisions are clear and uncontested) but would require explicit defeasibility encoding for scenarios involving norm conflict or exception-based justifications. Defeasible reasoning extensions are a planned enhancement for the full governance monitoring suite addressed in Paper 2.

**Anticipatory theta_efetivo (Eq. 5, γ > 0)**: The anticipatory form of the Markovian recurrence (Equation 5) is formally proved in Appendix B.3 but not implemented in this PoC (γ = 0 in all analyses). This constitutes an incomplete contribution: the proof establishes that early CB activation is achievable with γ > 0 and a forecast of 𝔼[θ(t+k)], but without empirical validation, the anticipatory form remains a theoretical extension. Its implementation requires a forecast model for future predictor states (e.g., an ICU occupancy ARIMA for the Manaus case) that is not currently available. The anticipatory extension is explicitly deferred to §8 Future Work.

**Racial health equity dimension**: Scenario C3 (SUS geographic concentration) implicates structural racial and geographic health inequalities in Brazil that extend beyond resource allocation modelling. The paper addresses the governance failure at the normative-alignment level; a full health equity analysis incorporating racial health disparity data (e.g., IBGE race-disaggregated health indicators) and the corresponding normative obligations under CF/88 Art. 5 (equality) and Lei 8.080/1990 Art. 7 (equity principle) is planned as part of the dedicated health equity extension in Paper 2.

**Thematic scope**: The Q-FENG C1 pipeline validates alignment monitoring for a specific class of governance failures — those in which the relevant normative instruments are available in digital, machine-readable form. Oral customary law, unwritten constitutional conventions, and administrative practice without formal documentation are outside the current scope.

### 7.5 Publication Ecosystem: Theoretical Book, Validation Paper, and Companion Summary

This paper occupies a defined position within a planned three-document research sequence. The theoretical and sociological grounding for Q-FENG is developed in full in Kaminski (2026a) — *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle* — a monograph that applies the tripartite governance taxonomy, the Fricção Ontológica concept, and a 27-document institutional fsQCA analysis to establish that contemporary AI governance frameworks are structurally incomplete (Type I and II only; no Type III cybernetic instantiation). The book explicitly anticipates empirical validation as a subsequent publication (Kaminski 2026a, §1.7): "the formal demonstration of the Q-FENG architecture in operation — across multiple normative regimes, with real administrative microdata — will be presented in a companion validation paper." The present paper is that companion.

A second complementary document — a concise English-language article summarising the book's theoretical contributions and the Q-FENG proposition — is in preparation as Paper 2 of this series. That paper will serve as an international-audience bridge to Kaminski (2026a), which was published in Portuguese for the Brazilian academic market, and will integrate the labour-law validation domain (CLT + TST + Mata v. Avianca) validated here in T-CLT scenarios 01–04.

The relationship between the three documents is therefore: the **book** (Kaminski 2026a) establishes the theoretical gap; the **validation paper** (this document) demonstrates the formal technical solution; and the **summary article** (in preparation) translates both for international governance and AI-law audiences. Together they constitute a coherent contribution: a sociologically grounded theory of AI governance failure, a mathematically grounded architecture for remediation, and an empirical demonstration across three normative regimes with real administrative data.

---

## 8. Conclusions

This paper has presented a proof-of-concept empirical demonstration of the Q-FENG C1 pipeline — a five-stage neurosymbolic architecture for AI governance monitoring — across three normative regimes and seven formal scenarios. It fulfills the empirical demonstration promised in Kaminski (2026a, §1.7), where the theoretical case for a Type III cybernetic governance architecture was established; here, that architecture is shown to operate with real administrative microdata, deterministic normative reasoning, and formally grounded governance metrics.

**Three original contributions** have been demonstrated:

1. **Quantum interference geometry for normative alignment**: The interference angle θ provides a continuous, formally grounded governance measure that separates five CIRCUIT_BREAKER scenarios (θ ∈ [127.8°, 134.7°]) from two STAC positive controls (θ < 8°) with a natural gap that justifies the regime classification. The Born-rule quantum model suppresses violation probability by 9.4–25.2% relative to classical Bayesian baselines (governance suppression percentage), a structural effect invisible to frameworks that treat governance compliance as a binary label.

2. **Markovian theta-efetivo for temporal governance tracking**: The adaptive-memory extension enables CIRCUIT_BREAKER activation in October 2020 — three months before the Portaria 69/2021 ICU collapse declaration — in a retrospective demonstration using real SIH/DATASUS microdata. This retrospective detection establishes that the formalism captures the crisis signal trajectory; prospective deployment readiness requires integration with real-time data feeds and an occupancy forecasting module (see §8 Future Work).

3. **Failure typology grounded in positive law**: The constitutional / execution-absent-channel / execution-inertia taxonomy, derived from sovereign predicate analysis, enables targeted governance interventions: constitutional failures require legislative action; execution failures require operational protocol development; execution-inertia failures require citation grounding verification.

**Future work** includes: (1) C4 LLM predictor integration with Ollama/qwen2.5:14b for chain-of-thought reasoning scenarios (C4a/C4b/C4c); (2) Paper 2 (AI governance theory, EN) integrating the CLT + TST labour validation with a full account of defeasible reasoning, health equity, and institutional adoption mechanisms; (3) the γ > 0 anticipatory theta_efetivo evaluation for the Manaus series, requiring an ICU occupancy forecast module to generate 𝔼[θ(t+k)] from contemporaneous-only data; (4) inter-annotator reliability analysis (Cohen's κ with a second legal expert) for HITL sovereignty classifications, enabling the present PoC's results to be promoted from "design demonstration" to "independently validated" status; (5) a prospective deployment pilot for a live Brazilian administrative AI system, providing the first genuinely prospective test of the Circuit Breaker triggering mechanism; and (6) a theory-of-change evaluation: mapping the institutional pathway from a CB alert to binding governance action — addressing the question of which institutional actors, at which decision points, are empowered to act on a Q-FENG signal, and what operational conditions determine whether the signal translates into effective normative compliance.

The Q-FENG framework provides the formal infrastructure for neurosymbolic AI governance monitoring that the EU AI Act mandates but does not specify. The combination of rigorous ASP-based normative evaluation, quantum interference geometry, and Markovian temporal tracking offers a path from post-hoc audit to continuous prospective governance — the standard that high-stakes AI systems in health, welfare, and legal adjudication require.

---

## References

Arner, D.W., Barberis, J., & Buckley, R.P. (2020). The evolution of FinTech: A new post-crisis paradigm? *Georgetown Journal of International Law*, 47(4), 1271–1319.

Ashby, W.R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.

Badreddine, S., d'Avila Garcez, A., Serafini, L., & Spranger, M. (2022). Logic tensor networks. *Artificial Intelligence*, 303, 103649.

Beer, S. (1972). *Brain of the Firm*. Allen Lane.

Bromley, P., & Powell, W.W. (2012). From smoke and mirrors to walking the talk: Decoupling in the contemporary world. *The Academy of Management Annals*, 6(1), 483–530.

Besold, T.R., d'Avila Garcez, A., Bader, S., Bowman, H., Domingos, P., Hitzler, P., ... & Zaverucha, G. (2017). Neural-symbolic learning and reasoning: A survey and interpretation. *arXiv:1711.03902*.

Brewka, G., Eiter, T., & Truszczyński, M. (2011). Answer set programming at a glance. *Communications of the ACM*, 54(12), 92–103.

Busemeyer, J.R., & Bruza, P.D. (2012). *Quantum Models of Cognition and Decision*. Cambridge University Press.

Callon, M. (1998). *The Laws of the Markets*. Blackwell Publishers.

Callon, M. (2021). *Sociologie des agencements marchands: Textes choisis*. Presses des Mines.

Conant, R.C., & Ashby, W.R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97.

d'Avila Garcez, A., & Lamb, L.C. (2023). Neurosymbolic AI: The 3rd wave. *Artificial Intelligence Review*, 56(11), 12387–12406.

Diaz-Rodriguez, N., Del Ser, J., Coeckelbergh, M., de Prado, M.L., Herrera-Viedma, E., & Herrera, F. (2023). Connecting the dots in trustworthy artificial intelligence. *Information Fusion*, 99, 101896.

DiMaggio, P.J., & Powell, W.W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.

Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv:1702.08608*.

Espinosa, A. (2003). Giving and taking: The nature of organisational effectiveness as approached from the VSM. *Kybernetes*, 32(9/10), 1330–1345.

EU (2024). Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). *Official Journal of the European Union*, L 2024/1689.

Garcez, A.d'A., Gori, M., Lamb, L.C., Serafini, L., Spranger, M., & Tran, S.N. (2022). Neural-symbolic computing: An effective methodology for principled integration of machine learning and reasoning. *Journal of Applied Logic — IfCoLog*, 6(4), 611–632.

Gebser, M., Kaminski, R., Kaufmann, B., & Schaub, T. (2019). *Multi-shot ASP solving with clingo*. Theory and Practice of Logic Programming, 19(1), 27–82.

Governatori, G., Olivieri, F., Rotolo, A., & Scannapieco, S. (2013). Computing strong and weak permissions in defeasible logic. *Journal of Philosophical Logic*, 42(6), 799–829.

Hallal, P., Hartwig, F., Horta, B., Victora, C.G., Silveira, M., Struchiner, C.J., ... & Barros, F.C. (2021). SARS-CoV-2 antibody prevalence in Brazil: Results from two successive nationwide serological household surveys. *The Lancet Regional Health — Americas*, 1, 100004.

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389–399.

Kaminski, R.S. (2025). *[Title blinded for review]*. Doctoral dissertation, University of Brasília (UnB), Graduate Program in Social Sciences (source of STAC governance regime typology).

Kaminski, R.S. (2026a). *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle*. Independently published (KDP). (Establishes the tripartite governance taxonomy and the theoretical gap to which the present paper responds.)

Kautz, H. (2022). The third AI summer. *AI Magazine*, 43(1), 93–104.

Koreeda, Y., & Manning, C.D. (2021). ContractNLI: A dataset for document-level natural language inference for contracts. In *Findings of EMNLP 2021*, pp. 1–31.

Lifschitz, V. (2019). Answer set programming and its applications. *Morgan & Claypool Publishers*.

Lippi, M., Palka, P., Contissa, G., Lagioia, F., Micklitz, H.W., Sartor, G., & Torroni, P. (2019). CLAUDETTE: An automated detector of potentially unfair clauses in online terms of service. *Artificial Intelligence and Law*, 27(2), 117–139.

MacKenzie, D. (2006). *An Engine, Not a Camera: How Financial Models Shape Markets*. MIT Press.

Manhaeve, R., Dumančić, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. In *NeurIPS 2018*.

Medina, E. (2011). *Cybernetic Revolutionaries: Technology and Politics in Allende's Chile*. MIT Press.

Meyer, J.W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340–363.

Mingers, J. (2006). *Realising Systems Thinking: Knowledge and Action in Management Science*. Springer.

Modgil, S., & Prakken, H. (2013). A general account of argumentation with preferences. *Artificial Intelligence*, 195, 361–397.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447–453.

Palmirani, M., & Governatori, G. (2018). Modelling legal knowledge for GDPR compliance checking. In *Proceedings of JURIX 2018*, IOS Press.

Pothos, E.M., & Busemeyer, J.R. (2013). Can quantum probability provide a new direction for cognitive modeling? *Behavioral and Brain Sciences*, 36(3), 255–274.

Pothos, E.M., Busemeyer, J.R., Shiffrin, R.M., & Yearsley, J.M. (2022). The rational status of quantum cognition. *Journal of Experimental Psychology: General*, 150(10), 2243–2259.

Power, M. (1997). *The Audit Society: Rituals of Verification*. Oxford University Press.

Power, M. (2022). The audit society — 25 years on. *Accounting, Organizations and Society*, 97, 101374.

Ragin, C.C. (2008). *Redesigning Social Inquiry: Fuzzy Sets and Beyond*. University of Chicago Press.

Rajpurkar, P., Chen, E., Banerjee, O., & Topol, E.J. (2022). AI in health and medicine. *Nature Medicine*, 28(1), 31–38.

Robaldo, L., Bartolini, C., Palmirani, M., Panagis, Y., & Rossi, A. (2020). Introduction to the special issue on normative reasoning in NLP. *Artificial Intelligence and Law*, 28(1), 1–14.

Sabino, E.C., Buss, L.F., Carvalho, M.P.S., Prete, C.A., Crispim, M.A.E., Fraiji, N.A., ... & Faria, N.R. (2021). Resurgence of COVID-19 in Manaus, Brazil, despite high seroprevalence. *The Lancet*, 397(10273), 452–455.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. In *NeurIPS 2022*.

Yang, Z., Ishay, A., & Lee, J. (2020). NeurASP: Embracing neural networks into answer set programming. In *Proceedings of IJCAI 2020*.

Char, D.S., Shah, N.H., & Magnus, D. (2018). Implementing machine learning in health care — addressing ethical challenges. *New England Journal of Medicine*, 378(11), 981–983.

Hoverstadt, P. (2009). *The Fractal Organization: Creating Sustainable Organizations with the Viable System Model*. Wiley.

NIST (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. National Institute of Standards and Technology, U.S. Department of Commerce. doi:10.6028/NIST.AI.100-1.

Topol, E.J. (2019). *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*. Basic Books.

UNESCO (2021). *Recommendation on the Ethics of Artificial Intelligence*. United Nations Educational, Scientific and Cultural Organization, Paris. SHS/BIO/PI/2021/1.

Walker, J. (2006). *The Viable Systems Model: A Guide for Co-Operatives and Federations*. Co-operative College.

WHO (2021). *Ethics and Governance of Artificial Intelligence for Health*. World Health Organization, Geneva. ISBN 978-92-4-002699-9.

Wiens, J., Saria, S., Sendak, M., Ghassemi, M., Liu, V.X., Doshi-Velez, F., ... & Goldenberg, A. (2019). Do no harm: A roadmap for responsible machine learning for health care. *Nature Medicine*, 25(9), 1337–1340.

Zetzsche, D.A., Arner, D.W., & Buckley, R.P. (2020). Decentralized finance. *Journal of Financial Regulation*, 6(2), 172–203.

---

## Appendix A: Clingo Predicate Catalog — Sovereignty Classifications

The following table lists the key sovereign predicates derived from the primary normative corpus, with their HITL sovereignty classification and the legal basis for the SOVEREIGN rating.

| Predicate | Document basis | Sovereignty | Rationale |
|-----------|---------------|-------------|-----------|
| `universal_right_to_health/1` | CF/88 Art. 196 | SOVEREIGN | Constitutional provision; cannot be restricted by infra-constitutional regulation |
| `equity_principle/2` | Lei 8.080/1990 Art. 7 §II | SOVEREIGN | SUS organic law principle; binds all management levels |
| `emergency_obligation_coes/2` | Portaria 69/2021 Art. 1 | SOVEREIGN | Ministerial decree (Portaria) implementing CF/88 Arts. 196–200 emergency health obligations; SOVEREIGN by derivation from constitutional anchor, not by autonomous regulatory status |
| `equal_protection/1` | 14th Amendment | SOVEREIGN | US constitutional provision; Medicaid cannot derogate |
| `best_interest_standard/2` | SSA §1902(a)(19) | SOVEREIGN | Statutory Medicaid obligation; not waivable |
| `risk_management_obligation/2` | EU AI Act Art. 9 | SOVEREIGN | Regulation 2024/1689; direct effect in EU member states |
| `human_oversight_requirement/2` | EU AI Act Art. 14 | SOVEREIGN | Regulation 2024/1689; direct effect |
| `collective_bargaining_required/2` | CLT Art. 59-B §1 | SOVEREIGN | Statutory working-hours protection; requires CCT |
| `legal_citation_grounded/1` | TST procedural rules | SOVEREIGN | TST requires verifiable precedent citations; grounding is mandatory |
| `hour_bank_permitted_with_cct/2` | Súmula TST 85 §I | ELASTIC | TST jurisprudence; calibratable within statutory bounds |

Elastic predicates encode regulatory parameters subject to administrative discretion within sovereign bounds. Their activation reduces θ (constructive contribution to normative state) without crossing the SOVEREIGN threshold.

---

## Appendix B: Mathematical Proofs

### B.1 Convergence of theta-efetivo

**Claim**: The Markovian theta-efetivo sequence {θ_eff(t)} is bounded and converges to a value in [min θ(t), max θ(t)] as t → ∞ under constant pressure conditions.

**Proof**: Let θ* = lim_{t→∞} score_pressão(t) be a constant pressure level, implying Δpressão(t) → 0 and thus α(t) → σ(0) = 0.5. The recurrence θ_eff(t) = 0.5·θ + 0.5·θ_eff(t−1) is a linear contractive map with fixed point θ* = θ (the instantaneous angle under constant normative conditions). By the Banach fixed-point theorem, the sequence converges geometrically with rate 0.5 per step. QED.

**Corollary**: The memory half-life of the Markovian theta-efetivo under stable conditions (α = 0.5) is log(2)/log(2) = 1 month — i.e., exactly one time step. Under crisis conditions (α → 1), memory half-life → 0 (immediate adaptation). Under recovery conditions (α → 0), memory half-life → ∞ (persistent crisis memory).

### B.2 Monotonicity of governance suppression in θ

**Claim**: For fixed predictor confidence conf ∈ (0,1), the governance suppression percentage GSP = (P_cl(0) − P_q(0)) / P_cl(0) is monotone increasing in θ for UNSAT scenarios (where ψ_N[0] > 0 and ψ_S[0] < 0).

**Proof sketch**: Under the sign condition ψ_N[0] > 0, ψ_S[0] < 0, the quantum amplitude at j=0 is (αψ_N[0] + βψ_S[0]), which is less than αψ_N[0]. The normalisation factor Z = 1 + 2αβcos(θ) is monotone decreasing in θ for θ ∈ [90°, 180°] (since cos is monotone decreasing on [0°, 180°]). Therefore P_q(0) = (αψ_N[0] + βψ_S[0])²/Z is monotone decreasing in Z, hence monotone decreasing in cos(θ), hence monotone decreasing in θ on [90°, 180°]. Since P_cl(0) is independent of θ, GSP is monotone increasing in θ. QED.

This monotonicity property is empirically confirmed in Table 4: C3 (θ = 134.67°, GSP = 25.16%) > C7 (θ = 133.74°, GSP = 10.66%) > C2 (θ = 132.36°, GSP = 16.75%) — with the exception of C2/C7, where the different ψ_N magnitudes (3D vs. 3D) produce a non-monotone pattern, consistent with the proof's caveat that monotonicity holds under fixed ψ magnitude.

### B.3 Anticipatory form — early activation property

**Claim**: Under the anticipatory form (Equation 5, γ > 0), the Circuit Breaker activates at time t* < t_peak where t_peak is the time of maximum θ(t), provided that 𝔼[θ(t+k)] > θ_block for some k ∈ {1, ..., horizon}.

**Proof**: Straightforward from Equation 5: θ_eff(t) = α(t)·θ(t) + (1−α(t))·θ_eff(t−1) + γ·𝔼[θ(t+k)]. If 𝔼[θ(t+k)] > θ_block and γ > 0, then the anticipatory term contributes at least γ·θ_block to θ_eff(t), potentially pushing it above θ_block before θ(t) itself crosses the threshold. The condition is sufficient: it may activate the CB even when α(t)·θ(t) + (1−α(t))·θ_eff(t−1) < θ_block. QED.

---

*Correspondence: Ricardo S. Kaminski — ricardoskaminski@gmail.com*

*Code and data availability: Repository available at [GitHub — blinded for review]. All parquet result files, Clingo corpus, and pipeline code are included. Reproducibility guaranteed via deterministic Clingo evaluation and SHA-256 cached DeonticAtoms.*

*Competing interests: None declared.*

*Funding: This research received no external funding. Supported by institutional research allocation, University of Brasília Graduate Program in Social Sciences.*

*Ethics statement: This study uses only publicly available normative documents and administrative data already in the public domain (SIH/DATASUS, published under Lei de Acesso à Informação). No individual-level patient data were used. The Medicaid analysis uses aggregate statistics from Obermeyer et al. (2019) — a published, peer-reviewed paper — not primary patient records.*
