# Ponte de memória — Revisão Paper 1 Q-FENG e Caminho 2 BI multi-fonte

**Sessão anterior:** 25 de abril de 2026 (madrugada — Brasília UTC-3)
**Próxima sessão:** [data a definir após Fase 0 do Caminho 2 e/ou continuação revisão §3]
**Documento canônico:** `C:\Workspace\academico\qfeng_validacao\docs\papers\PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed_diagrams_v1.docx`

---

## Estado consolidado das decisões (25/abr/2026)

### §3 — Mathematical Foundations

| Sub-seção | Estado | Observações |
|---|---|---|
| §3.1 Hilbert space | ✅ Aplicada | Texto entregue para colar; LightGBM removido como executado; "Paper 2" → "future work"; ψ_N de C2 sem números numéricos (remetidos a §5/Appendix A) |
| §3.2 Markovian θ_eff | ✅ Aplicada | Diagram 4 removido; β = 3.0 confirmado canônico; números fabricados (Δ=+0.767, α=0.91) substituídos por descrição qualitativa |
| §3.3 Born-Rule | ⏳ Pendente | Não revisada — entra na próxima rodada |
| §3.4 Alhedonic Loss | ⏳ Pendente | Não revisada |
| §3.5 Failure Typology | ⏳ Pendente | Não revisada |

### Caminho 2 — BI multi-fonte para Manaus

**Decisão:** 25/abr/2026 — Reconstruir o predictor de Manaus com BI multi-fonte (TOH + SRAG + O₂) antes da submissão de Paper 1, eliminando a inconsistência estrutural entre score_pressao (case-mix SIH) e ψ_S (TOH real), e estabelecendo fundação metodologicamente sólida para Paper 2 (Lancet/npj saúde digital).

**Janela operacional:** 25/abr a 15/mai/2026 (2-3 semanas).

**Cronograma:**
- Fase 0: Preparação (autor) — 1-2 dias
- Fase 1: Levantamento dados primários (Claude Code) — 3-5 dias
- Fase 2: Refactor pipeline (Claude Code) — 2-3 dias
- Fase 3: Regeneração outputs (Claude Code) — 1 dia
- Fase 4: Atualização paper (chat de revisão) — 2-3 dias
- Fase 5: Validação final (chat + autor) — 1 dia

**Documentos de suporte (já gravados em workspace):**
- Relatório operacional: `artefatos/briefings/RELATORIO_CAMINHO2_BI_MULTIFONTE.md`
- Prompt Fase 1 para Claude Code: `artefatos/briefings/PROMPT_CLAUDECODE_FASE1_BI_MULTIFONTE.md`

---

## Inconsistências estruturais identificadas (já documentadas no relatório)

1. **score_pressao usa case-mix SIH (`t_uti`)** enquanto ψ_S usa TOH real (FVS-AM). Resolve com Caminho 2.
2. **Bug `t_mort = 0` em todos os 12 meses** — investigar `MORTE` codificação em `process_sih()` do `microdatasus`.
3. **Limitação de fundo: score_pressao é agregação linear ad-hoc** sem fundamento metodológico. Resolve com Caminho 2 (BI multi-fonte com pesos justificados).

---

## Mistura de gerações de dados no DOCX (a corrigir na Fase 4)

- §26 (Abstract Results) cita 126.41° → vem de `table7_new_values.csv` (atual)
- §147 (§3.2) cita β=2.0, Δ=+0.767, α=0.91 → **fabricados** (já tratados na §3.2 final)
- §330–§331 (§5.3) citam 124.88°, 130.91° → vêm de `table7_new_values_pre_health03.csv` (geração anterior)
- §332 (§5.3) cita CI [126.52°, 128.73°] → atual
- §382 (§6.3) σ=0.05/0.10 → terminologia obsoleta (todos os 12 meses são SIH+TOH)
- §419 (§7.4) "Six of twelve Manaus months use literature estimates" → **OBSOLETO**

---

## Pendências técnicas remanescentes (independentes do Caminho 2)

1. §3.1 final aplicada — confirmar aplicação no DOCX
2. §3.2 final aplicada (Diagram 4 removido) — confirmar aplicação
3. §3.3, §3.4, §3.5 — revisar (não dependem de Manaus)
4. Renumeração Diagrams 5-10 → 4-9
5. §40 "alpha" → "α"
6. §290 ψ_N de C7: `[0.991, 0.117, 0.058]` é typo? Confirmar `_PSI_N_RAW`
7. §175 vs §33: C2 classificado como `execution_absent_channel` vs `execution_inertia` — resolver
8. §401 Pothos&Busemeyer 2013 — corrigir para 2022
9. §44, §430, §439 inconsistência sobre "Paper 2" — substituir por "future work"
10. Tabelas 3 e 4 — verificar manualmente no DOCX (extração via python-docx pula de Table 2 para Table 5)

---

## Mapa exaustivo de retrabalho no DOCX (resumo)

Detalhamento completo no relatório operacional. Resumo:

**Substituições numéricas mecânicas (depois de Fase 3 entregar valores novos):**
- §26, §147 (já tratado), §260, §330, §331, §332, §336, §382, §383, §384, Tabela 7, Tabela 10

**Reescrita narrativa estrutural:**
- §27, §32, §96, §253, §326, §328 — preservam tese mas ajustam números (3 meses → N meses se mudar)

**Conteúdo a apagar:**
- §419 inteiro
- §332 trecho sobre assimetria de bootstrap CI
- §382 trecho sobre σ=0.10 para literatura

**Conteúdo a adicionar:**
- §5.3 (entre §253 e §260): descrição BI multi-fonte
- §7.4 (substituindo §419): limitação BI multi-fonte

---

## Decisões abertas que requerem o autor antes de Fase 1

1. Acesso a SCTIE/MS empenhos de O₂ Manaus 2020-2021 — viável via DEMAS/SEIDIGI?
2. Pesos do BI: PCA empírica OU pesos a priori (autor é autor das fichas técnicas MS)?
3. Granularidade temporal mensal (recomendado para Paper 1; semanal fica para Paper 2)
4. Caso C7 também usa BI multi-fonte? **Não** — só Manaus C2

---

## Acessos institucionais confirmados pelo autor (25/abr/2026)

- ✅ DATASUS (base-fonte) — acesso direto como cientista de dados MS/DEMAS/SEIDIGI
- ✅ TabNet, FTP DATASUS — acesso público
- ✅ SIVEP-Gripe — acessível
- ⚠️ SCTIE/MS empenhos O₂ — a confirmar viabilidade na Fase 0

---

## Posicionamento estratégico do paper

- **Audiência atual:** Paco Herrera (UGR/DaSCI) e Natalia Díaz-Rodríguez como suporte à candidatura pós-doc
- **Venue alvo:** JURIX 2026 (deadline ~setembro), submissão Zenodo→SSRN→arXiv como demarcação de autoria após Caminho 2 finalizado
- **Evento intermediário:** IEEE CAI Granada (8-10 mai 2026) — networking; ter draft Caminho 2 quase finalizado é vantagem
- **Paper 2 (futuro):** Lancet Digital Health / npj Digital Medicine — herdará infraestrutura BI multi-fonte

---

## Para a próxima sessão de chat

Iniciar com escolha:

**Caminho A:** Continuar revisão §3 (§3.3 Born-Rule, §3.4 Alhedonic Loss, §3.5 Failure Typology) em paralelo à Fase 0/1 do Caminho 2.

**Caminho B:** Aguardar Fase 1 do Caminho 2 ser executada por Claude Code, retomando chat para Fase 4 (atualização do paper).

**Caminho C:** Sessão dedicada de revisão de pendências técnicas independentes (renumeração diagramas, harmonização notacional, resolução §175 vs §33, etc.).

Recomendação: **Caminho A** maximiza paralelismo — revisão §3.3-§3.5 não depende de Manaus e pode avançar enquanto Claude Code executa Fases 1-3.

---

*Fim da ponte de memória.*
