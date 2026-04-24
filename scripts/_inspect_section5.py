"""Inspect §5 (Discussion/Limitations) structure in the auditfixed docx."""
from docx import Document
from docx.oxml.ns import qn

doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")

in_s5 = False
lines = []
for i, para in enumerate(doc.paragraphs):
    txt = para.text.strip()
    style = para.style.name if para.style else ""
    # Detect §5 start
    if not in_s5 and ("5 " in txt[:8] or txt.startswith("5.") or "Discussion" in txt or "Limitation" in txt):
        if any(h in style for h in ("Heading", "heading", "Title")):
            in_s5 = True
    # Detect §6 start (end of §5)
    if in_s5 and txt and any(h in style for h in ("Heading", "heading", "Title")):
        if txt.startswith("6") or "Conclusion" in txt or "Related" in txt:
            break

    if in_s5:
        lines.append((i, style[:25], txt[:120]))

for idx, (i, s, t) in enumerate(lines):
    print(f"[{i:4d}] ({s:25s}) {t}")
    if idx > 60:
        print("... (truncated)")
        break
