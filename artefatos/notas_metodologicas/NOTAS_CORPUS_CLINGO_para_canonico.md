# Methodological Notes for Integration into PAPER1_CANONICO.md

**Date:** 26/Apr/2026
**Branch:** `caminho2` | **Audit commit:** `49808c4`
**Purpose:** Atomic snippets with target-section indication and complete diff, ready for application to `docs/papers/paper1/PAPER1_CANONICO.md` via Claude Code `edit_block`. Application is **decoupled** from this audit cycle and can be deferred until Path 2 (multi-source BI) is mature, since Snippet 4 (operational thresholds) may need adjustment after Table 7 is regenerated with the new BI predictor outputs.

**Modus operandi:** Apply each snippet independently, in any order; each is self-contained. After applying, run `python scripts/validate_clingo_corpus.py` to confirm no regression in the canonical 7-scenario validation (the snippets do not modify `.lp` files, but the convention is to validate after any documentation change that references the corpus).

---

## Snippet 1 — Three-Layer Normative Topology (§2.7)

**Target section:** §2.7 Theoretical context — Normative state space architecture (or equivalent subsection introducing the corpus structure).
**Rationale:** The canonical paper currently describes the corpus implicitly through scenario examples; an explicit statement of the three-layer topology improves the methodological framing and reduces cognitive load for reviewers from constitutional law and public health backgrounds.

### Diff

```diff
@@ §2.7 Theoretical context @@

 The Q-FENG normative state space ψ_S is constructed by composition over a corpus
 of formal predicates encoded as Clingo Answer Set Programming facts and rules.
+
+The corpus is organized in three hierarchically nested layers that mirror the
+formal stratification of positive law (Kelsen 1934; Bobbio 1960):
+
+- **Layer 1 — Constitutional**: petreous clauses, foundational principles, and
+  fundamental rights (in the Brazilian instance, CF/88 Art. 60 §4°, Art. 1°,
+  Art. 3°, Art. 5°, Art. 23 II). Predicates at this layer are classified
+  `sovereign/1` either in the strict petreous sense (entrenched against
+  constitutional amendment) or in the structuring sense (constitutional norms
+  that ground the operational stratum of the federation).
+
+- **Layer 2 — Statutory and regulatory**: legislation enacted by the
+  legislature and regulatory instruments of executive agencies, including
+  ministerial portarias and emergency decrees. Predicates at this layer are
+  classified `sovereign/1` when constitutionally anchored — typically through
+  dual-anchoring patterns documented in Appendix A — and `elastic/1` when
+  modulable by infralegal regulatory instruments.
+
+- **Layer 3 — Scenarios**: factual instances that invoke predicates from
+  Layers 1 and 2 and provide the operational facts (hospital occupancy rates,
+  hour-bank periods, decisions issued, citations used) that activate
+  constraints and trigger the SAT/UNSAT verdict.
+
+The hierarchical separation is methodologically important because it
+implements the Kelsenian normative hierarchy operationally: integrity
+constraints triggered at the constitutional layer cannot be overridden by
+predicates from infralegal layers, and scenario instantiations cannot
+instantiate facts that contradict positive law in superior layers.
+
 The dual-classification scheme SOVEREIGN/ELASTIC operates over the union of
 Layers 1 and 2; scenarios in Layer 3 are factual and not subject to this
 classification. ...
```

---

## Snippet 2 — HITL Sovereignty Classification with Three Criteria (§4.4)

**Target section:** §4.4 E4 — HITL Sovereignty Classification.
**Rationale:** The canonical paper currently describes the E4 stage as binary classification (SOVEREIGN vs. ELASTIC). The April 2026 audit cycle made evident that the classification should be guided by three explicit criteria derived from the dogmatic discussion in Appendix A. Documenting these criteria strengthens the methodological reproducibility of E4 and provides reviewers a transparent protocol.

### Diff

```diff
@@ §4.4 E4 — HITL Sovereignty Classification @@

 The E4 stage classifies each LLM-extracted ClingoPredicate into the dual
 SOVEREIGN/ELASTIC scheme through human-in-the-loop review.
+
+The classification is guided by three explicit criteria, calibrated through
+the April 2026 audit cycle (Appendix A.5):
+
+**Criterion 1 — Constitutional anchoring (audit LAW-BR-05).**
+A predicate is classified `sovereign/1` only if at least one anchor is
+constitutional. Predicates anchored solely in statutory or regulatory norms
+are classified `elastic/1` even if they encode rights or obligations of
+broad applicability. When a statutory norm encodes a right with
+constitutional grounding, dual-anchoring is applied: the predicate is
+sovereign only when both the statutory and the constitutional anchors are
+co-present.
+
+**Criterion 2 — Deontic validation against thematic relevance (audit C-4).**
+LLM extraction may return predicates whose source instrument is thematically
+relevant but deontically irrelevant to the scenario (e.g., a portaria
+covering an adjacent regulatory matter). The HITL review verifies that the
+anchor instrument actually establishes the obligation invoked by the
+predicate, not merely a textual co-occurrence.
+
+**Criterion 3 — Citation existence cross-reference (audit F0-1).**
+Jurisprudential anchors (precedent citations) are cross-referenced against
+authoritative public databases of the issuing court before being admitted
+to the corpus. Syntactically valid case numbers are insufficient; the case
+must be verifiable in the public registry.
+
+These three criteria operationalize the methodological lessons of the
+audit cycle: that LLM-assisted normative extraction systematically requires
+semantic-juridical filtering, not merely syntactic validation, and that the
+legal weight of a predicate is a function of its anchor topology, not of
+the LLM's extraction confidence.
+
 The classification is recorded as the value of the `sovereignty` field in
 the SovereigntyAtom record produced by E4, and persisted in the corresponding
 parquet output file. ...
```

---

## Snippet 3 — Operational Thresholds and the Law-Data Interface (§5.3)

**Target section:** §5.3 Validation Results — C2 Manaus 2021 (or equivalent subsection on the operational thresholds invoked by the C2 scenario).
**Rationale:** The canonical paper currently asserts the 85% TOH and 3-day oxygen thresholds as operational parameters without explicit documentation of their provenance. The April 2026 audit cycle (LAW-BR-08) anchored these thresholds in specific institutional sources; documenting them in the canonical paper is necessary for reviewer transparency, particularly for reviewers from epidemiology and public health.

**Note:** This snippet may need adjustment after Path 2 (multi-source BI) regenerates the predictor outputs and Table 7 is updated. The 85% TOH threshold is canonical for the BI predictor; the 3-day oxygen threshold is the configurable parametric fact.

### Diff

```diff
@@ §5.3 Validation Results — C2 Manaus 2021 @@

 The C2 scenario instantiates two operational thresholds that trigger the
 cascade of constitutional and statutory derivations: hospital capacity
 critical (TOH > 85%) and oxygen supply critical (oxygen days remaining < 3).
+
+The provenance of these thresholds, documented in Appendix A.5.6 (audit
+LAW-BR-08), is as follows:
+
+- **TOH > 85%** is anchored in the Technical Indicator Sheet for Hospital
+  Care of the Brazilian Ministry of Health (TOH UTI), prepared by the
+  General Coordination of Hospital Care / DAHU / SAES / MS. There is
+  convergence with the critical Brazilian intensive-care literature (AMIB)
+  which classifies TOH > 85% as operational saturation — a state in which
+  ICU bed waiting time grows non-linearly and mortality from inadequate
+  prioritization increases.
+
+- **Oxygen days remaining < 3** is anchored in the operational precedent of
+  Manaus 2021 (White Martins notification to the Ministry of Health on
+  14/Jan/2021 of impossibility of replenishment in 24-48h). The threshold
+  is implemented as a configurable parametric fact
+  (`oxygen_critical_threshold_days(3).`), allowing adjustment without
+  modification of the logical predicate.
+
+The separation between logical predicate (rule) and parametric fact (value)
+is a normative engineering pattern that makes the corpus auditable and
+adaptable without losing documentary grounding. The pattern is generalizable
+to other thresholds and is recommended for any NeSy system operating on
+empirical data.
+
 The C2 scenario activates these thresholds against the hospital occupancy
 and oxygen logistics data of the Manaus crisis (Jan 2021), triggering the
 cascade ... [...] ... and the resulting verdict is UNSAT (CIRCUIT_BREAKER,
 θ ≈ 132°).
```

---

## Snippet 4 — Real Precedent in T-CLT-04 Positive Control (§5.3)

**Target section:** §5.3 Validation Results — T-CLT-04 (positive control) or equivalent subsection.
**Rationale:** The canonical paper must document explicitly that T-CLT-04 invokes a real, verifiable precedent (TST-Ag-RR-868-65.2021.5.13.0030), not the previously fabricated case number that was corrected in audit C-6. This is essential for the falsifiability of the framework: the positive control of an experiment must be constructed on verifiable grounds.

### Diff

```diff
@@ §5.3 Validation Results — T-CLT-04 Positive Control @@

 The T-CLT-04 scenario is the positive control of the labor-domain validation:
 a well-grounded judicial decision invoking a real precedent with explicitly
 identified ratio decidendi.
+
+The invoked precedent is **TST-Ag-RR-868-65.2021.5.13.0030**, a ruling of
+the 2nd Panel of the Brazilian Superior Labor Court (TST), published in
+DEJT on 06/Dec/2023, addressing a banking-sector collective bargaining
+agreement articulated with STF Theme 1046 (ARE 1.121.633). The case is
+verifiable in the public TST database and provides the dogmatic foundation
+for the positive control: a decision that grounds itself in identified
+ratio, addresses all deduced arguments (CPC Art. 489 §1° IV/VI), and is
+sustained by a real, traceable jurisprudential anchor.
+
+This explicit identification of the precedent is the result of audit C-6
+(Apr 2026), which substituted a previously fabricated case number that
+had passed initial validation through syntactic format-matching. The audit
+protocol now requires cross-reference of every jurisprudential anchor
+against the issuing court's public database, as documented in Appendix
+A.5.4 and §4.4 (Criterion 3).
+
 The scenario invokes CF/88 Art. 93 IX, Art. 5° XXXV, CPC Art. 489 §1° V/VI,
 LINDB Art. 20, CLT Art. 59 §2°, and Art. 611-A I — all of which are
 satisfied by the operational facts of the case. The verdict is SAT (STAC,
 θ ≈ 7°). ...
```

---

## Snippet 5 — Defeasibility and Audit Transparency Limitations (§7.4)

**Target section:** §7.4 Limitations and Future Work.
**Rationale:** The canonical paper's §7.4 currently lists limitations in general terms. Two specific limitations identified by the April 2026 audit cycle should be documented explicitly: (a) defeasibility is deferred to the full governance suite, and (b) audit transparency is itself a methodological commitment that requires periodic review of the corpus.

### Diff

```diff
@@ §7.4 Limitations and Future Work @@

 [...existing limitations content...]
+
+**Defeasibility deferred to the full governance suite.** The current corpus
+encodes obligations as hard ASP facts. Formal treatment of defeasibility —
+exceptions, hierarchical priority among norms, the strong/weak distinction
+of permissions (Governatori, Olivieri, Rotolo, and Scannapieco 2013) — is
+deferred to the full governance suite. This is a deliberate methodological
+choice for the proof-of-concept stage: hard ASP semantics is sufficient to
+demonstrate that Ontological Friction can be operationalized as a
+continuous scalar, and the binary SAT/UNSAT verdicts of the canonical
+scenarios suffice to validate the four failure types (§3.5). For the
+production version of Q-FENG, integration with defeasible deontic logic
+is a priority direction.
+
+**Audit transparency as methodological commitment.** The Q-FENG corpus is
+subject to periodic semantic audit cycles, the most recent of which (April
+2026) consolidated 14 numbered audits across the Brazilian sub-corpus
+(Appendix A.5; full report in `artefatos/auditorias/`). Each audit cycle
+may modify the corpus content (predicate definitions, dual-anchoring
+patterns, threshold provenance) without modifying the SAT/UNSAT verdicts
+of canonical scenarios — the substantive content of corrections is in the
+documentary anchoring and engineering structure, not in the binary
+outcomes. A consequence is that **reproducibility of the framework is
+conditioned on the commit hash of the corpus version used**, not merely
+on the framework architecture. The branch `caminho2` of the public
+repository (`github.com/Ricardo-Kaminski/qfeng_validation`) preserves the
+complete audit trail.
+
 [...remaining limitations content...]
```

---

## Snippet 6 — EU/USA Sub-Corpus Audit (§7.4 or §7.5 Future Work)

**Target section:** §7.4 Limitations or §7.5 Future Work.
**Rationale:** The international submission of Paper 1 requires symmetric methodological treatment of the EU and USA sub-corpora. The April 2026 audit cycle focused on the Brazilian domain; the EU/USA audit is identified as a forthcoming work and is being conducted in parallel-silent mode to Path 2.

### Diff

```diff
@@ §7.4 Limitations / §7.5 Future Work @@

 [...existing future work content...]
+
+**EU and USA sub-corpus systematic audit (in progress).** The April 2026
+audit cycle focused on the Brazilian sub-corpus
+(`brasil/constitucional/`, `brasil/saude/`, `brasil/emergencia_manaus/`,
+`brasil/processual/`, `brasil/trabalhista/`). Analogous systematic audit
+of the EU sub-corpus (`eu/ai_act/eu_ai_act_obligations.lp`,
+`eu/gdpr/gdpr_data_protection.lp`) and USA sub-corpus
+(`usa/civil_rights/civil_rights_14th.lp`, `usa/medicaid/medicaid_access.lp`,
+with re-review of `scenarios/c7_obermeyer_facts.lp` against Obermeyer et
+al. 2019 Table 2) is being conducted in parallel-silent mode. The audit
+plan is documented in `artefatos/briefings/PROMPT_CLAUDECODE_AUDITORIA_CORPUS_EU_USA.md`,
+and results will be re-incorporated into the Paper 1 canonical text upon
+completion. The methodological framework of the audit (four classes of
+pendencies A/B/C/D, dual-classification protocol, citation cross-reference)
+is jurisdiction-portable by design.
+
 [...remaining future work content...]
```

---

*End of methodological notes.*

*Document produced in Opus 4.7 chat session and recorded by Claude Code local in `artefatos/notas_metodologicas/NOTAS_CORPUS_CLINGO_para_canonico.md` on 26/Apr/2026, branch `caminho2`.*
