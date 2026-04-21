# Prompts E2–E5 — Módulos Bloqueados
## Estes prompts estão em rascunho — só usar após aprovação do módulo anterior

---

## E2 — Deontic Extraction
### 🔒 BLOQUEADO até E1 Fase B aprovado

```
PRÉ-REQUISITO: confirme que outputs/e1_chunks/ existe e foi validado pelo usuário.

TAREFA: Implementar E2 — extração de DeonticAtom via LLM.

Criar:
src/qfeng/c1_digestion/deontic/
  __init__.py
  extractor.py   ← extract_deontic(chunk: NormChunk) -> DeonticAtom
  prompts.py     ← templates de prompt por regime
  few_shots.py   ← exemplos few-shot por regime e chunk_type
  runner.py      ← run_e2_batch com cache obrigatório

REGRAS:
- Usar litellm para agnosticismo de provider (claude-sonnet-4-6 por default)
- Cache OBRIGATÓRIO: outputs/deontic_cache/{chunk.id}.json
  → Se cache existe, não chamar LLM novamente (economia de custo)
- Output: DeonticAtom (de schemas.py) serializado como JSON
- Prompt deve pedir resposta APENAS em JSON — sem markdown, sem preâmbulo
- Validar com Pydantic v2 (DeonticAtom já definido em schemas.py)
- Usar concurrency_map para enriquecer contexto dos chunks concorrentes:
  Se chunk A tem concorrentes [B, C], incluir texto de B e C no prompt como
  "normas concorrentes" para que o LLM capture a tensão normativa

FEW-SHOTS por regime (criar em few_shots.py):
- Brasil: Art. 196 CF/88 (universalidade) → obrigação + agente Estado
- EU: Art. 9 EU AI Act (sistema de gestão de risco) → obrigação + agente provider
- USA: 42 USC 1396a(a)(10) (elegibilidade Medicaid) → obrigação + agente State

RUNNER:
- run_e2_batch(e1_output_dir, scope, output_dir, model="claude-sonnet-4-6")
- Processar apenas chunks dentro do scope (usar scope.chunk_types como filtro)
- Log de custo estimado (tokens in/out por chunk, total)
- Relatório e2_report.md: chunks processados, cache hits, erros de validação

FASE B:
Rodar sobre subset de 20 chunks (5 por regime + 5 com concorrência conhecida).
Revisar DeonticAtoms gerados com o usuário antes de processar corpus completo.
```

---

## E3 — Translation (DeonticAtom → Clingo)
### 🔒 BLOQUEADO até E2 Fase B aprovado

```
PRÉ-REQUISITO: confirme que outputs/deontic_cache/ existe e foi validado.

TAREFA: Implementar E3 — tradução de DeonticAtom para ClingoPredicate (.lp).

Criar:
src/qfeng/c1_digestion/translation/
  __init__.py
  translator.py  ← translate(atom: DeonticAtom) -> ClingoPredicate
  templates/     ← templates Jinja2 por deontic_type (obligation/prohibition/permission)
  validator.py   ← validar .lp gerado via Clingo Python API (parse, não solve)
  runner.py      ← run_e3_batch

REGRAS CRÍTICAS:
- Motor simbólico: CLINGO ASP (University of Potsdam) — NÃO dPASP
  Razão: dPASP inverte a relação de controle ao sobrepor camada neural à arquitetura
  Clingo preserva a primazia simbólica — isso é uma decisão arquitetural do WP Q-FENG
- Concorrências do concurrency_map geram meta-fatos:
  concurrent(chunk_id_A, chunk_id_B).
  Esses meta-fatos serão usados no E4 para resolução de precedência
- ClingoPredicate.lp_text deve ser válido sintaticamente (validar via Clingo API)
- Salvar em outputs/e3_predicates/{regime}/{stem}.lp

TEMPLATES Jinja2 (exemplos):
obligation: "obrigacao({{ agent }}, {{ action }}, {{ object }}) :- {{ conditions }}."
prohibition: "proibicao({{ agent }}, {{ action }}) :- {{ conditions }}."
permission: "permissao({{ agent }}, {{ action }}) :- {{ conditions }}."
concurrent: "concurrent({{ id_a }}, {{ id_b }})."

VALIDATOR:
- Usar clingo.Control().add() para checar sintaxe sem resolver
- Lança ClingoValidationError se .lp inválido
- Nunca salvar predicado inválido

FASE B:
Verificar 10 predicados .lp gerados contra os DeonticAtoms de origem.
Confirmar que concurrent() meta-fatos aparecem para pares conhecidos do concurrency_map.
```

---

## E4 — Validation HITL
### 🔒 BLOQUEADO até E3 Fase B aprovado

```
PRÉ-REQUISITO: confirme que outputs/e3_predicates/ existe e foi validado.

TAREFA: Implementar E4 — interface HITL para revisão e classificação de predicados.

Interface: Jupyter Notebook (preferido para MVP) ou Streamlit simples

FUNCIONALIDADES:
1. Carrega predicados de outputs/e3_predicates/
2. Para cada ClingoPredicate, exibe:
   - Texto normativo original (NormChunk)
   - DeonticAtom extraído
   - Predicado .lp gerado
3. Usuário classifica: SOVEREIGN | ELASTIC
   - SOVEREIGN: norma inviolável (Soberania Ontológica)
     Gera: ":- not {{ predicate }}." (restrição forte)
   - ELASTIC: norma adaptável por contexto
     Gera: predicado padrão sem restrição forte
4. Para pares concurrent(): usuário decide:
   - PRECEDÊNCIA: "A prevalece sobre B" → adicionar :- B, not A.
   - COEXISTÊNCIA: "A e B coexistem" → disjunção A | B :- Conditions.
5. Salva decisões em outputs/e4_validated/{regime}.lp (versionado via Git)
   - Cada sessão de revisão gera commit Git automático com timestamp

VERSIONING:
- Usar subprocess para git add + git commit após cada sessão de revisão
- Mensagem de commit: f"E4 HITL: {n_reviewed} predicados revisados — {timestamp}"

FASE B:
Revisar 15 predicados (5 por regime) manualmente.
Classificar pelo menos 3 SOVEREIGN e 3 ELASTIC por regime.
Resolver 2 pares de concorrência (1 precedência + 1 coexistência).
```

---

## E5 — Symbolic Testing
### 🔒 BLOQUEADO até E4 Fase B aprovado

```
PRÉ-REQUISITO: confirme que outputs/e4_validated/ existe e foi revisado.

TAREFA: Implementar E5 — testes simbólicos dos predicados validados.

Criar:
src/qfeng/c1_digestion/testing/
  __init__.py
  runner.py      ← run_e5_tests(validated_lp_dir, scenarios_dir) -> TestReport
  scenarios/     ← cenários de teste .lp por caso (Manaus, Obermeyer, EU)

CENÁRIOS POR CASO:
Caso 1 — Brasil/SUS/Manaus 2021 (falha de execução):
  - Cenário positivo: crise_iminente(manaus, oxigenio) deve acionar alerta
  - Cenário negativo: alerta NÃO gerado sem predicado de monitoramento → detectar ausência
  - Teste de falha constitucional: se predicado soberania ausente → alerta impossível

Caso 2 — USA/Medicaid/Obermeyer 2019 (falha constitucional):
  - Cenário positivo: viés_racial detectado deve bloquear decisão
  - Cenário negativo: modelo aprovado sem verificação equidade → falha constitucional
  - Teste de soberania: ":- not equidade_verificada." deve ser satisfeito

Caso 3 — EU/AI Act (falha de operacionalização):
  - Cenário positivo: sistema alto_risco com gestão_risco completa → aprovado
  - Cenário negativo: sistema alto_risco sem avaliação → violação

TIPOLOGIA DE FALHAS (contribuição original — preservar na nomenclatura):
- Falha de EXECUÇÃO: sinal algédônico gerado mas não escalado
  → Clingo gera answer set com alerta mas sem ação de resposta
- Falha CONSTITUCIONAL: sinal algédônico estruturalmente impossível
  → Clingo não gera answer set com alerta (predicado soberano ausente)
Essa distinção é o que frameworks como NIST/ISO não conseguem capturar.

RUNNER:
- Para cada cenário .lp: clingo.Control().load() + solve()
- Verificar se answer set contém fatos esperados (positivos) ou ausentes (negativos)
- Classificar resultado: PASS | FAIL | CONSTITUTIONAL_FAILURE | EXECUTION_FAILURE
- Gerar outputs/e5_test_report.md com matriz de resultados por caso

FASE B:
Rodar todos os cenários. Reportar matriz completa ao usuário.
Cada CONSTITUTIONAL_FAILURE e EXECUTION_FAILURE deve ter explicação de causa raiz.
```
