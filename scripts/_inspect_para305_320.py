"""Show full text of paragraphs 305-325 (mandatory disclosure area)."""
from docx import Document

doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")
paras = doc.paragraphs

for i in range(300, 330):
    if i >= len(paras):
        break
    t = paras[i].text.strip()
    s = (paras[i].style.name or "")[:20]
    if t:
        print(f"[{i:4d}] {t.encode('ascii', 'replace').decode()}")
        print()
