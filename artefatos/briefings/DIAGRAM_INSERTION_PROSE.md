# Prose de Conexão — Inserção de Diagramas no Paper JURIX Q-FENG

Cada bloco abaixo é o parágrafo de transição que entra DEPOIS do parágrafo-âncora
e ANTES do Diagram correspondente.

---

## INS-1 (antes de Diagram 1 — âncora: "This paper presents the Q-FENG C1 pipeline")

The complete Q-FENG cybernetic cycle is illustrated in Diagram 1. Three distinct flows
are encoded: solid inference arrows trace the signal from the algorithmic predictor
(VSM System 1) through the five-stage neurosymbolic pipeline (E0–E5) to the
governance decision output; dashed logging channels feed observational data back
through System 2 and System 3 (audit and control layers); and long-dashed algedonic
feedback arrows carry Circuit Breaker activations directly to the policy-setting layer
(System 5) and continuous retraining signals to System 1. This architecture ensures
that governance failures detected at the normative evaluation stage propagate upstream
to reshape both operational decisions and institutional policy.

---

## INS-2 (antes de Diagram 2 — âncora: "Mapping the full Q-FENG C1 architecture to the VSM systems")

Diagram 2 makes the scale-invariant fractal property concrete. The same S1–S5 Viable
System Model structure recurs simultaneously at three governance levels: the
constitutional and regulatory level (Macro), the agency-operational level (Meso), and
the deployment-unit level (Micro). At each scale, Q-FENG occupies the System 3–System 4
interface — the observational and anticipatory intelligence layer that Beer's original
cybernetic model required but did not provide a computational specification for. The
fractal recursion implies that a Circuit Breaker activation at the deployment level
(Micro) propagates structurally equivalent algedonic signals up to the agency (Meso)
and constitutional (Macro) levels, enabling multi-scale governance co-ordination from
a single formal evaluation mechanism.

---

## INS-3 (antes de Diagram 3 — âncora: parágrafo antes de Table 1)

Diagram 3 provides geometric intuition for the three interference regimes before the
formal partition in Table 1 below. In the unit-sphere decision space defined by the
Hilbert inner product ⟨ψ_N | ψ_S⟩, three canonical configurations arise: (a) STAC,
where ψ_N and ψ_S are nearly co-directional (cos θ ≈ +1), so the quantum superposition
amplifies the preferred action above the classical Bayesian mixture — constructive
interference; (b) HITL, where the vectors are approximately orthogonal (cos θ ≈ 0),
yielding intermediate normative friction and a governance signal that warrants human
review; and (c) CIRCUIT_BREAKER, where ψ_N and ψ_S point in opposing directions
(cos θ ≈ −1), generating maximally destructive interference that renders the preferred
predictor action normatively inadmissible.

---

## INS-4 (antes de Diagram 4 — âncora: "when L exceeds the CB threshold, mandatory intervention is activated")

Diagram 4 illustrates the topology of L_Global as a loss landscape over the
policy-action space. The quantum penalty ridge λ·max(0, −cos θ) rises steeply as θ
approaches 180°, creating a potential barrier that excludes configurations with severe
normative misalignment from the predictor's optimisation trajectory. The STAC
equilibrium basin at the centre of the landscape corresponds to the region of
governance compliance; the HITL boundary marks the point at which the gradient of L
exceeds the threshold for autonomous operation; and the Circuit Breaker wall at the
ridge marks the mandatory intervention boundary. The landscape is therefore not merely
a performance metric but a normative topography: the governance architecture imposes
the shape of the space within which the predictor may operate.

---

## INS-5 (antes de Diagram 5 — âncora: parágrafo imediatamente antes de "Three features of this series are theoretically significant")

The twelve-month sequence from July 2020 to June 2021 is reconstructed in Diagram 5 as
a two-track comparative timeline. The upper track documents the actual event sequence:
the first anomalous ICU occupancy readings in July 2020 (30% but abnormally early for
the seasonal pattern), the oxygen supply collapse of January 2021, and the Decreto AM
43.303/2021 calamity declaration of 23 January — the first binding governance response
issued three months after θ_eff had already exceeded 120°. The lower track shows the
contrafactual Q-FENG-mediated response: the Markovian θ_eff formalism activates the
Circuit Breaker in October 2020, enabling preventive federal supply-chain intervention
and COES activation before the crisis became irreversible. The 3-month governance
lead-time quantified in this diagram is the central empirical claim of the time-series
analysis and the primary justification for the Markovian extension of the interference
angle formalism.

---

## INS-6 (antes de Diagram 6 — âncora: ultimo paragrafo de §3.5 Failure Typology)

The failure typology formalised above maps onto a geometric structure visualised in
Diagram 6. Three asymmetric regions partition the normative space according to the
presence or absence of two independent elements: the sovereign predicate and the
execution chain. Constitutional failures arise when both sovereign predicate and
execution chain are absent from the active corpus — a structural gap that cannot be
resolved by operational intervention alone and requires legislative or constitutional
remediation. Execution-absent-channel failures occur when the sovereign predicate is
derivable but no enabling condition instantiates it in the current execution context;
the governance infrastructure exists normatively but is inoperative at the deployment
layer. Execution-inertia failures arise when the citation chain is hallucinated or
misgrounded, collapsing the execution path at the predicate-derivation step regardless
of the sovereign predicate's presence. The triadic geometry makes the asymmetric causal
structure of normative violation legible as spatial distance from the sovereign predicate
axis — a visualisation of the third original contribution of this paper.

---

## INS-7 (antes de Diagram 7 — âncora: primeiro paragrafo de §4, antes de E0)

The computational architecture of the C1 pipeline is illustrated in Diagram 7 as a
concrete data-flow graph from raw normative input to interference-angle output. Each
stage produces a typed, Pydantic-validated artefact persisted to Parquet: E0 produces
a ScopeConfig object parameterising the normative domain; E1 emits NormChunks carrying
hierarchical provenance metadata; E2 extracts DeonticAtoms via few-shot LLM inference;
E3 translates atoms deterministically to Clingo predicates via Jinja2 templates; E4
classifies predicates as SOVEREIGN or ELASTIC through HITL review; and E5 executes
the Clingo ASP solver to derive SAT/UNSAT status and construct the normative state
vector ψ_S, from which the interference angle θ is computed. The determinism
guarantee — critical for reproducibility — is enforced at E3 (template-based
translation, no LLM stochasticity) and E5 (Clingo --seed=1 fixed). This diagram
complements Diagram 1, which shows the cybernetic governance cycle at an architectural
level; Diagram 7 exposes the underlying data engineering that makes that cycle
computationally executable.

---

## INS-8 (antes de Diagram 8 — âncora: final do paragrafo SOVEREIGN/ELASTIC em §4.4 E4)

The thermodynamic analogy that motivates the SOVEREIGN/ELASTIC classification is
rendered explicit in Diagram 8. The diagram frames the normative state space as a
free-energy landscape: sovereign predicates define the ground-state energy minimum —
the constitutionally mandated configuration that the governance system must attain —
while elastic predicates constitute the thermal bath of regulatorily calibratable
parameters whose values can fluctuate within statutory bounds without triggering
normative violation. The HITL review process, in this metaphor, determines the local
potential energy of each predicate: a SOVEREIGN classification raises a high-energy
barrier that the predictor cannot cross without explicit Circuit Breaker activation;
an ELASTIC classification contributes low-gradient energy, admitting operational
variation. The neurosymbolic interface — where LLM-extracted DeonticAtoms meet
Clingo's formal constraint-satisfaction — is the measurement apparatus that collapses
the superposition of possible sovereignty assignments into a definite, auditable
classification.

---

## INS-9 (antes de Diagram 9 — âncora: primeiro paragrafo de C3 em §5.2)

The regional concentration pattern that defines scenario C3 is visualised as an equity
map in Diagram 9. The map encodes the distribution of SUS specialist services across
Brazilian municipalities plotted against the population distribution, revealing the
structural mismatch between geographic availability and demographic need: metropolitan
regions — São Paulo, Rio de Janeiro, Belo Horizonte, Manaus — accumulate the majority
of high-complexity services (oncology, cardiac surgery, advanced imaging) while the 46%
of Brazilians residing in municipalities with fewer than 50,000 inhabitants are served
predominantly by primary-care units. The dual constitutional grounding of this violation
is reflected in the map's dual annotation layer: the CF/88 Art. 196 layer marks the
universal access gap, measuring the distance between available specialist capacity and
the constitutionally mandated universal and equal access standard; the Art. 198 III
layer identifies the SUS regionalisation deficit, quantifying the failure to distribute
services according to epidemiological need rather than administrative convenience. The
spatial representation makes the magnitude of the 25.16% governance suppression
intuitively legible as geographic distance from constitutional compliance.

---

## INS-10 (antes de Diagram 10 — nota: esta eh Diagram 5 atual ja inserida, apenas referencia)

[Esta entrada eh reservada para consistencia numerica. Diagram 10 (Manaus Timeline) nao
requer novo paragrafo de prosa pois ja possui conexao escrita como INS-5. A renumeracao
5 -> 10 eh aplicada pelo script de insercao nos textos existentes.]

---
