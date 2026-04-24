"""Busca rapida por referencias aos numeros de atoms no paper."""
import re
from pathlib import Path

PAPER = Path(__file__).resolve().parent.parent / "docs" / "papers" / "PAPER1_QFENG_VALIDATION.md"
text = PAPER.read_text(encoding="utf-8")
lines = text.split("\n")

patterns = [
    r"5[,.]?136",
    r"3[,.]?163",
    r"3[,.]?022",
    r"DeonticAtom",
    r"deontic atom",
    r"atoms?\s+(?:extracted|cached|total)",
    r"E2",
    r"e2_report",
    r"cache",
    r"chunks?\s+(?:processed|total|with|zero)",
    r"6[,.]?059",
    r"27[,.]?957",
    r"2[,.]?352",
]

for pat in patterns:
    rx = re.compile(pat, re.IGNORECASE)
    print(f"\n--- pattern: {pat}")
    hits = 0
    for i, line in enumerate(lines, 1):
        if rx.search(line):
            hits += 1
            snippet = line.strip()
            if len(snippet) > 180:
                snippet = snippet[:180] + "..."
            print(f"  L{i:>4}: {snippet}")
    if hits == 0:
        print("  (no matches)")
