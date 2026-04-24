"""Show full text of paragraph 308 (Mandatory disclosure 1)."""
from docx import Document

doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")
paras = doc.paragraphs

# Show para 307-310 in full
for i in range(305, 313):
    if i < len(paras):
        t = paras[i].text
        if t.strip():
            print(f"[{i}]")
            print(t.encode("ascii", "replace").decode())
            print("---")
