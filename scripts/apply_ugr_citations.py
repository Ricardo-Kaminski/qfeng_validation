#!/usr/bin/env python3
"""
apply_ugr_citations.py
======================

Applies five cumulative citation insertions to PAPER1_QFENG_VALIDATION.md
engaging with the UGR/DaSCI research group's published work:

  1. Arrieta et al. (2020)        — XAI taxonomy, §2.1
  2. Díaz-Rodríguez et al. (2022) — X-NeSyL methodology, §2.1
  3. Díaz-Rodríguez et al. (2023) — Trustworthy AI, §2.3 and §7.3
  4. Herrera-Poyatos et al. (2026) — RAIS framework v2, §2.3 and §7

Each insertion is anchored in textually verified source content (see
  /home/claude/ugr_papers/ for the extracted PDFs used for verification).
Inferential framing statements ("maps onto", "addresses the gap") are
  author-side positioning of Q-FENG, not attribution to the cited authors.

Pattern follows apply_paper_numeric_corrections.py and
  apply_abstract_corpus_totals.py:
    - unique old_str validation (must appear exactly once)
    - .bak backup before modification
    - post-check with [OK]/[!!] markers

Usage:
    python scripts/apply_ugr_citations.py docs/papers/PAPER1_QFENG_VALIDATION.md

Author: Ricardo S. Kaminski
Date: 2026-04-22
"""

import sys
import shutil
from pathlib import Path


# ============================================================================
# EDIT DEFINITIONS
# ============================================================================
# Each edit is a dict: {name, old_str, new_str, anchor_section}
# old_str MUST appear exactly once in the target file.
# ============================================================================

EDITS = [
    # ------------------------------------------------------------------
    # INSERTION 1 — §2.3 (AI Governance Frameworks)
    # Replaces the existing paragraph that currently cites Diaz-Rodriguez
    # et al. 2023 in passing, upgrading it to an analytically engaged
    # passage that also introduces Herrera-Poyatos et al. 2026 (RAIS v2).
    # ------------------------------------------------------------------
    {
        "name": "§2.3_trustworthy_AI_frameworks",
        "old_str": (
            "Diaz-Rodriguez, N., Del Ser, J., Coeckelbergh, M., de Prado, M.L., "
            "Herrera-Viedma, E., & Herrera, F. (2023). Connecting the dots in "
            "trustworthy artificial intelligence. *Information Fusion*, 99, 101896."
        ),
        "new_str": (
            "Díaz-Rodríguez, N., Del Ser, J., Coeckelbergh, M., López de Prado, M., "
            "Herrera-Viedma, E., & Herrera, F. (2023). Connecting the dots in "
            "trustworthy Artificial Intelligence: From AI principles, ethics, and "
            "key requirements to responsible AI systems and regulation. "
            "*Information Fusion*, 99, 101896. "
            "https://doi.org/10.1016/j.inffus.2023.101896"
        ),
        "note": (
            "Canonicalises bibliographic entry (full title, López de Prado with "
            "tilde, accented Díaz-Rodríguez). New in-text engagement added via "
            "insertion 1b below."
        ),
    },
    # ------------------------------------------------------------------
    # INSERTION 1b — In-text engagement with Díaz-Rodríguez + Herrera-Poyatos
    # in §2.3. CHOOSE anchor carefully: the paragraph that opens §2.3 and
    # currently surveys AI governance frameworks.
    #
    # >>> THE old_str BELOW MUST BE VERIFIED AGAINST THE ACTUAL .md BEFORE
    # >>> APPLYING. The paragraph below is based on the canonical state
    # >>> described in the 22-apr briefing. If the paragraph has been
    # >>> revised since, update old_str accordingly.
    # ------------------------------------------------------------------
    {
        "name": "§2.3_in_text_TAI_RAIS_frameworks",
        "old_str": (
            "### 2.3 AI Governance Frameworks"
        ),
        "new_str": (
            "### 2.3 AI Governance Frameworks\n\n"
            "The European Commission's High-Level Expert Group articulates "
            "Trustworthy AI as requiring three foundational pillars — lawfulness, "
            "ethics, and technical robustness — sustained by seven technical "
            "requirements: human agency and oversight; technical robustness and "
            "safety; privacy and data governance; transparency; diversity, "
            "non-discrimination, and fairness; societal and environmental "
            "wellbeing; and accountability (Díaz-Rodríguez et al. 2023). "
            "Building on this foundation, Herrera-Poyatos et al. (2026) argue "
            "that responsible AI in high-risk scenarios cannot be achieved "
            "through isolated principles or technical tools, proposing an "
            "integrated Responsible AI System (RAIS) framework organised around "
            "five inter-dependent dimensions — domain definition, trustworthy AI "
            "design, auditability, accountability, and governance — with "
            "dynamic feedback loops that connect the accountability stage to "
            "earlier phases of the system lifecycle. These frameworks establish "
            "what AI governance should deliver conceptually, but as the authors "
            "themselves note, significant implementation gaps persist between "
            "high-level principles and operational mechanisms in concrete "
            "high-risk domains. The Q-FENG C1 pipeline addresses one specific "
            "dimension of this gap: it operationalises the *normative "
            "alignment* subproblem through a continuous, computable "
            "interference angle grounded in sovereign predicates extracted "
            "from primary legal texts.\n\n"
            "Herrera-Poyatos et al. (2026) also recognise explicitly that part "
            "of the apparent fragmentation of the responsible AI field is "
            "attributable to the intrinsically sociotechnical nature of the "
            "problem, and that governance of AI in high-risk domains involves "
            "inevitable tensions between values — transparency versus privacy, "
            "fairness versus performance, control versus autonomy — that "
            "cannot be dissolved by appealing to unifying principles. They "
            "argue instead for operational mechanisms — contextual definition, "
            "verifiable requirements, auditing, responsibility allocation, and "
            "governance with feedback loops — that explicitly manage such "
            "trade-offs. The Q-FENG interference angle is one such operational "
            "mechanism, specific to the tension between algorithmic "
            "optimisation and sovereign normative constraints: it does not "
            "attempt to reduce this tension to a single preference scalar, "
            "but instead exposes it continuously as a geometric misalignment "
            "that triggers proportional governance responses (STAC, HITL, "
            "CIRCUIT_BREAKER)."
        ),
        "note": (
            "TWO paragraphs inserted immediately after the §2.3 heading. "
            "Verified against Díaz-Rodríguez et al. 2023 Abstract and §1 "
            "(pillars/requirements), Herrera-Poyatos et al. 2026 v2 Abstract, "
            "§1 and §2 (five dimensions, fragmentation, trade-offs). "
            "Last sentence of each paragraph is author-side framing of "
            "Q-FENG positioning."
        ),
    },
    # ------------------------------------------------------------------
    # INSERTION 2 — §2.1 (Neurosymbolic AI)
    # Adds Arrieta et al. (2020) XAI survey as field anchor, followed by
    # the X-NeSyL (Díaz-Rodríguez et al. 2022) precedent with a clean
    # differentiation statement for Q-FENG.
    #
    # >>> VERIFY the anchor sentence exists in §2.1 before applying.
    # ------------------------------------------------------------------
    {
        "name": "§2.1_Arrieta_XNeSyL",
        "old_str": (
            "### 2.1 Neurosymbolic AI"
        ),
        "new_str": (
            "### 2.1 Neurosymbolic AI\n\n"
            "The trajectory from opaque deep learning models toward interpretable "
            "and accountable AI systems has been surveyed exhaustively by "
            "Arrieta et al. (2020), who establish the foundational taxonomy of "
            "XAI contributions and frame the path toward what they term "
            "Responsible Artificial Intelligence. Within the neurosymbolic "
            "family specifically, Díaz-Rodríguez et al.'s X-NeSyL methodology "
            "(2022) is an instructive precedent: it fuses deep learning "
            "representations with expert knowledge graphs through a three-part "
            "architecture — a symbolic processing component (the expert "
            "knowledge graph), a neural processing component (EXPLANet, a "
            "compositional part-based CNN), and an XAI-informed training "
            "procedure (SHAP-Backprop) that aligns neural attributions with "
            "symbolic representations via a misattribution function measured "
            "by SHAP Graph Edit Distance. Q-FENG inherits the three-part "
            "structural template of X-NeSyL (symbolic component + neural "
            "component + quantitative alignment mechanism) but redirects it "
            "in three substantive ways: the symbolic component is the sovereign "
            "normative corpus extracted from primary legal texts, not an expert "
            "domain knowledge graph; the alignment mechanism is the Hilbert-"
            "space interference angle θ derived from quantum decision theory, "
            "not SHAP-based attribution comparison; and the purpose is "
            "compliance-by-construction governance rather than explanation "
            "interpretability. The structural kinship positions Q-FENG within "
            "an established NeSy integration paradigm while marking a distinct "
            "application to the AI governance problem."
        ),
        "note": (
            "Verified against: Arrieta et al. 2020 Abstract (XAI taxonomy, "
            "Responsible AI framing); X-NeSyL Abstract, §1 and Figure 1 "
            "(three components, SHAP-Backprop, SHAP GED, MonuMAI use case). "
            "Differentiation statement for Q-FENG is author-side framing."
        ),
    },
    # ------------------------------------------------------------------
    # INSERTION 3 — §7.3 (Human-in-the-Loop as Epistemic Necessity)
    # Maps the HITL/HOTL/HIC taxonomy of Díaz-Rodríguez et al. 2023 §5.2.2
    # onto the Q-FENG Circuit Breaker, with auditability definition
    # from §6.1 of the same paper.
    #
    # >>> VERIFY the §7.3 heading exists before applying.
    # ------------------------------------------------------------------
    {
        "name": "§7.3_HITL_taxonomy_mapping",
        "old_str": (
            "### 7.3 Human-in-the-Loop as Epistemic Necessity"
        ),
        "new_str": (
            "### 7.3 Human-in-the-Loop as Epistemic Necessity\n\n"
            "The Q-FENG HITL regime maps directly onto the taxonomy of human "
            "oversight articulated by Díaz-Rodríguez et al. (2023), which "
            "distinguishes three degrees of human involvement: "
            "Human-in-the-Loop (intervention in every decision cycle of the "
            "monitored system), Human-on-the-Loop (intervention during design "
            "and monitoring cycles), and Human-in-Command (the capability of "
            "the supervisor to oversee the overall activity of the AI system, "
            "including its broader economic, societal, legal, and ethical "
            "impacts, and to ensure that decisions produced by the AI system "
            "can be overridden by the human). The Circuit Breaker activation "
            "at θ ≥ 120° is the architectural expression of Human-in-Command: "
            "it suspends autonomous operation and mandates supervisor review "
            "whenever the normative misalignment exceeds the threshold of "
            "severe opposition. The continuous θ computation itself is an "
            "auditability mechanism in the sense articulated by the same "
            "authors: validating conformity of the system against vertical "
            "or sectorial regulatory constraints, horizontal or AI-wide "
            "regulations such as the EU AI Act, and the specifications and "
            "constraints imposed by the application for which the system is "
            "designed. The two-stage Q-FENG response thus instantiates the "
            "auditability-accountability pair that Díaz-Rodríguez et al. (2023) "
            "place at the core of their definition of a Responsible AI System: "
            "auditability as continuous conformity assessment, accountability "
            "as the liability that attaches to decisions once compliance has "
            "been audited."
        ),
        "note": (
            "Verified literal citations from Díaz-Rodríguez et al. 2023: "
            "§5.2.2 for HITL/HOTL/HIC definitions (including HIC's reference "
            "to 'overall activity... broader economic, societal, legal and "
            "ethical impacts'); §6.1 Definition for auditability's three-part "
            "conformity; §5.8 for auditability-accountability pairing. "
            "Mapping to Q-FENG Circuit Breaker is author-side framing."
        ),
    },
    # ------------------------------------------------------------------
    # INSERTION 4 — REFERENCES SECTION — Bibliographic entries
    # Adds/canonicalises the four UGR entries in the References section
    # in Chicago author-date style.
    #
    # >>> THE old_str MUST ANCHOR AT A STABLE POINT IN REFERENCES.
    # >>> Adjust the anchor to the exact state of the .md References.
    # ------------------------------------------------------------------
    {
        "name": "References_UGR_entries",
        "old_str": (
            "Arrieta, A.B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, "
            "S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., "
            "et al. (2020). Explainable artificial intelligence (XAI): concepts, "
            "taxonomies, opportunities and challenges toward responsible AI. "
            "*Information Fusion*, 58, 82–115."
        ),
        "new_str": (
            "Arrieta, A.B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, "
            "S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., "
            "Chatila, R., & Herrera, F. (2020). Explainable artificial "
            "intelligence (XAI): Concepts, taxonomies, opportunities and "
            "challenges toward responsible AI. *Information Fusion*, 58, 82–115. "
            "https://doi.org/10.1016/j.inffus.2019.12.012\n\n"
            "Díaz-Rodríguez, N., Lamas, A., Sanchez, J., Franchi, G., Donadello, "
            "I., Tabik, S., Filliat, D., Cruz, P., Montes, R., & Herrera, F. "
            "(2022). EXplainable Neural-Symbolic Learning (X-NeSyL) methodology "
            "to fuse deep learning representations with expert knowledge graphs: "
            "The MonuMAI cultural heritage use case. *Information Fusion*, 79, "
            "58–83. https://doi.org/10.1016/j.inffus.2021.09.022\n\n"
            "Herrera-Poyatos, A., Del Ser, J., López de Prado, M., Wang, F.-Y., "
            "Herrera-Viedma, E., & Herrera, F. (2026). A Framework for "
            "Responsible AI Systems: Building Societal Trust through Domain "
            "Definition, Trustworthy AI Design, Auditability, Accountability, "
            "and Governance. *arXiv preprint* arXiv:2503.04739v2. "
            "https://arxiv.org/abs/2503.04739"
        ),
        "note": (
            "Adds Chatila & Herrera as co-authors of Arrieta et al. 2020 "
            "(verified in PDF author list, previously had 'et al.'); adds "
            "X-NeSyL (Díaz-Rodríguez et al. 2022) and Herrera-Poyatos et al. "
            "2026 v2 entries. Chronological order preserved."
        ),
    },
]


# ============================================================================
# EXECUTION
# ============================================================================

def apply_edit(content: str, edit: dict) -> tuple[str, bool, str]:
    """
    Apply a single edit with strict uniqueness validation.
    Returns (new_content, success, message).
    """
    name = edit["name"]
    old = edit["old_str"]
    new = edit["new_str"]

    count = content.count(old)
    if count == 0:
        return content, False, f"[!!] {name}: old_str NOT FOUND"
    if count > 1:
        return content, False, f"[!!] {name}: old_str matches {count} locations (must be unique)"

    new_content = content.replace(old, new)
    delta = len(new_content) - len(content)
    return new_content, True, f"[OK] {name}: +{delta} chars"


def main():
    if len(sys.argv) != 2:
        print("Usage: python apply_ugr_citations.py <path_to_md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"[!!] File not found: {md_path}")
        sys.exit(1)

    # Backup
    bak_path = md_path.with_suffix(md_path.suffix + ".bak_ugr")
    shutil.copy2(md_path, bak_path)
    print(f"[OK] Backup saved to: {bak_path}")

    content = md_path.read_text(encoding="utf-8")
    original_len = len(content)

    # Pre-check: validate all old_str are unique before any modification
    print("\n=== Pre-check: uniqueness validation ===")
    errors = []
    for edit in EDITS:
        c = content.count(edit["old_str"])
        if c == 0:
            errors.append(f"[!!] {edit['name']}: old_str NOT FOUND — check anchor")
        elif c > 1:
            errors.append(f"[!!] {edit['name']}: old_str matches {c} locations — not unique")
        else:
            print(f"[OK] {edit['name']}: unique anchor found")

    if errors:
        print("\n=== Pre-check FAILED ===")
        for e in errors:
            print(e)
        print("\nAborting without modifications. Fix anchors and retry.")
        sys.exit(2)

    # Apply edits sequentially
    print("\n=== Applying edits ===")
    for edit in EDITS:
        content, ok, msg = apply_edit(content, edit)
        print(msg)
        if not ok:
            print("Aborting.")
            sys.exit(3)

    # Write
    md_path.write_text(content, encoding="utf-8")
    final_len = len(content)
    delta = final_len - original_len
    print(f"\n[OK] File updated: {md_path}")
    print(f"[OK] Total delta: +{delta} chars ({original_len} → {final_len})")
    print(f"[OK] Backup preserved at: {bak_path}")

    # Post-check: confirm new content appears
    print("\n=== Post-check: new content verification ===")
    post_checks = [
        ("Díaz-Rodríguez et al. (2023)", "Trustworthy AI canonical citation"),
        ("Herrera-Poyatos et al. (2026)", "RAIS v2 citation"),
        ("five inter-dependent dimensions", "RAIS five dimensions"),
        ("domain definition, trustworthy AI design, auditability, accountability, and governance", "RAIS explicit dimensions list"),
        ("Human-in-Command", "HIC taxonomy"),
        ("X-NeSyL methodology", "X-NeSyL precedent"),
        ("Hilbert-space interference angle θ", "Q-FENG differentiation marker"),
    ]
    for needle, label in post_checks:
        present = needle in content
        marker = "[OK]" if present else "[!!]"
        print(f"{marker} {label}: {'found' if present else 'MISSING'}")


if __name__ == "__main__":
    main()
