from docx import Document
WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")
hits = []
for para in doc.element.body.iter(f"{{{WNS}}}p"):
    txt = "".join((t.text or "") for t in para.iter(f"{{{WNS}}}t"))
    if "Ag-RR-868" in txt or "5.02.0020" in txt or "000200" in txt:
        hits.append(txt[:200])
for h in hits:
    print(h.encode("ascii", "replace").decode())
print(f"Total hits: {len(hits)}")
