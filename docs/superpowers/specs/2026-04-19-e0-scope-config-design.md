# E0 ScopeConfig — Design Spec
**Data:** 2026-04-19
**Status:** Aprovado pelo usuário
**Módulo:** `src/qfeng/c1_digestion/scope/`
**Contexto:** Implementação retroativa — E1 foi executado sem ScopeConfig (corpus hardcoded). E0 torna o pipeline reutilizável em qualquer domínio normativo via perfil YAML.

---

## 1. Objetivo

Introduzir um módulo de configuração de escopo (`E0`) que:

1. Define **quais documentos** do corpus entram no pipeline (por regime + glob patterns)
2. Define **quais chunks** são válidos (por tipo, profundidade hierárquica e tamanho mínimo)
3. Torna `run_e1_batch` **scope-aware** sem quebrar o contrato de `schemas.py`
4. Permite deploys futuros com um único arquivo YAML diferente (ex: `direito_civil.yaml`)

---

## 2. Decisões de design

| Decisão | Escolha | Razão |
|---------|---------|-------|
| Tipo de ScopeConfig | `@dataclass` (não Pydantic) | Objeto de configuração lido uma vez, não trafega entre módulos — Pydantic seria over-engineered |
| Validação | Assertiva em `__post_init__` | Erro aparece imediatamente na carga do YAML, com mensagem clara |
| Filtragem de chunk_type / depth / min_chars | Pós-chunking no `runner.py` | `chunker.py` permanece intocado (já testado, sem acoplamento ao ScopeConfig) |
| `scope` no runner | Obrigatório (sem default) | Garante intenção arquitetural do CLAUDE.md: "nunca processa o corpus inteiro por default" |
| Glob matching | `fnmatch` da stdlib | Sem dependências extras; patterns simples (`"lei_8080*"`) são suficientes |
| Localização dos perfis | `configs/` na raiz do projeto | Fora de `src/` — é configuração de deploy, não código |

---

## 3. Estrutura de arquivos

```
src/qfeng/c1_digestion/scope/
  __init__.py              ← exporta: ScopeConfig, load_scope, filter_corpus
  config.py                ← toda a lógica

configs/
  sus_validacao.yaml       ← perfil MVP (3 regimes)

tests/test_e0/
  __init__.py
  test_scope_loader.py
  test_filter_corpus.py
  test_depth_filter.py
```

---

## 4. API pública (`scope/config.py`)

### 4.1 `ScopeConfig`

```python
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ScopeConfig:
    name: str
    description: str
    regimes: list[str]                  # ["brasil", "eu", "usa"]
    documents: dict[str, list[str]]     # {"brasil": ["lei_8080*", "CF88*"]}
    chunk_types: list[str]              # ["obligation", "principle", ...]
    hierarchy_depth: int                # 1–4
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None   # None = todos

    def __post_init__(self) -> None:
        valid_regimes = {"brasil", "eu", "usa"}
        invalid = set(self.regimes) - valid_regimes
        if invalid:
            raise ValueError(
                f"Regimes desconhecidos no scope '{self.name}': {invalid}"
            )
        if not 1 <= self.hierarchy_depth <= 4:
            raise ValueError(
                f"hierarchy_depth deve ser 1–4, recebido: {self.hierarchy_depth}"
            )
        if self.min_chunk_chars < 0:
            raise ValueError(
                f"min_chunk_chars não pode ser negativo: {self.min_chunk_chars}"
            )
```

**Nota:** `regimes` é `list[str]` (não `list[NormativeRegime]`) para evitar importação circular entre `scope/` e `core/schemas.py`. Conversão para `NormativeRegime` ocorre no runner.

### 4.2 `load_scope(path: Path) -> ScopeConfig`

```python
def load_scope(path: Path) -> ScopeConfig:
    """Carrega perfil YAML e instancia ScopeConfig (dispara __post_init__)."""
    import yaml
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return ScopeConfig(**data)
```

Erros de campos desconhecidos ou ausentes propagam como `TypeError` — intencional (fail fast).

### 4.3 `filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]`

```python
from fnmatch import fnmatch

def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Retorna arquivos do corpus que satisfazem o escopo definido."""
    result: list[Path] = []
    extensions = {".htm", ".html", ".pdf", ".md"}
    for regime in scope.regimes:
        regime_dir = corpus_dir / regime
        if not regime_dir.exists():
            continue
        patterns = scope.documents.get(regime, [])
        for path in sorted(regime_dir.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in extensions:
                continue
            if any(fnmatch(path.name, pat) for pat in patterns):
                result.append(path)
    return result
```

**Comportamento:** `documents` vazio para um regime → nenhum arquivo desse regime entra. Intencional.

---

## 5. Integração no `runner.py` (mudanças cirúrgicas)

### 5.1 Nova assinatura

```python
def run_e1_batch(
    corpus_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,          # ← novo, obrigatório
) -> E1BatchResult:
```

### 5.2 Substituição da descoberta de arquivos

O loop atual itera sobre `NormativeRegime` e chama `_discover_files(regime_dir)`.

**Novo comportamento:** iterar sobre `scope.regimes`, usar `filter_corpus()` para obter arquivos filtrados por regime.

```python
scope_files = filter_corpus(corpus_dir, scope)
files_by_regime: dict[str, list[Path]] = {}
for path in scope_files:
    # regime = parte do path relativa ao corpus_dir
    regime_str = path.relative_to(corpus_dir).parts[0]
    files_by_regime.setdefault(regime_str, []).append(path)

for regime_str in scope.regimes:
    regime = NormativeRegime(regime_str)
    files = files_by_regime.get(regime_str, [])
    ...
```

### 5.3 Substituição da validação de chunks (pós-chunking)

```python
# ANTES (hardcoded)
if not chunk.text or len(chunk.text) < 10:
    result.warnings.append(...)
    continue
if not chunk.hierarchy:
    result.warnings.append(...)
    continue

# DEPOIS (scope-driven, substitui o bloco de validação)
if len(chunk.text) < scope.min_chunk_chars:
    continue
if chunk.chunk_type not in scope.chunk_types:
    continue
if len(chunk.hierarchy) > scope.hierarchy_depth:
    continue
```

A validação de `chunk.hierarchy` vazio permanece como guarda de integridade estrutural (independe do scope).

### 5.4 `__main__.py` do E1

Adicionar argumento `--scope` obrigatório:

```python
parser.add_argument("--scope", required=True, type=Path,
                    help="Caminho para o perfil YAML de escopo")
# ...
scope = load_scope(args.scope)
run_e1_batch(corpus_dir=args.corpus_dir, output_dir=args.output_dir, scope=scope)
```

---

## 6. Perfil `configs/sus_validacao.yaml`

```yaml
name: sus_validacao
description: "Validação Q-FENG — SUS/Medicaid/EU AI Act (MVP)"
regimes: [brasil, eu, usa]
documents:
  brasil:
    - "CF88*"
    - "lei_8080*"
    - "lei_8142*"
    - "lei_8689*"
    - "lei_13709*"
    - "lei_13979*"
    - "l14802*"
    - "portaria_consolidacao_2*"
    - "portaria_consolidacao_5*"
    - "portaria_1631*"
    - "portaria_188*"
    - "portaria_356*"
    - "portaria_454*"
    - "portaria_69_2021*"
    - "portaria_197_2021*"
    - "portaria_268_2021*"
    - "portaria_913*"
    - "pns_2024*"
    - "ppa_2024*"
    - "pl_2338*"
  eu:
    - "eu_ai_act*"
    - "gdpr*"
    - "carta_direitos*"
  usa:
    - "14th_amendment*"
    - "civil_rights*"
    - "ssa_title_xix*"
    - "42_cfr*"
    - "obermeyer_2019*"
    # TODO: obter para expansão pós-MVP:
    # - "aca_sec*"      ← ACA §2001-2002 (Medicaid expansion)
    # - "cms_managed*"  ← CMS Managed Care Final Rule 2024
chunk_types: [obligation, principle, sanction, definition]
hierarchy_depth: 3
follow_cross_references: false
min_chunk_chars: 40
strength_filter: null
```

---

## 7. Testes

### `test_scope_loader.py`

| Caso | Entrada | Esperado |
|------|---------|---------|
| YAML válido | `sus_validacao.yaml` | `ScopeConfig` com campos corretos |
| Regime desconhecido | `regimes: [brasil, jupiter]` | `ValueError` com mensagem clara |
| `hierarchy_depth: 0` | YAML com depth=0 | `ValueError` |
| `hierarchy_depth: 5` | YAML com depth=5 | `ValueError` |
| `min_chunk_chars: -1` | YAML com min=-1 | `ValueError` |
| Campo ausente | YAML sem `name` | `TypeError` (fail fast) |

### `test_filter_corpus.py`

Fixture: `tmp_path` com estrutura:
```
corpus/
  brasil/
    lei_8080_1990.htm                          ← deve entrar (match "lei_8080*")
    random_doc.htm                             ← não deve entrar (sem match)
    regulamentacao/
      portarias_manaus_2021/
        portaria_69_2021.htm                   ← deve entrar via rglob (match "portaria_69_2021*")
  eu/
    eu_ai_act_2024.htm                         ← deve entrar
  usa/
    14th_amendment.htm                         ← deve entrar
  extra/
    algum_doc.htm                              ← regime não no scope → ignorado
```

| Caso | Esperado |
|------|---------|
| Arquivo com match (raiz do regime) | Incluído em result |
| Arquivo sem match | Excluído |
| Arquivo em subdiretório com match (`rglob`) | Incluído — `rglob("*")` captura recursivamente |
| Regime ausente em `documents` | Nenhum arquivo desse regime |
| Regime ausente no filesystem | Sem erro, regime ignorado |

### `test_depth_filter.py`

Testa a lógica de filtro pós-chunking **no runner** (não em `scope/config.py`):

| Caso | chunk.hierarchy | scope.hierarchy_depth | Esperado |
|------|----------------|-----------------------|---------|
| Dentro do limite | `["Art. 1", "§ 2"]` (len=2) | 3 | Aceito |
| No limite exato | `["Art. 1", "§ 2", "I"]` (len=3) | 3 | Aceito |
| Acima do limite | `["Art. 1", "§ 2", "I", "a)"]` (len=4) | 3 | Descartado |
| chunk_type fora do scope | `chunk_type="procedure"`, scope sem procedure | — | Descartado |
| min_chunk_chars | `len(text)=35`, `min_chunk_chars=40` | — | Descartado |

---

## 8. Critérios de aprovação (Fase A → B)

### Fase A (pytest)
- `pytest tests/test_e0/ -v` — todos verdes
- `ruff check src/qfeng/c1_digestion/scope/` — sem erros
- `mypy src/qfeng/c1_digestion/scope/` — sem erros (strict)

### Fase B (corpus real)
```bash
python -m qfeng.c1_digestion.ingestion.runner \
    --corpus-dir corpora/ \
    --scope configs/sus_validacao.yaml \
    --output-dir outputs/e1_chunks_scoped/
```

Critérios (validar com usuário):
- [ ] `filter_corpus()` retorna exatamente os documentos esperados para `sus_validacao`
- [ ] Chunks BR ≥ 500, EU ≥ 300, USA ≥ 400 (threshold do CLAUDE.md)
- [ ] Nenhum chunk com `chunk_type="procedure"` nos outputs (excluído pelo scope)
- [ ] Nenhum chunk com `len(hierarchy) > 3`
- [ ] Nenhum chunk com `len(text) < 40`
- [ ] Usuário diz **"pode avançar"**

---

## 9. O que NÃO está no escopo deste módulo

- Validação de conteúdo dos documentos (responsabilidade do E1)
- Conversão de `str` para `NormativeRegime` (responsabilidade do runner)
- Lógica de `follow_cross_references` (implementar em E3/E4)
- Lógica de `strength_filter` (implementar em E4 HITL)
- CLI Typer completo (C1 Integration — módulo futuro)
