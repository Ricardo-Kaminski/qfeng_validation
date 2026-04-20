# Paper 1 — Methodology (AI Engineering)

**Target venues:** IEEE TNNLS | JAIR | ECAI | IJCAI | EPIA
**Dialogue:** DASCI/UGR (Herrera group) | UDC | Mila Montreal
**Working title:** *Q-FENG: A Quantum-Fractal Neurosymbolic Architecture
for Comparative Normative Governance of AI Systems*

---

## Pipeline C1 — Métodos de extração normativa

### E1 — Ingestion

*(ver docs/shared/e1_evaluation.md para avaliação completa)*

O módulo E1 implementa parsing estrutural hierárquico de documentos normativos
em formato HTML e PDF, sem uso de LLM. A estrutura hierárquica é extraída via
expressões regulares específicas por regime normativo (Brasil: Art./§/inciso/alínea;
EU: Article/paragraph/point; USA: Section/(a)(1)/(A)(i)), produzindo objetos
NormChunk com identificadores determinísticos SHA-256.

**Resultado:** 27.572 NormChunks extraídos de 28 documentos em 3 regimes,
com ~85% de precisão na classificação de chunk_type (avaliação manual, n=20)
e 342 pares de concorrência normativa identificados via similaridade Jaccard ≥ 0.55.

**A incluir quando disponível:**
- [ ] Resultados E2 — extração deontica
- [ ] Resultados E3 — tradução simbólica
- [ ] Resultados E4 — HITL + classificação soberania
- [ ] Resultados E5 — testes simbólicos Clingo
