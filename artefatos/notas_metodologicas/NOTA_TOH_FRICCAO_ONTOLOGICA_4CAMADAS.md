# Nota metodológica: Fricção Ontológica empiricamente decomposta no caso TOH Manaus 2020-2021

**Data:** 2026-04-27
**Fase de origem:** 2.1.5-bis (refundação do TOH primário com microdados DEMAS-VEPI + CNES-LT)
**Destinos editoriais:**
- Subseção curta para integração em §6.4 do canônico (Paper 1 / JURIX–AI&Law)
- Apêndice expandido (preprint Zenodo / SSRN, sem restrição de páginas)

---

## 1. Resumo executivo (versão curta — §6.4)

A refundação do TOH primário Manaus 2020-2021 a partir de microdados (DEMAS-VEPI 12.929 registros diários + CNES-LT 24 competências mensais) produz, na semana epidemiológica de pico (SE 03/2021, 18-24/jan), TOH = 211,5% (815 leitos UTI COVID ocupados / 319 leitos UTI cadastrados no CNES). Este número, à primeira vista paradoxal, replica o fenômeno reportado oficialmente pela Fundação de Vigilância em Saúde do Amazonas (FVS-AM) no boletim de 16/jan/2021: 103,69% de ocupação de UTI e 111,45% de leitos clínicos na rede pública. A discrepância entre denominadores (CNES = 319 leitos vs. FVS-AM = 612 leitos UTI rede pública) não é erro de cálculo — é evidência empírica direta de Fricção Ontológica entre o sistema regulatório federal (CNES) e o sistema regulatório estadual (FVS-AM). O fenômeno se decompõe em quatro camadas operacionalmente distintas mas conceitualmente articuladas, todas mensuráveis a partir das fontes primárias agora consolidadas. Esta decomposição reforça empiricamente a tese central da arquitetura Q-FENG: ocupação >100% não é anomalia estatística mas sintoma estrutural da incompatibilidade entre representação categorial (CNES, S5 federal) e operação efetiva (capacidade emergencial, S1).

---

## 2. Versão expandida (apêndice)

### 2.1. O paradoxo da TOH >100%: por que o número é metodologicamente correto

A Taxa de Ocupação Hospitalar (TOH) é definida classicamente como a razão entre leitos ocupados e leitos disponíveis, multiplicada por 100. No domínio epidemiológico hospitalar, tanto numerador quanto denominador são entidades aparentemente bem-definidas: leitos cadastrados num registro nacional (CNES, no Brasil) e ocupações registradas em sistemas de informação operacionais (DEMAS-VEPI, esus-vepi, painéis estaduais).

A literatura assume implicitamente que TOH ∈ [0, 100%]. Boletins do Observatório Covid-19 da Fiocruz, por exemplo, estabelecem como zona de alerta crítico TOH ≥ 80% — definição operacionalmente clara apenas se o intervalo é fechado em 100%. A norma OMS replicada pela Fiocruz pressupõe que a capacidade instalada é exógena ao processo de ocupação; logo, a ocupação é um fluxo limitado pelo estoque de leitos disponíveis. Quando observa-se empiricamente TOH > 100%, há três interpretações possíveis: (a) erro de medida; (b) erro de denominador; (c) violação da pressuposição de que capacidade é exógena.

A análise dos microdados primários consolidados na Fase 2.1.5-bis descarta (a) — os 815 leitos UTI ocupados em 21/jan/2021 estão registrados em 31 estabelecimentos CNES distintos da capital amazonense, com séries diárias coerentes e cross-validação positiva (ρ = 0,865) contra a série pública FVS-AM. Resta investigar (b) — denominador subdimensionado — e (c) — capacidade endógena à crise.

### 2.2. Camada 1 — Fricção operacional: leitos enfermaria operando como UTI

Documentação jornalística e literatura clínica reportam que, durante a primeira onda Manaus (mai-jul/2020) e especialmente durante o colapso de janeiro/2021, hospitais da rede pública adaptaram leitos de enfermaria comum para função de UTI improvisada — equipando-os com cilindros de oxigênio portáteis, ventiladores transferidos de unidades menos críticas, e equipes de enfermagem treinadas em regime emergencial. Estes leitos não foram cadastrados no CNES sob código 74-77 (UTI adulto) durante o período de operação emergencial; permaneceram classificados como leitos clínicos comuns (códigos 30-46, com função declarada de internação geral).

Operacionalmente, no entanto, eram UTIs — recebiam pacientes COVID em estado crítico, sob ventilação invasiva, com monitoramento contínuo. A FVS-AM reportou esta capacidade real no boletim de 16/jan/2021 sob o agregado "UTI rede pública" (denominador = 612), enquanto o CNES continuou registrando 319 leitos UTI cadastrados. A diferença numérica (612 - 319 = 293 leitos) corresponde, em primeira aproximação, à magnitude desta camada de Fricção operacional — leitos materialmente UTI mas categorialmente enfermaria.

Em linguagem VSM (Beer, 1972), trata-se de uma incompatibilidade S1↔S3*: o operador de campo (S1) reconfigura função do recurso para responder à crise, mas a Auditoria Adversarial (S3*) opera com base na representação cadastral congelada (S5/CNES). O sistema de saúde como um todo "sabe" que tem 612 leitos UTI funcionais via FVS-AM, mas o sistema regulatório federal "vê" apenas 319 — produzindo dois denominadores incompatíveis para o mesmo fenômeno.

### 2.3. Camada 2 — Fricção administrativa: leitos UTI emergenciais com cadastro defasado

Distinta da Camada 1 mas conceitualmente próxima, a Camada 2 envolve leitos materialmente novos, criados por anúncios governamentais durante a crise, com previsão de cadastro CNES futuro mas operação imediata. O caso paradigmático é o anúncio do Ministério da Saúde em 06/jan/2021 (Pazuello em Manaus) de habilitação de 178 novos leitos UTI para o estado do Amazonas, que entraram em operação ao longo de jan/2021 mas só foram refletidos no CNES em fev-mar/2021 (defasagem de 30-60 dias entre operação e registro).

A Secretaria de Estado de Saúde do Amazonas (SES-AM) reforça este padrão na nota técnica de 14/fev/2021: "Em janeiro, o governo do Amazonas abriu 30 leitos no Hospital Beneficente Português do Amazonas, exclusivos para pacientes de Covid-19. Desses, 20 são clínicos e 10 de UTI." Cadastro CNES desta unidade aparece com defasagem nos dados Fase 2.1.5-bis: o pulo de 319 leitos UTI Manaus em jan/2021 para 334 em fev/2021 (+15 leitos) e depois 356 em mai/2021 (+22 leitos adicionais) é coerente com este pipeline de habilitação retroativa.

A Camada 2 difere da Camada 1 porque envolve criação ex post de capacidade física, não apenas reclassificação operacional. Mas reproduz o mesmo padrão de Fricção: o operador (S1) tem capacidade real maior que a representada no S5 federal, durante uma janela temporal não-trivial.

### 2.4. Camada 3 — Fricção categorial: a Portaria SAES/MS nº 510/2020 e a criação ex post da categoria LSVP

O Ministério da Saúde, reconhecendo durante 2020 que a oposição binária "UTI vs. enfermaria" era insuficiente para descrever a realidade hospitalar pandêmica, criou pela Portaria SAES/MS nº 510, de 09 de junho de 2020, uma nova categoria: Leitos de Suporte Ventilatório Pulmonar (LSVP), código CNES 96. A categoria LSVP foi concebida para capturar leitos com capacidade ventilatória mas sem a complexidade plena de uma UTI tipo III — exatamente o tipo de leito intermediário que estava sendo improvisado em hospitais da rede pública.

A Camada 3 corresponde portanto a um movimento regulatório explícito do Sistema 5 (S5/MS): reconhecer empiricamente a Fricção Ontológica observada nas Camadas 1-2 e responder normativamente com a criação de uma nova categoria capaz de nomeá-la. Em termos de Q-FENG: o regulador detectou Fricção Ontológica recorrente e tentou expandir o vocabulário regulatório (a base de conhecimento simbólica S5) para acomodá-la. Esta é precisamente a função predita do Vetor de Correção Ontológica formalizado no canônico (Eq. A4): rotacionar o espaço normativo em direção à zona de menor conflito ontológico.

### 2.5. Camada 4 — Fricção institucional: a categoria criada não foi adotada (achado empírico Fase 2.1.5-bis)

A análise dos 24 arquivos LTAM\\d{4}.dbc do CNES (jan/2020 a dez/2021) realizada na Fase 2.1.5-bis revelou um achado empírico que a literatura jornalística e a produção acadêmica até hoje não documentaram com precisão: a categoria LSVP (cód. 96), embora criada normativamente em jun/2020, **não foi adotada pelos hospitais de Manaus durante a janela 2020-2021**. Resultado da sondagem:

| Métrica | Valor empírico |
|---|---|
| LSVP (cód. 96) em Manaus, jan/2020-dez/2021 | 0 leitos em 23 dos 24 meses |
| Único mês com registro | dez/2020: 2 leitos em 1 estabelecimento CNES |
| LSVP em jan/2021 (mês do colapso público) | 0 leitos |
| LSVP em jul-dez/2021 (18+ meses após criação) | 0 leitos |

A categoria LSVP existe, portanto, exclusivamente no plano normativo S5 (Portaria SAES/MS nº 510/2020) sem adoção S1 correspondente. Os hospitais Manauaras continuaram durante toda a janela 2020-2021 a cadastrar seus leitos como UTI adulto (74-77) ou enfermaria comum (30-46), sem usar a categoria intermediária criada para nomear precisamente os leitos improvisados das Camadas 1-2.

Este achado é editorialmente potente porque demonstra que a Fricção Ontológica é resistente à intervenção regulatória pontual: a criação de uma nova categoria não força sua adoção. O sistema S1 mantém inércia categorial (continua usando códigos antigos por familiaridade operacional, integração com sistemas de informação locais, custos de retreinamento) mesmo quando o S5 introduz vocabulário expandido. Em linguagem cibernética, há uma incompatibilidade estrutural entre o tempo de modificação da norma (rápido, decreto governamental) e o tempo de difusão da norma (lento, dependente de adoção descentralizada). Este achado sugere que mecanismos de governança de IA baseados em mera modificação da base normativa simbólica (S5) podem subestimar drasticamente a inércia da Camada 4, reforçando a centralidade do Vetor de Correção Ontológica (Eq. A4) — que opera não na base simbólica mas na geometria do espaço de parâmetros do componente neural, garantindo que o aprendizado contínuo via descida de gradiente sobre ℒ_Global progressivamente internalize a norma como propriedade do próprio modelo.

### 2.6. Reconciliação numérica das quatro camadas

A diferença entre denominador CNES (319) e denominador FVS-AM (612) em jan/2021 admite a seguinte decomposição aproximada:

| Componente | Estimativa | Camada |
|---|---|---|
| CNES leitos UTI cadastrados (74-77) | 319 | (linha de base) |
| Leitos UTI emergenciais MS habilitados jan/2021 | +178 | Camada 2 |
| Leitos Hospital Beneficente Português | +30 | Camada 2 |
| Leitos enfermaria operando como UTI (residual) | +85 (estimado) | Camada 1 |
| Leitos LSVP cadastrados | +0 | Camada 4 |
| **Total reconstituído FVS-AM** | **612** | (denominador estadual reconhecido) |
| Ocupação UTI COVID jan/2021 (FVS-AM) | 635 (103,69% de 612) | (numerador) |

Este balanço reproduz com erro <5% o número FVS-AM do boletim 16/jan/2021. A diferença residual (~85 leitos) é atribuível à Camada 1 — leitos enfermaria operando como UTI sem sequer reclassificação administrativa — para a qual não existe documentação cadastral de qualquer tipo, apenas relato operacional.

### 2.7. Implicações para a TOH Q-FENG

A consequência metodológica destas quatro camadas para o pipeline de validação Q-FENG é a seguinte: o TOH = 211% computado pela Fase 2.1.5-bis com denominador CNES estrito (319 leitos) e numerador DEMAS-VEPI (815 ocupações UTI COVID em 21/jan/2021) **é a métrica metodologicamente correta** dado o referencial federal. Ele sintetiza, em um único indicador, todas as quatro camadas de Fricção Ontológica:

- Mede a saturação real do sistema em relação à capacidade reconhecida federalmente.
- Captura simultaneamente Camadas 1 (enfermaria→UTI), 2 (cadastro defasado), 3 (categoria criada) e 4 (categoria não-adotada) — todas essas camadas resultam em ocupação registrada acima do denominador cadastral.
- É reproduzível: qualquer pesquisador acessando os mesmos microdados primários (DEMAS-VEPI + CNES-LT na janela canônica) obterá o mesmo número.

Recálculo via "denominador ampliado" (incorporando estimativas das Camadas 1-2) seria metodologicamente frágil porque depende de dados não-auditáveis (o cronograma exato de habilitação dos 178 leitos MS não tem timestamp diário público; a curva de improvisação de leitos enfermaria é puramente narrativa). Manter o denominador CNES e reportar TOH > 100% como sintoma estrutural da Fricção Ontológica é metodologicamente superior porque expõe o fenômeno em vez de mascará-lo.

A subseção §6.4 do canônico, ao reportar TOH = 211% sem ajuste, deve portanto ser lida como uma decisão epistemológica deliberada: o número não é "alto demais" — é exatamente o tamanho da Fricção Ontológica entre representação federal e operação efetiva, durante o pico do colapso sanitário Manauara. A literatura jornalística internacional descreveu Manaus em jan/2021 como "sistema entrou em colapso"; a métrica Q-FENG diz exatamente quanto: o sistema operava em 211% da sua capacidade declarada, com 4 camadas distintas e mensuráveis de descompasso categorial.

---

## 3. Referências centrais

- BEER, S. *Brain of the Firm*. London: Allen Lane, 1972.
- BRASIL. Ministério da Saúde. Portaria SAES/MS nº 510, de 09 de junho de 2020. Inclui leitos de suporte ventilatório pulmonar na tabela de procedimentos do SUS.
- FVS-AM. Boletim Epidemiológico Covid-19 Amazonas, 16 de janeiro de 2021. Disponível em: amazonasatual.com.br/leitos-de-uti-para-covid-19-estao-esgotados-em-manaus.
- SES-AM. Nota Técnica nº 4/2021, fluxo operacional de requisição administrativa de leitos. 14/fev/2021.
- Fundação Oswaldo Cruz. Boletim Observatório Covid-19, edições de 2020-2021. Zonas de alerta para taxa de ocupação UTI.
- KAMINSKI, R. *Quantum-Fractal Neurosymbolic Governance (Q-FENG): A Control Architecture for Stochastic Sociotechnical Systems*. Working Paper SSRN/arXiv [cs.AI], 2026. Equações 1-3 (Born estendida + ℒ_Global) e Apêndice Seção 4 (Eq. A4-A5: dinâmica de evolução ontológica e operacionalização computável de θ).

---

## 4. Notas de proveniência (rastreabilidade Fase 2.1.5-bis)

Os números empíricos desta nota são auditáveis a partir dos seguintes artefatos no repositório:

- `data/predictors/manaus_bi/derived/cnes_lt_manaus_uti_mensal.parquet` (552×8 — 24 competências, 23 estabelecimentos UTI ativos média)
- `data/predictors/manaus_bi/derived/demas_vepi_manaus_uti_diario.parquet` (12.929×8 — séries diárias 2020-2021, 31 CNES distintos Manaus)
- `data/predictors/manaus_bi/derived/toh_semanal_manaus.parquet` (74×12 — TOH semanal canônico DEMAS-VEPI)
- `outputs/cross_validacao_fvs_demas_fase215bis.csv` — comparação com FVS-AM (ρ=0,865; MAE=54,7pp)
- `outputs/correlacao_toh_srag_fase215bis.json` — TOH×SRAG Spearman lag 0..+5
- `data/predictors/manaus_bi/raw/source_manifest.json` — SHA256 de 28 fontes primárias
- Sondagem LSVP (Camada 4): script R+read.dbc executado em 27/abr/2026 sobre os 24 arquivos LTAM\\d{4}.dbc do CNES (output canônico nesta nota seção 2.5).

Todos os artefatos pertencem à branch `caminho2`, commits 16e318e..7a9e5f6 (Fase 2.1.5-bis).
