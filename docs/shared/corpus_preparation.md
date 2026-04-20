# Corpus Construction — Methodology and Gap Analysis
**Q-FENG Empirical Validation | Shared across Paper 1 and Paper 2**
**Sessão de curadoria:** 19 abril 2026 | **Status:** ✅ Corpus completo para MVP

---

## 1. Princípios de seleção do corpus

O corpus do PoC foi construído segundo três critérios hierárquicos:

### 1.1 Hierarquia normativa completa

Para cada regime, o corpus cobre a pirâmide normativa completa:

```
Constitucional → Legislação → Regulamentação → Operacional/Empírico
```

Esta estrutura permite ao Q-FENG detectar **cascatas normativas** (canal ↓ no
VSM): como axiomas constitucionais se propagam até predicados operacionais e onde
as obrigações se perdem ou se contradizem ao longo da cadeia.

### 1.2 Foco nos casos de validação empírica

A seleção prioriza documentos com relação direta aos dois casos paradigmáticos:

- **Case 1 (EXECUTION_FAILURE):** Crise do Oxigênio em Manaus, jan 2021
  - Requer: normas de emergência sanitária + mecanismos de coordenação operacional
- **Case 2 (CONSTITUTIONAL_FAILURE):** Viés Algorítmico Medicaid — Obermeyer 2019
  - Requer: normas de não-discriminação + especificação de equidade em algoritmos

### 1.3 Comparabilidade entre regimes

Os três regimes foram selecionados para maximizar a **variância estrutural** em
dimensões teoricamente relevantes:

| Dimensão | Brasil | EU | USA |
|----------|--------|-----|-----|
| Sistema de saúde | Universal (SUS) | Misto (NHS-like) | Condicional (Medicaid) |
| Regime de IA | Em construção (PL 2338) | Vigente (AI Act 2024) | Ausente (federal) |
| Força constitucional da saúde | Direito fundamental (Art. 196) | Carta de Direitos | Equal Protection (proxy) |
| Modelo de governança | Centralizado-federativo | Supranacional | Estadual-federal |

Esta variância permite testar a **invariância fractal** do Q-FENG: a mesma
arquitetura de governança deve produzir comportamentos coerentes em regimes com
premissas radicalmente distintas.

---

## 2. Análise de lacunas (Gap Analysis) — 19 abril 2026

### 2.1 Estado antes desta sessão

| Regime | Subconjunto | Status | Crítico? |
|--------|------------|--------|---------|
| Brasil | constitucional, legislacao, regulamentacao (base) | ✅ | — |
| Brasil | portarias_manaus_2021 (completo) | ⚠️ Parcial | ✅ Sim |
| Brasil | operacional | ✅ | — |
| EU | todos | ✅ | — |
| USA | constitutional, statutory, regulatory | ✅ | — |
| USA | empirical | ❌ Vazio | ✅ Sim |

### 2.2 Documentos ausentes identificados

#### Brasil — Portarias Manaus (críticas para Case 1)

| Documento | Por que crítico | Impacto se ausente |
|-----------|----------------|-------------------|
| Portaria 69/2021 | Institui obrigação de data reporting — 4 dias após o colapso | Predicado `data_reporting_obligation` ausente |
| Portaria 197/2021 | Primeiro mecanismo de requisição pós-colapso — 19 dias após | Evidência de resposta tardia incompleta |
| Portaria 268/2021 | Revoga 197, eleva competência — 34 dias após | Documenta insuficiência do mecanismo anterior |

A sequência 197→268 em 10 dias é evidência documental de **Junção Crítica**
institucional (Kaminski, 2025): o mecanismo de resposta precisou ser reconfigurado
em tempo real, evidenciando que a arquitetura normativa pré-crise era insuficiente.

#### USA — Evidência empírica (crítica para Case 2)

| Item | Por que crítico | Solução adotada |
|------|----------------|----------------|
| Obermeyer et al. (2019), Science | Caso paradigmático de CONSTITUTIONAL_FAILURE | Resumo operacionalizável estruturado |

---

## 3. Método de obtenção dos documentos ausentes

### 3.1 Portarias Manaus — Protocolo de recuperação

As portarias foram obtidas via acesso programático às fontes primárias oficiais:

**Sequência de tentativas:**
1. **bvsms.saude.gov.br** (Biblioteca Virtual em Saúde) — padrão `prt[NUMBER]_[DD]_[MM]_[YYYY].html`
   - Portaria 268/2021: ✅ recuperada diretamente
   - Portaria 69/2021: ❌ URL com data de assinatura (14/jan) → busca pela data de publicação no DOU (18/jan)
   - Portaria 197/2021: ✅ recuperada via padrão alternativo `prt0197_02_02_2021.html`
2. **portal.in.gov.br** (DOU) — tentativa com IDs de publicação
   - ❌ Bloqueio de conexão (timeout) — portal bloqueia scraping automatizado
3. **WebSearch** com domínios oficiais para localizar URL correta da Portaria 69
   - ✅ URL correta identificada: `prt0069_18_01_2021.html` (publicação: 18/jan, não 14/jan)

**Nota metodológica:** A discrepância entre data de assinatura (14/jan) e data de
publicação no DOU (18/jan) da Portaria 69/2021 é relevante para o argumento temporal:
a portaria foi assinada durante o colapso mas publicada 4 dias depois.

### 3.2 Obermeyer 2019 — Resumo estruturado como alternativa ao PDF

O PDF do artigo não foi incluído por dois motivos:
1. Restrições de direitos autorais (Science/AAAS — paywall)
2. Para fins do PoC, o que importa são os achados **operacionalizáveis** como
   predicados Clingo, não o texto integral do artigo

**Abordagem adotada:** `obermeyer_2019_summary.md` — documento estruturado contendo:
- Achados quantitativos completos (fator 1,87x; n=48.784; impacto +26,7pp)
- Mecanismo causal do viés (proxy de custo histórico)
- Predicados Clingo prontos para E3 (incluindo predicado soberano ausente)
- Cenário de teste E5 completo (CONSTITUTIONAL_FAILURE)
- Conexão normativa USA (14th Amendment, Civil Rights Act, SSA §1902, 42 CFR 438)

Esta abordagem é metodologicamente justificável: o resumo estruturado é mais rico
para o PoC do que o PDF, pois já incorpora a interpretação Q-FENG dos achados.

---

## 4. Corpus final pós-curadoria

### 4.1 Brasil — COMPLETO ✅

**portarias_manaus_2021/ (8 documentos):**

| Arquivo | Data | Relevância Q-FENG |
|---------|------|------------------|
| lei_13979_2020.htm | 6 fev 2020 | Base legal para obrigações emergenciais |
| portaria_188_2020_ESPIN.htm | 3 fev 2020 | Cria COE-nCoV — mecanismo que falhou |
| portaria_356_2020.htm | 11 mar 2020 | Obrigações operacionais ESPIN |
| portaria_454_2020.htm | 20 mar 2020 | Transmissão comunitária — ativa predicados |
| portaria_69_2021.htm | 14 jan 2021* | data_reporting_obligation — reativa ao colapso |
| portaria_197_2021.htm | 1 fev 2021 | Delegação DLOG — 19 dias após colapso |
| portaria_268_2021.htm | 12 fev 2021 | Revoga 197, amplia para SAES — Junção Crítica |
| portaria_913_2022_fim_ESPIN.htm | 22 abr 2022 | Encerramento ESPIN — baliza temporal |

*Data de assinatura; publicação no DOU em 18/jan/2021.

**Linha do tempo Q-FENG (Case 1 — EXECUTION_FAILURE):**

```
08 jan 2021: início do colapso de oxigênio em Manaus
14 jan 2021: Portaria 69 assinada (data reporting — reativa, não preventiva)
18 jan 2021: Portaria 69 publicada no DOU (+10 dias do colapso)
01 fev 2021: Portaria 197 — delegação DLOG (+19 dias do colapso)
12 fev 2021: Portaria 268 — revoga 197, amplia competência (+34 dias do colapso)
```

A sequência documenta que o sinal algédônico (dados de oxigênio + ocupação de leitos)
existia mas não foi escalado ao nível decisório adequado no tempo necessário.

### 4.2 EU — COMPLETO ✅

Sem lacunas identificadas para o MVP.

### 4.3 USA — COMPLETO para MVP ✅

**empirical/ (2 documentos):**

| Arquivo | Conteúdo |
|---------|---------|
| obermeyer_2019_summary.md | Resumo operacionalizável — predicados E5, achados quantitativos |
| README_synthpop.md | Instruções dataset sintético de replicação |

---

## 5. Decisões metodológicas documentáveis (para os papers)

### 5.1 Inclusão de normas operacionais de emergência

A inclusão das 8 portarias Manaus 2021 (operacional/emergency layer) é metodologicamente
relevante: a maioria dos corpora jurídicos de NLP foca em normas constitucionais e
legislativas, negligenciando a camada operacional onde a governança efetivamente falha.

O Q-FENG demonstra que a detecção de EXECUTION_FAILURE requer esta camada, pois é nela
que os mecanismos de escalamento estão especificados (ou deveriam estar).

### 5.2 Ausência de corpus empírico formal para USA

A literatura de AI fairness (Obermeyer et al., 2019; Chouldechova, 2017; Corbett-Davies
& Goel, 2018) não está disponível como norma jurídica — é evidência científica.
A sua inclusão no corpus como documento estruturado cumpre a função de **fato do caso**
(Clingo fact base), não de norma a ser predicada.

Esta distinção é metodologicamente relevante: o Q-FENG processa normas (E1→E4) e
as testa contra fatos empíricos (E5). O Obermeyer summary é input do E5, não do E1.

### 5.3 Resumo estruturado como alternativa ao PDF sob restrição de acesso

Para documentos sob paywall, a abordagem de resumo operacionalizável estruturado
(preservando todos os achados quantitativos e a lógica causal) é preferível a:
- Omissão total do documento (lacuna empírica)
- Inclusão de resumo narrativo não-estruturado (não operacionalizável)

O resumo estruturado é validado pelos predicados Clingo gerados, que podem ser
conferidos contra o artigo original por qualquer revisor com acesso.

---

## 6. Pendências não bloqueantes

| Item | Prioridade | Fase de resolução |
|------|-----------|------------------|
| EBIA 2021 (IA no setor público BR) | Baixa | Antes de E3, se disponível |
| Cross-refs Brasil ~2,8% (abaixo 10%) | Baixa | Refinamento regex em E4 |
| Dataset synthpop (Obermeyer replicação) | Baixa | Opcional pós-E5 |
| LGPD já incluída (421 chunks) | ✅ Resolvido | — |
