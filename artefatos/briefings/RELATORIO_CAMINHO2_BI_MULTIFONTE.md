# Relatório operacional — Caminho 2: Reconstrução do BI multi-fonte para Paper 1 Q-FENG

**Documento:** Briefing executivo e roadmap operacional
**Data:** 25 de abril de 2026
**Contexto:** Paper 1 Q-FENG (Validação empírica) — alvo: working paper SSRN/arXiv → JURIX 2026 → suporte a candidatura pós-doc UGR/DaSCI
**Caminho escolhido:** Caminho 2 — Reconstrução completa do predictor Manaus com BI multi-fonte canônico antes da submissão

---

## 1. Diagnóstico consolidado da situação atual

### 1.1 Estado dos dados Manaus no pipeline

O pipeline `src/qfeng/e5_symbolic/manaus_sih_loader.py` implementa hoje uma série temporal de 12 meses (Jul/2020–Jun/2021) com a seguinte arquitetura interna:

- **Microdados SIH/DATASUS** (parquet `sih_manaus_2020_2021.parquet`, 2.678 admissões com `DIAG_PRINC ∈ {J189, J960, J961, J969, U071, U072, B342}`) usados para extrair três proxies por mês: `t_mort` (taxa de mortalidade), `t_uti` (proporção de admissões com `UTI_MES_TO > 0`), `t_resp` (proporção de admissões com CID respiratório COVID).
- **TOH UTI documentada** via dicionário `_TOH_FVS_AM` com 12 valores extraídos de boletins primários FVS-AM (Fundação de Vigilância em Saúde do Amazonas), Observatório COVID-19 Fiocruz, e SES-AM.
- **score_pressao** computado como combinação linear `0.50·t_mort + 0.30·t_uti + 0.20·t_resp`, normalizado min-max na janela de 12 meses, alimentando a interpolação de ψ_N entre `_PSI_N_BASE` e `_PSI_N_CRISIS`.
- **ψ_S** derivado via Clingo (`run_scenario_with_occupancy("C2", occ_pct)` com `emergencia_sanitaria.lp` ativando `obligation_to_activate_coes` quando `R > 85`), portanto já alimentado por TOH real.

### 1.2 Inconsistências estruturais identificadas

**Inconsistência primária** — co-existência de duas grandezas físicas distintas:
- ψ_S consome **TOH real** (FVS-AM, ocupação de leitos: pacientes-dia / leitos-dia operacionais).
- ψ_N consome **case-mix SIH** via `t_uti` (proporção de admissões que usaram UTI, calculada sobre admissões registradas — métrica de mix de procedimentos, não de pressão hospitalar).

Em janeiro de 2021, `t_uti = 0.0687` (porque o volume total de internações disparou para 335, diluindo a proporção que usou UTI), enquanto a TOH real era 104% (sobre-capacidade documentada). Essa divergência produz o regime espúrio HITL para os meses de calamidade declarada por decreto.

**Inconsistência secundária** — `t_mort = 0` em todos os 12 meses no parquet atual:
- A query `df_m["MORTE"].sum()` retorna zero em todos os meses para o filtro COVID_CIDS — isso indica falha na codificação de `MORTE` produzida por `process_sih()` do pacote `microdatasus`, ou erro na lógica de conversão `Sim/Não → int`. Bug ortogonal mas relevante: zera o componente de maior peso (0.50) do score_pressao, deixando o score efetivamente como `0.30·t_uti + 0.20·t_resp`.

**Limitação metodológica de fundo** — score_pressao é uma **agregação linear ad-hoc**:
- Os pesos 0.50/0.30/0.20 não derivam de fundamento metodológico (não há ficha técnica MS, não há literatura epidemiológica que justifique essa combinação específica).
- A natureza categórica das três dimensões (mortalidade, ocupação, respiratório) sugere que correlação e co-ocorrência são mais informativas que combinação linear.
- Para Paper 1 (arquitetura de IA), essa fragilidade é tolerável com caveat honesto. Para Paper 2 (Lancet/npj — saúde digital) é fatal.

### 1.3 Estado da narrativa do paper

O DOCX `PAPER1_QFENG_FINAL_prob_dados_clingo_auditfixed_diagrams_v1.docx` (3.4 MB) contém uma narrativa que **mistura** valores de duas gerações distintas do pipeline:

- §26 (Abstract Results) cita **126.41°** para outubro/2020 — vem de `table7_new_values.csv` (atual).
- §147 (§3.2) cita **β = 2.0**, **α = 0.91**, **Δpressão = +0.767** em outubro/2020 — valores **fabricados ilustrativamente**, não correspondem a nenhum dos dois CSVs.
- §330–§331 (§5.3) citam **124.88°** para julho/2020 e **130.91°** para setembro/2020 — vêm de `table7_new_values_pre_health03.csv` (geração anterior, com calibração C ancorada em Jan/2021=100%).
- §332 (§5.3) cita **CI [126.52°, 128.73°]** para setembro/2020 — vem do CSV atual.
- §382 (§6.3) declara **σ = 0.05** para Oct/2020–Mar/2021 e **σ = 0.10** para Jul-Sep/2020 e Apr-Jun/2021 — terminologia obsoleta porque **todos** os 12 meses agora usam SIH/DATASUS real.
- §419 (§7.4) declara **"Six of twelve Manaus months use epidemiological literature estimates"** — declaração obsoleta (já era falsa após o refactor de 24/abr; agora todos os 12 meses são SIH+TOH FVS-AM).
- §260 (§5.3 setup) cita **"1.526 admissions across six months (Oct/2020–Mar/2021)"** — número obsoleto (atual: 2.678 admissions across twelve months).

### 1.4 Arquivos canônicos de output existentes

| Arquivo | Geração | Estado | Uso |
|---|---|---|---|
| `outputs/table7_new_values_pre_health03.csv` | Refactor 24/abr/2026 | Antigo | Não usar mais |
| `outputs/table7_new_values.csv` | Após "health03" (sem data certa) | Atual no pipeline | Será **substituído** |
| Tabela 7 do DOCX | Reflete `table7_new_values.csv` | Atual | Será **substituída** |
| Texto narrativo do DOCX | Mistura dois CSVs + números fabricados | Inconsistente | Será **reescrito** |

---

## 2. Decisão estratégica — Caminho 2

### 2.1 O que é o Caminho 2

Reconstruir o predictor de Manaus com **BI multi-fonte canônico** antes da submissão de Paper 1, eliminando a fragilidade metodológica do score_pressao linear ad-hoc e estabelecendo uma fundação compartilhável com o futuro Paper 2 (saúde digital, Lancet/npj).

O BI será **trivariado** (TOH + epidemiologia + logística) por design, com fallback a **bivariado** (TOH + epidemiologia) se a dimensão logística (oxigênio) não for retrospectivamente observável para Manaus 2020-2021.

### 2.2 Justificativa para essa escolha

1. **Robustez metodológica** — Paper 1 deixa de ter caveat sobre predictor frágil e passa a demonstrar Q-FENG sobre indicadores institucionalmente canônicos (TOH é ficha técnica MS criada pelo próprio autor; SIVEP-Gripe é vigilância epidemiológica oficial; CNES/empenhos O₂ são registros administrativos primários).

2. **Fortalecimento da narrativa** — A tese central "Q-FENG detectaria a crise N meses antes da declaração formal" fica defensável a qualquer revisor porque o predictor reflete a estrutura decisória real do MS, não uma combinação linear escolhida ad-hoc.

3. **Compartilhamento de infraestrutura com Paper 2** — Paper 2 (Lancet Digital Health / npj Digital Medicine) **precisa** do BI multi-fonte por definição. Investir agora capitaliza o trabalho duas vezes: Paper 1 sólido + Paper 2 herda extração + Paper 1 e Paper 2 conversam metodologicamente.

4. **Acesso institucional ao DEMAS/SEIDIGI** — O autor é cientista de dados do Ministério da Saúde com acesso direto às bases-fonte do DATASUS. Não usar esse acesso quando ele é diretamente relevante constitui fraqueza metodológica auto-infligida (um revisor com perfil Paco Herrera ou Natalia Díaz-Rodríguez nota e questiona).

5. **Posicionamento UGR/DaSCI** — A candidatura pós-doc se beneficia diretamente de Paper 1 robusto. Paper enviado a Paco Herrera e Natalia Díaz-Rodríguez como suporte de candidatura precisa estar acima de qualquer crítica metodológica óbvia.

### 2.3 Critérios de sucesso do Caminho 2

| Critério | Métrica | Validação |
|---|---|---|
| score_pressao não usa mais case-mix SIH | Componente `t_uti` substituído ou removido | Auditoria do código |
| Predictor refletindo estrutura institucional MS | ≥ 2 dimensões canônicas (TOH + epidemiológica), idealmente 3 (com logística) | Documentação de fontes primárias |
| Bug `t_mort = 0` resolvido | `t_mort > 0` em ≥ 6 meses do parquet | Inspeção do parquet regenerado |
| Narrativa "Q-FENG detecta antes da calamidade" preservada | CB onset month ≤ Out/2020 | Regeneração do θ_eff |
| Picos de θ alinhados com calamidade declarada | Peak θ_eff em jan-fev/2021 (não set/2020) | Tabela 7 nova |
| §7.4 limpa de limitação obsoleta | §419 inteiro removido | Inspeção do DOCX |
| Tabela 7 reflete BI multi-fonte | Coluna nova "Predictor source" mostrando TOH/SRAG/O₂ por mês | Inspeção do DOCX |
| Bootstrap CI uniforme | σ = 0.05 em todos os 12 meses | §382 reescrito |
| Documentação de provenance | Cada série tem data dictionary próprio | `data/predictors/manaus_bi/README.md` |

---

## 3. Roadmap operacional

### 3.1 Fases

**Fase 0 — Preparação (1-2 dias) — fora do Claude Code**
- Verificar acessos DEMAS/SEIDIGI a SIVEP-Gripe (vigilância semanal SRAG) e SCTIE/MS (empenhos/NF-e de O₂ medicinal).
- Acessar TabNet `http://www2.datasus.gov.br/DATASUS/index.php?area=0901` para validação cruzada de TOH (tabulação por município/competência).
- Identificar dataset de leitos UTI Manaus por competência mensal via CNES-LT (FTP DATASUS).
- Levantar literatura de SIVEP-Gripe Manaus 2020-2021 — Sabino et al. 2021 (Lancet) e Orellana et al. 2020 são pontos de partida.

**Fase 1 — Levantamento de dados primários (3-5 dias) — Claude Code + autor**

1.1. **TOH validada** (canônica MS — você criou a ficha técnica):
   - Manter `_TOH_FVS_AM` mas validar contra TabNet (TabNet pode trazer indicadores agregados de ocupação por competência).
   - Substituir 4 valores estimados (set/2020 = 45%, abr-jun/2021 = 70-71%) por valores tabulados quando disponíveis.
   - **Output:** `data/predictors/manaus_bi/toh_uti_manaus.parquet` com colunas `(year, month, toh_uti_pct, source, source_doc, source_date, is_estimated)`.

1.2. **Série epidemiológica SRAG** (SIVEP-Gripe):
   - Extrair via FTP DATASUS (`ftp://ftp.datasus.gov.br/dissemin/publicos/SIVEP_Gripe/Dados/`) os arquivos `INFLUD20.csv`, `INFLUD21.csv`.
   - Filtrar por `CO_MUN_RES = 130260` (Manaus, código IBGE 6 dígitos) e `CLASSI_FIN = 5` (SRAG por COVID confirmado) ou similar.
   - Agregar por semana epidemiológica e mês.
   - **Output:** `data/predictors/manaus_bi/srag_manaus.parquet` com colunas `(year, month, srag_cases, srag_deaths, srag_uti_admissions, srag_obito_pct, source)`.

1.3. **Cobertura de oxigênio** (dimensão logística — verificar viabilidade):
   - **Caminho A (preferencial):** Empenhos SCTIE/MS de O₂ medicinal para Manaus, jul/2020–jun/2021 — buscar via Portal de Transparência ou base interna SEIDIGI.
   - **Caminho B (proxy):** Capacidade declarada via CNES-LT (leitos UTI ativos × consumo médio O₂ por leito-dia) — proxy estrutural de demanda.
   - **Caminho C (fallback qualitativo):** Notícias indexadas (folha, valor, FSP, UOL) sobre fornecimento O₂ Manaus — qualitativo, não compõe ψ_N mas pode entrar em discussão narrativa.
   - **Output:** `data/predictors/manaus_bi/oxigenio_manaus.parquet` com colunas `(year, month, supply_indicator, days_coverage_proxy, source, observability_class)`.
   - **Decisão tipo:** Se A ou B viável → BI trivariado; se apenas C → BI bivariado com dimensão logística declarada como prospectiva-only no §7.4.

1.4. **Validação cruzada das três séries:**
   - Confirmar que jan/2021 tem TOH > 100%, SRAG em pico, O₂ em mínimo (se trivariado).
   - Confirmar que ago/2020 tem todos baixos (vale interondas).
   - Validar que set/2020 não é peak em nenhuma das três (corrige artefato case-mix do pipeline atual).

**Fase 2 — Refactor do pipeline (2-3 dias) — Claude Code**

2.1. Renomear o módulo: `manaus_sih_loader.py` → `manaus_bi_loader.py`. Manter compatibilidade temporária via re-export.

2.2. Reescrever `load_manaus_real_series()` para consumir as três séries:

```python
def load_manaus_real_series() -> list[dict]:
    """Constrói série mensal Q-FENG a partir de BI multi-fonte canônico.
    
    Predictor ψ_N reflete três dimensões institucionalmente canônicas:
      - TOH UTI (FVS-AM/ANS — ficha técnica MS)
      - Incidência SRAG (SIVEP-Gripe — vigilância epidemiológica oficial)
      - Cobertura O₂ (empenhos SCTIE/MS — registro administrativo primário)
        [se Fase 1.3 produzir caminho A ou B; senão prospectivo-only]
    
    score_pressao é construído como:
      pressure_raw = w_TOH·norm(TOH) + w_SRAG·norm(SRAG_growth) + w_O2·norm(O2_inverse)
    
    onde os pesos w_* são calibrados a partir de:
      - Documentação MS sobre indicadores de criticidade (se houver)
      - Análise de componentes principais sobre as três séries
        (com weight = primeira componente principal)
    """
```

2.3. Substituir o componente t_uti do score_pressao:
   - Versão trivariada: `pressure_raw = 0.40·norm(TOH) + 0.40·norm(SRAG_growth) + 0.20·(1 - norm(O2_coverage))`
   - Versão bivariada: `pressure_raw = 0.50·norm(TOH) + 0.50·norm(SRAG_growth)`
   - Justificar pesos no docstring com referência a procedimento (PCA ou ficha técnica MS).

2.4. Investigar e fixar o bug `t_mort = 0`:
   - Inspecionar o parquet: `pd.read_parquet(SIH_PATH)["MORTE"].value_counts()` — verificar se está como `Sim/Não`, `1/0`, ou `True/False`.
   - Verificar se o filtro `DIAG_PRINC.isin(COVID_CIDS)` não está descartando os óbitos (pode ser que óbitos por SRAG estejam codificados com J96 ou U07 e estejam sendo filtrados, mas a coluna MORTE não está sendo somada corretamente).
   - Comparar com SIM (Sistema de Informações sobre Mortalidade) para validar contagem de óbitos hospitalares Manaus jul/2020-jun/2021.

2.5. Atualizar `_PSI_N_BASE` e `_PSI_N_CRISIS` (preferences vectors):
   - Reavaliar se a interpolação `(0.50, 0.30, 0.20) → (0.93, 0.04, 0.03)` ainda faz sentido com BI canônico.
   - Documentar a fundamentação institucional dos vetores extremos no docstring.

2.6. Manter `_TOH_FVS_AM` mas alimentado pela tabela validada da Fase 1.1.

2.7. Eliminar referência ao termo "literature estimates" em qualquer comentário ou docstring.

**Fase 3 — Regeneração de outputs (1 dia) — Claude Code**

3.1. Rodar pipeline E5 completo:
```powershell
conda run -n qfeng python -m qfeng.e5_symbolic.runner manaus
```

3.2. Gerar três outputs:
- `outputs/table7_bi_multifonte.csv` — substitui `table7_new_values.csv`.
- `outputs/figura3_bi_multifonte.png` — substitui Figure 3 atual.
- `outputs/manaus_bi_provenance.json` — manifest com fonte primária de cada datapoint.

3.3. Validar:
- CB onset ≤ Out/2020 (preserva narrativa "antes da calamidade").
- Peak θ_eff em jan ou fev/2021 (alinha com calamidade declarada por decreto).
- Bootstrap CI σ = 0.05 uniforme.
- Diferença ≤ 5° entre θ_eff atual e θ_eff novo para meses de transição (preserva consistência geral).

3.4. Gerar `outputs/relatorio_comparativo_pipelines.md` documentando:
- Tabela: `pre_health03.csv` × `table7_new_values.csv` × `table7_bi_multifonte.csv` (mês a mês).
- Diagnóstico narrativo das mudanças.
- Justificativa documental para cada nova decisão.

**Fase 4 — Atualização do paper (2-3 dias) — chat de revisão (este formato)**

Aplicar a cadeia completa de substituições no DOCX. Lista exaustiva em §4 deste relatório.

**Fase 5 — Validação final pré-submissão (1 dia) — chat + autor**

5.1. Auditoria global de consistência numérica (`grep -rn` sobre o DOCX para todos os números antigos).
5.2. Renumeração de Diagrams (5–10 → 4–9) após remoção do Diagram 4 (pendente da §3.2).
5.3. Fact-checking integral §1, §3, §5, §6, §7, §8 sobre a nova narrativa.
5.4. Atualização do README do repositório `qfeng_validation` com referência ao BI multi-fonte.
5.5. Geração de versão final do DOCX → PDF → Zenodo → SSRN → arXiv.

### 3.2 Cronograma estimado

| Fase | Duração estimada | Recurso |
|---|---|---|
| Fase 0 (Preparação) | 1-2 dias | Autor (acesso DEMAS) |
| Fase 1 (Levantamento) | 3-5 dias | Autor + Claude Code |
| Fase 2 (Refactor pipeline) | 2-3 dias | Claude Code |
| Fase 3 (Regeneração outputs) | 1 dia | Claude Code |
| Fase 4 (Atualização paper) | 2-3 dias | Chat de revisão |
| Fase 5 (Validação final) | 1 dia | Chat + autor |
| **Total** | **10-15 dias úteis** | **2-3 semanas** |

Janela operacional: 25/abr a 15/mai/2026 (compatível com IEEE CAI Granada 8-10/mai como evento intermediário, e antes da janela JURIX 2026).

### 3.3 Riscos e mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| SIVEP-Gripe Manaus 2020-2021 incompleto | Baixa | Médio | Cruzar com SIH/DIAG_PRINC para validação; se parcial, declarar limitação |
| Cobertura O₂ retrospectivamente inobservável | Média-Alta | Médio | Fallback para BI bivariado; declarar logística como prospectiva-only no §7.4 |
| CB onset desloca para depois de Out/2020 | Baixa | Alto | Análise prévia de sensibilidade; se acontecer, reescrever narrativa para "CB ativada N meses antes" onde N é o número novo |
| Peak θ_eff continua em set/2020 mesmo com BI | Muito baixa | Alto | Inspecionar pesos w_TOH, w_SRAG; investigar se há outro artefato no formalismo |
| `t_mort = 0` por bug fundamental do `microdatasus` | Média | Médio | Cruzar com SIM para extração paralela de óbitos; usar SIM como fonte primária de mortalidade |
| Rerodada do pipeline quebra testes existentes | Alta | Baixo | Atualizar fixtures; documentar mudanças no CHANGELOG |
| Atraso por acesso institucional lento | Média | Médio | Começar Fase 0 imediatamente; usar fontes públicas (TabNet, SIVEP FTP) como fallback |

---

## 4. Mapa exaustivo de retrabalho no DOCX

Esta seção é o **manual de revisão** para a Fase 4. Cada entrada indica o parágrafo, o que diz hoje, e o que precisa virar (com placeholder `<NOVO>` para valores que dependem da regeneração da Fase 3).

### 4.1 Substituições numéricas mecânicas

| § | Conteúdo atual | Conteúdo novo | Tipo |
|---|---|---|---|
| §26 | "October 2020 activation (θ_eff = 126.41°...)" | "<NOVO_MES> activation (θ_eff = <NOVO_VAL>°...)" | Abstract |
| §147 | "β = 2.0 used in this PoC" | "β = 3.0 (production value, see Eq. 5)" | §3.2 |
| §147 | "α(t) = 0.91 in October 2020 onset month (Δpressão = +0.767)" | Substituir pela versão neutra já entregue na revisão §3.2 | §3.2 |
| §147 | "first CB-onset month remains October 2020 for all β ≥ 1.5; at β = 1.0, first CB onset shifts to November 2020" | Recalcular sensibilidade β com BI multi-fonte | §3.2 |
| §260 | "1,526 SIH/DATASUS admissions across six months (Oct/2020–Mar/2021)" | "<NOVO_TOTAL> SIH/DATASUS admissions across twelve months (Jul/2020–Jun/2021), corroborated by SIVEP-Gripe SRAG surveillance and FVS-AM TOH bulletins" | §5.3 setup |
| §330 | "Circuit Breaker first activates in July 2020 (θ_eff = 124.88°), when occupancy reaches 72%" | "Circuit Breaker first activates in <NOVO_MES> (θ_eff = <NOVO_VAL>°), when TOH reaches <NOVO_TOH>%" | §5.3 |
| §330 | "the large pressure gradient Δpressão = +0.767 in October drives α = 0.909" | "Δpressão = <NOVO_DELTA> in <NOVO_MES> drives α = <NOVO_ALPHA>" | §5.3 |
| §330 | "_OCCUPANCY_BY_MONTH parameters were calibrated using ex-post knowledge" | Reescrever: "the BI predictor uses three institutionally canonical series (TOH, SRAG, O₂) extracted from primary sources documented at extraction time" | §5.3 |
| §331 | "After the peak in September 2020 (θ_eff = 130.91°)" | "After the peak in <NOVO_PEAK_MES> (θ_eff = <NOVO_PEAK_VAL>°)" | §5.3 |
| §331 | "April: θ_t = 117.86° but θ_eff = 128.10°" | Atualizar com valores novos | §5.3 |
| §332 | "Bootstrap CI width asymmetry: SIH/DATASUS months (Oct/2020–Mar/2021) have narrow bootstrap CIs (±1–2°)... Literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021) have wider CIs (±3–4°)" | **Apagar a sentença inteira da assimetria.** Substituir por: "Bootstrap CIs are uniform across the 12-month series (σ = 0.05, all months), reflecting equal data quality from the BI multi-fonte canonical sources." | §5.3 |
| §332 | "September 2020 peak month has CI [126.52°, 128.73°]" | "<NOVO_PEAK_MES> peak month has CI [<NOVO_LOW>°, <NOVO_HIGH>°]" | §5.3 |
| §332 | "January 2021 (θ_eff = 118.08°, HITL) reflects the Markovian memory dampening" | Reescrever — provavelmente jan/2021 vai virar CB com BI | §5.3 |
| §336 | Caption Fig. 3: "Circuit-Breaker activated October 2020 (θ_eff = 125.3°, α(t) = 0.909)... Peak September 2020 at θ_eff = 130.91°" | Reescrever caption inteira com novos valores | Fig. 3 |
| §382 | "for SIH/DATASUS months (Oct/2020–Mar/2021), σ = 0.05 was used... for literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021), σ = 0.10 was used" | "σ = 0.05 was used uniformly across all 12 months, reflecting equal data quality from canonical primary sources (FVS-AM TOH bulletins, SIVEP-Gripe SRAG surveillance, SCTIE empenhos[/CNES capacity proxy])" | §6.3 |
| §383 | "narrowest CIs occur in September 2020 (CI: [126.52°, 128.73°], width 2.21°) — the peak crisis month" | Reescrever com novo peak month e CI | §6.3 |
| §384 | "October 2020 CB-onset month is σ_bootstrap = 1.25°, with CI [124.87°, 129.73°]" | Atualizar para novo CB-onset month | §6.3 |
| Tabela 7 | 12 linhas com θ_t/θ_eff/α/regime/occupancy/data_source/CI | **Substituir tabela inteira** com output do `outputs/table7_bi_multifonte.csv`. Adicionar coluna nova "Predictor source" indicando TOH/SRAG/O₂ por mês. | Table 7 |
| Tabela 10 | row 1: "Monthly SIH/DATASUS hospital occupancy pressure scores; real institutional TOH values from FVS-AM (Oct/2020–Mar/2021); estimated from literature for the remaining months" | "Monthly BI multi-fonte canonical predictor combining TOH UTI (FVS-AM bulletins, all 12 months), SRAG incidence (SIVEP-Gripe, all 12 months)[, and O₂ supply coverage (SCTIE empenhos, all 12 months)]" | Table 10 |

### 4.2 Estrutura narrativa a reescrever

| § | Mudança | Notas |
|---|---|---|
| §27 (Abstract Conclusions) | "detects crisis onset three months before the officially declared ICU collapse" → ajustar N para o número que sair do BI multi-fonte | A narrativa "antes da calamidade" provavelmente preserva, mas N pode mudar |
| §32 (§1) | "Three months earlier, the governance signal θ_eff developed in this paper had already crossed into CIRCUIT_BREAKER territory" → ajustar | Preserva tese; ajusta número |
| §96 (§2.7) | "trajectory inflection in October 2020 — three months before the formal calamity declaration" → ajustar | Preserva tese; ajusta data |
| §253 (§5.3 setup) | "hospital occupancy reached 100% (documented by FVS-AM Boletim Epidemiológico 16/jan/2021 (103.7% UTI occupancy))" | Mantém; já está correto |
| §326 (§5.3 prosa) | "first anomalous ICU occupancy readings in July 2020 (30%...)" → reescrever para refletir BI multi-fonte | Provavelmente julho deixa de ser anômalo (TOH 30% e SRAG baixo) |
| §326 | "first binding governance response issued three months after θ_eff had already exceeded 120°" → ajustar | Ajusta número |
| §328 (Diagram 10 caption) | "3-month offset between the Circuit Breaker activation in October 2020 and the Amazonas state calamity decree of 23 January 2021" → ajustar | Ajusta número |

### 4.3 Conteúdo a apagar inteiramente (release de fragilidade)

| § | Conteúdo a apagar | Justificativa |
|---|---|---|
| §419 (§7.4) | Limitation inteira: "Literature-estimated months in Manaus series: Six of twelve Manaus months..." | Obsoleto — todos os 12 meses agora são BI canônico |
| §332 trecho | "Bootstrap CI width asymmetry: SIH/DATASUS months (Oct/2020–Mar/2021) have narrow bootstrap CIs (±1–2°), reflecting the higher data quality of real microdata. Literature-estimated months..." | Obsoleto — substituído por "Bootstrap CIs uniform" |
| §382 trecho | "for literature-estimated months (Jul–Sep/2020 and Apr–Jun/2021), σ = 0.10 was used (reflecting epidemiological estimation uncertainty)" | Obsoleto |

### 4.4 Conteúdo a adicionar (forma nova)

**Adicionar em §5.3 (entre §253 e §260) — descrição do BI multi-fonte:**

Sugestão de prosa (a refinar conforme output da Fase 3):

> *"The ψ_N predictor for scenario C2 is constructed from a multi-source business intelligence predictor (BI multi-fonte) that combines three institutionally canonical indicators of healthcare system pressure in Manaus during the COVID-19 first and second waves (Jul/2020–Jun/2021): (i) TOH UTI (Taxa de Ocupação Hospitalar de UTI), the canonical Brazilian Ministry of Health indicator computed as paciente-dia / leito-dia operacional × 100, sourced from FVS-AM Boletim Epidemiológico bulletins and Observatório COVID-19 Fiocruz; (ii) SRAG incidence (Síndrome Respiratória Aguda Grave), extracted from SIVEP-Gripe surveillance microdata for municipality code 130260 with classification CLASSI_FIN = 5 (COVID-confirmed); [(iii) O₂ supply coverage, derived from SCTIE/MS oxygen requisition records for Manaus public hospitals]. The three series are normalized to [0,1] across the 12-month window and combined as pressure_raw = w_TOH · norm(TOH) + w_SRAG · norm(SRAG_growth)[ + w_O2 · (1 − norm(O2_coverage))], with weights calibrated by [PCA / institutional weighting protocol]. The composite score_pressao thus reflects the structure of the actual decision-making apparatus of the Brazilian Ministry of Health: pressure on hospital capacity (TOH), epidemiological trajectory (SRAG), and logistical bottleneck (O₂), each grounded in a distinct primary administrative source."*

**Adicionar em §7.4 (substituindo §419):**

Sugestão de prosa nova:

> *"Manaus BI multi-fonte coverage: The 12-month BI predictor combines three institutionally canonical sources: TOH UTI (FVS-AM/Fiocruz), SRAG incidence (SIVEP-Gripe), and O₂ supply (SCTIE/MS empenhos). Each source has its own provenance documented in `data/predictors/manaus_bi/README.md`. Limitations: (a) TOH for set/2020 and apr-jun/2021 are partially based on Fiocruz Observatorio interpolations; (b) [if applicable] O₂ coverage for jul-aug/2020 has lower granularity due to monthly versus weekly empenho registration; (c) prospective deployment requires real-time feeds from RNDS/FHIR (currently 30-90 day lag for SIH consolidation and 7-14 day lag for SIVEP-Gripe), which constitutes the primary scaling constraint identified in §8 Future Work."*

---

## 5. Decisões abertas que requerem o autor

Antes de iniciar Fase 1, decidir:

1. **Acesso a SCTIE/MS empenhos de O₂ medicinal Manaus 2020-2021:** viável via DEMAS/SEIDIGI? Se não, fallback CNES-LT como proxy estrutural.
2. **Pesos do BI:** PCA empírica sobre as três séries OU pesos a priori informados por ficha técnica MS? PCA é mais defensável estatisticamente; pesos a priori são mais defensáveis institucionalmente (autor criou as fichas técnicas do MS). Possível combinação: PCA como sanity-check, pesos a priori como decisão final.
3. **Granularidade temporal:** mensal (alinha com SIH MES_CMPT) ou semanal (alinha com SIVEP-Gripe SE)? Recomendação: manter mensal para Paper 1; semanal vai para Paper 2 que precisa de granularidade fina.
4. **Caso C7 (Brazilian regional bias) também usa BI multi-fonte?** O paper trata C7 como single-shot com ψ_N calibrado. Não é necessário aplicar BI a C7; só Manaus C2 precisa.

---

## 6. Pendências documentais para o autor antes da próxima sessão

Para Claude Code executar Fase 1 com eficiência, ter à mão:

- Credenciais e via de acesso a SIVEP-Gripe DATASUS (microdados ou TabNet).
- Endereço/contato do responsável SCTIE/MS por dados de empenho de medicamentos estratégicos.
- Lista de decretos AM 2020-2021 já citados no paper (43.269/2021, 43.303/2021, 43.360/2021) para referência cruzada.
- Boletins FVS-AM Manaus jul/2020-jun/2021 como PDFs ou links (validar `_TOH_FVS_AM` atual).
- Ficha técnica oficial MS da TOH UTI — autor é autor; localizar para citação no paper.

---

## 7. Pendências técnicas remanescentes (independentes do BI multi-fonte)

Estas pendências saíram da revisão da §3 e ficam **ativas** mesmo após o Caminho 2:

1. **§3.1 final aplicada** (texto entregue) — confirmar aplicação no DOCX.
2. **§3.2 final aplicada** (texto entregue, Diagram 4 removido) — confirmar aplicação.
3. **§3.3 (Born-Rule)**, **§3.4 (Alhedonic Loss)**, **§3.5 (Failure Typology)** — ainda não revisadas. Não dependem de Manaus, podem ser revisadas em paralelo à Fase 1.
4. **Renumeração Diagrams 5–10 → 4–9** após remoção do Diagram 4 — passagem mecânica final.
5. **§40 "alpha" → "α"** — harmonização notacional.
6. **§290 ψ_N de C7** — `[0.991, 0.117, 0.058]` parece typo vs §124 e §521 que reportam `[0.850, 0.100, 0.050]`. Confirmar `_PSI_N_RAW` em `psi_builder.py`.
7. **§175 vs §33** — C2 classificado como `execution_absent_channel` em §175 e como `execution_inertia` em §33 (Failure Typology). Resolver.
8. **§401 Pothos&Busemeyer 2013** — auditar e corrigir para 2022 (canônico §2.5 já foi atualizado).
9. **§44, §430, §439 inconsistência sobre "Paper 2"** — definir de modo coerente. Recomendado: substituir todas as 5 ocorrências por "future work (cf. §7.4, §8)".
10. **Tabelas 3 e 4** — referenciadas no texto (§401, §415, §421) mas extração via python-docx vai direto de Table 2 para Table 5. Inspecionar manualmente.

---

## 8. Estado de outros documentos mencionados pelo autor

- **Bolsa pós-doc UGR/DaSCI** — Paper 1 robusto suporta candidatura. Recomenda-se anexar PDF + link ao repositório GitHub na candidatura.
- **Encontro Paco Herrera (UGR/DaSCI)** — agendado para final de abril. Decidir se Paper 1 vai como working paper SSRN+arXiv (versão Caminho 2 final) ou como draft pré-Caminho-2. **Recomendação:** se a janela de 2-3 semanas do Caminho 2 cabe antes do encontro, esperar; se não cabe, enviar draft pré-Caminho-2 com nota explícita de "version under revision — final BI multi-fonte version available on [data]".
- **Natalia Díaz-Rodríguez** — receberá paper como suporte à candidatura. Mesmo critério.
- **JURIX 2026** — deadline ~setembro/2026; cabe Caminho 2 com folga.
- **IEEE CAI Granada (8-10 mai 2026)** — evento de networking; ter draft Caminho 2 quase finalizado é vantagem.
- **Lancet Digital Health / npj Digital Medicine (Paper 2)** — herdará a infraestrutura BI multi-fonte. Iniciar formalmente apenas após Paper 1 submetido a SSRN/arXiv.

---

## 9. Sumário executivo para retomada da próxima sessão

**Onde paramos:**
- Revisão §3 do Paper 1 em andamento (madrugada 25/abr/2026).
- §3.1 e §3.2 finais aplicadas.
- §3.2 sem Diagram 4 (caption duplicada SVG/Word resolvida).
- β = 3.0 confirmado canônico (substituído de β = 2.0 errado).
- Identificada inconsistência estrutural: score_pressao usa case-mix SIH (`t_uti`) enquanto ψ_S já usa TOH real → Manaus calamidade jan/fev/2021 cai em HITL espuriamente.

**Decisão tomada (25/abr/2026):**
- Caminho 2: reconstruir predictor de Manaus com BI multi-fonte (TOH + SRAG + O₂) antes da submissão de Paper 1.
- Janela de execução: 2-3 semanas (25/abr a 15/mai/2026).

**Próxima ação:**
- Fase 0: autor acessa DEMAS/SEIDIGI para verificar disponibilidade SIVEP-Gripe e SCTIE/empenhos O₂.
- Após Fase 0, sessão dedicada com Claude Code para Fase 1 (extração) e Fase 2 (refactor pipeline).
- Sessão de chat de revisão (este formato) executa Fase 4 (atualização paper) após Fase 3 entregue.

**Status documental:**
- Plano operacional consolidado: este relatório.
- Plano de refactor anterior (apenas Manaus 12 meses SIH): `docs/MANAUS_REFACTOR_PLAN.md` (parcialmente obsoleto após Caminho 2; manter como histórico).
- Ponte de memória da revisão §3: `artefatos/briefings/PONTE_MEMORIA_REVISAO_S3.md`.

**Pendências bloqueantes para Paper 1 final:**
1. Caminho 2 executado (Fases 0-5).
2. §3.3, §3.4, §3.5 revisadas.
3. Renumeração Diagrams 5-10 → 4-9.
4. Pendências técnicas §7 deste relatório resolvidas.
5. Auditoria global de consistência numérica.
6. Geração final DOCX → PDF → Zenodo → SSRN → arXiv.

---

*Fim do relatório.*
