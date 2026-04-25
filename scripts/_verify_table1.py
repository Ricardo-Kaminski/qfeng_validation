import docx
doc = docx.Document(r"C:\Workspace\academico\qfeng_validacao\artefatos\briefings\TABLE1_S2-8_Fractal_Mapping.docx")
for t in doc.tables:
    for i, row in enumerate(t.rows):
        print(f"row{i}: {row.cells[0].text[:25]!r}")
