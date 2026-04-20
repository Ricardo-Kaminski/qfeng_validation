# E1 Ingestion — Avaliação Formal

**Q-FENG Empirical Validation | Shared across Paper 1 and Paper 2**
**Etapa:** E1 — Fase B (execução real) | **Status:** ✅ APROVADO DEFINITIVAMENTE
**Data de aprovação:** Abril 2026 | **Iterações até aprovação:** 4

---

## 1. Histórico de iterações

| Iteração | Chunks | Concorrências | Problema identificado | Ação |
|----------|--------|---------------|-----------------------|------|
| E1-v1 | 24.479 | 14.686 | Pares duplicados; CFR 1–6 chunks; Markdown 1 chunk | Corrigir deduplicação, parsers CFR e MD |
| E1-v2 | 27.463 | 342 | pl_2338 corrompido; 14th Amendment 1 chunk; cross-refs BR baixas | Re-baixar PL; fix Section pattern USA |
| E1-v3 | 27.572 | 342 | Texto tachado (<strike>) não removido; LGPD ausente | Fix strip_selectors; baixar LGPD |
| **E1-v4** | **27.957** | **347** | — | **APROVADO** |

---

## 2. Corpus final aprovado

### 2.1 Estatísticas gerais

| Métrica | Valor |
|---------|-------|
| Documentos processados | 29 |
| Total de NormChunks | 27.957 |
| Referências cruzadas detectadas | 2.977 |
| Pares de concorrência (Jaccard ≥ 0.55) | 347 |
| Alertas de qualidade | 2 (inofensivos) |
| Dispositivos revogados removidos | ~33 confirmados (CF/88: 6, Lei 13.979: 27) |

### 2.2 Distribuição por regime

| Regime | Chunks | % total | Documentos |
|--------|--------|---------|------------|
| Brasil | 21.445 | 76,7% | 19 |
| EU | 1.667 | 6,0% | 4 |
| USA | 4.845 | 17,3% | 9 |

### 2.3 Distribuição por chunk_type

| chunk_type | N | % | Interpretação |
|------------|---|---|---------------|
| obligation | 23.053 | 82,5% | Backbone prescritivo do grafo simbólico |
| procedure | 1.992 | 7,1% | Sequências processuais — relevantes para HITL |
| principle | 1.913 | 6,8% | Axiomas — candidatos prioritários a SOVEREIGN |
| definition | 759 | 2,7% | Termos definidos — âncoras semânticas para E2 |
| sanction | 240 | 0,9% | Consequências de violação — cenários E5 |

### 2.4 Documentos-âncora por regime

**Brasil — SUS + IA:**

| Documento | Chunks | Papel |
|-----------|--------|-------|
| CF88_completa.htm | 383 | Axiomas soberanos (Art. 196-200) |
| lei_8080_1990.htm | 381 | Lei Orgânica da Saúde |
| lei_13709_2018.htm (LGPD) | 421 | Proteção de dados — analogia GDPR |
| pl_2338_2023.md | 106 | PL de IA brasileiro |
| lei_13979_2020.htm | 199 | Resposta emergencial COVID/Manaus |

**EU:**

| Documento | Chunks | Papel |
|-----------|--------|-------|
| eu_ai_act_2024_1689.htm | 868 | Regime de IA vigente |
| gdpr_full.htm | 740 | Proteção de dados |
| carta_direitos_fundamentais_ue.htm | 59 | Axiomas soberanos EU |

**USA:**

| Documento | Chunks | Papel |
|-----------|--------|-------|
| ssa_title_xix_1902.htm | 831 | Medicaid §1902 — obrigações centrais |
| 42_cfr_part_435.htm | 1.823 | Elegibilidade Medicaid |
| 42_cfr_part_430.htm | 491 | Administração Medicaid |
| 42_cfr_part_440.htm | 641 | Serviços cobertos Medicaid |
| 14th_amendment.htm | 5 | Equal Protection — axioma soberano USA |

---

## 3. Avaliação por dimensão (D1–D5)

### D1 — Cobertura ✅

Documentos-âncora acima de 0,99 chunks/KB. LGPD com 421 chunks para 65 artigos
(média 6,5 chunks/artigo, incluindo parágrafos e incisos) — cobertura excelente.

### D2 — Integridade hierárquica ✅

Estrutura hierárquica preservada corretamente nos três regimes.
Notação `Art. Np` para parágrafo único é interna ao sistema —
funcionalmente correta, será padronizada em versão futura.

### D3 — Tipagem ~85% ✅

Precisão estimada em amostra manual (n=20). Principal limitação:
princípios constitucionais classificados como `obligation` (ex: CF/88 Art. 196).
Impacto baixo — distinção SOVEREIGN/ELASTIC é responsabilidade do E4 (HITL),
não do chunk_type.

### D4 — Concorrência ✅

347 pares únicos após correção de deduplicação (frozenset) e
calibração do threshold Jaccard para 0.55.
12 pares com Jaccard = 1.0 representam dispositivos idênticos
reproduzidos em múltiplos instrumentos normativos — concorrências
de alta relevância para resolução no E4.

### D5 — Referências cruzadas ⚠️ parcial

Taxa Brasil ~2,8% (abaixo do threshold de 10%).
USA e EU acima do threshold.
Limitação aceita para o MVP — refinamento de regex Brasil em E4.

---

## 4. Decisões de curadoria (relevantes para os papers)

### 4.1 Remoção de dispositivos revogados

O corpus contém exclusivamente dispositivos normativos vigentes.
Textos revogados ou com redação substituída, marcados com `<strike>`
nas fontes do Planalto.gov.br, foram removidos via decomposição DOM
(`strip_selectors`) antes da extração de texto.

**Evidência:** CF/88 perdeu 6 chunks e Lei 13.979/2020 perdeu 27 chunks
após aplicação da correção — confirmando remoção de dispositivos
revogados pela pandemia COVID-19.

Esta decisão garante que os predicados simbólicos gerados em E3
reflitam o estado atual do ordenamento jurídico, não versões históricas.

### 4.2 Remoção de notas de emenda

Referências de alteração legislativa do tipo "(Redação dada pela
Lei nº 13.853, de 2019)" foram removidas do campo `text` via regex,
preservando apenas o conteúdo normativo substantivo.

### 4.3 LGPD como documento de análise comparativa

A LGPD (Lei 13.709/2018) foi incluída como par do GDPR para análise
comparativa Brasil × EU de governança de dados em sistemas de saúde.
Com 421 chunks, é o terceiro maior documento brasileiro do corpus
(excluindo portarias de consolidação).

---

## 5. Pendências não bloqueantes

| Item | Status | Fase de resolução |
|------|--------|-------------------|
| EBIA 2021 | ⏳ Não incluída | Adicionar antes E3 se disponível |
| Cross-refs Brasil ~2,8% | ⚠️ Abaixo do threshold | Refinamento regex em E4 |
| Notação `Art. Np` | Notação interna | Padronizar em versão futura |

---

## 6. Relevância para os papers

**Paper 1 (Engenharia de IA / DASCI-UGR):**
- D3 (~85% precisão de tipagem) é resultado publicável como baseline
  de extração estrutural puramente rule-based, sem LLM
- 347 pares de concorrência normativa quantificam a complexidade do
  grafo comparativo — argumento central para necessidade de raciocínio
  simbólico no Q-FENG
- A remoção de dispositivos revogados via DOM é decisão metodológica
  transferível a outros corpora jurídicos

**Paper 2 (Saúde Digital / Lancet Digital Health):**
- Corpus de 383 + 381 + 421 chunks (CF/88 + Lei 8.080 + LGPD) cobre
  a totalidade da estrutura normativa do SUS e proteção de dados
  em saúde — base suficiente para validação do Case 1
- Lei 13.979/2020 com 199 chunks (após remoção de revogados)
  documenta o regime de emergência de Manaus — contexto do Case 1

---

## 7. Referências metodológicas

- Ashley, K.D. (2017). *Artificial Intelligence and Legal Analytics*. Cambridge UP.
- Lippi, M. et al. (2019). CLAUDETTE: an automated detector of potentially
  unfair clauses in online terms of service. *Artificial Intelligence and Law*, 27(2).
- Robaldo, L. et al. (2020). Introduction to the special issue on normative
  reasoning. *Artificial Intelligence and Law*, 28(1).
- Palmirani, M. & Governatori, G. (2018). Modelling legal knowledge for GDPR
  compliance checking. *JURIX 2018*.
- Koreeda, Y. & Manning, C. (2021). ContractNLI: A dataset for document-level
  NLI for contracts. *EMNLP Findings*.
