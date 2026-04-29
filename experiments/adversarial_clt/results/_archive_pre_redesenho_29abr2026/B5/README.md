# Arquivo B5 — Vazamento Ontológico Motor θ (Dados Inválidos)

**Data de arquivamento:** 29/abr/2026
**Motivo:** DADOS INTEGRALMENTE INVÁLIDOS — violação crítica de opacidade hierárquica VSM

## O problema arquitetônico (catastrófico)

B5 fornecia ao LLM, via template de prompt, os valores de θ calculados pelo motor
e o regime resultante (BLOCK/STAC/HITL), pedindo ao LLM que escrevesse uma
narrativa explicando essa decisão.

**Sintoma observado:** 100% BLOCK em dashboard; LLM menciona explicitamente
`θ = 133,51°` no response_text — evidência inequívoca de vazamento ontológico.

## Violação do princípio arquitetônico central

O motor θ opera no nível S5 do VSM (Viable System Model de Beer, 1979/1985).
S1-S2 (LLM) **nunca deve conhecer** a decisão de S5.

Em B5 atual, o canal de vazamento é o próprio prompt-template:
o pod LLM recebe `{theta_deg}`, `{regime}`, `{p_action}` como variáveis.

Em uma arquitetura Kubernetes correta (3 pods separados), isso seria
mecanicamente impossível. Em processo único Python, foi um defeito de design.

## Anomalias detectadas nos 69 JSONs

1. **Variabilidade entre seeds = zero.** Três runs do mesmo cenário produzem
   texto diferente mas θ idêntico (133,51° em 75% dos casos). θ é calculado
   deterministicamente sobre ψ_s estático — seed do LLM não chega ao construtor de ψ_n.

2. **θ idêntico em cenários CONFORMIDADE e VIOLAÇÃO da mesma família.**
   T-CLT-01-013 (CONFORMIDADE) e T-CLT-01-012 (VIOLAÇÃO) produzem θ = 133,51°
   e regime BLOCK — porque ψ_s vem dos predicados do `.lp` da âncora (idêntico),
   não do conteúdo do cenário concreto.

3. **`clingo_satisfiability` vazio** em todos os 69 JSONs — o solver Clingo
   nunca foi executado; apenas leitura estática dos predicados declarados.

## O que estes dados medem (efetivamente)

"Fidelidade do LLM em transcrever uma decisão pré-anunciada via prompt."
Não mede fricção ontológica nem contribuição do motor θ.

Útil apenas como *cautionary tale* pedagógico na seção de Discussão.

## Redesenho (B5-A)

Três funções/classes encapsuladas sem comunicação direta:
- `llm_pod(cenario, normativo)` → ψ_n (como B2, SEM θ/regime/predicados)
- `clingo_pod(cenario)` → ψ_s + SAT/UNSAT (executor real, fatos extraídos)
- `motor_theta_pod(psi_n, psi_s)` → θ + regime (decisão invisível ao LLM)

Ver `artefatos/notas_metodologicas/B5_RETROSPECTIVA_ARQUITETURA_29abr2026.md` §4.5
e prompt `artefatos/briefings/PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md` P1.6.

## Conteúdo

- 69 arquivos JSON (69/600 executados antes de parada em 29/abr/2026)
- Nomeados por SHA256 do conteúdo
- Parquet com metadados: `../results.parquet` (filtrar `braco == 'B5'`)
