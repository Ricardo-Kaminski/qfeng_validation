#!/usr/bin/env python3
"""
Adiciona a frase canonica sobre sobrevivencia E2 -> E3 + E4 ao Paper 1.

Baseado no diagnostico DIAGNOSTICO_F7_atom_counts_21abr2026.md:
- E2 extrai 5.136 atoms (saude) + 5.006 atoms (trabalhista) = 10.142
- Apos E3 translation + E4 HITL, sobrevivem:
    * saude: 2.530 atoms (49.3% de 5.136)
    * trabalhista: 2.443 atoms (48.8% de 5.006)
    * TOTAL: 4.973 atoms (49.0% de 10.142)

Fonte: resposta do Claude Code em 21abr2026 + contagem dos .lp em
outputs/e3_predicates/ e outputs/e3_predicates_trabalhista/.

Uso:
    python scripts/apply_4_4_e3_survival_sentence.py docs/papers/PAPER1_QFENG_VALIDATION.md

Valida que cada old_str aparece exatamente uma vez antes de aplicar.
Salva backup .bak antes de sobrescrever.
"""
import sys
import shutil
from pathlib import Path


EDITS = [
    {
        "label": "4.5 E4 - closing sentence (survival after E3+E4)",
        "old": (
            "The SOVEREIGN/ELASTIC distinction is the formal basis for the "
            "failure typology described in Section 3.5: constitutional failures "
            "arise when a required sovereign predicate is absent from the "
            "corpus; execution failures arise when the sovereign predicate "
            "exists but the execution chain is blocked or misgrounded."
        ),
        "new": (
            "The SOVEREIGN/ELASTIC distinction is the formal basis for the "
            "failure typology described in Section 3.5: constitutional failures "
            "arise when a required sovereign predicate is absent from the "
            "corpus; execution failures arise when the sovereign predicate "
            "exists but the execution chain is blocked or misgrounded.\n\n"
            "**Pipeline survival E2 → E3 → E4.** Across both tracks, the E2 "
            "stage produced 10,142 DeonticAtoms (5,136 health/governance; "
            "5,006 labour). After the E3 deterministic Jinja-template "
            "translation and the E4 HITL sovereignty review, 4,973 atoms "
            "(49.0%) produced valid, scope-admissible Clingo predicates that "
            "form the symbolic substrate for the seven scenarios evaluated "
            "in Section 5: 2,530 predicates for the health/governance track "
            "(49.3% of its E2 output) and 2,443 for the labour track (48.8%). "
            "The attrition is concentrated at two stages: template-pattern "
            "mismatch in E3 (atoms whose conditions or patient roles did not "
            "admit a deterministic Jinja mapping were discarded rather than "
            "coerced) and scope filtering enforced by ScopeConfig (only "
            "chunks belonging to the active scenario scope enter the Clingo "
            "fact base). Both mechanisms are features, not defects: E3 "
            "refuses lossy translations to preserve formal correctness, and "
            "ScopeConfig ensures that each scenario is evaluated against "
            "exactly the normative surface relevant to its governance "
            "question. Limitations of the underlying LLM extraction — "
            "particularly its uneven performance across languages — are "
            "discussed in Section 7.4."
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

    print("=" * 72)
    print("VALIDACAO: cada old_str deve aparecer exatamente 1x")
    print("=" * 72)
    for e in EDITS:
        count = text.count(e["old"])
        status = "[OK]" if count == 1 else f"[!! count={count}]"
        print(f"  {status} {e['label']}")
        if count != 1:
            print(f"    old_str (primeiros 200 chars):\n      {e['old'][:200]}")
            print(f"\nABORTANDO. Corrija old_str antes de re-executar.")
            sys.exit(1)

    backup = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, backup)
    print(f"\nBackup criado: {backup}")

    size_before = len(text)
    for e in EDITS:
        text = text.replace(e["old"], e["new"], 1)
    path.write_text(text, encoding="utf-8")

    size_after = len(text)
    print("Correcoes aplicadas com sucesso.")
    print(f"Tamanho antes : {size_before:,} chars")
    print(f"Tamanho depois: {size_after:,} chars")
    print(f"Delta         : +{size_after - size_before:,} chars")

    # Post-verification
    print("\n=== Pos-verificacao ===")
    probes = [
        ("10,142 DeonticAtoms", True),
        ("4,973 atoms", True),
        ("49.0%", True),
        ("2,530 predicates", True),
        ("2,443 for the labour", True),
    ]
    for s, should_exist in probes:
        found = s in text
        ok = (found == should_exist)
        status = "[OK]" if ok else "[!!]"
        print(f"  {status} {'present' if should_exist else 'absent':>7} : '{s}' -> "
              f"{'found' if found else 'not found'}")


if __name__ == "__main__":
    main()
