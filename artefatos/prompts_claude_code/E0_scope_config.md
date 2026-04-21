# Prompt E0 — Scope Configuration
## MODULE 0: `src/qfeng/c1_digestion/scope/`
## PRÉ-REQUISITO de todos os módulos — implementar primeiro

---

```
Leia CLAUDE.md seção "MODULE 0: E0 — Scope Configuration" completa antes de começar.

TAREFA: Implementar o módulo E0 — ScopeConfig.

Criar a seguinte estrutura:
src/qfeng/c1_digestion/scope/
  __init__.py
  config.py          ← ScopeConfig dataclass + funções loader e filter_corpus
  profiles/
    sus_validacao.yaml    ← perfil MVP (conteúdo exato no CLAUDE.md)
    direito_civil.yaml    ← placeholder comentado

REGRAS OBRIGATÓRIAS:
- Usar Python 3.11+ com type hints em tudo
- Usar @dataclass (não Pydantic) para ScopeConfig — é configuração, não schema de dados
- NÃO modificar schemas.py nem interference.py
- NÃO importar de módulos E1–E5 (E0 não depende de nada além de stdlib + pathlib)
- Usar rich.console.Console para logs (nunca print())
- UTF-8 em tudo, diacríticos PT obrigatórios nos comentários e strings

FUNÇÕES OBRIGATÓRIAS em config.py:
1. load_scope(path: Path) -> ScopeConfig
   - Carrega YAML com pyyaml
   - Valida campos obrigatórios (lança ValueError se ausente)
   - Converte regimes para enum NormativeRegime (importar de core.schemas)

2. filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]
   - Usa scope.documents {regime: [glob_patterns]} para filtrar
   - Retorna lista de Path absolutos dos arquivos que correspondem
   - Ordena por regime depois por nome
   - Loga (rich) quantos arquivos encontrados por regime

TESTES a criar em tests/test_e0/:
- test_scope_loader.py: carregar sus_validacao.yaml, assert todos os campos
- test_filter_corpus.py: mock corpus_dir com 20 arquivos, scope filtra subset correto
- test_validation.py: YAML sem campo obrigatório lança ValueError

SEQUÊNCIA:
1. Criar estrutura de pastas
2. Implementar config.py
3. Criar sus_validacao.yaml (conteúdo exato do CLAUDE.md)
4. Criar testes
5. Rodar: pytest tests/test_e0/ -v
6. Reportar resultado — aguardar aprovação antes de qualquer outra coisa

FASE B (só após pytest verde E aprovação do usuário):
Rodar filter_corpus() contra o corpus real:
  python -c "
  from pathlib import Path
  from qfeng.c1_digestion.scope.config import load_scope, filter_corpus
  scope = load_scope(Path('src/qfeng/c1_digestion/scope/profiles/sus_validacao.yaml'))
  files = filter_corpus(Path('corpora'), scope)
  for f in files: print(f.relative_to(Path('corpora')))
  print(f'Total: {len(files)} arquivos')
  "
Reportar output completo. Usuário valida se os arquivos são os esperados.
```

---

## Contexto teórico (por que E0 importa)

O ScopeConfig torna o Q-FENG **reutilizável em qualquer domínio** sem reprocessar o corpus inteiro. Um deployment de direito civil usaria um perfil diferente — mesma arquitetura, novo `ScopeConfig`. Isso é central para a afirmação de generalidade do WP (Seção 3.1).

## Critério de aprovação da Fase B

- [ ] filter_corpus() retorna exatamente os documentos esperados para sus_validacao
- [ ] Nenhum arquivo de regime incorreto incluído
- [ ] Log rico com contagem por regime
- [ ] Usuário diz **"pode avançar para E1"**
