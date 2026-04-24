"""Add missing TRT-13 suffix to partial case number occurrences in the docx.

After the split-run fix, 'Ag-RR-868-65.2021' appears without '.5.13.0030'.
This script adds the full suffix.
"""
import shutil
from datetime import datetime
from pathlib import Path
from docx import Document

DOCX_PATH = Path("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")
WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# Patterns to fix — order matters (longer first)
FIXES = [
    # If somehow TST- prefix was doubled
    ("TST-TST-Ag-RR-868-65.2021.5.13.0030", "TST-Ag-RR-868-65.2021.5.13.0030"),
    # Full case with wrong TRT suffix (shouldn't exist but defensive)
    ("Ag-RR-868-65.2021.5.02.0020", "Ag-RR-868-65.2021.5.13.0030"),
    # Already correct — skip
    # Partial case without TRT suffix (the actual problem)
    ("TST-Ag-RR-868-65.2021", "TST-Ag-RR-868-65.2021.5.13.0030"),
    # Partial without TST prefix
    ("Ag-RR-868-65.2021", "Ag-RR-868-65.2021.5.13.0030"),
]


def _get_para_text(para_elem) -> str:
    return "".join(t.text or "" for t in para_elem.iter(f"{{{WNS}}}t"))


def fix_para(para_elem, old: str, new: str) -> int:
    full = _get_para_text(para_elem)
    if old not in full or new in full:  # skip if already correct
        return 0
    replaced = full.replace(old, new)
    t_nodes = list(para_elem.iter(f"{{{WNS}}}t"))
    if not t_nodes:
        return 0
    t_nodes[0].text = replaced
    t_nodes[0].set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    for t in t_nodes[1:]:
        t.text = ""
    return full.count(old)


def main():
    bak = DOCX_PATH.with_suffix(f".bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx")
    shutil.copy2(DOCX_PATH, bak)
    print(f"Backup: {bak}")

    doc = Document(DOCX_PATH)
    total = 0
    for old, new in FIXES:
        for para in doc.element.body.iter(f"{{{WNS}}}p"):
            n = fix_para(para, old, new)
            if n:
                ctx = _get_para_text(para)[:100].encode("ascii", "replace").decode()
                print(f"  [OK] '{old}' -> '{new}' ({n}x)")
                print(f"       Now: '{ctx}'")
                total += n

    doc.save(DOCX_PATH)
    print(f"\nSaved: {DOCX_PATH} ({total} fixes)")

    # Post-check
    doc2 = Document(DOCX_PATH)
    checks = {"5.13.0030": 0, "5.02.0020": 0, "Ag-RR-868": 0, "000200": 0}
    for para in doc2.element.body.iter(f"{{{WNS}}}p"):
        txt = _get_para_text(para)
        for k in checks:
            checks[k] += txt.count(k)
    for k, v in checks.items():
        ok = (k in ("5.13.0030", "Ag-RR-868") and v > 0) or (k in ("5.02.0020", "000200") and v == 0)
        print(f"  {'[OK]' if ok else '[WARN]'} '{k}': {v}")


if __name__ == "__main__":
    main()
