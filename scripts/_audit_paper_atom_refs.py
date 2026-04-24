"""
Auditoria do paper para identificar mencoes a contagens de atoms que
podem precisar de contextualizacao (saude vs trabalhista vs total) apos
a entrada do diagnostico canonico.
"""
import re
import sys
from pathlib import Path

# Forca UTF-8 no stdout (Windows PowerShell padrao e cp1252)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
paper = (PROJECT_ROOT / "docs" / "papers" / "PAPER1_QFENG_VALIDATION.md").read_text(encoding="utf-8")
lines = paper.splitlines()

patterns = {
    "5,136 (saude only)": r"5[,.]?136",
    "5,006 (trabalhista)": r"5[,.]?006",
    "10,142 (total)": r"10[,.]?142",
    "4,973 (post E3+E4)": r"4[,.]?973",
    "2,530 (saude .lp)": r"2[,.]?530",
    "2,443 (trab .lp)": r"2[,.]?443",
    "829 atoms (USA)": r"\b829\b",
    "1,101 atoms (EU)": r"1[,.]?101",
    "3,206 atoms (BR saude)": r"3[,.]?206",
    "27,957 (E1 chunks)": r"27[,.]?957",
    "Total NormChunks": r"Total\s+NormChunks",
    "537 predicates (HITL old number)": r"537\s*(predicates|/537)",
    "labour / trabalhista corpus": r"\b(labour|trabalhista|CLT|TST)\b",
}

def safe(s):
    return s.encode("ascii", errors="replace").decode("ascii")

for label, pat in patterns.items():
    print(f"\n--- {label}  pattern: {pat}")
    rx = re.compile(pat, re.IGNORECASE)
    matched_any = False
    for i, line in enumerate(lines, 1):
        if rx.search(line):
            snippet = line.strip()[:220]
            print(f"  L{i:>4}: {safe(snippet)}")
            matched_any = True
    if not matched_any:
        print("  (no matches)")
