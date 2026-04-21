# Prompt E1 — Ingestion
## MODULE 1: `src/qfeng/c1_digestion/ingestion/`
## PRÉ-REQUISITO: E0 concluído e aprovado (Fase A + Fase B)

---

```
Leia CLAUDE.md seção "MODULE 1: E1 — Ingestion" completa antes de começar.
Confirme que E0 está aprovado antes de prosseguir.

TAREFA: Implementar o módulo E1 — Ingestion completa.

Criar:
src/qfeng/c1_digestion/ingestion/
  __init__.py
  parser.py      ← parse_document: Path → list[NormChunk]
  chunker.py     ← chunk_by_hierarchy: text → list[NormChunk]
  registry.py    ← REGIME_CONFIGS: padrões regex por regime
  runner.py      ← run_e1_batch: corpus + scope → outputs/e1_chunks/

REGRAS OBRIGATÓRIAS:
- NÃO modificar schemas.py — NormChunk é o tipo de saída, imutável
- concurrency_map.json é EXTERNO ao NormChunk — ver CLAUDE.md seção Arquitetura
- IDs determinísticos: sha256(f"{source}:{hierarchy_path}")[:16]
- UTF-8 em tudo; diacríticos PT em logs e comentários
- Usar rich para progresso (rich.progress.Progress para batch)
- Nunca print() — apenas rich ou logging

PARSER (parser.py):
- parse_document(path: Path, regime: NormativeRegime) -> list[NormChunk]
- HTML → BeautifulSoup + lxml: strip de nav, footer, script, style antes de parsear
- PDF → PyMuPDF (fitz): extrair texto página a página
- Preservar marcadores estruturais: números de artigos, cabeçalhos de seção
- Retornar texto bruto estruturado (não chunks ainda — chunker faz isso)

CHUNKER (chunker.py):
- chunk_by_hierarchy(raw_text, regime, scope: ScopeConfig) -> list[NormChunk]
- Hierarquias por regime (CRÍTICO — seguir exatamente):
  Brasil: Art. N → § N / Parágrafo único → I, II, III → a), b)
  USA: Section NNNN → (a)(1) → (A)(i)
  EU: Article N → N. → (a)
- Respeitar scope.hierarchy_depth (não ir além do nível configurado)
- Respeitar scope.chunk_types (descartar tipos fora do escopo)
- Respeitar scope.min_chunk_chars (descartar chunks curtos — ruído)
- Detectar cross_references: "nos termos do art. X", "pursuant to Section Y"
- chunk_type inferido por heurística: obligation/principle/sanction/definition

REGISTRY (registry.py):
- REGIME_CONFIGS: dict[NormativeRegime, dict] com padrões regex por regime
- Centraliza todos os padrões de parsing — parser.py e chunker.py importam daqui
- Facilita adicionar novos regimes sem modificar lógica

RUNNER (runner.py):
- run_e1_batch(corpus_dir, scope: ScopeConfig, output_dir) -> E1BatchResult
- Usa filter_corpus() do E0 para obter lista de arquivos
- Para cada arquivo: parse_document() → chunk_by_hierarchy()
- Salva outputs/e1_chunks/{regime}/{stem}.json (lista de NormChunk serializados)
- Gera outputs/e1_chunks/concurrency_map.json
  Algoritmo: dois chunks são concorrentes se mesmo chunk_type + mesmo agent +
  action semanticamente similar (comparação de tokens, threshold jaccard >= 0.6)
- Gera outputs/e1_chunks/e1_report.md com:
  - Total chunks por regime/documento
  - Distribuição de chunk_type
  - Referências cruzadas detectadas
  - Pares no concurrency_map
  - Alertas de qualidade (chunks vazios, hierarquias quebradas)

TESTES (tests/test_e1/):
- test_parser.py: parsear lei_8080_1990.htm, ssa_title_xix.htm, eu_ai_act.htm
  → assert chunks não vazios, IDs únicos, regime correto
- test_chunker.py: texto sintético de 10 artigos → assert hierarquia correta
- test_concurrency_map.py: dois chunks artificialmente similares → assert detectados
- test_runner_dry.py: rodar com scope minimal (2 documentos) → assert outputs criados

SEQUÊNCIA:
1. Implementar registry.py primeiro (regex de hierarquia)
2. Implementar parser.py
3. Implementar chunker.py
4. Implementar runner.py
5. Criar testes
6. Rodar: pytest tests/test_e1/ -v
7. Reportar — aguardar aprovação

FASE B — Execução real:
python -m qfeng.c1_digestion.ingestion.runner \
    --corpus-dir corpora/ \
    --scope src/qfeng/c1_digestion/scope/profiles/sus_validacao.yaml \
    --output-dir outputs/e1_chunks/

Critérios de aprovação (reportar para o usuário validar):
- Brasil: >= 500 chunks
- EU: >= 300 chunks
- USA: >= 400 chunks
- Amostra de 5 chunks por regime com hierarquia plausível
- concurrency_map.json com pelo menos 1 par real identificado
- e1_report.md sem alertas CRITICAL
```

---

## Nota arquitetural importante

O `concurrency_map.json` externo é uma decisão deliberada para preservar o contrato de `schemas.py`. Não adicionar `concurrent_with` ao `NormChunk` — a relação é entre chunks, não propriedade de um chunk. Isso é discutido no WP Q-FENG Seção 3.2 (relações normativas como tensões externas ao predicado individual).

## Critério de aprovação da Fase B

- [ ] Contagens de chunks plausíveis por regime
- [ ] Hierarquias corretas em amostra validada pelo usuário
- [ ] concurrency_map identifica sobreposições normativas reais conhecidas (ex: art. 196 CF/88 e art. 2 Lei 8.080/90 sobre universalidade)
- [ ] e1_report.md sem alertas críticos
- [ ] Usuário diz **"pode avançar para E2"**
