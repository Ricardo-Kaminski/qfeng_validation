#!/usr/bin/env python3
"""
Etapa final de fechamento do Paper 1:

1. REMOVE a duplicata do paragrafo "Pipeline survival E2 -> E3 -> E4"
   (apareceu duas vezes apos a aplicacao do script anterior; mantemos uma).

2. ADICIONA o subitem "Multilingual extraction asymmetry (PT-BR vs EN)"
   ao final da §7.4 Limitations, articulando a tese das tres camadas
   com fundamentacao na literatura (dPASP/Geh et al. 2024, KEML/C4AI-USP,
   Tucano/Correa et al. 2025, PoETa v2 2025, Niklaus et al. multilingual
   legal reasoning).

3. ADICIONA as referencias correspondentes em ordem alfabetica na secao
   References, mantendo o formato author-date (Chicago/APA-adjacent) ja
   usado no paper.

Uso:
    python scripts/apply_section_7_4_dpasp_kelm_pt_br.py docs/papers/PAPER1_QFENG_VALIDATION.md
"""
import sys
import shutil
from pathlib import Path


# ---------------------------------------------------------------------
# 1. Deduplicate: remove second occurrence of the survival paragraph
# ---------------------------------------------------------------------
SURVIVAL_PARA = (
    "**Pipeline survival E2 \u2192 E3 \u2192 E4.** Across both tracks, the E2 "
    "stage produced 10,142 DeonticAtoms (5,136 health/governance; 5,006 "
    "labour). After the E3 deterministic Jinja-template translation and the "
    "E4 HITL sovereignty review, 4,973 atoms (49.0%) produced valid, "
    "scope-admissible Clingo predicates that form the symbolic substrate "
    "for the seven scenarios evaluated in Section 5: 2,530 predicates for "
    "the health/governance track (49.3% of its E2 output) and 2,443 for the "
    "labour track (48.8%). The attrition is concentrated at two stages: "
    "template-pattern mismatch in E3 (atoms whose conditions or patient "
    "roles did not admit a deterministic Jinja mapping were discarded "
    "rather than coerced) and scope filtering enforced by ScopeConfig "
    "(only chunks belonging to the active scenario scope enter the Clingo "
    "fact base). Both mechanisms are features, not defects: E3 refuses "
    "lossy translations to preserve formal correctness, and ScopeConfig "
    "ensures that each scenario is evaluated against exactly the normative "
    "surface relevant to its governance question. Limitations of the "
    "underlying LLM extraction \u2014 particularly its uneven performance "
    "across languages \u2014 are discussed in Section 7.4."
)


# ---------------------------------------------------------------------
# 2. New 7.4 subsection: Multilingual extraction asymmetry
# ---------------------------------------------------------------------
NEW_7_4_SUBSECTION = (
    "\n\n**Multilingual extraction asymmetry (PT-BR vs. EN) and corpus "
    "curation strategy.** The E2 extraction pipeline relies on a few-shot "
    "LLM extractor whose performance is empirically uneven across the "
    "languages of the source corpora. The Brazilian (PT-BR), EU (EN), and "
    "US (EN) sub-corpora were processed with the same extraction protocol, "
    "but produced predicates of qualitatively different depth and "
    "semantic precision: extractions over EN legal text yielded richer "
    "deontic structures (full agent / patient / conditions / temporality "
    "fields) than extractions over dense PT-BR statutory text, which more "
    "frequently produced shallow predicates with under-specified conditions "
    "or generic agent roles. This pattern is consistent with a robust "
    "finding in the multilingual NLP literature: large language models "
    "trained on English-dominant corpora exhibit measurable performance "
    "degradation on non-English tasks, and this gap is magnified for "
    "morphologically rich and lexically complex domains such as legal "
    "Portuguese (Niklaus et al. 2025; Corr\u00eaa et al. 2025; Magalh\u00e3es "
    "et al. 2025). Three interlocking architectural decisions follow from "
    "this observation, each of which we make explicit here for "
    "reproducibility and methodological transparency.\n\n"
    "*First* (selective normative scope): the E1\u2192E2 pipeline was not "
    "designed for exhaustive ingestion of the full normative corpus. The "
    "ScopeConfig mechanism (\u00a74.1) deliberately restricts processing to "
    "the chain of constitutional, statutory, and infralegal provisions "
    "that anchor each scenario's governance question. This is a design "
    "choice grounded in the validation goal of this paper: Q-FENG is "
    "demonstrated as a cybernetic-interference architecture, not as an "
    "end-to-end legal-compliance system. The 6,059 chunks processed in E2 "
    "(out of 27,957 in the full health-track corpus) reflect this "
    "scoping discipline rather than a coverage failure.\n\n"
    "*Second* (assisted PT-BR curation): where the automatic E2 extraction "
    "produced shallow predicates over PT-BR text, the resulting "
    "DeonticAtoms were complemented by an LLM-assisted human curation "
    "step \u2014 conducted by the author with Claude Opus 4 as a structured "
    "review interface \u2014 prior to E3 translation. Curated atoms inherit "
    "the same {atom_id, source_chunk_id, modality, agent, action, "
    "strength} schema as automatically extracted ones and are stored in the "
    "same e3_predicates artefact (one .lp file per source instrument), so "
    "the chain `clause \u2192 chunk \u2192 atom \u2192 Clingo predicate` "
    "remains fully auditable in both cases. This approach is closer in "
    "spirit to what Lippi et al. (2019) call \"hybrid annotation\" than to "
    "fully automated extraction; the trade-off is explicit reduced "
    "throughput for explicit increased per-predicate quality and legal "
    "traceability.\n\n"
    "*Third* (Clingo-only symbolic core, deferring dPASP integration): a "
    "natural alternative to the present design would be to adopt a "
    "neuro-symbolic probabilistic logic programming framework such as "
    "dPASP (Geh et al. 2024) developed by the KEML \u2014 Knowledge "
    "Enhanced Machine Learning \u2014 group at C4AI/USP (Cozman, Mau\u00e1, "
    "and collaborators), in which neural predicates and probabilistic "
    "facts are jointly optimised with logic constraints. dPASP would "
    "plausibly absorb part of the multilingual extraction problem into a "
    "differentiable end-to-end pipeline. We deliberately deferred this "
    "integration in the present PoC for three reasons aligned with the "
    "paper's validation focus: (i) dPASP introduces a neural component "
    "into the symbolic substrate, which complicates the determinism "
    "guarantee that this paper relies on for reproducibility (Clingo's "
    "stable-model semantics is fully deterministic; dPASP's MaxEnt-Stable "
    "learning is not); (ii) the legal auditability requirement is more "
    "naturally satisfied when each Clingo predicate has a single, "
    "transparent rule for its derivation rather than a learned weight on "
    "a neural-symbolic predicate; and (iii) the PoC's primary contribution "
    "is the quantum-interference governance geometry over the Clingo "
    "output, not the legal-NLP extraction stack. A dPASP-based replacement "
    "of the E2/E3 stages \u2014 potentially leveraging Portuguese-native "
    "language models such as Tucano (Corr\u00eaa et al. 2025), evaluated "
    "on Portuguese legal benchmarks such as PoETa v2 (Magalh\u00e3es et "
    "al. 2025) \u2014 is a natural direction for a successor paper "
    "specifically targeted at the legal-NLP venue (e.g., JURIX, ICAIL).\n\n"
    "We therefore characterise the present pipeline as a *Clingo-pure, "
    "scope-bounded, hybrid-curated* architecture: deterministic at the "
    "symbolic core, deliberately scoped at the corpus boundary, and "
    "transparently augmented at the multilingual extraction interface. "
    "The 4,973 final Clingo predicates that result from this discipline "
    "are not the maximum extractable signal from the source corpora; they "
    "are the maximum *legally auditable* signal that the present "
    "architecture commits to, and they suffice for the validation claims "
    "advanced in this paper."
)


# ---------------------------------------------------------------------
# 3. New references (alphabetical insertion targets)
# ---------------------------------------------------------------------
# Each entry is (anchor_text_to_insert_BEFORE, new_reference_block)
# Anchors must be unique and immediately precede the alphabetical position.
NEW_REFS = [
    {
        "label": "Correa et al. 2025 (Tucano)",
        "anchor": "d'Avila Garcez, A., & Lamb, L.C. (2023).",
        "new_ref": (
            "Corr\u00eaa, N.K., Falk, S., Fatimah, S., Sen, A., & "
            "de Oliveira, N. (2025). Tucano: Advancing neural text "
            "generation for Portuguese. *Patterns* (Cell Press), online "
            "first. https://doi.org/10.1016/j.patter.2025.101291\n\n"
        ),
    },
    {
        "label": "Geh et al. 2024 (dPASP)",
        "anchor": "Governatori, G., Olivieri, F., Rotolo, A., & Scannapieco, S. (2013).",
        "new_ref": (
            "Geh, R.L., Gon\u00e7alves, J., Silveira, I.C., Mau\u00e1, "
            "D.D., & Cozman, F.G. (2024). dPASP: A comprehensive "
            "differentiable probabilistic answer set programming "
            "environment for neurosymbolic learning and reasoning. "
            "In *Proceedings of the 21st International Conference on "
            "Principles of Knowledge Representation and Reasoning (KR "
            "2024)*, 731\u2013742.\n\n"
        ),
    },
    {
        "label": "Magalhaes et al. 2025 (PoETa v2)",
        "anchor": "Manhaeve, R., Dumancic, S., Kimmig, A.,",
        "new_ref": (
            "Magalh\u00e3es, T., Almeida, T., Souza, R., et al. (2025). "
            "PoETa v2: Toward more robust evaluation of large language "
            "models in Portuguese. arXiv:2511.17808.\n\n"
        ),
    },
    {
        "label": "Niklaus et al. 2025 (multilingual legal LLMs)",
        "anchor": "Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019).",
        "new_ref": (
            "Niklaus, J., Stuermer, M., & Chalkidis, I. (2025). "
            "Evaluating the limits of large language models in "
            "multilingual legal reasoning. arXiv:2509.22472.\n\n"
        ),
    },
]


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <caminho_md>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERRO: arquivo nao encontrado: {path}")
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    backup = path.with_suffix(path.suffix + ".bak3")
    shutil.copy2(path, backup)
    print(f"Backup criado: {backup}\n")

    # ---- Step 1: dedupe survival paragraph ----
    print("=" * 72)
    print("STEP 1: deduplicate 'Pipeline survival' paragraph")
    print("=" * 72)
    n_before = text.count(SURVIVAL_PARA)
    print(f"  Occurrences before: {n_before}")
    if n_before == 0:
        print("  ABORTANDO: survival paragraph not found verbatim.")
        sys.exit(1)
    if n_before == 1:
        print("  (no duplication detected; skipping dedupe)")
    else:
        # Remove all occurrences then re-insert one at the original location
        first_idx = text.find(SURVIVAL_PARA)
        text_after_first = text[first_idx + len(SURVIVAL_PARA):]
        # Remove subsequent duplicates from the tail
        while SURVIVAL_PARA in text_after_first:
            # The duplicates are usually preceded by extra whitespace; remove them with surrounding "\n\n"
            target = "\n\n" + SURVIVAL_PARA
            if target in text_after_first:
                text_after_first = text_after_first.replace(target, "", 1)
            else:
                text_after_first = text_after_first.replace(SURVIVAL_PARA, "", 1)
        text = text[:first_idx + len(SURVIVAL_PARA)] + text_after_first
        n_after = text.count(SURVIVAL_PARA)
        print(f"  Occurrences after: {n_after}")
        if n_after != 1:
            print("  ABORTANDO: dedupe did not converge to 1 occurrence.")
            sys.exit(1)

    # ---- Step 2: append new 7.4 subsection ----
    print("\n" + "=" * 72)
    print("STEP 2: append 'Multilingual extraction asymmetry' to 7.4")
    print("=" * 72)
    # Anchor: end of "Thematic scope" paragraph (the last item in 7.4)
    anchor_7_4 = (
        "**Thematic scope**: The Q-FENG C1 pipeline validates alignment "
        "monitoring for a specific class of governance failures \u2014 those "
        "in which the relevant normative instruments are available in "
        "digital, machine-readable form. Oral customary law, unwritten "
        "constitutional conventions, and administrative practice without "
        "formal documentation are outside the current scope."
    )
    n_anchor = text.count(anchor_7_4)
    print(f"  anchor occurrences: {n_anchor}")
    if n_anchor != 1:
        print("  ABORTANDO: anchor for 7.4 must appear exactly once.")
        # Help diagnose: search for the start
        head = "**Thematic scope**:"
        print(f"  '{head}' count: {text.count(head)}")
        sys.exit(1)
    text = text.replace(anchor_7_4, anchor_7_4 + NEW_7_4_SUBSECTION, 1)
    print("  inserted new subsection.")

    # ---- Step 3: insert new references (alphabetical) ----
    print("\n" + "=" * 72)
    print("STEP 3: insert references into References section")
    print("=" * 72)
    for ref in NEW_REFS:
        n = text.count(ref["anchor"])
        if n != 1:
            print(f"  [!!] {ref['label']}: anchor count={n} (expected 1)")
            sys.exit(1)
        text = text.replace(ref["anchor"], ref["new_ref"] + ref["anchor"], 1)
        print(f"  [OK] inserted {ref['label']}")

    # ---- Persist ----
    path.write_text(text, encoding="utf-8")
    size_after = len(text)
    print(f"\nFile written. Final size: {size_after:,} chars")

    # ---- Post-verification ----
    print("\n=== Pos-verificacao ===")
    probes = [
        ("Multilingual extraction asymmetry", True),
        ("Geh et al. 2024", True),
        ("KEML \u2014 Knowledge Enhanced Machine Learning", True),
        ("dPASP", True),
        ("Tucano", True),
        ("PoETa v2", True),
        ("Niklaus", True),
        ("Clingo-pure, scope-bounded, hybrid-curated", True),
        ("Corr\u00eaa, N.K.", True),
        ("Magalh\u00e3es, T.", True),
    ]
    n_ok = 0
    for s, should_exist in probes:
        found = s in text
        ok = (found == should_exist)
        n_ok += int(ok)
        status = "[OK]" if ok else "[!!]"
        print(f"  {status} '{s[:50]}{'...' if len(s) > 50 else ''}'  -> "
              f"{'found' if found else 'not found'}")
    print(f"\n{n_ok}/{len(probes)} probes passed.")

    # Also confirm dedupe stuck
    n_survival_final = text.count(SURVIVAL_PARA)
    print(f"\nFinal 'Pipeline survival' count: {n_survival_final} (expected 1)")


if __name__ == "__main__":
    main()
