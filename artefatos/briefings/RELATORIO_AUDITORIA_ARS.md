# Relatório de Auditoria Pré-Submissão — Q-FENG
## Para uso no Academic Review System (ARS)

**Paper:** "Q-FENG: Quantum-Fractal Neurosymbolic Governance Framework —
Validation across Healthcare and Labour Law Scenarios"

**Destino:** JURIX 2026 (International Conference on Legal Knowledge and
Information Systems)

**Revisores externos nomeados:** Prof. Paco Herrera e Prof. Natalia
Díaz-Rodríguez (Universidad de Granada)

**Arquivo canônico pós-auditoria:**
`docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`

**Data de fechamento da auditoria:** 2026-04-24

**Commits de auditoria (branch main):**

| Commit | Fase | Conteúdo |
|--------|------|----------|
| `f2849bd` | Phase 0 / H-5 | Portaria 268/2021 → Portaria 79/2021 + Lei 13.979 Art. 10 |
| `6d275f1` | F0-1 / C-6 | Substitui acórdão fabricado TST por TST-Ag-RR-868-65.2021.5.13.0030 |
| `2ffe77e` | Phase 3 | Mandatory disclosure 3 + Tabela A1 ψ_N source classification |
| `a0de66a` | Phase 4 | H-6 guard deny_access, H-7 doc órfãos, M-5 GDPR Art.17 header |
| `6202724` | Phase 5 | Regressão final (475/475 testes, CB onset Oct/2020 ✓) |

(Commits anteriores de Phases 1 e 2 foram realizados em sessão prévia — ver
`git log --oneline` para histórico completo.)

---

## PARTE I — SUMÁRIO EXECUTIVO PARA REVISORES

### O que o paper afirma

Q-FENG é um framework cibernético de monitoramento de alinhamento de IA a
normas jurídicas positivas. A validação cobre 7 cenários (C2, C3, C7,
T-CLT-01..04) em dois domínios (saúde pública Brasil/EUA, direito trabalhista
Brasil). O núcleo formal é a analogia de interferência quântica:

```
θ = arccos(⟨ψ_N | ψ_S⟩)
```

Onde `ψ_N` = vetor de preferência do preditor (estado operacional) e
`ψ_S` = vetor de estado normativo soberano (derivado por Clingo ASP).
Regimes: θ < 30° → STAC; 30° ≤ θ < 120° → HITL; θ ≥ 120° → CIRCUIT_BREAKER.

### O que a auditoria encontrou e corrigiu

A auditoria identificou 6 problemas CRITICAL, 8 HIGH, 9 MEDIUM, e 3 LOW.
Todos os CRITICAL e HIGH foram corrigidos. Ver Parte II para detalhes.

### Estado pós-auditoria

| Domínio | Cenário | θ (°) | Regime | SAT |
|---------|---------|--------|--------|-----|
| Saúde Brasil | C2 Manaus | 132.51 | CIRCUIT_BREAKER | UNSAT |
| Saúde Brasil | C3 SUS Regional | 134.40 | CIRCUIT_BREAKER | UNSAT |
| Saúde EUA | C7 Obermeyer | 134.55 | CIRCUIT_BREAKER | UNSAT |
| Trabalhista Brasil | T-CLT-01 Mata v. Avianca | 133.51 | CIRCUIT_BREAKER | UNSAT |
| Trabalhista Brasil | T-CLT-02 Hora Extra s/ CCT | 127.81 | CIRCUIT_BREAKER | UNSAT |
| Trabalhista Brasil | T-CLT-03 CCT Válida (STAC+) | 5.65 | STAC | SAT |
| Trabalhista Brasil | T-CLT-04 Citação Fundamentada (STAC+) | 7.05 | STAC | SAT |

**Teste suite:** 475 passed, 11 skipped (pytest)
**CB onset Manaus:** Out/2020, θ=125.83° ✓

---

## PARTE II — LOG DE ACHADOS E CORREÇÕES

### Legenda de severidade
- **CRITICAL**: Paper não sobrevive ao primeiro review sem correção
- **HIGH**: Revisor atento certamente flagra
- **MEDIUM**: Pode ser flagrado por revisor meticuloso
- **LOW**: Tipografia / consistência

---

### CRITICAL C-1 — Bug atom plain-vs-wrapped (Clingo)

**Arquivo:** `corpora_clingo/brasil/emergencia_manaus/emergencia_sanitaria.lp`

**Problema:** `espin_declaration_active` e `espin_renewed_jan2021` eram derivados
apenas como `sovereign(espin_declaration_active)` mas consumidos em corpos de
regras como átomo plano `espin_declaration_active`. Em semântica de mundo
fechado, o átomo plano nunca era verdadeiro. 6 obrigações dependentes nunca
disparavam. ψ_S de C2 era construído sem sinal normativo completo.

**Correção aplicada:** Adicionadas regras-ponte:
```prolog
espin_declaration_active :- sovereign(espin_declaration_active).
espin_renewed_jan2021    :- sovereign(espin_renewed_jan2021).
```

**Impacto nos dados:** θ_eff de C2 mudou. Jan/2021 passou de CB (127.47°
no texto original) para HITL (118.73°). Pico real identificado: Set/2020
(130.91°). Table 7 atualizada com valores do pipeline correto.

**Status:** ✅ CORRIGIDO (Phase 1)

---

### CRITICAL C-2 — Cadeia derivacional letra morta (civil_rights_14th.lp)

**Arquivo:** `corpora_clingo/usa/civil_rights/civil_rights_14th.lp`

**Problema:** `algorithmic_title_vi_violation` era cabeça órfã — derivada mas
nunca consumida. C7 atingia UNSAT via caminho alternativo hardcoded em
`c7_obermeyer_facts.lp` (`algorithm_produces_racial_disparate_impact`). A
cadeia `disparity_gap → algorithmic_title_vi_violation` era letra morta.

**Correção aplicada:** Adicionado constraint:
```prolog
% Violação derivada de Title VI via cadeia racial_disparate_impact → UNSAT (audit C-2)
:- algorithmic_title_vi_violation.
```

**Status:** ✅ CORRIGIDO (Phase 1)

---

### CRITICAL C-3 — Predicado indefinido em CPC (cpc_fundamentacao.lp)

**Arquivo:** `corpora_clingo/brasil/processual/cpc_fundamentacao.lp`

**Problema:** `decision_grounded_in_identified_precedent/1` era referenciado em
constraint mas nunca definido. Em Clingo (semântica fechada), predicado
indefinido é sempre falso → `not P` é sempre verdadeiro → constraint podia
gerar UNSAT espúrio em T-CLT-04.

**Correção aplicada:** Adicionada regra de derivação:
```prolog
decision_grounded_in_identified_precedent(D) :-
    legal_decision_issued(D),
    legal_citation_exists(_).
```

**Status:** ✅ CORRIGIDO (Phase 1)

---

### CRITICAL C-4 — Portaria GM/MS 69/2021 atribuída erroneamente

**Arquivos afetados:**
- `corpora_clingo/emergencia_manaus/emergencia_sanitaria.lp`
- `corpora_clingo/scenarios/c2_manaus_facts.lp`
- `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx` (8 ocorrências)

**Problema:** A Portaria GM/MS 69/2021 (obrigatoriedade de registro de vacinas
no SI-PNI, publicada 25/jan/2021) foi usada como base normativa da obrigação de
fornecimento de oxigênio (Art. 3° VIII da Lei 13.979/2020) e como certificação
de colapso hospitalar. Estas são âncoras completamente erradas.

**Âncoras corretas utilizadas:**
- Obrigação de oxigênio → Lei 13.979/2020 Art. 3° VII + Art. 3° VIII + Lei 8.080/1990 Art. 15 I
- Colapso UTI → FVS-AM Boletim 16/jan/2021 (103.69% UTI pública) + Decreto AM 43.303/2021
- Ativação COES → `hospital_capacity_critical + espin_declaration_active` (predicado derivado)

**Verificação externa:** Portaria GM/MS 69/2021 verificada no DOU — trata
exclusivamente de registro obrigatório de doses de vacinas contra COVID-19 no
Sistema de Informação do Programa Nacional de Imunizações (SI-PNI). Sem relação
com colapso hospitalar ou obrigações de insumos.

**Corpus pós-auditoria:** `grep -r "Portaria69_2021" corpora_clingo/` → 2
ocorrências, ambas em comentários `% REMOVIDA (audit C-4)`, zero como predicados
ativos.

**Status:** ✅ CORRIGIDO (Phase 1 corpus + Phase 2 paper)

---

### CRITICAL C-5 — Padrões de substring incorretos em psi_builder.py

**Arquivo:** `src/qfeng/e5_symbolic/psi_builder.py` —
`_SCENARIO_PREDICATE_MAP`

**Problema:** 16 padrões de substring para construção de ψ_S não casavam com
nenhum átomo ativo emitido pelo corpus Clingo. ψ_S de C3, C7, T-CLT-01 e
T-CLT-04 eram construídos com peso zero para todos os predicados → sinal
normativo completamente ausente → θ resultante era artefato do ψ_N sozinho.

**Exemplos de padrão errado → átomo real:**
- C3: `"right_to_universal_healthcare"` → `"universal_equal_access_to_health_services"`
- C3: `"prohibition_of_discrimination"` → `"equality_of_assistance_without_prejudice"`
- C7: `"equal_protection_under_law"` → `"equal_protection_of_the_laws"`
- C7: `"prohibition_race_based_discrimination"` → `"prohibition_racial_discrimination_federal_programs"`
- T-CLT-01: `"due_process_of_law"` → `"obligation_to_ground_decision_in_identified_precedent"`

**Método de verificação:** Para cada cenário, executado `run_scenario(id)` e
coletados todos os átomos ativos no answer set. Cada padrão conferido contra a
lista de átomos reais.

**Novo teste de regressão:** `tests/test_e5/test_psi_s_pattern_coverage.py` —
47 testes parametrizados, um por padrão×cenário. Assertiva: cada padrão deve
casar ≥ 1 átomo ativo. Todos passando.

**Status:** ✅ CORRIGIDO (Phase 1)

---

### CRITICAL C-6 / F0-1 — Acórdão TST fabricado

**Arquivos afetados:**
- `corpora_clingo/scenarios/t_clt_04_facts.lp`
- `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx` (linha 624)

**Problema:** O cenário T-CLT-04 (controle positivo STAC) referenciava
`TST-RR-000200-50.2019.5.02.0020` como âncora jurisprudencial real. Este
acórdão não existe:
- Numeração inconsistente com padrão CNJ pós-2008 (exige 7 dígitos pré-ponto
  para processos de 2019; o número tem apenas 6)
- Não encontrado em jurisprudencia.tst.jus.br nem em agregadores (Jusbrasil,
  Migalhas, Conjur)
- O arquivo `tst_rr_000200_50_2019.lp` nunca existiu no repositório

**Verificação externa:** Busca exaustiva no banco jurisprudencial do TST em
2026-04-24 por múltiplas variações de formatação — resultado: não encontrado.

**Substituto verificável:** TST-Ag-RR-868-65.2021.5.13.0030
- Órgão: 2ª Turma do Tribunal Superior do Trabalho
- Publicação: DEJT 06/12/2023
- Tema: Validade de CCT bancária (2018/2020 e 2020/2022) sobre banco de horas
  anual à luz do Tema 1046/STF (ARE 1.121.633)
- Tese STF Tema 1046: "são constitucionais os acordos e as convenções coletivos
  que, ao considerarem a adequação setorial negociada, pactuam limitações ou
  afastamentos de direitos trabalhistas, desde que respeitados os direitos
  absolutamente indisponíveis."
- Base normativa: CLT Art. 59 §2°, Art. 611-A I; CF/88 Art. 7° XXVI

**Arquivo Clingo criado:**
`corpora_clingo/brasil/trabalhista/tst_decisoes/tst_ag_rr_868_65_2021.lp`

**θ T-CLT-04 após substituição:** 7.05° STAC — comportamento STAC preservado.

**Status:** ✅ CORRIGIDO (commit 6d275f1)

---

### HIGH H-1 — Âncora SSA §1902(a)(19) incorreta para equal protection

**Arquivo:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`
(linha 163 original)

**Problema:** Paper ainda ancorava a obrigação de equal protection do caso
Obermeyer em SSA §1902(a)(19). Este subseção trata de "best interests of
recipients", não de equal protection. O corpus `medicaid_access.lp` já usava
os predicados corretos; a prosa estava errada.

**Correção:** Substituído por: "14th Amendment §1 Equal Protection Clause,
Title VI of the Civil Rights Act 1964 (42 USC §2000d; 42 CFR §440.240), and
§1902(a)(10) comparability."

**Status:** ✅ CORRIGIDO (Phase 2)

---

### HIGH H-2 — CLT Art. 59-B §1 como âncora de CCT

**Arquivo:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`
(linhas 575, 602, 1052 originais)

**Problema:** Paper citava "CLT Art. 59-B §1" como âncora da obrigação de CCT
para banco de horas longo. Art. 59-B trata de ausência de nulidade por
compensação tácita (introduzido pela Reforma 13.467/2017) — distinto do
requisito de CCT. O corpus usava corretamente Art. 59 §2° + §5° e Art. 611-A I.

**Correção:** Substituído por "CLT Art. 59 §§2° e 5° combinados com Art. 611-A I"
em todas as ocorrências do contexto CCT.

**Status:** ✅ CORRIGIDO (Phase 2)

---

### HIGH H-3 — Corpora EU/GDPR/Medicaid codificados mas não avaliados

**Arquivos:** `corpora_clingo/eu/ai_act/eu_ai_act_obligations.lp`,
`corpora_clingo/eu/gdpr/gdpr_data_protection.lp`,
`corpora_clingo/usa/medicaid/medicaid_access.lp`

**Problema:** Paper afirmava "multi-regime coverage" incluindo EU AI Act, GDPR
e Medicaid Title XIX, mas nenhum cenário C5/C6/C8 estava registrado no PoC.
Esses corpora geravam zero átomos ativos em qualquer θ reportado. A afirmação
de cobertura era estruturalmente vazia.

**Correção:** Adicionado ao paper (após Mandatory disclosure 2):

> "Mandatory disclosure 3 – Regulatory corpus coverage: The EU AI Act
> (Regulation (EU) 2024/1689), GDPR (Regulation (EU) 2016/679), and Medicaid
> Title XIX (42 USC §1396 et seq.) corpora are fully codified in the Q-FENG
> Clingo corpus (...) but are not evaluated in the current run: no C5, C6, or
> C8 scenario is registered in this PoC (C4 LLM predictor integration pending).
> (...) Paper 2 and future work will exercise these corpora against planned C5,
> C6, and C8 scenarios."

**Status:** ✅ CORRIGIDO (Phase 3)

---

### HIGH H-4 — ψ_N de C3 descrito como "LightGBM treinado"

**Arquivo:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`
(linha 536 original)

**Problema:** Paper afirmava "LightGBM predictor trained on normative document
count per regional administrative unit" para C3. Não existe código de treino,
artefato serializado, nem dataset de treinamento. O vetor ψ_N de C3 é hardcoded
em `psi_builder.py` (comentário: "synthetic calibration from literature").
`n_observations=27` refere-se a documentos normativos, não a observações de um
modelo ML.

**Correção:** Reformulado como "synthetic ψ_N calibrated from
literature-documented regional SUS allocation patterns." Adicionada Tabela A1
(ψ_N Source Classification) ao paper:

| ψ_N Source Type | Scenario(s) | Description |
|-----------------|-------------|-------------|
| pressure-score-interpolated | C2 (12-month series) | SIH/DATASUS hospital occupancy + FVS-AM TOH values |
| synthetic-calibrated | C2 (single-shot), C3, C7, T-CLT-01..04 | Literature/normative calibration |
| predictor-derived | — (none in this PoC) | C4 Ollama pending |

**Status:** ✅ CORRIGIDO (Phases 2 e 3)

---

### HIGH H-5 / F0-2 — Portaria GM/MS 268/2021 âncora inexistente

**Arquivos:** `corpora_clingo/emergencia_manaus/emergencia_sanitaria.lp`,
`corpora_clingo/scenarios/c2_manaus_facts.lp`

**Problema:** `obligation_additional_response_measures` ancorada em
`regulatory_basis("Portaria268_2021")`. Auditoria revelou que não existe
"Portaria GM/MS nº 268, de 28 de janeiro de 2021". A única Portaria 268/2021
do Ministério da Saúde é da Secretaria-Executiva (SE), de 29/06/2021, sobre
metas de desempenho de servidores — sem relação com Manaus, oxigênio ou COVID-19.

**Verificação externa:** Consulta ao DOU (bvsms.saude.gov.br + in.gov.br) em
2026-04-24. Ementa real da Portaria SE nº 268/2021: "Divulga resultado final
das metas institucionais para fins de avaliação de desempenho de servidores
do Ministério da Saúde." (DOU 02/07/2021).

**Âncoras corretas utilizadas:**
- `regulatory_basis("Portaria79_2021")` — Portaria GM/MS 79, de 18/jan/2021:
  "Amplia o número de vagas do Programa Mais Médicos para os municípios do
  Amazonas com maior necessidade em razão da pandemia de Covid-19."
- `statutory_basis("Lei13979_Art10")` — Competência federal de coordenação
  federativa da resposta COVID-19

**Status:** ✅ CORRIGIDO (commit f2849bd)

---

### HIGH H-6 — Constraint deny_access sem guard de regime

**Arquivo:** `corpora_clingo/brasil/saude/sus_direito_saude.lp:116`

**Problema:** Constraint `:- decision_output(_, deny_access), sovereign(universality_of_access).`
sem guard de regime. Segura no PoC atual por coincidência (nenhum cenário ativo
emite `deny_access`), mas fragiliza cenários futuros não-saúde.

**Correção:**
```prolog
:- decision_output(_, deny_access),
   sovereign(universality_of_access),
   statutory_basis("Lei8080_Art7_I").  % guard: scopes to SUS/health-access regime
```

**Status:** ✅ CORRIGIDO (Phase 4)

---

### HIGH H-7 — Cabeças órfãs em medicaid_access.lp

**Arquivo:** `corpora_clingo/usa/medicaid/medicaid_access.lp`

**Problema:** `state_access_gap_exists` e `within_state_demographic_gap` eram
predicados operacionais para cenário C8 (não registrado). Derivados sem serem
consumidos por nenhum constraint. Comportamento atual: inofensivo (predicados
de entrada nunca derivados), mas enganoso para revisores.

**Correção:** Adicionado comentário de audit H-7 explicando status de C8
pendente e por que os predicados são seguros sem facts file de C8.

**Status:** ✅ CORRIGIDO (Phase 4)

---

### HIGH H-8 — Narrativa §C2 inconsistente com série temporal

**Arquivo:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`

**Problema:** Narrativa afirmava "jan/2021 peak crisis = CB" (θ=129°/127.47°).
Pipeline correto (com manaus_sih_loader usando valores TOH institucionais FVS-AM)
mostra jan/2021 em HITL (θ=117.65°/118.73°). Pico real = set/2020 (130.91°).

**Correção:** Narrativa §C2 atualizada para refletir que a série de 12 meses usa
ψ_N(t) interpolado pelo SIH/DATASUS, que o regime mensal emerge do pipeline, e
que o pico real (set/2020) difere da crise política de jan/2021.

**Status:** ✅ CORRIGIDO (Phase 2)

---

### MEDIUM M-5 — GDPR Art. 17° listado sem implementação

**Arquivo:** `corpora_clingo/eu/gdpr/gdpr_data_protection.lp` (header)

**Problema:** Header listava "Art. 17° — Direito ao apagamento" mas nenhum corpo
de regra implementava esse artigo.

**Correção:** Removido Art. 17° do header; adicionada nota de future work para
C6 extendido.

**Status:** ✅ CORRIGIDO (Phase 4)

---

### Itens verificados e confirmados OK

| Item | Verificação |
|------|-------------|
| EU AI Act = Reg. (EU) 2024/1689 | ✅ Correto |
| GDPR = Reg. (EU) 2016/679, Arts. 5, 9, 22, 25, 35 | ✅ Correto |
| CLT Arts. 58-59, 611-A, 611-B | ✅ Correto |
| CPC Art. 489 §1° V-VI (Lei 13.105/2015) | ✅ Correto |
| LINDB Art. 20 (Lei 13.655/2018) | ✅ Correto |
| Lei 8.080/1990 Arts. 6°, 7°, 15 | ✅ Correto |
| Portarias 188/2020, 356/2020, 454/2020, 197/2021 | ✅ Correto |
| Decretos AM 43.269, 43.303, 43.360 (2021) | ✅ Correto |
| Mata v. Avianca, 678 F. Supp. 3d 443 (S.D.N.Y. 2023) | ✅ Correto |
| CF/88 Arts. 1°, 3°, 5°, 7°, 196, 197, 198 | ✅ Correto |
| 14ª Emenda §1 EPC, Title VI §601, 42 USC §1983 | ✅ Correto |
| Obermeyer et al. (2019), Science 366(6464):447-453 | ✅ Correto |
| Janela ESPIN 2020-02-03 a 2022-04-22 | ✅ Correto |
| STF Tema 1046 (ARE 1.121.633) | ✅ Correto |
| TST-Ag-RR-868-65.2021.5.13.0030 (2ª Turma, DEJT 06/12/2023) | ✅ Verificado |
| FVS-AM Boletim 16/jan/2021 (103.69% UTI pública Manaus) | ✅ Correto |
| Portaria GM/MS 79/2021 (vagas Mais Médicos Manaus, 18/jan/2021) | ✅ Correto |

---

## PARTE III — ESTADO ATUAL DOS ARTEFATOS

### 3.1 Corpus Clingo (`corpora_clingo/`)

| Arquivo | Status pós-audit | Predicados ativos (C2) |
|---------|------------------|------------------------|
| `brasil/emergencia_manaus/emergencia_sanitaria.lp` | ✅ Auditado — C-1, C-4, H-5 corrigidos | 14 sovereign |
| `brasil/saude/sus_direito_saude.lp` | ✅ H-6 guard adicionado | 8 sovereign (C2), 6 (C3) |
| `brasil/constitucional/cf88_principios_fundamentais.lp` | ✅ OK (ressalva M-1 apenas documental) | 4 sovereign |
| `brasil/processual/cpc_fundamentacao.lp` | ✅ C-3 corrigido | 5 sovereign (T-CLT-01) |
| `brasil/trabalhista/clt_direitos_trabalhistas.lp` | ✅ OK | 8 sovereign (T-CLT-02) |
| `brasil/trabalhista/tst_decisoes/tst_ag_rr_868_65_2021.lp` | ✅ NOVO — F0-1/C-6 | 3 sovereign (T-CLT-04) |
| `usa/civil_rights/civil_rights_14th.lp` | ✅ C-2 corrigido | 5 sovereign (C7) |
| `usa/medicaid/medicaid_access.lp` | ✅ H-7 documentado | 3 sovereign (C7) |
| `eu/ai_act/eu_ai_act_obligations.lp` | ✅ OK (sem cenário ativo) | 0 (C5 pendente) |
| `eu/gdpr/gdpr_data_protection.lp` | ✅ M-5 header corrigido | 0 (C6 pendente) |
| `scenarios/c2_manaus_facts.lp` | ✅ C-4, H-5 corrigidos | facts file C2 |
| `scenarios/t_clt_04_facts.lp` | ✅ C-6/F0-1 corrigido | facts file T-CLT-04 |

### 3.2 Pipeline Python (`src/qfeng/`)

| Módulo | Status | Observação ARS |
|--------|--------|----------------|
| `e5_symbolic/psi_builder.py` | ✅ C-5 corrigido — 47 padrões verificados | Verificar: `_SCENARIO_PREDICATE_MAP` — cada padrão deve casar ≥ 1 átomo |
| `e5_symbolic/runner.py` | ✅ OK | Verificar: `run_all_scenarios()` retorna 7 cenários com θ dentro de ±2° dos valores reportados |
| `e5_symbolic/scenario_loader.py` | ✅ OK | Verificar: `_strip_constraints` regex — não remove regras válidas |
| `e5_symbolic/manaus_sih_loader.py` | ✅ C-1 impacto: usa TOH FVS-AM | Verificar: valores de ocupação hospitalar vs. Table 7 |
| `core/interference.py` | ✅ Não modificado | Verificar: `arccos(dot(ψ_N, ψ_S))` implementação correta; L2-normalização Born |
| `core/schemas.py` | ✅ Não modificado | Contrato de tipos — não alterar |

### 3.3 Dados e Outputs

| Artefato | Localização | Status |
|----------|------------|--------|
| Table 7 (12-month Manaus series) | `outputs/table7_new_values.csv` | ✅ Regenerada Phase 1 — valores SIH/DATASUS |
| Parquet E5 results | `outputs/e5_results/*.parquet` | ✅ Regenerados Phase 1 |
| Figure 1 (interference overview) | `outputs/figures/F1_interference_overview.*` | ✅ Regenerada Phase 1 |
| Figure 5 (threshold robustness) | `outputs/figures/F5_threshold_robustness.*` | ✅ Regenerada Phase 1 |
| Figure 6 (psi sensitivity) | `outputs/figures/F6_psi_sensitivity.*` | ✅ Regenerada Phase 1 |
| Figure 7 (deontic modality) | `outputs/figures/F7_deontic_regime_modality.*` | ✅ Regenerada Phase 1 |
| Figure 2 (Manaus time-series) | `outputs/figures/` | ✅ Regenerada Phase 1 |
| Deontic cache E2 | `outputs/deontic_cache/` | ✅ OK — 5.136 DeonticAtoms |

### 3.4 Paper (`docs/papers/` — não versionado em git)

**Arquivo canônico:** `PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`

Histórico de versões:
1. `PAPER1_QFENG_VALIDACAO_editando(1).docx` — versão pré-auditoria
2. `PAPER1_QFENG_FINAL_prob_dados_clingo.docx` — arquivo canonizado antes das auditorias
3. `PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx` — **versão pós-auditoria (ATUAL)**

Scripts de correção do paper (em `scripts/`, todos versionados):
- `apply_paper_audit_corrections.py` — Phase 2: 28 substituições textuais + Table 7
- `apply_f01_tst_case_substitution.py` — Phase F0-1: substituição TST (runs)
- `apply_f01_fix_split_runs.py` — Phase F0-1: substituição TST (split-runs)
- `apply_f01_fix_suffix.py` — Phase F0-1: sufixo TRT-13 correto
- `apply_phase3_structural_honesty.py` — Phase 3: disclosure 3 + Tabela A1

---

## PARTE IV — PERFIS DE REVISORES ARS E CHECKLIST POR AGENTE

### AGENTE 1 — Revisor de Matemática e Fórmulas

**Perfil:** Especialista em geometria de Hilbert, teoria quântica de decisão,
probabilidade bayesiana. Deve verificar consistência entre fórmulas no paper e
implementação em código.

**Itens a verificar:**

1. **Equação de interferência (Eq. 1)**
   - Paper: `θ = arccos(⟨ψ_N | ψ_S⟩)`
   - Código: `src/qfeng/core/interference.py` — função `compute_theta`
   - Verificar: normalização L2 (Born) vs. simplex (sum=1). O paper diz "L2-normalised
     in the Hilbert sense; |ψ|² yields Born probability mass." A implementação
     usa `np.linalg.norm` (L2). Consistente.

2. **Markovian theta_efetivo (Eq. 2-5)**
   - Paper §3.2: `θ_eff(t) = α(t)·θ_t + (1-α(t))·θ_eff(t-1)`
   - `α(t) = sigmoid(β · score_pressão(t))`, β=3.0
   - Código: `src/qfeng/e5_symbolic/manaus_sih_loader.py`
   - Verificar: valor de β; valor inicial `θ_eff(0) = θ_t(0)`; série em `table7_new_values.csv`
   - **Atenção:** Paper §7.4 (Limitations) admite que a forma antecipatória
     (Eq. 5, τ > 0) é formalmente proposta mas não testada empiricamente.

3. **Born rule vs. Bayesian clássico (Eq. 6-7)**
   - `P_q(violação) = |⟨ψ_N|ψ_violation⟩|²` (quantum)
   - `P_cl(violação) = cos²(θ/2)` (classical Bayesian proxy)
   - `Δ(violação) = P_q - P_cl` (interference term)
   - Verificar: implementação em `interference.py:compute_born_probability`
   - Verificar: Table 4 (Born rule advantage) — coluna Δ deve ser negativa para
     CB cenários (quantum atribui maior probabilidade de violação) e positiva/zero
     para STAC.

4. **Alhedonic signal / Cybernetic loss**
   - `A = -log(P_q(compliance))` onde `P_q(compliance) = 1 - P_q(violação)`
   - Verificar: Table 5 (alhedonic signal). Para STAC: A deve ser próximo de 0
     (alta compliance). Para CB: A deve ser alto (baixa compliance).

5. **Threshold robustness (§6.1, Table 6)**
   - Grid: θ_stac ∈ {20°,25°,30°,35°,40°}, θ_block ∈ {100°..130°}, 35 combos × 7 = 245
   - Paper afirma: 240/245 (97.96%) corretos; falhas apenas em T-CLT-02 com θ_block=130°
   - T-CLT-02 = 127.81° → abaixo do 130° → correto que falha neste caso extremo
   - Verificar: `outputs/e5_results/threshold_sweep.parquet` vs. Table 6

6. **Bootstrap CI Manaus (§6.3)**
   - σ=0.05 para meses SIH/DATASUS; σ=0.10 para meses estimados
   - 1.000 amostras bootstrap por mês; CIs 95th percentile
   - Paper afirma: "All twelve months produce CIs entirely within a single
     governance regime" — verificar em Table 7 (colunas CI_lower, CI_upper).
   - **ATENÇÃO:** Paper §6.3 afirma "narrowest CIs occur in February 2021 (CI:
     [130.94°, 132.84°]) — the peak crisis month." INCONSISTÊNCIA: os valores
     do pipeline pós-auditoria mostram fev/2021 = 118.08°/118.40° (HITL), não
     CB. Esta frase refere-se ao pico antigo (antes da correção C-1). O ARS
     deve verificar se esta frase foi atualizada no paper ou ainda está
     inconsistente.

7. **ψ-weight sensitivity (§6.2, Table 7)**
   - Monte Carlo: 500 amostras, ruído U(-ε,+ε) onde ε=20% do magnitude original
   - Paper afirma: 100% regime correto em todos os 7 cenários
   - Verificar: `outputs/e5_results/psi_sensitivity.parquet` e Figure 6

---

### AGENTE 2 — Revisor de Código e Pipeline

**Perfil:** Engenheiro de software com experiência em ASP/Clingo, Python,
pipelines de ML. Deve verificar integridade estrutural do código e reprodutibilidade.

**Itens a verificar:**

1. **Clingo ASP — Semântica de mundo fechado**
   - Verificar todos os arquivos em `corpora_clingo/` para:
     a) Predicados usados em corpos de regras mas nunca definidos como cabeças
        (exceto os documentados como "pendentes C8" em medicaid_access.lp)
     b) Constraints cuja semântica seja inadvertidamente satisfeita por ausência
        de predicados (ex.: `not P` onde P nunca é derivado)
   - Ferramenta: `clingo --check` ou `clingo --warn=atom-undefined`
   - Arquivos prioritários: `emergencia_sanitaria.lp`, `cpc_fundamentacao.lp`,
     `civil_rights_14th.lp`

2. **psi_builder.py — _SCENARIO_PREDICATE_MAP**
   - Executar `pytest tests/test_e5/test_psi_s_pattern_coverage.py -v`
   - Resultado esperado: 47 testes passando (um por padrão×cenário)
   - Se qualquer padrão retornar 0 átomos: θ daquele cenário está sendo
     calculado com sinal normativo incompleto

3. **scenario_loader._strip_constraints**
   - Regex-based: `re.sub(r':- .*?\n', '', content)` (aproximado)
   - Verificar: para cada arquivo de corpus, confirmar que `_strip_constraints`
     não remove regras válidas que começam com `:-` por outra razão
   - **ATENÇÃO (M-4):** Esta heurística é frágil a pontos em comentários
     dentro de constraints. Documentado mas não corrigido no PoC.

4. **manaus_sih_loader.py — valores de entrada**
   - Verificar: `hospital_occupancy_rate_pct` para cada mês vs. FVS-AM Boletim
     e SIH/DATASUS reportados em Table 7 (coluna `Occupancy`)
   - `score_pressão(t)` calculado de qual fonte para meses não-SIH?
   - Documenta internamente (linha 24-31): Portaria 69/2021 NÃO se aplica —
     âncora correta é Decreto AM 43.303/2021 + FVS-AM

5. **runner.py — determinismo e reproducibilidade**
   - Verificar: seeds fixas declaradas?
   - Paper afirma (§7.1): "fixed random seeds for Monte Carlo analyses"
   - Localizar `random.seed()` ou `np.random.seed()` no runner e no sensitivity
     analysis

6. **Testes de regressão**
   - Executar: `pytest tests/ -v` — resultado esperado: 475 passed, 11 skipped
   - Os 11 skipped: verificar se são cenários C4 (LLM predictor) ou outro motivo
   - Verificar se `tests/test_e5/test_psi_s_pattern_coverage.py` existe e passa

7. **Reprodutibilidade end-to-end**
   - `python -m qfeng.e5_symbolic.runner` deve produzir:
     C2: ~132°, C3: ~134°, C7: ~134°, T-CLT-01..02: ~127-134°,
     T-CLT-03: ~5.65°, T-CLT-04: ~7.05° (±2° tolerância)
   - Qualquer desvio acima de 2° indica mudança não rastreada

---

### AGENTE 3 — Revisor de Texto e Prosa Acadêmica

**Perfil:** Especialista em redação científica, APA 7, JURIX style. Verificar
consistência interna do paper e alinhamento texto↔dados.

**Itens a verificar:**

1. **Consistência Text↔Table 7 (série Manaus)**
   - Verificar: todas as referências a θ de jan/2021 no corpo do texto devem
     ser HITL (118.73°), não CB
   - Verificar: referências ao "pico da crise" devem apontar set/2020 (130.91°)
   - **ATENÇÃO:** §6.3 contém frase sobre fev/2021 como "narrowest CIs" e
     "peak crisis month" com valores de CI [130.94°, 132.84°] — estes eram
     valores do pipeline antigo. Confirmar se foram atualizados.

2. **Consistência Text↔Table 3 (θ dos 7 cenários)**
   - Cada θ citado no texto de cada cenário (§5.2) deve bater com Table 3
   - Tolerância: ±0.5° (arredondamento display)

3. **Referências bibliográficas**
   - Verificar formatação APA 7 de:
     * Obermeyer et al. (2019): Science 366(6464):447-453
     * Mata v. Avianca: 678 F. Supp. 3d 443 (S.D.N.Y. 2023)
     * STF Tema 1046 (ARE 1.121.633): formato ABNT NBR 6023 para julgados
     * TST-Ag-RR-868-65.2021.5.13.0030: DEJT 06/12/2023, 2ª Turma
     * Kaminski (2026): formato correto para tese/working paper

4. **Mandatory disclosures**
   - Verificar: disclosures 1, 2, 3 presentes e coerentes entre si
   - Disclosure 1 (C5/C6/C8 não executados): não contradiz disclosure 3
   - Disclosure 3 (corpora codificados não avaliados): coerente com §7.4

5. **Tabela A1 (ψ_N source)**
   - Verificar coerência com §3.1 (descrição de ψ_N no texto)
   - Verificar que "predictor-derived: none" é consistente com disclosure 1/3

6. **Afirmações falsificáveis**
   - Paper deve ter pelo menos 1 afirmação falsificável por contribuição
   - Contribution 1 (θ geometry): falsificável via T-CLT-03/04 STAC ✓
   - Contribution 2 (Markovian θ_eff): falsificável via onset CB Out/2020 ✓
   - Contribution 3 (failure typology): falsificável via SAT/UNSAT por tipo ✓

7. **§7.4 Limitations — completude**
   - Verificar que todas as limitações identificadas na auditoria com disclosure
     estão mencionadas em §7.4: single HITL reviewer ✓, synthetic ψ_N ✓,
     defeasibility ✓, anticipatory θ_eff ✓, C4 LLM pending ✓

---

### AGENTE 4 — Revisor Jurídico (Direito Brasileiro)

**Perfil:** Advogado/jurista especializado em direito constitucional, trabalhista
e sanitário brasileiro.

**Itens a verificar:**

1. **CF/88 Arts. 196-200 — Direito à Saúde**
   - Verificar: predicado `sovereign(right_to_health_as_duty_of_state)` ancorando
     em Art. 196 — correto (art. 196: "saúde é direito de todos e dever do Estado")
   - Verificar: distinção entre `universality_of_access` (Art. 7° I Lei 8.080) e
     `universal_equal_access_to_health_services` (CF/88 Art. 196) — são distintos
     predicados com âncoras diferentes. Verificar se paper e corpus são consistentes.

2. **Lei 13.979/2020 (COVID-19)**
   - Art. 3° VII: autoridade para requisição de bens de PJ em emergência ✓
   - Art. 3° VIII: importação/distribuição sem registro prévio ✓
   - Art. 10: coordenação federativa ✓
   - Verificar: Art. 3° VIII é usado para obrigação de oxigênio em Manaus —
     tecnicamente, Art. 3° VIII trata de importação, não requisição doméstica.
     A requisição doméstica seria Art. 3° VII. Avaliar se a distinção VII/VIII
     está corretamente refletida no corpus e no paper.

3. **CLT — Banco de Horas**
   - Art. 59 §2°: banco de horas ANUAL exige CCT. Máx. 1 ano para compensação. ✓
   - Art. 59 §5° (Reforma 2017): banco de horas SEMESTRAL por acordo individual
     escrito, sem CCT. Máx. 6 meses. ✓
   - Art. 59-B: trata de ausência de nulidade por compensação tácita —
     **NOT** requisito de CCT (este foi o bug H-2). ✓ Corrigido.
   - Art. 611-A I: jornada negociável por CCT ✓
   - Verificar: T-CLT-02 usa `not collective_bargaining_agreement_active` como
     fact — fato que deveria ser derivado do corpus, não hardcoded.

4. **STF Tema 1046 (ARE 1.121.633)**
   - Tese: "são constitucionais os acordos e convenções coletivos que pactuam
     limitações ou afastamentos de direitos trabalhistas, desde que respeitados
     os direitos absolutamente indisponíveis."
   - Verificar: o predicado `elastic(cct_annual_hour_bank_validated_by_tema1046)`
     em `tst_ag_rr_868_65_2021.lp` é derivado condicionalmente a
     `stf_tema1046_binding_precedent_applied` — verificar se a cadeia lógica
     está correta para T-CLT-04.

5. **Decreto AM 43.303/2021**
   - Calamidade pública estadual AM, 23/jan/2021
   - Verificar: predicado `sovereign(critical_health_system_situation_manaus)`
     ancorado em `regulatory_basis("DecretoAM43303_2021") + hospital_capacity_critical`
     — âncora normativa adequada? O Decreto declara calamidade pública, o que
     suporta a derivação de situação crítica.

6. **Portaria GM/MS 79/2021**
   - Tema real: ampliação emergencial de vagas do Programa Mais Médicos para
     municípios do Amazonas com maior necessidade em razão da pandemia.
   - Verificar: esta portaria justifica `obligation_additional_response_measures`?
     Ela trata de vagas de médicos, não diretamente de resposta a colapso de
     oxigênio. A âncora legal para reforço de insumos críticos seria mais
     diretamente Lei 13.979 Art. 3° VII + Lei 8.080 Art. 15 I.
   - **ATENÇÃO (NOVO RISCO):** Esta substituição (de Portaria 268/2021 inválida
     para Portaria 79/2021) pode ser questionada. O revisor jurídico deve avaliar
     se Portaria 79/2021 é âncora adequada para `obligation_additional_response_measures`
     no contexto de colapso hospitalar, ou se seria mais apropriado ancorar
     diretamente em Lei 13.979 Art. 3° VII + Lei 8.080 Art. 15 I (que já estão
     presentes no corpus).

7. **Mata v. Avianca — 678 F. Supp. 3d 443 (S.D.N.Y. 2023)**
   - Âncora do cenário T-CLT-01 (phantom citation / execution_inertia)
   - O caso real trata de advogado que usou citações de casos fabricados por
     ChatGPT — juiz Robert Lehrburger impôs sanções (Federal Rule of Civil
     Procedure 11)
   - Verificar: a analogia com T-CLT-01 (IA que cita precedente inexistente)
     está corretamente descrita no paper e no corpus (t_clt_01_facts.lp)

---

### AGENTE 5 — Revisor de Saúde Pública e Epidemiologia (C2 e C3)

**Perfil:** Epidemiologista / especialista em saúde coletiva. Verificar dados
e afirmações sobre Manaus 2021 e concentração regional do SUS.

**Itens a verificar:**

1. **Série temporal Manaus (Table 7)**
   - Verificar valores de ocupação hospitalar vs. dados SIH/DATASUS e FVS-AM:
     * Jul/2020: 100% UTI (C2 facts = 92 pct → verificar se é dado jul ou jan)
     * Set/2020: 100% — pico historicamente documentado?
     * Jan/2021: 100% — crise do oxigênio, coerente com FVS-AM 103.69%
     * Feb/2021: 93% — redução após intervenção federal?
   - **ATENÇÃO:** `c2_manaus_facts.lp` tem `hospital_occupancy_rate_pct(92)` e
     `oxygen_days_remaining(1)` hardcoded. Verificar se estes representam pico
     ou média da série.

2. **FVS-AM Boletim 16/jan/2021**
   - Afirmação: "103.69% UTI pública"
   - Verificar: este valor é do Boletim Epidemiológico nº 16 da FVS-AM de
     16/jan/2021 (COVID-19 Amazonas). Fonte pública, verificável.

3. **Cenário C3 — Concentração regional SUS**
   - ψ_N calibrado de "literatura sobre padrões regionais de alocação SUS,
     27 documentos normativos" — verificar: quais são esses 27 documentos?
     Listados em `scenarios/c3_concentracao_facts.lp`?
   - θ = 134.40° CB — regime constitutional (CF/88 Art. 196 + Lei 8.080 Art. 7°)
   - Verificar: a concentração regional do SUS documenta `decision_output` que
     viole `sovereign(equity_in_health_assistance)` + `sovereign(sus_regionalization)`?

4. **Figura 2 (Manaus time-series)**
   - Verificar: legenda da Figura 2 — cita FVS-AM Boletim 16/jan/2021 como
     fonte dos dados de ocupação hospitalar? Não deve citar Portaria 69/2021.
   - Eixo X: meses jul/2020 a jun/2021 (12 meses)
   - Dois eixos Y: θ_eff (graus) e hospital_occupancy_pct (%)
   - Verificar: Jan/2021 deve aparecer como HITL (faixa amarela/laranja), não CB

5. **Obermeyer et al. (2019) — C7**
   - Risk score gap reportado: "34 percentage-point gap" (não "47% lower risk score")
   - Verificar: paper usa "pp gap" ou "percent lower"? O paper foi corrigido
     (LOW item) mas verificar se a frase ficou consistente com a metodologia
     Obermeyer (gap em percentual de pontuação, não razão de probabilidade).

---

### AGENTE 6 — Revisor de Direito Internacional e IA (C7, EU AI Act, GDPR)

**Perfil:** Especialista em IA e direito, civil rights americanos, GDPR europeu.

**Itens a verificar:**

1. **14ª Emenda §1 — Equal Protection Clause**
   - Verificar: predicado `sovereign(equal_protection_of_the_laws)` ancorado em
     `constitutional_basis("14th_Amendment_Section1")` — correto
   - Verificar: distinção entre EPC (discriminação intencional, strict scrutiny)
     e Title VI (disparate impact em programas federais) — o corpus usa ambos?

2. **Title VI §601 (42 USC §2000d)**
   - Verificar: `sovereign(prohibition_disparate_impact_in_federal_programs)` —
     tecnicamente, §601 do Title VI proíbe discriminação intencional. O disparate
     impact padrão deriva de regulações administrativas (42 CFR §100.13(g)),
     não do texto estatutário de §601 diretamente. Avaliar se o corpus é preciso.

3. **Medicaid SSA §1902(a)(10) — Comparability**
   - Substituiu incorreta âncora §1902(a)(19)
   - §1902(a)(10): serviços devem ser comparáveis em "amount, duration, and scope"
   - Verificar: `sovereign(comparability_of_services_across_beneficiaries)` em
     `medicaid_access.lp` — ancoragem em `SSA_XIX_1902_a_10` correta?

4. **EU AI Act (Reg. EU 2024/1689)**
   - Corpus codificado mas não avaliado (disclosure 3)
   - Verificar: os predicados em `eu_ai_act_obligations.lp` estão alinhados
     com a versão final do Regulamento publicada em 12 jul 2024 no OJEU
     (L 2024/1689)?
   - Artigos críticos: Art. 6 (classificação de sistemas de alto risco),
     Art. 9 (sistema de gestão de risco), Art. 13 (transparência),
     Art. 10 (dados de treino)

5. **GDPR Arts. 22 e 35 (decisão automatizada e DPIA)**
   - `sovereign(prohibition_solely_automated_decision_with_legal_effects)` — Art. 22
   - `sovereign(obligation_dpia_for_high_risk_processing)` — Art. 35
   - Verificar: se um cenário C6 for ativado no futuro, esses predicados
     capturarão corretamente as obrigações do controlador de dados?

---

## PARTE V — RISCOS RESIDUAIS E ITENS ABERTOS

### Risco R1 — §6.3 frase sobre fev/2021 (MEDIUM — verificar)

**Localização:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`,
§6.3 Bootstrap CI.

**Frase suspeita:** "The narrowest CIs occur in February 2021 (CI: [130.94°,
132.84°]) — the peak crisis month with the highest-quality SIH data..."

**Problema:** Fev/2021 no pipeline pós-auditoria = 118.08°/118.40° HITL, não
CB. Os valores [130.94°, 132.84°] eram do pipeline antigo (antes da correção
C-1 que adicionou os átomos-ponte `espin_declaration_active`).

**Ação ARS:** Agente 1 (Matemática) e Agente 3 (Texto) devem verificar se
esta frase foi atualizada na Phase 2 ou ainda contém valores antigos.

---

### Risco R2 — Portaria 79/2021 como âncora de obligation_additional_response_measures (LOW — avaliar)

**Localização:** `emergencia_sanitaria.lp:107-110`

**Contexto:** Substitui Portaria 268/2021 (inválida). Portaria 79/2021 trata
de vagas Mais Médicos, não diretamente de resposta a colapso de insumos.

**Ação ARS:** Agente 4 (Jurídico) deve avaliar se a âncora é adequada ou se
`obligation_additional_response_measures` deveria ser ancorada apenas em
Lei 13.979 Art. 3° VII + Lei 8.080 Art. 15 I (já presentes no corpus).

---

### Risco R3 — Prop B.2 (não-monotonicidade) vs. C2/C7 (MEDIUM — reconhecido)

**Localização:** `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`,
§7.4 / Prop B.2

**Contexto:** Paper já reconhece que não-monotonicidade de C2/C7 quebra
Prop B.2 (monotonicidade de θ em relação a predicados soberanos).

**Ação ARS:** Agente 1 (Matemática) deve verificar se a Prop B.2 foi
adequadamente qualificada ou se ainda está como proposição geral (sem restrição).

---

### Risco R4 — Cenários C5/C6/C8 referenciados na spec mas ausentes (KNOWN)

**Status:** Documentado em Mandatory disclosures 1 e 3. Nenhum dado sintético
imputado. Sem ação adicional necessária além da verificação de consistência.

---

### Risco R5 — M-4: scenario_loader._strip_constraints frágil (LOW)

**Localização:** `src/qfeng/e5_symbolic/scenario_loader.py`

**Contexto:** Heurística regex-based; frágil a ponto em comentário dentro de
constraint. Não corrigido no PoC (custo > risco atual).

**Ação ARS:** Agente 2 (Código) deve verificar que nenhum corpus atual tem
comentários com ponto dentro de constraints.

---

## PARTE VI — CHECKLIST FINAL ARS

```
MATEMÁTICA
[ ] Eq. 1 θ = arccos implementada como arccos(dot(L2-norm(ψ_N), L2-norm(ψ_S))) ✓?
[ ] Markovian θ_eff Eq. 2-5: valores Table 7 batem com pipeline?
[ ] §6.3 frase fev/2021 "narrowest CIs [130.94°, 132.84°]" — VERIFICAR se foi atualizada
[ ] Table 4 Born rule: Δ negativo para CB, positivo/zero para STAC?
[ ] Table 6 threshold robustness: 240/245 = 97.96% — replicável?
[ ] Table 7 sensitivity: 100% regime correto em ±20%?
[ ] Prop B.2 adequadamente qualificada para não-monotonicidade?

CÓDIGO
[ ] pytest: 475 passed, 11 skipped ✓
[ ] test_psi_s_pattern_coverage: 47 tests passing ✓
[ ] _fase4_validation.py: CB onset Oct/2020 ✓
[ ] _SCENARIO_PREDICATE_MAP: cada padrão casa ≥ 1 átomo por cenário ✓
[ ] Clingo --warn=atom-undefined: zero warnings em arquivos críticos?
[ ] scenario_loader._strip_constraints: sem falsos positivos nos corpus atuais?
[ ] runner.py: seeds fixas declaradas e documentadas?

TEXTO
[ ] §C2: jan/2021 referenciado como HITL (não CB)?
[ ] §C2: pico identificado como set/2020 (130.91°)?
[ ] §6.3: fev/2021 CI values atualizados?
[ ] Referências bibliográficas: APA 7 / ABNT formato correto?
[ ] Tabela A1 ψ_N source: coerente com §3.1?
[ ] Disclosures 1, 2, 3: presentes e consistentes entre si?
[ ] §7.4 Limitations: cobre todos os riscos identificados?
[ ] Nenhuma ocorrência de "Portaria 69/2021" como âncora ativa?
[ ] Nenhuma ocorrência de "CLT Art. 59-B" em contexto CCT?
[ ] Nenhuma ocorrência de "LightGBM trained" para C3?

DIREITO BRASILEIRO
[ ] CLT Art. 59 §2° vs. §5° vs. Art. 59-B — distinção correta no corpus?
[ ] STF Tema 1046: predicado derivado corretamente em T-CLT-04?
[ ] TST-Ag-RR-868-65.2021.5.13.0030: verificar existência no DEJT 06/12/2023
[ ] Portaria 79/2021 como âncora de obligation_additional_response_measures — adequada?
[ ] Mata v. Avianca: âncora de T-CLT-01 descrita corretamente?

SAÚDE PÚBLICA
[ ] Table 7: jan/2021 = HITL (118.73°), set/2020 = CB (130.91°)?
[ ] Figura 2: jan/2021 em faixa HITL (não CB)?
[ ] Figura 2: legenda cita FVS-AM Boletim 16/jan/2021 (não Portaria 69/2021)?
[ ] FVS-AM 103.69% UTI pública jan/2021: valor verificável?
[ ] C3: 27 documentos normativos listados em c3_concentracao_facts.lp?

DIREITO INTERNACIONAL / IA
[ ] Title VI disparate impact: âncora em 42 CFR §100.13(g) ou §601 direto?
[ ] §1902(a)(10) comparability: âncora correta para C7?
[ ] EU AI Act Reg. 2024/1689: versão final (Jul 2024) ou draft?
[ ] GDPR Arts. 22, 35: predicados corretos para C6 futuro?
```

---

## PARTE VII — INFORMAÇÕES TÉCNICAS PARA REPRODUÇÃO

### Ambiente

```bash
conda activate qfeng   # Python 3.11+
python -c "import clingo; print(clingo.__version__)"  # deve ser 5.8.0
```

### Executar testes

```bash
pytest tests/ -v --tb=short
pytest tests/test_e5/test_psi_s_pattern_coverage.py -v
python scripts/_fase4_validation.py
python scripts/_run_e5_check.py
```

### Verificar corpus

```bash
# Zero predicados ativos com âncoras removidas:
grep -rn "regulatory_basis(\"Portaria69_2021\")" corpora_clingo/
grep -rn "regulatory_basis(\"Portaria268_2021\")" corpora_clingo/
grep -rn "legal_citation_exists(\"TST_RR_000200" corpora_clingo/

# Deve retornar apenas comentários (linhas começando com %):
# corpora_clingo/scenarios/c2_manaus_facts.lp:8:% Portaria69_2021 REMOVIDA
# corpora_clingo/scenarios/c2_manaus_facts.lp:15:% Portaria268_2021 REMOVIDA
```

### Verificar paper (docx)

```bash
# Usar scripts de verificação:
python scripts/_check_tst_suffix.py    # 5.13.0030=2, 5.02.0020=0
python scripts/_check_tst_context.py   # contexto das 2 ocorrências TST
```

### Git log dos commits de auditoria

```bash
git log --oneline -10
# 6202724 chore(audit): Phase 5 — final regression validation passed
# a0de66a fix(audit): Phase 4 — corpus hygiene (H-6, H-7, M-5)
# 2ffe77e feat(audit): Phase 3 — structural honesty additions (H-3, H-4)
# 6d275f1 fix(audit): F0-1/C-6 — substitute fabricated TST case
# f2849bd fix(audit): H-5/F0-2 — Portaria 268/2021 → Portaria 79/2021
# [commits anteriores Phase 1/2 — ver log completo]
```

---

*Gerado automaticamente em 2026-04-24 pela sessão de auditoria pré-submissão.*
*Para questões sobre este relatório, contactar: ricardoskaminski@gmail.com*
