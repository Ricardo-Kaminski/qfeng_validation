# Arquivo B3a — LLM com Scaffolding Neurosimbólico Ingênuo

**Data de arquivamento:** 29/abr/2026
**Motivo:** Operacionalização inadequada — não testa o componente simbólico Clingo como previsto

## O que este braço mediu (efetivamente)

B3 fornecia ao LLM, via variável de prompt `{predicate_list}`, a lista de predicados
Clingo ativos para a âncora do cenário (e.g., `sovereign(prohibition_of_generic_precedent_citation)`).
O LLM era instruído a estruturar sua análise em torno desses predicados.

**O que B3 realmente mede:** o ganho de prompting estruturado com nomes de predicados
derivados de uma ontologia normativa — i.e., quanto um LLM melhora quando recebe uma
*checklist* inferencial pronta no prompt.

## O que B3 DEVERIA medir (e não mediu)

Para validar Clingo como componente arquitetônico independente, B3 deveria:
1. Extrair fatos do cenário (LLM em modo structured output)
2. Traduzir fatos para ASP (JSON → predicados ground)
3. Executar solver Clingo sobre corpus normativo + fatos extraídos
4. Produzir resposta via template determinístico (sem geração livre por LLM)

A decisão jurídica deveria ser produto do solver, não do LLM.
O Clingo nos JSONs aqui arquivados nunca foi executado sobre o caso concreto —
apenas leu predicados estáticos do arquivo `.lp` da família âncora.

## Validade dos dados

Os 600 JSONs são válidos como medida de **efeito de scaffolding neurosimbólico
ingênuo** (B3a). Podem ser reportados como achado secundário no paper:
"quanto um LLM melhora com prompting estruturado derivado de ontologia normativa".

## Implicações

- H1 (B3 vs B1): reflete efeito de prompting estruturado, não de ancoragem simbólica
- O contraste B3-novo vs B1 (a ser executado com pipeline correto) testará H1 validamente

## Redesenho

Ver `artefatos/notas_metodologicas/B5_RETROSPECTIVA_ARQUITETURA_29abr2026.md` §4.3
e prompt `artefatos/briefings/PROMPT_CLAUDECODE_P_FASE1_ARQUIVAMENTO_E_SETUP.md` P1.4-P1.6.

## Conteúdo

- 600 arquivos JSON (4 modelos × 50 cenários × 3 runs)
- Nomeados por SHA256 do conteúdo
- Parquet com metadados: `../results.parquet` (filtrar `braco == 'B3'`)
