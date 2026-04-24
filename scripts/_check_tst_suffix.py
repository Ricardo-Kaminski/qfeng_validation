from docx import Document
WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")

checks = {
    "5.02.0020": 0,   # wrong TRT-2 suffix from old case
    "5.13.0030": 0,   # correct TRT-13 suffix from new case
    "Ag-RR-868": 0,   # new case number
    "000200": 0,       # old case number fragment
}

for para in doc.element.body.iter(f"{{{WNS}}}p"):
    txt = "".join((t.text or "") for t in para.iter(f"{{{WNS}}}t"))
    for k in checks:
        checks[k] += txt.count(k)

for k, v in checks.items():
    status = "OK" if (k in ("5.13.0030", "Ag-RR-868") and v > 0) or (k in ("5.02.0020", "000200") and v == 0) else "WARN"
    print(f"[{status}] '{k}': {v} occurrences")
