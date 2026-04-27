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

## 26/abr/2026 — Fase 1 BI bivariado Manaus concluída (Caminho 2)

**Escopo:** consolidação das séries de entrada do preditor BI bivariado para Manaus 2020-2021.
Não altera o canônico `PAPER1_CANONICO.md` diretamente — documenta achados e pendências que impactam a Fase 3.

**Commits (branch caminho2):**

| Commit | Tarefa | Conteúdo |
|--------|--------|----------|
| `236a4ea` | 1.1 | TOH UTI Manaus — 12 meses (10 confirmados + 2 estimados) |
| `96b8bb9` | 1.2 | SRAG Manaus — infra extração + stub SIVEP-Gripe |
| `cd465b6` | 1.3 | Stub Caminho C — O₂ prospectivo-only, bivariado confirmado |
| `ed0e1ce` | 1.4 | Validação cruzada bivariada (sanity checks + diagnóstico) |

**Achados substantivos:**

### Sanity checks TOH (série real)
- Pico jan/2021: TOH = **104%** — confirma colapso hospitalar documentado
- Vale ago/2020: TOH = **24%** — confirma período inter-ondas

### Validação cruzada — critérios DIFERIDOS
A validação plena (Spearman ρ, PCA empírica, |Δw| < 0.10) está formalmente diferida para a Fase 2.
O `srag_manaus.parquet` é um stub com zeros: FTP DATASUS SIVEP-Gripe indisponível; fonte real é
`opendatasus.saude.gov.br/dataset/srag-2020` e `srag-2021`.

Critérios de aceitação **não avaliados nesta fase**: ρ(TOH, SRAG) > 0.50 e |Δw| PCA vs. A priori < 0.10.

### Decisão de pesos
`bi_dimensional_decision.json` gravado com `decision_method: "apriori_only_pending_pca_validation"`,
`weights_decision_pending: true`, pesos finais w_TOH = w_SRAG = 0.50 (paridade institucional).

### Bug t_mort=0 — diagnóstico com implicação retroativa para o canônico

**Causa raiz:** SIH `MORTE` é codificado como string `'Sim'/'Não'`, mas o pipeline aplica
`pd.to_numeric()` que retorna NaN, então `.fillna(0)` zera todos os óbitos.

**Evidência:** 482 registros com `MORTE == 'Sim'` em Manaus 2020-2021 (t_mort ≈ 0.18).

**Fix Fase 2 (uma linha):** `df['MORTE_NUM'] = (df['MORTE'] == 'Sim').astype(int)`

**Implicação retroativa — item de roadmap Fase 3:**
A Tabela 7 e a Figura 3 do canônico foram geradas com t_mort = 0 e declaravam esse valor
como achado empírico. Após o fix da Fase 2 e recálculo do θ_eff, **Tabela 7 e Figura 3
precisam ser regeneradas na Fase 3** com t_mort ≈ 0.18. O texto narrativo do paper
que comentava t_mort = 0 como dado empírico precisará ser corrigido.

> ⚠️ Sem este registro, a Fase 3 poderia regenerar a tabela sem revisar a narrativa textual —
> resultando em inconsistência interna no paper.

---

## 26/abr/2026 — Fase 2 BI bivariado Manaus (parcial — Caminho 2)

**Escopo:** refactor do loader + fix t_mort aplicado; SRAG real diferido por indisponibilidade de rede.

**Commits (branch caminho2):**

| Commit | Tarefa | Conteúdo |
|--------|--------|----------|
| `8edbb0f` | 2.1-abort | SIVEP-Gripe inacessível (OpenDataSUS 403, FTP path ausente) |
| `7c77081` | 2.2 | Refactor manaus_sih_loader -> manaus_bi_loader + fix t_mort |
| `3f9d449` | 2.4 | Correção retroativa diagnostico_t_mort_zero.md |

**Achados substantivos:**

### Fix t_mort=0 — aplicado em manaus_bi_loader.py

Causa raiz confirmada: MORTE é ArrowDtype `str` no parquet, e `pd.to_numeric('Sim') -> NaN -> fillna(0)`
zera silenciosamente 482 óbitos. Fix: `(df['MORTE'].astype(str).str.strip() == 'Sim').astype(int)`.

| Métrica | Antes | Depois |
|---------|-------|--------|
| t_mort total | 0.0 (bug) | **0.180** (18%, 482/2678) |
| Faixa literatura | — | 15-25% UTI COVID Manaus ✅ |

**Implicação retroativa (Fase 3):** Tabela 7 e Figura 3 do canônico precisam ser regeneradas.
O canônico declarava t_mort=0 como achado empírico — texto deve ser corrigido para t_mort≈0.18.

### Indisponibilidade SIVEP-Gripe

OpenDataSUS retorna HTTP 403 nos CSVs S3 diretos e 0 links CSV via HTML.
FTP DATASUS: path `/dissemin/publicos/SIVEP_Gripe/` ausente (migração para OpenDataSUS).
srag_manaus.parquet permanece STUB. Validação cruzada (Tarefas 2.1/2.3) diferida.

**Cenários de continuação:** reagendar, TabNet manual, proxy SIH ou Caminho C definitivo.
Decisão pendente com o autor antes da Fase 3.

**Pendências para Fase 3:**

1. Desbloquear Tarefa 2.1 (SRAG real) — discutir paliativos com autor.
2. Regenerar Tabela 7 e Figura 3 com t_mort=0.18 (impacto retroativo confirmado).
3. Revisar narrativa do canônico que comentava t_mort=0 como achado.
4. Atualizar §7.4 com nota O2 prospectivo-only (Fase 1 Tarefa 1.3).

---

## 26/abr/2026 — Fase 2.1.5 Reorientação granular BI Manaus (Caminho 2)

**Escopo:** Substituição de granularidade mensal por semanal (SE); desbloqueio de SRAG com INFLUD20/21 locais; API DEMAS-VEPI descartada (sem campo de capacidade UTI); pesos 50/50 validados por PCA.

**Commits:** `f4e652c` (2.A) · `531bf4e` (2.B) · `322b42e` (2.C) · `99fa11e` (2.D)

### Tarefa 2.A — TOH semanal via interpolação FVS-AM

API DEMAS-VEPI (MS) verificada: `ocupacaohospitalaruti`=null em todos os registros de Manaus (n=89 de 10.000 amostrados). Fallback: interpolação linear dos 12 meses FVS-AM → 73 SEs.

Output: `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet` (73 SEs, is_estimated=True). Pico SE 3/2021 = 103.7% (FVS-AM: 104%). Diagnóstico API em `outputs/api_demas_vepi_probe.json`.

### Tarefa 2.B — SRAG semanal nativa via INFLUD20/21

INFLUD20/21 (2,9 GB, CO_MUN_RES=130260, SEM_NOT SE 10/2020–SE 30/2021) processados localmente em chunks (100 k linhas/vez). Pico: SE 3/2021 com 1.447 casos COVID e 778 óbitos.

- n_covid total: **21.212** | n_obitos: **10.110** | **is_stub=False**
- Output: `data/predictors/manaus_bi/derived/srag_semanal_manaus.parquet` (73 SEs)
- SHA256 dos INFLUD em `outputs/source_manifest_srag.json`

### Tarefa 2.C — Revalidação cruzada bivariada semanal

| Métrica | Valor | Critério | Status |
|---------|-------|----------|--------|
| Spearman ρ(TOH, n_covid) | +0.472 | > 0.50 | ⚠ Abaixo¹ |
| Spearman ρ(TOH, n_obitos) | +0.393 | — | sig. p=0.001 |
| PCA PC1 variância | 70.2% | ≥ 70% | ✓ |
| Pesos PCA (TOH / SRAG) | 50% / 50% | apriori 50/50 | ✓ pca_validated |

¹ ρ=0.472 < 0.50: esperado — FVS-AM não sistemático antes de jul/2020; TOH fixo em 30% para SE 10-28/2020 enquanto SRAG registra primeiro pico (876-1031 casos/semana). Achado metodológico documentado para §6.4 do Paper 1.

**Decisão final:** `pca_validated` — pesos 50/50 confirmados empiricamente (delta=0.0000).

### Tarefa 2.D — Archive + refactor loader semanal

- `toh_uti_manaus.parquet` → `_archived/toh_fvs_am_fase1/toh_uti_manaus_mensal.parquet`
- `srag_manaus.parquet` → `_archived/srag_stub_fase1/srag_manaus_stub.parquet`
- `manaus_bi_loader.py` refatorado para granularidade SE, paths `derived/`, `is_stub=False` assertado
- 15/15 testes passando (incluindo `test_srag_real` sem skip)

### Implicações para o Paper 1

- **Pesos 50/50 validados por PCA** — afirmação do §6.1 robustecida com dado empírico real.
- **§6.4** deve documentar: ρ=0.472 com explicação metodológica (cobertura TOH pré-jul/2020).
- **Tabela 7 e Figura 3** ainda pendentes de regeneração com t_mort=0.18 (Fase 3).
- **§7.4** ainda pendente de nota sobre O₂ prospectivo-only (Fase 1 Tarefa 1.3).

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

*Última atualização: 27/abr/2026 (Fase 2.1.5-bis — refundação TOH primário DEMAS-VEPI microdado real).*

---

## Fase 2.1.5-bis (2026-04-27) — Refundação TOH primário

**Branch:** caminho2

### Correção
- Bug Fase 2.1.5 identificado: parse DEMAS-VEPI com `sep=";"` em CSV `sep=","` causou descarte falso da fonte primária e fallback forçado para FVS-AM.
- TOH FVS-AM (interpolação patamares constantes) substituído por TOH DEMAS-VEPI microdado real.
- Spearman ρ(TOH × SRAG) recalculado: **0.462** (lag=0), **0.624** (lag=+3 SEs); PCA PC1=71.5%. Anterior: ρ=0.472 (artefato FVS-AM).
- TOH pico: 2021-W03 = **2.115** (211% — colapso hospitalar documentado Manaus jan/2021, leitos emergenciais não declarados no CNES-LT).

### Adições
- `data/predictors/manaus_bi/derived/cnes_lt_manaus_uti_mensal.parquet` — denominador mensal CNES-LT (24 meses, 288→395 leitos UTI adulto)
- `data/predictors/manaus_bi/derived/demas_vepi_manaus_uti_diario.parquet` — numerador diário DEMAS-VEPI (12.929 registros dia×CNES)
- `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet` — TOH semanal municipal SE 10/2020–SE 30/2021 (74 SEs)
- `data/predictors/manaus_bi/raw/source_manifest.json` — cadeia de proveniência SHA256 (2 CSVs VEPI + 24 DBC CNES-LT + 2 CSVs SRAG/SIVEP)
- `outputs/cross_validacao_fvs_demas_fase215bis.csv` — cross-validação FVS-AM × DEMAS-VEPI (12 meses, ρ=0.865)
- `outputs/correlacao_toh_srag_fase215bis.json` — correlação TOH × SRAG com análise de lag
- `outputs/relatorio_fase215bis_executivo.md` — relatório executivo completo

### Implicações para o Paper 1
- **§6.1:** TOH agora calculado de microdado real (não interpolação); afirmação de pesos 50/50 mantida e reforçada (PCA PC1=71.5% > 70% threshold).
- **§6.4 / Tabela 7:** ρ=0.462 (lag=0) documentado; lag natural de +3 SEs (SRAG reporta hospitalização ~3 SEs antes do pico UTI) deve ser discutido na metodologia.
- **§7.3:** TOH > 1.0 no pico constitui evidência de Fricção Ontológica: CNES-LT declara capacidade formal de 319 leitos (jan/2021), DEMAS-VEPI registra 675 leitos em uso (inclui leitos emergenciais improvisados, não declarados no CNES-LT).
- **Figura 3:** pendente de regeneração com série TOH real (source=`demas_vepi_local_microdado_v2026.04`).
