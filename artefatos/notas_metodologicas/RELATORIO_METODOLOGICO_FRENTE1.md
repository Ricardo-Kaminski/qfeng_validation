# Relatório Metodológico — Frente 1: Pipeline Q-FENG Semanal Manaus 2020-2021

> ⚠️ **Atualizado em 27/abr/2026 — Opção 2 implementada.** Série truncada em SE 14/2020 (n=70). Ver `_addendum_OPCAO2_truncamento_serie.md`.

**Caminho 2 — Frente 1: Validação empírica multivariada com TOH primário Fase 2.1.5-bis**

**Branch:** `caminho2`  ·  **Workspace:** `C:\Workspace\academico\qfeng_validacao\`
**Data de fechamento:** 27 de abril de 2026  ·  **Status:** ✓ Aprovado para integração ao canônico (§5.3 reescrita)

**Destino editorial:** material-fonte para reescrita da §5.3 (*Manaus Theta-Efetivo Series*) do Paper 1 (`PAPER1_CANONICO.md`) e para o *Methodological Appendix* a ser anexado ao depósito Zenodo da Frente 1.

---

## 1. Objetivo metodológico

A Frente 1 do Caminho 2 substitui o pipeline mensal antigo (`manaus_sih_loader.py`, 12 competências jul/2020–jun/2021 com TOH interpolado dos boletins FVS-AM) pelo pipeline semanal canônico (`manaus_bi_loader.py`, 70 SEs ativas SE 14/2020–SE 30/2021 (Opção 2) com TOH primário derivado dos microdados DEMAS-VEPI). A operação é **execução pura** sobre matemática Q-FENG já programada em `src/qfeng/core/interference.py` (Eqs. 1, 2, 3, A5, A10) e camada simbólica em `src/qfeng/e5_symbolic/`. Nenhuma formalização nova é proposta; nenhuma alteração editorial dPASP→Clingo é requerida (canônico já 100% Clingo desde 27/abr/2026).

O resultado primário é a métrica **ΔSE_CB_estável** — diferença, em semanas epidemiológicas, entre o instante em que o framework Q-FENG entra em regime CIRCUIT_BREAKER sustentado (≥3 SEs consecutivas com θ_efetivo ≥ 120°) e o instante de reconhecimento formal da calamidade pública pelo aparato regulatório do estado do Amazonas (decreto AM 43.269/2021, 23/jan/2021, correspondente à SE 03/2021). O *gate criterion* metodológico, fixado *a priori* no briefing operacional de despacho, é ΔSE_CB_estável > 4 semanas.

## 2. Refundação Fase 2.1.5-bis: TOH primário em substituição à interpolação FVS-AM

A Fase 2.1.5-bis, fechada em 27/abr/2026, reconstruiu a Taxa de Ocupação Hospitalar (TOH) semanal Manaus 2020-2021 a partir de microdados oficiais primários do Ministério da Saúde, em substituição à série FVS-AM interpolada usada no canônico pré-bis. A motivação é dupla: (i) eliminar a dependência de boletins estaduais com periodicidade não uniforme e janelas de estimativa não documentadas; (ii) expor a **Fricção Ontológica** entre representação federal CNES (denominador estrito 319 leitos UTI em jan/2021) e operação real (812 ocupações UTI COVID em 21/jan/2021 segundo DEMAS-VEPI), que resulta em pico TOH de 211,5%.

### 2.1 Fontes primárias DEMAS-VEPI

A série semanal de TOH primário é derivada dos arquivos `esus-vepi.LeitoOcupacao_2020.csv` (119 MB) e `esus-vepi.LeitoOcupacao_2021.csv` (159 MB), disponibilizados pelo Departamento de Monitoramento, Avaliação e Disseminação de Informações Estratégicas em Saúde (DEMAS) do Ministério da Saúde via API DataSUS. O dataset bruto contém 12.929 registros diários de ocupação UTI COVID atribuídos aos 31 estabelecimentos CNES de Manaus durante 2021. O denominador (capacidade UTI cadastrada) é extraído dos arquivos CNES-LT mensais (`LTAM2001.dbc` a `LTAM2112.dbc`, 24 competências de 2020-2021), que registram leitos UTI por código CNES (códigos 74-77 para UTI adulto/pediátrica/neonatal/queimados; código 96 para Leito Suporte Ventilatório Pulmonar — LSVP).

A Tabela A.1 sumariza a transformação de microdado em série semanal:

| Estágio | Insumo | Operação | Saída |
|---|---|---|---|
| 2.1.5-bis-i | DEMAS-VEPI bruto (12.929 reg) | Filtragem por CNES Manaus + agregação diária por estabelecimento | `demas_vepi_manaus_uti_diario.parquet` (6.945 reg COVID 2021) |
| 2.1.5-bis-ii | CNES-LT 24 meses | Soma mensal de leitos UTI Manaus por código (74-77, 96) | `cnes_lt_manaus_uti_mensal.parquet` (552×8 colunas) |
| 2.1.5-bis-iii | Junção numerador-denominador | Razão diária ocupação/cadastrado, depois agregação por SE | `toh_semanal_manaus.parquet` (74×12 colunas) |

A unidade de TOH no parquet final é **percentual** (0–211,5), padronizada nesta passagem para alinhamento com o pipeline E5 a jusante; a operação interna em `_load_toh()` mantém fração para preservar precisão nas operações de razão.

### 2.2 Validação por triangulação cruzada com FVS-AM

A consistência entre a série primária DEMAS-VEPI e a literatura FVS-AM foi auditada formalmente. O coeficiente de Spearman entre as duas séries na janela 29/jun/2020 a 31/mai/2021 é ρ = 0,865 (n = 49 semanas comparáveis), com erro absoluto médio (MAE) de 54,7 pontos percentuais. A divergência sistemática é explicada pelo fato de que o denominador FVS-AM (612 leitos em jan/2021) inclui leitos emergenciais reconhecidos pelo regulador estadual mas não cadastrados no CNES federal — exatamente o gap entre Camadas 1 e 2 da Fricção Ontológica documentadas na seção 4. O artefato `outputs/cross_validacao_fvs_demas_fase215bis.csv` contém o cruzamento ponto a ponto.

A correlação Spearman entre TOH semanal primário e SRAG-COVID semanal SIVEP-Gripe é ρ = 0,462 em lag 0 e ρ = 0,624 em lag +3 (TOH lidera SRAG por três semanas), consistente com a literatura epidemiológica que identifica a hospitalização UTI como sinal antecipatório da hospitalização SRAG geral.

### 2.3 Sondagem de leitos LSVP (código CNES 96): a Camada 4 de Fricção Ontológica

A Portaria SAES/MS nº 510 de 09/jun/2020 criou a categoria CNES "Leito Suporte Ventilatório Pulmonar" (cód. 96), explicitamente para nomear os leitos intermediários ad hoc que estavam sendo improvisados nos primeiros meses da pandemia. A sondagem dos arquivos CNES-LT via biblioteca R `read.dbc` (R 4.5.3) revela que **0 leitos LSVP foram cadastrados em Manaus em 23 das 24 competências de 2020-2021**; o único registro positivo (dezembro/2020, 2 leitos em 1 estabelecimento) é estatisticamente irrelevante. A categoria normativa existe e foi auditada operacionalmente pelo regulador federal, mas não foi adotada como prática institucional pelos gestores hospitalares amazonenses. Este achado, registrado como **Camada 4 (Institucional) da Fricção Ontológica**, demonstra empiricamente que a criação ex post de categoria categorial é insuficiente para forçar adoção operacional — ponto que tem implicações diretas para o argumento metodológico da §5.3 reescrita.

## 3. Migração técnica do runner E5

### 3.1 Refactor do consumer

A operação F1.1 consistiu em três alterações cirúrgicas no orquestrador E5 (`src/qfeng/e5_symbolic/runner.py`), preservando integralmente a lógica matemática de Q-FENG:

(i) substituição do import `from .manaus_sih_loader import load_manaus_real_series` por `from .manaus_bi_loader import load_manaus_bi_series, load_sih_with_fixed_tmort`;

(ii) ajuste do schema de saída em `run_theta_efetivo_manaus()` para refletir granularidade semanal — adição dos campos `year`, `week_se`, `month_sih`, `srag_n_covid`, `srag_is_stub`, `toh_is_estimated`, `data_source`; o campo `competencia` mantém-se mas passa a codificar `YYYYWW` (e.g., `202103` agora significa SE 03 de 2021, não março/2021);

(iii) unificação do parâmetro σ do bootstrap em 0,05 para todas as 70 SEs ativas (Opção 2), em substituição ao critério anterior `σ=0.05 if data_source == "sih_datasus" else 0.10`. A justificativa é que **todas as 70 SEs ativas operam sobre fontes primárias** (TOH DEMAS-VEPI, SRAG SIVEP-Gripe, SIH/DATASUS), eliminando a categoria "literature months" que justificava o σ majorado no pipeline antigo. A mudança é documentada como contrato Zenodo v2026.04.

O loader antigo (`manaus_sih_loader.py`) é preservado como código histórico, sem modificação. O backup integral dos seis parquets pré-Frente 1 está armazenado em `outputs/e5_results/_archive_pre_frente1/` com README descritivo.

### 3.2 Re-execução E5 e validação imediata

A operação F1.2 re-executou o pipeline completo (`conda run -n qfeng python -m qfeng.e5_symbolic.runner`) e gerou a nova série semanal:

- `theta_efetivo_manaus.parquet`: 70 linhas ativas (Opção 2; anteriormente 12), schema enriquecido com 23 colunas;
- `manaus_bootstrap_ci.parquet`: 70 linhas (Opção 2) com intervalos de confiança bootstrap 95%, σ unificado;
- `validation_results.parquet`, `psi_sensitivity.parquet`, `threshold_robustness.parquet`, `llm_comparison.parquet`: regenerados.

A validação imediata confirma TOH pico em SE 03/2021 = 212% (concordante com a expectativa do briefing de 211%), θ_efetivo mínimo de 100,59° e máximo de 133,07°, e θ_efetivo no momento de colapso público (SE 03/2021) de 123,27° — interior à zona CIRCUIT_BREAKER.

## 4. Arquitetura analítica da Frente 1: ΔSE de antecipação

A operação F1.3 implementa o script analítico `scripts/analise_frente1.py`, que opera sobre `theta_efetivo_manaus.parquet` para produzir três artefatos: (i) `outputs/frente1_delta_se_antecipacao.json` com métricas e tabelas de sensibilidade; (ii) `outputs/frente1_analise_descritiva.md` com prosa acadêmica de 153 linhas integrando 4 camadas e ΔSE; (iii) duas figuras em `outputs/figures/`: série θ_t × SE com marcações de regime, e heatmap de sensibilidade.

### 4.1 Definição operacional da SE de colapso público

Adoto como **SE de colapso público canônica** a SE 03/2021 (semana de 18 a 24 de janeiro de 2021), correspondente à publicação do decreto AM 43.269/2021 (15/jan/2021, vigência a partir de 23/jan/2021), que declara estado de calamidade pública no Amazonas em razão do esgotamento de oxigênio hospitalar e da necessidade de transferências interestaduais emergenciais. A escolha desta SE como referência canônica é fundamentada em três fatores: (i) é o evento institucional formal que ativa o aparato federal de resposta emergencial; (ii) coincide com o pico de cobertura midiática internacional do colapso (Reuters, BBC, NYT, 14-23/jan/2021); (iii) é a janela temporal usada nas notas técnicas do MS e SES-AM como referência de severidade.

### 4.2 Métricas computadas

Para cada uma de três thresholds operacionais distintas, a métrica ΔSE é computada como:

ΔSE_X = SE_colapso_canônica − SE_primeiro_alerta_X

onde SE_primeiro_alerta_X é definida conforme a Tabela 4.1.

**Tabela 4.1 — Definição operacional dos três limiares de ΔSE.**

| Limiar | Definição operacional | Critério lógico |
|---|---|---|
| ΔSE_HITL | Primeira SE com θ_efetivo > 60° | Marca o momento em que o regime sai de STAC |
| ΔSE_CB | Primeira SE com θ_efetivo > 120° | Marca a primeira ativação de CB (sem requisito de persistência) |
| ΔSE_CB_estável | Primeira SE inicial de uma run de ≥3 SEs consecutivas com θ_efetivo > 120° | Marca o início de regime CB sustentado, filtrando ruído transiente |

A métrica ΔSE_CB_estável é a métrica primária de antecipação: o requisito de 3 SEs consecutivas no mesmo regime filtra falsos positivos transitórios (oscilações de uma única semana ao redor do threshold) e captura o início de uma fase de pressão sustentada, que é o que importa do ponto de vista de governança operacional. O limiar de 3 SEs é escolhido como o menor inteiro k > 1 que (a) admite robustez face a um outlier semanal isolado e (b) é compatível com a janela de 28 dias usada como ciclo mínimo de reposta institucional em planos de contingência sanitária do Brasil (resoluções CONASS/CONASEMS 2020).

### 4.3 Análise de sensibilidade aos thresholds

A robustez do gate criterion é avaliada sobre uma grade 5×5 de thresholds:

- threshold CB ∈ {110°, 115°, 120°, 125°, 130°};
- threshold HITL ∈ {45°, 52,5°, 60°, 67,5°, 75°}.

Para cada uma das 25 combinações, recomputo ΔSE_CB e ΔSE_CB_estável, e classifico como "gate aprovado" se ΔSE_CB_estável > 4 SEs. A heatmap resultante (`outputs/figures/frente1_sensibilidade_thresholds.png`) e a tabela linear no `frente1_delta_se_antecipacao.json` documentam, com transparência editorialmente exigível, a faixa de robustez do resultado principal.

### 4.4 Decomposição empírica da Fricção Ontológica em quatro camadas

A nota metodológica `artefatos/notas_metodologicas/NOTA_TOH_FRICCAO_ONTOLOGICA_4CAMADAS.md` (15.465 bytes, 117 linhas) decompõe o gap entre denominador CNES (319 leitos UTI Manaus jan/2021) e denominador FVS-AM (612 leitos contabilizados pelo regulador estadual) em quatro camadas auditáveis:

**Tabela 4.2 — Decomposição da Fricção Ontológica Manaus jan/2021.**

| Camada | Tipo | Mecanismo | Magnitude estimada |
|---|---|---|---|
| 1 | Operacional | Leitos de enfermaria operando como UTI improvisada (códigos CNES 30-46 em vez de 74-77) | ~85 leitos |
| 2 | Administrativa | Leitos UTI emergenciais habilitados pelo MS em jan/2021 com cadastro CNES defasado em 30-60 dias | ~208 leitos (178 MS + 30 Hosp Beneficente Português) |
| 3 | Categorial | Portaria SAES/MS nº 510/2020 cria categoria LSVP (cód. 96) para nomear leitos intermediários | 0 leitos (categoria criada normativamente) |
| 4 | Institucional | LSVP não adotada operacionalmente em Manaus: 0 leitos em 23/24 meses CNES-LT | 0 leitos (categoria existente mas não operacionalizada) |

A soma reconstituída das Camadas 1 e 2 (293 leitos acima do CNES) reconcilia, com erro abaixo de 5%, o denominador CNES (319) com o denominador FVS-AM (612). As Camadas 3 e 4 são qualitativamente distintas e mais relevantes para o argumento canônico do paper: demonstram empiricamente que a criação de categoria normativa, mesmo quando explicitamente desenhada para nomear o fenômeno, é insuficiente para forçar adoção operacional — ponto que sustenta a tese da Fricção Ontológica como invariante institucional resistente à intervenção regulatória pontual.

## 5. Schema final do parquet de saída

A Tabela 5.1 documenta o schema completo de `outputs/e5_results/theta_efetivo_manaus.parquet`, que é o artefato canônico de entrada para a reescrita da §5.3 do paper.

**Tabela 5.1 — Schema theta_efetivo_manaus.parquet (70 SEs × 23 colunas, Opção 2).**

| Coluna | Tipo | Descrição |
|---|---|---|
| competencia | int | Codificação YYYYWW (e.g. 202103 = SE 03/2021) |
| year, week_se | int | Ano e número da semana epidemiológica |
| month_sih | int | Mês SIH/DATASUS (mapeado por mês de início da SE) |
| theta_t | float | Ângulo θ instantâneo (Eq. A5) |
| theta_efetivo | float | Ângulo θ Markoviano com memória β=3.0 (Eq. A10) |
| alpha_t | float | Peso adaptativo sigmoidal do termo Markoviano |
| interference_regime | str | STAC / HITL / CIRCUIT_BREAKER |
| internacoes, obitos | int | Internações e óbitos SIH/DATASUS no mês de início da SE |
| taxa_mortalidade, taxa_uti, taxa_respiratorio | float | Taxas derivadas SIH |
| score_pressao | float | Score composto de pressão hospitalar multidimensional |
| hospital_occupancy_pct | float | TOH primário DEMAS-VEPI (0–212%) |
| toh_is_estimated | bool | Indicador de SEs com TOH ausente/zero (SE 10-13/2020 — ver §6) |
| srag_n_covid | int | Casos SRAG-COVID semanais SIVEP-Gripe |
| srag_is_stub | bool | Indicador de imputação SRAG (False = real para todas as SEs após validação) |
| delta_pressao, delta_theta | float | Variações SE-a-SE (não mês-a-mês) |
| n_sovereign_ativados | int | Predicados Clingo sovereign ativos no estado |
| data_source | str | Lineage tag = "sih_datasus+toh_demas_vepi_semanal+srag_sivep" |
| evento_critico | str | Marcador qualitativo de eventos canônicos da janela |

Para o bootstrap 95%, o schema complementar de `manaus_bootstrap_ci.parquet` (70 linhas, Opção 2) inclui `theta_ci_lower_95`, `theta_ci_upper_95`, `theta_bootstrap_std`, `score_sigma`.

## 6. Limitação metodológica documentada: TOH zero nas SEs 10-13/2020

A auditoria forense de fechamento da Frente 1 revelou que as quatro primeiras semanas epidemiológicas da série (SE 10/2020 a SE 13/2020) registram `hospital_occupancy_pct = 0`. A causa é a consolidação tardia do registro DEMAS-VEPI: o sistema só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), o que é cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais.

A consequência para a métrica ΔSE_HITL é que o valor reportado (46 SEs) é parcialmente artefatual, já que o regime HITL está formalmente ativado nas SEs 10-13/2020 com θ_efetivo = 115,27° apesar de TOH = 0. O θ_t nestas semanas é dominado pela ψ_S (predicados Clingo derivados da pressão composta SRAG + SIH) e pela inicialização do cache Markoviano, não pela dimensão TOH.

A decisão editorial implementada (Opção 2, 27/abr/2026) é **truncar a série em SE 14/2020 (n=70 SEs)** — os 4 zeros iniciais são excluídos da série ativa. ΔSE_CB e ΔSE_CB_estável (resultados primários) não são afetados por esta limitação, uma vez que a primeira ativação CB ocorre em SE 37/2020, instante em que o pipeline opera com TOH primário consolidado. O adendo metodológico `artefatos/notas_metodologicas/_addendum_OPCAO2_truncamento_serie.md` documenta as três opções de redação consideradas e a justificativa da opção selecionada.

## 7. Reprodutibilidade e arquitetura de dados Zenodo

Todos os artefatos da Frente 1 estão sob versionamento Git na branch `caminho2`, com manifesto SHA256 no `data/predictors/manaus_bi/raw/source_manifest.json` cobrindo as 28 fontes brutas (microdados oficiais MS). A árvore de execução é reprodutível via:

```bash
conda activate qfeng
cd C:\Workspace\academico\qfeng_validacao
python -m qfeng.e5_symbolic.runner   # F1.2: regenera parquets E5
python scripts/analise_frente1.py    # F1.3: regenera analise descritiva
```

O contrato Zenodo v2026.04 documenta as decisões metodológicas críticas: σ=0,05 uniforme; denominador CNES estrito (em vez de FVS-AM corrigido) para preservar visibilidade da Fricção Ontológica; exclusão de SEs 10-13/2020 da métrica ΔSE_HITL; e granularidade semanal SE-a-SE (não mês-a-mês) para `delta_pressao` e `delta_theta`.

## 8. Cadeia de commits Frente 1

A operação completa está distribuída em três commits sequenciais na branch `caminho2`:

- `edd15b1` — `frente1: migrate runner to weekly bi_loader (Fase 2.1.5-bis canonical)`
- `9be1dd0` — `frente1: regenerate E5 outputs with weekly TOH primário`
- `1f5c6dd` — `frente1: analise descritiva e metrica delta-SE de antecipacao`
- `5f39560` — `frente1: relatorio final consolidado` (referência: `outputs/RELATORIO_FRENTE1_FINAL.md`)

## 9. Status para integração ao canônico

Esta Frente 1 produz o material-fonte para reescrita integral da §5.3 do `PAPER1_CANONICO.md` (atualmente 12 competências mensais, a ser substituída por 70 SEs semanais (Opção 2) com ΔSE_CB_estável = 19 SEs como resultado principal). O documento companion `RESULTADOS_FRENTE1_PARA_CANONICO.md` (mesmo diretório, versão paralela a este) contém a redação acadêmica densa pronta para inserção, com referências cruzadas para §3 (matemática), §6 (análise estatística) e §7.4 (limitações). A integração ao canônico está condicionada à conclusão da Frente 2 (Adversarial CLT), conforme orientação editorial registrada nesta sessão.

---

*Fim do relatório metodológico Frente 1.*
*Q-FENG Caminho 2 · Branch `caminho2` · Workspace `C:\Workspace\academico\qfeng_validacao\`*
*Autor: Ricardo da Silva Kaminski (ORCID: 0000-0002-8882-9248)*
