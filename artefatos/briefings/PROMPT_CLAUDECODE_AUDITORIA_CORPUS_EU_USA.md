# PROMPT_CLAUDECODE_AUDITORIA_CORPUS_EU_USA

**Data:** 26 de abril de 2026
**Tipo:** Briefing operacional para Claude Code local (OpusPlan)
**Branch:** `caminho2`
**Modus operandi:** **Paralelo silencioso ao Caminho 2 BI multi-fonte.** As auditorias deste plano não bloqueiam a Fase 1 do Caminho 2 — são executadas em sessões dedicadas Opus quando o ciclo do Caminho 2 estiver em pausa (e.g., aguardando acesso institucional a SIVEP-Gripe ou empenhos O₂). Resultados são reincorporados na fase de regeneração dos outputs.
**Contexto canônico:** este briefing é a continuação simétrica de `PROMPT_CLAUDECODE_AUDITORIA_CORPUS_CLINGO.md` (auditoria do sub-corpus brasileiro, concluída em 26/abr/2026 com commit `49808c4`), aplicando a mesma metodologia de quatro estágios e quatro classes de pendências (A/B/C/D) aos sub-corpora EU e USA.

---

## Sumário executivo

Este briefing especifica auditoria semântica sistemática dos sub-corpora EU e USA do corpus Clingo Q-FENG, organizada em **duas frentes**:

- **Frente A — USA (alta prioridade).** Cobre `usa/civil_rights/civil_rights_14th.lp`, `usa/medicaid/medicaid_access.lp` e — extensão obrigatória — re-revisão de `scenarios/c7_obermeyer_facts.lp` verificando o gap de 28.8 percentage points contra Obermeyer et al. (2019, *Science*) Table 2. Justificativa: o C7 é cenário ativo do conjunto canônico (UNSAT esperado, regime CIRCUIT_BREAKER constitucional). Revisor crítico que examine o paper questionará o cenário diretamente — assimetria metodológica entre sub-corpus brasileiro auditado e sub-corpus USA não-auditado é alavanca exposta.

- **Frente B — EU (média prioridade, valor estratégico alto).** Cobre `eu/ai_act/eu_ai_act_obligations.lp` e `eu/gdpr/gdpr_data_protection.lp`. Os sub-corpora EU não são invocados pelos cenários ativos atuais (todos os sete cenários canônicos invocam apenas direito brasileiro ou USA). O valor estratégico é externo ao Paper 1 stricto sensu: (i) candidatura pós-doc UGR/DaSCI tem o EU AI Act como referência primária central; (ii) Layer S5 do Q-FENG (governança metanormativa multijurisdicional) precisa do sub-corpus EU como base dogmática; (iii) Herrera-Poyatos et al. (2026), referência canônica da rede UGR, cita explicitamente o AI Act.

**Sequenciamento.** Ambas as frentes em paralelo silencioso ao Caminho 2. **Sem dependência cruzada** entre A e B — podem ser executadas independentemente, em qualquer ordem, conforme janelas Opus disponíveis. Frente A é tendencialmente mais curta (dois arquivos + revisão do C7); Frente B é mais densa (AI Act tem 113 artigos + Anexos I-VIII; GDPR tem 99 artigos + 173 considerandos).

---

## Diferenças metodológicas em relação à auditoria brasileira

A metodologia em quatro estágios (detecção → diagnóstico → remediação → validação) e as quatro classes de pendências (A lacunas estruturais; B anti-padrões; C cobertura tipológica; D refinamentos) são **jurisdiction-portable por design** e aplicam-se diretamente aos sub-corpora EU e USA. As diferenças que demandam recalibração são as seguintes.

### Diferença 1 — Estabilidade formal das fontes primárias

AI Act (Regulamento UE 2024/1689) e GDPR (Regulamento UE 2016/679) são instrumentos extensamente debatidos cuja redação é canônica em 24 línguas oficiais da UE com força jurídica equivalente. 14th Amendment (1868) e Civil Rights Act 1964 são instrumentos institucionalmente consolidados há décadas. Não há equivalente ao problema brasileiro de portarias ministeriais sobre temas adjacentes (Audit C-4: Portaria 69/2021 sobre vacinas no SI-PNI vs. cenário de calamidade hospitalar Manaus). **Implicação operacional:** o risco de "arrasto temático LLM" é menor; a maior parte dos predicados extraídos corresponde a obrigações deônticas reais do instrumento. Isso **não** elimina a necessidade da auditoria semântica — a Frente A precisa especificamente verificar se predicados sobre Title VI § 601 não foram confundidos com Title IX (gender) ou Title VII (employment), por exemplo —, mas reduz o número esperado de auditorias da classe A em comparação com o sub-corpus brasileiro.

### Diferença 2 — Auditoria de precedentes jurisprudenciais

Para EU: o equivalente seria revisar invocações ao **CJEU** (Court of Justice of the European Union), particularmente acórdãos sobre GDPR (e.g., Schrems II — C-311/18; Meta Ireland v. Bundeskartellamt — C-252/21) e referências preliminares sobre AI Act (que ainda são limitadas porque o regulamento entrou em aplicação plena em 2025-2026).

Para USA: o equivalente seria revisar invocações ao **SCOTUS** (Brown v. Board, Plyler v. Doe, Department of Health and Human Services v. Texas, etc.) e **Federal Circuits** (relevantes para Title VI implementation — e.g., Alexander v. Sandoval, 532 U.S. 275 (2001) — que limitou ações privadas sob Title VI a discriminação intencional).

**Implicação operacional:** o protocolo de cross-referência contra bases públicas autoritativas (Audit F0-1) é **obrigatório** para qualquer precedente invocado. Para CJEU, base é EUR-Lex e Curia.europa.eu. Para SCOTUS, base é supreme.justia.com e oyez.org. Para Federal Circuits, base é Westlaw / LexisNexis ou (acesso aberto) court of appeals websites.

### Diferença 3 — Hierarquia normativa USA difere estruturalmente

USA não tem cláusulas pétreas formais análogas ao Art. 60 §4° CF/88. A hierarquia normativa estrutura-se como: Constitution → Federal statutes (e.g., Civil Rights Act) → Federal regulations (CFR) → State Medicaid Plans → administrative discretion. **Conceito de "petrification" não opera da mesma forma.** A classificação SOVEREIGN/ELASTIC para o sub-corpus USA precisa ser repensada conceitualmente:

- **SOVEREIGN no sub-corpus USA** = predicado cujo conteúdo deôntico é estabelecido por norma constitucional federal (14th Amendment, Equal Protection Clause) ou por norma estatutária federal explicitamente blindada contra modificação por nível subordinado (Civil Rights Act 1964, particularmente Title VI §601). Critério: o predicado é "irreducível pelo nível subordinado" (Federal Regulations não podem revogar Title VI §601; State Medicaid Plans não podem revogar 14th Amendment).
- **ELASTIC no sub-corpus USA** = predicado modulável por nível subordinado dentro dos limites do nível superior. Tipicamente Federal Regulations (CFR §435.4, §440.230(c)) e State Medicaid Plans.

A escolha de não usar o termo "petreous" em prosa EN é deliberada: o termo é constitutionalist-Brazilian e seria opaco para revisor USA. O equivalente operacional é "constitutionally entrenched" ou "federally preempted from regulatory modification."

### Diferença 4 — EU regulamento direto sobre Estados-Membros

GDPR e AI Act são **regulamentos** (não diretivas) — diretamente aplicáveis em todos os Estados-Membros sem necessidade de transposição nacional. Mas operam sobre Estados-Membros que têm constituições próprias, sistemas processuais próprios, e órgãos de proteção de dados nacionais (DPAs) que aplicam GDPR. Adiciona uma camada que o sub-corpus brasileiro não tem: a **interface EU ↔ Estado-Membro**.

Para os cenários atuais (não há nenhum cenário ativo no sub-corpus EU), essa interface não precisa ser modelada ainda. Mas a documentação do sub-corpus deve registrar que a aplicação dos predicados EU em qualquer cenário futuro envolverá a interface com o ordenamento do Estado-Membro relevante. **Implicação operacional:** comentários inline nos arquivos `.lp` EU devem registrar essa pendência arquitetural.

---

## Frente A — Sub-corpus USA

### A.1 Escopo

Arquivos a auditar (na ordem):

1. `corpora_clingo/usa/civil_rights/civil_rights_14th.lp`
2. `corpora_clingo/usa/medicaid/medicaid_access.lp`
3. `corpora_clingo/scenarios/c7_obermeyer_facts.lp` **(extensão obrigatória)**

### A.2 Fontes primárias para validação

- **14th Amendment**, especialmente Section 1 (Equal Protection Clause). Texto canônico em archives.gov; fontes secundárias: Cornell LII, Chemerinsky's *Constitutional Law*.
- **Civil Rights Act of 1964**, Title VI (42 U.S.C. §2000d et seq.). Texto canônico em legislative record + USC. Particular atenção a: §601 (proibição de discriminação), §602 (regulatory authority), §605 (preserva ações administrativas).
- **42 CFR Part 435 e 440**, regulamentos federais de Medicaid. Particular atenção a: §435.4 (definitions), §440.230 (sufficiency of amount, duration and scope), §440.230(c) (specific prohibition contra discriminação).
- **Obermeyer et al. (2019), "Dissecting racial bias in an algorithm used to manage the health of populations", *Science* 366(6464):447-453.** Particular atenção a: Table 2 (race-stratified outcomes), Methods (cohort definition, label proxy = total medical expenditures), Results section (28.8 pp gap reportado).

### A.3 Protocolo de auditoria por arquivo

**Para `civil_rights_14th.lp`:**

- Verificar que cada predicado SOVEREIGN tem `constitutional_basis("US_14thAmendment_Section1_EPC")` ou `statutory_basis("US_CivilRightsAct1964_TitleVI_§601")` adequadamente.
- Verificar que predicados sobre disparate impact estão **adequadamente qualificados** (após Alexander v. Sandoval 2001, ações privadas sob Title VI estão limitadas a intentional discrimination; disparate impact é actionable somente via regulamentação federal §602 ou Title VII employment context).
- Verificar tipologia de proteção: Equal Protection Clause cobre state action (não private action por sua própria força); Title VI cobre programs receiving federal financial assistance — distinção crítica para Medicaid (que é federal-state cooperative com financiamento federal).

**Para `medicaid_access.lp`:**

- Verificar âncoras a 42 CFR §435.4 (definitions of eligibility groups) e §440.230(c) (proibição de discriminação na "amount, duration, and scope" da cobertura).
- Verificar a relação Federal-State: predicados sobre obrigação federal (ELASTIC para state implementation) vs. proibição absoluta federal (SOVEREIGN para state implementation).
- Cross-referenciar com Olmstead v. L.C. (1999) sobre integração comunitária, se invocado.

**Para `c7_obermeyer_facts.lp` (re-revisão):**

- Verificar o gap de 28.8pp contra Obermeyer et al. (2019) Table 2 **literalmente**. Buscar o número canônico, pegar evidência exata: a Tabela 2 reporta percentage of Black patients at threshold X vs. baseline; o "28.8" deve corresponder a uma diferença específica entre quantis ou entre regras de treino/avaliação. Verificar se o predicado `racial_outcome_gap_pp(28.8)` (ou nome análogo) está corretamente parametrizado.
- Verificar âncoras constitucionais e estatutárias do cenário: 14th Amendment, Title VI §601, 42 CFR §440.230(c).
- Verificar se o cenário codifica adequadamente o **mecanismo da injustiça** (label proxy: total medical expenditures, que é correlacionado com raça via diferenças historicamente acumuladas no acesso ao sistema, não com necessidade médica genuína).

### A.4 Output esperado da Frente A

- Patches aplicados (correspondentes a auditorias da classe A/B/C/D que forem identificadas).
- Auditorias acumuladas com prefixo `LAW-USA-XX` (e.g., LAW-USA-01, LAW-USA-02, ...).
- Re-validação do cenário C7 mantém regime UNSAT (CIRCUIT_BREAKER, falha constitutional). **Se o regime se altera após correções, é regression real e precisa ser investigada antes de qualquer push.**
- Documentação derivada: análoga aos três artefatos da auditoria brasileira (relatório PT, apêndice EN, snippets EN). Pode ser arquivo único `AUDITORIA_CORPUS_USA_<data>.md` cobrindo as três finalidades, ou três arquivos paralelos — decisão a ser tomada na execução.

---

## Frente B — Sub-corpus EU

### B.1 Escopo

Arquivos a auditar (na ordem):

1. `corpora_clingo/eu/ai_act/eu_ai_act_obligations.lp`
2. `corpora_clingo/eu/gdpr/gdpr_data_protection.lp`

### B.2 Fontes primárias para validação

- **Regulamento (UE) 2024/1689 — AI Act.** Texto canônico em EUR-Lex (versão consolidada). Particular atenção a:
  - Art. 5 (proibições absolutas — risk assessment, social scoring, biometric categorization restricted, etc.)
  - Art. 9 (risk management system para high-risk AI)
  - Art. 10 (data governance — quality, representativeness, bias mitigation)
  - Art. 13 (transparency obligations — informing users)
  - Art. 14 (human oversight)
  - Art. 15 (accuracy, robustness, cybersecurity)
  - Anexo III (high-risk AI systems list — including social scoring, recruitment, education, law enforcement, migration, justice administration, healthcare access)

- **Regulamento (UE) 2016/679 — GDPR.** Texto canônico em EUR-Lex. Particular atenção a:
  - Art. 5 (principles relating to processing — lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity, confidentiality, accountability)
  - Art. 6 (lawfulness of processing — consent, contract, legal obligation, vital interests, public task, legitimate interests)
  - Art. 22 (automated individual decision-making, including profiling — particularmente §1 e §4 sobre special categories)
  - Art. 25 (data protection by design and by default)
  - Art. 35 (data protection impact assessment for high-risk processing)

### B.3 Protocolo de auditoria por arquivo

**Para `eu_ai_act_obligations.lp`:**

- Verificar tipologia das obrigações por artigo: proibições absolutas (Art. 5) vs. obrigações condicionadas a high-risk classification (Arts. 9-15).
- Verificar a interseção AI Act ↔ GDPR explicitamente (Art. 22 GDPR ↔ Art. 5 AI Act). Sistemas de IA que processam dados pessoais e tomam decisões automatizadas estão sujeitos a ambos os regulamentos; predicados devem refletir essa dupla aplicabilidade.
- Verificar se os predicados sobre Anexo III (high-risk) estão exaustivamente cobertos ou amostrados — se amostrados, documentar a amostragem explicitamente.

**Para `gdpr_data_protection.lp`:**

- Verificar âncoras dos princípios do Art. 5 — cada um dos 7 princípios deve ter predicado autônomo (analogia ao desdobramento Art. 196 CF/88, Audit C-5 brasileira).
- Verificar Art. 22 sobre decisão automatizada: as exceções (§2 — necessary for contract, authorized by Union/Member State law, explicit consent) devem ser predicados ELASTIC; a regra base (§1 — direito a não ser sujeito a decisão automatizada) deve ser SOVEREIGN.
- Verificar que `purpose_limitation` não é confundido com `data_minimisation` — são princípios distintos do Art. 5(1)(b) e 5(1)(c) respectivamente.

### B.4 Output esperado da Frente B

- Patches aplicados (auditorias classe A/B/C/D conforme identificadas).
- Auditorias acumuladas com prefixo `LAW-EU-XX`.
- **Atenção especial ao acoplamento AI Act ↔ GDPR:** se o corpus tratar AI Act e GDPR como totalmente desacoplados, isso é anti-padrão classe B (engenharia normativa incorreta — perde-se a interseção que é o ponto mais relevante para sistemas de IA generativa).
- Documentação derivada análoga à da Frente A.

---

## Especificação operacional comum (ambas as frentes)

### Etapa 0 — Preparação

- Verificar que branch é `caminho2` e working tree está limpa (ou em estado conhecido).
- Confirmar que `scripts/validate_clingo_corpus.py` está funcional (rodar `python scripts/validate_clingo_corpus.py` antes de qualquer modificação para baseline).

### Etapa 1 — Detecção (semantic audit)

Para cada arquivo no escopo:

1. Ler o `.lp` integralmente.
2. Cross-referenciar cada predicado contra a fonte primária correspondente (texto canônico do AI Act/GDPR/Civil Rights Act/Obermeyer 2019).
3. Classificar pendências encontradas em A/B/C/D conforme rubrica da auditoria brasileira:
   - **A** — lacuna estrutural com impacto epistêmico em cenário ativo;
   - **B** — anti-padrão de engenharia (duplicação, link quebrado, threshold sem âncora);
   - **C** — cobertura tipológica incompleta;
   - **D** — refinamento de constraint.
4. Atribuir número de auditoria com prefixo de frente (`LAW-USA-XX` ou `LAW-EU-XX`).

### Etapa 2 — Diagnóstico (Opus chat session)

- Cada pendência detectada na Etapa 1 deve ser validada em sessão Opus dedicada (chat) antes de qualquer aplicação de patch.
- O Opus produz: (i) descrição dogmática da pendência; (ii) patch proposto (predicados a adicionar/remover/modificar, com formulação Clingo-correta); (iii) justificativa de classificação SOVEREIGN/ELASTIC quando aplicável; (iv) impacto esperado na validação dos cenários.
- Para a Frente A, a re-revisão do C7 Obermeyer deve incluir verificação literal contra Table 2 do paper original — não basta confiar no histórico do CHANGELOG (a correção de 34pp → 28.8pp já registrada é ponto de partida, não validação completa).

### Etapa 3 — Remediação (Claude Code execução)

- Patches aprovados pelo Opus são aplicados via `edit_block` ou `write_file`.
- Cada patch é commitado independentemente com mensagem `audit: [LAW-USA-XX/LAW-EU-XX] descrição curta`.
- Após cada bloco de patches, rodar `clingo --syntax-check` em todos os arquivos modificados.

### Etapa 4 — Validação

- Rodar `python scripts/validate_clingo_corpus.py` após **cada commit**.
- Frente A: cenário C7 deve permanecer UNSAT. Se mudar para SAT, **investigar antes de prosseguir** (regressão real exige diagnóstico).
- Frente B: cenários ativos não invocam sub-corpus EU; validação se limita a syntax-check.

### Etapa 5 — Documentação derivada

Análoga aos três artefatos da auditoria brasileira:

- `artefatos/auditorias/AUDITORIA_CORPUS_USA_<data>.md` (PT — relatório operacional)
- `artefatos/auditorias/AUDITORIA_CORPUS_EU_<data>.md` (PT — relatório operacional)
- `docs/papers/paper1/_apendices/apendice_corpus_usa_eu.md` (EN — apêndice acadêmico, eventualmente combinando ambas as frentes em arquivo único)
- `artefatos/notas_metodologicas/NOTAS_CORPUS_USA_para_canonico.md` (EN — snippets se aplicáveis)
- `artefatos/notas_metodologicas/NOTAS_CORPUS_EU_para_canonico.md` (EN — snippets se aplicáveis)

### Etapa 6 — CHANGELOG

Atualização do `docs/papers/paper1/historico_submissoes/CHANGELOG.md` na conclusão de cada frente, com entrada análoga à de 26/abr/2026 (auditoria brasileira), listando pendências corrigidas, auditorias acumuladas, validação, documentação derivada.

### Etapa 7 — Commit consolidado e git push (com confirmação)

- Commit final consolidando os artefatos derivados.
- **`git push` retido aguardando confirmação explícita do Ricardo no chat.**

---

## Princípios operacionais

- **Modo paralelo silencioso.** Estas auditorias não bloqueiam o Caminho 2. Resultados são reincorporados na fase de regeneração dos outputs (Fase 3 do Caminho 2 ou equivalente). O paper canônico só recebe as atualizações decorrentes destas auditorias quando ambas as frentes (A e B) tiverem fechado.

- **Sem dependência cruzada A ↔ B.** A Frente A pode ser executada antes, depois ou em paralelo à Frente B. Sequenciamento é decidido em função de janelas Opus disponíveis.

- **Cross-referência obrigatória.** Toda invocação a precedente jurisprudencial passa por verificação na base pública autoritativa do tribunal emissor (Audit F0-1, brasileira, generaliza-se para SCOTUS/Federal Circuits/CJEU).

- **Documentação dogmática inline.** Decisões dogmáticas não-triviais (e.g., classificação SOVEREIGN de norma estatutária federal sem clausula pétrea formal análoga; tratamento da interseção AI Act ↔ GDPR) devem ser documentadas em comentários inline no `.lp`, no formato % NOTE: ou % DOGMATIC:, com referência explícita à auditoria que motivou a decisão.

- **Sem alteração silenciosa de cenários ativos.** Frente A modifica `c7_obermeyer_facts.lp`, que é cenário ativo. Qualquer mudança no regime SAT/UNSAT exige aprovação explícita no chat antes de ser commitada.

---

## Referências canônicas para o auditor

- **AI Act:** Regulamento (UE) 2024/1689, EUR-Lex. Versão consolidada (acessível em https://eur-lex.europa.eu).
- **GDPR:** Regulamento (UE) 2016/679, EUR-Lex.
- **14th Amendment:** Constitution of the United States, archives.gov.
- **Civil Rights Act 1964:** 42 U.S.C. §§2000a-2000h-6 (Title VI: §§2000d-2000d-7).
- **Obermeyer et al. 2019:** Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. *Science*, 366(6464), 447-453. DOI: 10.1126/science.aax2342.
- **Auditoria brasileira (precedente metodológico):** `artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md`.

---

*Briefing produzido em sessão Opus 4.7 (chat) e gravado em `artefatos/briefings/PROMPT_CLAUDECODE_AUDITORIA_CORPUS_EU_USA.md` em 26/abr/2026, branch `caminho2`.*
