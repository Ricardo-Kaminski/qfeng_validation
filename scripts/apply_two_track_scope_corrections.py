#!/usr/bin/env python3
"""
Atualiza o Paper 1 para refletir o escopo COMPLETO de duas trilhas
(saude/governance + trabalhista), corrigindo subdimensionamento
identificado na auditoria:

1. Abstract: passa de "5,136 DeonticAtoms" para "10,142 DeonticAtoms
   across two tracks (5,136 health/governance + 5,006 labour)"
   e atualiza a contagem total de NormChunks para incluir o corpus
   trabalhista.

2. Apos Tabela 1 (saude): adiciona uma Tabela 1b separada apresentando
   o corpus trabalhista (4.488 chunks, 4 documentos, 5.006 atoms) com
   um paragrafo de transicao explicando o porque de tabelas separadas
   (corpora colhidos em fases distintas, Tabela 1 = saude/governance,
   Tabela 1b = trabalhista).

Nao toca no numero "537 predicates" da secao 4.5 — fica como item de
verificacao para a proxima rodada (potencialmente uma contagem diferente
de "predicate types" vs. "predicate instances").

Uso:
    python scripts/apply_two_track_scope_corrections.py docs/papers/PAPER1_QFENG_VALIDATION.md
"""
import sys
import shutil
from pathlib import Path


EDITS = [
    {
        "label": "Abstract: 5,136 -> 10,142 dual-track contextualisation",
        "old": (
            "This proof-of-concept demonstration covers three normative regimes "
            "(Brazil/SUS, EU AI Act, US Medicaid/Equal Protection) and two domains "
            "(public health infrastructure and labour law) using 29 primary "
            "normative documents (27,957 NormChunks), 5,136 DeonticAtoms (mean "
            "confidence: 0.930), and seven author-designed formal scenarios."
        ),
        "new": (
            "This proof-of-concept demonstration covers three normative regimes "
            "(Brazil/SUS, EU AI Act, US Medicaid/Equal Protection) and two domains "
            "(public health infrastructure and labour law). The integrated normative "
            "base comprises 33 primary documents (32,445 NormChunks across both "
            "tracks) from which 10,142 DeonticAtoms were extracted (5,136 in the "
            "health/governance track at mean confidence 0.930; 5,006 in the labour "
            "track at mean confidence 0.942), and seven author-designed formal "
            "scenarios are evaluated."
        ),
    },
    {
        "label": "Insert Table 1b (labour corpus) immediately after Table 1 paragraph",
        "old": (
            "Chunk type distribution: obligation (82.5%, n=23,053), procedure "
            "(7.1%, n=1,992), principle (6.8%, n=1,913), definition (2.7%, n=759), "
            "sanction (0.9%, n=240). The dominance of obligation chunks is "
            "consistent with the legal structure of the target documents — "
            "primarily legislative statutes and regulations rather than commentary "
            "or doctrine."
        ),
        "new": (
            "Chunk type distribution: obligation (82.5%, n=23,053), procedure "
            "(7.1%, n=1,992), principle (6.8%, n=1,913), definition (2.7%, n=759), "
            "sanction (0.9%, n=240). The dominance of obligation chunks is "
            "consistent with the legal structure of the target documents — "
            "primarily legislative statutes and regulations rather than commentary "
            "or doctrine.\n\n"
            "**Labour-track corpus.** The labour-law domain (T-CLT-01 through "
            "T-CLT-04 scenarios) is supported by a separate, jurisdiction-specific "
            "Brazilian sub-corpus assembled in a distinct ingestion pass and "
            "reported separately for traceability:\n\n"
            "**Table 1b. Labour-track corpus distribution and DeonticAtom "
            "extraction results.**\n\n"
            "| Document | Chunks | DeonticAtoms |\n"
            "|----------|-------:|-------------:|\n"
            "| CF/88 Art. 7º (XIII–XVI: working-hours rights) | partial | included below |\n"
            "| CLT — Consolidação das Leis do Trabalho (full) | majority | majority |\n"
            "| Lei 13.467/2017 (Reforma Trabalhista) | partial | partial |\n"
            "| TST jurisprudence (Súmulas 85, 291; selected acórdãos) | partial | partial |\n"
            "| **Total (4 documents, regime: Brasil)** | **4,488** | **5,006** |\n\n"
            "Mean confidence in the labour track is 0.942 (median 0.950); only 5 "
            "atoms (0.1%) were extracted with confidence below 0.7. The labour "
            "modality distribution differs structurally from the health/governance "
            "track: obligation 70.6% (vs. 84.2%), prohibition 16.3% (vs. 4.8%), "
            "permission 9.2% (vs. 9.4%), and faculty 3.9% (vs. 1.6%). The 3.4× "
            "higher prohibition rate reflects a defining stylistic property of "
            "Brazilian labour law — the historical predominance of explicit "
            "vedações *ao empregador* (prohibitions binding the employer) as the "
            "primary regulatory device, in contrast to the principle-and-permission "
            "structure typical of constitutional and health-system instruments. "
            "This asymmetry is visualised in Figure 7 (§5.5)."
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

    backup = path.with_suffix(path.suffix + ".bak2")
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
        ("33 primary documents", True),
        ("32,445 NormChunks", True),
        ("10,142 DeonticAtoms were extracted", True),
        ("Table 1b. Labour-track", True),
        ("4,488", True),
        ("5,006", True),
        ("0.942", True),
        ("3.4x higher prohibition", False),  # we wrote "3.4×" with multiplication sign
        ("3.4", True),
    ]
    for s, should_exist in probes:
        found = s in text
        ok = (found == should_exist)
        status = "[OK]" if ok else "[!!]"
        print(f"  {status} {'present' if should_exist else 'absent':>7} : '{s}' -> "
              f"{'found' if found else 'not found'}")


if __name__ == "__main__":
    main()
