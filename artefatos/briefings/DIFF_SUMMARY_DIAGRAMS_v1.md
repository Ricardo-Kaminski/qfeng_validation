# DIFF_SUMMARY — Inserção de Diagramas v1

**Data:** 2026-04-24\
**Canonical (entrada):** PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx\
**Saída:** PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed_diagrams_v1.docx\
**Scripts:** scripts/insert_diagrams_v2.py + scripts/\_fix_diagram4_prose.py

---

## 1. Inserções aplicadas (5 novos diagramas)

Posição finalDiagramaSVG fonteÂncora no DOCX§SeçãoDiagram 4FiguraA8 — θ instantâneo vs θ\_eff`FiguraA8_Theta_EN_clean.svg`Após "where γ &gt; 0 is the anticipatory weight and"§3.2 MarkovianDiagram 6Triadic Tension`Diagram7_Triadic_Tension_clean.svg`Após "references a non-existent precedent or phantom citation, so the grounding predicate cannot be derived."§3.5 Failure TypologyDiagram 7MLOps Pipeline`Diagram5_MLOps_Pipeline_clean.svg`ANTES de "The pipeline's entry point is the ScopeConfig schema"§4 introDiagram 8Neurosymbolic Thermo`Diagram6_Neurosymbolic_Thermo_clean.svg`Após "constitutional failures arise when a required sovereign predicate is absent from the corpus; execution failures arise when..."§4.4 E4 HITLDiagram 9Equity Map`Diagram9_Equity_Map_clean.svg`Após "This scenario evaluates a structural pattern in Brazilian health policy: the concentration of SUS specialist services"§5.2 C3

**DPI de conversão:** 300 dpi via cairosvg\
**FiguraA8 traduzido:** `FiguraA8_Theta_EN_clean.svg` gerado com substituições PT→EN:

- `Tempo (τ)` → `Time (τ)`
- `Zona HITL` → `HITL Zone`
- `Zona cinzenta` → `Grey Zone`
- `θ_t (instantâneo)...` → `θ_t (instantaneous)...`
- `projeção futura — trajetória de deterioração` → `forward projection — deterioration trajectory`
- `dispara Circuit Breaker` → `triggers Circuit Breaker`
- `Figura A8 — θ instantâneo vs. θ efetivo...` → `Diagram 4 — Instantaneous θ vs. effective θ_eff...`

---

## 2. Referências cruzadas atualizadas

LocalizaçãoTexto antigoTexto novoTipop151 (§3.4 prose INS-4)"Diagram 4 illustrates the topology of L_Global""Diagram 5 illustrates the topology of L_Global"Xref prosep153 (§3.4 caption)"Diagram 4. Conceptual loss landscape...""Diagram 5. Conceptual loss landscape..."Captionp309 (§5.3 prose INS-5)"reconstructed in Diagram 5 as a two-track""reconstructed in Diagram 10 as a two-track"Xref prosep311 (§5.3 caption)"Diagram 5. Manaus oxygen crisis...""Diagram 10. Manaus oxygen crisis..."Caption

**Total de ocorrências atualizadas:** 4 (2 captions + 2 referências em prosa)

---

## 3. Integridade do documento

MétricaOriginalV1ΔParágrafos499514+15Imagens embutidas1217+5Diagramas (Caption)510+5Figures (Caption)770Tables (Caption)880Tamanho do arquivo2981 KB2906 KB−75 KBOrdem Diagrams 1–10—✅ CORRETO—

**Ordem final verificada:** \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\] ✅\
**Limite de 5 MB:** 2.84 MB ✅

---

## 4. Prosa de conexão adicionada ao DIAGRAM_INSERTION_PROSE.md

KeyDiagramaPalavras aprox.StatusINS-6Triadic Tension (Diagram 6)\~120✅INS-7MLOps Pipeline (Diagram 7)\~130✅INS-8Neurosymbolic Thermo (Diagram 8)\~125✅INS-9Equity Map (Diagram 9)\~125✅INS-10Placeholder para consistência numérica—reservado

**Nota:** O mapeamento INS-N → Diagram-N não é linear para as novas inserções:

- INS-8 (no arquivo) → Diagram 8 (Neurosymbolic Thermo) — conforme numeração de sessão
- INS-9 (no arquivo) → Diagram 9 (Equity Map) — conforme numeração de sessão
- A prosa do Diagram 4 (FiguraA8) foi gerada inline no script \_fix_diagram4_prose.py e inserida diretamente

---

## 5. Lacunas de auditoria (resumo — ver AUDIT_DIAGRAM_INSERTION_v1.md)

PrioridadeQuantidadeLocalizaçãoAlta4D4 (redundância α(t)), D6 (transição §3→§4), D7 (heading→diagrama), D9 (posicionamento)Média2D3 (justaposição com Table 1), D8 (justaposição thermo→estatísticas)Baixa4D1, D2, D5, D10

**Ação recomendada:** Ricardo deve revisar as 4 lacunas de alta prioridade antes da submissão Zenodo→SSRN→arXiv.

---

## 6. Próximos passos (pós-validação de Ricardo)

1. Abrir `_diagrams_v1.docx` no Word e inspecionar visualmente os 10 diagramas in situ
2. Endereçar as 4 lacunas de alta prioridade identificadas em AUDIT_DIAGRAM_INSERTION_v1.md
3. Regenerar markdown mirror: `python scripts/extract_docx_to_md.py`
4. Commit: `git add docs/papers/PAPER1_QFENG_FINAL_..._diagrams_v1.docx artefatos/briefings/`
5. Promover para canônico (renomear/sobrescrever) após validação
6. Iniciar pipeline Zenodo→SSRN→arXiv→IPR
