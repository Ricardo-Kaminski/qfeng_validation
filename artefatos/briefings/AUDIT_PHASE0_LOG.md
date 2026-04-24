# Audit Phase 0 Log — Verificações Externas Bloqueantes
# Q-FENG Pre-submission Audit — JURIX 2026 / UGR Review
# Verificado em: 2026-04-24

---

### F0-1 — TST-RR-000200-50.2019.5.02.0020
**Status:** NÃO ENCONTRADO
**Data verificação:** 2026-04-24

**Resultado:**
Consulta exaustiva à base jurisprudencial do TST (jurisprudencia.tst.jus.br),
PJe TRT-2 e agregadores públicos (Jusbrasil, Migalhas, Conjur) com múltiplas
variações de formatação (RR, AIRR, 6 e 7 dígitos pré-ponto) não retornou o
acórdão. A própria numeração é inconsistente com o padrão CNJ vigente desde
2008 para feitos de 2019 (que exige 7 dígitos pré-ponto). O acórdão não existe.
Trata-se de fabricação sintética inadvertida que ingressou no corpus como real.

**Ação no paper:** Substituir âncora por acórdão real verificável (Opção A —
recomendada) OU reformular T-CLT-04 como "synthetic positive control" explícito
(Opção B).

**OPÇÃO A (recomendada):** Substituir por TST-Ag-RR-868-65.2021.5.13.0030
  - Julgado pela 2ª Turma, DEJT 06/12/2023
  - Tema: validade de cláusula da CCT dos bancários (2018/2020 e 2020/2022)
    sobre compensação de horas à luz do Tema 1046/STF (ARE 1.121.633)
  - Tese STF Tema 1046: "são constitucionais os acordos e as convenções
    coletivos que, ao considerarem a adequação setorial negociada, pactuam
    limitações ou afastamentos de direitos trabalhistas, desde que respeitados
    os direitos absolutamente indisponíveis"
  - Cria controle positivo mais forte: vincula decisão a precedente obrigatório

**OPÇÃO B:** Reformular T-CLT-04 como "synthetic positive control" na tabela de
  cenários e remover o path do paper (linha 624 do docx canônico).

---

### F0-2 — Portaria GM/MS 268/2021
**Status:** ERRO — âncora normativa inexistente para o escopo atribuído
**Data verificação:** 2026-04-24

**Ementa real:**
"Divulga resultado final das metas institucionais para fins de avaliação de
desempenho de servidores do Ministério da Saúde."
(Portaria SE nº 268, de 29/06/2021 — NÃO GM/MS, NÃO 28/jan, NÃO Manaus)

**Data publicação:** DOU de 02/07/2021

**Resultado:**
Não existe "Portaria GM/MS nº 268, de 28 de janeiro de 2021". A única Portaria
268/2021 do MS é da Secretaria-Executiva (SE), de junho de 2021, sobre metas
de desempenho de servidores. Não tem relação com emergência sanitária, Manaus,
oxigênio ou COVID-19. A hipótese de ser o PNO também não se sustenta: o PNO
foi veiculado pela MP 1.026/2021 (06/jan) e pela Portaria GM/MS 69/2021
(registro SI-PNI — já removida no C-4). Possível origem da confusão: cruzamento
com art. 268 do Código Penal (infração de medida sanitária preventiva).

**Ação no corpus:** Remover regulatory_basis("Portaria268_2021") e substituir
por âncoras reais:
  - Lei 13.979/2020 Art. 3º VII (requisição) + Art. 10 (coordenação federativa)
  - Decreto AM 43.303/2021 (calamidade estadual, 23/jan/2021) — já no corpus
  - Portaria GM/MS 79, de 18/jan/2021 (ampliação emergencial vagas Mais Médicos
    para Manaus em razão da pandemia) — âncora específica e verificável
  - Portaria GM/MS 188/2020 (ESPIN + COE-COVID-19) — já no corpus

**APLICADO:** H-5 fix em emergencia_sanitaria.lp + c2_manaus_facts.lp
  (Portaria268_2021 → Portaria79_2021 + Lei13979_Art10)
  Data: 2026-04-24

---

---

### F0-1 — Resolução final (Opção A aplicada)
**Data aplicação:** 2026-04-24

**Substituto:** TST-Ag-RR-868-65.2021.5.13.0030
- 2ª Turma TST, DEJT 06/12/2023
- Tema: validade de CCT bancária (2018/2020 e 2020/2022) sobre banco de horas anual
- Âncora: STF Tema 1046 (ARE 1.121.633) — prevalência do negociado sobre o legislado
- Base: CLT Art. 59 §2° + Art. 611-A I + CF/88 Art. 7° XXVI

**Arquivos modificados:**
- NOVO: `corpora_clingo/brasil/trabalhista/tst_decisoes/tst_ag_rr_868_65_2021.lp`
- ATUALIZADO: `corpora_clingo/scenarios/t_clt_04_facts.lp`
  (remoção de `TST_RR_000200_50_2019_5_02_0020`, adição de `TST_Ag_RR_868_65_2021_5_13_0030`)
- ATUALIZADO: `docs/papers/PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed.docx`
  (3 scripts aplicados: apply_f01_tst_case_substitution.py + apply_f01_fix_split_runs.py + apply_f01_fix_suffix.py)
  Post-check: `5.13.0030`=2, `5.02.0020`=0, `Ag-RR-868`=2, `000200`=0 ✓

---

### Status geral Phase 0

| Item | Status | Ação | Data |
|------|--------|------|------|
| F0-1 TST case | RESOLVIDO + APLICADO | Opção A — TST-Ag-RR-868-65.2021.5.13.0030 | 2026-04-24 |
| F0-2 Portaria 268 | RESOLVIDO + APLICADO | H-5 fix aplicado | 2026-04-24 |
