# Auditoria de Prosa Adjacente — Inserção de Diagramas v1
**Data:** 2026-04-24  
**Documento alvo:** PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed_diagrams_v1.docx  
**Diagramas auditados:** Diagram 1–10 (5 já presentes + 5 novos)

---

## Instruções de leitura

Para cada ponto de inserção:
- **Local**: seção + parágrafo âncora
- **Lacunas identificadas**: prosa que assume conexão visual não explicitada após a inserção
- **Sugestão**: o que Ricardo deve avaliar (sem redigir texto)

---

## Diagrams 1–5 (já inseridos na sessão anterior)

### Diagram 1 — §1 Introduction
**Local:** Após "This paper presents the Q-FENG C1 pipeline"  
**Lacunas identificadas:**
- O parágrafo logo após o Diagram 1 continua com a lista de contribuições (numbered bullets). A transição visual → lista é abrupta: o leitor vê o ciclo cibernético e depois é jogado diretamente em "Our contributions are:". Não há parágrafo de volta ao texto narrativo.
- A prosa de conexão fala em "three distinct flows" mas o Diagram 1 pode ter 4 ou mais setas dependendo da versão SVG. Verificar coerência count.

**Sugestão:** Ricardo deve avaliar se inserir meia frase de ponte entre o caption do Diagram 1 e o início da lista de contribuições melhora a fluidez.

---

### Diagram 2 — §2.7 Fractal VSM
**Local:** Após "Mapping the full Q-FENG C1 architecture to the VSM systems clarifies the governance role of each pipeline stage"  
**Lacunas identificadas:**
- O parágrafo imediatamente posterior ao Diagram 2 retoma a narrativa do VSM sem referenciar o diagrama explicitamente. Há uma frase implícita como "as shown" que ficou pressuposta.
- O trecho sobre "fractal recursion" na prosa de conexão (INS-2) usa "Micro/Meso/Macro" mas o diagrama pode usar ordem inversa. Verificar consistência terminológica.

**Sugestão:** Ricardo deve avaliar se referenciar "Diagram 2 above" na primeira sentença do parágrafo pós-diagrama adiciona clareza ou é redundante.

---

### Diagram 3 — §3.1 (antes de Table 1)
**Local:** Após "The Q-FENG thresholds partition this range into three governance regimes (Table 1):"  
**Lacunas identificadas:**
- Diagram 3 fica entre a frase âncora e a Table 1. O leitor vê: frase → diagrama → caption → tabela. A justaposição é densa. A Table 1 repete em tabular form o que o Diagram 3 já mostra geometricamente — podem parecer redundantes para revisores.
- A prosa de conexão (INS-3) usa "formal partition" mas a table só vem depois. O leitor pode se confundir com a ordem de "formal" vs "geometric" explanations.

**Sugestão:** Ricardo deve avaliar se um parágrafo de transição breve entre o caption do Diagram 3 e Table 1 (indicando que a tabela formaliza o que o diagrama ilustra geometricamente) é necessário ou se a justaposição é deliberada e suficientemente clara.

---

### Diagram 4 — §3.2 após Eq. 5 (FiguraA8 — NOVO)
**Local:** Após "where γ > 0 is the anticipatory weight and E[θ(t+k)] is the expected mean"  
**Lacunas identificadas:**
- O parágrafo que segue o Diagram 4 no documento é "The adaptive memory has the following governance semantics: when Δpressão(t) > 0 (deteriorating), α(t) → 1...". Esta prosa DUPLICA parcialmente o que o caption do Diagram 4 já descreve (α(t) sensitivity). Risco de redundância semântica.
- A prose de conexão (INS-8/FiguraA8) menciona "γ > 0 in the full form of Eq. A10" mas o Diagram 4 pode não mostrar a trajetória γ>0 explicitamente (a implementação usa γ=0). Verificar se caption é claro que o diagrama é conceitual, não da implementação PoC.

**Sugestão:** Ricardo deve avaliar se o parágrafo sobre "adaptive memory semantics" (logo após Diagram 4) precisa de uma sentença inicial que remeta ao diagrama para evitar que pareça repetição.

---

### Diagram 5 — §3.4 Loss Landscape
**Local:** Após "when L exceeds the CB threshold, mandatory intervention is activated"  
**Lacunas identificadas:**
- O parágrafo de prosa de conexão (INS-4, agora com "Diagram 5") é seguido pelo Diagram 5 e depois pela seção "Failure Typology". Não há parágrafo de fechamento do Diagram 5 — o texto pula direto para a nova seção. A transição visual → próxima seção é abrupta.

**Sugestão:** Ricardo deve avaliar se uma sentença de ponte ("The failure typology operationalises the regimes visually distinguished in Diagram 5 as formal predicate patterns") entre o caption do Diagram 5 e o início de §3.5 melhora a coesão.

---

## Diagrams 6–10 (novos — inseridos nesta sessão)

### Diagram 6 — §3.5 Failure Typology
**Local:** Após "references a non-existent precedent or phantom citation, so the grounding predicate cannot be derived. Example: Mata v. Avianca phantom citation (T-CLT-01)."  
**Lacunas identificadas:**
- Diagram 6 é o ÚLTIMO elemento de §3.5. Após o caption, o documento entra em §4 "The C1 Pipeline". A transição de uma tipologia visual (Diagram 6) para a seção de pipeline é completamente abrupta — não há parágrafo de síntese de §3 nem de anúncio de §4.
- A prosa de conexão (INS-6) descreve "três regiões assimétricas" mas não referencia os exemplos reais (C2, T-CLT-01, C7) que serão usados em §5. Uma referência adiantada ("as demonstrated in the scenarios of §5") poderia fortalecer a antecipação.

**Sugestão:** Ricardo deve avaliar se um parágrafo de síntese de §3 (fechando o argumento matemático antes de §4) e/ou uma sentença de antecipação dos cenários de §5 seria necessário entre o caption do Diagram 6 e o heading de §4.

---

### Diagram 7 — §4 Introdução (antes de E0)
**Local:** Inserido ANTES de "The pipeline's entry point is the ScopeConfig schema"  
**Lacunas identificadas:**
- Diagram 7 não tem parágrafo âncora que o preceda no texto — ele foi inserido como o primeiro elemento da seção após o heading "# The C1 Pipeline: Stages E0–E4". Um heading imediatamente seguido de um diagrama (sem parágrafo de contexto) pode ser desconcertante para o leitor.
- A prosa de conexão (INS-7) menciona "Parquet persistence" e "Pydantic schemas" — esses termos aparecem novamente em §4.1 E0. Há risco de repetição antes de os conceitos serem definidos.
- O Diagram 7 menciona E5 no título do pipeline mas §4 só cobre E0–E4 (o título da seção é "Stages E0–E4"). Verificar se o caption de Diagram 7 ("E0–E5") conflita com o heading de seção.

**Sugestão:** Ricardo deve avaliar: (a) se um parágrafo de introdução à seção §4 deve preceder o Diagram 7 (para que não haja heading→diagrama direto); (b) se "E0–E5" no caption de Diagram 7 precisa ser "E0–E4" para consistência com o heading.

---

### Diagram 8 — §4.4 E4 HITL
**Local:** Após "constitutional failures arise when a required sovereign predicate is absent from the corpus; execution failures arise when the sovereign predicate exists but the execution chain is blocked or misgrounded."  
**Lacunas identificadas:**
- O parágrafo após o Diagram 8 é "Pipeline survival E2 → E3 → E4. Across both tracks...". Esse parágrafo discute números de atoms (10,142 DeonticAtoms, 49.0% survival rate). A justaposição de uma metáfora termodinâmica (Diagram 8) com estatísticas de pipeline é brusca.
- A prosa de conexão (INS-9) menciona "SOVEREIGN raises a high-energy barrier" mas o Diagram 8 pode mostrar apenas dois níveis de energia genéricos, sem rotulação explícita de SOVEREIGN/ELASTIC. Se o leitor olha o diagrama esperando ver essas labels e não as encontra, a prosa cria expectativa não cumprida.

**Sugestão:** Ricardo deve avaliar se (a) uma sentença de transição entre o caption do Diagram 8 e "Pipeline survival" é necessária; (b) os rótulos SOVEREIGN/ELASTIC estão explicitamente visíveis no Diagram8_Neurosymbolic_Thermo_clean.svg.

---

### Diagram 9 — §5.2 C3 Regional SUS Concentration
**Local:** Após "This scenario evaluates a structural pattern in Brazilian health policy: the concentration of SUS specialist services (oncology, cardiac surgery, high-complexity imaging) in capitals and large metropolitan centres..."  
**Lacunas identificadas:**
- O parágrafo âncora é o PRIMEIRO parágrafo do C3 narrative. Inserir o Diagram 9 logo após o primeiro parágrafo (antes da derivação de predicados Clingo e dos ψ_N/ψ_S valores) pode interromper o fluxo argumentativo do cenário antes de ele ser completamente apresentado.
- A prosa de conexão (INS-10) menciona "Art. 198 III SUS regionalisation deficit" como um dos fatores visuais do mapa — mas a discussion de Art. 198 III no texto principal só aparece mais abaixo, depois do Diagram 9. Referência adiantada pode confundir o leitor que ainda não viu o Art. 198 III ser introduzido.
- O Diagram 9 (Equity Map) provavelmente usa dados sintéticos (calibração de 27 documentos normativos) — verificar se o caption ou a prosa de conexão esclarece que é representação normativa, não um mapa geográfico com dados reais IBGE/DATASUS.

**Sugestão:** Ricardo deve avaliar: (a) se mover o Diagram 9 para APÓS os predicados Clingo (após "The ψ_N vector for C3...") seria melhor posicionamento narrativo; (b) se o caption precisa de nota "(representação normativa sintética)" para evitar leitura equivocada como mapa empírico.

---

### Diagram 10 — §5.3 Manaus Timeline
**Local:** Inserido antes de "Three features of this series are theoretically significant" (posicionamento original, inalterado)  
**Lacunas identificadas:**
- O parágrafo após o Diagram 10 é "Three features of this series are theoretically significant: (i) early CB activation in October 2020 (3 months before the calamity declaration)...". Esse parágrafo resume o que o Diagram 10 já mostra visualmente. A estrutura funciona mas pode ser redundante.
- A renumeração de Diagram 5 → Diagram 10 afeta a referência "Diagram 5 as a two-track" → "Diagram 10 as a two-track" no parágrafo de prosa de conexão (INS-5). Verificar se essa referência está corretamente atualizada no _diagrams_v1.docx (confirmado: p309 "Diagram 10 as a two-track").

**Sugestão:** Ricardo deve avaliar se o "Three features" paragraph pode ser encurtado para eliminar repetição com o que já é visualmente óbvio no Diagram 10.

---

## Resumo de lacunas por seção

| Seção | Diagrama | Tipo de lacuna | Prioridade de revisão |
|-------|----------|---------------|----------------------|
| §1 Introduction | D1 | Transição visual→lista de contribuições | Baixa |
| §2.7 Fractal VSM | D2 | Referência pós-diagrama ausente | Baixa |
| §3.1 | D3 | Justaposição densa D3+Table 1 | Média |
| §3.2 | D4 (FiguraA8) | Redundância com parágrafo sobre α(t) semantics | **Alta** |
| §3.4 | D5 (Loss Landscape) | Ausência de parágrafo de fechamento | Baixa |
| §3.5 | D6 (Triadic Tension) | Transição §3→§4 abrupta | **Alta** |
| §4 intro | D7 (MLOps) | Heading direto→diagrama; conflito E0–E4 vs E0–E5 | **Alta** |
| §4.4 | D8 (Thermo) | Justaposição metáfora→estatísticas pipeline | Média |
| §5.2 | D9 (Equity Map) | Posicionamento antes dos predicados; dados sintéticos | **Alta** |
| §5.3 | D10 (Timeline) | Redundância com "Three features" paragraph | Baixa |

**Lacunas de alta prioridade (4):** D4 redundância α(t), D6 transição §3→§4, D7 heading→diagrama, D9 posicionamento e dados.
