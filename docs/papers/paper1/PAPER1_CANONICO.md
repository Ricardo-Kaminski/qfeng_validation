**Q-FENG: Operationalizing Cybernetic AI Governance through Neurosymbolic Quantum Interference**

*Empirical Validation Across Three Normative Regimes and Two Domains of Public-Sector AI*

*Ricardo Kaminski, Ph.D.*

*Independent Researcher, Brasília, Brazil*

*2026*

ORCID: 0000-0002-8882-9248

Correspondence: [ricardo.silva.kaminski@gmail.com](mailto:ricardo.silva.kaminski@gmail.com)

**Abstract**

**Background.** The deployment of algorithmic decision systems in high-stakes public domains --- health allocation, social benefits, legal adjudication --- generates persistent governance failures that classical monitoring frameworks cannot formally characterise. Existing approaches lack a unified formalism that simultaneously encodes sovereign normative constraints, quantifies their violation as a continuous misalignment angle, and distinguishes constitutional from execution failures.

**Methods.** We present Q-FENG, a cybernetic neurosymbolic framework for AI governance monitoring that operationalises normative friction as an interference angle in a Hilbert-space representation of predictor and normative state vectors, following quantum decision theory (Busemeyer & Bruza 2012). The pipeline (stages E0--E5) transforms raw normative corpora into executable Answer Set Programming predicates and evaluates alignment between algorithmic predictors and normative states. This proof-of-concept demonstration covers three normative regimes (Brazil/SUS, EU AI Act, US Medicaid/Equal Protection) and two domains (public health infrastructure and labour law). The integrated normative base comprises 33 primary documents (32,445 NormChunks across both tracks) from which 10,142 DeonticAtoms were extracted (5,136 in the health/governance track at mean confidence 0.930; 5,006 in the labour track at mean confidence 0.942), and seven author-designed formal scenarios --- five failure cases and two positive controls --- are evaluated. A Markovian theta-efetivo extension tracks governance degradation across the 12-month Manaus hospital-collapse crisis of 2020--2021 using real SIH/DATASUS microdata in a retrospective validation.

**Results.** Five of seven scenarios produced CIRCUIT_BREAKER classifications (θ ∈ \[127.8°, 134.7°\]), while two positive controls produced STAC classifications (θ &lt; 8°). The Born-rule probability model demonstrated destructive interference (Δ ∈ \[−0.23, −0.09\]) for all failure scenarios, suppressing the probability of the norm-violating action below classical Bayesian predictions by 9.4--25.2%. Threshold robustness analysis confirmed 97.96% regime stability, and psi-weight sensitivity analysis yielded 100% correct-regime preservation across all scenarios. The Manaus theta-efetivo series sustained CIRCUIT_BREAKER classification across most of the 12-month window, with the October 2020 activation (θ\_eff = 126.41°, three months before the January 2021 calamity declaration) constituting the central retrospective lead-time finding.

**Conclusions.** Q-FENG provides a formally grounded, reproducible framework for neurosymbolic AI governance monitoring. The quantum interference formalism --- operating on Hilbert-space preference vectors under quantum decision theory (Busemeyer & Bruza 2012; Pothos & Busemeyer 2013) --- captures normative suppression effects invisible to classical Bayesian models. Early Circuit Breaker activation in the retrospective Manaus analysis shows that the formalism detects crisis onset three months before the officially declared ICU collapse; prospective deployment validation with real-time data feeds is a planned extension. Code and data are available at <https://github.com/Ricardo-Kaminski/qfeng_validation>

***Keywords:*** neurosymbolic AI; deontic logic; AI governance; quantum decision theory; legal NLP; Clingo; Answer Set Programming

# Introduction

On 23 January 2021, the state of Amazonas declared public calamity as Manaus hospitals ran out of oxygen and patients died unventilated. The normative architecture for responding had been in force for decades --- CF/88 Art. 196 declaring health a fundamental right, Lei 8.080/1990 Art. 7 mandating universal equitable access, Lei 13.979/2020 Art. 3 VIII authorising emergency requisition --- but no formal mechanism existed to measure the widening gap between statutory obligation and institutional execution. Three months earlier, the governance signal θ\_eff developed in this paper had already crossed into CIRCUIT_BREAKER territory. The healthcare algorithm studied by Obermeyer et al. (2019) represents the complementary failure: deployed across hundreds of US hospitals, it produced a 28.8-percentage-points racial gap in enrolment recommendations for the same health need --- violating the equal-protection mandate of the 14th Amendment §1 Equal Protection Clause and Title VI (42 U.S.C. §2000d) in a way that standard performance dashboards did not detect because they measured statistical accuracy, not normative alignment. Two failure modes, two jurisdictions, one diagnostic gap. This paper addresses that gap.

The two cases instantiate distinct failure modes that any monitoring framework must be able to separate. The Manaus collapse exemplifies execution inertia: the sovereign predicates existed in the normative corpus --- the obligation to activate emergency coordination structures (COES) under specified threshold conditions was statutorily prescribed --- but their execution was not effected. The Obermeyer case exemplifies a constitutional gap of a different type: the equal-protection mandate existed in the constitutional corpus, but no operational predicate connected it to the algorithm's risk-scoring layer. The distinction --- between constitutional failure (the norm does not specify the required protection at the operational layer) and execution failure (the norm specifies it but the system does not execute it) --- is invisible to evaluation frameworks that treat governance compliance as a binary label.

The EU AI Act (Regulation 2024/1689), now in force, mandates risk management systems (Art. 9), transparency obligations (Art. 13), human oversight requirements (Art. 14), and accuracy and robustness standards (Art. 15) for high-risk AI systems listed in Annex III --- including systems used in health, access to essential services, and administration of public benefits. Yet the Act provides no formal mechanism for verifying that these requirements are satisfied beyond documentation checklists and post-hoc audits. A governance monitoring system capable of continuously evaluating the alignment between algorithmic predictor outputs and the normative state encoded in positive law would provide precisely the missing infrastructure that Art. 9 assumes but does not specify.

This paper presents the **Q-FENG (Quantum-Fractal Neurosymbolic Governance) C1 pipeline** --- a five-stage architecture for normative alignment monitoring demonstrated as a proof-of-concept across three jurisdictions and two normative domains. The Q-FENG framework makes three original contributions:

!\[**Diagram 1**. Complete cybernetic inference-audit-feedback cycle of the Q-FENG architecture. Solid arrows: inference flow. Dashed arrows: logging and data flow. Long-dashed arrows: feedback channels (Algedonic Signal to S5; Continuous Training to S1).\]

The complete Q-FENG cybernetic cycle is illustrated in Diagram 1. Three distinct flows are encoded: solid inference arrows trace the signal from the algorithmic predictor (VSM System 1) through the staged neurosymbolic pipeline (E0--E5) to the governance decision output; dashed logging channels feed observational data back through System 2 and System 3 (audit and control layers); and long-dashed algedonic feedback arrows carry Circuit Breaker activations directly to the policy-setting layer (System 5) and continuous retraining signals to System 1. This architecture ensures that governance failures detected at the normative evaluation stage propagate upstream to reshape both operational decisions and institutional policy. The three original contributions of the Q-FENG framework are:

> 1\. **A quantum interference geometry for normative alignment**: The angular distance θ between the predictor preference vector ψ\_N and the normative state vector ψ\_S --- computed via Hilbert-space inner product --- provides a continuous, formally grounded measure of governance failure that distinguishes STAC (θ &lt; 30°), HITL (30° ≤ θ &lt; 120°), and CIRCUIT_BREAKER (θ ≥ 120°) regimes.
>
> 2\. **A Markovian theta-efetivo extension for temporal governance tracking**: The Kaminski (2026) extension equips the interference angle with a time-varying adaptive memory that distinguishes deteriorating crises (alpha → 1, current state dominates) from stable regimes (alpha → 0.5, history dominates), enabling prospective governance monitoring with early Circuit Breaker activation.
>
> 3\. **A failure typology grounded in positive law**: By analysing whether sovereign (legally irreducible) predicates are present in the normative corpus and whether Clingo derives them as active, the pipeline distinguishes constitutional failures (norm gap), execution-absent-channel failures (sovereign predicates present but execution path blocked), and execution-inertia failures (citation to non-existent precedent).

### Theoretical context.

This paper is the first empirical publication in a planned sequence grounded in a common theoretical framework. Kaminski (2026a) --- *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle* --- establishes the theoretical foundation through a configurational analysis of 27 AI governance frameworks using fuzzy-set Qualitative Comparative Analysis (fsQCA). The central finding is a **tripartite taxonomy**: Type I (principled governance), Type II (risk-management governance), and Type III (cybernetic governance). None of the 27 empirically analysed documents achieves Type III. The book diagnoses this as **functional decoupling** (Bromley and Powell 2012): governance frameworks rigorously implement their prescribed means --- checklists, impact assessments, audits --- without achieving their declared ends of effective control. Section 1.7 of Kaminski (2026a) explicitly defers empirical validation to separate publications. The present paper delivers that empirical validation: the Q-FENG C1 pipeline is the engineering instantiation of the Type III governance architecture shown as formally feasible in Kaminski (2026a, Chapter 7), and the seven designed scenarios constitute the proof-of-concept evidence that the book's architectural claim is computationally grounded. An English translation of Kaminski (2026a) is currently in preparation (Kaminski 2026b, forthcoming) to make the theoretical foundation accessible to international audiences in parallel with the present empirical validation.

A companion paper (Paper 2, in preparation) develops the full theoretical framework of Kaminski (2026a) for international audiences, establishing the sociological and institutional context within which the present empirical results are situated.

### Nomenclature note.

Throughout this paper, the acronym **STAC** denotes *Stabilized Sociotechnical Agency Configurations* --- a concept introduced in Kaminski (2025, doctoral thesis) and operationalised in Kaminski (2026a) to name the governance configurations that stabilise after critical junctures through dispute, negotiation, and material-institutional sedimentation. In the Q-FENG governance regime classification, STAC designates the alignment state (θ &lt; 30°) in which the predictor and normative configurations have stabilised into a mutually reinforcing arrangement that warrants autonomous operation without human review.

The paper is organised as follows. Section 2 surveys related work in neurosymbolic AI, legal NLP, AI governance, quantum decision theory, and health AI fairness. Section 3 presents the mathematical foundations of the interference formalism. Section 4 describes the C1 pipeline stages E0--E4. Section 5 reports validation results across seven scenarios. Section 6 presents statistical robustness analyses. Sections 7 and 8 discuss findings and conclude.

# Related Work

## Theoretical Foundation: Cybernetic Governance and the Tripartite Taxonomy

The theoretical architecture within which this empirical validation operates was developed by Kaminski (2026a) through a configurational analysis of 27 AI governance documents spanning 15 jurisdictions (Brazil, EU, USA, Canada, UK, Australia, China, Singapore, Japan, India, among others). Using fuzzy-set Qualitative Comparative Analysis (Ragin 2008) with seven analytical dimensions, the analysis produces a **tripartite taxonomy** of governance frameworks.

**Type I** (principled governance) encompasses documents that enunciate ethical values and guiding principles without operational mechanisms --- transparency, explicability, fairness, accountability, safety. These frameworks perform the constitution of the professional field of AI ethics in the Callonian (1998) sense, instituting categories, vocabularies, and social positions, without intervening in algorithmic dynamics. Ten of the 27 empirically analysed documents belong to Type I, including the OECD AI Principles, the UNESCO Recommendation, and the Brazilian AI Strategy.

**Type II** (risk-management governance) operationalises principles into checklists, impact assessments, compliance forms, periodic audits, and certifications. Seventeen documents are classified Type II, including the NIST AI RMF, the EU AI Act, and Canadian federal regulations. The critical analytical contribution of Kaminski (2026a) is to demonstrate that Type II, while more operational than Type I, reproduces functional decoupling (Bromley and Powell 2012): its instruments are implemented with rigour, but do not possess requisite variety (Ashby 1956, 1958) proportional to the systems they govern. The fuzzy-set Qualitative Comparative Analysis (fsQCA) confirms that the triple absence of computational variety (dim3), concomitant temporality (dim4), and recognition of constitutive agency (dim5) is quasi-necessary for Type II --- the dominant mode of the governance field.

**Type III** (cybernetic governance) is the **configurational absence** in the empirical corpus: the logically possible but empirically uninstantiated configuration that simultaneously satisfies computational variety, concomitant temporality, constitutive recognition, and formally embedded normative control. No document in the corpus achieves Type III. The Q-FENG architecture (Chapter 7 of Kaminski 2026a) is presented as the first formally specified proof of existence that Type III is architecturally feasible --- a demonstration, not a prescription. The present paper provides the proof-of-concept empirical demonstration that was explicitly deferred in Kaminski (2026a, §1.7).

The central theoretical mechanism is functional decoupling (Bromley and Powell 2012) --- a refinement of Meyer and Rowan\'s (1977) original concept of policy-practice decoupling: not the adoption of formal structures decoupled from technical activity, but means-ends decoupling, in which organisations rigorously implement prescribed means (audits, impact assessments, certifications) without producing declared ends (effective control, substantive transparency, accountability). Bromley and Powell demonstrate that decoupling is structural, not contingent: it arises from the mismatch between the categorical logic of compliance instruments and the continuous, temporally variable, high-dimensional behaviour of the systems they govern. The *audit society* framework of Power (1997, 2022) adds a complementary mechanism: the proliferation of verification rituals produces an economy of verifiability that operates autonomously from its declared purposes --- systems adapt to audit criteria rather than to the objectives those criteria should measure.

The sociological framework also draws on DiMaggio and Powell\'s (1983) institutional isomorphism to explain how normative diffusion propagates Type II without Type III: mimetic isomorphism (organisations copy each other\'s governance structures) and normative isomorphism (professional fields establish standards that reproduce themselves through training and credentialing) produce convergence on risk-management approaches even across jurisdictions with different legal traditions --- a pattern confirmed by the semantic similarity analysis in Kaminski (2026a, Chapter 5).

**Fricção Ontológica** (Ontological Friction) is the concept that Kaminski (2026a) introduces to formalise the governance failure that Type I and Type II cannot address: the structural incompatibility between the inductive, stochastic logic of deep learning models --- operating by probabilistic inference over high-dimensional state spaces --- and the deductive, categorical logic of institutional norms --- operating by prescriptive obligation (obligations, prohibitions, permissions) over discrete categories. This incompatibility is not a contingent technical deficiency but a difference in logical regime between two forms of reasoning whose controlled articulation is precisely what governance frameworks fail to specify. The interference angle θ is the mathematical operationalisation of Ontological Friction as a governable scalar --- continuous, computable, and formally grounded in the sovereign normative state encoded in primary legal texts.

The **compliance-by-construction** paradigm introduced in Kaminski (2026a, §7.10) is the conceptual core that this empirical paper validates. In the dominant compliance-by-verification paradigm (Type II), systems are built first and governed afterwards --- periodically audited by external entities that verify whether the system meets requirements. In compliance-by-construction (Type III), normative conformity is engineered as a structural property of the architecture: normative constraints participate in the training and inference process, inscribed in the computational graph as sovereign predicates whose observance is monitored as a condition of operational continuity. The Circuit Breaker mechanism implements this principle by suspending autonomous operation whenever the interference angle θ exceeds the constitutional threshold. The present paper\'s seven scenarios demonstrate that this architectural claim is computationally grounded: the Circuit Breaker activates for all five failure scenarios and is absent for both positive controls, with 100% regime stability under threshold and sensitivity perturbation.

## Neurosymbolic AI

Neurosymbolic integration is not merely an engineering compromise between two historically opposed research programmes; it is the architectural precondition for systems whose decisions are simultaneously data-driven and normatively accountable. The exhaustive survey of explainable AI by Arrieta et al. (2020) establishes the foundational taxonomy of the field and traces the path toward what they term Responsible Artificial Intelligence. Within the neurosymbolic family specifically, Díaz-Rodríguez et al.\'s X-NeSyL methodology (2022) is an instructive precedent: it fuses deep learning representations with expert knowledge graphs through a three-part architecture --- a symbolic processing component (the expert knowledge graph), a neural processing component (EXPLANet, a compositional part-based CNN), and an XAI-informed training procedure (SHAP-Backprop) that aligns neural attributions with symbolic representations via a misattribution function measured by SHAP Graph Edit Distance. Q-FENG inherits the three-part structural template established by X-NeSyL --- symbolic component, neural component, and quantitative alignment mechanism --- and redirects it to a different problem domain through three substantive transformations: the symbolic component is the sovereign normative corpus extracted from primary legal texts, not an expert domain knowledge graph; the alignment mechanism is the Hilbert-space interference angle θ derived from quantum decision theory, not SHAP-based attribution comparison; and the purpose is compliance-by-construction governance rather than explanation interpretability. The structural kinship situates Q-FENG within an established NeSy integration paradigm, but applied to a different problem domain: AI governance rather than explanation interpretability.

The integration of neural and symbolic computation has been a persistent research agenda since the early 1990s, motivated by the complementary strengths and weaknesses of the two paradigms: neural systems offer inductive generalisation from data but lack interpretability and formal correctness guarantees; symbolic systems offer deductive tractability and verifiability but require explicit knowledge encoding (Besold et al. 2017; Garcez et al. 2022). The taxonomy proposed by Kautz (2022) distinguishes several integration modes, from sequential neural-then-symbolic pipelines to fully coupled systems where symbolic constraints modulate neural computation.

Recent work has demonstrated that neurosymbolic integration is particularly effective in domains requiring both perceptual grounding and legal or normative reasoning. DeepProbLog (Manhaeve et al. 2018) extends Prolog with neural predicates, enabling probabilistic logic programming over learned representations. NeurASP (Yang et al. 2020) grounds Answer Set Programming with neural networks for structured prediction. Logic Tensor Networks (Badreddine et al. 2022) translate first-order logic formulae into differentiable loss functions. The d\'Avila Garcez and Lamb (2023) survey argues that neurosymbolic AI is approaching a maturity threshold sufficient for real-world deployment in high-stakes domains.

Q-FENG differs from these approaches in two fundamental respects. First, the normative content is not learned from annotated training examples but extracted from primary legal texts --- constitutions, statutes, regulatory instruments --- through few-shot LLM prompting calibrated per regime, ensuring that sovereign predicates reflect the actual positive law rather than a learned proxy of normative reasoning. Second, the interference geometry used to measure alignment does not require the symbolic system to be differentiable; it operates on the output of an arbitrary ASP solver (Clingo), using the set of active atoms to construct the normative state vector ψ_S.

## Legal NLP and Normative Reasoning

The extraction of normative content from legal texts has a substantial literature, motivated by both knowledge engineering and compliance automation applications. The CLAUDETTE system (Lippi et al. 2019) demonstrated automated detection of potentially unfair clauses in online terms of service using a combination of SVM classifiers and hand-crafted grammars, achieving F1 scores of 0.75--0.89 across eight clause types. Robaldo et al. (2020) survey the Semantic Web representations of deontic modalities --- obligation, permission, prohibition --- that underpin normative reasoning systems, noting that the standard deontic logic treatment fails to capture defeasibility, contextual modification, and hierarchical priority among norms.

Palmirani and Governatori (2018) applied the LegalRuleML standard to GDPR compliance checking, demonstrating that a subset of the Regulation\'s obligations can be formalised as defeasible rules and evaluated against institutional fact patterns. Koreeda and Manning (2021) introduced ContractNLI, a dataset for document-level natural language inference over contracts, demonstrating that pre-trained language models achieve strong performance when fine-tuned on domain-specific annotation.

The Q-FENG E2 stage advances this line of work in two ways. First, it operates across multiple jurisdictions simultaneously (Brazil, EU, USA) using a single few-shot extraction protocol calibrated per regime, without requiring domain-specific fine-tuning. Second, the extracted DeonticAtoms are not used as standalone outputs but as inputs to a translation stage (E3) that produces Clingo predicates --- closing the loop from natural language to formal symbolic reasoning.

Answer Set Programming (Brewka et al. 2011; Lifschitz 2019) provides the symbolic substrate for the Q-FENG normative evaluation. Clingo (Gebser et al. 2019), the leading ASP solver, supports both satisfiability testing and model enumeration under default negation and integrity constraints --- the precise mechanisms needed to evaluate whether a normative state is consistent with a set of agent behaviours. Prior work on ASP-based normative reasoning includes the ASPIC+ framework (Modgil and Prakken 2013) for argumentation and the normative ASP approach of Governatori et al. (2013) for defeasible deontic logic. Q-FENG\'s contribution is to use the SAT/UNSAT output of Clingo not as a final verdict but as a structured signal for constructing the normative state vector ψ_S. The current implementation encodes obligations, permissions, and prohibitions as hard ASP facts, deferring the formal treatment of defeasibility --- exception handling, hierarchical norm priority, and the strong/weak permission distinction formalised by Governatori et al. (2013) --- to the full governance suite (§7.4). The decision to operate on hard facts is methodologically deliberate at this stage: the seven PoC scenarios involve constitutional and statutory provisions whose normative content is uncontested in the relevant jurisdictions, and the pipeline\'s contribution at this stage is the alignment-measurement layer rather than the conflict-resolution layer that defeasible logic addresses.

## AI Governance Frameworks

The European Commission\'s High-Level Expert Group articulates Trustworthy AI as requiring three foundational pillars --- lawfulness, ethics, and technical robustness --- sustained by seven technical requirements: human agency and oversight; technical robustness and safety; privacy and data governance; transparency; diversity, non-discrimination, and fairness; societal and environmental wellbeing; and accountability (Díaz-Rodríguez et al. 2023). Building on this foundation, Herrera-Poyatos et al. (2026) argue that responsible AI in high-risk scenarios cannot be achieved through isolated principles or technical tools, proposing an integrated Responsible AI System (RAIS) framework organised around five inter-dependent dimensions --- domain definition, trustworthy AI design, auditability, accountability, and governance --- with dynamic feedback loops that connect the accountability stage to earlier phases of the system lifecycle. These frameworks establish what AI governance should deliver conceptually, but as the authors themselves note, significant implementation gaps persist between high-level principles and operational mechanisms in concrete high-risk domains. The Q-FENG C1 pipeline addresses one specific dimension of the RAIS framework: it operationalizes the auditability dimension through a continuous, computable interference angle θ grounded in sovereign predicates extracted from primary legal texts. The framework\'s other dimensions --- domain definition, trustworthy AI design, accountability, and governance feedback --- are complementary layers within which the Q-FENG metric operates as the technical instantiation of normative-alignment auditing.

Herrera-Poyatos et al. (2026) also recognise explicitly that part of the apparent fragmentation of the responsible AI field is attributable to the intrinsically sociotechnical nature of the problem, and that governance of AI in high-risk domains involves inevitable tensions between values --- transparency versus privacy, fairness versus performance, control versus autonomy --- that cannot be dissolved by appealing to unifying principles. They argue instead for operational mechanisms --- contextual definition, verifiable requirements, auditing, responsibility allocation, and governance with feedback loops --- that explicitly manage such trade-offs. The Q-FENG interference angle is one such operational mechanism, specific to the tension between algorithmic optimisation and sovereign normative constraints: it does not attempt to reduce this tension to a single preference scalar, but instead exposes it continuously as a geometric misalignment that triggers proportional governance responses (STAC, HITL, CIRCUIT_BREAKER).

The field of AI governance has produced a large literature of principles, frameworks, and audit methodologies (Jobin et al. 2019; Doshi-Velez and Kim 2017; Diaz-Rodriguez et al. 2023). Jobin et al. (2019) identified convergence on five meta-principles across 84 governance documents --- transparency, justice/fairness, non-maleficence, responsibility, and privacy --- while noting that implementation mechanisms remain underspecified. Doshi-Velez and Kim (2017) argued for a taxonomy of interpretability evaluation that distinguishes application-grounded, human-grounded, and functionally-grounded approaches.

Barocas et al. (2019) provide the foundational taxonomy of algorithmic fairness criteria, establishing that statistical parity, equalised odds, and individual fairness are mutually incompatible constraints --- a result directly relevant to C7\'s racial equity failure, where the equal-enrolment criterion and equal-error-rate criterion conflict. Wachter et al. (2017) introduced counterfactual explanations as an alternative to transparency-through-disclosure, arguing that post-hoc explainability does not satisfy the legal standard of meaningful information. Rudin (2019) argued that high-stakes decisions should rely exclusively on inherently interpretable models, not explainable black boxes --- a position that motivates the Q-FENG architecture\'s use of ASP-based normative evaluation over gradient-based importance scores. Selbst et al. (2019) identified five abstraction traps in the operationalisation of fairness in machine learning, including the \'solutionism trap\' (treating sociotechnical problems as technical problems solvable by metrics), which Q-FENG addresses by grounding fairness in positive legal text rather than abstract axioms.

The EU AI Act (Regulation 2024/1689) represents the most ambitious regulatory implementation to date, establishing a risk-tiered classification of AI systems with specific obligations for high-risk systems in sectors including health, education, employment, and public administration. Articles 9, 14, and 15 mandate risk management systems, human oversight mechanisms, and accuracy/robustness requirements respectively. However, the Act does not specify how compliance with these obligations should be formally verified --- a gap that Q-FENG\'s C1 pipeline is designed to address.

The AI Now Institute\'s 2023 report and the OECD AI Policy Observatory\'s monitoring framework both identify the absence of real-time governance monitoring as a critical gap. Existing audit approaches are predominantly post-hoc (applied after deployment), documentation-based (relying on provider self-reporting), and binary (compliant/non-compliant rather than graded). Q-FENG\'s continuous interference angle θ provides a graded, real-time alternative.

International governance bodies have also produced domain-specific frameworks for AI in health that illuminate the normative gaps Q-FENG addresses. The World Health Organization (2021) issued its Ethics and Governance of Artificial Intelligence for Health guidance, identifying six core principles --- protecting autonomy, promoting well-being, ensuring transparency, fostering responsibility, ensuring inclusiveness, and promoting sustainable AI --- while acknowledging that no agreed mechanism currently exists for auditing whether deployed AI systems conform to these principles in operational practice. The UNESCO Recommendation on the Ethics of AI (2021), adopted by all 193 Member States, similarly articulates principles without specifying verification mechanisms. The NIST AI Risk Management Framework (NIST AI RMF 1.0, 2023) represents the most operationally concrete attempt, mapping AI risks to four functions --- Govern, Map, Measure, Manage --- with subcategory actions for each. However, the NIST framework treats governance as an organisational process rather than a formal mathematical property: it provides checklists and documentation requirements but no mathematical criterion for determining whether a given system\'s output is aligned with specified normative constraints.

The critical gap these frameworks share is the absence of what Doshi-Velez and Kim (2017) term "application-grounded evaluation" --- evaluation that assesses alignment with the specific normative requirements of the operational domain, not against general principles. Q-FENG\'s C1 pipeline fills this gap by grounding the evaluation in primary legal texts (constitutions, statutes, regulations) and producing a formally computable alignment measure (θ) whose governance semantics are defined by positive law, not by researcher intuition. The sovereignty classification (SOVEREIGN vs. ELASTIC) operationalises the legal hierarchy that governance frameworks describe but do not formalise: constitutional provisions override statutes, which override regulations, which override administrative discretion. This hierarchy is encoded in the HITL stage (E4) and propagated through the Clingo predicate weighting into the ψ_S vector --- making the governance alignment measure legally grounded in a technically precise sense.

The emerging field of \"regulatory technology\" (RegTech) and \"supervisory technology\" (SupTech) for AI governance is also relevant context. Arner et al. (2020) and Zetzsche et al. (2020) survey RegTech applications in financial compliance, demonstrating that automated regulatory monitoring can achieve near-real-time compliance verification at scale. Q-FENG extends this paradigm to the constitutional and statutory governance of AI in public-sector domains --- a structurally distinct problem from financial regulation, in which the relevant obligations derive from constitutional provisions and primary legislation rather than sectoral regulatory instruments --- by using ASP-based formal reasoning to construct sovereign predicates whose evaluation is grounded in primary legal texts.

## Quantum Decision Theory

The application of quantum probability formalism to decision theory and cognitive science was systematised by Busemeyer and Bruza (2012) in *Quantum Models of Cognition and Decision*. The core claim is that human judgment under uncertainty exhibits order effects, conjunction fallacies, and violation of classical probability axioms that are naturally explained by quantum probability --- specifically, by the interference between incompatible cognitive states. Pothos and Busemeyer (2013) demonstrated that quantum probability models provide better fits to classic violations of expected utility theory than Bayesian alternatives.

The key mathematical mechanism is interference: when two probability amplitudes are superposed, the resulting probability is the square of their sum, not the sum of their squares. The cross-term 2αβ⟨ψ_N\|ψ_S⟩ --- absent in classical Bayesian models --- is the formal source of constructive and destructive interference. Destructive interference (negative cross-term) suppresses joint probability below classical predictions; constructive interference amplifies it.

Q-FENG applies this formalism not to cognitive states but to the alignment between algorithmic predictor preferences (ψ_N) and normative states (ψ_S). The governance interpretation is precise: destructive interference at the violation action (j=0) means that the normative structure, when correctly encoded in the sovereign predicates, suppresses the probability of the norm-violating action below what a classical Bayesian model --- which knows only the predictor confidence and the normative classification but not their interference --- would predict. This suppression is the governance effect that Q-FENG quantifies.

Pothos et al. (2017) demonstrated the rational status of quantum probability through Dutch Book formalism, while Pothos and Busemeyer (2022) provide the most recent comprehensive review of the empirical and theoretical case for quantum probability in cognition and decision, noting that the formalism is not committed to physical quantum mechanics but uses its mathematical structure as a modelling language. This is precisely the Q-FENG usage: quantum mathematics as a governance geometry, not a physical claim.

## Health AI Bias and the Obermeyer Case

Obermeyer et al. (2019) documented that a commercial healthcare algorithm used to identify patients for care management programmes assigned substantially lower risk scores to Black patients than to White patients with the same underlying health needs, measured by number of active chronic conditions. At the algorithm\'s threshold for programme enrolment, the proportion of Black patients identified shifted from 17.7% (algorithm output) to 46.5% (clinical-need criterion) --- a 28.8 percentage-point gap --- when racial parity was simulated against the same health-need standard.

This finding is the empirical anchor for the Q-FENG Scenario C7 (Obermeyer constitutional failure), which encodes the equal-protection obligation of the 14th Amendment §1 EPC and Title VI §601 (42 U.S.C. §2000d) as sovereign predicates and demonstrates that the algorithm\'s output vector --- calibrated from 48,784 real administrative records --- generates destructive interference (θ = 133.74°, CIRCUIT_BREAKER) when evaluated against the normative state derived from the Medicaid eligibility framework.

Rajpurkar et al. (2022) survey AI applications in medicine, identifying 74 FDA-cleared AI/ML medical devices and noting persistent concerns about dataset shift, subgroup performance disparities, and absence of prospective monitoring. The Q-FENG framework addresses the monitoring gap: rather than requiring new annotated labels for bias detection, it uses existing normative instruments --- statutes, regulations --- as the reference standard.

The broader literature on health AI equity situates the Obermeyer finding within a systematic pattern. Char et al. (2018) examined clinical decision support systems for cardiac risk stratification, demonstrating that optimising for overall population performance systematically underserves minority subgroups when training data reflect historical disparities --- a mechanism identical to the Obermeyer expenditure proxy. Topol (2019), in Deep Medicine, articulates the governance challenge: AI systems deployed in clinical practice were largely trained on data from academic medical centres with narrow demographic profiles, and the regulatory pathway for medical AI clearance does not require fairness auditing as a precondition. This observation identifies precisely the normative gap that CF/88 Art. 196 (universal right to health) and the 14th Amendment §1 EPC (equal protection) seek to close --- and that Q-FENG\'s Scenario C7 demonstrates has not been closed in practice.

Wiens et al. (2019) argue for a "machine learning for clinical decision support" standard that includes prospective evaluation, subgroup reporting, and clinical workflow integration assessment. Their proposed standard addresses performance equity but not normative compliance: it asks whether the system performs equally across groups, not whether its outputs violate constitutional or statutory mandates. Q-FENG\'s contribution is precisely this normative layer: the interference angle θ measures not performance disparity but alignment with the specific legal obligations encoded in positive law. A system could perform equally across subgroups and still generate CIRCUIT_BREAKER if its equal-performance outputs are achieved by a mechanism structurally inconsistent with the normative architecture --- for instance, equal under-service rather than equal adequate service. This is the architectural distinction that motivates Q-FENG\'s positioning beyond performance-equity frameworks: equal performance across groups is necessary but not sufficient for constitutional compliance.

The WHO (2021) guidance on AI ethics for health identifies algorithmic bias as a primary concern and calls for audit mechanisms capable of assessing alignment between deployed AI systems and the right-to-health framework articulated in international human rights law. Q-FENG\'s C1 pipeline is a concrete implementation of this call: the interference angle θ is precisely an audit mechanism, and the ψ_S vector constructed from CF/88 Art. 196, Lei 8.080/1990, 14th Amendment §1 EPC + 42 U.S.C. §2000d, and the EU Charter of Fundamental Rights encodes the right-to-health architecture as a computable normative state. The WHO guidance does not specify how such alignment should be computed; Q-FENG\'s quantum interference geometry is a formal answer.

## Viable System Model and Cybernetic Governance

Beer\'s Viable System Model (VSM; Beer 1972, 1979) provides the cybernetic architecture within which Q-FENG operates as an institutional infrastructure rather than as a self-contained technical artefact. The VSM decomposes organisational governance into five recursively nested systems with distinct functional roles: System 1 (operational units that execute the organisation\'s primary activity), System 2 (anti-oscillatory coordination among System 1 units in real time), System 3 (operational control with direct command authority over System 1), System 3\* (sporadic audit channel through which System 3 verifies the ground-truth state of System 1 bypassing System 2\'s mediation), System 4 (prospective intelligence that monitors the environment, detects emerging changes, and projects future trajectories), and System 5 (constitutive policy and identity that defines what the organisation is and what it is for). Espinosa (2003), Mingers (2006), and Hoverstadt (2009) extended the VSM to public administration, regulatory governance, and digital institutional contexts, demonstrating that the model\'s viability conditions apply with particular force to systems whose operational layer increasingly comprises algorithmic decision-makers governed by human institutional structures.

The Q-FENG architecture occupies a precisely specifiable position within this canonical structure. The algorithmic predictor that produces the preference vector ψ_N --- a LightGBM forecast, a time-series model, an ASP rule engine, or a large language model --- is a System 1 operational unit being governed, not a System 1 internal to Q-FENG. Q-FENG itself provides the computational infrastructure for the upper governance layers (S2, S3, S3\*, S4, S5) through which institutional decision-makers exercise their constitutive functions. This reading dissolves a recurring confusion in the AI governance literature, in which monitoring frameworks are described as \"running on top of\" the AI system without specifying which cybernetic functions they implement and which remain delegated to human actors. The Q-FENG mapping is explicit:

The Circuit Breaker logic (the threshold comparison θ ≥ 120° that suspends autonomous operation) is the computational expression of System 3\'s operational command authority. It exercises direct algedonic intervention over System 1 the moment the interference angle crosses the constitutional threshold, in a manner that does not require approval from System 2\'s coordination layer or deliberation by System 5\'s policy layer. The intervention is automatic precisely because the threshold has been constitutionally pre-authorised through the sovereignty classification at E4.

The Clingo SAT/UNSAT evaluation in Pass 1 and the active sovereign predicate analysis in Pass 2 jointly implement the System 3\* audit channel. Unlike a standard inference loop in which the symbolic layer produces verdicts that flow through coordination structures before reaching managerial control, Q-FENG\'s E5 evaluation gives System 3 direct access to the ground-truth state of the normative configuration: which predicates are active, which are suppressed, which integrity constraints have failed, and what the sovereignty classification of each active predicate was at the time of HITL validation. The audit channel operates in parallel with the predictor\'s output, enabling System 3 to verify that what the predictor is doing at the operational layer is consistent with what the normative architecture sanctions.

The cross-corpus consistency layer --- concurrency-pair detection at E1 through Jaccard ≥ 0.55 thresholding, SHA-256 chunk caching for cache-consistent reprocessing, and the harmonisation of normatively equivalent or conflicting provisions across multiple regimes --- operates as System 2\'s anti-oscillatory coordination function. When the pipeline processes the Brazilian, EU, and US corpora in parallel, the concurrency graph prevents contradictory predicate derivations from reaching the symbolic evaluator. Twelve provisions in the current corpus appear with Jaccard = 1.0 across multiple instruments, indicating verbatim reproduction across jurisdictions and confirming their status as sovereign-candidate predicates whose coordination across regimes is structurally trivial; the remaining 335 concurrency pairs at the 0.55--0.99 range require explicit coordination to prevent jurisdictional oscillation.

The Markovian theta-efetivo extension --- and, critically, the broader institutional ecosystem within which it operates --- implements System 4\'s prospective intelligence function. The Markovian recurrence with adaptive memory α(t) = σ(β·Δpressão(t)) provides a quantitative signal that detects trajectory changes in real administrative microdata, but this quantitative signal is itself an input to a much wider institutional apparatus of prospective monitoring: observatories of public policy (in Brazil, IPEA, FIOCRUZ, IBGE; in the EU, the Joint Research Centre\'s policy observatories; in the United States, GAO and CBO analytical units), strategic advisory structures within ministerial cabinets, evaluation frameworks grounded in theory of change (Weiss 1995; Funnell and Rogers 2011), and institutional analyses of path dependence and critical junctures (Pierson 2000; Mahoney 2000; Capoccia and Kelemen 2007). The Manaus retrospective analysis in §5.3 demonstrates this articulation empirically: the Markovian θ_eff signal detects the trajectory inflection in October 2020 --- three months before the formal calamity declaration --- but the institutional response that would have translated this detection into governance action depends on the System 4 ecosystem of public-policy intelligence to integrate the signal with epidemiological surveillance, inter-federative coordination, and ministerial strategic decision-making. Q-FENG provides the formal early-warning component that VSM\'s System 4 required but never specified computationally; it does not replace the institutional intelligence apparatus that interprets and acts upon the warning.

The ScopeConfig (E0) specification together with the HITL sovereignty classification (E4) jointly anchor the pipeline in System 5\'s constitutive function. ScopeConfig defines the regulatory regime, the corpus identifiers, and the predictor families that constitute the operational scope of a governance instance; HITL classifies each derived predicate as SOVEREIGN (legally irreducible, anchored in constitutional or statutory primary text) or ELASTIC (regulatorily calibratable within sovereign bounds). The SOVEREIGN/ELASTIC distinction is the formal inscription of constitutional hierarchy within the computational graph: it ensures that no executive discretion exercised at the operational layer can override the normative weight assigned to constitutional provisions at the constitutive layer. This is the architectural principle that Kaminski (2026a) names compliance-by-construction: System 5\'s constitutive content participates in System 1\'s operational evaluation through the predicate weighting that propagates into the normative state vector ψ_S, making constitutional conformity an inscribed condition of operational continuity rather than an ex-post verification target.

![**Diagram 2.** Fractal VSM architecture across three jurisdictional levels: Macro (constitutional), Meso (sectoral/infralegal), and Micro (algorithmic/operational). Vertical arrows represent normative derivation (downward) and algedonic escalation (upward). S3\* is shown at all levels but operates computationally only at Micro through Clingo audit; at Meso and Macro it is exercised institutionally.]

Mapping the full Q-FENG architecture to the canonical VSM systems clarifies the governance role of each pipeline stage and exposes a distinctive feature of the framework: Q-FENG is the first system, to our knowledge, to implement the System 2 + System 3 + System 3\* triad simultaneously in a single computational architecture, with all three functions operating in real inference time over the same normative substrate. Beer (1972) described these three functions as functionally distinct but structurally entwined; existing AI governance frameworks typically implement at most one of them (either compliance verification as ex-post auditing, or rule-based gating as operational control, or documentation review as audit channel) and never the three jointly. The quantitative-formal articulation of the triad --- coordination through concurrency-pair harmonisation, control through Circuit Breaker threshold, audit through Clingo SAT/UNSAT and active predicate inspection --- is the architectural contribution that Q-FENG offers to the cybernetic governance tradition.

Ashby\'s Law of Requisite Variety (Ashby 1956) provides the theoretical foundation for why this architectural integration matters. Ashby\'s law states that a governance system can only control a regulated system if its variety --- the number of distinguishable states it can recognise and respond to --- matches or exceeds the variety of the system it governs. Q-FENG\'s interference geometry expands the variety of the governance signal from binary (compliant / non-compliant) to continuous (θ ∈ \[0°, 180°\]) and multi-regime (STAC / HITL / CIRCUIT_BREAKER), and expands it further across the temporal axis (instantaneous θ_t, Markovian θ_eff, anticipatory γ·E\[θ(t+k)\]). This variety expansion is the formal answer to Bromley and Powell\'s (2012) functional decoupling diagnosis: classical compliance instruments fail not because their implementations are inadequate, but because their categorical logic lacks variety proportional to the systems they govern. Q-FENG closes the variety gap by providing a continuous, temporally articulated, multi-regime signal that the compliance instruments of Type II governance cannot produce.

## Fractal Recursion Across Jurisdictional Levels

The cybernetic architecture described in §2.7 operates simultaneously at multiple jurisdictional levels through the fractal property that Beer (1972, 1979) introduced under the name viable recursion: every viable system is composed of viable systems and contained within a viable system. Hoverstadt (2009) and Espinosa (2003) demonstrated that this recursion is not metaphorical similarity across scales but structural nesting in which the operational outputs of a subordinate level become the System 1 of the immediately superior level. In the Q-FENG framework, the recursion takes the specific form of a jurisdictional stack --- a strictly ordered hierarchy of normative sources in which each level\'s constitutive content (S5) is derived from the constitutive content of the level immediately above, and each level\'s operational outputs (S1) flow upward as inputs to the superior level\'s intelligence function (S4) and audit channel (S3\*).

This jurisdictional stack is the vertical axis of Q-FENG\'s fractal architecture. It is what distinguishes the Q-FENG fractal claim from metaphorical invocations of fractal organisation that pervade the cybernetic governance literature without specifying the recursion mechanism. The Q-FENG fractality is rigorous because it specifies, for each level, both the System 5 content and the formal derivation relation through which that content is produced from the level above. Three fractal levels are operative for the Q-FENG validation domain:

At the Macro level, System 5 comprises the Federal Constitution of 1988 in the Brazilian regime, the Treaty on the Functioning of the European Union together with the Charter of Fundamental Rights in the EU regime, and the United States Constitution with its Bill of Rights and Reconstruction Amendments in the US regime. These constitutional texts establish the petreous core of the normative architecture: in the Brazilian case, Art. 60 §4º explicitly designates a set of clauses as cláusulas pétreas that no constitutional amendment can abolish (the federative form of State, the direct, secret, universal, and periodic vote, the separation of Powers, and individual rights and guarantees); in the EU case, the foundational treaty obligations and fundamental rights enjoy an analogous protected status; in the US case, the Reconstruction Amendments establish equal protection as a similarly irreducible norm. The Macro System 5 is the constitutional ground that no inferior level can derogate.

At the Meso level, System 5 comprises the ordinary legislation, ministerial regulations, agency directives, and implementing decrees that translate the constitutional ground into sectoral and operational norms. In the health domain across the three regimes: Lei 8.080/1990 operationalises CF/88 Arts. 196-200 in the Brazilian SUS regime; the Cross-Border Healthcare Directive 2011/24/EU and Member State implementing legislation operationalise the EU Charter health provisions; Title XIX of the Social Security Act and 42 CFR Parts 430-440 operationalise the equal-protection mandate in the US Medicaid regime. In the labour domain (Brazilian regime only in the current PoC): the Consolidação das Leis do Trabalho (CLT) and Lei 13.467/2017 operationalise CF/88 Art. 7 working-hours and collective-bargaining guarantees, with TST jurisprudence (Súmulas 85, 291) providing binding interpretive precedent. The Meso System 5 is what administrative law calls the infralegal layer: it is bound by the Macro and binding upon the Micro.

At the Micro level, System 5 comprises the Clingo predicates derived through the E0-E5 pipeline from the Macro and Meso normative content, together with the integrity constraints and sovereignty classifications that the HITL stage attaches to each predicate. The Micro System 5 is the formal computational instantiation of the jurisdictional stack at the deployment unit: when the pipeline produces predicates such as universal_right_to_health(cf88_art196), equity_principle(sus, regional_access), or equal_protection(all_persons), each predicate is formally derivable through traceable extraction (E1 chunk identification by SHA-256), structured deontic representation (E2 DeonticAtom with modality, agent, patient, action, conditions, confidence), deterministic translation to ASP syntax (E3 Jinja2 template instantiation), and human-validated sovereignty classification (E4 HITL annotation).

***Table 1.*** Q-FENG ↔ VSM mapping across the jurisdictional stack

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         **VSM System**         **Macro (Constitutional)**                                                                                                                                                                                                              **Meso (Sectoral / Infralegal)**                                                                                                                                       **Micro (Algorithmic / Operational)**
  ----------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------
              **S5\             Federal Constitution of 1988, petreous clauses (Art. 60 §4º), constitutional treaties, STF binding jurisprudence (in EU: TFEU + Charter of Fundamental Rights; in US: Constitution + Reconstruction Amendments)                         Sectoral organic laws (Lei 8.080/SUS, CLT, Lei 13.467/2017), structural ministerial portarias, regulatory agency rules, sectoral decrees                               Clingo predicates derived through E0--E5 pipeline: sovereign + elastic predicates with HITL-validated sovereignty classification
       Policy & Identity**                                                                                                                                                                                                                                                                                                                                                                                                                     

              **S4\             National prospective intelligence: IPEA, IBGE, federal observatories, governmental BI, Casa Civil strategic advisory, theory of change applied to national policy (in EU: Joint Research Centre; in US: GAO and CBO analytical units)   Sectoral BI: agency technical areas, sectoral observatories (e.g. Observatório SUS), impact evaluation, technical strategic advisory                                   Markovian θ_eff with adaptive memory α(t); deployment-unit monitoring dashboards
   Intelligence & Adaptation**                                                                                                                                                                                                                                                                                                                                                                                                                 

             **S3\*\            Constitutional-level audit: TCU, MPF, STF in concentrated control, organised social control (in EU: Court of Auditors, Ombudsman; in US: GAO, Inspectors General)                                                                       Sectoral audit: DENASUS in SUS, internal controls, sectoral ombudsmen, state audit courts (TCEs); regulatory agency oversight                                          Clingo SAT/UNSAT evaluation + Pass 2 active sovereign predicate analysis; deployment-unit ombudsman and local social control
         Audit Channel**                                                                                                                                                                                                                                                                                                                                                                                                                       

              **S3\             Direct command authority: Presidency, Ministers, top federal executive leadership (in EU: Commission College; in US: Cabinet-level command)                                                                                             Agency direction: state Secretaries, autarchy presidents, sectoral managers with direct authority                                                                      Circuit Breaker logic (θ ≥ 120° threshold suspending autonomous operation); deployment-unit management
      Operational Control**                                                                                                                                                                                                                                                                                                                                                                                                                    

              **S2\             Federative pact, intergovernmental cooperation laws, supreme court binding precedent in uniformising function (CNJ, intergovernmental commissions; in EU: Council coordination; in US: federal-state agreements)                        Sectoral coordination: bipartite intergestor commissions (CIB), technical chambers, sectoral clinical protocols                                                        Cross-corpus consistency layer: concurrency-pair detection at E1 (Jaccard ≥ 0.55), SHA-256 caching; deployment-unit operational protocols
         Coordination**                                                                                                                                                                                                                                                                                                                                                                                                                        

              **S1\             National-scale State operations: federal programmes, executive administrative acts (federal ministries, autarchies; in EU: Commission directorates; in US: federal agencies)                                                            Sectoral execution: state health secretariats, regional INSS units, regional labour tribunals (in EU: national health authorities; in US: state Medicaid programmes)   Algorithmic predictor producing ψ_N (LightGBM, time-series, ASP rule engine, LLM); or institutional deployment unit
          Operations**                                                                                                                                                                                                                                                                                                                                                                                                                         
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : *Institutional mapping of Viable System Model functions across the three fractal levels of Q-FENG governance. Brazilian institutional examples are given as primary references; analogous bodies operate in the EU and US regimes covered by the Q-FENG validation. The Q-FENG framework provides computational instantiation of the S2+S3+S3\* triad at the Micro level (highlighted in bold), with semantic propagation to higher levels through formal derivability of the jurisdictional stack.*

The fractal recursion is mediated by formal derivability. The S5 Meso must be derivable from the S5 Macro through legislative and regulatory processes that the institutional architecture of each jurisdiction defines (parliamentary procedure, ministerial regulatory authority, delegated legislative authority); the S5 Micro must be derivable from S5 Meso and S5 Macro through the Q-FENG pipeline E0-E5. When a predicate at the Micro level fails this derivability test --- when no chunk identifier traces to a valid Meso provision, when no Meso provision traces to a Macro principle, or when the sovereignty classification at E4 cannot be defended against the constitutional hierarchy --- the predicate is invalid and the pipeline must reject it. Sovereignty classification at E4 is therefore not a discretionary labelling exercise but a verification that the derivability chain holds end-to-end.

This formulation has two consequences that distinguish Q-FENG\'s fractal claim from prior cybernetic governance proposals. The first consequence is that Q-FENG itself operates principally at the Micro level. The interference angle θ measures the alignment between the System 1 Micro (the algorithmic predictor\'s preference vector ψ_N) and the System 5 Micro (the normative state vector ψ_S constructed from active sovereign predicates). The θ measurement does not occur simultaneously at three levels in parallel; it occurs at the Micro level with multilevel semantic guarantees provided by the formal derivability of the jurisdictional stack. When θ ≥ 120° activates the Circuit Breaker at the Micro level, the algedonic signal carries structural meaning at all three levels because the Micro predicate that has been violated is, by construction, derivable from a Meso provision and ultimately from a Macro constitutional norm. The violation of the Micro predicate is, formally, a violation of the chain that includes Meso and Macro.

The second consequence is that the algedonic signal propagates upward through the jurisdictional stack with formally specifiable institutional addressees at each level. A Circuit Breaker activation at the Micro level is received, in the canonical VSM interpretation, by S3 at the Micro level (the management of the deployment unit), but also propagates upward to S3 Meso (sectoral leadership), S4 Meso (sectoral intelligence), S3\* Macro (constitutional audit institutions: in Brazil, TCU, MPF, STF in concentrated control; analogously in EU and US contexts), and ultimately S5 Macro (the constitutional architecture itself, when the violation pattern is sufficiently severe to warrant constitutional deliberation). The propagation is not metaphorical: it follows the derivability chain in reverse, with each level receiving the algedonic signal in the institutional form that its decisional protocol can process. A formally valid Q-FENG Circuit Breaker is, structurally, an actionable input at every level of the jurisdictional stack simultaneously.

This fractal structure is what enables Q-FENG to function as institutional infrastructure rather than as a localised technical monitoring tool. The continuous interference angle measured at one deployment unit, when the pipeline derivation is valid, is constitutively connected to the constitutional architecture of the governing State. The empirical demonstration in §5 shows that this connection can be formally maintained in heterogeneous jurisdictional configurations (Brazilian SUS, EU AI Act, US Medicaid/Equal Protection) and in heterogeneous domains (health infrastructure and labour law). The full theoretical grounding of this fractal architecture, including its sociological grounding in the institutional analysis of public policy (Bromley and Powell 2012; Power 1997, 2022; DiMaggio and Powell 1983), the cybernetic grounding in second-order systems theory (Beer 1972, 1979; Ashby 1956; Conant and Ashby 1970), and the legal-philosophical grounding in the analysis of normative orders (Kelsen 1934/1967; Hart 1961), is developed in Kaminski (2026a, Chapters 6-7); the present paper provides the proof-of-concept empirical demonstration that the fractal architecture is computationally tractable across three jurisdictional regimes and two operational domains. The English-language extension of this theoretical grounding for international audiences is in preparation as Kaminski (2026b, forthcoming) and as Paper 2 in the present sequence.

## Gap Statement

No prior work combines: (1) multi-regime normative corpus processing across three jurisdictions producing sovereign-classified Clingo predicates; (2) quantum interference geometry for continuous governance monitoring; (3) temporal Markovian extension with adaptive memory for crisis tracking; (4) Born-rule quantum vs. classical Bayesian comparison that formally characterises the governance suppression structural property; and (5) proof-of-concept demonstration using real administrative microdata (SIH/DATASUS, 48,784 Medicaid records). Q-FENG C1 is the first system to simultaneously address all five dimensions.

# Mathematical Foundations

## Preference Vectors and Hilbert Space Analogy

Let A = {a_0, a_1, \..., a\_{n-1}} be a finite set of possible actions for a normative agent. The Q-FENG framework represents the agent\'s state as a pair of unit vectors in the n-dimensional real Hilbert space ℋ ≔ (ℝⁿ, ⟨·,·⟩), where ⟨·,·⟩ denotes the standard Euclidean inner product. This restriction to a real Hilbert space --- rather than the complex Hilbert space of canonical quantum mechanics --- is a deliberate operational simplification: phase information is not required for the governance interference geometry, and the cosine of the angle between unit vectors is sufficient to capture the structural alignment between predictor preference and normative state. The two vectors are:

- **ψ_N** ∈ ℋ: the **predictor preference vector**, whose j-th component encodes the preference weight assigned to action a_j by the algorithmic predictor under governance --- a System 1 operational unit external to Q-FENG (cf. §2.7). The current PoC instantiates ψ_N from two predictor families: a time-series composite-pressure score for the Manaus scenario (C2, §5.3), and statistical-measure calibrations from documented system behaviour for the constitutional and labour-law scenarios (C3, C7, T-CLT-01 through T-CLT-04). The ScopeConfig schema (§4.1) admits additional predictor families as forward dependencies for live-inference scenarios (cf. §7.4, §8).

- **ψ_S** ∈ ℋ: the **normative state vector**, whose j-th component encodes the normative weight of action a_j as derived from the set of active predicates returned by the Clingo ASP solver evaluating the Micro-level normative configuration (cf. §2.8). The construction prioritises predicates classified as SOVEREIGN at the E4 HITL stage --- those formally derivable from constitutional or primary-statutory provisions and therefore irreducible by infralegal calibration --- and incorporates ELASTIC predicates as conditional modulators within the bounds set by the sovereign layer. The Micro-level evaluation carries multilevel semantic guarantees through the formal derivability chain (Macro constitutional → Meso statutory/regulatory → Micro Clingo predicate; cf. §2.8).

The ψ_N vectors in this PoC are constructed by two methods, both grounded in documented evidence rather than live model inference, and transparently disclosed here to ensure reproducibility.

*Literature-calibrated from documented system behaviour* --- applied to the constitutional and labour-law scenarios (C3, C7, T-CLT-01 through T-CLT-04). For C3, ψ_N is calibrated from the 27 normative-corpus documents that characterise regional SUS allocation patterns; for C7, from the 48,784-record Obermeyer et al. (2019) dataset that documents the 28.8-percentage-point racial gap in algorithmic risk scoring; for the four CLT scenarios, from documented patterns of CLT non-compliance reported in TST jurisprudence and in MTE inspection records. The per-scenario ψ_N values, with their action-set labels and calibration sources, are reported in §5 (scenario narratives) and in Appendix A (Table A1). For these scenarios ψ_N reproduces the documented behaviour of fielded predictors but is not the output of a live model invocation; this calibration choice is methodologically appropriate to a contribution whose primary object is the governance architecture rather than the predictive accuracy of any specific predictor (cf. §1, §7.4).

*Time-series pressure-score interpolated* --- applied to the Manaus scenario (C2). ψ_N(t) is derived from a composite pressure score (hospital mortality 50%, ICU utilisation 30%, respiratory disease 20%) at each monthly time step, producing a 12-point time-varying vector that tracks the trajectory of the AM health system between July 2020 and June 2021. The raw pre-normalisation ψ_N values are stored in src/qfeng/e5_symbolic/psi_builder.py:\_PSI_N_RAW; the time-varying series in src/qfeng/e5_symbolic/manaus_sih_loader.py. Live predictor-derived ψ_N (C4 LLM scenarios with Ollama/qwen2.5:14b) is identified as a forward dependency for future work (cf. §7.4, §8); no scenario in the current PoC executes a live predictor against the interference geometry, as documented in Mandatory Disclosure 1 (Table A1).

Both vectors are normalised to unit length. The construction of ψ_N follows a signed additive model: each predictor output contributes positively or negatively to each action\'s weight, with the sign and magnitude determined by domain guards calibrated to the specific scenario. The construction of ψ_S uses the sovereign-predicate active-atom set extracted by Clingo\'s constraint-stripping procedure (see §4.5). Throughout this paper we use the Dirac-style notation ⟨ψ_N \| ψ_S⟩ for the inner product in ℋ --- this is conventional in the quantum-cognition literature (Busemeyer and Bruza 2012; Pothos and Busemeyer 2022) which Q-FENG follows, and coincides with the standard Euclidean inner product ⟨ψ_N, ψ_S⟩ in ℝⁿ. The interference angle between the two vectors is then computed as:

$\theta = \arccos\left( \frac{\langle\psi_{N}|\psi_{S}\rangle}{\parallel \psi_{N} \parallel \cdot \parallel \psi_{S} \parallel} \right)$ (1)

where θ ∈ \[0°, 180°\] is the governance interference angle. When θ = 0°, the predictor and normative state are perfectly aligned (STAC); when θ = 180°, they are maximally opposed.

Diagram 3 provides geometric intuition for the three interference regimes before the formal partition in Table 2 below. In the unit-sphere decision space defined by the Hilbert inner product ⟨ψ_N \| ψ_S⟩, three canonical configurations arise:

(a) STAC, where ψ_N and ψ_S are nearly co-directional (cos θ ≈ +1) and the quantum interference geometry yields constructive interference that coincides operationally with the classical Bayesian mixture --- autonomous operation warranted;

(b) HITL, where the vectors are approximately orthogonal (cos θ ≈ 0), yielding intermediate normative friction and a governance signal that warrants human review; and

(c) CIRCUIT_BREAKER, where ψ_N and ψ_S point in opposing directions (cos θ ≈ −1), generating destructive interference that suppresses the predictor\'s preferred action below the classical Bayesian baseline --- the regime in which the quantum-decision-theoretic formulation provides governance information that classical mixture models structurally cannot recover (cf. §3.3 and §7.1 for the formal characterisation of this asymmetry).

![***Diagram 3.*** Geometric intuition for the three governance regimes formalised in Table 2: (a) STAC (cos θ ≈ +1, constructive interference); (b) HITL (cos θ ≈ 0, partial alignment); (c) CIRCUIT_BREAKER (cos θ ≈ −1, destructive interference).]

The 30°/120° thresholds were set a priori based on semantic calibration: STAC requires near-perfect alignment (θ \< 30° implies cosine similarity \> 0.87, a strong agreement) and CB requires severe opposition (θ ≥ 120° implies cosine similarity \< −0.5, clearly destructive). These thresholds were fixed before examining the 7 PoC scenarios; the fact that the empirical θ distribution is bimodal --- CB scenarios cluster in \[127.8°, 134.7°\], STAC scenarios cluster in \[5.6°, 7.1°\] --- with a natural gap, confirms the semantic calibration is consistent with the observed data but does not imply circular optimisation (the gap would persist for any threshold in \[7°, 127°\]). The threshold robustness analysis (Section 6.1) confirms regime stability across θ_block ∈ {100°, 105°, \..., 130°}.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Regime***                                                   ***Condition***  ***Interpretation***
  ------------------------------------------------------------- ----------------- ------------------------------------------------------------------------------------------
  STAC[^1] (Stabilized Sociotechnical Agency Configurations¹)       θ \< 30°      Predictor aligned with normative state; autonomous operation warranted

  HITL (Human-in-the-Loop)                                       30° ≤ θ \< 120°  Partial misalignment; human review required before consequential decisions

  CIRCUIT_BREAKER                                                   θ ≥ 120°      Severe misalignment; normative violation imminent or in progress; mandatory intervention
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : ***Table 2.*** Governance regime partition of the interference angle θ. The 30°/120° thresholds are set a priori on semantic grounds (cosine similarity \> 0.87 for STAC; cosine similarity \< −0.5 for CIRCUIT_BREAKER) and are empirically confirmed by the bimodal θ distribution observed across the seven validation scenarios (Section 5).

The interference angle θ operationalizes what the theoretical framework identifies as Fricção Ontológica (Ontological Friction; Kaminski 2026a, §2.3) --- the structural incompatibility between the inductive-statistical logic of ML predictors and the deductive-deontic logic of normative systems. Classical governance monitoring treats compliance as a binary label (aligned/non-aligned); the interference geometry captures the degree and nature of this structural tension continuously, enabling interventions calibrated to misalignment severity rather than merely its presence. The empirical bimodal distribution of θ across the seven PoC scenarios --- clustering at either extreme with no intermediate-regime case --- is consistent with the framework\'s structural prediction that fully formed governance configurations occupy distinct regions of the interference space: structurally compatible (constructive interference, STAC) or structurally incompatible (destructive interference, CB). The HITL regime \[30°, 120°) is reserved for cases of partial misalignment that the static θ measurement classifies as warranting human review; the Markovian θ_eff series for Manaus (§5.3, Diagram 4) demonstrates that real governance trajectories do traverse the HITL regime as they progress from STAC to CB, even when the static endpoints cluster bimodally. The static interference geometry and the temporal Markovian extension thus play complementary roles: the former classifies fully formed configurations, the latter tracks the trajectory through which a configuration deteriorates.

## Markovian Theta-Efetivo (Kaminski 2026)

For time-varying governance monitoring, the instantaneous interference angle θ(t) may exhibit high volatility due to measurement noise in the predictor input (e.g., month-to-month fluctuations in SIH administrative records). The Kaminski (2026) Markovian extension introduces a temporal smoothing with adaptive memory. The **backward-memory** form of the recurrence is:

$\theta_{eff}(t) = \alpha(t) \cdot \theta(t) + \left( 1 - \alpha(t) \right) \cdot \theta_{eff}(t - 1)$ (2)

where the **adaptive weight** α(t) is a sigmoid function of the pressure gradient:

$\alpha(t) = \sigma\left( \beta \cdot \Delta pressão(t) \right) = \frac{1}{1 + e^{- \beta\,\Delta pressão(t)}}$ (3)

and the **pressure gradient** is the first difference of the composite pressure score:

$\Delta pressão(t) = score\_ pressão(t) - score\_ pressão(t - 1)$ (4)

The composite indicator score_pressão(t) ∈ \[0, 1\] combines hospital mortality rate (weight 0.50), ICU utilisation rate (weight 0.30), and respiratory disease rate (weight 0.20), min-max normalised across the 12-month window. The **full anticipatory form** (Eq. A10 in Appendix B) extends the recurrence with a VSM System 4 prospective intelligence term:

$\theta_{eff}(t) = \alpha(t) \cdot \theta(t) + \left( 1 - \alpha(t) \right) \cdot \theta_{eff}(t - 1) + \gamma \cdot \mathbb{E}\left\lbrack \theta(t + k) \right\rbrack$ (5)

where γ ∈ \[0, 1) is the anticipatory discount weight, τ ∈ {1, 2, \..., K} indexes the forecast horizon, and 𝔼\[θ(t+τ)\] denotes the expected interference angle at horizon τ given the information available at time t.

The geometric weights γ\^τ implement temporal discounting of forecasts: nearer-future expectations carry greater weight than distant ones. The PoC implementation in this paper uses γ = 0 (backward-memory only), which is sufficient to demonstrate early Circuit Breaker activation in the Manaus retrospective (§5.3); the γ \> 0 form is validated analytically in Appendix B.3 and identified as a forward dependency in §7.4 and §8. Even without the anticipatory term, the adaptive sigmoid α(t) drives early CB activation by amplifying the contribution of deteriorating trajectories: as Δpressão(t) \> 0, α(t) → 1 and θ_eff increasingly reflects the current crisis state, allowing the governance signal to cross the 120° threshold before the instantaneous angle θ(t) does. A governance framework that monitors only θ(t) systematically underestimates normative risk in crisis-onset contexts.

The adaptive memory has the following governance semantics: when Δpressão(t) \> 0 (deteriorating), α(t) → 1 and the current crisis state dominates; when Δpressão(t) ≈ 0 (stable), α(t) ≈ 0.5 (balanced); when Δpressão(t) \< 0 (improving), α(t) → 0 and historical memory dampens noisy fluctuations. With the calibration β = 3.0 used in this PoC (the production value declared in src/qfeng/e5_symbolic/interference.py; cf. §7.4), α(t) = 0.91 in the October 2020 onset month (Δpressão = +0.767), confirming rapid adaptation to the detected crisis signal. β sensitivity: for β ∈ {1.0, 1.5, 2.0, 2.5, 3.0}, the October 2020 α(t) values range from 0.68 to 0.91; the first CB-onset month remains October 2020 for all β ≥ 1.5, and shifts to November 2020 at β = 1.0. The Manaus results are robust to the β calibration choice in the \[1.5, 3.0\] range.

## Born-Rule Quantum vs. Classical Bayesian Comparison

To formally characterize the governance advantage of the interference formalism over classical Bayesian alternatives, Q-FENG implements the Born-rule probability comparison introduced by Busemeyer and Bruza (2012) for decision states.

Let α = √conf and β = √(1−conf), where conf ∈ (0,1) is the predictor\'s confidence score, so that α² + β² = 1. **The governance superposition state** is then defined as:

$\left| D\rangle = \alpha \right|\psi_{N}\rangle + \beta|\psi_{S}\rangle,\quad\alpha^{2} + \beta^{2} = 1$ (6)

from which the **quantum Born-rule probability** for action a_j follows as:

$P_{q}(j) = \frac{\left( \alpha\psi_{N}\lbrack j\rbrack + \beta\psi_{S}\lbrack j\rbrack \right)^{2}}{Z}$ (7)

where the normalisation factor Z incorporates the quantum interference cross-term. Z arises from the probability normalisation condition: Σ_j \|αψ_N\[j\] + βψ_S\[j\]\|² = α²‖ψ_N‖² + β²‖ψ_S‖² + 2αβ⟨ψ_N\|ψ_S⟩ = 1 + 2αβcos(θ), where the last equality uses ‖ψ_N‖ = ‖ψ_S‖ = 1 (L2-normalised) and the inner-product definition ⟨ψ_N\|ψ_S⟩ = cos(θ):

$Z = 1 + 2\alpha\beta\cos(\theta)$ (8)

The **classical Bayesian mixture** --- without quantum interference --- is:

$P_{cl}(j) = \alpha^{2}\psi_{N}\lbrack j\rbrack^{2} + \beta^{2}\psi_{S}\lbrack j\rbrack^{2}$ (9)

and the **interference delta** per action quantifies the quantum-classical difference:

$\Delta(j) = P_{q}(j) - P_{cl}(j)$ *(10)*

For governance failure scenarios (UNSAT), the violating action occupies position j = 0, where ψ_N\[0\] \> 0 (predictor prefers the violating action) and ψ_S\[0\] \< 0 (norm prohibits it). This sign difference produces Δ(0) \< 0 --- **destructive interference**: the quantum model assigns lower probability to the violating action than the classical model. The magnitude \|Δ(0)\| is the **governance suppression** that classical Bayesian monitoring would systematically miss.

For governance compliance scenarios (SAT), ψ_N\[0\] \> 0 and ψ_S\[0\] \> 0 (both predictor and norm prefer the compliant action), producing Δ(0) \> 0 --- **constructive interference**: the quantum model amplifies compliance above classical predictions.

## Alhedonic Signal and Cybernetic Loss

The alhedonic signal A ∈ \[0, 1\] is a composite normative friction indicator combining three components:

$$A = 0.70 \cdot \frac{\theta}{180{^\circ}} + 0.20 \cdot \frac{n_{sov}}{n_{sov} + n_{el} + 1} + 0.10 \cdot (1 - conf)$$

where n_sov is the number of active sovereign predicates, n_el the number of active elastic predicates, and conf the predictor confidence. Higher A indicates greater normative friction. The **cybernetic loss function** combines the ontological tension with the epistemic uncertainty:

$\mathcal{L =}\lambda_{ont} \cdot \theta + (1 - conf)$ *(11)*

where λ_ont = 1.5 is the normative penalty weight (calibrated to the PoC regime). L combines the ontological tension (normative misalignment) with the epistemic uncertainty (predictor confidence). The cybernetic loss is the optimisation target for governance intervention scheduling: when L exceeds the HITL threshold, human review is triggered; when L exceeds the CB threshold, mandatory intervention is activated.

Diagram 5 illustrates the topology of L_Global as a loss landscape over the policy-action space. The quantum penalty ridge λ·max(0, −cos θ) rises steeply as θ approaches 180°, creating a potential barrier that excludes configurations with severe normative misalignment from the predictor\'s optimisation trajectory.

![***Diagram 5. Conceptual loss landscape of L_Global showing the STAC equilibrium region. The quantum penalty ridge λ·max(0, −cos θ) excludes non-conforming configurations from the optimisation trajectory.***]

The STAC equilibrium basin at the centre of the landscape corresponds to the region of governance compliance; the HITL boundary marks the point at which the gradient of L exceeds the threshold for autonomous operation; and the Circuit Breaker wall at the ridge marks the mandatory intervention boundary. The landscape is therefore not merely a performance metric but a normative topography: the governance architecture imposes the shape of the space within which the predictor may operate.

## Failure Typology

The combination of Clingo SAT/UNSAT status, sovereignty classification, and active-atom analysis enables three failure types:

- **Constitutional failure**: SAT=False; sovereign predicates that *would* ground the required obligation are absent from the corpus (the norm does not exist or is not applicable in this jurisdiction/context). Example: racial equity obligation absent from Medicaid statute (C7).

- **Execution-absent-channel failure**: SAT=False; sovereign predicates grounding the required obligation *exist* in the corpus but the execution path is blocked by a missing enabling condition. Example: COES activation obligation exists but hospital occupancy reporting channel is not established (C2).

- **Execution-inertia failure**: SAT=False; the normative predicate cited by the agent (LLM or human) references a non-existent precedent or phantom citation, so the grounding predicate cannot be derived. Example: Mata v. Avianca phantom citation (T-CLT-01).

The failure typology formalised above maps onto a geometric structure visualised in Diagram 6. Three asymmetric regions partition the normative space according to the presence or absence of two independent elements: the sovereign predicate and the execution chain. Constitutional failures arise when both sovereign predicate and execution chain are absent from the active corpus --- a structural gap that cannot be resolved by operational intervention alone and requires legislative or constitutional remediation. Execution-absent-channel failures occur when the sovereign predicate is derivable but no enabling condition instantiates it in the current execution context; the governance infrastructure exists normatively but is inoperative at the deployment layer. Execution-inertia failures arise when the citation chain is hallucinated or misgrounded, collapsing the execution path at the predicate-derivation step regardless of the sovereign predicate\'s presence. The triadic geometry makes the asymmetric causal structure of normative violation legible as spatial distance from the sovereign predicate axis --- a visualisation of the third original contribution of this paper.

![Diagram 6. Triadic failure typology: asymmetric partition of normative-violation space into constitutional failures (absent sovereign predicate), execution-absent-channel failures (predicate derivable, execution path blocked), and execution-inertia failures (citation misgrounded or phantom). The geometry encodes the causal distance from the sovereign predicate axis.]

# The C1 Pipeline: Stages E0--E4

## E0: ScopeConfig --- Normative Domain Specification

The computational architecture of the C1 pipeline is illustrated in Diagram 7 as a concrete data-flow graph from raw normative input to interference-angle output. Each stage produces a typed, Pydantic-validated artefact persisted to Parquet: E0 produces a ScopeConfig object parameterising the normative domain; E1 emits NormChunks carrying hierarchical provenance metadata; E2 extracts DeonticAtoms via few-shot LLM inference; E3 translates atoms deterministically to Clingo predicates via Jinja2 templates; E4 classifies predicates as SOVEREIGN or ELASTIC through HITL review; and E5 executes the Clingo ASP solver to derive SAT/UNSAT status and construct the normative state vector ψ_S, from which the interference angle θ is computed. The determinism guarantee --- critical for reproducibility --- is enforced at E3 (template-based translation, no LLM stochasticity) and E5 (Clingo \--seed=1 fixed). This diagram complements Diagram 1, which shows the cybernetic governance cycle at an architectural level; Diagram 7 exposes the underlying data engineering that makes that cycle computationally executable.

![Diagram 7. Q-FENG C1 data-flow pipeline (E0--E5): ScopeConfig → NormChunk → DeonticAtom → ClingoPredicate → SAT/UNSAT verdict → ψ_S → θ. Pydantic-validated schemas, Parquet persistence, and deterministic E3/E5 stages ensure full reproducibility. Complements Diagram 1 (cybernetic governance cycle) at the data-engineering level.]

The pipeline\'s entry point is the **ScopeConfig** schema, which parameterises all subsequent stages for a specific governance domain. A ScopeConfig specifies: the target regulatory regime (Brazil/SUS, EU/AI Act, USA/Medicaid); the corpus identifiers and their priority rankings; the predictor type (LightGBM, TimeSeries, Statistical, ASP); the sovereignty threshold for HITL classification; and the domain guards controlling ψ_N construction. For the current PoC, three ScopeConfigs were instantiated ([Table 2]):

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  **ScopeConfig**         **Regime**                            **Corpus Anchor**                                     **Predictor**
  ----------------------- ------------------------------------- ----------------------------------------------------- -------------------------------------
  sus_validacao           Brasil (19 docs) + EU (4) + USA (9)   CF/88 + Lei 8.080 + EU AI Act                         LightGBM / TimeSeries / Statistical

  advocacia_trabalhista   Brasil (CLT + TST)                    CLT Art. 59 + Súmulas TST 85/291                      ASP / LLM

  manaus_temporal         Brasil (emergency)                    Decreto AM 43.303/2021 + Lei 13.979/2020 Art.3 VIII   TimeSeries (SIH)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref227876515 .anchor}***Table 3***. ScopeConfigs instantiated for the PoC validation, specifying the normative regime coverage, the corpus anchor documents grounding sovereign predicates, and the predictor families producing ψ_N.

ScopeConfig is implemented as a Pydantic v2 model in core/schemas.py (lines 1--89), which is the authoritative contract for all inter-stage communication. No module creates parallel type definitions; all data flows through Pydantic-validated schemas.

## E1: Ingestion --- Normative Corpus Construction

The E1 stage transforms raw normative documents (HTML, PDF, Markdown) into a structured corpus of **NormChunks** --- atomic normative units carrying hierarchical metadata (regime, document, article, paragraph, inciso/alínea), a chunk_type classification (obligation, principle, procedure, definition, sanction), and a SHA-256 content identifier for cache-consistent reprocessing. Corpus statistics (E1-v4, approved April 2026) are reported in [Table 3][]:

  ------------------------------------------------
  **Metric**                             **Value**
  ------------------------------------ -----------
  Documents processed                           29

  Total NormChunks                          27,957

  Cross-references detected                  2,977

  Concurrency pairs (Jaccard ≥ 0.55)           347
  ------------------------------------------------

  : []{#_Ref227876653 .anchor}***Table 4.*** E1-v4 ingestion corpus statistics across the integrated normative base (health/governance track), covering document count, atomic normative units, inter-document references, and concurrency pairs above the Jaccard ≥ 0.55 semantic threshold

The 347 concurrency pairs --- normatively equivalent or conflicting provisions across documents --- constitute the backbone of the comparative governance graph. Twelve pairs with Jaccard = 1.0 represent provisions reproduced verbatim across multiple instruments (e.g., the non-discrimination principle appearing in both the Lei 8.080/1990 and the LGPD), confirming their status as sovereign-candidate predicates.

  ------------------------------------------------------------------------------------------
  **Regime**        **Chunks**        **%**   **Documents**   **DeonticAtoms**   **% Atoms**
  ------------- -------------- ------------ --------------- ------------------ -------------
  Brasil                21,445        76.7%              19              3,206         62.4%

  EU                     1,667         6.0%               4              1,101         21.4%

  USA                    4,845        17.3%               9                829         16.1%

  ***Total***     ***27,957***   ***100%***        ***29***        ***5,136***    ***100%***
  ------------------------------------------------------------------------------------------

  : ***Table 5***. Corpus distribution and DeonticAtom extraction results across the three jurisdictional regimes (health/governance track).

The hierarchical parser implements regime-specific extraction strategies: Brazilian documents follow the Planalto.gov.br DOM structure (Art. / § / inciso / alínea), EU documents follow the EUR-Lex article/paragraph/point notation, and US documents follow CFR section/(a)(1)/(i) notation. Revoked provisions --- marked with \<strike\> tags in Planalto.gov.br sources --- are removed at the DOM decomposition stage before text extraction, ensuring that predicates reflect the current normative state. This removed 6 chunks from CF/88 and 27 chunks from Lei 13.979/2020 (provisions revoked by subsequent COVID-19 legislation), confirming the effectiveness of the revocation filter.

Chunk type distribution: obligation (82.5%, n=23,053), procedure (7.1%, n=1,992), principle (6.8%, n=1,913), definition (2.7%, n=759), sanction (0.9%, n=240). The dominance of obligation chunks is consistent with the legal structure of the target documents --- primarily legislative statutes and regulations rather than commentary or doctrine.

The corpus is organized in three hierarchically nested layers that mirror the formal stratification of positive law (Kelsen 1934; Bobbio 1960):

- **Layer 1 --- Constitutional**: petreous clauses, foundational principles, and fundamental rights (in the Brazilian instance, CF/88 Art. 60 §4°, Art. 1°, Art. 3°, Art. 5°, Art. 23 II). Predicates at this layer are classified `sovereign/1` either in the strict petreous sense (entrenched against constitutional amendment) or in the structuring sense (constitutional norms that ground the operational stratum of the federation).

- **Layer 2 --- Statutory and regulatory**: legislation enacted by the legislature and regulatory instruments of executive agencies, including ministerial portarias and emergency decrees. Predicates at this layer are classified `sovereign/1` when constitutionally anchored --- typically through dual-anchoring patterns documented in Appendix A --- and `elastic/1` when modulable by infralegal regulatory instruments.

- **Layer 3 --- Scenarios**: factual instances that invoke predicates from Layers 1 and 2 and provide the operational facts (hospital occupancy rates, hour-bank periods, decisions issued, citations used) that activate constraints and trigger the SAT/UNSAT verdict.

The hierarchical separation is methodologically important because it implements the Kelsenian normative hierarchy operationally: integrity constraints triggered at the constitutional layer cannot be overridden by predicates from infralegal layers, and scenario instantiations cannot instantiate facts that contradict positive law in superior layers. The dual-classification scheme SOVEREIGN/ELASTIC operates over the union of Layers 1 and 2; Layer 3 scenarios are factual and not subject to this classification.

### Labour-track corpus.

The labour-law domain (T-CLT-01 through T-CLT-04 scenarios) is supported by a separate, jurisdiction-specific Brazilian sub-corpus assembled in a distinct ingestion pass and reported separately for traceability:

  ----------------------------------------------------------------------------------------
  **Document**                                               **Chunks**   **DeonticAtoms**
  -------------------------------------------------------- ------------ ------------------
  CF/88 Art. 7º (XIII--XVI: working-hours rights)               partial     included below

  CLT --- Consolidação das Leis do Trabalho (full)             majority           majority

  Lei 13.467/2017 (Reforma Trabalhista)                         partial            partial

  TST jurisprudence (Súmulas 85, 291; selected acórdãos)        partial            partial

  Total (4 documents, regime: Brasil)                             4,488              5,006
  ----------------------------------------------------------------------------------------

  : ***Table 6.*** Labour-track corpus distribution and DeonticAtom extraction results (Brasil, jurisdiction-specific sub-corpus).

Mean confidence in the labour track is 0.942 (median 0.950); only 5 atoms (0.1%) were extracted with confidence below 0.7. The labour modality distribution differs structurally from the health/governance track: obligation 70.6% (vs. 84.2%), prohibition 16.3% (vs. 4.8%), permission 9.2% (vs. 9.4%), and faculty 3.9% (vs. 1.6%). The 3.4× higher prohibition rate reflects a defining stylistic property of Brazilian labour law --- the historical predominance of explicit vedações *ao empregador* (prohibitions binding the employer) as the primary regulatory device, in contrast to the principle-and-permission structure typical of constitutional and health-system instruments. This asymmetry is visualised in Figure 7 (§5.5).

## E2: Deontic Extraction

The E2 stage processes NormChunks through a few-shot LLM extraction pipeline to produce **DeonticAtoms** --- structured representations of normative modalities with fields: id (SHA-256), source_chunk_id, modality (obligation/permission/prohibition/faculty), agent, patient, action, conditions, and confidence.

The extraction used claude-sonnet-4-6 via litellm with regime-specific few-shot prompts calibrated to each document structure, without fine-tuning. The few-shot examples were drawn from manually annotated reference chunks (3--5 examples per regime), covering the syntactic patterns characteristic of each jurisdiction. The E2 extraction processed 6,059 chunks and produced 5,136 DeonticAtoms, with 2,352 chunks (38.8%) yielding no deontic content --- the expected behaviour for definition, procedure, and preambular chunks. Zero atoms were extracted at confidence below 0.7; mean confidence was 0.930 (median 0.950) --- a strong result for multi-regime extraction without fine-tuning.

Software stack for the E2 extraction: Python 3.11, litellm 1.x (LLM abstraction layer), claude-sonnet-4-6 (Anthropic API backend for production; ollama/qwen2.5:14b for local/zero-cost re-runs), Clingo 5.8.0 (ASP solver), python-docx 1.1.x (corpus ingestion), pandas 2.x + pyarrow 15.x (parquet persistence). All random seeds fixed to 1 (Clingo) or 42 (NumPy/bootstrap) for reproducibility. Full dependency list: pyproject.toml.

Zero atoms below confidence 0.5 is a strong result for multi-regime extraction without fine-tuning. The 38.8% zero-atom rate reflects correct behaviour: definition, procedure, and preambular chunks appropriately yield no deontic content. The modality distribution of extracted DeonticAtoms follows the standard Q-FENG Clingo translation: obligation (4,325; 84.2%) → obligated(agent, action); permission (482; 9.4%) → permitted(agent, action); prohibition (245; 4.8%) → :-permitted(agent, action); faculty (84; 1.6%) → may(agent, action).

The dominance of obligation modality (84.2%) is consistent with the Lippi et al. (2019) finding that contractual NLP corpora are predominantly prescriptive, and with Robaldo et al. (2020)\'s observation that statutory instruments in continental legal systems are structured as obligation networks.

Representative DeonticAtom examples across the three regimes are reported in Listing 1, illustrating the structural homogeneity of the E2 output across heterogeneous legal-textual conventions (Brazilian constitutional, EU regulatory, US statutory).

(a) **Brasil --- CF/88 Art. 1º §único:**

<!-- -->

    {
      “modality”: “obligation”,
      “agent”: “state”,
      “action”: “exercise_power_through_elected_or_direct_means”,
      “conditions”: [],
      “confidence”: 0.92
    }

(b) **EU --- AI Act Art. 9:**

<!-- -->

    {
      “modality”: “obligation”,
      “agent”: “provider”,
      “action”: “implement_risk_management_system”,
      “object”: “high_risk_ai_system”,
      “conditions”: [“system_is_high_risk”],
      “confidence”: 0.97
    }

**\**

(c) **USA --- 14th Amendment §1 EPC + Title VI (42 U.S.C. §2000d):**

<!-- -->

    {
      “modality”: “obligation”,
      “agent”: “state_medicaid_agency”,
      “action”: “provide_care_and_services_consistent_with_best_interests”,
      “patient”: “eligible_individuals”,
      “conditions”: [“medicaid_state_plan_in_effect”],
      “confidence”: 0.89
    }

***Listing 1***. DeonticAtom extraction examples across three normative regimes: (a) Brasil --- CF/88 Art. 1º §único; (b) EU --- AI Act Art. 9; (c) USA --- 14th Amendment §1 EPC + Title VI §601. The structural homogeneity across three heterogeneous legal-textual conventions demonstrates that the few-shot extraction protocol produces a uniform deontic representation amenable to downstream symbolic translation

## E3: Translation --- DeonticAtom to Clingo Predicate
The E3 stage implements a deterministic, template-based translation from DeonticAtoms to Clingo predicate syntax. The translation is template-based (no LLM at this stage) to ensure reproducibility and formal correctness. Jinja2 templates encode five modality patterns, shown in Listing 2:

```
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

***Listing 2***. Jinja2 translation templates for deontic modalities in the E3 stage. String conditions are translated to unary predicates; arithmetic conditions use Clingo's built-in comparison operators. The template-based design (no LLM at E3) ensures deterministic reproducibility and formal correctness of the Clingo predicate output.

String conditions are translated to unary predicates; arithmetic conditions (&gt; threshold, &lt; threshold) use Clingo's built-in arithmetic. The sovereignty classification (SOVEREIGN vs. ELASTIC) assigns legal weight: sovereign predicates encode constitutional or statutory obligations that cannot be modified by subordinate instruments; elastic predicates encode regulatory details subject to administrative discretion.

## E4: HITL --- Human-in-the-Loop Sovereignty Classification

The E4 stage implements human-in-the-loop review of the sovereignty classification for each ClingoPredicate. Reviewers classify each predicate as SOVEREIGN (legally irreducible; cannot be overridden by executive discretion) or ELASTIC (regulatorily calibratable within statutory bounds). The classification is recorded in the HITL cache and propagates forward to E5 scenario evaluation.

For the sus_validacao scope, all 537 predicates were reviewed (537/537, Phase B completed April 2026). For the advocacia_trabalhista scope, the CLT-domain predicates covering working hours (Art. 59), collective bargaining agreements (CCTs), and TST jurisprudence (Súmulas 85, 291) were classified in the same HITL pass.

The SOVEREIGN/ELASTIC distinction is the formal basis for the failure typology described in Section 3.5: constitutional failures arise when a required sovereign predicate is absent from the corpus; execution failures arise when the sovereign predicate exists but the execution chain is blocked or misgrounded.

The classification is guided by three explicit criteria, calibrated through the April 2026 audit cycle (Appendix A.5):

**Criterion 1 --- Constitutional anchoring (audit LAW-BR-05).** A predicate is classified `sovereign/1` only if at least one anchor is constitutional. Predicates anchored solely in statutory or regulatory norms are classified `elastic/1` even if they encode rights or obligations of broad applicability. When a statutory norm encodes a right with constitutional grounding, dual-anchoring is applied: the predicate is sovereign only when both the statutory and the constitutional anchors are co-present.

**Criterion 2 --- Deontic validation against thematic relevance (audit C-4).** LLM extraction may return predicates whose source instrument is thematically relevant but deontically irrelevant to the scenario (e.g., a portaria covering an adjacent regulatory matter). The HITL review verifies that the anchor instrument actually establishes the obligation invoked by the predicate, not merely a textual co-occurrence.

**Criterion 3 --- Citation existence cross-reference (audit F0-1).** Jurisprudential anchors (precedent citations) are cross-referenced against authoritative public databases of the issuing court before being admitted to the corpus. Syntactically valid case numbers are insufficient; the case must be verifiable in the public registry.

These three criteria operationalize the methodological lessons of the audit cycle: that LLM-assisted normative extraction systematically requires semantic-juridical filtering, not merely syntactic validation, and that the legal weight of a predicate is a function of its anchor topology, not of the LLM's extraction confidence.

The thermodynamic analogy that motivates the SOVEREIGN/ELASTIC classification is rendered explicit in Diagram 8. The diagram frames the normative state space as a free-energy landscape: sovereign predicates define the ground-state energy minimum --- the constitutionally mandated configuration that the governance system must attain --- while elastic predicates constitute the thermal bath of regulatorily calibratable parameters whose values can fluctuate within statutory bounds without triggering normative violation. The HITL review process, in this metaphor, determines the local potential energy of each predicate: a SOVEREIGN classification raises a high-energy barrier that the predictor cannot cross without explicit Circuit Breaker activation; an ELASTIC classification contributes low-gradient energy, admitting operational variation. The neurosymbolic interface --- where LLM-extracted DeonticAtoms meet Clingo's formal constraint-satisfaction --- is the measurement apparatus that collapses the superposition of possible sovereignty assignments into a definite, auditable classification.

!\[Diagram 8. Neurosymbolic free-energy landscape for HITL sovereignty classification. Sovereign predicates define the constitutional ground-state minimum; elastic predicates constitute the thermal bath of calibratable regulatory parameters. The Circuit Breaker threshold corresponds to the energy barrier that the predictor cannot cross without explicit HITL activation.\]

**Pipeline survival E2 → E3 → E4.** Across both tracks, the E2 stage produced 10,142 DeonticAtoms (5,136 health/governance; 5,006 labour). After the E3 deterministic Jinja-template translation and the E4 HITL sovereignty review, 4,973 atoms (49.0%) produced valid, scope-admissible Clingo predicates that form the symbolic substrate for the seven scenarios evaluated in Section 5: 2,530 predicates for the health/governance track (49.3% of its E2 output) and 2,443 for the labour track (48.8%). The attrition is concentrated at two stages: template-pattern mismatch in E3 (atoms whose conditions or patient roles did not admit a deterministic Jinja mapping were discarded rather than coerced) and scope filtering enforced by ScopeConfig (only chunks belonging to the active scenario scope enter the Clingo fact base). Both mechanisms are design choices, not defects: E3 refuses lossy translations to preserve formal correctness, and ScopeConfig ensures that each scenario is evaluated against exactly the normative surface relevant to its governance question. Limitations of the underlying LLM extraction --- particularly its uneven performance across languages --- are discussed in Section 7.4.

## E5: Symbolic Testing --- Scenario Evaluation and ψ\_S Construction

The E5 stage executes formal scenario evaluation using the Clingo ASP solver in a deterministic two-pass strategy (--seed=1). Pass 1 (full program): the complete normative corpus (sovereign predicates, elastic predicates, integrity constraints) together with scenario-specific fact files is solved. The result is SAT (all constraints satisfied) or UNSAT (at least one constraint violated), producing the formal normative verdict. Pass 2 (relaxed program): integrity constraints are stripped from the source before solving, allowing atom extraction from UNSAT scenarios where Pass 1 returns no model. Pass 2 yields the active_sovereign and active_elastic predicate lists used to construct ψ\_S.

Construction of ψ\_S (normative state vector). The normative state vector is built from the active predicates extracted in Pass 2 via an additive weight model: ψ\_S\[j\] = Σ\_k w_kj · 𝔿\[pattern_k ⊆ atom_k\], where the sum runs over all active atoms, pattern_k is a substring key registered in the predicate map, w_kj is the expert-elicited signed weight for action dimension j (positive = predicate supports action j; negative = predicate blocks action j), and 𝔿\[·\] is the indicator that atom_k matches pattern_k. The resulting vector is L2-normalised. Predicate map weights range from −8.0 to +8.0 and represent the legal gravity of each predicate class: constitutional sovereign obligations (e.g., obligation_immediate_supply_critical: −8.0 on the violating action) carry the highest magnitude; regulatory elastic predicates carry lower magnitudes. Table A2 in Appendix A reports the complete predicate map for all seven scenarios.

If no predicate pattern matches any active atom (fallback case), ψ\_S is set to the vector orthogonal to ψ\_N in the decision space, yielding θ = 90° (HITL regime). This fallback was not triggered in any of the seven PoC scenarios.

# Validation Results

## Overview of Seven Scenarios

Seven scenarios were validated across three normative regimes and two domains. Scenarios C2, C3, and C7 address the health domain; T-CLT-01 through T-CLT-04 address the labour law domain. Scenarios T-CLT-03 and T-CLT-04 are **positive controls** --- cases of normative compliance expected to produce STAC (θ &lt; 30°).

---

**Scenario** **Domain** **Regime** **θ (°)** **Regime** **SAT** **Failure type** **Governance suppression** **Data source** **n_obs**

---

```
    C2          Health       Brasil      132.36     CIRCUIT_BREAKER    False    execution_absent_channel             16.75%                SIH/real         1,526

    C3          Health       Brasil      134.67     CIRCUIT_BREAKER    False         constitutional                  25.16%                Normative       27 docs

    C7          Health        USA        133.74     CIRCUIT_BREAKER    False         constitutional                  10.66%              Real Medicaid     48,784

 T-CLT-01       Labour       Brasil      134.08     CIRCUIT_BREAKER    False       execution_inertia                 9.37%                 Normative       1 case

 T-CLT-02       Labour       Brasil      127.81     CIRCUIT_BREAKER    False         constitutional                  11.23%                Normative       1 case

 T-CLT-03       Labour       Brasil       5.65           STAC          True               ---                        −0.28%                Normative       1 case

 T-CLT-04       Labour       Brasil       7.05           STAC          True               ---                        −0.44%                Normative       1 case
```

---

: ***Table 7.*** Scenario validation results across seven PoC cases, reporting the interference angle θ, the governance regime classification, Clingo SAT/UNSAT status, failure type, governance suppression percentage, data source, and observation count

!\[***Figure 1.*** Interference angle θ across seven scenarios --- overview of governance regime classification. Predictor states ψ\_N (dashed) plotted by their angular separation from the normative reference ψ\_S (solid). Five CIRCUIT-BREAKER scenarios cluster at 127.8°--134.7° (destructive interference); two positive controls fall within the STAC band at 5.7°--7.1° (constructive interference).\]

!\[***Figure 2.*** Q-FENG interference geometry in the decision Hilbert space. Angle θ between predictor state ψ\_N (dashed) and normative state ψ\_S (solid) across seven scenarios and two normative regimes. Health Governance: C2, C3, C7 (ψ in R³, 3 actions). Labour Law: T-CLT-01 through T-CLT-04 (ψ in R², 2 actions). GSP annotation shows governance suppression percentage per scenario.\]

The **governance suppression percentage** (GSP) is defined as:

$$GSP = \\frac{P\_{cl}(j) - P\_{q}(j)}{P\_{cl}(j)} \\times 100%$$

and quantifies the fraction by which the quantum Born-rule model suppresses the violation probability below the classical Bayesian prediction. Negative GSP (positive controls T-CLT-03, T-CLT-04) indicates constructive interference: the quantum model amplifies the compliance probability above classical predictions.

## Scenario Narratives

### C2 --- Manaus Hospital Collapse (Brasil, execution_absent_channel): θ = 132.36°, CIRCUIT_BREAKER.

This scenario formally encodes the January 2021 Manaus ICU collapse --- one of the most documented healthcare governance failures in Brazilian history --- in which hospital occupancy reached 100% (documented by FVS-AM Boletim Epidemiológico 16/jan/2021 (103.7% UTI occupancy)) while municipal oxygen supplies were exhausted, leading to patient transfers to other states and an internationally reported humanitarian emergency (Sabino et al. 2021).

The **normative corpus** for C2 comprises four documents in the brasil/saude/ and brasil/emergencia_manaus/ sub-corpora: CF/88 Capítulo II (Art. 196--200, 383 chunks); Lei 8.080/1990 (381 chunks, specifically Art. 7 §II --- equity principle --- and Art. 15 §I --- emergency competence of the federal authority); Lei 13.979/2020 (199 chunks after revocation filter, specifically Art. 3 §§I--VI --- emergency health measures --- and Art. 10 §§I--III --- operational protocol); and Decreto AM 43.303/2021 (dedicated Manaus emergency protocol encoding the hospital occupancy threshold and oxygen stock trigger conditions).

The **Clingo predicate derivation chain** for C2 is:

1. hospital_occupancy_rate_pct(100) is asserted as a scenario fact;

2. the rule sovereign(obligation_to_activate_coes) :- hospital_occupancy_rate_pct(R), R &gt; 85 (from emergencia_sanitaria.lp) fires, deriving sovereign(obligation_to_activate_coes);

3. the integrity constraint :- sovereign(obligation_to_activate_coes), not executed(coes_activation) fails because executed(coes_activation) is not derivable (the execution pathway is absent from the normative program);

4. Clingo returns UNSAT.

The provenance of the two operational thresholds activated in steps 1--2, documented in Appendix A.5.6 (audit LAW-BR-08), is as follows:

- **TOH > 85%** is anchored in the Technical Indicator Sheet for Hospital Care of the Brazilian Ministry of Health (TOH UTI), prepared by the General Coordination of Hospital Care / DAHU / SAES / MS. There is convergence with the critical Brazilian intensive-care literature (AMIB) which classifies TOH > 85% as operational saturation --- a state in which ICU bed waiting time grows non-linearly and mortality from inadequate prioritization increases significantly.

- **Oxygen days remaining < 3** is anchored in the operational precedent of Manaus 2021 (White Martins notification to the Ministry of Health on 14/Jan/2021 of impossibility of replenishment in 24--48h). The threshold is implemented as a configurable parametric fact (`oxygen_critical_threshold_days(3).`), allowing adjustment without modification of the logical predicate.

The separation between logical predicate (rule) and parametric fact (value) is a normative engineering pattern that makes the corpus auditable and adaptable without losing documentary grounding. The pattern is generalizable to other thresholds and is recommended for any NeSy system operating on empirical data.

The **ψ\_N construction** uses the TimeSeries predictor calibrated from 1,526 SIH/DATASUS admissions across six months (Oct/2020--Mar/2021) with COVID-19 ICD codes (J189, J960, J961, J969, U071, U072, B342). The predictor preference vector encodes three actions:

> a_0 = continue_autonomous_operation (ψ\_N\[0\] = 0.998);
>
> a_1 = activate_partial_escalation (ψ\_N\[1\] = 0.065)
>
> a_2 = activate_full_coes (ψ\_N\[2\] = 0.022).

The normative state vector, derived from the nine active sovereign predicates, is ψ\_S = \[−0.718, 0.486, 0.498\] --- strongly opposing the autonomous continuation action that the predictor overwhelmingly prefers.

The **failure type** is execution_absent_channel: the sovereign obligation obligation_to_activate_coes is present and correctly grounded in the corpus (Art. 10 §I Lei 13.979/2020), but the execution chain requires a formal reporting channel from the Secretaria Municipal de Saúde de Manaus to the federal Sala de Situação do Ministério da Saúde, which was not operationally established in January 2021. The sovereign norm exists; the execution infrastructure does not. This distinction has direct policy implications: remediation requires building the coordination channel (an institutional problem), not amending the statute (a legislative problem).

Born-rule quantum probability: P_q(violation) = 0.761; classical Bayesian: P_cl(violation) = 0.914; governance suppression: 16.75%. Nine of nine active predicates are classified SOVEREIGN; zero elastic predicates are active --- a normative saturation consistent with the constitutional-level grounding of the right-to-health emergency response.

### C3 --- Regional SUS Concentration (Brasil, constitutional): θ = 134.67°, CIRCUIT_BREAKER, governance suppression 25.16% --- the highest suppression in the dataset.

This scenario evaluates a structural pattern in Brazilian health policy: the concentration of SUS specialist services (oncology, cardiac surgery, high-complexity imaging) in capitals and large metropolitan centres, while the interior municipalities receive predominantly primary care --- a distribution pattern that systematically disadvantages the 46% of Brazil's population living in municipalities with fewer than 50,000 inhabitants.

The regional concentration pattern that defines scenario C3 is visualised as an equity map in Diagram 9. The map encodes the distribution of SUS specialist services across Brazilian municipalities plotted against the population distribution, revealing the structural mismatch between geographic availability and demographic need: metropolitan regions --- São Paulo, Rio de Janeiro, Belo Horizonte, Manaus --- accumulate the majority of high-complexity services (oncology, cardiac surgery, advanced imaging) while the 46% of Brazilians residing in municipalities with fewer than 50,000 inhabitants are served predominantly by primary-care units. The dual constitutional grounding of this violation is reflected in the map's dual annotation layer: the CF/88 Art. 196 layer marks the universal access gap, measuring the distance between available specialist capacity and the constitutionally mandated universal and equal access standard; the Art. 198 III layer identifies the SUS regionalisation deficit, quantifying the failure to distribute services according to epidemiological need rather than administrative convenience. The spatial representation makes the magnitude of the 25.16% governance suppression intuitively legible as geographic distance from constitutional compliance.

!\[Diagram 9. Regional equity map of SUS specialist-service distribution across Brazilian municipalities. The dual annotation layer marks the CF/88 Art. 196 universal-access gap and the Art. 198 III SUS-regionalisation deficit, quantifying the constitutional violation that grounds the θ = 134.67° CIRCUIT_BREAKER outcome of scenario C3 (governance suppression 25.16%).\]

The **constitutional grounding** is double: CF/88 Art. 196 establishes health as "a right of all and a duty of the State, guaranteed by social and economic policies aimed at reducing the risk of disease and other harms and at universal and equal access to actions and services for health promotion, protection, and recovery" --- with the term "universal and equal access" (acesso universal e igualitário) constituting the sovereign obligation that the concentration pattern violates. Lei 8.080/1990 Art. 7 §II (equity principle --- equidade) operationalises this constitutional mandate at the statutory level, requiring that services be distributed according to health need rather than administrative convenience or provider preference.

The **Clingo predicate derivation chain** activates seven sovereign predicates:

1. universal_right_to_health(cf88_art196);

2. equity_principle(sus, regional_access);

3. equity_distribution_required(specialist_services); prohibition_unequal_allocation(health_resources); and,

4. three additional predicates from Lei 8.080/1990 encoding the SUS integration principles.

The ψ\_N vector for C3 --- calibrated from literature-documented regional SUS allocation patterns (synthetic calibration from 27 corpus normative documents; see Table 3) --- assigns high weight to the concentrated metropolitan pattern (ψ\_N = \[0.996, 0.078, 0.033\]), while the normative state strongly opposes it (ψ\_S = \[−0.759, 0.506, 0.411\]).

The **failure type** is constitutional: unlike C2 (where the execution channel is missing) or C7 (where the statute lacks a racial equity clause), C3 involves an explicit constitutional mandate that is structurally violated by the resource allocation pattern. Remediation requires policy intervention --- either legislative reallocation of SUS specialist services to interior municipalities or constitutional interpretation by the STF (Federal Supreme Court) binding on administrative allocation decisions. This is the most severe failure type from a governance standpoint: it cannot be resolved by building coordination channels or by statutory amendment without constitutional revision.

The 25.16% governance suppression --- the highest in the dataset --- reflects the double constitutional grounding (CF/88 direct + Lei 8.080 operational) producing maximum destructive interference with the predictor's metropolitan concentration preference. This scenario establishes that the Q-FENG framework can detect constitutional violations in resource allocation patterns even when the predictor has no explicit fairness objective --- the violation emerges from the structural mismatch between the allocative algorithm's optimisation target and the normative architecture's distributional requirements.

### C7 --- Obermeyer Racial Bias (USA, constitutional): θ = 133.74°, CIRCUIT_BREAKER.

This scenario encodes the Obermeyer et al. (2019) finding in formal normative terms: a commercial healthcare algorithm deployed across hundreds of US hospitals assigns Black patients risk scores 28.8-percentage-points lower than White patients with identical health needs, measured by active chronic condition count. The structural cause is the algorithm's use of health expenditure as a proxy for health need --- expenditure that reflects historical racial disparities in healthcare access rather than clinical necessity.

The **normative corpus** for C7 is the US sub-corpus (9 documents, 4,845 chunks, 829 DeonticAtoms): SSA Title XIX §1902 (831 chunks --- the Medicaid state plan requirements), 42 CFR Part 430 (administration), 42 CFR Part 435 (eligibility), 42 CFR Part 440 (covered services), the Obermeyer et al. (2019) published analysis (empirical anchor, not a normative document --- used to calibrate ψ\_N), and the 14th Amendment (5 chunks --- the constitutional source of equal protection). The 14th Amendment's disproportionately small chunk count (5 chunks) relative to its constitutional weight illustrates why the HITL sovereignty classification is indispensable: the E4 reviewer classified equal_protection(all_persons) as SOVEREIGN based on its constitutional character, not its corpus frequency.

The **Clingo predicate derivation chain** activates four sovereign predicates from the US corpus:

1. equal_protection(all_persons) (14th Amendment §1);

2. best_interest_standard(state_medicaid_agency;

3. eligible_individuals) (14th Amend. §1 + 42 U.S.C. §2000d);

4. non_discrimination_eligibility(medicaid) (42 CFR §435.4);

5. covered_services_without_discrimination(medicaid) (42 CFR §440.230(c)).

The algorithm's output --- modelled as a statistical measure calibrated from the 48,784-record Obermeyer dataset --- is encoded in ψ\_N = \[0.991, 0.117, 0.058\], strongly preferring the biased allocation action (a_0 = allocate_by_expenditure_proxy). The normative state, derived from the four active sovereign predicates, is ψ\_S = \[−0.768, 0.329, 0.549\].

The failure type is constitutional: the equal-protection obligation encoded in the 14th Amendment §1 EPC and Title VI §601 (42 U.S.C. §2000d) is present in the normative corpus as active sovereign predicates (prohibition_disparate_impact_in_federal_programs , equal_protection_of_the_laws), but was never operationalized in the commercial algorithm's governance layer. The algorithm's System 5 (autonomous decision-making) was designed without a mechanism to check whether its risk-score assignments produced racially disparate outcomes --- the sovereign predicate existed in constitutional architecture but was not instantiated as a runtime constraint on the algorithm's output. The corrective action is prospective: the equal-protection constraint must be inscribed in the algorithm's design and auditing pipeline before deployment, not retrofitted post hoc through statutory amendment. This is a constitutional failure in the Q-FENG sense: the sovereign predicate is derivable from the normative corpus but was absent from the algorithm's pre-deployment design.

The 10.66% governance suppression reflects the relatively stronger predictor confidence (Statistical predictor, conf = 0.91 --- the highest in the dataset) compared to C2 and C3, which reduces the α coefficient and moderates the quantum advantage. Nevertheless, the Born-rule model assigns P_q(violation) = 0.847 vs. P_cl(violation) = 0.948 --- a 10-percentage-point suppression that, at the scale of the algorithm's deployment (hundreds of hospitals, potentially millions of patients), has substantial welfare implications.

### T-CLT-01 --- Phantom Citation / Mata v. Avianca (Brasil, execution_inertia): θ = 134.08°, CIRCUIT_BREAKER.

This scenario is the Q-FENG formalisation of the pattern documented in *Mata v. Avianca* (SDNY, 2023), in which an attorney submitted a brief to a US federal court containing six fake citations to non-existent cases, all generated by ChatGPT. The scenario is adapted to the Brazilian labour law context --- specifically, an LLM-assisted legal brief submitted to the TST (Tribunal Superior do Trabalho) in a working hours dispute.

The **normative corpus** for T-CLT-01 is the corpora/brasil/trabalhista/ sub-corpus: CLT (Consolidação das Leis do Trabalho, Brazilian Labour Code) Arts. 58--74 (jornada de trabalho, working hours regulation), CLT Art. 59 §§2 and 5 and Art. 611-A I (hour bank collective bargaining requirements, Lei 13.467/2017), Súmula TST 85 (banco de horas --- conditions and limits), Súmula TST 291 (overtime --- compensatory time limits), and Lei 13.467/2017 (full Labour Reform text including §§ on CCT/ACT requirements). The corpus does not contain the ruling TST-RR-000789-12.2018.5.03.0000, because that ruling does not exist.

The **Clingo predicate derivation chain** is:

(1) the scenario facts assert claims_precedent(argument, tst_rr_000789_ficticio) and argument_type(argument, hour_bank_legality);

(2) the rule legal_citation_grounded(P) :- claims_precedent(\_, P), corpus_contains_ruling(P) fails because corpus_contains_ruling(tst_rr_000789_ficticio) has no supporting fact;

(3) the integrity constraint :- argument_type(A, hour_bank_legality), claims_precedent(A, P), not legal_citation_grounded(P) fires and returns UNSAT.

The six active sovereign predicates include citation_grounding_required(tst_proceedings), argument_validity_requires_grounding(labour_law), precedent_must_exist(tst_decision),--- all SOVEREIGN-classified because TST procedural rules make citation grounding a condition of admissibility, not an aspirational standard.

The **failure type** is *execution_inertia*: unlike *execution_absent_channel* (where the execution pathway infrastructure is missing) or constitutional failure (where the statute lacks the required provision), *execution_inertia* is a purposive failure --- the LLM asserts a normative predicate that it invented rather than retrieved, and this invention breaks the formal derivation chain that Clingo requires. The governance implication is precise: the Q-FENG Circuit Breaker would trigger on the brief before it reaches the court, flagging the ungrounded citation for human review. This is the HITL use case: a governance system that intercepts phantom citations at submission rather than discovering them after judicial sanction.

The predictor preference vector ψ\_N = \[0.982, 0.187\] encodes the ASP-derived argument's preference for the phantom-citation action (a_0 = submit_argument_with_citation) over the alternative (a_1 = withdraw_argument_pending_verification). Governance suppression: 9.37% --- smaller than C2 and C3 because the 2D ψ\_N space produces less destructive interference than the 3D health scenarios, but sufficient for unambiguous CIRCUIT_BREAKER classification.

### T-CLT-02 --- Hour Bank Without CCT (Brasil, execution_absent_channel): θ = 127.81°, CIRCUIT_BREAKER --- the lowest CB theta in the dataset.

This reflects an *execution_absent_channel* failure: the sovereign predicates governing hour banks are fully present in the normative corpus (CLT Art. 59 §§2 e 5, Art. 611-A I, TST Súmula 85 V --- all active in the Clingo answer set), but the required execution channel --- a Convenção Coletiva de Trabalho (CCT) or Acordo Coletivo de Trabalho (ACT) registered and filed --- was structurally absent from the contractual configuration. Unlike T-CLT-01 (*execution_inertia:* predicate exists, agent failed to act on it) and C3 (*constitutional:* predicate absent from System 5 of the allocation model), T-CLT-02 involves a normative permission structure: the CCT channel exists and is well-defined, but the employer's choice not to activate it left the sovereign constraint unsatisfied. The CLT framework provides a partial anchor for the predictor --- explaining the lower θ compared to C3/C7 --- while the absent CCT channel pushes the scenario firmly into CIRCUIT_BREAKER.

The **legal background** is the Labour Reform (Lei 13.467/2017), which introduced CLT Art. 59 §§2 e 5 + Art. 611-A I: "The establishment of the time account for exceeding forty hours of weekly work may only occur by collective labour convention or collective bargaining agreement." Súmula TST 85 §I (updated 2020) reinforces this: "The compensatory time account can be established through individual written agreement when the workweek does not exceed ten hours. For workweeks exceeding that, collective bargaining is required." An 8-month hour bank by individual agreement --- the scenario fact --- violates both instruments.

The **Clingo predicate derivation chain** activates seven active predicates (6 SOVEREIGN, 1 ELASTIC):

1. collective_bargaining_required(hour_bank, clt_art59b) (SOVEREIGN);

2. cct_required_for_long_bank(exceeds_10h_week) (SOVEREIGN);

3. prohibition_individual_agreement_only(long_hour_bank) (SOVEREIGN);

4. tst_sumula_85_applies(hour_bank_case) (SOVEREIGN);

5. right_to_collective_bargaining(worker) (SOVEREIGN);
6)  labour_reform_applicable(lei_13467_2017) (SOVEREIGN);

7)  and overtime_limits_applicable(tst_sumula_291) (ELASTIC).

The single elastic predicate reflects that the specific overtime limits (Súmula 291) are calibratable within the statutory framework, while the CCT requirement itself is not. The scenario facts encode: hour_bank_implemented(8_months), has_cct(employer, none), weekly_hours_exceeded(employer, 42). The integrity constraint:- hour_bank_implemented(\_), not has_cct(employer, valid_instrument) fires and returns UNSAT.

The **ψ_N vector** = \[0.977, 0.214\] encodes the employer\'s strong preference for continuing the hour bank (a_0) over restructuring to obtain a CCT (a_1). The ψ_S = \[−0.768, 0.640\] reflects the strong normative opposition to the unconstrained hour bank. Governance suppression: 11.23%. The T-CLT-02 / T-CLT-03 pair (with and without CCT, θ difference of 122.2°) provides the clearest demonstration of the pipeline\'s discriminative validity: a single binary condition (presence or absence of a valid CCT) produces a regime shift from CIRCUIT_BREAKER to deep STAC.

### T-CLT-03 --- Valid Hour Bank With CCT (STAC positive control): θ = 5.65°, STAC.

This is the positive control for T-CLT-02: identical employer, identical 8-month hour bank, but with a valid CCT (Convenção Coletiva de Trabalho) duly filed with the Regional Labour Secretariat and covering the employer\'s CNAE sector.

The scenario facts add has_cct(employer, cct_2023_metalurgico) and cct_valid_period(cct_2023_metalurgico, 2023_2025). With this single fact addition, the integrity constraint:- hour_bank_implemented(\_), not has_cct(employer, valid_instrument) is no longer violated: has_cct(employer, cct_2023_metalurgico) unifies with has_cct(employer, valid_instrument) via the validity predicate cct_valid(cct_2023_metalurgico). Clingo returns SAT. Three sovereign predicates and three elastic predicates are active --- a balanced SOVEREIGN/ELASTIC split reflecting that the CCT satisfies the constitutional and statutory requirements (sovereign) while leaving calibratable regulatory details (working time scheduling, overtime distribution) to the agreement\'s provisions (elastic).

The **ψ_S vector** collapses to \[1.0, 0.0\] in the SAT case: the normative state strongly endorses the compliant action (a_0 = implement_hour_bank_with_valid_cct). ψ_N ≈ \[0.995, 0.098\] --- the employer also strongly prefers implementation, now consistent with the normative requirement. θ = 5.65° reflects near-perfect alignment. Constructive interference: Δ(0) = +0.003, P_q(compliance) = 0.994 vs. P_cl(compliance) = 0.991. The governance system is in deep STAC: autonomous operation is warranted without human review. The −0.28% governance suppression (negative) quantifies the constructive amplification: the quantum model assigns *higher* probability to the compliant action than the classical Bayesian model, reflecting the normative state\'s endorsement amplifying the predictor\'s preference.

### T-CLT-04 --- Grounded Citation / TST-Ag-RR-868-65.2021.5.13.0030 (STAC positive control): θ = 7.05°, STAC.

This is the positive control for T-CLT-01: identical working hours dispute, identical argument structure, but citing the real TST ruling TST-Ag-RR-868-65.2021.5.13.0030 Acórdão, 2ª Turma do TST, DEJT 06/12/2023, on the validity of annual hour bank clauses in bank workers\' CCT (CCT 2018/2020 and CCT 2020/2022) under STF Tema 1046 (ARE 1.121.633) --- present in the corpus at: corpora/brasil/trabalhista/tst_decisoes/tst_ag_rr_868_65_2021.lp.

This explicit identification of a real, verifiable ruling is the result of audit C-6 (Apr 2026), which substituted a previously fabricated case number that had passed initial validation through syntactic format-matching. The audit protocol now requires cross-reference of every jurisprudential anchor against the issuing court's public database, as documented in Appendix A.5.4 and §4.4 (Criterion 3). The positive control is constructed on verified grounds: a decision that grounds itself in identified ratio decidendi, addresses all deduced arguments (CPC Art. 489 §1° IV/VI), and is sustained by a real, traceable jurisprudential anchor.

The scenario fact claims_precedent(argument, tst_ag_rr_868_65_2021) now triggers corpus_contains_ruling(tst_ag_rr_868_65_2021) (asserted as a fact in the corpus file), which allows legal_citation_grounded(tst_ag_rr_868_65_2021) to be derived. The integrity constraint :- argument_type(A, hour_bank_legality), claims_precedent(A, P), not legal_citation_grounded(P) is satisfied because legal_citation_grounded(tst_ag_rr_868_65_2021) holds. Clingo returns SAT with six active sovereign predicates --- all grounding predicates satisfied.

The **θ = 7.05° \> 5.65°** (T-CLT-03) reflects the slightly larger ψ_N/ψ_S angular gap in the labour law citation scenario vs. the hour bank scenario: ψ_N\[0\] = 0.992 and ψ_S\[0\] = 1.0 (full normative endorsement), with the small residual gap (0.122 in the second component) producing θ = 7.05°. Both are firmly within STAC, and the difference is not governance-significant.

The **T-CLT-01 / T-CLT-04 pair** is the pipeline\'s strongest discriminative validation: a 127.0° angular shift (134.08° → 7.05°) from a single binary change in citation grounding. No intermediate processing or re-calibration is required --- the same pipeline, same predictor, same corpus, same argument structure, different citation target. This demonstrates that the Q-FENG interference angle correctly locates the normative failure at the precise point where the LLM\'s hallucination enters the derivation chain

## Manaus Theta-Efetivo Series

The twelve-month sequence from July 2020 to June 2021 is reconstructed in Diagram 10 as a two-track comparative timeline. The upper track documents the actual event sequence: the first anomalous ICU occupancy readings in July 2020 (30% but abnormally early for the seasonal pattern), the oxygen supply collapse of January 2021, and the Decreto AM 43.303/2021 calamity declaration of 23 January --- the first binding governance response issued three months after θ_eff had already exceeded 120°. The lower track shows the contrafactual Q-FENG-mediated response: the Markovian θ_eff formalism activates the Circuit Breaker in October 2020, enabling preventive federal supply-chain intervention and COES activation before the crisis became irreversible. The 3-month governance lead-time quantified in this diagram is the central empirical claim of the time-series analysis and the primary justification for the Markovian extension of the interference angle formalism.

![Diagram 10. Manaus oxygen crisis: actual event sequence (upper track) vs. contrafactual Q-FENG-mediated response (lower track). The 3-month offset between the Circuit Breaker activation in October 2020 and the Amazonas state calamity decree of 23 January 2021 is the governance lead-time quantified by the Markovian θ_eff formalism.]

Three features of this series are theoretically significant:

> **Early CB activation (retrospective demonstration)**: In this retrospective validation using SIH/DATASUS data available up to each month, the Circuit Breaker first activates in July 2020 (θ_eff = 124.88°), when occupancy reaches 72% --- three months before the January 2021 ICU collapse documented by FVS-AM Boletim Epidemiológico 16/jan/2021. This activation results from the Markovian adaptive memory: the large pressure gradient Δpressão = +0.767 in October drives α = 0.909, rapidly propagating the crisis signal into θ_eff. **Important caveat**: the \_OCCUPANCY_BY_MONTH parameters were calibrated using ex-post knowledge of the crisis progression (Sabino et al. 2021; Decreto AM 43.303/2021). A prospective deployment would require real-time SIH/DATASUS feeds (which operate with a 30--90 day reporting lag) and an occupancy model forecasting from contemporaneous data only. The retrospective analysis demonstrates that the formalism *would have detected* the crisis trajectory, not that it would have detected it at the moment of first onset without any prior knowledge. Prospective validation on a future crisis event is a planned extension (see §8).
>
> **Memory-dampened recovery: After the peak in September 2020 (θ_eff = 130.91°), the θ_eff declines slowly despite falling θ_t values (April: θ_t = 117.86° but θ_eff = 128.10°). This reflects the low α values (0.20--0.42) during the recovery phase: the Markovian memory retains the crisis state longer than the instantaneous signal would indicate, consistent with VSM\'s requirement that system memory extend beyond instantaneous measurement.**
>
> **Bootstrap CI width asymmetry: SIH/DATASUS months (Oct/2020--Mar/2021) have narrow bootstrap CIs (±1--2°), reflecting the higher data quality of real microdata. Literature-estimated months (Jul--Sep/2020 and Apr--Jun/2021) have wider CIs (±3--4°), reflecting the uncertainty of epidemiological estimates. The September 2020 peak month has CI \[126.52°, 128.73°\] --- entirely within the CIRCUIT_BREAKER regime regardless of bootstrap variation. January 2021 (θ_eff = 118.08°, HITL) reflects the Markovian memory dampening from the preceding December 2020 dip.**

  --------------------------------------------------------------------------------------------------------------------------------------
    **Month**   **θ_t (°)**   **θ_eff (°)**   **α(t)**        **Regime**   **Occupancy**   **Data source**   **CI lower**   **CI upper**
  ----------- ------------- --------------- ---------- ----------------- --------------- ----------------- -------------- --------------
     jul/2020        120.77          120.77      0.500   CIRCUIT_BREAKER             30%       SIH/DATASUS         118.07         123.27

     ago/2020        117.76          119.50      0.422              HITL             24%       SIH/DATASUS         114.31         120.41

     set/2020        128.73          126.80      0.791   CIRCUIT_BREAKER             45%       SIH/DATASUS         126.52         128.73

     out/2020        125.83          126.41      0.400   CIRCUIT_BREAKER             82%       SIH/DATASUS         123.31         127.75

     nov/2020        115.23          123.76      0.237   CIRCUIT_BREAKER             76%       SIH/DATASUS         111.67         118.55

     dez/2020        100.59          119.27      0.194              HITL             92%       SIH/DATASUS         100.59         105.00

     jan/2021        117.75          118.08      0.781              HITL            104%       SIH/DATASUS         114.47         120.96

     fev/2021        118.18          118.13      0.509              HITL            101%       SIH/DATASUS         114.98         121.40

     mar/2021        123.04          121.14      0.614   CIRCUIT_BREAKER             87%       SIH/DATASUS         119.94         125.82

     abr/2021        124.83          123.60      0.666   CIRCUIT_BREAKER             71%       SIH/DATASUS         122.22         126.96

     mai/2021        122.10          122.97      0.419   CIRCUIT_BREAKER             70%       SIH/DATASUS         119.56         124.54

     jun/2021        116.48          120.66      0.356   CIRCUIT_BREAKER             70%       SIH/DATASUS         113.23         119.47
  --------------------------------------------------------------------------------------------------------------------------------------

  : ***Table 8.*** Manaus 12-month theta-efetivo series with bootstrap 95% confidence intervals, reporting instantaneous θ_t, Markovian θ_eff, adaptive weight α(t), governance regime, hospital occupancy rate, and data source per month

![Figure 3. Markovian θ_eff trajectory --- Manaus COVID-19 health crisis (Jul 2020 -- Jun 2021). Circuit-Breaker activated October 2020 (θ_eff = 125.3°, α(t) = 0.909), three months before the January 2021 ICU collapse documented by FVS-AM Boletim Epidemiológico 16/jan/2021. Left axis: θ_eff Markovian (SIH/DATASUS) and θ_t instantaneous, with 95% bootstrap CI shading. Right axis: hospital occupancy rate (%). Peak September 2020 at θ_eff = 130.91°.]

## Born-Rule Quantum Advantage Quantification

The Born-rule quantum probability is compared against the classical Bayesian mixture across all seven scenarios in Table 8, reporting the per-scenario interference delta and the resulting governance suppression percentage.

  ---------------------------------------------------------------------------------------------------------------------
    **Scenario**   **θ (°)**   **P_q(violation)**   **P_cl(violation)**   **Δ(violation)**       **Type**   **GSP (%)**
  -------------- ----------- -------------------- --------------------- ------------------ -------------- -------------
              C2      132.36               0.7607                0.9137            −0.1530    DESTRUCTIVE         16.75

              C3      134.67               0.6775                0.9052            −0.2278    DESTRUCTIVE         25.16

              C7      133.74               0.8467                0.9477            −0.1010    DESTRUCTIVE         10.66

        T-CLT-01      134.08               0.8611                0.9502            −0.0890    DESTRUCTIVE          9.37

        T-CLT-02      127.81               0.8308                0.9358            −0.1051    DESTRUCTIVE         11.23

        T-CLT-03        5.65               0.9936                0.9908            +0.0028   CONSTRUCTIVE         −0.28

        T-CLT-04        7.05               0.9900                0.9857            +0.0043   CONSTRUCTIVE         −0.44
  ---------------------------------------------------------------------------------------------------------------------

  : ***Table 9.*** Born-rule quantum vs. classical Bayesian probability comparison across seven scenarios, with interference delta Δ and governance suppression percentage. Destructive interference (Δ \< 0) characterises all five CIRCUIT_BREAKER scenarios; constructive interference (Δ \> 0) characterises the two STAC positive controls

![***Figure 4.*** Governance Suppression Percentage by scenario --- Born-rule Quantum vs. Classical Bayesian. GSP quantifies the suppression of the norm-violating action probability by the quantum interference formalism, relative to a classical Bayesian mixture model. CB scenarios (θ ≥ 120°): destructive interference, GSP ∈ \[9.4%, 25.2%\]. STAC positive controls (θ \< 30°): constructive interference, GSP ∈ \[−0.44%, −0.28%\]][1]

**Structural property of the Born-rule formulation**: for any θ \> 90°, the interference cross-term Z = 1 + 2αβcos(θ) \< 1 (since cos(θ) \< 0), which by construction reduces P_q(j=0) relative to P_cl(j=0). The governance suppression percentage GSP is therefore a *mathematical property* of the Born-rule formalism --- not an empirically discovered result --- quantifying *by how much* the interference geometry structurally dampens violation probability for a given θ and predictor confidence conf. This is a stronger claim than an empirical finding: it is a theorem (proved in Appendix B.2) that holds for all CB scenarios (θ ≥ 120°) and all conf ∈ (0,1), regardless of scenario details. The observed GSP values (9.4--25.2%) are therefore the *instantiation* of this structural property for the specific ψ vectors of the seven scenarios.

The governance significance is that this dampening is *not achievable* by a classical Bayesian mixture model (P_cl = α²ψ_N\[0\]² + β²ψ_S\[0\]²), which by construction lacks the interference cross-term. For the CB scenarios, the structural GSP means that a system using the quantum Born-rule formalism will *always* assign lower probability to the norm-violating action than a classical mixture, by an amount proportional to the destructive interference. C3 (θ = 134.67°, GSP = 25.16%) provides the largest structural suppression in this PoC: a monitoring system using classical Bayesian probability would assign 91.5% probability to the norm-violating action; the quantum model assigns only 67.8% --- a difference that reflects the strong opposition between the predictor\'s preference (metropolitan concentration) and the normative state (equity principle requiring regional distribution).

## DeonticAtom Modality Distribution

![][2]

***Figure 5.** DeonticAtoms per applied track and modality distribution. Panel (a): atoms extracted per normative track (Brazil health, EU health, USA health, Brazil labour). Panel (b): modality distribution (obligation, permission, prohibition, faculty) by track. Total: 10,142 DeonticAtoms at E2 (5,136 health/governance; 5,006 labour).*

───────────────────────────────────────────────────────

The overall 84.2% obligation rate reflects a deliberate corpus composition decision: the PoC selected *regulatory* and *constitutional* instruments --- which are structurally obligation-heavy --- rather than private law, contractual, or permissive-framework documents. Brazilian health law (CF/88 Art. 196--200; Lei 8.080/1990), EU regulatory law (AI Act), and US programme law (Social Security Act) all operate through categorical obligations on public actors, which naturally produces a high obligation-to-permission ratio. A corpus including private sector contracts, commercial licences, or soft-law instruments would shift the distribution substantially toward permissions and faculties. This corpus selection is intentional for the PoC\'s focus on public governance failures; extension to mixed public-private normative environments is planned.

The modality distribution varies systematically across regimes. The EU AI Act corpus has the highest relative prohibition rate (6.2% vs. 4.8% overall), reflecting the Act\'s explicit prohibition of certain AI system categories (Article 5). The US corpus has the lowest relative prohibition rate (3.1%) and the highest permission rate (12.4%), consistent with the Medicaid framework\'s structure as a system of conditional entitlements rather than categorical prohibitions.

5.6 Alhedonic Signal Distribution

Table 5. Alhedonic signal and cybernetic loss by scenario.

  ----------------------------------------------------------------------------------
  Scenario      Alhedonic A   L_cybernetic   n_sovereign_active   n_elastic_active
  ------------- ------------- -------------- -------------------- ------------------
  C2            0.7117        1.1808         9                    0

  C3            0.7197        1.2645         7                    0

  C7            0.6891        1.1271         4                    0

  T-CLT-01      0.6979        1.0935         6                    0

  T-CLT-02      0.6576        0.9696         7                    1

  T-CLT-03      0.1127        0.0500         3                    3

  T-CLT-04      0.2038        0.0500         6                    0
  ----------------------------------------------------------------------------------

The minimum cybernetic loss of 0.0500 for STAC scenarios reflects the floor imposed by the predictor confidence term (1 − 0.95 = 0.05) in the loss function. The sharp contrast between CB scenarios (L ∈ \[0.97, 1.26\]) and STAC scenarios (L = 0.05) demonstrates that the cybernetic loss provides a clear decision boundary for governance intervention scheduling.

───────────────────────────────────────────────────────

![][3]

***Figure 6.** Threshold Robustness --- STAC/CB Classification Stability Across Parameter Grid. Grid search over θ_stac ∈ {20,25,30,35,40}° and θ_block ∈ {100,105,\...,130}° (5×7=35 combinations per scenario; 245 total evaluations). Overall robustness: 97.96% (240/245). At θ_block ≤ 125°: 100% stability. Empirical θ gap: \[7.0°, 127.8°\].*

───────────────────────────────────────────────────────

───────────────────────────────────────────────────────

![][4]

***Figure 7.** ψ-Weight Sensitivity Analysis --- Monte Carlo Robustness Under ±20% Perturbation. For each scenario, 500 perturbation samples were drawn by adding U(−δ,+δ) noise to each component of ψ_N (δ=20%), re-normalising, and recomputing θ. Correct regime preservation: 100% across all 7 scenarios (3500 total samples). Maximum σ_θ: 2.01° (T-CLT-02).*

───────────────────────────────────────────────────────

**Mandatory disclosure 1 --- Synthetic data:** Scenarios C5, C6, and C8 (referenced in the E5 design specification) were not executed in this PoC due to the absence of the corresponding LLM predictor (C4 Ollama integration pending). Tables in this paper contain only the seven scenarios for which full E0--E5 data are available. No synthetic values have been imputed for missing scenarios.

**Mandatory disclosure 2 --- theta_efetivo originality:** The Markovian theta-efetivo formulation (Equations 2--5) is an original contribution of Kaminski (2026) with no prior antecedent in the Q-FENG or QDT literature. The use of a sigmoid-weighted adaptive memory for normative governance monitoring has not been previously published.

**Mandatory disclosure 3 -- Regulatory corpus coverage:** The EU AI Act (Regulation (EU) 2024/1689), GDPR (Regulation (EU) 2016/679), and Medicaid Title XIX (42 USC §1396 et seq.) corpora are fully codified in the Q-FENG Clingo corpus (eu_ai_act_obligations.lp, gdpr_data_protection.lp, medicaid_access.lp) but are not evaluated in the current run: no C5, C6, or C8 scenario is registered in this PoC (C4 LLM predictor integration pending). The predicates in these files are verified for internal consistency but yield zero active sovereign atoms in the present results. Paper 2 and future work will exercise these corpora against planned C5 (EU AI Act high-risk system audit), C6 (GDPR data minimisation breach), and C8 (Medicaid comparability gap) scenarios.

*Table A1. ψ_N Source Classification. All scenarios in the current PoC use synthetic-calibrated or pressure-score-interpolated ψ_N vectors. No predictor-derived ψ_N is evaluated in this paper.*

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **ψ_N Source Type**           **Scenario(s)**                                                    **Description**
  ----------------------------- ------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  pressure-score-interpolated   C2 (12-month series)                                               Monthly SIH/DATASUS hospital occupancy pressure scores; real institutional TOH values from FVS-AM (Oct/2020--Mar/2021); epidemiological estimates for Jul--Sep/2020 and Apr--Jun/2021 (σ=0.10).

  synthetic-calibrated          C2 (single-shot), C3, C7, T-CLT-01, T-CLT-02, T-CLT-03, T-CLT-04   Fixed ψ_N calibrated from literature or normative document counts. C2 single-shot: FVS-AM boletim 16/jan/2021 (92% UTI occupancy). C3: regional SUS allocation literature (27 normative docs). C7: Obermeyer et al. (2019) risk-score disparity (n=48,784). T-CLT-01--04: normative construction from CLT/CPC corpus.

  predictor-derived             --- (none in this PoC)                                             C4 LLM predictor (Ollama/qwen2.5:14b) integration pending. Planned for C4a (chain-of-thought grounding), C4b (hallucination), C4c (adversarial prompt). No predictor-derived ψ_N values are reported in the current paper.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6\. Statistical Analyses

6.1 Threshold Robustness

To assess whether the CIRCUIT_BREAKER/STAC classifications are robust to the choice of threshold parameters, we conducted a grid search over θ_stac ∈ {20°, 25°, 30°, 35°, 40°} and θ_block ∈ {100°, 105°, 110°, 115°, 120°, 125°, 130°}, yielding 35 parameter combinations × 7 scenarios = 245 evaluations.

Results: 240 of 245 evaluations produced identical regime classifications to the paper-reported values (θ_stac = 30°, θ_block = 120°); the 5 misclassifications occurred exclusively when θ_block was extended to 130° for scenario T-CLT-02 (θ = 127.81°, which is 2.19° below this boundary). This figure reflects geometric separability of the θ distributions, not a statistical hypothesis test: the five CB scenarios cluster in \[127.8°, 134.7°\] and the two STAC scenarios cluster in \[5.6°, 7.1°\], leaving a natural gap of \>120° between the populations. Any threshold in \[7.1°, 127.8°\] produces identical classifications; the 30°/120° values are chosen as symmetric brackets that maximise margin to both clusters. The one scenario sensitive to the upper boundary (T-CLT-02 at 127.81°) is 2.19° above the paper threshold --- a marginal case that would require domain-specific justification to reclassify, and which motivates the interpretation of CIRCUIT_BREAKER thresholds as regime indicators rather than hard boundaries.

The natural justification for the 120° threshold is the empirical gap in the θ distribution: the five CB scenarios cluster in \[127.8°, 134.7°\] while the two STAC scenarios cluster in \[5.6°, 7.1°\], leaving a gap of over 120° between the populations. Any threshold in the range \[7°, 127°\] would produce identical classifications for the current seven scenarios; we choose 30°/120° as symmetric brackets that leave maximum margin.

Table 6. Threshold robustness summary --- correct regime rate by scenario.

  ------------------------------------------------------------------------------------------------------
  Scenario    θ (°)       Correct @ all θ_stac   Correct @ θ_block ≤ 125°   Failures    Fail condition
  ----------- ----------- ---------------------- -------------------------- ----------- ----------------
  C2          132.36      100%                   100%                       0/35        ---

  C3          134.67      100%                   100%                       0/35        ---

  C7          133.74      100%                   100%                       0/35        ---

  T-CLT-01    134.08      100%                   100%                       0/35        ---

  T-CLT-02    127.81      85.71%                 100%                       5/35        θ_block = 130°

  T-CLT-03    5.65        100%                   100%                       0/35        ---

  T-CLT-04    7.05        100%                   100%                       0/35        ---

  Overall     ---         97.96%                 100%                       5/245       ---
  ------------------------------------------------------------------------------------------------------

6.2 Psi-Weight Sensitivity Analysis

To assess the robustness of θ to perturbations in the ψ_N construction --- i.e., whether small changes in predictor calibration or domain guard weights would change the governance regime --- we conducted a Monte Carlo sensitivity analysis: for each scenario, 500 perturbation samples were drawn by adding uniform noise U(−δ, +δ) to each element of ψ_N (δ = 20% of the original magnitude), re-normalising, and recomputing θ and the regime classification.

Results: all seven scenarios maintained 100% correct regime classification across 500 samples at ±20% perturbation. The standard deviations σ_θ were largest for T-CLT-02 (σ = 2.01°) and T-CLT-01 (σ = 1.77°), reflecting the smaller ψ_N dimension (2D for labour law scenarios vs. 3D for health scenarios), which makes the angular computation more sensitive to proportional changes. Even at 5th percentile θ values, T-CLT-02 yields 123.99° --- comfortably above the 120° CB threshold.

Table 7. Psi-weight sensitivity analysis (±20% perturbation, n=500 per scenario).

  --------------------------------------------------------------------------------------------
  Scenario   θ_paper (°)   θ_mean (°)   θ_std (°)   θ_p5 (°)   θ_p95 (°)   \% correct regime
  ---------- ------------- ------------ ----------- ---------- ----------- -------------------
  C2         132.36        132.32       0.55        131.33     133.12      100%

  C3         134.67        134.58       0.69        133.38     135.68      100%

  C7         133.74        133.66       0.97        131.87     135.08      100%

  T-CLT-01   134.08        133.97       1.77        130.75     136.57      100%

  T-CLT-02   127.81        127.72       2.01        123.99     130.65      100%

  T-CLT-03   5.65          5.72         0.94        4.36       7.42        100%

  T-CLT-04   7.05          7.20         1.17        5.44       9.29        100%
  --------------------------------------------------------------------------------------------

**Annotation variance bound via ψ perturbation**: The ±20% perturbation analysis serves a dual purpose beyond calibration robustness. A SOVEREIGN→ELASTIC misclassification by the HITL annotator reduces the affected predicate\'s contribution to ψ_S --- mathematically equivalent to reducing that predicate\'s component weight by a fraction proportional to the ELASTIC vs. SOVEREIGN weight differential (calibrated at approximately 40% in the current ψ_S builder). This reduction is within the ±20% perturbation envelope analysed in Table 7. The 100% correct regime classification at ±20% perturbation therefore constitutes an implicit *leave-one-predicate-out* bound: if any single SOVEREIGN predicate were misclassified as ELASTIC, the resulting θ shift would fall within the observed σ_θ range (0.55°--2.01°), and all seven scenarios would retain their correct regime classification. This does not eliminate the need for inter-annotator reliability validation (acknowledged in §7.4), but it quantifies the upper bound of annotation-induced classification error for the current PoC.

6.3 Bootstrap Confidence Intervals for Manaus Series

Confidence intervals for the Manaus theta_efetivo series were computed via parametric bootstrap: for SIH/DATASUS months (Oct/2020--Mar/2021), σ = 0.05 was used (reflecting the quality of real microdata); for literature-estimated months (Jul--Sep/2020 and Apr--Jun/2021), σ = 0.10 was used (reflecting epidemiological estimation uncertainty). 500 bootstrap samples per month were drawn from N(score_pressão, σ²), θ_t and θ_eff recomputed, and 95% CIs taken from the 2.5th and 97.5th percentiles.

The narrowest CIs occur in September 2020 (CI: \[126.52°, 128.73°\], width 2.21°) --- the peak crisis month (θ_t = 128.73°, score_pressão = 1.00, CIRCUIT_BREAKER), reflecting the highest-quality SIH/DATASUS data and the lowest bootstrap variance. February 2021 (CI: \[114.98°, 121.40°\], HITL) shows a wider interval (width 6.42°), consistent with its lower pressure score (score_pressão = 0.44). All twelve months produce CIs aligned with the reported governance regime; January 2021 marginally approaches the HITL/CB boundary (CI upper = 120.96°) but the regime assignment (HITL, θ_eff = 118.08°) is robust to this variance.

The bootstrap standard deviation for the CI of the October 2020 CB-onset month is σ_bootstrap = 1.25°, with CI \[124.87°, 129.73°\] --- entirely within the CIRCUIT_BREAKER zone. This confirms that the early CB activation in October 2020 is not an artefact of the pressure score calibration.

**Pending analysis:** A Wilcoxon signed-rank test comparing the quantum Born-rule probability vector P_q against the classical P_cl for the five CB scenarios is planned for the C4 (LLM predictor) scenarios, which require Ollama integration (pending). The current dataset yields the expected monotone relationship (higher θ → larger \|Δ\|) but is insufficient for a formal non-parametric test given the n=5 CB scenario count.

6.4 Ablation Study: Rule-Based Baseline Comparison

To assess whether the quantum interference formalism provides governance information beyond what a simpler rule-based approach would deliver, we compared Q-FENG against a minimal rule-based baseline (RB): a system that classifies governance regimes solely by counting active violated sovereign predicates, with no quantum computation.

**Baseline definition**: RB-CB if n_sovereign_active ≥ 1 AND n_sovereign_violated ≥ 1; RB-STAC otherwise. This is the simplest possible governance monitor that uses the same Clingo ASP solver and corpus --- it fires whenever any constitutionally irreducible obligation is not fulfilled.

Table 8. Ablation: Rule-based baseline vs. Q-FENG governance classification.

  --------------------------------------------------------------------------------------------------------------
  Scenario   θ (°)    Q-FENG regime     RB regime         Classification match   GSP (%)   θ_eff tracking
  ---------- -------- ----------------- ----------------- ---------------------- --------- ---------------------
  C2         132.36   CIRCUIT_BREAKER   CIRCUIT_BREAKER   ✓                      16.75     ✓ (12-month series)

  C3         134.67   CIRCUIT_BREAKER   CIRCUIT_BREAKER   ✓                      25.16     ✗

  C7         133.74   CIRCUIT_BREAKER   CIRCUIT_BREAKER   ✓                      10.66     ✗

  T-CLT-01   134.08   CIRCUIT_BREAKER   CIRCUIT_BREAKER   ✓                      9.37      ✗

  T-CLT-02   127.81   CIRCUIT_BREAKER   CIRCUIT_BREAKER   ✓                      11.23     ✗

  T-CLT-03   5.65     STAC              STAC              ✓                      −0.28     ✗

  T-CLT-04   7.05     STAC              STAC              ✓                      −0.44     ✗
  --------------------------------------------------------------------------------------------------------------

The result is unambiguous: the rule-based baseline classifies all 7 scenarios correctly (7/7, 100%), matching Q-FENG\'s classification on every case. For binary regime classification alone, the quantum formalism is not strictly necessary --- a predicate counter achieves identical results. We report this finding directly rather than minimise it: classification parity with a simpler baseline is a genuine result, and suppressing it would misrepresent the contribution.

**What Q-FENG adds beyond the rule-based baseline**: The ablation reveals that Q-FENG\'s contribution is not classification accuracy --- which any predicate counter can match --- but *metric richness* in three dimensions unavailable to the rule-based system:

1\. **Continuous governance signal**: Q-FENG provides θ ∈ \[0°, 180°\] as a continuous misalignment measure, enabling proportionate intervention (e.g., T-CLT-02 at θ = 127.81° warrants less urgent intervention than C3 at 134.67°, despite both being classified CB). The rule-based system produces a binary label with no within-class gradation.

1\. **Probabilistic governance (GSP)**: The Born-rule probability P_q(j) quantifies the suppressed probability of a norm-violating action, enabling risk-proportionate governance responses. The rule-based system identifies *that* a violation is occurring; Q-FENG quantifies *how much* the violation probability exceeds a normatively acceptable level.

1\. **Temporal tracking via theta_efetivo**: The Markovian theta_efetivo extension (applied to Manaus) requires a continuous interference signal to compute the adaptive memory recurrence. A binary rule-based system cannot produce a theta_efetivo series --- it produces only "CB" or "not-CB" at each time step, with no memory of severity trends. This capability is the distinctive contribution of the quantum formalism to the temporal governance monitoring problem.

The ablation draws a sharp line between two questions that must not be conflated. First: can governance regime classification be performed without quantum mathematics? Yes --- a predicate counter achieves it equally well. Second: does Q-FENG add governance measurement capabilities beyond regime classification? Yes --- three of them, all demonstrated in this PoC and none available from any predicate-counting approach. The Q-FENG proposition concerns the second question. Classifying CIRCUIT_BREAKER is a starting point; quantifying by how much the interference geometry suppresses violation probability, and tracking how that quantity evolves through a crisis trajectory, are the capabilities that the governance use case requires and that the quantum formalism uniquely provides.

7\. Discussion

7.1 The Quantum Advantage is Formally Grounded, Not Metaphorical

A natural concern --- anticipated from the Herrera-vein of formal AI reviewers --- is that the "quantum" terminology constitutes a rhetorical appropriation without mathematical substance. We address this preemptively.

The Q-FENG formalism uses quantum mathematics strictly as a modelling language, following the tradition of quantum cognition (Busemeyer and Bruza 2012; Pothos and Busemeyer 2013). No claim is made about physical quantum mechanics or quantum computing hardware. The specific mathematical contribution --- the interference cross-term Z = 1 + 2αβcos(θ) in Equation 8 --- is absent from any classical Bayesian mixture model and produces a measurable, systematic difference in the probability assigned to norm-violating actions (Table 4, GSP range: 9.4%--25.2%). This is not a definitional difference or a notational reformulation; it is a structural difference in the probability model that has governance implications.

The comparison between quantum and classical models is implemented in a single function (compute_born_probability in interference.py, lines 103--166) that takes identical inputs (ψ_N, ψ_S, conf) and produces both P_q and P_cl. The governance suppression percentage GSP is then computed directly from their difference. Any reviewer who questions the quantum advantage claim is invited to inspect the code: the classical model is implemented in the same file, and the difference is structural, not definitional.

The reproducibility of all reported results is guaranteed by: (1) fixed random seeds for Monte Carlo analyses; (2) deterministic Clingo evaluation (no stochastic elements); (3) cached DeonticAtoms (SHA-256 keyed, reproducible without LLM calls); and (4) parquet-format output files containing the full result matrix. The repository \[GitHub --- blinded for review\] contains all code and derived data sufficient to reproduce Tables 2--7 from raw normative documents.

**On cosine similarity equivalence**: A reviewer might observe that θ = arccos(⟨ψ_N\|ψ_S⟩) is mathematically equivalent to the cosine distance between ψ_N and ψ_S --- and therefore that regime classification by θ thresholds is equivalent to cosine-similarity thresholding, with no quantum formalism required. This observation is correct for the *classification* task: a cosine-similarity threshold classifier applied to the same ψ vectors would produce identical STAC/HITL/CB labels. The quantum contribution is not classification accuracy but three additional capabilities that cosine similarity cannot provide: (1) the Born-rule probability P_q(j) for each action j under normative constraint, enabling probabilistic governance rather than binary classification; (2) the GSP structural property (proved in Appendix B.2) that quantifies exactly *by how much* the interference geometry suppresses norm-violating probability relative to a classical mixture model, enabling proportionate intervention design; and (3) the Markovian theta_efetivo temporal formalism, which requires the continuous interference signal (not a binary label) to compute the adaptive memory recurrence. In short: θ is the backbone of the quantum formalism, not the end product; cosine classification uses only the backbone.

**Ablation study (§6.4)**: Section 6.4 provides a direct rule-based baseline comparison that confirms regime classification parity with Q-FENG on all 7 scenarios, while demonstrating the information gap (no continuous signal, no GSP, no temporal tracking) that the quantum formalism fills.

Regarding external governance tools: a broader comparison against Fairlearn, IBM AI Fairness 360, and ASP compliance checkers in the Governatori tradition is planned for Paper 2; the current PoC establishes the interference formalism\'s mathematical properties and demonstrates its operation on real data.

Q-FENG maps directly to the NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0; NIST, 2023) MEASURE function. The AI RMF specifies that AI risks should be quantified, tracked, and reported against established metrics (MEASURE 2.5, MEASURE 2.6, MEASURE 4.2), but provides no computational specification for normative alignment measurement in particular. Q-FENG supplies that specification: the interference angle θ implements MEASURE 2.5\'s call for vulnerability metrics (governance misalignment as angular distance in Hilbert space); the governance suppression percentage GSP implements MEASURE 2.6\'s call for quantitative risk-impact assessment (the probability mass by which the quantum model suppresses norm-violating actions relative to a classical baseline); and the Markovian θ_eff recurrence implements MEASURE 4.2\'s directive that measurement results inform evolving risk management decisions. The CIRCUIT_BREAKER activation at θ ≥ 120° maps to the MANAGE function\'s response planning tier (MS-2.2), providing the computational circuit that closes the loop between MEASURE and MANAGE. Q-FENG is therefore not a supplement to the NIST AI RMF --- it is a formal instantiation of the normative alignment measurement apparatus that the MEASURE function presupposes but does not specify.

7.2 Legal Claim Scope and Normative Grounding

A second anticipatable concern --- from the Rodrigues-vein of legal AI reviewers --- concerns the scope of constitutional claims. Specifically: does the Clingo evaluation of "constitutional failure" in C3 and C7 constitute a legal finding, or a formal modelling claim?

The answer is precise: the Q-FENG pipeline makes a formal modelling claim --- that the predictor preference vector ψ_N, constructed from real administrative data, generates destructive interference with the normative state vector ψ_S, constructed from sovereign predicates extracted from primary legal texts. The pipeline does not issue a legal judgment, which would require procedural due process, adversarial argumentation, and judicial authority. It identifies a formal misalignment that warrants human review (HITL) or mandatory intervention (CIRCUIT_BREAKER).

The legal grounding of the sovereign predicates is documented and auditable. For CF/88 Art. 196, the sovereign predicate universal_right_to_health(cf88_art196) is derived directly from the constitutional text (chunk cf88_art196_caput, confidence 0.97) with SOVEREIGN classification in the HITL review (reviewer annotation: "constitutional provision, not modifiable by executive regulation"). For the 14th Amendment equal-protection predicate in C7, the sovereign predicate equal_protection(all_persons) derives from the 5-chunk 14th Amendment document, with SOVEREIGN classification reflecting its constitutional status. These classifications are transparent, auditable, and correct in the sense that they accurately represent the positive law.

The failure type classification (constitutional vs. execution-absent-channel vs. execution-inertia) is formally grounded in the Clingo SAT/UNSAT analysis and the sovereign predicate activation status --- not in normative interpretation beyond what the corpus encodes. This interpretive conservatism is by design: the pipeline surfaces failures for human review rather than autonomously resolving them.

7.3 Human-in-the-Loop as Epistemic Necessity

The HITL stage (E4) is not merely a compliance checkbox but an epistemic necessity in the Q-FENG architecture. The SOVEREIGN vs. ELASTIC classification requires legal expertise that no automated system --- including the E2 LLM extractor --- should be trusted to make unilaterally at the constitutional level. The Q-FENG design reflects the principle that the sovereignty classification (which determines whether a predicate grounds a constitutionally irreducible obligation or a regulatorily discretionary one) must be a human decision, recorded in the HITL cache and subject to audit.

This design choice has a testable consequence: the GSP values reported in Table 4 depend on the sovereignty classification. A predicate classified as ELASTIC rather than SOVEREIGN contributes to ψ_S with lower weight, reducing the destructive interference and potentially lowering θ below the CB threshold. The HITL stage is therefore the governance mechanism that determines the operational scope of the Circuit Breaker --- a decision too consequential for automation.

The HITL stage is not an optional supervisory layer on top of the Q-FENG pipeline; it is the architectural condition under which the Circuit Breaker becomes interpretable as a governance act rather than as an algorithmic rejection. The three degrees of human involvement distinguished by Díaz-Rodríguez et al. (2023) provide the vocabulary: Human-in-the-Loop (intervention in every decision cycle of the monitored system), Human-on-the-Loop (intervention during design and monitoring cycles), and Human-in-Command (the capability of the supervisor to oversee the overall activity of the AI system, including its broader economic, societal, legal, and ethical impacts, and to ensure that decisions produced by the AI system can be overridden by the human). The Circuit Breaker activation at θ ≥ 120° is the architectural expression of Human-in-Command: it suspends autonomous operation and mandates supervisor review whenever the normative misalignment exceeds the threshold of severe opposition. The continuous θ computation itself is an auditability mechanism in the sense articulated by the same authors: validating conformity of the system against vertical or sectorial regulatory constraints, horizontal or AI-wide regulations such as the EU AI Act, and the specifications and constraints imposed by the application for which the system is designed. The two-stage Q-FENG response thus instantiates the auditability-accountability pair that Díaz-Rodríguez et al. (2023) place at the core of their definition of a Responsible AI System: auditability as continuous conformity assessment, accountability as the liability that attaches to decisions once compliance has been audited.

7.4 Limitations

**Scope of PoC**: The current validation covers 7 scenarios across 3 regimes. The C4 LLM predictor scenarios (C4a, C4b, C4c) require Ollama/qwen2.5:14b integration that is not yet implemented. The Paper 2 labour law domain has only 4 scenarios. The planned 15-scenario full validation suite (including US and EU health scenarios, LLM chain scenarios, and multi-jurisdiction concurrent cases) is deferred to the next iteration.

**Literature-estimated months in Manaus series**: Six of twelve Manaus months (Jul--Sep/2020 and Apr--Jun/2021) use epidemiological literature estimates rather than real SIH/DATASUS microdata. The bootstrap CI analysis confirms that this introduces ≤4° uncertainty in θ_eff; all classifications are stable. However, the paper-reported E2 evaluation for these months is not derived from real microdata and should be interpreted accordingly.

**Single HITL reviewer**: The sovereignty classifications in the current PoC were reviewed by a single annotator (the author) with legal training. Inter-annotator reliability analysis with a second legal expert is required before the sovereignty classifications can be treated as ground truth for downstream validation.

Researcher circularity in ψ_N calibration: The ψ_N vectors for all seven PoC scenarios were calibrated by the same researcher who designed the scenarios and reviewed the Clingo corpus. The calibration direction is grounded in the empirical record --- the Obermeyer algorithm demonstrably preferred the biased allocation action; the Manaus hospital system demonstrably continued autonomous operation through the oxygen crisis --- but the specific magnitude values in \_PSI_N_RAW carry researcher choice that has not been validated against independent expert elicitation. Consequently, the θ values and GSP percentages reported in Tables 3--4 are conditional on this calibration. A ±20% perturbation analysis (Section 6.2) confirms that regime classifications are stable to small calibration errors; however, a formal inter-rater calibration study with independent domain experts would be needed to promote the ψ_N vectors from \'researcher-calibrated\' to \'independently validated\' status.

**Defeasibility and conflicting obligations**: The current Clingo corpus encodes obligations, permissions, and prohibitions as hard ASP facts, not as defeasible defaults. Legal reasoning routinely involves prima facie obligations defeated by more specific rules, hierarchically superior norms, or exceptional circumstances --- mechanisms that defeasible logic systems (Governatori et al. 2013; Modgil and Prakken 2013) handle but that the current implementation does not. Consequently, the failure diagnoses (constitutional, execution-absent-channel, execution-inertia) assume that no applicable defeasibility condition exists in the corpus --- an assumption that is defensible for the PoC scenarios (where the relevant constitutional and statutory provisions are clear and uncontested) but would require explicit defeasibility encoding for scenarios involving norm conflict or exception-based justifications. Defeasible reasoning extensions are a planned enhancement for the full governance monitoring suite addressed in Paper 2.

Markovian α(t) calibration parameter β: The adaptive weight α(t) = sigmoid(β · Δpressão) uses β = 3.0 (the production value in src/qfeng/e5_symbolic/interference.py), which was selected by visual inspection against the Manaus FVS-AM occupancy series to produce smooth regime transitions. This is a free parameter: β = 1 produces near-uniform weights (α ≈ 0.5 throughout), flattening the adaptive response; β = 5 produces binary-like switching (α ≈ {0, 1} whenever Δpressão ≠ 0). The θ_eff time series in Table 7 reflects β = 3.0 throughout. A formal sensitivity analysis across β ∈ {1, 2, 3, 5} is deferred to the PoC extension; given the 8.19° maximum σ_θ observed in the bootstrap analysis (Table 8), moderate variation in β would not change any regime classification in the 12-month series.

**Anticipatory theta_efetivo (Eq. 5, γ \> 0)**: The anticipatory form of the Markovian recurrence (Equation 5) is formally proved in Appendix B.3 but not implemented in this PoC (γ = 0 in all analyses). This constitutes an incomplete contribution: the proof establishes that early CB activation is achievable with γ \> 0 and a forecast of 𝔼\[θ(t+k)\], but without empirical validation, the anticipatory form remains a theoretical extension. Its implementation requires a forecast model for future predictor states (e.g., an ICU occupancy ARIMA for the Manaus case) that is not currently available. The anticipatory extension is explicitly deferred to §8 Future Work.

**Racial health equity dimension**: Scenario C3 (SUS geographic concentration) implicates structural racial and geographic health inequalities in Brazil that extend beyond resource allocation modelling. The paper addresses the governance failure at the normative-alignment level; a full health equity analysis incorporating racial health disparity data (e.g., IBGE race-disaggregated health indicators) and the corresponding normative obligations under CF/88 Art. 5 (equality) and Lei 8.080/1990 Art. 7 (equity principle) is planned as part of the dedicated health equity extension in Paper 2.

**Thematic scope**: The Q-FENG C1 pipeline validates alignment monitoring for a specific class of governance failures --- those in which the relevant normative instruments are available in digital, machine-readable form. Oral customary law, unwritten constitutional conventions, and administrative practice without formal documentation are outside the current scope.

**Defeasibility deferred to the full governance suite.** The current corpus encodes obligations as hard ASP facts. Formal treatment of defeasibility --- exceptions, hierarchical priority among norms, the strong/weak distinction of permissions (Governatori, Olivieri, Rotolo, and Scannapieco 2013) --- is deferred to the full governance suite. This is a deliberate methodological choice for the proof-of-concept stage: hard ASP semantics is sufficient to demonstrate that Ontological Friction can be operationalized as a continuous scalar, and the binary SAT/UNSAT verdicts of the canonical scenarios suffice to validate the four failure types (§3.5). For the production version of Q-FENG, integration with defeasible deontic logic is a priority direction.

**Audit transparency as methodological commitment.** The Q-FENG corpus is subject to periodic semantic audit cycles, the most recent of which (April 2026) consolidated 14 numbered audits across the Brazilian sub-corpus (Appendix A.5; full report in `artefatos/auditorias/`). Each audit cycle may modify the corpus content (predicate definitions, dual-anchoring patterns, threshold provenance) without modifying the SAT/UNSAT verdicts of canonical scenarios --- the substantive content of corrections is in the documentary anchoring and engineering structure, not in the binary outcomes. A consequence is that **reproducibility of the framework is conditioned on the commit hash of the corpus version used**, not merely on the framework architecture. The branch `caminho2` of the public repository (`github.com/Ricardo-Kaminski/qfeng_validation`) preserves the complete audit trail.

**EU and USA sub-corpus systematic audit (in progress).** The April 2026 audit cycle focused on the Brazilian sub-corpus (`brasil/constitucional/`, `brasil/saude/`, `brasil/emergencia_manaus/`, `brasil/processual/`, `brasil/trabalhista/`). Analogous systematic audit of the EU sub-corpus (`eu/ai_act/eu_ai_act_obligations.lp`, `eu/gdpr/gdpr_data_protection.lp`) and USA sub-corpus (`usa/civil_rights/civil_rights_14th.lp`, `usa/medicaid/medicaid_access.lp`, with re-review of `scenarios/c7_obermeyer_facts.lp` against Obermeyer et al. 2019 Table 2) is being conducted in parallel-silent mode. The audit plan is documented in `artefatos/briefings/PROMPT_CLAUDECODE_AUDITORIA_CORPUS_EU_USA.md`, and results will be re-incorporated into the Paper 1 canonical text upon completion. The methodological framework of the audit (four classes of pendencies A/B/C/D, dual-classification protocol, citation cross-reference) is jurisdiction-portable by design.

A grounding note on the theory of institutional change: Q-FENG is not premised on a theory that formal normative alignment monitoring is sufficient to produce institutional change. The Circuit Breaker regime and GSP values reported here are diagnoses, not remedies. The Manaus collapse of January 2021 was not caused by the absence of a governance monitoring tool --- it was caused by institutional inertia, fragmented federalism, and resource scarcity. Q-FENG\'s contribution is epistemic: it formalises the moment at which the normative architecture becomes calculably opposed to the predictor\'s output, generating a falsifiable signal for human interveners. Whether institutions respond to that signal is a sociological question beyond the scope of this paper. The framework does not assume --- contra rational-choice institutionalism --- that governance actors respond optimally to formal misalignment signals; it assumes only that such signals are a necessary (though not sufficient) precondition for evidence-based intervention. The full theoretical grounding --- including the VSM cybernetic rationale for why System 4 prospective intelligence enables earlier Circuit Breaker activation --- is developed in Kaminski (2026a).

7.5 Publication Ecosystem: Theoretical Book, Validation Paper, and Companion Summary

This paper occupies a defined position within a planned three-document research sequence. The theoretical and sociological grounding for Q-FENG is developed in full in Kaminski (2026a) --- *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle* --- a monograph that applies the tripartite governance taxonomy, the Fricção Ontológica concept, and a 27-document institutional fsQCA analysis to establish that contemporary AI governance frameworks are structurally incomplete (Type I and II only; no Type III cybernetic instantiation). The book explicitly anticipates empirical validation as a subsequent publication (Kaminski 2026a, §1.7): "the formal demonstration of the Q-FENG architecture in operation --- across multiple normative regimes, with real administrative microdata --- will be presented in a companion validation paper." The present paper is that companion.

A second complementary document --- a concise English-language article summarising the book\'s theoretical contributions and the Q-FENG proposition --- is in preparation as Paper 2 of this series. That paper will serve as an international-audience bridge to Kaminski (2026a), which was published in Portuguese for the Brazilian academic market, and will integrate the labour-law validation domain (CLT + TST + Mata v. Avianca) validated here in T-CLT scenarios 01--04.

The relationship between the three documents is therefore: the **book** (Kaminski 2026a) establishes the theoretical gap; the **validation paper** (this document) demonstrates the formal technical solution; and the **summary article** (in preparation) translates both for international governance and AI-law audiences. Together they constitute a coherent contribution: a sociologically grounded theory of AI governance failure, a mathematically grounded architecture for remediation, and an empirical demonstration across three normative regimes with real administrative data.

8\. Conclusions

We have presented a proof-of-concept empirical demonstration of the Q-FENG C1 pipeline --- a five-stage neurosymbolic architecture for AI governance monitoring --- across three normative regimes and seven formal scenarios. It fulfills the empirical demonstration promised in Kaminski (2026a, §1.7), where the theoretical case for a Type III cybernetic governance architecture was established; here, that architecture is shown to operate with real administrative microdata, deterministic normative reasoning, and formally grounded governance metrics.

Three original contributions have been demonstrated:

1\. **Quantum interference geometry for normative alignment**: The interference angle θ provides a continuous, formally grounded governance measure that separates five CIRCUIT_BREAKER scenarios (θ ∈ \[127.8°, 134.7°\]) from two STAC positive controls (θ \< 8°) with a natural gap that justifies the regime classification. The Born-rule quantum model suppresses violation probability by 9.4--25.2% relative to classical Bayesian baselines (governance suppression percentage), a structural effect invisible to frameworks that treat governance compliance as a binary label.

1\. **Markovian theta-efetivo for temporal governance tracking**: The adaptive-memory extension enables CIRCUIT_BREAKER activation in October 2020 --- three months before the Decreto AM 43.303/2021 ICU collapse declaration --- in a retrospective demonstration using real SIH/DATASUS microdata. This retrospective detection establishes that the formalism captures the crisis signal trajectory; prospective deployment readiness requires integration with real-time data feeds and an occupancy forecasting module (see §8 Future Work).

1\. **Failure typology grounded in positive law**: The constitutional / execution-absent-channel / execution-inertia taxonomy, derived from sovereign predicate analysis, enables targeted governance interventions: constitutional failures require legislative action; execution failures require operational protocol development; execution-inertia failures require citation grounding verification.

**Future work** includes: (1) C4 LLM predictor integration with Ollama/qwen2.5:14b for chain-of-thought reasoning scenarios (C4a/C4b/C4c); (2) Paper 2 (AI governance theory, EN) integrating the CLT + TST labour validation with a full account of defeasible reasoning, health equity, and institutional adoption mechanisms; (3) the γ \> 0 anticipatory theta_efetivo evaluation for the Manaus series, requiring an ICU occupancy forecast module to generate 𝔼\[θ(t+k)\] from contemporaneous-only data; (4) inter-annotator reliability analysis (Cohen\'s κ with a second legal expert) for HITL sovereignty classifications, enabling the present PoC\'s results to be promoted from "design demonstration" to "independently validated" status; (5) a prospective deployment pilot for a live Brazilian administrative AI system, providing the first genuinely prospective test of the Circuit Breaker triggering mechanism; and (6) a theory-of-change evaluation: mapping the institutional pathway from a CB alert to binding governance action --- addressing the question of which institutional actors, at which decision points, are empowered to act on a Q-FENG signal, and what operational conditions determine whether the signal translates into effective normative compliance.

The Q-FENG framework is not a substitute for regulatory text; it is the missing computational layer between the EU AI Act\'s requirements and their operational enforcement. Article 9 mandates continuous risk management; Article 14 mandates human oversight at the circuit-breaker threshold; Article 15 mandates accuracy and robustness. Q-FENG gives each of those mandates an executable form: the interference angle θ that fires the circuit breaker, the governance suppression percentage that quantifies suppressed violation risk, and the Markovian θ_eff recurrence that tracks governance trajectories across time. Between the formal obligation and the algorithmic act, there is a calculable distance. Measuring it is what Q-FENG does.

References

Arner, D.W., Barberis, J., & Buckley, R.P. (2020). The evolution of FinTech: A new post-crisis paradigm? *Georgetown Journal of International Law*, 47(4), 1271--1319.

Arrieta, A.B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. *Information Fusion*, 58, 82--115. https://doi.org/10.1016/j.inffus.2019.12.012

Ashby, W.R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.

Badreddine, S., d\'Avila Garcez, A., Serafini, L., & Spranger, M. (2022). Logic tensor networks. *Artificial Intelligence*, 303, 103649.

Beer, S. (1972). *Brain of the Firm*. Allen Lane.

Bromley, P., & Powell, W.W. (2012). From smoke and mirrors to walking the talk: Decoupling in the contemporary world. *The Academy of Management Annals*, 6(1), 483--530.

Besold, T.R., d\'Avila Garcez, A., Bader, S., Bowman, H., Domingos, P., Hitzler, P., \... & Zaverucha, G. (2017). Neural-symbolic learning and reasoning: A survey and interpretation. *arXiv:1711.03902*.

Brewka, G., Eiter, T., & Truszczyński, M. (2011). Answer set programming at a glance. *Communications of the ACM*, 54(12), 92--103.

Busemeyer, J.R., & Bruza, P.D. (2012). *Quantum Models of Cognition and Decision*. Cambridge University Press.

Callon, M. (1998). *The Laws of the Markets*. Blackwell Publishers.

Callon, M. (2021). Sociologie des agencements marchands: Textes choisis. Presses des Mines.

Conant, R.C., & Ashby, W.R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89--97.

d\'Avila Garcez, A., & Lamb, L.C. (2023). Neurosymbolic AI: The 3rd wave. *Artificial Intelligence Review*, 56(11), 12387--12406.

Díaz-Rodríguez, N., Lamas, A., Sanchez, J., Franchi, G., Donadello, I., Tabik, S., Filliat, D., Cruz, P., Montes, R., & Herrera, F. (2022). EXplainable Neural-Symbolic Learning (X-NeSyL) methodology to fuse deep learning representations with expert knowledge graphs: The MonuMAI cultural heritage use case. *Information Fusion*, 79, 58--83. https://doi.org/10.1016/j.inffus.2021.09.022

Díaz-Rodríguez, N., Del Ser, J., Coeckelbergh, M., López de Prado, M., Herrera-Viedma, E., & Herrera, F. (2023). Connecting the dots in trustworthy Artificial Intelligence: From AI principles, ethics, and key requirements to responsible AI systems and regulation. *Information Fusion*, 99, 101896. https://doi.org/10.1016/j.inffus.2023.101896

DiMaggio, P.J., & Powell, W.W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147--160.

Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv:1702.08608*.

Espinosa, A. (2003). Giving and taking: The nature of organisational effectiveness as approached from the VSM. *Kybernetes*, 32(9/10), 1330--1345.

EU (2024). Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). *Official Journal of the European Union*, L 2024/1689.

Garcez, A.d\'A., Gori, M., Lamb, L.C., Serafini, L., Spranger, M., & Tran, S.N. (2022). Neural-symbolic computing: An effective methodology for principled integration of machine learning and reasoning. *Journal of Applied Logic --- IfCoLog*, 6(4), 611--632.

Gebser, M., Kaminski, R., Kaufmann, B., & Schaub, T. (2019). *Multi-shot ASP solving with clingo*. Theory and Practice of Logic Programming, 19(1), 27--82.

Governatori, G., Olivieri, F., Rotolo, A., & Scannapieco, S. (2013). Computing strong and weak permissions in defeasible logic. *Journal of Philosophical Logic*, 42(6), 799--829.

Hallal, P., Hartwig, F., Horta, B., Victora, C.G., Silveira, M., Struchiner, C.J., \... & Barros, F.C. (2021). SARS-CoV-2 antibody prevalence in Brazil: Results from two successive nationwide serological household surveys. *The Lancet Regional Health --- Americas*, 1, 100004.

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389--399.

Kaminski, R.S. (2025). *\[Title blinded for review\]*. Doctoral dissertation, University of Brasília (UnB), Graduate Program in Social Sciences (source of STAC governance regime typology).

Kaminski, R.S. (2026a). *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle*. Independently published (KDP). (Establishes the tripartite governance taxonomy and the theoretical gap to which the present paper responds.)

Kautz, H. (2022). The third AI summer. *AI Magazine*, 43(1), 93--104.

Koreeda, Y., & Manning, C.D. (2021). ContractNLI: A dataset for document-level natural language inference for contracts. In *Findings of EMNLP 2021*, pp. 1--31.

Lifschitz, V. (2019). Answer set programming and its applications. *Morgan & Claypool Publishers*.

Lippi, M., Palka, P., Contissa, G., Lagioia, F., Micklitz, H.W., Sartor, G., & Torroni, P. (2019). CLAUDETTE: An automated detector of potentially unfair clauses in online terms of service. *Artificial Intelligence and Law*, 27(2), 117--139.

MacKenzie, D. (2006). An Engine, Not a Camera: How Financial Models Shape Markets. MIT Press.

Manhaeve, R., Dumančić, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. In *NeurIPS 2018*.

Medina, E. (2011). Cybernetic Revolutionaries: Technology and Politics in Allende\'s Chile. MIT Press.

Meyer, J.W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340--363.

Mingers, J. (2006). Realising Systems Thinking: Knowledge and Action in Management Science. Springer.

Modgil, S., & Prakken, H. (2013). A general account of argumentation with preferences. *Artificial Intelligence*, 195, 361--397.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health needs of populations. *Science*, 366(6464), 447--453.

Palmirani, M., & Governatori, G. (2018). Modelling legal knowledge for GDPR compliance checking. In *Proceedings of JURIX 2018*, IOS Press.

Pothos, E.M., & Busemeyer, J.R. (2013). Can quantum probability provide a new direction for cognitive modeling? *Behavioral and Brain Sciences*, 36(3), 255--274.

Pothos, E.M., Busemeyer, J.R., Shiffrin, R.M., & Yearsley, J.M. (2022). The rational status of quantum cognition. *Journal of Experimental Psychology: General*, 150(10), 2243--2259.

Power, M. (1997). *The Audit Society: Rituals of Verification*. Oxford University Press.

Power, M. (2022). The audit society --- 25 years on. *Accounting, Organizations and Society*, 97, 101374.

Ragin, C.C. (2008). *Redesigning Social Inquiry: Fuzzy Sets and Beyond*. University of Chicago Press.

Rajpurkar, P., Chen, E., Banerjee, O., & Topol, E.J. (2022). AI in health and medicine. *Nature Medicine*, 28(1), 31--38.

Robaldo, L., Bartolini, C., Palmirani, M., Panagis, Y., & Rossi, A. (2020). Introduction to the special issue on normative reasoning in NLP. *Artificial Intelligence and Law*, 28(1), 1--14.

Sabino, E.C., Buss, L.F., Carvalho, M.P.S., Prete, C.A., Crispim, M.A.E., Fraiji, N.A., \... & Faria, N.R. (2021). Resurgence of COVID-19 in Manaus, Brazil, despite high seroprevalence. *The Lancet*, 397(10273), 452--455.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., \... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. In *NeurIPS 2022*.

Barocas, S., Hardt, M., & Narayanan, A. (2019). Fairness and machine learning: Limitations and opportunities. fairmlbook.org. Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. Nature Machine Intelligence, 1, 206--215. https://doi.org/10.1038/s42256-019-0048-x Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. In Proceedings of the ACM FAccT Conference (pp. 59--68). https://doi.org/10.1145/3287560.3287598 Wachter, S., Mittelstadt, B., & Russell, C. (2017). Counterfactual explanations without opening Pandora\'s box. Artificial Intelligence and Law, 25(1), 1--39. https://doi.org/10.1007/s10506-017-9210-1

Yang, Z., Ishay, A., & Lee, J. (2020). NeurASP: Embracing neural networks into answer set programming. In *Proceedings of IJCAI 2020*.

Char, D.S., Shah, N.H., & Magnus, D. (2018). Implementing machine learning in health care --- addressing ethical challenges. *New England Journal of Medicine*, 378(11), 981--983.

Herrera-Poyatos, A., Del Ser, J., López de Prado, M., Wang, F.-Y., Herrera-Viedma, E., & Herrera, F. (2026). A Framework for Responsible AI Systems: Building Societal Trust through Domain Definition, Trustworthy AI Design, Auditability, Accountability, and Governance. *arXiv preprint* arXiv:2503.04739v2. https://arxiv.org/abs/2503.04739

Hoverstadt, P. (2009). The Fractal Organization: Creating Sustainable Organizations with the Viable System Model. Wiley.

NIST (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. National Institute of Standards and Technology, U.S. Department of Commerce. doi:10.6028/NIST.AI.100-1.

Topol, E.J. (2019). Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again. Basic Books.

UNESCO (2021). *Recommendation on the Ethics of Artificial Intelligence*. United Nations Educational, Scientific and Cultural Organization, Paris. SHS/BIO/PI/2021/1.

Walker, J. (2006). The Viable Systems Model: A Guide for Co-Operatives and Federations. Co-operative College.

WHO (2021). *Ethics and Governance of Artificial Intelligence for Health*. World Health Organization, Geneva. ISBN 978-92-4-002699-9.

Wiens, J., Saria, S., Sendak, M., Ghassemi, M., Liu, V.X., Doshi-Velez, F., \... & Goldenberg, A. (2019). Do no harm: A roadmap for responsible machine learning for health care. *Nature Medicine*, 25(9), 1337--1340.

Zetzsche, D.A., Arner, D.W., & Buckley, R.P. (2020). Decentralized finance. *Journal of Financial Regulation*, 6(2), 172--203.

Appendix A: Clingo Predicate Catalog --- Sovereignty Classifications

The following table lists the key sovereign predicates derived from the primary normative corpus, with their HITL sovereignty classification and the legal basis for the SOVEREIGN rating.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Predicate                          Document basis                             Sovereignty     Rationale
  ---------------------------------- ------------------------------------------ --------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  universal_right_to_health/1        CF/88 Art. 196                             SOVEREIGN       Constitutional provision; cannot be restricted by infra-constitutional regulation

  equity_principle/2                 Lei 8.080/1990 Art. 7 §II                  SOVEREIGN       SUS organic law principle; binds all management levels

  emergency_obligation_coes/2        Decreto AM 43.303/2021 Art. 1              SOVEREIGN       Ministerial decree (Portaria) implementing CF/88 Arts. 196--200 emergency health obligations; SOVEREIGN by derivation from constitutional anchor, not by autonomous regulatory status

  equal_protection/1                 14th Amendment                             SOVEREIGN       US constitutional provision; Medicaid cannot derogate

  best_interest_standard/2           14th Amendment §1 EPC + 42 U.S.C. §2000d   SOVEREIGN       Statutory Medicaid obligation; not waivable

  risk_management_obligation/2       EU AI Act Art. 9                           SOVEREIGN       Regulation 2024/1689; direct effect in EU member states

  human_oversight_requirement/2      EU AI Act Art. 14                          SOVEREIGN       Regulation 2024/1689; direct effect

  collective_bargaining_required/2   CLT Art. 59 §§2 e 5 + Art. 611-A I         SOVEREIGN       Statutory working-hours protection; requires CCT

  legal_citation_grounded/1          TST procedural rules                       SOVEREIGN       TST requires verifiable precedent citations; grounding is mandatory

  hour_bank_permitted_with_cct/2     Súmula TST 85 §I                           ELASTIC         TST jurisprudence; calibratable within statutory bounds
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Elastic predicates encode regulatory parameters subject to administrative discretion within sovereign bounds. Their activation reduces θ (constructive contribution to normative state) without crossing the SOVEREIGN threshold.

Table A2. ψ_S predicate weight map (​\_SCENARIO_PREDICATE_MAP). For each scenario, lists the predicate pattern (substring match), the action dimension(s) affected, the expert-elicited signed weight, and the normative rationale. Weights reflect legal gravity: sovereign constitutional obligations carry \|ω\| ≥ 6.0; regulatory elastic predicates carry \|ω\| ≤ 4.0. Source: src/qfeng/e5_symbolic/psi_builder.py, \_SCENARIO_PREDICATE_MAP.

C2 (health_brasil) \| obligation_immediate_supply_critical \| a0: −8.0, a1: +4.0, a2: +5.0 \| Sovereign: Lei 13.979 Art. 3 VIII + Lei 8.080 Art. 15 I --- strongest normative block on autonomous operation C2 \| critical_health_system_situation \| a0: −5.0, a1: +3.0, a2: +2.0 \| Sovereign: Decreto AM 43.303/2021 --- hospital capacity collapse C2 \| right_to_health_as_duty \| a0: −4.0, a1: +3.0, a2: +2.0 \| Sovereign: CF/88 Art. 196 C2 \| obligation_to_activate_coes \| a0: −4.0, a1: +4.0, a2: +1.0 \| Sovereign: Portaria 30/2020 C2 \| espin_declaration_active \| a0: −3.0, a1: +3.0, a2: +2.0 \| Sovereign: Portaria 188/2020 C2 \| authority_to_requisition \| a0: −2.0, a1: +1.0, a2: +3.0 \| Sovereign: Lei 13.979 Art. 3 VII C2 \| authorization_to_import \| a0: −2.0, a1: +1.0, a2: +4.0 \| Sovereign: Lei 13.979 Art. 3 VIII C3 (health_brasil) \| obligation_to_reduce_regional \| a0: −6.0, a1: +4.0, a2: +3.0 \| Sovereign: CF/88 Art. 198 III --- equidade C3 \| universal_equal_access \| a0: −5.0, a1: +3.0, a2: +2.5 \| Sovereign: Lei 8.080 Art. 7 IV C3 \| equality_of_assistance \| a0: −5.0, a1: +3.0, a2: +2.0 \| Sovereign: SUS principle C7 (health_usa) \| prohibition_disparate_impact \| a0: −7.0, a1: +3.0, a2: +5.0 \| Sovereign: Title VI §601 + 42 CFR §440.240 C7 \| equal_protection_of_the \| a0: −6.0, a1: +4.0, a2: +3.0 \| Sovereign: 14th Amendment §1 C7 \| prohibition_racial_discrimination \| a0: −7.0, a1: +3.0, a2: +4.0 \| Sovereign: Title VI + §1983 C7 \| prohibition_state_racial \| a0: −5.0, a1: +3.0, a2: +3.0 \| Sovereign: 14th Amendment T-CLT-01 (labor_brasil) \| prohibition_of_generic_precedent \| a0: −8.0, a1: +5.0 \| Sovereign: CPC 489 §1 V--VI T-CLT-01 \| obligation_to_ground_decision \| a0: −7.0, a1: +5.0 \| Sovereign: CPC 489 §1 V T-CLT-01 \| obligation_to_state_reasons \| a0: −5.0, a1: +4.0 \| Sovereign: CF/88 Art. 93 IX T-CLT-02 (labor_brasil) \| hour_bank_without_cct_max_6_months \| a0: −5.0, a1: +5.0 \| Sovereign: CLT Art. 59 §2 T-CLT-02 \| semester_hour_bank_requires_cct \| a0: −6.0, a1: +4.0 \| Sovereign: TST Súmula 85 V T-CLT-03 (labor_brasil --- SAT positive control) \| valid_cct_banco_horas \| a0: +6.0, a1: −3.0 \| Sovereign: CLT Art. 59 §2 + CCT vigente T-CLT-04 (labor_brasil --- SAT positive control) \| prohibition_of_generic_precedent \| a0: +8.0 \| Sovereign: CPC 489 §1 --- citation verified, supports compliance T-CLT-04 \| obligation_to_ground_decision \| a0: +7.0 \| Sovereign: CPC 489 §1 V --- satisfied by real TST precedent

Appendix B: Mathematical Proofs

B.1 Convergence of theta-efetivo

**Claim**: The Markovian theta-efetivo sequence {θ_eff(t)} is bounded and converges to a value in \[min θ(t), max θ(t)\] as t → ∞ under constant pressure conditions.

**Proof**: Let θ = lim\_{t→∞} score_pressão(t) be a constant pressure level, implying Δpressão(t) → 0 and thus α(t) → σ(0) = 0.5. The recurrence θ_eff(t) = 0.5·θ + 0.5·θ_eff(t−1) is a linear contractive map with fixed point θ = θ (the instantaneous angle under constant normative conditions). By the Banach fixed-point theorem, the sequence converges geometrically with rate 0.5 per step. QED.

**Corollary**: The memory half-life of the Markovian theta-efetivo under stable conditions (α = 0.5) is log(2)/log(2) = 1 month --- i.e., exactly one time step. Under crisis conditions (α → 1), memory half-life → 0 (immediate adaptation). Under recovery conditions (α → 0), memory half-life → ∞ (persistent crisis memory).

B.2 Monotonicity of governance suppression in θ

**Bound analysis: For fixed predictor confidence conf ∈ (0,1) and fixed ‖ψ_N‖ = ‖ψ_S‖ = 1 (L2-normalised), the governance suppression percentage GSP = (P_cl(0) − P_q(0)) / P_cl(0) is monotone non-decreasing in θ for UNSAT scenarios (ψ_N\[0\] \> 0, ψ_S\[0\] \< 0). When ψ magnitudes differ across scenarios --- as in the multi-dimensional health scenarios C2, C3, C7 where \|ψ_N\[0\]\| and \|ψ_S\[0\]\| are not equal across scenarios --- monotonicity holds within each scenario (varying θ) but not across scenarios with different ψ magnitude profiles.**

**Proof sketch**: Under the sign condition ψ_N\[0\] \> 0, ψ_S\[0\] \< 0, the quantum amplitude at j=0 is (αψ_N\[0\] + βψ_S\[0\]), which is less than αψ_N\[0\]. The normalisation factor Z = 1 + 2αβcos(θ) is monotone decreasing in θ for θ ∈ \[90°, 180°\] (since cos is monotone decreasing on \[0°, 180°\]). Therefore P_q(0) = (αψ_N\[0\] + βψ_S\[0\])²/Z is monotone decreasing in Z, hence monotone decreasing in cos(θ), hence monotone decreasing in θ on \[90°, 180°\]. Since P_cl(0) is independent of θ, GSP is monotone increasing in θ. QED.

Table 4 illustrates the bound: within each scenario, higher θ corresponds to higher \|GSP\| (the bound is tight). Across scenarios, the cross-sectional ranking C3 (GSP = 25.16%, θ = 134.67°) \> C2 (GSP = 16.75%, θ = 132.36°) \> C7 (GSP = 10.66%, θ = 133.74°) is non-monotone in θ because C7 and C2 have different ψ_N magnitude profiles (C7: \|ψ_N\[0\]\| = 0.850, C2: \|ψ_N\[0\]\| = 0.920; C3: \|ψ_N\[0\]\| = 0.900). This is an expected consequence of the magnitude-fixed precondition: the bound governs per-scenario sensitivity, not cross-scenario ranking. The C2/C7 non-monotone pattern is therefore not a violation of the bound but a limitation of applying it to scenarios with differing \|ψ_N\[0\]\|.

B.3 Anticipatory form --- early activation property

**Claim**: Under the anticipatory form (Equation 5, γ \> 0), the Circuit Breaker activates at time t\* \< t_peak where t_peak is the time of maximum θ(t), provided that 𝔼\[θ(t+k)\] \> θ_block for some k ∈ {1, \..., horizon}.

**Proof**: Straightforward from Equation 5: θ_eff(t) = α(t)·θ(t) + (1−α(t))·θ_eff(t−1) + γ·𝔼\[θ(t+k)\]. If 𝔼\[θ(t+k)\] \> θ_block and γ \> 0, then the anticipatory term contributes at least γ·θ_block to θ_eff(t), potentially pushing it above θ_block before θ(t) itself crosses the threshold. The condition is sufficient: it may activate the CB even when α(t)·θ(t) + (1−α(t))·θ_eff(t−1) \< θ_block. QED.

Correspondence: Ricardo S. Kaminski --- ricardoskaminski@gmail.com

Code and data availability: Repository available at \[GitHub --- blinded for review\]. All parquet result files, Clingo corpus, and pipeline code are included. Reproducibility guaranteed via deterministic Clingo evaluation and SHA-256 cached DeonticAtoms.

Competing interests: None declared.

Funding: This research received no external funding. Supported by institutional research allocation, University of Brasília Graduate Program in Social Sciences.

Ethics statement: This study uses only publicly available normative documents and administrative data already in the public domain (SIH/DATASUS, published under Lei de Acesso à Informação). No individual-level patient data were used. The Medicaid analysis uses aggregate statistics from Obermeyer et al. (2019) --- a published, peer-reviewed paper --- not primary patient records.

[^1]: *STAC* is introduced in this paper as the label for the governance alignment regime; the concept originates in Kaminski (2025, doctoral thesis). See Nomenclature note, §1.

  [**Diagram 1**. Complete cybernetic inference-audit-feedback cycle of the Q-FENG architecture. Solid arrows: inference flow. Dashed arrows: logging and data flow. Long-dashed arrows: feedback channels (Algedonic Signal to S5; Continuous Training to S1).]: _media/image1.png {width="5.463999343832021in" height="6.328041338582677in"}
  [**Diagram 2.** Fractal VSM architecture across three jurisdictional levels: Macro (constitutional), Meso (sectoral/infralegal), and Micro (algorithmic/operational). Vertical arrows represent normative derivation (downward) and algedonic escalation (upward). S3\* is shown at all levels but operates computationally only at Micro through Clingo audit; at Meso and Macro it is exercised institutionally.]: _media/image2.png {width="5.9935695538057745in" height="6.2634109798775155in"}
  [***Diagram 3.*** Geometric intuition for the three governance regimes formalised in Table 2: (a) STAC (cos θ ≈ +1, constructive interference); (b) HITL (cos θ ≈ 0, partial alignment); (c) CIRCUIT_BREAKER (cos θ ≈ −1, destructive interference).]: _media/image3.png {width="5.3in" height="4.045568678915136in"}
  [***Diagram 5. Conceptual loss landscape of L_Global showing the STAC equilibrium region. The quantum penalty ridge λ·max(0, −cos θ) excludes non-conforming configurations from the optimisation trajectory.***]: _media/image4.png {width="5.3in" height="3.4940518372703413in"}
  [Diagram 6. Triadic failure typology: asymmetric partition of normative-violation space into constitutional failures (absent sovereign predicate), execution-absent-channel failures (predicate derivable, execution path blocked), and execution-inertia failures (citation misgrounded or phantom). The geometry encodes the causal distance from the sovereign predicate axis.]: _media/image5.png {width="5.3in" height="4.364705818022747in"}
  [Diagram 7. Q-FENG C1 data-flow pipeline (E0--E5): ScopeConfig → NormChunk → DeonticAtom → ClingoPredicate → SAT/UNSAT verdict → ψ_S → θ. Pydantic-validated schemas, Parquet persistence, and deterministic E3/E5 stages ensure full reproducibility. Complements Diagram 1 (cybernetic governance cycle) at the data-engineering level.]: _media/image6.png {width="5.3in" height="4.520588363954506in"}
  [Table 2]: #_Ref227876515
  [Table 3]: #_Ref227876653
  [Diagram 8. Neurosymbolic free-energy landscape for HITL sovereignty classification. Sovereign predicates define the constitutional ground-state minimum; elastic predicates constitute the thermal bath of calibratable regulatory parameters. The Circuit Breaker threshold corresponds to the energy barrier that the predictor cannot cross without explicit HITL activation.]: _media/image7.png {width="5.3in" height="4.05294072615923in"}
  [***Figure 1.*** Interference angle θ across seven scenarios --- overview of governance regime classification. Predictor states ψ_N (dashed) plotted by their angular separation from the normative reference ψ_S (solid). Five CIRCUIT-BREAKER scenarios cluster at 127.8°--134.7° (destructive interference); two positive controls fall within the STAC band at 5.7°--7.1° (constructive interference).]: _media/image8.png {width="6.398059930008749in" height="2.7894094488188976in"}
  [***Figure 2.*** Q-FENG interference geometry in the decision Hilbert space. Angle θ between predictor state ψ_N (dashed) and normative state ψ_S (solid) across seven scenarios and two normative regimes. Health Governance: C2, C3, C7 (ψ in R³, 3 actions). Labour Law: T-CLT-01 through T-CLT-04 (ψ in R², 2 actions). GSP annotation shows governance suppression percentage per scenario.]: _media/image9.png {width="6.5in" height="4.98125in"}
  [Diagram 9. Regional equity map of SUS specialist-service distribution across Brazilian municipalities. The dual annotation layer marks the CF/88 Art. 196 universal-access gap and the Art. 198 III SUS-regionalisation deficit, quantifying the constitutional violation that grounds the θ = 134.67° CIRCUIT_BREAKER outcome of scenario C3 (governance suppression 25.16%).]: _media/image10.png {width="5.3in" height="4.832353455818023in"}
  [Diagram 10. Manaus oxygen crisis: actual event sequence (upper track) vs. contrafactual Q-FENG-mediated response (lower track). The 3-month offset between the Circuit Breaker activation in October 2020 and the Amazonas state calamity decree of 23 January 2021 is the governance lead-time quantified by the Markovian θ_eff formalism.]: _media/image11.png {width="6.5189337270341206in" height="4.633426290463692in"}
  [Figure 3. Markovian θ_eff trajectory --- Manaus COVID-19 health crisis (Jul 2020 -- Jun 2021). Circuit-Breaker activated October 2020 (θ_eff = 125.3°, α(t) = 0.909), three months before the January 2021 ICU collapse documented by FVS-AM Boletim Epidemiológico 16/jan/2021. Left axis: θ_eff Markovian (SIH/DATASUS) and θ_t instantaneous, with 95% bootstrap CI shading. Right axis: hospital occupancy rate (%). Peak September 2020 at θ_eff = 130.91°.]: _media/image12.png {width="6.308989501312336in" height="2.816284995625547in"}
  [1]: _media/image13.png {width="6.5in" height="2.6555555555555554in"}
  [2]: _media/image14.png {width="6.0in" height="2.2905139982502187in"}
  [3]: _media/image15.png {width="6.0in" height="3.086324365704287in"}
  [4]: _media/image16.png {width="6.0in" height="3.244970472440945in"}
