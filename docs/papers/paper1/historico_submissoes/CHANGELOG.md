# CHANGELOG — Histórico de versões do Paper 1

Registra a evolução do Paper 1 (*Q-FENG: Operationalizing Cybernetic AI Governance through Neurosymbolic Quantum Interference*). Apenas mudanças **substantivas** (dados, achados, claims, nomenclatura de artefatos) são listadas. Revisões de redação, formatação e referências bibliográficas não geram entrada.

A versão **canônica de trabalho** vive em `../PAPER1_CANONICO.md` (raiz de `docs/papers/paper1/`). Este diretório (`historico_submissoes/`) preserva snapshots anteriores para auditoria e reuso de seções já validadas.

---

## Estrutura deste diretório

```
historico_submissoes/
├── CHANGELOG.md                                      (este arquivo)
├── PAPER1_v_pre_revisao_manaus.md                    (snapshot MD pré-revisão dos dados de Manaus)
└── docx_backups/                                     (11 .docx — auditoria forense, ignorado no remoto)
    ├── PAPER1_QFENG_FINAL_pre_refactor_manaus_23abr2026.docx  (snapshot 23/abr — pré-refactor Manaus)
    ├── PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx
    ├── PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed - Copia.docx
    ├── PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.bak_*.docx    (×7 timestamped)
    └── PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed_diagrams_v1.docx
```

Os arquivos `.bak_YYYYMMDD_HHMMSS.docx` foram gerados por backup automático durante a sessão de auditoria de figuras e Clingo (24/abr/2026) e estão preservados apenas como segurança forense — não devem ser usados para reuso de conteúdo. A versão consolidada dessa sessão é `PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`, posteriormente revisada para o canônico atual após o refactor dos dados Manaus.

A pasta `docx_backups/` está listada no `.gitignore` da raiz e **não é versionada no remoto público** — preserva-se apenas localmente para acesso imediato sem precisar consultar o histórico Git.

---

## 26/abr/2026 — Auditoria semântica completa do corpus Clingo

**Escopo:** auditoria das duas frentes ativas (saúde + trabalhista) com correções estruturais, integridade do corpus e extensões tipológicas.

**Mudanças aplicadas:**

### Etapa 1 — Limpeza de escopo

- C1 CEAF descartado do conjunto canônico de cenários ativos.
- `c1_ceaf_facts.lp` movido para `_deprecated/` com header explicativo.
- Comentário em `sus_direito_saude.lp` ajustado: predicados Lei 8080 Art. 6° I d permanecem (cobertura normativa SUS) sem invocação a C1.

### Etapa 2 — Bloco 1: Lacunas constitucionais
- Adicionado Art. 200 II CF/88 (vigilância epidemiológica/sanitária) em `sus_direito_saude.lp`.
- Adicionado Art. 23 II CF/88 (competência comum federalismo sanitário) em `cf88_principios_fundamentais.lp`.
- Adicionado Art. 7° XXII CF/88 (redução de riscos do trabalho) em `clt_direitos_trabalhistas.lp` + reforço da ancoragem dupla do `prohibition_negotiation_reducing_health_safety`.
- Art. 196 CF/88 desdobrado em três núcleos (direito-dever, redução de risco, acesso universal igualitário) em `sus_direito_saude.lp`.

### Etapa 3 — Bloco 2: Integridade do corpus
- Implementado predicado Lei 8080 Art. 15 I (link quebrado consertado).
- Deduplicação CPC: predicados centralizados em `cpc_fundamentacao.lp`, removidos de `clt_direitos_trabalhistas.lp` (substituídos por comentário de referência).
- Documentadas âncoras dos limiares operacionais em `emergencia_sanitaria.lp` (TOH > 85% via Ficha Técnica MS/AMIB; oxygen days < 3 via precedente Manaus 2021).

### Etapa 4 — Bloco 3: Extensões e refinamentos
- CPC Art. 489 §1° I-IV adicionados em `cpc_fundamentacao.lp`.
- Constraint T-CLT-01 refinada com cobertura de citação real sem ratio.
- Generalizada constraint regional_allocation em `sus_direito_saude.lp`.
- Adicionado Art. 7° XV CF/88 (repouso semanal) por completude pétrea.
- Adicionado CLT Art. 818 (ônus da prova) com distinção SOVEREIGN/ELASTIC.
- Adicionado Lei 13.979 Art. 3° §7° (dispensa de licitação emergencial) em `emergencia_sanitaria.lp`.
- Documentada unidade temporal (meses) nas constraints de banco de horas.

### Auditorias acumuladas
- Audit C-1: wrapper sovereign() / átomo plano (já existente).
- Audit C-3: remoção de constraint UNSAT espúrio (já existente).
- Audit C-4: Portaria 69/2021 substituída por Decreto AM 43.303/2021 (já existente).
- Audit C-5 [novo]: desdobramento Art. 196 em três núcleos.
- Audit C-6 [já existente]: TST-RR fabricado substituído por TST-Ag-RR-868.
- Audit F0-1: detecção de citação sintética (já existente).
- Audit H-5: Portaria 268/2021 removida (já existente).
- Audit H-6: scope guard Lei8080_Art7_I (já existente).
- Audit LAW-BR-04: predicado Mais Médicos renomeado (já existente).
- Audit LAW-BR-05 [novo]: ancoragem dupla de Art. 611-B XVII com Art. 7° XXII.
- Audit LAW-BR-06 [novo]: link Lei 8080 Art. 15 I implementado.
- Audit LAW-BR-07 \[novo\]: deduplicação CPC.
- Audit LAW-BR-08 \[novo\]: limiares operacionais documentados.
- Audit LAW-BR-09 \[novo\]: cobertura tipológica CPC §1° I-IV.

### Validação

- Todos os arquivos passam `clingo --syntax-check`.
- Todos os 7 cenários ativos validados via `scripts/validate_clingo_corpus.py`:
  - SAT: T-CLT-03, T-CLT-04
  - UNSAT: C2, C3, C7, T-CLT-01, T-CLT-02

### Documentação derivada

- Diretórios criados: `artefatos/auditorias/`, `artefatos/notas_metodologicas/`, `docs/papers/paper1/_apendices/`.
- Três artefatos gerados em sessão Opus 4.7 (chat) na própria data:
  - `artefatos/auditorias/AUDITORIA_CORPUS_CLINGO_26abr2026.md` — relatório operacional, PT, 340 linhas. Cobre sumário executivo, topologia em três camadas, pendências por classe (A/B/C/D), 14 auditorias acumuladas, validação integrada, discussão dogmática (C-5, C-4, F0-1/C-6, LAW-BR-05, LAW-BR-08), pendências pós-auditoria, reprodutibilidade.
  - `docs/papers/paper1/_apendices/apendice_corpus_clingo.md` — apêndice acadêmico, EN, 227 linhas. Cobre A.1 (topologia 3 camadas), A.2 (SOVEREIGN/ELASTIC), A.3 (cenários ativos pós-deprecação C1), A.4 (tabela de âncoras por cenário), A.5 (audits dogmaticamente densos), A.6 (validação 7/7), A.7 (limitações: defeasibility, arbitragem, tradução EN, auditoria EU/USA, jurisprudência TST expandida, reprodutibilidade).
  - `artefatos/notas_metodologicas/NOTAS_CORPUS_CLINGO_para_canonico.md` — notas metodológicas, EN, 274 linhas. Seis snippets atômicos com diffs prontos para `edit_block` aplicação no `PAPER1_CANONICO.md`: Snippet 1 (§2.7 Topologia 3 camadas), Snippet 2 (§4.4 E4 com 3 critérios), Snippet 3 (§5.3 Limiares operacionais TOH/O₂), Snippet 4 (§5.3 Precedente real T-CLT-04), Snippet 5 (§7.4 Defeasibility + audit transparency), Snippet 6 (§7.4 EU/USA forthcoming).
- Aplicação dos snippets ao `PAPER1_CANONICO.md` está **decoupled** desta auditoria e pode aguardar maturação do Caminho 2 (BI multi-fonte) — Snippet 3 sobre limiares operacionais pode precisar de ajuste após regeneração da Tabela 7 com BI multi-fonte.

---

## v_canonico (atual) — 25/abr/2026

- **Arquivo de trabalho (MD):** `../PAPER1_CANONICO.md` (1.258 linhas, 220 KB)
- **DOCX-fonte da conversão:** `../PAPER1_QFENG_FINAL.docx` (3,4 MB, modificado em 25/abr/2026)
- **Renomeação em 26/abr/2026:** o DOCX-fonte canônico foi renomeado de `PAPER1_QFENG_FINAL_revidando_final.docx` para `PAPER1_QFENG_FINAL.docx`, consolidando a nomenclatura definitiva do projeto. Ver Notas de Manutenção.
### Mudanças substantivas em relação a `v_pre_revisao_manaus`

| # | Tópico | Pré-revisão | Canônico |
|---|---|---|---|
| 1 | **Disparidade racial — Obermeyer et al. 2019** (Caso US/Medicaid) | 34-percentage-point racial gap | 28.8-percentage-points racial gap |
| 2 | **Pico do θ_eff no episódio Manaus 2020–2021** | θ_eff = 130.91° em **setembro/2020** | série sustentou CIRCUIT_BREAKER ao longo da janela; ativação central em **outubro/2020** com θ_eff = 126.41° |
| 3 | **Primeira ativação do Circuit Breaker (Manaus)** | **Julho/2020**, persistindo por 12 meses | **Outubro/2020**, três meses antes da declaração de calamidade pública (23/jan/2021) |
| 4 | **Lead-time retrospectivo** | implícito (junho 2020 → janeiro 2021 ≈ 7 meses) | explicitado como contribuição central: **3 meses** entre ativação CB e calamidade declarada |
| 5 | **Frase-âncora da Introdução (parágrafo 1)** | ICU occupancy had already crossed into CIRCUIT_BREAKER territory by the metric developed in this paper | the governance signal θ_eff developed in this paper had already crossed into CIRCUIT_BREAKER territory — desloca o foco do ICU bruto para o **sinal de governança θ_eff**, alinhando com a contribuição teórica |

### Razão das mudanças (#1–#4)

A revisão dos dados Manaus (`MANAUS_REFACTOR_PLAN.md`, 22–24/abr/2026)
recalibrou o cálculo do θ_eff usando microdados SIH/DATASUS reprocessados
com critérios de inclusão mais restritos (apenas internações COVID
confirmadas; exclusão de transferências interhospitalares duplicadas). O
recálculo deslocou o pico de set/2020 para out/2020 e adiou a primeira
ativação CB de jul/2020 para out/2020 — preservando o achado central
(detecção precoce em relação à calamidade declarada) mas com lead-time
mais conservador e empiricamente defensável.

A correção do gap racial (34pp → 28.8pp) reflete leitura cuidadosa do
artigo original de Obermeyer et al. (2019, *Science*), Tabela 2 — o valor
de 34pp circulou em derivações secundárias mas não corresponde ao reporte
primário.

### Razão da mudança (#5)

Reescrita motivada por feedback de revisão interna: ancorar a introdução
no **objeto de mensuração próprio do paper** (θ_eff como sinal de
governança normativa) em vez de uma proxy externa (occupancy). Isso
fortalece o argumento de contribuição original: o paper não está apenas
medindo crise hospitalar, mas operacionalizando uma **geometria de
interferência quântica** sobre o estado normativo.

---

## v_pre_revisao_manaus — 24/abr/2026

- **Arquivo:** `PAPER1_v_pre_revisao_manaus.md` (1.144 linhas, 168 KB)
- **DOCX-fonte:** sessão de auditoria de Clingo + figuras (snapshot
  intermediário, antes do refactor Manaus)

Esta versão consolida a **arquitetura completa do paper** (Introdução,
Related Work, Mathematical Foundations, Pipeline E0–E5, Validação,
Robustez, Discussão) com os achados originais sobre os 7 cenários
designados (5 CIRCUIT_BREAKER, 2 STAC). É preservada como base
estrutural reutilizável: as seções 2 (Related Work), 3 (Mathematical
Foundations) e 4 (Pipeline) permaneceram **substancialmente inalteradas**
no canônico — apenas os dados Manaus (seção 5/6) e a frase-âncora da
introdução foram revisados.

**Uso recomendado:** consulta para reaproveitamento de prosa em seções
não-Manaus. Para qualquer reuso, validar contra o canônico antes de
copiar — pode haver micro-ajustes não registrados aqui.

---

## Notas de manutenção

### 26/abr/2026 — Reorganização docs/papers/{paper1,paper2}/

Estrutura migrada de `docs/papers/` plana para `docs/papers/paper1/` e
`docs/papers/paper2/`. Migrações executadas:

- `paper1_ai_engineering/methodology.md` → `paper1/methodology.md`
- `paper2_health/methodology.md` → `paper2/methodology.md`
- `historico_submissoes/` → `paper1/historico_submissoes/`
- `media/media/` → `paper1/_media/` (desaninhamento do artefato pandoc)
- `docs/figuras/` → `paper1/_figuras/`
- `PAPER1_CANONICO.md`, `PAPER1_QFENG_FINAL.docx` → `paper1/`
- `PAPER2_GOVERNANCE_QFENG.md` → `paper2/`

Adicionalmente, **16 referências de paths absolutos** no
`PAPER1_CANONICO.md` foram atualizadas de
`...\docs\papers\media/media/imageN.png` para
`...\docs\papers\paper1\_media/imageN.png`.

Em ação subsequente do mesmo dia, esses 16 paths absolutos foram
**migrados para relativos** (`_media/imageN.png`), aumentando a
portabilidade do MD canônico para contextos de clone/fork por
colaboradores externos e reduzindo o tamanho do arquivo em ~928 bytes.

### 26/abr/2026 — Renomeação do DOCX-fonte canônico

Renomeado em disco:

```
ANTES:  docs/papers/PAPER1_QFENG_FINAL_revidando_final.docx
DEPOIS: docs/papers/paper1/PAPER1_QFENG_FINAL.docx
```

**Motivação.** Convergência de nomenclatura: o sufixo `_revidando_final`
era um marcador de processo (em revisão) que perdeu sentido após o
refactor Manaus consolidado. O nome `PAPER1_QFENG_FINAL.docx` é a
denominação definitiva para a versão de trabalho canônica.

### 26/abr/2026 — Resolução da colisão de nomenclatura
O arquivo homônimo `PAPER1_QFENG_FINAL.docx` que existia em `docx_backups/` foi renomeado para `PAPER1_QFENG_FINAL_pre_refactor_manaus_23abr2026.docx`, eliminando a ambiguidade com o canônico em `paper1/`.

ArquivoTamanhoModificadoConteúdo`paper1/PAPER1_QFENG_FINAL.docx`3,4 MB25/abr/2026**Canônico atual** — pós-refactor Manaus + figuras inseridas`paper1/historico_submissoes/docx_backups/PAPER1_QFENG_FINAL_pre_refactor_manaus_23abr2026.docx`1,5 MB23/abr/2026Snapshot anterior — pré-refactor Manaus

A diferença de tamanho (\~2× maior no canônico) reflete a inserção das figuras pós-auditoria (Diagrams 1–11 + figura A8).

### 26/abr/2026 — Política de versionamento do DOCX-fonte

Decisão registrada: o `PAPER1_QFENG_FINAL.docx` é versionado
**deliberadamente** no Git (local e remoto), mesmo sendo regenerável a
partir do `PAPER1_CANONICO.md` via pandoc reverso. Justificativa: seguro
contra falhas de regeneração (formatação, figuras, equações). Custo de
~3,4 MB no repositório é aceitável diante do valor de imutabilidade do
artefato.

---

## Convenção de versionamento

- **Snapshots MD** seguem `PAPER1_v_<descritor_curto>.md` (ex.:
  `v_pre_revisao_manaus`, `v_jurix2026_submission`, `v_arxiv_v1`).
- **Backups DOCX automáticos** (`*.bak_*`, `*.bak_YYYYMMDD_HHMMSS.docx`)
  ficam em `docx_backups/` e são preservados apenas para auditoria
  forense — não constituem versões consultáveis.
- **Pasta `docx_backups/`** é local-only: ignorada no `.gitignore` e
  não versionada no remoto público.
- Mudanças substantivas (dados, achados, claims, contribuições,
  nomenclatura de artefatos canônicos) geram entrada neste CHANGELOG.
- Mudanças de redação, ortografia, formatação ou referência bibliográfica
  **não** geram entrada.

---

*Última atualização: 26/abr/2026.*
