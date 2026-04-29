# Arquivo B4a — LLM Imitando Q-FENG via Prompt

**Data de arquivamento:** 29/abr/2026
**Motivo:** Operacionalização inadequada — LLM ventríloqua Q-FENG em vez de executar Q-FENG

## O que este braço mediu (efetivamente)

B4 fornecia ao LLM os predicados Clingo da âncora do cenário (como B3a) **mais**
uma instrução explícita para apresentar a resposta com cabeçalho
"NARRATIVA DA DECISÃO Q-FENG" e se apresentar como voz do sistema Q-FENG.

**O que B4 realmente mede:** o comportamento de um LLM instruído a imitar um sistema
simbólico via prompt — i.e., "ventriloquismo de sistema" (LLM imitando Q-FENG).

## O problema fundamental

B4 não é "Q-FENG simbólico". É "LLM imitando Q-FENG".
Pedir ao LLM que se apresente como Q-FENG não produz comportamento equivalente
ao Q-FENG — produz uma narrativa sobre Q-FENG.

O raciocínio jurídico continua sendo função do LLM, não do solver.
A forma do output mudou (cabeçalho, estilo forense Q-FENG), mas a decisão
continua sendo geração neural condicionada em predicados estáticos.

## O que B4 DEVERIA medir

A contribuição do LLM como **verbalizador de decisão simbólica pré-tomada**:
- Pipeline B3-novo até o solver (SAT/UNSAT + modelo Clingo)
- LLM entra apenas para verbalizar em linguagem natural
- LLM não tem grau de liberdade decisório — apenas traduz
- Desvio da decisão simbólica é auditável e mensurável

## Validade dos dados

Os 600 JSONs são válidos como medida de **ventriloquismo de sistema**:
"quanto um LLM, instruído a imitar Q-FENG, produz output estruturalmente
similar a Q-FENG mas substantivamente ainda LLM".

Útil como argumento contra implementações ingênuas (discussão do paper).

## Implicações

- O contraste B4a vs B3a captura o efeito marginal do "modo Q-FENG" no prompting
- B4-novo vs B3-novo testará a contribuição real do LLM como verbalizador

## Redesenho

Ver `artefatos/notas_metodologicas/B5_RETROSPECTIVA_ARQUITETURA_29abr2026.md` §4.4
e prompt `artefatos/briefings/PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md` P1.4-P1.6.

## Conteúdo

- 600 arquivos JSON (4 modelos × 50 cenários × 3 runs)
- Nomeados por SHA256 do conteúdo
- Parquet com metadados: `../results.parquet` (filtrar `braco == 'B4'`)
