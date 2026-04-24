# Briefing de ponte — Paper 1 Q-FENG: reconciliação do DOCX Chicago e das figuras

**Data:** 22 abr 2026
**Propósito:** Transferir contexto completo entre a sessão longa encerrada em 21/22 abr e a próxima sessão (Opus 4.7, chat novo).
**Fonte canônica:** `docs/papers/PAPER1_QFENG_VALIDATION.md` no disco local.

---

## 1. Estado macro do projeto

O Paper 1 do Q-FENG (submissão a *Applied Intelligence*, Springer) está em fase de consolidação final. Todas as sete figuras foram validadas, o manuscrito em Markdown atravessou quatro rodadas de edição cirúrgica esta semana, o Claude Code gerou um DOCX Chicago-style (`PAPER1_QFENG_VALIDATION_CHICAGO_FINAL.docx`) a partir do `.md`, e agora é necessário reconciliar três defeitos remanescentes antes da submissão: um problema de duplicação de parágrafo, um desalinhamento entre numeração de figuras no DOCX e arquivos `.png` no diretório de saída, e dois placeholders de figuras que nunca foram gerados.

A próxima sessão precisa resolver esses três defeitos em sequência, produzir um `.md` consistente, e regenerar o DOCX para submissão.

---

## 2. O que foi feito nas últimas sessões (21–22 abr)

Ao longo de três sessões consecutivas entre 21 e 22 de abril, o manuscrito recebeu quatro intervenções estruturais que alteraram tanto conteúdo quanto numeração. Elas estão todas refletidas no estado atual do `.md` em disco, mas precisam ser compreendidas em conjunto para não desfazer acidentalmente nenhuma delas na próxima sessão.

A primeira intervenção foi a **correção numérica da análise de robustez de threshold** (§6.1 e Abstract). O parquet `threshold_robustness.parquet` reporta 240/245 = 97,96% de estabilidade de regime com 5 falhas concentradas exclusivamente em θ_block = 130° para o cenário T-CLT-02. O paper originalmente reportava 241/245 = 98,4% com 4 falhas. A correção foi aplicada em quatro pontos (Abstract, narrativa §6.1, Tabela 6 linha T-CLT-02, Tabela 6 linha Overall) via o script `scripts/apply_paper_numeric_corrections.py`. Backup salvo em `.bak`.

A segunda intervenção foi o **diagnóstico arquitetural da contagem de DeonticAtoms**, documentado em `artefatos/briefings/DIAGNOSTICO_F7_atom_counts_21abr2026.md`. Três fontes divergiam na contagem: `e2_report.md` reportava 5.136 atoms (trilha saúde) e `e2_report_trabalhista.md` reportava 5.006 (trilha trabalhista), totalizando 10.142; o `deontic_cache/` tinha apenas 3.022 atoms (saúde); os arquivos `.lp` em `e3_predicates/` tinham 2.530 (saúde) + 2.443 (trabalhista) = 4.973. A consulta ao Claude Code via memória Serena confirmou que o `.md` do `reporter.py` é a fonte canônica; o cache é resíduo de runs anteriores; os `.lp` são o subconjunto que sobreviveu a E3 translation + E4 HITL. A memória `feedback_pipeline_en.md` do Serena registra adicionalmente que o pipeline LLM (qwen2.5:14b via Ollama) performa pior em texto legal PT-BR denso comparado ao EN, o que motivou curadoria humana assistida para parte do corpus brasileiro.

A terceira intervenção foi a **atualização do Abstract e do §4.5** para refletir os totais agregados das duas trilhas. O Abstract passou a reportar "33 primary documents (32,445 NormChunks across both tracks) from which 10,142 DeonticAtoms were extracted (5,136 in the health/governance track at mean confidence 0.930; 5,006 in the labour track at mean confidence 0.942)". O §4.5 recebeu um parágrafo novo "Pipeline survival E2 → E3 → E4" explicando que dos 10.142 atoms extraídos apenas 4.973 (49,0%) sobreviveram a E3 + E4, com as duas causas de atrição identificadas (template Jinja estrito e filtro de ScopeConfig) apresentadas como features arquiteturais e não defeitos. O parágrafo termina fazendo gancho para §7.4 sobre limitações do extractor LLM.

A quarta intervenção, aplicada pelo Claude Code em sessão separada, foi a **reestruturação da §4.2** com a introdução da Tabela 1b dedicada ao corpus trabalhista (4 documentos, 4.488 chunks, 5.006 atoms). Essa tabela revela a assimetria empírica entre as duas trilhas: prohibition 16,3% no trabalhista versus 4,8% na saúde, uma diferença de 3,4× que reforça visualmente o argumento da Fricção Ontológica como Figura 7. O Claude Code também atualizou o título do paper de "Empirical Validation of the C1 Pipeline Across Three Normative Regimes" para "Q-FENG: Operationalizing Cybernetic AI Governance through Neurosymbolic Quantum Interference", transformando o título antigo em subtítulo.

Em paralelo, a figura F7 (DeonticAtom distribution) foi recomposta como painel duplo com dados canônicos dos reports, sem cross-tab regime × modalidade (já que não existe fonte consolidada no pipeline para isso). A versão final está em `outputs/figures/F7_deontic_regime_modality.{pdf,png,svg}` e foi validada visualmente.

---

## 3. Os três defeitos remanescentes

### 3.1 Duplicação do parágrafo "Pipeline survival E2 → E3 → E4"

O `.md` atual no disco contém **duas ocorrências idênticas consecutivas** do parágrafo de pipeline survival, nas linhas 430 e 432. Provavelmente o script `apply_4_4_e3_survival_sentence.py` foi executado duas vezes em rodadas diferentes sem checagem de idempotência, ou uma sessão do Claude Code reaplicou a edição sobre o `.md` já editado. O DOCX gerado pelo Claude Code carrega a duplicação adiante (paragraphs 214 e 215 do DOCX).

**Solução preparada.** O script `scripts/fix_duplicate_pipeline_survival.py` foi criado na sessão anterior e está pronto para execução. Ele detecta as duas ocorrências, verifica que são textualmente idênticas, salva backup `.bak2`, remove a segunda ocorrência mantendo o separador `\n\n` correto, e faz pós-verificação confirmando que sobrou exatamente uma ocorrência. Comando:

```
cd C:\Workspace\academico\qfeng_validacao
python scripts\fix_duplicate_pipeline_survival.py docs\papers\PAPER1_QFENG_VALIDATION.md
```

### 3.2 Desalinhamento entre numeração de figuras no DOCX e arquivos .png

O DOCX contém sete placeholders nomeados `[INSERT FIGURE 1 HERE]` até `[INSERT FIGURE 7 HERE]`, cada um seguido por uma legenda textual escrita no `.md` em iterações anteriores. A numeração reflete a estrutura do manuscrito antes da consolidação recente das figuras, e não bate com os arquivos em `outputs/figures/`. Proposta de correspondência semântica (carece de validação visual na próxima sessão):

| Placeholder DOCX | Legenda pedida | Arquivo `.png` candidato | Observação |
|---|---|---|---|
| Figure 1 (§5.1, para 223) | Interference angle θ por cenário com bandas STAC/HITL/CB | `F3_hilbert_decision_space.png` | Confirmar que os 7 subplots cobrem a mesma narrativa |
| Figure 2 (§5.2, para 271) | Born-rule vs. classical Bayesian, 2 painéis | *não há match direto* | Precisa decisão: gerar nova ou reassignar F4_governance_suppression |
| Figure 3 (§5.3, para 282) | Manaus theta-efetivo, dual-axis time series | `F2_manaus_theta_efetivo.png` | Match semântico exato |
| Figure 4 (§5.4, para 292) | Governance suppression percentage by scenario | `F4_governance_suppression.png` | Match semântico exato |
| Figure 5 (§5.5, para 297) | DeonticAtom modality distribution | `F7_deontic_regime_modality.png` | Match semântico (versão expandida com trilha trabalhista) |
| Figure 6 (§5.6, para 307) | Alhedonic heatmap 3-column | *não existe* | Decisão pendente: gerar ou remover placeholder |
| Figure 7 (§5.4 sub-seção, para 311) | Obermeyer C7 ψ_N calibration histogram | *não existe* | Decisão pendente: gerar ou remover placeholder |

Duas figuras foram produzidas esta semana mas **não têm placeholder correspondente no DOCX**: `F5_threshold_robustness.png` (pertence à §6.1) e `F6_psi_sensitivity.png` (pertence à §6.2). Precisam ser inseridos placeholders nessas duas seções.

### 3.3 Figuras F6 (alhedonic heatmap) e F7 (Obermeyer C7) do DOCX nunca foram geradas

Ambas constam como placeholders no DOCX com legendas completas, mas os arquivos `.png` nunca foram produzidos. Decisão pendente do usuário: (a) gerar as duas figuras agora antes de regerar o DOCX, o que fortalece a narrativa visual do paper mas consome tempo; ou (b) remover os placeholders e as legendas correspondentes do `.md`, entregando o paper com 5 figuras ao invés de 7. Nenhuma das duas é bloqueante para a submissão.

---

## 4. Arquivos-chave para a próxima sessão

A próxima sessão precisa ter acesso imediato aos seguintes artefatos. Todos estão no disco local do usuário, dentro de `C:\Workspace\academico\qfeng_validacao\`:

**Manuscrito e derivados.** O arquivo canônico é `docs/papers/PAPER1_QFENG_VALIDATION.md` (963 linhas, 135 KB após a duplicação, esperado 944 linhas após deduplicação). O DOCX consolidado fica em `PAPER1_QFENG_VALIDATION_CHICAGO_FINAL.docx` (469 parágrafos, 15 tabelas, 0 inline shapes — todos os placeholders ainda textuais). Backups `.bak` e `.bak2` estão no mesmo diretório.

**Figuras validadas.** O diretório `outputs/figures/` contém os arquivos PDF/PNG/SVG de F2 até F7, todos com nomenclatura `F{n}_{descriptive}.{ext}`. F1 (pipeline diagram E0–E5) ainda está pendente de decisão: reusar `docs/figuras/qfeng_pipeline_saude_v3.svg` ou produzir versão nova unificada.

**Scripts de edição cirúrgica.** Em `scripts/`, na convenção `apply_*.py` e `fix_*.py`, estão as ferramentas de modificação do `.md`. Destacam-se para a próxima sessão: `fix_duplicate_pipeline_survival.py` (pronto para execução imediata), `apply_paper_numeric_corrections.py` (já aplicado, referência para padrão), `apply_abstract_corpus_totals.py` (já aplicado), `apply_4_4_e3_survival_sentence.py` (já aplicado, causador da duplicação quando rodado duas vezes).

**Dados canônicos.** Os reports E2 em `outputs/e2_report.md` e `outputs/e2_report_trabalhista.md` são a fonte de verdade para todas as contagens do paper. Os parquets em `outputs/e5_results/` sustentam as tabelas de resultados. Inventário dos `.lp` finais em `outputs/e3_predicates/` e `outputs/e3_predicates_trabalhista/`.

**Briefings acumulados.** Em `artefatos/briefings/`, especialmente `DIAGNOSTICO_F7_atom_counts_21abr2026.md` (explicação arquitetural das três fontes de contagem de atoms), `BRIEFING_SESSAO_20-21abr2026.md` (sessão anterior), e este próprio arquivo.

---

## 5. Plano de ação sugerido para a próxima sessão

A próxima sessão deve começar executando imediatamente o script de deduplicação, sem necessidade de confirmação prévia do usuário, já que a duplicação é textualmente idêntica e o defeito está documentado. Em seguida, a sessão deve abrir as sete figuras `.png` em `outputs/figures/` (usar `copy_file_user_to_claude` e `view`) para confirmação visual das correspondências semânticas propostas acima. Sugiro fazer em paralelo: enquanto a visualização ocorre, pedir ao usuário a decisão sobre F6 (alhedonic heatmap) e F7 (Obermeyer C7) do DOCX — gerar ou remover.

Após essas confirmações, o terceiro passo é produzir um script único (`scripts/reconcile_figures_numbering.py` sugerido) que faça três edições no `.md`: (a) renumere as referências de figura conforme o mapeamento acordado, (b) insira os dois placeholders faltantes em §6.1 e §6.2, e (c) ajuste qualquer legenda cujo conteúdo não corresponda mais ao arquivo `.png` apontado. O script deve seguir o padrão estabelecido dos outros scripts `apply_*` e `fix_*`: validação prévia de que cada `old_str` aparece exatamente uma vez, backup `.bak`, pós-verificação.

O quarto passo é pedir ao Claude Code, via prompt no chat do usuário com ele, para regerar o DOCX a partir do `.md` reconciliado, agora com as imagens inseridas nos placeholders. Preservar a convenção de conversão Chicago-style que o Claude Code já domina.

O quinto e último passo é uma inspeção visual do DOCX final e, se tudo estiver conforme, marcar o Paper 1 como pronto para submissão ao arXiv e ao *Applied Intelligence*.

Como tarefas paralelas de menor urgência que podem aguardar a próxima sessão estão: a pesquisa de literatura sobre o grupo de pesquisa KELM do C4AI/USP (Cozman, Garcez, Lamb, dPASP) para fundamentar uma eventual reescrita do §7.4 com a tese das três camadas de curadoria PT-BR (esse parágrafo ainda não foi reescrito e existe apenas como gancho no final do §4.5); e o fechamento da decisão sobre F1 (pipeline diagram).

---

## 6. Preferências de trabalho do usuário (consolidado das sessões)

O usuário prefere entregáveis diretos sobre comentários analíticos extensos, aprova seção por seção antes de avançar, e não modifica texto já aprovado sem instrução explícita. Trabalha em prosa acadêmica densa em inglês para o paper e português formal para briefings e comunicações com contatos institucionais. Valoriza consistência tipográfica e identifica erros matemáticos ou visuais com precisão. Os scripts de edição devem seguir o padrão já estabelecido: validação prévia de unicidade do `old_str`, backup `.bak`, aplicação, pós-verificação explícita com `[OK]`/`[!!]`. Para edições em arquivos do projeto Q-FENG, preferir Desktop Commander (edit_block, write_file) sobre Filesystem MCP quando ambos estiverem disponíveis, pois são considerados mais seguros para modificações em arquivos grandes. Citações em estilo author-date (Chicago/APA-adjacent) no paper; ABNT nos documentos em português. Os diagramas seguem padrão grayscale acadêmico com tipografia serif (DejaVu Serif / Times New Roman), 300 dpi para PNG, matplotlib com `mathtext.fontset=dejavuserif`.

---

## 7. Riscos a monitorar na próxima sessão

Dois riscos merecem atenção específica. O primeiro é a tentação de fazer edições na sequência errada: se o DOCX for regerado antes da deduplicação do `.md`, a duplicação se propagará novamente; portanto a ordem (dedup → renumeração → DOCX) deve ser respeitada. O segundo é a reversão acidental das edições cumulativas já aplicadas: o `.md` atual contém 97,96%, totais agregados, Tabela 1b, parágrafo de pipeline survival — toda intervenção nova deve ser cirúrgica e preservar esse estado, nunca regenerar o `.md` a partir de uma versão anterior. A versão do `.md` anexada ao upload da sessão anterior (944 linhas) é anterior a todas essas edições e deve ser explicitamente descartada como referência.

Um terceiro risco menor é a acumulação de arquivos `.bak` no diretório `docs/papers/`. Após validação final do manuscrito, o usuário pode optar por consolidar tudo sob git e limpar os backups.

---

*Preparado para transferência a uma nova sessão Claude Opus 4.7.
Arquivo canônico referenciado: `C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_VALIDATION.md`.*
