# Inserções de novas seções no PAPER1_CANONICO.md

> ⚠️ **Atualizado em 27/abr/2026 — Opção 2 implementada.** Série truncada em SE 14/2020 (n=70). Ver `_addendum_OPCAO2_truncamento_serie.md`.

**Documento de redação editorial pronta para inserção direta no canônico após conclusão da Frente 2 (Adversarial CLT).**

**Workspace:** `C:\Workspace\academico\qfeng_validacao\docs\papers\paper1\PAPER1_CANONICO.md`
**Branch:** `caminho2`  ·  **Data de produção:** 27 de abril de 2026
**Status:** ✓ Pronto para inserção  ·  Aguardando: conclusão Frente 2 + integração resultados Frente 1

---

## Objetivo deste documento

Este documento contém a redação acadêmica densa, em registro compatível com o canônico atual, das novas seções a serem inseridas no `PAPER1_CANONICO.md` para neutralizar a primeira objeção previsível de qualquer revisor JURIX/AI&Law/JAIR ou banca CEREBRA-AI/UGR: *"por que não usar simplesmente um BI com alertas de TOH?"*

A inserção responde a três questões editoriais críticas:

1. **Q-FENG não é um BI mais sofisticado.** É camada arquitetônica nova, com propriedades não preenchidas por dashboards, NeSy 1.0 ou Constitutional AI.
2. **A arquitetura é agnóstica de domínio.** Saúde, educação, trabalho, governança privada — mesma matemática, corpus parametrizável.
3. **A arquitetura é agnóstica de stack ML.** LightGBM, séries temporais, LLM, redes neurais profundas — superposição aditiva ψ_N + ψ_S sem requisito de diferenciabilidade fim-a-fim.

A redação é estruturada em três blocos distintos, com instruções de inserção precisas para cada um.

---

# BLOCO A — Nova subseção em §1 (Introduction)

**Localização canônica:** após o parágrafo final da §1, antes da §2 *Related Work* (linha ~58 atual).

**Justificativa de posicionamento:** a §1 atual estabelece o problema (Fricção Ontológica em sistemas de governança de IA) e o argumento central (Q-FENG como arquitetura). Faltava sinalizar, ainda na introdução, *por que* o problema não é resolvido por instrumentos de monitoramento já consolidados — i.e., por que o leitor deve continuar lendo após a §1. A nova subseção responde a esta questão antes que ela seja levantada pelo revisor.

**Título proposto:** `### Why not a BI dashboard? Architectural distinction.`

---

## Texto proposto para inserção (Bloco A)

### Why not a BI dashboard? Architectural distinction.

A reasonable first objection to a framework as elaborate as Q-FENG is that operational monitoring of public health systems is already a solved problem. Business intelligence dashboards (Power BI, Tableau, Qlik, Grafana) and domain-specific platforms (DEMAS-VEPI, InfoGripe in Brazil; the European Centre for Disease Prevention and Control's ECDC-COVID dashboard; the US Department of Health and Human Services' HHS Protect platform) provide near-real-time monitoring of bed occupancy, mortality, and respiratory load with threshold-based alerts. Why not simply add a column to such a dashboard?

The answer is that BI dashboards are *descriptive operational instruments* and Q-FENG is a *prescriptive normative-governance instrument*. The two operate at different architectural levels. A dashboard tells the manager *what* is happening (bed occupancy at 95%); Q-FENG tells the manager *which constitutional and statutory obligations are being violated*, *which provisions of which law authorize and require which institutional response*, and *which juridically sustainable justification* the manager can present to a Federal Audit Court (TCU), Public Prosecutor's Office (MP) or Parliamentary Inquiry Commission (CPI) months later. Three structural differences make this distinction non-trivial.

First, BI dashboards are *blind to ontological friction by construction*. A dashboard operating on the Brazilian National Health Establishment Registry (CNES) denominator for Manaus would have shown a permanent red alert from July 2020 onward, but the alert would not have explained that the actual operational denominator was 612 beds (the State Health Surveillance Foundation FVS-AM figure) rather than the 319 beds officially registered in the federal system. A dashboard operating on the FVS-AM denominator would have shown 103.69% occupancy in January 2021 — a number perceived as "near limit, under control" by managers familiar with the metric. Neither dashboard captures that *the gap between the two denominators is itself the institutional fact that matters*: it is the operational manifestation of the regulatory mismatch between federal categorical representation and state operational reality. Section 5 documents this mismatch as the empirical decomposition of *ontological friction* into four auditable layers, of which the most editorially significant — the formal creation of a CNES code (LSVP, code 96) explicitly intended to name the phenomenon and its non-adoption in 23 of 24 monthly observations of Manaus 2020-2021 — would be invisible to any threshold-based monitoring system.

Second, BI dashboards are *normatively silent*. When a public manager in Manaus authorizes R$ 30 million for emergency air transport of patients to other states in January 2021, the manager is exercising discretionary administrative power that requires juridical foundation. A dashboard alert reading "ICU occupancy 191% — red zone" is operationally meaningful but provides no fundamentation for the resource allocation decision. Q-FENG, by contrast, in the same operational moment exposes the active set of Clingo predicates derived from Federal Constitution Articles 1°(III), 3°(III), 5°, 196 and 198, from Lei 8.080/SUS Articles 7°(I)(II)(IV) and 43, and from Decreto AM 43.269/2021, with the satisfiability state of the predicate set against the proposed action and the deontic chain that justifies (or precludes) the decision. This is not metaphor: the predicate set is a directly auditable artifact, machine-checkable and human-readable, that constitutes juridically sustainable foundation for the manager's decision.

Third, BI dashboards are *synchronous with manifestation*. A threshold-based alert on TOH fires when TOH crosses the threshold. Q-FENG fires when the *composite angle θ between the predictor's vector and the normative state* exceeds the regime threshold, where the composite captures TOH, mortality, respiratory load, SRAG cases, and the Markovian memory of the system's own trajectory (Equation A10). The composite is *intrinsically multidimensional* and incorporates anticipation that no single threshold can produce. The empirical demonstration in Section 5.3 shows that, in the Manaus 2020-2021 series, Q-FENG entered a sustained CIRCUIT_BREAKER regime in epidemiological week 37 of 2020 — 19 weeks before the formal recognition of public calamity by the state regulatory apparatus (Decree AM 43.269/2021, EW 03/2021). A TOH-based dashboard at standard public-health calibration would have signaled red only in EW 02/2021, when oxygen was already running out. The 19-week interval is not a marginal improvement: it corresponds to the time required for federal emergency procurement, budget redirection, transportation logistics, and inter-state bed solidarity activation.

The architectural distinction admits a precise positioning. BI dashboards operate at the operational level of observation; Q-FENG operates at the *meta-operational level of measuring tension between observation and normative expectation*. The two are not competitors. Q-FENG can in principle be deployed as a *governance sidecar* over any existing BI infrastructure: ingest the dashboard's raw indicators as ψ_N, execute the Clingo corpus over the relevant normative domain to derive ψ_S, and expose θ as an additional governance signal alongside the dashboard's existing alerts. The framework is architecturally additive, not substitutive.

The remainder of the paper develops this argument formally and validates it empirically. Section 3 establishes the mathematical foundation of the framework. Sections 4 and 5 document the C1 pipeline and the seven-scenario validation. Section 7.X (the new subsection introduced in this revision) addresses two further architectural properties — *domain-agnostic* operation across health, education, labour and private-sector governance corpora, and *ML-stack-agnostic* operation across LightGBM, time-series, LLM and deep-network predictors — that distinguish Q-FENG from prior NeSy and from training-time alignment frameworks.

---

# BLOCO B — Nova subseção em §7 (Discussion), antes de §7.4 Limitations

**Localização canônica:** após §7.3 *Human-in-the-Loop as Epistemic Necessity* (linha ~1041 atual), antes de §7.4 *Limitations* (linha 1042 atual).

**Justificativa de posicionamento:** a §7 atual discute as implicações teóricas (§7.1, §7.2, §7.3). Faltava elaborar as duas propriedades arquitetônicas mais subexploradas no canônico — **agnosticismo de domínio** e **agnosticismo de stack ML** — que são, junto com a posição como sidecar de runtime governance, os diferenciais editoriais mais relevantes face à literatura NeSy 1.0 e a frameworks como Constitutional AI. A inserção em §7 (em vez de §1) é deliberada: estes pontos exigem o leitor ter percorrido §3 (matemática) e §5 (validação) para serem compreendidos em profundidade.

**Numeração proposta:** §7.4 (renumerando §7.4 atual *Limitations* → §7.5 e §7.5 atual *Publication Ecosystem* → §7.6).

**Título proposto:** `7.4 Architectural Generality: Domain-Agnostic and ML-Stack-Agnostic Operation`

---

## Texto proposto para inserção (Bloco B)

## 7.4 Architectural Generality: Domain-Agnostic and ML-Stack-Agnostic Operation

The Manaus validation in Section 5.3 and the labour-track CLT scenarios in Sections 5.4–5.5 provide concrete instantiations of the Q-FENG framework in two distinct normative domains and over distinct predictor architectures. We now elaborate the architectural generality that those instantiations exemplify but do not exhaust. Two properties of the framework deserve explicit reivindication, both because they are subextracted in prior NeSy literature and because they constitute the most consequential differences between Q-FENG and competing approaches to AI governance.

### 7.4.1 Domain-agnostic operation: same mathematics, parameterizable corpus

The mathematical core of the framework — the Hilbert space construction of Section 3.1, the Born-rule probability of Section 3.3, the Markovian θ_efetivo of Section 3.2, and the alhedonic loss of Section 3.4 — is *invariant across normative domains*. The framework instantiation for a specific domain requires two parameterizations: (i) the Clingo corpus encoding the domain's normative structure into sovereign and elastic predicates with the appropriate fractal-derivational stack (constitutional → statutory → regulatory → operational levels); (ii) the calibration of ψ_N in the predictor space relevant to the domain. The mathematical invariants — superposition, interference geometry, regime classification thresholds — are not domain-specific.

This property has direct implications for application beyond public health. Three concrete cases illustrate the generality. In **education governance**, Q-FENG can monitor municipal-level dropout, repetition and age-grade distortion against the constitutional obligation of mandatory basic education (CF/88 Article 208(I)), the Statute of the Child and Adolescent (Lei 8.069/1990 Article 53), and the Law of National Education Guidelines (Lei 9.394/1996 Article 4). When the composite pressure indicator triggers θ_efetivo > 120°, the framework activates predicates corresponding to violation of the *direito subjetivo público* to education, providing juridical foundation for intervention by the Public Prosecutor's Office (MPE), the Guardianship Council, or the Federal Court System under the constitutional individual right to education guaranteed by CF/88 Article 208 §1. The same VSM mapping (S1 = local school operation; S3 = municipal regulator; S4 = state secretariat; S5 = constitutional sovereignty hierarchy) holds without modification.

In **private-sector AI governance under LGPD and the EU AI Act**, Q-FENG can serve as a runtime auditor of model decisions. ψ_N is the output of the production model (a credit-scoring decision, a content-moderation classification, a hiring-screening rank); ψ_S is the predicate set derived from the company's Data Protection Impact Assessment, AI Impact Assessment, and the relevant LGPD legal bases (Article 7 for personal data; Article 11 for sensitive data) and AI Act explainability obligations (Article 13). When θ enters CIRCUIT_BREAKER, the framework triggers automatic suspension or human review of the decision, with auditable foundation in the active predicate set. This is functionally equivalent to a "constitutional layer" for the production AI system, but operating at runtime rather than at training time, and with the company's specific normative obligations (rather than a generic constitutional rule set) as ψ_S.

In **labour governance under CLT**, the application demonstrated in Section 5.4 (T-CLT-01 through T-CLT-04) shows that the framework operates over a fundamentally different normative corpus from public health, with different constitutional anchors (CF/88 Article 7 instead of Article 196), different statutory framework (CLT Articles 58, 59, 71, 477 instead of Lei 8.080/SUS), and different operational predicates (hour-bank validity, phantom-citation, reasoning-grounding instead of ICU bed availability). The mathematical framework absorbs the domain change without modification.

The architectural property that enables this generality is the **separation of concerns between mathematics and corpus**: the matrix of theta calculations does not need to "know" what the predicates mean; it only needs to know which predicates are active in which scenario. The Clingo corpus encodes domain knowledge; the Hilbert-space machinery encodes interference measurement; the two are coupled only through ψ_S construction (Section 4.5). This contrasts with approaches that fuse domain knowledge into the model's parametric structure (rule-based reasoning systems with hardcoded predicates) or that require co-training of neural and symbolic components (DeepProbLog, NeurASP, dPASP at training time): in those frameworks, domain change requires re-engineering or re-training. In Q-FENG, domain change requires only swapping the Clingo corpus.

### 7.4.2 ML-stack-agnostic operation: the additive superposition property

The second property of architectural generality is that Q-FENG operates over *any* predictor producing a coherent ψ_N vector, irrespective of the predictor's internal architecture. The seven scenarios validated in this paper instantiate this property over three distinct predictor families: gradient-boosted decision trees (LightGBM for C7 Obermeyer-style risk-score auditing), time-series structural models (the Manaus C2 series at monthly granularity in the prior canonical version, now extended to weekly via the bivariate loader), and rule-based deontic-extraction predictors (the CLT scenarios T-CLT-01 through T-CLT-04). The Frente 2 adversarial CLT experiment, in preparation as of this revision, will additionally exercise the framework over four locally-deployed large language models (Qwen 3 14B, Phi-4 14B, Gemma 3 12B, Llama 3.3 8B) running on consumer-grade GPU (RTX 3060 12GB Q4_K_M) via the Ollama runtime.

The property that enables this stack-agnostic operation is the *additive superposition* construction in the Hilbert space: ψ_N and ψ_S inhabit the same vector space, where the mode of construction of ψ_N (gradient descent, posterior sampling, autoregressive token generation, expert-system rule firing) is irrelevant to the angle θ between ψ_N and ψ_S. The framework requires only that ψ_N be expressible as a normalized vector in the same basis as ψ_S, and the construction of this vector from any predictor's output is a one-line projection.

Three architectural consequences follow. **First**, *no retraining is required when the normative corpus changes*. If the Clingo corpus is updated (a new Supreme Court decision, a new regulation, a new statutory provision), only ψ_S is recomputed; the predictor producing ψ_N remains untouched. This contrasts with NeSy 1.0 frameworks (DeepProbLog, NeurASP, dPASP) that fuse logical constraints into the differentiable computation graph, where corpus changes require retraining. **Second**, *no domain-specific fine-tuning of the predictor is required*. A LightGBM model trained for hospital occupancy prediction in São Paulo can be deployed in Manaus without retraining, provided the Clingo corpus reflects the local jurisdictional stack. The predictor encodes operational reality; the corpus encodes normative obligation; the framework measures tension between the two without forcing either to "know" the other. **Third**, *the symbolic layer is editable by jurists without ML engineering competency*. The Clingo corpus is plain ASP code. Domain experts (lawyers, public health specialists, education policy researchers) can audit and modify the predicate set directly, without requiring the ML team's participation. Conversely, the ML team can iterate on predictors without requiring legal-domain expertise. The architectural separation is enforced by the framework, not by team discipline.

This property has particular relevance for the deployment scenarios where Q-FENG is most likely to be useful in practice: large public organizations and private companies that *already have predictive systems in production* and need to add governance layers without disrupting existing infrastructure. The Q-FENG sidecar can be deployed as a microservice observing the production system's outputs (ψ_N) and producing governance signals (θ) without modifying the production system's code or retraining its models. This zero-disruptive deployment property is, to our knowledge, not available in any prior NeSy or AI-alignment framework.

### 7.4.3 Runtime governance vs. training-time alignment

The two properties above — domain agnosticism and stack agnosticism — together position Q-FENG in a distinct architectural quadrant from prior approaches to AI governance. We summarize the comparison in Table 7.4.1.

**Table 7.4.1.** Architectural positioning of Q-FENG relative to prior approaches.

| Approach | Operates at | Symbolic content | Coupling with predictor | Domain change requires |
|---|---|---|---|---|
| BI dashboards | Runtime (descriptive) | Threshold rules (numeric) | Loose (observation only) | Reconfiguration of thresholds |
| NeSy 1.0 (DeepProbLog, NeurASP, dPASP) | Training time | Logic programs in differentiable graph | Tight (co-training) | Retraining |
| Constitutional AI (Anthropic 2022) | Training time | Natural-language constitutional rules | Tight (RLHF-style) | Retraining |
| Rule-based expert systems | Runtime (prescriptive) | Hardcoded rules | Tight (rule engine = predictor) | Re-engineering |
| **Q-FENG (this paper)** | **Runtime (governance sidecar)** | **Clingo corpus over fractal-derivational stack** | **Loose (additive superposition)** | **Corpus swap** |

The framework occupies a distinct position: runtime governance with normatively rich symbolic content and loose coupling. None of the prior approaches simultaneously satisfy these three properties. NeSy 1.0 frameworks are tightly coupled (the logic is fused into the model); Constitutional AI operates at training time and uses natural-language rules without normative-derivational structure; expert systems lack the multidimensional θ measurement and the ψ_N/ψ_S superposition. The architectural difference is consequential for adoption: Q-FENG can be deployed over an existing AI system that the deploying organization does not control (a third-party vendor's classification API, for instance), provided the system's outputs can be projected to ψ_N — a condition that is satisfied by virtually any classification or regression API.

### 7.4.4 Implications for AI governance research and practice

The properties documented in this section have implications for both research and practice. For research, they suggest that a productive direction for the NeSy field is to develop frameworks that are *additive rather than substitutive* with respect to existing predictive infrastructure. The dominant paradigm in NeSy 1.0 (fuse logic into the model) is well-suited for novel models built specifically with logical constraints in mind, but is poorly suited for the deployment scenario most relevant to public-policy AI governance: legacy production systems that cannot be retrained or modified. Q-FENG illustrates that additive composition is feasible and produces interpretable governance signals.

For practice, the properties suggest a deployment pattern that we tentatively name *governance sidecar*: a microservice or function-as-a-service deployment that observes a production AI system's inputs and outputs, projects them to ψ_N, executes a Clingo program against the relevant normative corpus to derive ψ_S, computes θ, and emits governance signals (HITL alerts, CIRCUIT_BREAKER suspensions, audit log entries) without modifying the production system. This deployment pattern is architecturally compatible with the dominant patterns in cloud-native infrastructure (service mesh, distributed tracing) and can be incrementally adopted by organizations without disrupting existing pipelines. The Vetor de Correção Ontológica (Equation A4) provides the additional property that the sidecar can produce *suggestions for parameter rotation* (ψ_N adjustment) compatible with existing normative obligations, rather than forcing reform of the corpus itself — a property of particular relevance in jurisdictions where the legislative process is slow, captured, or paralyzed.

The Frente 2 experiment, currently in preparation, will provide the first empirical demonstration of the stack-agnostic property over four LLM predictor architectures from distinct families (Alibaba/Qwen, Microsoft/Phi, Google/Gemma, Meta/Llama). The experimental hypothesis is that the magnitude of the Q-FENG effect (D1 hallucination reduction, D2 coverage increase) is statistically independent of the LLM architecture — a hypothesis whose confirmation would constitute the strongest possible empirical evidence of architectural generality.

---

# BLOCO C — Nota suplementar em §7.4 (Limitations) — agora §7.5

**Localização canônica:** dentro da §7.5 *Limitations* (renumerada da §7.4 atual após inserção do Bloco B), como parágrafo adicional.

**Justificativa de posicionamento:** a §7.4 atual lista limitações da PoC. Após inserção do Bloco B (§7.4 nova), a antiga §7.4 passa a §7.5. Devemos acrescentar nesta seção uma menção honesta às limitações específicas das duas propriedades arquitetônicas reivindicadas, para evitar overclaim e para sinalizar agenda de validação futura.

---

## Texto proposto para inserção (Bloco C)

A reivindicação de generalidade arquitetônica formulada na §7.4 está sujeita a limitações empíricas que devemos explicitar. A propriedade de *agnosticismo de domínio* foi instanciada em duas áreas (saúde pública e direito do trabalho) e é apenas teoricamente suportada nas demais áreas mencionadas (educação, governança privada sob LGPD, mercado de capitais sob CVM/SEC). A confirmação empírica da generalidade depende de PoC adicional em cada domínio, com curadoria do corpus normativo correspondente e calibração específica de ψ_N. Esperamos abordar essas instanciações em trabalhos subsequentes, com prioridade para o domínio de educação (onde os dados IDEB e Censo Escolar fornecem séries temporais municipais comparáveis às séries SIH/DATASUS exploradas neste trabalho).

A propriedade de *agnosticismo de stack ML*, por sua vez, foi instanciada sobre três famílias de preditores no canônico atual (gradient-boosted trees, séries temporais estruturais, rule-based deontic extractors) e será estendida sobre quatro arquiteturas LLM distintas no experimento Frente 2 (Adversarial CLT). A generalidade plena para todas as arquiteturas de aprendizado de máquina é uma hipótese teórica sustentada pela superposição aditiva no espaço de Hilbert, mas a validação empírica para outras arquiteturas (transformer-based vision models, graph neural networks, diffusion models) permanece como trabalho futuro. A propriedade de *zero-disruptive sidecar deployment* foi articulada arquitetonicamente mas não foi demonstrada em ambiente de produção real; a demonstração desta propriedade requer parceria com organização operacional disposta a aceitar instrumentação Q-FENG sobre sistema de IA já em produção, e está sob negociação no contexto da agenda de pesquisa pós-doutoral discutida em §7.6 (renumerada de §7.5 atual).

---

# Sumário das alterações editoriais propostas

A inserção dos três blocos requer as seguintes alterações no `PAPER1_CANONICO.md`:

| Bloco | Localização atual no canônico | Localização proposta | Operação |
|---|---|---|---|
| A | Linha ~58 (entre §1 e §2) | Nova subseção `### Why not a BI dashboard?` em §1 | Inserção |
| B | Linha ~1042 (entre §7.3 e §7.4) | Nova §7.4 *Architectural Generality* | Inserção + renumeração |
| C | Linha ~1042 (em §7.4 atual *Limitations*) | Parágrafo adicional em §7.5 *Limitations* (renumerada) | Inserção parágrafo |

**Renumeração necessária após inserção do Bloco B:**

| Numeração atual | Nova numeração |
|---|---|
| §7.4 *Limitations* | §7.5 *Limitations* |
| §7.5 *Publication Ecosystem: Theoretical Book, Validation Paper, and Companion Summary* | §7.6 *Publication Ecosystem* |

**Cross-references a atualizar:**

A inserção dos novos blocos requer a atualização das referências cruzadas no canônico atual. As referências a §7.4 (atualmente apontando para *Limitations*) devem passar a apontar para §7.5; as referências a §7.5 (atualmente apontando para *Publication Ecosystem*) devem passar a apontar para §7.6. A varredura no canônico atual identifica as seguintes ocorrências:

- §1 menciona "(see §7.4)" três vezes — verificar se a referência continua sendo *Limitations* (passa a §7.5) ou se passa a apontar para a nova §7.4 *Architectural Generality*.
- §3 menciona "(cf. §7.4)" duas vezes — mesma análise.
- §4.5 menciona "(cf. §7.4 limitations)" uma vez — atualizar para §7.5.

Esta varredura deve ser executada como uma operação Claude Code dedicada (find-and-replace contextualizada) após a aprovação editorial do conteúdo dos três blocos por Ricardo.

---

# Notas finais

Este documento contém **apenas** a redação editorial pronta para inserção. A integração propriamente dita ao `PAPER1_CANONICO.md` e ao `PAPER1_QFENG_FINAL.docx` será executada como operação Claude Code dedicada (`PROMPT_CLAUDECODE_INTEGRACAO_NOVAS_SECOES_CANONICO.md`), a ser produzida após:

(i) aprovação editorial deste documento por Ricardo;
(ii) conclusão da Frente 2 (Adversarial CLT) e produção dos relatórios metodológico e de resultados correspondentes;
(iii) integração consolidada ao canônico em uma única passada editorial cuidadosa, em vez de inserções parciais sequenciais.

A motivação para diferir a integração é editorial: alterações incrementais ao canônico introduzem risco de inconsistências de cross-reference e de quebra de numeração de tabelas/figuras. A integração consolidada em janela única, executada após Frente 2 e revisada manualmente, mitiga este risco e produz uma única passagem auditável da versão atual à versão final.

A redação dos três blocos foi calibrada para o registro acadêmico denso do canônico atual, com terminologia consistente (Q-FENG, Fricção Ontológica, ψ_N, ψ_S, θ_efetivo, ψ_S construction, fractal-derivational stack, VSM mapping S1-S5+S3*) e com referências cruzadas internas explícitas que garantem coerência editorial. As tabelas (Tabela 7.4.1) e títulos de subseção foram numerados conforme a posição proposta; ajustes de numeração e formatação Markdown serão executados na operação de integração.

---

*Fim do documento de inserções.*
*Q-FENG Caminho 2 · Branch `caminho2` · Workspace `C:\Workspace\academico\qfeng_validacao\`*
*Autor: Ricardo da Silva Kaminski (ORCID: 0000-0002-8882-9248)*
*Pronto para integração ao canônico após conclusão da Frente 2 (Adversarial CLT).*
