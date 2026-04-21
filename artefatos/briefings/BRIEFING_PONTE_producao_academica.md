# BRIEFING DE PONTE — Projeto: Produção Acadêmica → Q-FENG Validação
**Gerado em:** 19 abril 2026  
**Origem:** Projeto Claude.ai "Produção Acadêmica" (livro + papers derivados)  
**Destino:** Projeto Claude.ai "pos doc" (Q-FENG PoC + validação técnica)  
**Finalidade:** Manter coerência cross-projeto sem fusão de espaços

---

## 1. ESTADO DO LIVRO (canônico)

**Título definitivo (18/abr/2026):**  
PT-BR: *A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle*  
EN: *The Cybernetic Governance of Artificial Intelligence: From Compliance to Control*

**Arquivo canônico:** `C:\Workspace\academico\govern_ai_paper\livro_final\KAMINSKI_livro_versão_final.docx`  
(175 pgs, 8/8 capítulos redigidos)

**Estado em 19/abr/2026:**
- Caps 1–8 completos; correções ARS aplicadas
- Apêndice A (ex-B, mapeamento AGORA) a reintegrar
- Pendentes: mudança de título na capa/folha de rosto, 2 correções CRITICAL + 3 adicionais Field Analysis, ISBN, publicação Amazon KDP
- fsQCA executado em R (QCA 3.24, R 4.5.3): dim1 necessária (1.000); parcimoniosa: dim1+dim3+dim5 (inclS=0.798); 37 figuras + 11 tabelas

**Cap 7 Q-FENG — estado crítico:**
- DOCX canônico difere dos .md de referência — NUNCA confundir
- Estrutura final aprovada: novo §7.2 inserido manualmente via Word (copy-paste de `cap7_qfeng_v5_para_docx.md`)
- Arquitetura validada: 3 níveis recursivos (Macro/Meso/Micro), 5 canais inter-nível, motor simbólico Clingo ASP

---

## 2. OUTPUTS DERIVADOS DO LIVRO

### 2a. Paper PT-BR (A1 brasileiro + SSRN WP)
- Audiência: gestores/pesquisadores brasileiros
- Status: estrutura definida no BRIEFING_13

### 2b. Paper EN — ESTRATÉGICO (periódico internacional)
- **Mais importante para posicionamento europeu (pós-doc UGR/DaSCI Granada)**
- Referência de posicionamento: Profa. Natalia (DaSCI/Granada), Paco Herrera (potencial referee)
- Tom: técnico-formal com Q-FENG como contribuição central
- Título possível: "Compliance-by-Construction" (distinto do livro)
- BRIEFING detalhado em: `C:\Workspace\academico\govern_ai_paper\artefatos\briefings\BRIEFING_13_paper_en_derivado.md`

### 2c. Livro Amazon (editorial)
- Derivado do DOCX canônico; tom acessível

---

## 3. CITAÇÃO CANÔNICA WP Q-FENG (usar em todos os outputs)

KAMINSKI, Ricardo S. *Quantum-Fractal Neurosymbolic Governance (Q-FENG): A Cybernetic Architecture for Ontological Friction Mitigation in Sociotechnical Systems of Critical Infrastructure.* SSRN, 17 mar 2026.  
DOI: 10.2139/ssrn.6433122 | URL: https://ssrn.com/abstract=6433122

---

## 4. CONCEITOS ORIGINAIS DO AUTOR (uso rigoroso obrigatório)

| Conceito | Definição operacional |
|---|---|
| **STAC** (Stabilized Sociotechnical Agency Configurations) | Configurações sociotécnicas que se estabilizam após junções críticas via disputa, negociação e sedimentação material/institucional. **Atribuição obrigatória**: conceito original do autor (tese 2025) |
| **Tensão Triádica** | Tensão entre dimensões de governança — ver `/mnt/project/Tensao_Triadica.md` |
| **Junções Críticas** | Ver `/mnt/project/Juncoes_Criticas.md` |
| **Compliance-by-construction** | Abordagem construtiva (Kaminski) vs. compliance-by-design preventivo (Cavoukian) |
| **Fricção Ontológica** | Conflito entre predições estocásticas e normas institucionais — detectada via ângulo θ no Q-FENG |
| **Falha de execução vs. constitucional** | Distinção tipológica original: falha de execução = sinal algédônico gerado mas não escalado; falha constitucional = sinal estruturalmente impossível por ausência de predicados soberanos |

---

## 5. RESTRIÇÕES DE PORTUGUÊS BRASILEIRO (CRÍTICO)

- **NUNCA** português europeu: proibido *reflectindo, efectivo, directa, nomeadamente, reflecte*
- **SEMPRE** PT-BR: *refletindo, efetivo, direta, especificamente*
- Diacríticos obrigatórios em todos os formatos (HTML, SVG, Markdown, Python)
- Encoding UTF-8 em todos os arquivos gerados

---

## 6. INTERFACE COM O PoC DE VALIDAÇÃO (este projeto)

O livro (Cap 7 especialmente) e o WP Q-FENG são os **documentos de especificação** do PoC.  
A validação empírica do PoC é o que ancora a credibilidade do paper EN.  
**Fluxo de dependência:**

```
PoC validado → evidência computacional → paper EN robusto → posicionamento pós-doc
```

**Casos de validação definidos:**
1. Brasil SUS — Manaus 2021 (falha de execução)
2. EUA Medicaid — Obermeyer et al. 2019 (falha constitucional)
3. EU AI Act (falha de operacionalização)
4. Opcional: PRONAF/DAP/CAF — agricultura familiar brasileira (transferência cross-domain)

**Workspace PoC:** `C:\Workspace\pessoal\qfeng_validacao\`  
**Pipeline C1:** cinco estágios E1→E5 (PyMuPDF/BeautifulSoup4, litellm+Pydantic v2, Clingo, Streamlit/Jupyter, testes simbólicos)

---

*Para detalhes do PoC, ver briefings internos deste projeto (pos doc).*  
*Para detalhes editoriais do livro, ver BRIEFING_13 e arquivos do projeto "Produção Acadêmica".*
