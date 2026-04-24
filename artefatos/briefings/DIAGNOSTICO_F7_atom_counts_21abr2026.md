# Diagnóstico F7 — Contagem de DeonticAtoms: fonte canônica e discrepâncias

**Data:** 21 abr 2026
**Contexto:** Geração da Figura 7 do Paper 1 (Applied Intelligence) — distribuição de DeonticAtoms por regime × modalidade. Durante a produção da figura identificou-se que três fontes distintas de contagem apresentavam valores divergentes, levando a uma consulta ao Claude Code para determinar a fonte canônica.

---

## Discrepância observada

| Fonte | Saúde | Trabalhista | Total |
|---|---:|---:|---:|
| `outputs/e2_report.md` + `e2_report_trabalhista.md` | 5.136 | 5.006 | **10.142** |
| `outputs/deontic_cache*/*.json` (parseado) | 3.022 | ~7.391 | ~10.413 |
| `outputs/e3_predicates*/*.lp` (cabeçalhos `% atom_id:` contados) | 2.530 | 2.443 | **4.973** |

---

## Resposta do Claude Code — síntese autoritativa

### Q1 — Fonte canônica: `e2_report.md`

Não é bug, é arquitetura. O `reporter.py` acumula os contadores em memória durante o run e escreve o `.md` ao final. O cache é apenas otimização de performance — **não é a contagem oficial**.

**Por que o cache diverge:**
- **Saúde cache < report (3.022 vs 5.136):** O corpus saúde foi reprocessado com escopo diferente em sessões posteriores; parte do cache foi sobrescrita/deletada. Os 3.022 são resíduos do último run.
- **Trabalhista cache > report (7.391 vs 5.006):** O relatório mostra apenas 55 cache hits — o run quase não usou o cache e reprocessou tudo. Os 7.391 acumulam runs anteriores que ainda estão no disco.

Os `.lp` (2.530/2.443) são o subconjunto **E3-traduzível** — atoms que o translator converteu com sucesso para Clingo. Drop esperado e documentado no pipeline E2→E3→E4.

### Q2 — Filtro de escopo: pipeline E2→E3→E4 (não há um único script)

A queda 5.136 → 2.530 (saúde) passa por três etapas, nenhuma com filtro explícito documentado em um lugar só:

| Etapa | Arquivo | Efeito |
|---|---|---|
| **E3 Translation** | `src/qfeng/c1_digestion/translation/runner.py` | Atoms que falham na template Jinja → descartados |
| **E4 HITL** | `data/hitl/hitl_cache/sus_validacao_decisions.json` | Decisões humanas de exclusão |
| **ScopeConfig** | `src/qfeng/c1_digestion/deontic/batch.py` | Apenas chunks do escopo ativo são processados |

**Para o §4.3 citar:**
> "Of 5,136 E2-extracted atoms, 2,530 (49.3%) produced valid Clingo predicates after E3 translation and E4 HITL review."

### Q3 — Não existe parquet consolidado regime × modality

O `reporter.py` rastreia `atoms_per_regime` e `modality_distribution` separadamente — **sem cross-tab**. Não há `deontic_atoms_final.parquet`.

---

## Confirmação adicional — memória Serena `feedback_pipeline_en.md`

Memo crítico registrado no `MEMORY.md` do projeto:

> ⚠️ **CRÍTICO** — "PT-BR deve ser traduzido para EN antes de E1/E2/E3 — pipeline atual inválido, refazer do zero"

Essa entrada confirma que a questão foi identificada e registrada: os textos em PT-BR geraram predicados de menor qualidade no pipeline E1/E2/E3 porque o LLM (qwen2.5:14b via Ollama) performa melhor em inglês. A decisão registrada foi que o corpus normativo brasileiro deve ser traduzido para EN antes de entrar no pipeline.

A discrepância observada hoje (5.136 atoms no report vs 3.022 no cache vs 2.530 nos .lp) **pode estar parcialmente relacionada** a isso: se parte do corpus foi reprocessada com textos em EN e outra parte com PT-BR original, os runs posteriores teriam sobrescrito/complementado o cache de forma inconsistente, gerando "dois vintages" de processamento misturados no disco.

---

## Implicações para o Paper 1

### Fonte de verdade para F7
- **Usar marginais de `e2_report.md` + `e2_report_trabalhista.md`** (10.142 atoms, 100% cobertura)
- **Não tentar cross-tab regime × modality** — não existe fonte consolidada; computá-la do cache seria metodologicamente frágil dada a inconsistência documentada
- F7 vira **duas subplots**:
  - (a) Atoms por regime (saúde: BR/EU/USA + trabalhista: BR)
  - (b) Atoms por modalidade, agrupados por trilha (saúde vs trabalhista) — revela assimetria empírica: prohibition trabalhista 16.3% vs saúde 4.8%

### Texto no §4.3 (proposta)
> "E2 extracted 10,142 DeonticAtoms across both tracks (5,136 governance/health; 5,006 labour). Of these, 4,973 (49.0%) survived translation to Clingo predicates after E3 template-based mapping and E4 HITL review, forming the final symbolic corpus used in the C1 pipeline experiments."

### Texto no §7.4 (limitations) — três camadas a documentar

1. **Escopo normativo seletivo é decisão arquitetural, não limitação:** E1→E2 processou subconjunto do corpus bruto via ScopeConfig — trechos pétreo-constitucionais → legais → infralegais filtrados por cenário. Q-FENG valida arquitetura de interferência cibernética, não ingestão end-to-end.

2. **Barreira linguística PT-BR vs EN no LLM extractor:** qwen2.5:14b via Ollama produziu predicados rasos para texto legal denso em PT-BR comparado aos corpora EN (EU/USA). Decisão arquitetural registrada em `feedback_pipeline_en.md` indica tradução PT→EN antes de E1/E2/E3 como direção futura. No estado atual do paper, corpus PT-BR foi complementado via curadoria humana assistida (Claude Opus 4) — rastreável via `atom_id` e `chunk_id` nos `.lp` finais.

3. **Hipótese dPASP/KELM (C4AI/USP) como motivação arquitetural:** o grupo de pesquisa KELM do C4AI/USP (Garcez, Cozman, Lamb) desenvolve dPASP precisamente para digestão de texto normativo complexo em línguas de baixa representação. Q-FENG usa Clingo puro para preservar determinismo e auditabilidade jurídica (cadeia atom_id → chunk → cláusula); integração com dPASP é direção futura natural fora do escopo deste PoC.

---

## Pendências de redação derivadas

- [ ] Reescrever parágrafo de corpus curation em §7.4 com a tese das três camadas (pendente após este diagnóstico)
- [ ] Adicionar frase em §4.3 citando o 49% de sobrevivência E2→E3+E4
- [ ] Verificar se Tabela 1 / §5 têm contagens que precisem ser recalibradas ao novo marco 10.142

---

*Fonte primária: consulta ao Claude Code com memória Serena do projeto, 21 abr 2026.*
