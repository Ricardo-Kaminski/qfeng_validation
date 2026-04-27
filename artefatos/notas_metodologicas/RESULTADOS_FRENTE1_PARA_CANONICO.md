# Resultados Frente 1 — Q-FENG Semanal Manaus 2020-2021

> ⚠️ **Atualizado em 27/abr/2026 — Opção 2 implementada.** Série truncada em SE 14/2020 (n=70). Ver `_addendum_OPCAO2_truncamento_serie.md`.

**Material-fonte para reescrita integral da §5.3 do `PAPER1_CANONICO.md` (Manaus Theta-Efetivo Series).**

**Caminho 2 — Frente 1 · Branch:** `caminho2`  ·  **Data de fechamento:** 27 de abril de 2026
**Status:** ✓ Aprovado para integração ao canônico após conclusão da Frente 2 (Adversarial CLT)
**Documento companion metodológico:** `RELATORIO_METODOLOGICO_FRENTE1.md` (mesmo diretório)

---

## A. Sumário executivo dos resultados

A aplicação do framework Q-FENG à série semanal de 70 semanas epidemiológicas (SEs) de Manaus/AM (SE 14/2020 a SE 30/2021, Opção 2), construída a partir de microdados oficiais primários do Ministério da Saúde (DEMAS-VEPI, SIH/DATASUS, SIVEP-Gripe) na refundação Fase 2.1.5-bis, detectou regime de alarme sustentado (CIRCUIT_BREAKER) com **19 semanas de antecipação** em relação ao reconhecimento formal de calamidade pública pelo aparato regulatório do estado do Amazonas (decreto AM 43.269/2021, SE 03/2021, 23 de janeiro de 2021).

O *gate criterion* metodológico, fixado a priori em ΔSE_CB_estável > 4 semanas, é aprovado com folga 4,75× superior ao limiar mínimo (resultado: 19 SEs). A robustez aos thresholds operacionais sustenta o resultado em 60% das 25 configurações de sensibilidade testadas, com falha apenas para CB threshold ≥ 125° — faixa que está acima da calibração canônica de 120° fundamentada na geometria de interferência construtiva dominante.

A análise revela três achados editorialmente relevantes para a reescrita do canônico: (i) a Fricção Ontológica entre denominador CNES (319 leitos UTI cadastrados em jan/2021) e operação real (DEMAS-VEPI registra 815 ocupações UTI COVID em 21/jan/2021) produz pico de TOH em 211,5%, que não é anomalia estatística mas medição direta da Fricção; (ii) a categoria CNES "Leito Suporte Ventilatório Pulmonar" (cód. 96), criada normativamente pela Portaria SAES/MS nº 510/2020 com finalidade explícita de nomear leitos UTI improvisados, não foi adotada operacionalmente em Manaus em 23 de 24 competências de 2020-2021, sustentando a tese da Fricção Ontológica como invariante institucional resistente à intervenção regulatória pontual; (iii) a correlação Spearman entre score de pressão composto e θ_efetivo é ρ = 0,906, contrastando com a correlação direta TOH × θ_efetivo de apenas ρ = 0,374, confirmando que o ângulo Q-FENG opera no espaço de parâmetros multidimensional e não é redutível a um único indicador operacional.

## B. Distribuição de regimes nas 70 SEs (Opção 2)

A Tabela B.1 sumariza a distribuição dos três regimes Q-FENG ao longo da série completa.

**Tabela B.1 — Distribuição de regimes Q-FENG, série semanal Manaus 2020-2021.**

| Regime | Threshold (calibração canônica) | N SEs | % |
|---|---|---|---|
| STAC | θ_efetivo < 60° | 0 | 0,0 |
| HITL | 60° ≤ θ_efetivo < 120° | 48 | 64,9 |
| CIRCUIT_BREAKER | θ_efetivo ≥ 120° | 26 | 35,1 |

A ausência completa de SEs em regime STAC durante toda a janela 2020-2021 confirma que o período representa um episódio de pressão sistêmica contínua, sem retorno do sistema hospitalar amazonense a operação normal. Esta é uma propriedade emergente do framework Q-FENG, não uma calibração dos thresholds: as 70 SEs ativas operam com θ_efetivo mínimo acima de 100° (início SE 14/2020, Opção 2) e máximo de 133,07° (SE 07-08/2021, pico da segunda onda CB).

## C. Resultado primário: ΔSE de antecipação

A Tabela C.1 reporta as três métricas operacionais de antecipação computadas conforme a calibração canônica de thresholds (CB = 120°, HITL = 60°, persistência mínima = 3 SEs consecutivas).

**Tabela C.1 — Métricas de antecipação ΔSE, calibração canônica.**

| Métrica | Valor (SEs) | Competência de origem | Interpretação |
|---|---|---|---|
| ΔSE_HITL | 42 | SE 14/2020 (início série, Opção 2) | Primeira SE com θ_efetivo > 60° |
| ΔSE_CB | 19 | SE 37/2020 (set/2020) | Primeira SE com θ_efetivo > 120° |
| **ΔSE_CB_estável** | **19** | SE 37/2020 (set/2020) | Início de run ≥3 SEs consecutivas em CB |
| Gate criterion (briefing) | > 4 | — | ✓ Aprovado |
| SE de colapso público canônica | — | SE 03/2021 | Decreto AM 43.269/2021 |

\* *Ver §G — limitação metodológica: ΔSE_HITL é parcialmente artefatual devido a TOH zero nas SEs 10-13/2020. Métrica ΔSE_HITL ajustada (a partir de SE 14/2020) = 42 SEs, também > 4. Resultado primário ΔSE_CB_estável não é afetado pela limitação.*

A coincidência numérica entre ΔSE_CB e ΔSE_CB_estável (ambos 19 SEs) decorre do fato de que a primeira ativação CB (SE 37/2020) inicia imediatamente uma run de oito SEs consecutivas em regime CB, ultrapassando com folga o requisito de persistência mínima de 3 SEs e tornando as duas métricas numericamente idênticas neste caso.

A interpretação operacional de ΔSE_CB_estável = 19 SEs é direta: o framework Q-FENG, operando exclusivamente sobre dados disponíveis em tempo real ao gestor público (microdados DEMAS-VEPI sincronizados com defasagem de 24-48 horas, SIVEP-Gripe semanal, CNES-LT mensal), entrou em regime de alarme sustentado quase cinco meses antes do colapso de oxigênio que mobilizou intervenção federal. Em termos de tempo institucional, 19 semanas correspondem a janela operacional para licitação federal de insumos críticos, redirecionamento orçamentário emergencial via TC nº 27/2021 do TCU, mobilização da Aeronáutica para transporte de pacientes, ou ativação antecipada de leitos solidários inter-estaduais.

## D. Estrutura de ondas CIRCUIT_BREAKER

A Tabela D.1 documenta a distribuição temporal das duas ondas de regime CB identificadas na série.

**Tabela D.1 — Ondas Circuit Breaker na série semanal Manaus 2020-2021.**

| Onda | Período (competência) | Período (calendário) | Duração | Contexto epidemiológico |
|---|---|---|---|---|
| 1 | SE 37/2020 a SE 44/2020 | set–out/2020 | 8 SEs | Segunda onda Manaus, esgotamento progressivo, pré-colapso |
| 2 | SE 01/2021 a SE 18/2021 | jan–mai/2021 | 18 SEs | Colapso catastrófico (jan/2021) e recuperação lenta com TOH > 100% sustentado |

A onda 1 antecipa o colapso público da onda 2 com intervalo de 19 semanas. A onda 2 cobre o período de colapso agudo (SEs 01-04/2021, com TOH oscilando entre 191% e 212%) e a fase de recuperação institucional lenta, durante a qual o TOH permanece acima de 100% por múltiplas semanas consecutivas. Esta estrutura em duas ondas, com plateau de recuperação parcial entre elas, é coerente com a dinâmica de colapso sanitário documentada clinicamente para Manaus na literatura epidemiológica e nas notas técnicas SES-AM 2021. A granularidade semanal do pipeline expõe esta estrutura de forma irreproduzível pelo pipeline mensal anterior, que mostrava todas as competências jul/2020 a jun/2021 indistintamente em CB.

## E. Perfil estatístico de θ_efetivo

A Tabela E.1 sumariza as estatísticas descritivas de θ_efetivo na série completa.

**Tabela E.1 — Estatísticas descritivas, θ_efetivo.**

| Estatística | Valor (graus) |
|---|---|
| Mínimo | ~100° (SE 14-17/2020, Opção 2) |
| Máximo | 133,07 (SE 07-08/2021) |
| Mediana | ~114 (regime HITL) |
| θ_efetivo na SE de colapso (SE 03/2021) | 123,27 (regime CB) |

O θ_efetivo permanece acima do threshold HITL (60°) em todas as 70 SEs da série ativa, confirmando ausência de operação STAC durante a janela de observação. O pico em SEs 07-08/2021 (~133°) coincide com a fase mais aguda da segunda onda CB, durante a qual o TOH permaneceu acima de 160% por múltiplas semanas consecutivas e a mortalidade hospitalar SIH atingiu o pico mensal de 4,87% em fevereiro/2021.

## F. Correlações descritivas: a estrutura multidimensional do θ_efetivo

A Tabela F.1 reporta os coeficientes de correlação de Spearman entre θ_efetivo e os indicadores operacionais primários da série, com p-valores associados.

**Tabela F.1 — Correlações Spearman θ_efetivo vs. indicadores operacionais.**

| Par | ρ Spearman | p-valor | Interpretação |
|---|---|---|---|
| score_pressao × θ_efetivo | **0,906** | < 0,001 | Dominância do score composto multidimensional |
| Óbitos × θ_efetivo | 0,399 | < 0,001 | Sinal de mortalidade capturado parcialmente |
| TOH × θ_efetivo | 0,374 | 0,001 | TOH contribui via score, não diretamente |

A correlação muito alta entre score_pressao e θ_efetivo (ρ = 0,906) confirma a propriedade arquitetônica central do framework Q-FENG: o ângulo θ não é proxy de um único indicador operacional, mas captura intensidade composta de pressão hospitalar multidimensional, integrando TOH, mortalidade, ocupação respiratória, SRAG semanal e o próprio passado da série via memória Markoviana β = 3,0 (Eq. A10). A correlação direta moderada entre TOH e θ_efetivo (ρ = 0,374) é a contraparte estatística desta propriedade: nenhum dos componentes individuais explica isoladamente o ângulo. Esta é a diferença estrutural entre o Q-FENG e qualquer dashboard threshold-based operando sobre TOH ou qualquer outro indicador isolado — diferença que é elaborada na seção *§Q-FENG vs. monitoramento descritivo* a ser inserida no canônico (ver `INSERCOES_NOVAS_SECOES_CANONICO.md`).

## G. Limitação metodológica: TOH zero nas SEs 10-13/2020

A auditoria forense de fechamento da Frente 1 identifica que as quatro primeiras SEs da série (SE 10/2020 a SE 13/2020) registram `hospital_occupancy_pct = 0`. A causa é a consolidação tardia do registro DEMAS-VEPI: o sistema só passa a registrar consistentemente ocupação UTI COVID em Manaus a partir de SE 14/2020 (TOH = 48%), o que é cronologicamente coerente com o início efetivo da pandemia em Manaus (primeiro caso 13/03/2020) e com o tempo institucional de padronização do registro pelos hospitais (média de 4-6 semanas de estabilização para campos novos em sistemas DEMAS).

A consequência editorial é que ΔSE_HITL = 42 SEs (série canônica Opção 2, SE 14/2020–SE 30/2021), uma vez que o regime HITL está formalmente ativado nestas quatro SEs com θ_efetivo = 115,27° apesar de TOH = 0. Nestas semanas, o θ_t é dominado pela dimensão simbólica ψ_S (predicados Clingo de soberania institucional) e pela inicialização do cache Markoviano, não pela dimensão operacional TOH. A decisão editorial adotada para a redação canônica é **Opção 2: truncar série em SE 14/2020 (n=70 SEs ativas)** (ΔSE_HITL = 42 SEs, ainda > 4 e portanto compatível com gate criterion). ΔSE_CB e ΔSE_CB_estável (resultados primários) não são afetados, uma vez que a primeira ativação CB ocorre em SE 37/2020, instante em que o pipeline opera com TOH primário consolidado.

A documentação detalhada desta opção e das alternativas consideradas (truncar a série em SE 14/2020; manter n = 74 com nota metodológica completa) está no adendo `artefatos/notas_metodologicas/_addendum_OPCAO2_truncamento_serie.md`.

## H. Robustez sob sensibilidade aos thresholds

A Tabela H.1 sumariza a análise de sensibilidade do gate criterion sobre uma grade 5 × 5 de thresholds (CB ∈ {110°, 115°, 120°, 125°, 130°}; HITL ∈ {45°, 52,5°, 60°, 67,5°, 75°}).

**Tabela H.1 — Sensibilidade aos thresholds: aprovação do gate criterion (ΔSE_CB_estável > 4 SEs).**

| CB threshold | Configurações testadas | Configurações aprovadas | Faixa de ΔSE_CB_estável |
|---|---|---|---|
| 110° | 5 | 5 (100%) | 42 SEs (todas) |
| 115° | 5 | 5 (100%) | 42 SEs (todas) |
| 120° (canônico) | 5 | 5 (100%) | 19 SEs (todas) |
| 125° | 5 | 0 (0%) | n/d (CB transiente) |
| 130° | 5 | 0 (0%) | n/d (5 SEs apenas) |
| **Total** | **25** | **15 (60%)** | — |

O gate criterion é aprovado em 60% das configurações testadas. A faixa robusta é CB ∈ [110°, 120°], com transição para falha em CB = 125°. A explicação geométrica é direta: a SE de colapso público canônica (SE 03/2021) tem θ_efetivo = 123,27°, abaixo do threshold de 125° — quando o critério exige que a primeira CB anteceda o colapso, qualquer threshold acima de 123,27° produz inversão lógica. A escolha canônica de 120° é fundamentada pela teoria de interferência construtiva dominante (Eq. A5 do canônico) e não é retro-calibrada contra o resultado: a faixa segura inclui um buffer de aproximadamente 3° em relação ao θ_efetivo do colapso, suficiente para absorver oscilação bootstrap sem comprometer a coerência matemática do framework.

A Figura `outputs/figures/frente1_sensibilidade_thresholds.png` apresenta a heatmap completa da grade 5 × 5, com codificação binária aprovação/reprovação do gate.

## I. Decomposição empírica da Fricção Ontológica em quatro camadas

O TOH de 211,5% no pico do colapso (SE 03/2021), com numerador DEMAS-VEPI = 815 ocupações UTI COVID em 21/jan/2021 e denominador CNES-LT = 319 leitos UTI cadastrados, **não é anomalia estatística**. É a métrica empírica da Fricção Ontológica entre representação regulatória federal e operação real, decomposta em quatro camadas auditáveis cuja soma reconstitui, com erro inferior a 5%, o gap entre denominador CNES (319) e denominador FVS-AM (612).

**Tabela I.1 — Decomposição da Fricção Ontológica em quatro camadas, Manaus jan/2021.**

| Camada | Tipo | Descrição operacional | Magnitude estimada |
|---|---|---|---|
| 1 | Operacional | Leitos de enfermaria (códigos CNES 30-46) operando como UTI improvisada | ~85 leitos |
| 2 | Administrativa | Leitos UTI emergenciais habilitados pelo MS em jan/2021 com cadastro CNES defasado em 30-60 dias (178 do MS + 30 do Hosp Beneficente Português) | ~208 leitos |
| 3 | Categorial | Portaria SAES/MS nº 510/2020 cria categoria LSVP (cód. 96) para nomear leitos intermediários ad hoc | 0 leitos (categoria criada) |
| 4 | Institucional | LSVP não adotada operacionalmente em Manaus: 0 leitos em 23/24 meses CNES-LT | 0 leitos (categoria existe mas é inerte) |

As Camadas 1 e 2 são **operacionalmente reconciliáveis**: somam aproximadamente 293 leitos acima do CNES e explicam aritmeticamente a diferença entre denominador CNES (319) e denominador FVS-AM (612). As Camadas 3 e 4 são **qualitativamente distintas e mais relevantes editorialmente**: documentam que a criação ex post de categoria normativa, mesmo quando explicitamente desenhada para nomear o fenômeno, é insuficiente para forçar adoção operacional. A Camada 4 é o achado empírico inédito da Fase 2.1.5-bis: a sondagem dos 24 arquivos CNES-LT mensais Manaus 2020-2021 via biblioteca R `read.dbc` confirma que **0 leitos LSVP foram cadastrados em 23 das 24 competências**, com único registro positivo (dezembro/2020, 2 leitos em 1 estabelecimento) estatisticamente irrelevante.

A interpretação editorial deste achado é direta: o regulador federal **criou a categoria nominal para registrar o fenômeno**, mas o sistema operacional Manaus **não internalizou a categoria como prática institucional**. Esta é uma demonstração empírica de Fricção Ontológica como **invariante resistente à intervenção regulatória pontual** — propriedade que sustenta a tese de governança Q-FENG: medir tensão sem prescrever reforma normativa, rotacionar o espaço de parâmetros (Vetor de Correção Ontológica, Eq. A4 do canônico) sem tocar no corpus normativo. A Camada 4 é a contraparte empírica da formalização teórica da §3 do canônico.

A correlação operacional entre a Fricção Ontológica e o regime CB também é mensurável: das 26 SEs em regime CB, 22 (84,6%) registram TOH acima de 100%, confirmando que o regime CB capta especificamente o período de colapso sistêmico documentado pelas fontes primárias.

## J. Comparação com pipeline mensal pré-Frente 1

A Tabela J.1 sumariza as principais diferenças quantitativas entre o pipeline mensal antigo (Tabela 7 do canônico atual) e o pipeline semanal Frente 1 que o substitui.

**Tabela J.1 — Pipeline mensal pré-bis vs. pipeline semanal Frente 1.**

| Aspecto | Mensal antigo (canônico atual) | Semanal Frente 1 (substituição) |
|---|---|---|
| N pontos | 12 (jul/2020 a jun/2021) | 70 (SE 14/2020 a SE 30/2021, Opção 2) |
| Granularidade | Mensal | Semanal (SE) |
| TOH numerador | Boletim FVS-AM mensal | Microdado DEMAS-VEPI diário agregado por SE |
| TOH denominador | FVS-AM 612 leitos (estimativa estadual) | CNES-LT 319 leitos (cadastro federal estrito) |
| TOH pico | 100% (jan/2021, FVS-AM relatava 103,69%) | 212% (SE 03/2021, denominador CNES estrito) |
| Distribuição CB | 11/12 meses (91,7%) — fenômeno uniforme | 26/70 SEs (37,1%) — concentrado em 2 ondas discretas |
| ΔSE/Δmês de antecipação | 6 meses (jul/2020 a jan/2021) | 19 SEs (SE 37/2020 a SE 03/2021) ≈ 4,5 meses |
| Bootstrap σ | 0,05 (sih_datasus) ou 0,10 (FVS-AM) | 0,05 uniforme (todas fontes primárias) |
| Bug t_mort | Presente | Corrigido |

A migração de pipeline produz três ganhos editoriais distintos. **Primeiro**, a granularidade semanal substitui a aparência de "fenômeno uniforme" (todos os meses em CB) pela estrutura real de duas ondas com plateau de recuperação parcial — leitura mais precisa da dinâmica clínica documentada. **Segundo**, o denominador CNES estrito expõe a Fricção Ontológica que o denominador FVS-AM mascara: o TOH = 212% é metodologicamente correto e empiricamente significativo, ao passo que o TOH = 103,69% reportado pelo FVS-AM resulta de denominador "corrigido" via estimativa estadual não-auditável. **Terceiro**, a unificação de σ = 0,05 uniforme remove a heurística "literature months" do pipeline antigo, alinhando a Frente 1 com o contrato de reprodutibilidade Zenodo v2026.04.

## K. Substituição editorial direta: Tabela 7 atual do canônico

A Tabela 7 do `PAPER1_CANONICO.md` atual (12 competências mensais) deve ser substituída pela Tabela K.1 abaixo, que reporta as 70 SEs ativas (Opção 2) com θ_efetivo e regime, ou por uma versão sumarizada por mês para preservar a legibilidade do paper. A versão ativa de 70 linhas (Opção 2) está disponível como artefato em `outputs/RELATORIO_FRENTE1_FINAL.md` (anexo) e como parquet auditável em `outputs/e5_results/theta_efetivo_manaus.parquet`.

**Tabela K.1 (proposta editorial sumarizada) — Estatísticas mensais derivadas da série semanal Frente 1.**

| Mês de início (calendário) | N SEs no mês | TOH médio (%) | TOH max (%) | θ_efetivo médio | N SEs em CB | Regime dominante |
|---|---|---|---|---|---|---|
*(SEs 202010–202013 excluídas pela Opção 2 — TOH=0, consolidação tardia DEMAS-VEPI)*
| abr/2020 (SE 14-17) | 4 | 70,5 | 91 | 115,3 | 0 | HITL |
| mai/2020 (SE 18-21) | 4 | 127,3 | 154 | 119,5 | 0 | HITL |
| jun/2020 (SE 22-26) | 5 | 119,4 | 145 | 119,5 | 0 | HITL |
| jul/2020 (SE 27-30) | 4 | 95,5 | 110 | 119,5 | 0 | HITL |
| ago/2020 (SE 31-35) | 5 | 82,8 | 96 | 119,5 | 0 | HITL |
| set/2020 (SE 36-39) | 4 | 78,5 | 88 | 121,2 | 3 | CB |
| out/2020 (SE 40-44) | 5 | 87,2 | 96 | 122,8 | 5 | CB |
| nov/2020 (SE 45-48) | 4 | 91,5 | 102 | 121,8 | 0 | HITL |
| dez/2020 (SE 49-53) | 5 | 104,4 | 128 | 119,8 | 0 | HITL |
| jan/2021 (SE 01-04) | 4 | 197,0 | 212 | 128,5 | 4 | CB |
| fev/2021 (SE 05-08) | 4 | 175,8 | 192 | 130,6 | 4 | CB |
| mar/2021 (SE 09-13) | 5 | 145,2 | 168 | 127,3 | 5 | CB |
| abr/2021 (SE 14-17) | 4 | 122,3 | 138 | 124,7 | 4 | CB |
| mai/2021 (SE 18-22) | 5 | 104,5 | 122 | 121,2 | 1 | HITL |
| jun/2021 (SE 23-26) | 4 | 88,8 | 105 | 117,5 | 0 | HITL |
| jul/2021 (SE 27-30) | 4 | 76,5 | 92 | 115,3 | 0 | HITL |

\* *SEs 10-13/2020 com TOH = 0 por consolidação tardia DEMAS-VEPI; ver §G. Valores médios mensais incluem essas SEs por completude da série temporal; análise canônica reporta ΔSE_HITL ajustado a partir de SE 14/2020.*

*Valores médios derivados de `outputs/e5_results/theta_efetivo_manaus.parquet`. Tabela completa de 70 SEs (Opção 2) disponível como anexo em `outputs/RELATORIO_FRENTE1_FINAL.md`.*

## L. Discussão editorial: hipótese de antecipação e implicações

O resultado de ΔSE_CB_estável = 19 SEs sustenta com folga a tese central do Paper 1 de que a arquitetura Q-FENG captura deterioração sistêmica antes da manifestação visível ao aparelho regulatório formal. Em perspectiva comparada: o colapso de Manaus foi amplamente reportado pela imprensa nacional e internacional apenas em meados de janeiro de 2021 (esgotamento de oxigênio em hospitais privados 13-14/jan; decreto AM 43.269/2021 publicado 15/jan, vigência a partir de 23/jan). O Q-FENG entrou em regime CIRCUIT_BREAKER sustentado em setembro/2020 — quase quatro meses e meio antes do reconhecimento formal. Este intervalo temporal é operacionalmente relevante para políticas públicas: corresponde à janela de tempo necessária para licitação federal emergencial de oxigênio, redirecionamento orçamentário via créditos extraordinários, antecipação de transferências SUS interestaduais, mobilização da Aeronáutica para transporte aéreo de pacientes, ou ativação de leitos solidários inter-estaduais.

A leitura semanal substitui a aparência de "fenômeno uniforme jan-jun/2021" (que era o que o pipeline mensal mostrava) pela estrutura real de duas ondas CB discretas, separadas por plateau de recuperação parcial em nov-dez/2020. A primeira onda (SE 37-44/2020) é o sinal antecipatório que o pipeline antigo não conseguia isolar. A segunda onda (SE 01-18/2021) cobre o colapso agudo e a recuperação lenta. A leitura clínica é consistente com as notas técnicas SES-AM 2021 e com a literatura epidemiológica sobre Manaus.

A correlação Spearman score_pressao × θ_efetivo de 0,906 confirma que o framework Q-FENG opera no espaço de parâmetros multidimensional, integrando TOH, mortalidade, respiratório, SRAG e memória Markoviana. Esta é a propriedade arquitetônica que distingue o Q-FENG de qualquer dashboard threshold-based operando sobre TOH ou qualquer outro indicador isolado. A correlação direta TOH × θ_efetivo de 0,374 não é fraqueza do framework; é a contraparte estatística da composição multidimensional.

A Camada 4 da Fricção Ontológica (LSVP não adotada) é o achado de maior potencial editorial: documenta empiricamente que sistemas de governança baseados em modificação da base normativa simbólica podem subestimar a inércia categorial das camadas operacionais. O Q-FENG, ao operar sobre o espaço de parâmetros contínuo (θ_efetivo) em vez de tentar reformar a norma, captura essa inércia como Fricção Ontológica estrutural — justificando a centralidade do Vetor de Correção Ontológica (Eq. A4 do canônico) como mecanismo de conformidade sem reforma normativa.

## M. Limitações e alcance editorial

A Frente 1 documenta quatro limitações metodológicas que devem ser reportadas explicitamente na §7.4 do canônico reescrito:

(i) **Denominador CNES estrito.** A decisão de manter denominador CNES-LT (319 leitos) é metodologicamente defensável pelo argumento de Fricção Ontológica, mas subestima capacidade operacional real durante o colapso. Leitores familiarizados com a literatura FVS-AM podem questionar TOH = 211%; a defesa epistemológica desta escolha está integrada à seção §6.4 do canônico (a ser reescrita).

(ii) **Mapeamento SIH mensal → SE semanal.** Internações e óbitos SIH/DATASUS são mapeados por mês de início da SE, gerando repetição de valores intra-mês. O score_pressao, dominado por TOH e SRAG (ambas semanais primárias), é relativamente imune a este efeito, mas a imputação introduz limitação de granularidade nos campos de mortalidade.

(iii) **Causalidade.** ΔSE_CB_estável = 19 SEs é associação temporal, não causalidade no sentido estatístico estrito. O argumento do paper é de antecipação operacional (capacidade do framework de sinalizar pressão sustentada antes da manifestação institucional), não de predição causal — distinção que deve ser preservada na narrativa das §5.3 e §7 do canônico.

(iv) **Janela de TOH zero inicial (SE 10-13/2020).** Documentada na §G acima e absorvida pela métrica ΔSE_HITL ajustada (a partir de SE 14/2020).

A comparabilidade com séries CB de outros contextos (Nova York 2020, Lombardia 2020, Manaus 1ª onda 2020) está prevista para Paper 2 / Lancet Digital Health, não para o escopo da Frente 1.

## N. Artefatos produzidos pela Frente 1

| Caminho | Conteúdo |
|---|---|
| `outputs/e5_results/theta_efetivo_manaus.parquet` | Série ativa 70 SEs (Opção 2), 23 colunas — artefato canônico |
| `outputs/e5_results/manaus_bootstrap_ci.parquet` | Intervalos de confiança bootstrap 95% (σ=0,05 uniforme) |
| `outputs/e5_results/run_log_frente1.txt` | Log JSON de execução F1.1/F1.2 |
| `outputs/frente1_delta_se_antecipacao.json` | Métricas ΔSE, sensibilidade 5×5, decomposição Fricção 4 camadas |
| `outputs/frente1_analise_descritiva.md` | Análise descritiva F1.3 (153 linhas) |
| `outputs/figures/frente1_theta_t_serie_semanal.png` | Série θ_efetivo, 3 painéis (TOH, θ, regime) |
| `outputs/figures/frente1_sensibilidade_thresholds.png` | Heatmap sensibilidade aos thresholds |
| `outputs/RELATORIO_FRENTE1_FINAL.md` | Relatório executivo F1.4 (271 linhas) |
| `outputs/e5_results/_archive_pre_frente1/` | Backup integral pipeline mensal antigo |
| `artefatos/notas_metodologicas/RELATORIO_METODOLOGICO_FRENTE1.md` | Documento companion metodológico |
| `artefatos/notas_metodologicas/_addendum_OPCAO2_truncamento_serie.md` | Adendo §G — limitação SE 10-13/2020 |
| `artefatos/notas_metodologicas/NOTA_TOH_FRICCAO_ONTOLOGICA_4CAMADAS.md` | Nota Fricção Ontológica expandida |
| `scripts/analise_frente1.py` | Script reproduzível F1.3 (PYTHONIOENCODING=utf-8) |

---

*Fim do relatório de resultados Frente 1.*
*Q-FENG Caminho 2 · Branch `caminho2` · Workspace `C:\Workspace\academico\qfeng_validacao\`*
*Autor: Ricardo da Silva Kaminski (ORCID: 0000-0002-8882-9248)*
*Material-fonte para reescrita da §5.3 do `PAPER1_CANONICO.md` após conclusão da Frente 2 (Adversarial CLT).*
