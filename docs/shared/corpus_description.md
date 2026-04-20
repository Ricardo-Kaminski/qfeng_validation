# Corpus Normativo — Descrição Formal

**Q-FENG Empirical Validation | Shared across Paper 1 and Paper 2**
**Última atualização:** Abril 2026 | **Etapa:** Pós-E1

---

## 1. Justificativa da seleção do corpus

O corpus foi construído para validação comparativa da arquitetura Q-FENG em
três regimes normativos com características distintas de governança de saúde
pública e inteligência artificial:

| Regime | Sistema de saúde | Regime de IA | Força constitucional |
|--------|-----------------|--------------|----------------------|
| **Brasil** | SUS (universal, público) | PL 2338/2023 (em tramitação) | Art. 196 CF/88 |
| **EU** | NHS-like (variável por estado-membro) | EU AI Act 2024/1689 (vigente) | Carta de Direitos Fundamentais |
| **USA** | Medicaid (condicional, público-privado) | Sem lei federal específica de IA | 14th Amendment Equal Protection |

Esta triangulação permite testar a **invariância fractal** do Q-FENG: a mesma
arquitetura de governança deve produzir comportamentos coerentes em regimes com
premissas constitucionais e estruturas normativas radicalmente distintas.

---

## 2. Corpus processado (E1 final)

### 2.1 Estatísticas gerais

| Métrica | Valor |
|---------|-------|
| Documentos processados | 28 |
| Total de NormChunks | 27.572 |
| Referências cruzadas | 2.933 |
| Pares de concorrência (Jaccard ≥ 0.55) | 342 |
| Alertas de qualidade | 2 (inofensivos) |

### 2.2 Distribuição por regime

| Regime | Chunks | % total | Documentos |
|--------|--------|---------|------------|
| Brasil | 21.060 | 76,4% | 18 |
| EU | 1.667 | 6,1% | 4 |
| USA | 4.845 | 17,6% | 9 |

> **Nota metodológica:** O domínio brasileiro é numericamente dominante devido
> às Portarias de Consolidação nº 2 e nº 5/2017 (7.341 e 12.394 chunks
> respectivamente), que consolidam centenas de portarias do MS. Estes documentos
> têm alta granularidade normativa operacional. Para análises comparativas entre
> regimes, utilizar subsets balanceados por documento-âncora (ver §2.4).

### 2.3 Distribuição por tipo de chunk

| chunk_type | N | % | Interpretação |
|------------|---|---|---------------|
| obligation | 22.772 | 82,6% | Normas prescritivas — backbone do grafo simbólico |
| procedure | 1.986 | 7,2% | Sequências processuais — relevantes para HITL |
| principle | 1.836 | 6,7% | Axiomas constitucionais — candidatos a SOVEREIGN |
| definition | 751 | 2,7% | Termos definidos — âncoras semânticas para E2 |
| sanction | 227 | 0,8% | Consequências de violação — para cenários E5 |

### 2.4 Documentos-âncora por regime (análise comparativa)

Para fins de comparação entre regimes, os seguintes documentos são os
**documentos-âncora** — aqueles que melhor representam a estrutura normativa
central de cada regime:

**Brasil — SUS:**
- `lei_8080_1990.htm` — 383 chunks — Lei Orgânica da Saúde (estrutura constitutiva)
- `CF88_completa.htm` — 389 chunks — Constituição Federal (axiomas soberanos)
- `pl_2338_2023.md` — 106 chunks — PL de IA brasileiro (regime em construção)

**EU:**
- `eu_ai_act_2024_1689.htm` — 868 chunks — EU AI Act (regime de IA vigente)
- `gdpr_full.htm` — 740 chunks — GDPR (analogia com LGPD brasileira)
- `carta_direitos_fundamentais_ue.htm` — 59 chunks — axiomas soberanos EU

**USA:**
- `ssa_title_xix_1902.htm` — 831 chunks — Medicaid §1902 (obrigações centrais)
- `42_cfr_part_435.htm` — 1.823 chunks — Elegibilidade Medicaid (detalhe operacional)
- `14th_amendment.htm` — 5 chunks — Equal Protection (axiomas soberanos USA)

### 2.5 Fontes e URLs de origem

| Documento | Fonte | Regime Normativo |
|-----------|-------|-----------------|
| CF88_completa.htm | planalto.gov.br | Constitucional BR |
| lei_8080_1990.htm | planalto.gov.br | Statutory BR |
| lei_8142_1990.htm | planalto.gov.br | Statutory BR |
| lei_8689_1993.htm | planalto.gov.br | Statutory BR |
| lei_13979_2020.htm | planalto.gov.br | Regulatory BR |
| pl_2338_2023.md | camara.leg.br | AI Governance BR |
| portaria_consolidacao_2_2017.htm | saude.gov.br | Regulatory BR |
| portaria_consolidacao_5_2017.htm | saude.gov.br | Regulatory BR |
| pns_2024_2027_metas.md | saude.gov.br | Operational BR |
| ppa_2024_2027_saude_programas.md | planejamento.gov.br | Operational BR |
| l14802-texto.pdf | planalto.gov.br | Statutory BR |
| eu_ai_act_2024_1689.htm | eur-lex.europa.eu | AI Governance EU |
| gdpr_full.htm | eur-lex.europa.eu | Data Protection EU |
| carta_direitos_fundamentais_ue.htm | eur-lex.europa.eu | Constitutional EU |
| pl_2338_2023.htm | camara.leg.br | Comparative |
| ssa_title_xix_1901-1905.htm | law.cornell.edu | Statutory USA |
| 42_cfr_part_430/435/440.htm | law.cornell.edu | Regulatory USA |
| civil_rights_act_title_vi.htm | law.cornell.edu | Constitutional USA |
| 14th_amendment.htm | law.cornell.edu | Constitutional USA |

---

## 3. Atualizações de corpus — 19 abril 2026

### 3.1 Documentos adicionados nesta sessão

| Documento | Localização | Método de obtenção |
|-----------|------------|-------------------|
| portaria_69_2021.htm | brasil/regulamentacao/portarias_manaus_2021/ | bvsms.saude.gov.br (DOU 18/jan/2021) |
| portaria_197_2021.htm | brasil/regulamentacao/portarias_manaus_2021/ | bvsms.saude.gov.br (prt0197_02_02_2021) |
| portaria_268_2021.htm | brasil/regulamentacao/portarias_manaus_2021/ | bvsms.saude.gov.br (texto completo) |
| obermeyer_2019_summary.md | usa/empirical/ | Resumo operacionalizável estruturado |

Ver metodologia completa de obtenção: `docs/shared/corpus_preparation.md`

### 3.2 Pendências resolvidas

| Item | Status anterior | Status atual |
|------|----------------|-------------|
| Portarias Manaus 69/197/268 | ❌ Ausentes | ✅ Incluídas |
| USA empirical (Obermeyer) | ❌ Vazio | ✅ Resumo estruturado |
| LGPD (Lei 13.709/2018) | ⏳ Listada como pendente | ✅ Já incluída (421 chunks em E1-v4) |
| pl_2338_2023.htm | ✅ Corrigido (106 chunks via .md) | ✅ — |
| 14th_amendment.htm | ✅ Corrigido (5 chunks) | ✅ — |

### 3.3 Pendências remanescentes (não bloqueantes)

| Item | Prioridade | Fase de resolução |
|------|-----------|------------------|
| EBIA 2021 | Baixa | Antes de E3, se disponível |
| Cross-refs Brasil ~2,8% | Baixa | Refinamento regex em E4 |
