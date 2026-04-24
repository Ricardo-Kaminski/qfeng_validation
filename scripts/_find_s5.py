"""Find §5 discussion/limitations area in docx."""
from docx import Document

doc = Document("docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx")
paras = doc.paragraphs
total = len(paras)
print(f"Total paragraphs: {total}")

# Find headings
headings = []
for i, p in enumerate(paras):
    s = p.style.name or ""
    if "Heading" in s:
        headings.append((i, s, p.text[:80].encode("ascii", "replace").decode()))

# Print last 10 headings
print("\nLast 10 headings:")
for h in headings[-10:]:
    print(f"  [{h[0]:4d}] {h[1]:20} | {h[2]}")

last_h = headings[-1][0]
print(f"\nParagraphs after last heading (index {last_h}):")
for i in range(last_h, min(last_h + 100, total)):
    t = paras[i].text.strip()
    s = (paras[i].style.name or "")[:20]
    if t:
        print(f"  [{i:4d}] {t[:100].encode('ascii', 'replace').decode()}")

# Also search for key terms
print("\n\nSearch for 'limitation', 'disclosure', 'future work', 'conclusion':")
for i, p in enumerate(paras):
    t = p.text.lower()
    if any(kw in t for kw in ["limitation", "disclosure", "future work", "conclusion", "psi_n source", "synthetic"]):
        print(f"  [{i:4d}] {p.text[:120].encode('ascii', 'replace').decode()}")
