"""List all headings in the auditfixed docx to understand structure."""
from docx import Document

doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")

for i, para in enumerate(doc.paragraphs):
    style = para.style.name if para.style else ""
    if "Heading" in style or "heading" in style or "Title" in style:
        print(f"[{i:4d}] ({style:30s}) {para.text[:100]}")
