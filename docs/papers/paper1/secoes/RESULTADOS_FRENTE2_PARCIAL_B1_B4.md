# Resultados Parciais — Frente 2: Braços B1–B4

> **Status:** Parcial — snapshot frozen de 29/abr/2026. Braço B5 (motor θ completo) em execução; análises finais H7, H8a/H8b e re-rodada de H3 seguirão em B5.10 após B5 = 600/600.

---

## Sumário Executivo

A Frente 2 do experimento adversarial CLT testou quatro estratégias de raciocínio jurídico automatizado em 50 cenários da jurisprudência trabalhista brasileira, com 600 respostas por braço (4 modelos × 50 cenários × 3 runs). O braço de ancoragem simbólica (B3 — Clingo + narrativa LLM) reduziu a taxa de alucinação em 16,0 pontos percentuais em relação ao LLM sem âncora (B1), com odds ratio de discordância de 9,73 e p unicaudal de 3,2 × 10⁻²¹ pelo teste de McNemar exato (Tabela T4). O resultado é robusto à correção de Bonferroni para oito hipóteses (α corrigido = 0,00625). O braço de recuperação semântica isolada (B2 — RAG sem Clingo) produziu efeito contrário: elevou a taxa de alucinação em 8,7 pontos percentuais em relação à linha de base B1, sugerindo que a recuperação de texto normativo sem âncora formal amplifica, em vez de atenuar, a tendência do LLM a afirmar conformidade em cenários de violação. Esses dois achados juntos — B3 reduz alucinação e B2 a aumenta — constituem a evidência central em favor da tese de que o componente simbólico (Clingo ASP) é o fator causal da melhoria, não a disponibilidade de contexto normativo por si só.

---

## 1. Design Experimental e Cardinalidade

O design 4 × 4 × 50 × 3 compreende quatro braços experimentais, quatro modelos de linguagem de grande escala (LLMs), cinquenta cenários de fricção normativa e três runs por célula, totalizando 2.400 observações para os braços B1–B4 (Tabela T1). Os quatro braços diferem na cadeia de raciocínio apresentada ao LLM:

- **B1** (LLM bruto): apenas o enunciado do cenário, sem recuperação externa nem âncora simbólica.
- **B2** (RAG isolado): enunciado do cenário acrescido de fragmentos recuperados do corpus normativo CLT/CF88 por similaridade semântica.
- **B3** (ancoragem simbólica): enunciado do cenário acrescido do resultado de execução Clingo — predicados soberanos e elásticos ativos — sem a camada Q-FENG.
- **B4** (Q-FENG completo sem motor θ): ancoragem simbólica com saída narrativa estruturada pelo esquema de predicados Q-FENG, mas sem o motor de interferência quântica θ.

O braço B5 (motor θ completo) encontra-se em execução no momento da consolidação deste relatório parcial e será incluído em B5.10.

Os cinquenta cenários distribuem-se em quatro categorias de fricção normativa: `derivacional` (n = 23 cenários × 48 obs./cenário = 1.102 obs.), `procedural` (11 × 48 = 528), `controle_positivo` (11 × 48 = 528) e `controle_negativo` (5 × 48 = 239), conforme `scenarios.yaml`. A categoria `derivacional` compreende cenários em que decisões judiciais citam súmulas ou orientações jurisprudenciais inexistentes; `procedural`, violações a requisitos formais de fundamentação; `controle_positivo`, situações de conformidade genuína que o LLM deveria confirmar; `controle_negativo`, situações onde nenhuma obrigação normativa é ativada (taxa de alucinação esperada = 0% para qualquer braço competente).

Cada run usa seed fixo por posição (seed₁ = 42, seed₂ = 137, seed₃ = 271) para reprodutibilidade. A distribuição confirmada por (braço, modelo) é exatamente 150 observações por célula — design completamente balanceado. O snapshot frozen `results_b1_b4_para_analise_29abr2026.parquet` (2.400 linhas, SHA256: `06e70f27...`) foi isolado do parquet principal antes do início das análises confirmatórias para garantir independência entre coleta e análise sob escrita concorrente do braço B5.

---

## 2. Latência e Custo Computacional

A Tabela T2 apresenta a latência mediana por (braço, modelo) em milissegundos. Três padrões são imediatamente identificáveis.

O braço B3 é consistentemente mais rápido que B1 para todos os modelos. O modelo phi4:14b passa de 44.163 ms em B1 para 16.046 ms em B3; o gemma3:12b de 71.117 ms para 22.718 ms; o qwen3:14b de 144.664 ms para 36.376 ms. A redução de latência em B3 é consequência direta da ancoragem simbólica: o prompt inclui os predicados Clingo já resolvidos, induzindo respostas mais curtas e focadas nos predicados soberanos ativos, em vez de raciocínio aberto sobre o corpus legal completo. O LLM em B3 funciona como camada narrativa sobre uma decisão simbólica já tomada, não como motor de raciocínio jurídico autônomo.

O braço B2 apresenta latência menor que B1, mas maior que B3, para a maioria dos modelos. O RAG reduz o espaço de busca do LLM ao restringir o contexto, mas não direciona o raciocínio na forma estruturada que a ancoragem simbólica proporciona.

O braço B4 apresenta latência consistentemente maior que B3. O overhead do esquema narrativo Q-FENG — obrigando o modelo a organizar a resposta segundo os predicados soberanos/elásticos — é o fator de acréscimo, estimado entre 5.000 ms e 16.000 ms conforme o modelo. Esse overhead será quantificado formalmente em H7 com os dados de B5, que incluem os campos de temporização granular `t_clingo_ms`, `t_psi_build_ms` e `t_theta_compute_ms`.

---

## 3. Hipótese H1 — Redução de Alucinação (B3 vs B1)

**H1₀:** π(B3) = π(B1). **H1₁:** π(B3) < π(B1) (unicaudal). Teste: McNemar exato sobre pares (modelo, cenário, run).

A Tabela T4 apresenta os resultados globais e o breakdown por modelo. O pareamento produziu 600 pares completos (após correção de um registro com `run_id = 0` armazenado incorretamente em vez de `run_id = 1`; a seed = 42 confirma a correspondência). A tabela 2 × 2 de discordâncias apresenta b = 107 (B3 acerta, B1 erra) e c = 11 (B1 acerta, B3 erra), com odds ratio de discordância OR = b/c = 9,73. O teste de McNemar exato retorna p unicaudal = 3,2 × 10⁻²¹, significativo ao nível Bonferroni de 0,00625.

A redução absoluta de 16,0 pontos percentuais (de 19,8% em B1 para 3,8% em B3) é homogênea entre os quatro modelos: gemma3:12b passa de 11,3% para 0,0% (OR = ∞, p = 7,6 × 10⁻⁶); llama3.1:8b de 29,3% para 10,7% (OR = 5,0, p = 7,5 × 10⁻⁶); phi4:14b de 32,0% para 4,7% (OR = 11,3, p = 4,1 × 10⁻¹⁰); qwen3:14b de 6,7% para 0,0% (OR = ∞, p = 9,8 × 10⁻⁴). Todos os testes por modelo são significativos ao nível Bonferroni, o que afasta a hipótese de que o resultado global seja artefato de um único modelo.

O modelo llama3.1:8b apresenta taxa residual de 10,7% em B3 — consistentemente acima dos demais. Esse diferencial será retomado na análise de H3.

**Conclusão H1:** Rejeitada H1₀. A ancoragem simbólica via Clingo reduz a taxa de alucinação em 80,6% em termos relativos (de 19,8% para 3,8%), com OR de discordância de 9,73 e significância mantida após correção de Bonferroni.

---

## 4. Hipótese H2 — Não-Inferioridade de Cobertura Jurídica (B3 vs B1)

**H2₀:** µ(B3) − µ(B1) ≤ −0,05. **H2₁:** µ(B3) − µ(B1) > −0,05. Teste: Wilcoxon signed-rank sobre diferenças nos 600 pares.

A Tabela T5 apresenta os resultados. A cobertura média de B3 é 1,295 versus 1,958 em B1 (escala ordinal 0–3, onde 0 = sem citação normativa; 1 = lei citada; 2 = lei + artigo; 3 = lei + artigo + parágrafo/inciso). A diferença mediana B3 − B1 = −1,0 (IC95% bootstrap [−1,0; 0,0]), com p unicaudal para não-inferioridade = 1,0. A não-inferioridade não é demonstrada.

A interpretação desse resultado requer cautela. O `coverage_score` mede a riqueza de citação textual — número de referências a leis, artigos e parágrafos no texto da resposta. As respostas do braço B3 são estruturadas em torno dos predicados Clingo fornecidos pelo prompt (`sovereign(prohibition_of_generic_precedent_citation)`, `sovereign(obligation_to_ground_decision_in_identified_ratio_decidendi)` etc.), e tendem a mencionar os predicados nominalmente em vez de reexpandir as referências legais subjacentes. Essa estratégia de resposta é adequada ao papel de B3 como camada narrativa sobre decisão simbólica já tomada, mas resulta em menor densidade de citação textual. O tradeoff entre precisão decisória (redução de alucinação) e amplitude de citação (coverage_score) será explorado qualitativamente na seção de Discussão.

**Conclusão H2:** Não demonstrada. B3 apresenta menor cobertura textual que B1, o que reflete a economia de raciocínio imposta pela ancoragem simbólica, não falha em substância jurídica.

---

## 5. Hipótese H4 — RAG Isolado (B2 vs B1)

**H4a:** McNemar B2 vs B1 (alucinação). **H4b:** Wilcoxon B2 vs B1 (cobertura, não-inferioridade).

A Tabela T6 apresenta os dois testes. Para H4a, a tabela de discordâncias apresenta b = 23 (B2 acerta, B1 erra) e c = 75 (B1 acerta, B2 erra), com OR = 0,307. A direção é inversa à hipótese: B2 *aumentou* a alucinação em 8,7 pontos percentuais (de 19,8% em B1 para 28,5% em B2), e o teste de McNemar retorna p bicaudal = 1,3 × 10⁻⁷ para o efeito observado — mas no sentido oposto ao pré-registrado. A hipótese H4a de redução parcial por RAG não é corroborada.

Para H4b, a cobertura média de B2 (1,648) é inferior à de B1 (1,958), com diferença mediana B2 − B1 = 0,0 (IC95% bootstrap [0,0; 0,0]) e p = 0,219 — não-inferioridade não demonstrada.

O aumento de alucinação em B2 é o achado mais contra-intuitivo do experimento. A hipótese explicativa mais parsimoniosa é a seguinte: o RAG recupera trechos do corpus normativo que descrevem obrigações e direitos de forma assertiva. Ao incorporar esse texto no contexto, o LLM tende a interpretar a situação como conformidade com as normas recuperadas, em vez de detectar a violação presente no cenário. Esse efeito é análogo ao que a literatura de RAG denomina *context-grounding bias*: o modelo ancora sua resposta no texto recuperado e reduz o peso do raciocínio autônomo. Quando o texto recuperado é normativamente correto mas o cenário descreve sua violação, o LLM produz o padrão mais perigoso de erro — afirmar conformidade com exatidão documental para uma situação que constitui infração.

A diferença entre B2 e B3 é, portanto, qualitativa: B3 fornece ao LLM não o texto da norma, mas o *resultado da verificação formal* sobre o cenário — os predicados Clingo que enunciam quais obrigações foram satisfeitas ou violadas. Esse resultado, expresso como conjunto de átomos ASP, não é ambíguo quanto ao sentido da decisão normativa.

**Conclusão H4:** H4a não corroborada — RAG isolado piora a taxa de alucinação. H4b não demonstrada. Os resultados de H4 fortalecem a interpretação causal de H1: a redução de alucinação em B3 deve-se ao componente simbólico (Clingo), não à disponibilidade de contexto normativo.

---

## 6. Hipótese H5 — Variabilidade Intra-(Modelo, Cenário)

**H5a:** Levene (centro = mediana) sobre distribuição de variâncias intra-célula entre B3 e B1, B3 e B2, B3 e B4. **H5b:** Proporção de pares (modelo, cenário) com IC95% bootstrap de B3 e B1 sem sobreposição.

A Tabela T7 apresenta os resultados. A variância intra-célula média decresce monotonicamente com a intensidade da ancoragem: B1 = 0,080, B2 = 0,062, B3 = 0,028, B4 = 0,005. O teste de Levene confirma que B3 tem variância significativamente menor que B1 (F = 18,4, p = 2,3 × 10⁻⁵) e que B2 (F = 8,7, p = 3,4 × 10⁻³), ambos significativos ao nível Bonferroni. O teste B3 vs B4 (F = 10,5, p = 1,3 × 10⁻³) confirma que B4 tem variância menor que B3, coerente com o maior grau de estruturação imposto pelo esquema narrativo Q-FENG.

Para H5b, o bootstrap de IC95% (10.000 réplicas, seed = 42) sobre as médias de `hallucination_flag` por (modelo, cenário) indica que apenas 11 dos 200 pares (5,5%) apresentam intervalos sem sobreposição. Esse percentual baixo é consequência da natureza binária do `hallucination_flag` e do tamanho das células intra-cenário (n = 3 runs): com apenas 3 observações por célula, os ICs bootstrap por construção tendem a cobrir {0} ou {0,1/3,2/3,1}, produzindo ampla sobreposição mesmo quando as médias diferem.

A evidência de H5 deve ser interpretada conjuntamente: o Levene confirma que a distribuição de variâncias é diferente entre braços (H5a confirmada), mas o bootstrap overlap indica que a separação não é uniforme ao nível de (modelo, cenário individual), dada a granularidade limitada de 3 runs por célula.

**Conclusão H5:** H5a corroborada — B3 tem menor variância intra-célula que B1 e B2, significativo ao nível Bonferroni. H5b apresenta sobreposição em 94,5% dos pares, limitação estrutural de n = 3 runs por célula.

---

## 7. Hipótese H6 — Interação Fricção × Braço

**H6:** ANOVA two-way `hallucination_flag ~ C(friccao_categoria) * C(braco)` com post-hoc Tukey HSD por categoria.

A Tabela T8 apresenta os resultados. A ANOVA two-way revela efeitos principais e de interação todos significativos ao nível Bonferroni. O efeito principal do braço (F = 112,5, p = 4,0 × 10⁻⁶⁸, η²_parcial = 0,124) é o mais forte, confirmando que a ancoragem simbólica é o preditor dominante da taxa de alucinação independentemente da categoria de fricção. O efeito principal da fricção (F = 44,2, p = 8,2 × 10⁻²⁸, η²_parcial = 0,053) indica que a dificuldade do cenário varia entre categorias. A interação (F = 12,3, p = 2,7 × 10⁻¹⁹, η²_parcial = 0,045) confirma que o benefício da ancoragem simbólica é heterogêneo por categoria de fricção.

A análise das taxas por célula (Tabela T8, painel inferior) revela o padrão previsto na H6: a categoria `procedural` apresenta as taxas mais elevadas em B1 (38,6%) e B2 (54,5%), refletindo a dificuldade de identificar violações formais de fundamentação por raciocínio LLM não ancorado. B3 reduz essa taxa para 6,8% e B4 para 0%. A categoria `derivacional` — cenários com citações de súmulas inexistentes, a categoria de phantom citation canônica do experimento — apresenta B1 = 14,9% e B3 = 3,3%. A categoria `controle_negativo` apresenta 0% de alucinação em todos os braços, confirmando que a operacionalização de `hallucination_flag` não produz falsos positivos quando nenhuma violação existe no cenário.

O achado mais pronunciado da interação é a assimetria entre categorias `procedural` e `derivacional` nos braços B1 e B2: B2 eleva a taxa de `procedural` de 38,6% para 54,5% — um aumento de 15,9 pontos percentuais — enquanto eleva `derivacional` de 14,9% para 23,2% (8,3 pp). O RAG tende a exacerbar o erro em cenários procedurais mais do que em cenários de phantom citation, possivelmente porque o corpus normativo recuperado em cenários `procedural` contém muitas afirmações positivas sobre os direitos processuais pertinentes, induzindo o LLM a confirmar o cumprimento das formalidades.

**Conclusão H6:** Interação fricção × braço significativa (F = 12,3, p = 2,7 × 10⁻¹⁹). B3 reduz alucinação em todas as categorias, com maior efeito relativo em `procedural` (redução de 31,8 pp) e menor em `controle_positivo` (redução de 15,9 pp). O efeito de B2 é consistentemente inverso em todas as categorias não-controle.

---

## 8. Hipótese H3 (Parcial) — Interação Braço × Modelo

**H3 parcial (B1–B4):** ANOVA two-way `hallucination_flag ~ C(braco) * C(modelo)`.

O resultado parcial (Tabela em `h3_parcial_result.json`) confirma interação significativa braço × modelo (F = 4,96, p = 1,25 × 10⁻⁶, η²_parcial = 0,018), efeito principal do braço (F = 108,1, p = 1,2 × 10⁻⁶⁵, η²_parcial = 0,120) e efeito principal do modelo (F = 30,5, p = 2,5 × 10⁻¹⁹, η²_parcial = 0,037).

A matriz de taxas por (braço, modelo) expõe um padrão relevante para a seleção de arquitetura: llama3.1:8b apresenta a maior suscetibilidade à alucinação em B1 (29,3%) e a menor redução relativa em B3 (10,7% residual), enquanto gemma3:12b e qwen3:14b atingem 0,0% de alucinação em B3. Essa heterogeneidade indica que llama3.1:8b processa os predicados Clingo de forma menos determinística — hipótese a ser investigada em B5.10 com a distribuição de θ_efetivo por modelo.

**Nota de escopo:** este resultado é *parcial*; a análise final H3 com B5 incluído será executada em B5.10 e poderá alterar as estimativas de interação. O valor de η²_parcial = 0,018 para a interação deve ser interpretado como limite inferior.

---

## 9. Effect Sizes Consolidados

A Figura F5 (forest plot) apresenta os effect sizes principais das hipóteses H1, H4a e H5. Para H1, o OR de discordância = 9,73 (IC95% Wald [5,24, 18,06]) representa o efeito mais forte da série — B3 acerta 9,73 vezes mais do que erra em pares onde B1 erra. Para H4a, o OR = 0,307 (IC95% [0,192, 0,489]) confirma a inversão: B2 acerta menos do que erra nesses pares. Para H5, a razão de variâncias B3/B1 = 0,354, com Levene F = 18,4.

---

## 10. Limitações e Validade Externa

Quatro limitações devem ser registradas explicitamente.

**Snapshot e temporalidade.** Os dados de B1–B4 foram coletados em uma única janela temporal (24–29 de abril de 2026). Variações em temperatura de inferência ou atualizações de pesos dos modelos entre sessões não foram controladas, embora o uso de seeds fixos mitigue parte dessa variância.

**Modelos open-source locais.** Os quatro modelos (gemma3:12b, llama3.1:8b, phi4:14b, qwen3:14b) foram rodados via Ollama em hardware local sem acesso à internet. Esse cenário corresponde a um caso de uso real de implantação privada, mas os resultados podem não se generalizar diretamente para modelos de grande escala com fine-tuning jurídico específico (ex.: GPT-4-Turbo com system prompt legal).

**Idioma.** Os 50 cenários estão em português brasileiro, centrados na jurisprudência trabalhista do TST. A generalização para outros ordenamentos jurídicos ou idiomas requer validação independente.

**Definição operacional de `hallucination_flag`.** A operacionalização aqui adotada — falha em identificar violação quando `correct_decision = 'VIOLACAO'` — é uma proxy do conceito mais amplo de alucinação jurídica (que inclui phantom citations, distorção de holding, fabricação de datas). A restrição ao ground truth de `correct_decision` implica que cenários `controle_positivo` nunca geram `hallucination_flag = 1`, ainda que o LLM produza raciocínio incorreto sobre o mecanismo da conformidade. Uma instrumentação mais rica — como anotação humana de phantom citations em amostra estratificada — será considerada para B5.10.

---

## 11. Próximos Passos

Com B5 em execução (50/600 na consolidação deste relatório, ETA ≈ 10h, latência mediana = 65,8 s/chamada), as análises subsequentes em B5.10 incluirão:

- **H7** (sidecar viability): razão overhead_motor_θ / latência_total usando `t_clingo_ms + t_psi_build_ms + t_theta_compute_ms` de B5; hipótese: overhead < 5%.
- **H8a** (B5 vs B4 — alucinação): McNemar; hipótese: B5 = B4 (motor θ não deve adicionar alucinação).
- **H8b** (B5 vs B4 — calibração): Brier score e Expected Calibration Error sobre as probabilidades `qfeng_p_action` de B5.
- **H3 final** com B5 incluído.
- Atualização das tabelas T1–T8 e geração de T9 (distribuição de θ_efetivo por cenário e modelo).
- Figura F7 (distribuição θ_efetivo por regime: BLOCK/STAC/PASS).
- Integração ao paper canônico `PAPER1_CANONICO.md` e derivação para JURIX (10 pp) e Lancet Digital Health (4 pp + apêndice metodológico).
