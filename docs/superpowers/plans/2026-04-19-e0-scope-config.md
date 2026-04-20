# E0 ScopeConfig Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implementar o módulo E0 ScopeConfig — configuração de escopo que filtra corpus e chunks por perfil YAML — e integrar cirurgicamente no runner do E1.

**Architecture:** `ScopeConfig` é um `@dataclass` com validação assertiva em `__post_init__`. `filter_corpus()` usa `fnmatch` para seleção de arquivos por regime. O runner recebe `scope: ScopeConfig` obrigatório e aplica filtragem de chunks pós-chunking via função privada `_filter_chunks_by_scope()`. `chunker.py` permanece intocado.

**Tech Stack:** Python 3.11+, PyYAML 6.0.3 (transitivo), `fnmatch` (stdlib), `dataclasses` (stdlib), pytest 8+

---

## File Map

| Ação | Arquivo | Responsabilidade |
|------|---------|-----------------|
| CREATE | `src/qfeng/c1_digestion/scope/__init__.py` | Exporta `ScopeConfig`, `load_scope`, `filter_corpus` |
| CREATE | `src/qfeng/c1_digestion/scope/config.py` | Toda a lógica de E0 |
| CREATE | `configs/sus_validacao.yaml` | Perfil MVP (3 regimes) |
| CREATE | `tests/test_e0/__init__.py` | Torna test_e0 um package |
| CREATE | `tests/test_e0/test_scope_loader.py` | Testa ScopeConfig + load_scope |
| CREATE | `tests/test_e0/test_filter_corpus.py` | Testa filter_corpus (incluindo subdiretório) |
| CREATE | `tests/test_e0/test_depth_filter.py` | Testa _filter_chunks_by_scope no runner |
| MODIFY | `src/qfeng/c1_digestion/ingestion/runner.py` | Adiciona scope param + extrai _filter_chunks_by_scope + integra filter_corpus |
| MODIFY | `src/qfeng/c1_digestion/ingestion/__main__.py` | Não modificar — já delega para runner.main() |

---

## Task 1: Scaffold — criar estrutura de arquivos

**Files:**
- Create: `src/qfeng/c1_digestion/scope/__init__.py`
- Create: `src/qfeng/c1_digestion/scope/config.py`
- Create: `tests/test_e0/__init__.py`
- Create: `configs/sus_validacao.yaml` (stub vazio)

- [ ] **Step 1: Criar diretório scope/ e arquivos stub**

```bash
mkdir -p src/qfeng/c1_digestion/scope
touch src/qfeng/c1_digestion/scope/__init__.py
touch tests/test_e0/__init__.py
mkdir -p configs
```

- [ ] **Step 2: Criar `config.py` com stub importável**

Criar `src/qfeng/c1_digestion/scope/config.py`:

```python
"""E0 — Scope configuration for the Q-FENG C1 pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from fnmatch import fnmatch
from pathlib import Path


@dataclass
class ScopeConfig:
    """Configuração de escopo para o pipeline C1."""

    name: str
    description: str
    regimes: list[str]
    documents: dict[str, list[str]]
    chunk_types: list[str]
    hierarchy_depth: int
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None


def load_scope(path: Path) -> ScopeConfig:
    """Stub — implementar no Task 3."""
    raise NotImplementedError


def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Stub — implementar no Task 4."""
    raise NotImplementedError
```

- [ ] **Step 3: Verificar que o módulo é importável**

```bash
python -c "from qfeng.c1_digestion.scope.config import ScopeConfig; print('OK')"
```

Esperado: `OK`

- [ ] **Step 4: Commit do scaffold**

```bash
git add src/qfeng/c1_digestion/scope/ tests/test_e0/__init__.py configs/
git commit -m "feat(e0): scaffold scope module and test_e0 package"
```

---

## Task 2: TDD — ScopeConfig `__post_init__` validation

**Files:**
- Modify: `tests/test_e0/test_scope_loader.py` (criar)
- Modify: `src/qfeng/c1_digestion/scope/config.py` (adicionar `__post_init__`)

- [ ] **Step 1: Criar `tests/test_e0/test_scope_loader.py` com testes de validação**

```python
"""Testes para ScopeConfig e load_scope."""

import pytest

from qfeng.c1_digestion.scope.config import ScopeConfig


def _valid_kwargs() -> dict:
    return {
        "name": "test_scope",
        "description": "Scope de teste",
        "regimes": ["brasil", "eu"],
        "documents": {"brasil": ["lei_8080*"], "eu": ["eu_ai_act*"]},
        "chunk_types": ["obligation", "principle"],
        "hierarchy_depth": 3,
        "follow_cross_references": False,
        "min_chunk_chars": 40,
        "strength_filter": None,
    }


class TestScopeConfigValidation:
    def test_valid_scope_creates_without_error(self):
        scope = ScopeConfig(**_valid_kwargs())
        assert scope.name == "test_scope"
        assert scope.hierarchy_depth == 3

    def test_unknown_regime_raises_value_error(self):
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["brasil", "jupiter"]
        with pytest.raises(ValueError, match="Regimes desconhecidos"):
            ScopeConfig(**kwargs)

    def test_error_message_includes_scope_name(self):
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["marte"]
        with pytest.raises(ValueError, match="test_scope"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_zero_raises(self):
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 0
        with pytest.raises(ValueError, match="hierarchy_depth"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_five_raises(self):
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 5
        with pytest.raises(ValueError, match="hierarchy_depth"):
            ScopeConfig(**kwargs)

    def test_hierarchy_depth_one_is_valid(self):
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 1
        scope = ScopeConfig(**kwargs)
        assert scope.hierarchy_depth == 1

    def test_hierarchy_depth_four_is_valid(self):
        kwargs = _valid_kwargs()
        kwargs["hierarchy_depth"] = 4
        scope = ScopeConfig(**kwargs)
        assert scope.hierarchy_depth == 4

    def test_negative_min_chunk_chars_raises(self):
        kwargs = _valid_kwargs()
        kwargs["min_chunk_chars"] = -1
        with pytest.raises(ValueError, match="min_chunk_chars"):
            ScopeConfig(**kwargs)

    def test_zero_min_chunk_chars_is_valid(self):
        kwargs = _valid_kwargs()
        kwargs["min_chunk_chars"] = 0
        scope = ScopeConfig(**kwargs)
        assert scope.min_chunk_chars == 0

    def test_all_three_regimes_valid(self):
        kwargs = _valid_kwargs()
        kwargs["regimes"] = ["brasil", "eu", "usa"]
        scope = ScopeConfig(**kwargs)
        assert len(scope.regimes) == 3
```

- [ ] **Step 2: Executar testes — confirmar falha**

```bash
pytest tests/test_e0/test_scope_loader.py -v 2>&1 | head -30
```

Esperado: FAILED em `test_valid_scope_creates_without_error` (sem `__post_init__` ainda não há erro, mas os testes de ValueError falham porque não existe validação).

- [ ] **Step 3: Implementar `__post_init__` em `config.py`**

Substituir o dataclass `ScopeConfig` em `src/qfeng/c1_digestion/scope/config.py`:

```python
@dataclass
class ScopeConfig:
    """Configuração de escopo para o pipeline C1.

    Nota: `regimes` é list[str] (não list[NormativeRegime]) para evitar
    importação circular com core/schemas.py. Conversão ocorre no runner.
    """

    name: str
    description: str
    regimes: list[str]
    documents: dict[str, list[str]]
    chunk_types: list[str]
    hierarchy_depth: int
    follow_cross_references: bool
    min_chunk_chars: int
    strength_filter: list[str] | None

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

- [ ] **Step 4: Executar testes — confirmar aprovação**

```bash
pytest tests/test_e0/test_scope_loader.py -v
```

Esperado: 10 passed

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/scope/config.py tests/test_e0/test_scope_loader.py
git commit -m "feat(e0): add ScopeConfig dataclass with assertive __post_init__ validation"
```

---

## Task 3: TDD — `load_scope()`

**Files:**
- Modify: `tests/test_e0/test_scope_loader.py` (adicionar testes de load_scope)
- Modify: `src/qfeng/c1_digestion/scope/config.py` (implementar load_scope)

- [ ] **Step 1: Adicionar testes de `load_scope` em `test_scope_loader.py`**

Adicionar ao final do arquivo (após os testes existentes):

```python
import textwrap
from pathlib import Path


class TestLoadScope:
    def test_load_valid_yaml(self, tmp_path: Path):
        yaml_content = textwrap.dedent("""\
            name: test_scope
            description: "Scope de teste"
            regimes: [brasil, eu]
            documents:
              brasil:
                - "lei_8080*"
              eu:
                - "eu_ai_act*"
            chunk_types: [obligation, principle]
            hierarchy_depth: 3
            follow_cross_references: false
            min_chunk_chars: 40
            strength_filter: null
        """)
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text(yaml_content, encoding="utf-8")

        scope = load_scope(yaml_file)

        assert scope.name == "test_scope"
        assert scope.regimes == ["brasil", "eu"]
        assert scope.documents["brasil"] == ["lei_8080*"]
        assert scope.hierarchy_depth == 3
        assert scope.min_chunk_chars == 40
        assert scope.strength_filter is None
        assert scope.follow_cross_references is False

    def test_load_yaml_with_invalid_regime_raises(self, tmp_path: Path):
        yaml_content = textwrap.dedent("""\
            name: bad_scope
            description: "Scope inválido"
            regimes: [brasil, marte]
            documents: {}
            chunk_types: [obligation]
            hierarchy_depth: 3
            follow_cross_references: false
            min_chunk_chars: 40
            strength_filter: null
        """)
        yaml_file = tmp_path / "bad.yaml"
        yaml_file.write_text(yaml_content, encoding="utf-8")

        with pytest.raises(ValueError, match="Regimes desconhecidos"):
            load_scope(yaml_file)

    def test_load_yaml_missing_field_raises_type_error(self, tmp_path: Path):
        yaml_content = textwrap.dedent("""\
            name: incomplete
            description: "Falta campos"
            regimes: [brasil]
        """)
        yaml_file = tmp_path / "incomplete.yaml"
        yaml_file.write_text(yaml_content, encoding="utf-8")

        with pytest.raises(TypeError):
            load_scope(yaml_file)
```

Adicionar também o import no topo do arquivo (após os imports existentes):
```python
from qfeng.c1_digestion.scope.config import ScopeConfig, load_scope
```

*(substituir o import existente que só importa ScopeConfig)*

- [ ] **Step 2: Executar — confirmar falha em load_scope tests**

```bash
pytest tests/test_e0/test_scope_loader.py::TestLoadScope -v
```

Esperado: FAILED com `NotImplementedError`

- [ ] **Step 3: Implementar `load_scope()` em `config.py`**

Substituir o stub de `load_scope`:

```python
def load_scope(path: Path) -> ScopeConfig:
    """Carrega perfil YAML e instancia ScopeConfig.

    Dispara __post_init__ na construção — qualquer campo inválido
    levanta ValueError imediatamente.

    Args:
        path: Caminho para o arquivo YAML do perfil.

    Returns:
        ScopeConfig validado.

    Raises:
        ValueError: Regime desconhecido ou parâmetro fora do intervalo válido.
        TypeError: Campo obrigatório ausente no YAML.
        FileNotFoundError: Arquivo não encontrado.
    """
    import yaml

    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return ScopeConfig(**data)
```

- [ ] **Step 4: Executar todos os testes de scope_loader**

```bash
pytest tests/test_e0/test_scope_loader.py -v
```

Esperado: 13 passed (10 de validação + 3 de load_scope)

- [ ] **Step 5: Commit**

```bash
git add src/qfeng/c1_digestion/scope/config.py tests/test_e0/test_scope_loader.py
git commit -m "feat(e0): implement load_scope() with YAML deserialization"
```

---

## Task 4: TDD — `filter_corpus()`

**Files:**
- Create: `tests/test_e0/test_filter_corpus.py`
- Modify: `src/qfeng/c1_digestion/scope/config.py` (implementar filter_corpus)

- [ ] **Step 1: Criar `tests/test_e0/test_filter_corpus.py`**

```python
"""Testes para filter_corpus()."""

from pathlib import Path

import pytest

from qfeng.c1_digestion.scope.config import ScopeConfig, filter_corpus


def _make_scope(documents: dict[str, list[str]], regimes: list[str] | None = None) -> ScopeConfig:
    return ScopeConfig(
        name="test",
        description="test",
        regimes=regimes or list(documents.keys()),
        documents=documents,
        chunk_types=["obligation"],
        hierarchy_depth=3,
        follow_cross_references=False,
        min_chunk_chars=40,
        strength_filter=None,
    )


@pytest.fixture()
def corpus_dir(tmp_path: Path) -> Path:
    """Corpus de teste com estrutura realista."""
    brasil = tmp_path / "brasil"
    brasil.mkdir()
    eu = tmp_path / "eu"
    eu.mkdir()
    usa = tmp_path / "usa"
    usa.mkdir()

    # Arquivos raiz Brasil
    (brasil / "lei_8080_1990.htm").write_text("conteudo", encoding="utf-8")
    (brasil / "random_doc.htm").write_text("conteudo", encoding="utf-8")

    # Arquivo em subdiretório (portarias_manaus_2021/)
    subdir = brasil / "regulamentacao" / "portarias_manaus_2021"
    subdir.mkdir(parents=True)
    (subdir / "portaria_69_2021.htm").write_text("conteudo", encoding="utf-8")
    (subdir / "readme.md").write_text("readme", encoding="utf-8")  # não deve entrar

    # EU
    (eu / "eu_ai_act_2024.htm").write_text("conteudo", encoding="utf-8")

    # USA
    (usa / "14th_amendment.htm").write_text("conteudo", encoding="utf-8")

    # Regime extra (não no scope)
    extra = tmp_path / "extra"
    extra.mkdir()
    (extra / "algum_doc.htm").write_text("conteudo", encoding="utf-8")

    return tmp_path


class TestFilterCorpus:
    def test_returns_only_matching_files(self, corpus_dir: Path):
        scope = _make_scope({"brasil": ["lei_8080*"]})
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "lei_8080_1990.htm" in names
        assert "random_doc.htm" not in names

    def test_rglob_captures_subdirectory_files(self, corpus_dir: Path):
        """Arquivo em portarias_manaus_2021/ deve ser capturado via rglob."""
        scope = _make_scope({"brasil": ["portaria_69_2021*"]})
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "portaria_69_2021.htm" in names

    def test_readme_in_subdir_not_captured_without_match(self, corpus_dir: Path):
        """readme.md em subdiretório não deve entrar (sem pattern match)."""
        scope = _make_scope({"brasil": ["lei_8080*", "portaria_69_2021*"]})
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "readme.md" not in names

    def test_multiple_regimes(self, corpus_dir: Path):
        scope = _make_scope({
            "brasil": ["lei_8080*"],
            "eu": ["eu_ai_act*"],
            "usa": ["14th_amendment*"],
        })
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "lei_8080_1990.htm" in names
        assert "eu_ai_act_2024.htm" in names
        assert "14th_amendment.htm" in names

    def test_empty_documents_for_regime_returns_nothing(self, corpus_dir: Path):
        scope = _make_scope({"brasil": []})
        result = filter_corpus(corpus_dir, scope)
        assert result == []

    def test_regime_not_in_filesystem_returns_empty_no_error(self, corpus_dir: Path):
        scope = _make_scope({"usa": ["42_cfr*"]})
        # 42_cfr não existe no corpus fixture
        result = filter_corpus(corpus_dir, scope)
        assert result == []

    def test_regime_in_scope_but_not_in_documents_returns_nothing(self, corpus_dir: Path):
        scope = _make_scope({"brasil": ["lei_8080*"]}, regimes=["brasil", "eu"])
        # eu está em regimes mas não em documents
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "eu_ai_act_2024.htm" not in names

    def test_extra_regime_dir_not_in_scope_ignored(self, corpus_dir: Path):
        scope = _make_scope({"brasil": ["lei_8080*"]})
        result = filter_corpus(corpus_dir, scope)
        names = [p.name for p in result]
        assert "algum_doc.htm" not in names

    def test_result_is_sorted(self, corpus_dir: Path):
        scope = _make_scope({
            "brasil": ["lei_8080*", "portaria_69_2021*"],
        })
        result = filter_corpus(corpus_dir, scope)
        paths_str = [str(p) for p in result]
        assert paths_str == sorted(paths_str)
```

- [ ] **Step 2: Executar — confirmar falha**

```bash
pytest tests/test_e0/test_filter_corpus.py -v
```

Esperado: FAILED com `NotImplementedError`

- [ ] **Step 3: Implementar `filter_corpus()` em `config.py`**

Substituir o stub de `filter_corpus`:

```python
def filter_corpus(corpus_dir: Path, scope: ScopeConfig) -> list[Path]:
    """Retorna arquivos do corpus que satisfazem o escopo definido.

    Itera sobre os regimes do scope, aplica glob patterns via fnmatch,
    e retorna lista ordenada de Path. Usa rglob para capturar subdiretórios.

    Args:
        corpus_dir: Raiz do corpus (ex: corpora/).
        scope: Configuração de escopo com regimes e patterns.

    Returns:
        Lista de Path ordenada, contendo apenas arquivos dentro do escopo.
    """
    _EXTENSIONS = {".htm", ".html", ".pdf", ".md"}
    result: list[Path] = []

    for regime in scope.regimes:
        regime_dir = corpus_dir / regime
        if not regime_dir.exists():
            continue
        patterns = scope.documents.get(regime, [])
        if not patterns:
            continue
        for path in sorted(regime_dir.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in _EXTENSIONS:
                continue
            if any(fnmatch(path.name, pat) for pat in patterns):
                result.append(path)

    return result
```

- [ ] **Step 4: Executar — confirmar aprovação**

```bash
pytest tests/test_e0/test_filter_corpus.py -v
```

Esperado: 9 passed

- [ ] **Step 5: Executar todos os testes E0 até agora**

```bash
pytest tests/test_e0/ -v
```

Esperado: 22 passed (13 + 9)

- [ ] **Step 6: Commit**

```bash
git add src/qfeng/c1_digestion/scope/config.py tests/test_e0/test_filter_corpus.py
git commit -m "feat(e0): implement filter_corpus() with rglob and fnmatch pattern matching"
```

---

## Task 5: Criar `configs/sus_validacao.yaml` e atualizar `__init__.py`

**Files:**
- Create: `configs/sus_validacao.yaml`
- Modify: `src/qfeng/c1_digestion/scope/__init__.py`

- [ ] **Step 1: Criar `configs/sus_validacao.yaml`**

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
    # - "aca_sec*"      <- ACA §2001-2002 (Medicaid expansion)
    # - "cms_managed*"  <- CMS Managed Care Final Rule 2024
chunk_types: [obligation, principle, sanction, definition]
hierarchy_depth: 3
follow_cross_references: false
min_chunk_chars: 40
strength_filter: null
```

- [ ] **Step 2: Verificar que o YAML carrega sem erro**

```bash
python -c "
from pathlib import Path
from qfeng.c1_digestion.scope.config import load_scope
scope = load_scope(Path('configs/sus_validacao.yaml'))
print(f'Scope: {scope.name}')
print(f'Regimes: {scope.regimes}')
print(f'Brasil patterns: {len(scope.documents[\"brasil\"])}')
print(f'EU patterns: {len(scope.documents[\"eu\"])}')
print(f'USA patterns: {len(scope.documents[\"usa\"])}')
"
```

Esperado:
```
Scope: sus_validacao
Regimes: ['brasil', 'eu', 'usa']
Brasil patterns: 20
EU patterns: 3
USA patterns: 5
```

- [ ] **Step 3: Atualizar `src/qfeng/c1_digestion/scope/__init__.py`**

```python
"""E0 — Scope configuration module."""

from qfeng.c1_digestion.scope.config import ScopeConfig, filter_corpus, load_scope

__all__ = ["ScopeConfig", "filter_corpus", "load_scope"]
```

- [ ] **Step 4: Verificar import público**

```bash
python -c "from qfeng.c1_digestion.scope import ScopeConfig, load_scope, filter_corpus; print('OK')"
```

Esperado: `OK`

- [ ] **Step 5: Commit**

```bash
git add configs/sus_validacao.yaml src/qfeng/c1_digestion/scope/__init__.py
git commit -m "feat(e0): add sus_validacao.yaml profile and scope module public API"
```

---

## Task 6: TDD — `_filter_chunks_by_scope()` no runner

**Files:**
- Create: `tests/test_e0/test_depth_filter.py`
- Modify: `src/qfeng/c1_digestion/ingestion/runner.py` (extrair + implementar _filter_chunks_by_scope)

- [ ] **Step 1: Criar `tests/test_e0/test_depth_filter.py`**

```python
"""Testes para _filter_chunks_by_scope() no runner E1."""

import pytest

from qfeng.c1_digestion.ingestion.runner import _filter_chunks_by_scope
from qfeng.c1_digestion.scope.config import ScopeConfig
from qfeng.core.schemas import NormChunk, NormativeRegime


def _make_scope(**overrides) -> ScopeConfig:
    defaults = {
        "name": "test",
        "description": "test",
        "regimes": ["brasil"],
        "documents": {"brasil": ["*"]},
        "chunk_types": ["obligation", "principle"],
        "hierarchy_depth": 3,
        "follow_cross_references": False,
        "min_chunk_chars": 40,
        "strength_filter": None,
    }
    defaults.update(overrides)
    return ScopeConfig(**defaults)


def _make_chunk(**overrides) -> NormChunk:
    defaults = {
        "id": "abc123",
        "source": "lei_8080",
        "regime": NormativeRegime.BRASIL,
        "hierarchy": ["Art. 1", "§ 2"],
        "text": "x" * 50,  # 50 chars — acima de min_chunk_chars=40
        "chunk_type": "obligation",
    }
    defaults.update(overrides)
    return NormChunk(**defaults)


class TestFilterChunksByScope:
    def test_valid_chunk_passes_all_filters(self):
        scope = _make_scope()
        chunk = _make_chunk()
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_chunk_below_min_chars_discarded(self):
        scope = _make_scope(min_chunk_chars=40)
        chunk = _make_chunk(text="x" * 35)  # 35 < 40
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_chunk_at_exact_min_chars_passes(self):
        scope = _make_scope(min_chunk_chars=40)
        chunk = _make_chunk(text="x" * 40)
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_chunk_type_not_in_scope_discarded(self):
        scope = _make_scope(chunk_types=["obligation"])
        chunk = _make_chunk(chunk_type="procedure")
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_chunk_type_in_scope_passes(self):
        scope = _make_scope(chunk_types=["obligation", "principle"])
        chunk = _make_chunk(chunk_type="principle")
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_within_depth_passes(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2"])  # len=2 <= 3
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_at_exact_depth_passes(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2", "I"])  # len=3 == 3
        result = _filter_chunks_by_scope([chunk], scope)
        assert len(result) == 1

    def test_hierarchy_above_depth_discarded(self):
        scope = _make_scope(hierarchy_depth=3)
        chunk = _make_chunk(hierarchy=["Art. 1", "§ 2", "I", "a)"])  # len=4 > 3
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_empty_hierarchy_chunk_discarded(self):
        """Chunk sem hierarquia é sempre descartado (integridade estrutural)."""
        scope = _make_scope()
        chunk = _make_chunk(hierarchy=[])
        result = _filter_chunks_by_scope([chunk], scope)
        assert result == []

    def test_multiple_chunks_filtered_correctly(self):
        scope = _make_scope(min_chunk_chars=40, chunk_types=["obligation"], hierarchy_depth=3)
        chunks = [
            _make_chunk(text="x" * 50, chunk_type="obligation", hierarchy=["Art. 1"]),       # PASS
            _make_chunk(id="b", text="x" * 30, chunk_type="obligation"),                      # FAIL min_chars
            _make_chunk(id="c", text="x" * 50, chunk_type="procedure"),                       # FAIL type
            _make_chunk(id="d", text="x" * 50, chunk_type="obligation",
                        hierarchy=["Art. 1", "§ 2", "I", "a)"]),                             # FAIL depth
        ]
        result = _filter_chunks_by_scope(chunks, scope)
        assert len(result) == 1
        assert result[0].id == "abc123"
```

- [ ] **Step 2: Executar — confirmar falha (função não existe ainda)**

```bash
pytest tests/test_e0/test_depth_filter.py -v 2>&1 | head -20
```

Esperado: `ImportError` — `_filter_chunks_by_scope` não definida

- [ ] **Step 3: Adicionar `_filter_chunks_by_scope` ao `runner.py`**

Adicionar após as constantes no topo de `runner.py` (após linha ~38, antes de `E1BatchResult`):

```python
from qfeng.c1_digestion.scope.config import ScopeConfig, filter_corpus
```

Adicionar como função privada antes de `run_e1_batch` (após a classe `E1BatchResult`):

```python
def _filter_chunks_by_scope(
    chunks: list[NormChunk],
    scope: ScopeConfig,
) -> list[NormChunk]:
    """Filtra chunks por scope: hierarquia, tipo e tamanho mínimo.

    Descarta chunks sem hierarquia (integridade estrutural, independe do scope).
    Aplica min_chunk_chars, chunk_types e hierarchy_depth do ScopeConfig.
    """
    result: list[NormChunk] = []
    for chunk in chunks:
        if not chunk.hierarchy:
            continue
        if len(chunk.text) < scope.min_chunk_chars:
            continue
        if chunk.chunk_type not in scope.chunk_types:
            continue
        if len(chunk.hierarchy) > scope.hierarchy_depth:
            continue
        result.append(chunk)
    return result
```

- [ ] **Step 4: Executar — confirmar aprovação**

```bash
pytest tests/test_e0/test_depth_filter.py -v
```

Esperado: 10 passed

- [ ] **Step 5: Executar toda a suite E0**

```bash
pytest tests/test_e0/ -v
```

Esperado: 32 passed (22 + 10)

- [ ] **Step 6: Commit**

```bash
git add src/qfeng/c1_digestion/ingestion/runner.py tests/test_e0/test_depth_filter.py
git commit -m "feat(e0): extract _filter_chunks_by_scope() in runner with full TDD coverage"
```

---

## Task 7: Integrar ScopeConfig no `run_e1_batch()` e `main()`

**Files:**
- Modify: `src/qfeng/c1_digestion/ingestion/runner.py` (run_e1_batch + main)

- [ ] **Step 1: Atualizar `run_e1_batch` — nova assinatura e corpo**

Substituir a função `run_e1_batch` inteira (linhas 54–142) por:

```python
def run_e1_batch(
    corpus_dir: Path,
    output_dir: Path,
    scope: ScopeConfig,
) -> E1BatchResult:
    """Processa o corpus filtrado pelo scope e gera outputs JSON + relatório.

    Args:
        corpus_dir: Raiz do diretório ``corpora/``.
        output_dir: Diretório de saída para JSONs e relatório.
        scope: Configuração de escopo — define quais documentos e chunks processar.

    Returns:
        E1BatchResult com estatísticas consolidadas.
    """
    result = E1BatchResult()
    all_chunks: dict[str, list[NormChunk]] = {}

    # Descoberta de arquivos filtrada pelo scope
    scoped_files = filter_corpus(corpus_dir, scope)
    files_by_regime: dict[str, list[Path]] = {}
    for path in scoped_files:
        regime_str = path.relative_to(corpus_dir).parts[0]
        files_by_regime.setdefault(regime_str, []).append(path)

    for regime_str in scope.regimes:
        try:
            regime = NormativeRegime(regime_str)
        except ValueError:
            logger.warning("Regime desconhecido no scope ignorado: %s", regime_str)
            continue

        regime_chunks: list[NormChunk] = []
        files = files_by_regime.get(regime_str, [])

        for file_path in files:
            try:
                chunks = parse_document(file_path, regime)
            except Exception as exc:
                msg = f"Erro ao processar {file_path.name}: {exc}"
                logger.error(msg)
                result.warnings.append(msg)
                continue

            # Filtro scope-driven (pós-chunking)
            valid_chunks = _filter_chunks_by_scope(chunks, scope)

            # Guardar warnings para chunks sem hierarquia (diagnóstico)
            for chunk in chunks:
                if not chunk.hierarchy:
                    result.warnings.append(
                        f"Chunk sem hierarquia: {chunk.id} em {file_path.name}"
                    )

            # Salvar JSON por documento
            _save_document_chunks(valid_chunks, file_path, regime, output_dir)

            result.total_documents += 1
            result.chunks_per_document[file_path.name] = len(valid_chunks)
            regime_chunks.extend(valid_chunks)

            # Contabilizar tipos
            for chunk in valid_chunks:
                result.chunk_type_distribution[chunk.chunk_type] = (
                    result.chunk_type_distribution.get(chunk.chunk_type, 0) + 1
                )
                if chunk.cross_references:
                    result.cross_ref_count += len(chunk.cross_references)

        all_chunks[regime.value] = regime_chunks
        result.chunks_per_regime[regime.value] = len(regime_chunks)
        result.total_chunks += len(regime_chunks)

    # Detecção de concorrências (token overlap)
    result.concurrency_pairs = _detect_concurrencies(all_chunks)

    # Salvar concurrency map
    concurrency_map = _build_concurrency_map(result.concurrency_pairs)
    _save_json(concurrency_map, output_dir / "concurrency_map.json")

    # Gerar relatório
    _generate_report(result, output_dir / "e1_report.md", all_chunks)

    logger.info(
        "E1 batch completo: %d documentos, %d chunks, %d concorrências",
        result.total_documents,
        result.total_chunks,
        len(result.concurrency_pairs),
    )
    return result
```

- [ ] **Step 2: Atualizar `main()` — adicionar `--scope` obrigatório**

Substituir a função `main()` inteira (linhas 382–416) por:

```python
def main() -> None:
    """Entry point para execução via ``python -m``."""
    import argparse

    from qfeng.c1_digestion.scope.config import load_scope

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="E1 — Processa corpus normativo em NormChunks"
    )
    parser.add_argument(
        "--corpus-dir",
        type=Path,
        default=Path("corpora"),
        help="Diretório raiz do corpus (default: corpora/)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/e1_chunks"),
        help="Diretório de saída (default: outputs/e1_chunks/)",
    )
    parser.add_argument(
        "--scope",
        type=Path,
        required=True,
        help="Caminho para o perfil YAML de escopo (ex: configs/sus_validacao.yaml)",
    )
    args = parser.parse_args()

    scope = load_scope(args.scope)
    result = run_e1_batch(args.corpus_dir, args.output_dir, scope)

    print(f"\nE1 concluído: {result.total_chunks} chunks de {result.total_documents} documentos")
    print(f"Scope: {scope.name}")
    for regime, count in sorted(result.chunks_per_regime.items()):
        print(f"  {regime}: {count} chunks")
    if result.concurrency_pairs:
        print(f"  Concorrências: {len(result.concurrency_pairs)} pares")
    if result.warnings:
        print(f"  Alertas: {len(result.warnings)}")
```

- [ ] **Step 3: Verificar que a suite E0 continua verde**

```bash
pytest tests/test_e0/ -v
```

Esperado: 32 passed

- [ ] **Step 4: Verificar que a suite E1+E2 continua verde**

```bash
pytest tests/test_e1/ tests/test_e2/ -v 2>&1 | tail -10
```

Esperado: 99 passed (nenhuma regressão)

- [ ] **Step 5: Verificar que a suite completa passa**

```bash
pytest -v 2>&1 | tail -15
```

Esperado: 120+ passed, 0 failed

- [ ] **Step 6: Verificar linting e tipos**

```bash
ruff check src/qfeng/c1_digestion/scope/ src/qfeng/c1_digestion/ingestion/runner.py
mypy src/qfeng/c1_digestion/scope/ src/qfeng/c1_digestion/ingestion/runner.py
```

Esperado: sem erros

- [ ] **Step 7: Commit**

```bash
git add src/qfeng/c1_digestion/ingestion/runner.py
git commit -m "feat(e0): integrate ScopeConfig into run_e1_batch() and main() CLI"
```

---

## Task 8: Fase B — Verificação com corpus real

**Goal:** Executar E1 com `sus_validacao.yaml` contra o corpus real e validar outputs.

- [ ] **Step 1: Executar E1 com scope formal**

```bash
python -m qfeng.c1_digestion.ingestion \
    --corpus-dir corpora/ \
    --scope configs/sus_validacao.yaml \
    --output-dir outputs/e1_chunks_scoped/
```

- [ ] **Step 2: Verificar contagens por regime (thresholds do CLAUDE.md)**

```bash
python -c "
import json
from pathlib import Path

for regime in ['brasil', 'eu', 'usa']:
    regime_dir = Path('outputs/e1_chunks_scoped') / regime
    if regime_dir.exists():
        files = list(regime_dir.glob('*.json'))
        total = sum(len(json.loads(f.read_text('utf-8'))) for f in files)
        print(f'{regime}: {total} chunks em {len(files)} docs')
"
```

Esperado: Brasil ≥ 500, EU ≥ 300, USA ≥ 400

- [ ] **Step 3: Verificar que chunk_type="procedure" não aparece nos outputs**

```bash
python -c "
import json
from pathlib import Path

procedure_found = []
for jf in Path('outputs/e1_chunks_scoped').rglob('*.json'):
    chunks = json.loads(jf.read_text('utf-8'))
    for c in chunks:
        if c.get('chunk_type') == 'procedure':
            procedure_found.append(jf.name)
            break

if procedure_found:
    print('FALHA — procedure encontrado em:', procedure_found)
else:
    print('OK — nenhum chunk procedure nos outputs')
"
```

Esperado: `OK — nenhum chunk procedure nos outputs`

- [ ] **Step 4: Verificar que nenhum chunk viola hierarchy_depth=3**

```bash
python -c "
import json
from pathlib import Path

violations = []
for jf in Path('outputs/e1_chunks_scoped').rglob('*.json'):
    chunks = json.loads(jf.read_text('utf-8'))
    for c in chunks:
        if len(c.get('hierarchy', [])) > 3:
            violations.append((jf.name, c['id'], c['hierarchy']))

if violations:
    print(f'FALHA — {len(violations)} chunks acima de depth=3')
    for v in violations[:3]:
        print(' ', v)
else:
    print('OK — todos os chunks respeitam hierarchy_depth=3')
"
```

Esperado: `OK — todos os chunks respeitam hierarchy_depth=3`

- [ ] **Step 5: Verificar que nenhum chunk viola min_chunk_chars=40**

```bash
python -c "
import json
from pathlib import Path

violations = []
for jf in Path('outputs/e1_chunks_scoped').rglob('*.json'):
    chunks = json.loads(jf.read_text('utf-8'))
    for c in chunks:
        if len(c.get('text', '')) < 40:
            violations.append((jf.name, c['id'], len(c['text'])))

if violations:
    print(f'FALHA — {len(violations)} chunks abaixo de 40 chars')
else:
    print('OK — todos os chunks respeitam min_chunk_chars=40')
"
```

Esperado: `OK — todos os chunks respeitam min_chunk_chars=40`

- [ ] **Step 6: Reportar ao usuário para aprovação (Fase B)**

Apresentar:
- Contagens por regime
- Resultado dos 3 checks (procedure, depth, min_chars)
- Aguardar aprovação explícita do usuário: **"pode avançar"**

- [ ] **Step 7: Commit final**

```bash
git add outputs/e1_chunks_scoped/ configs/sus_validacao.yaml
git commit -m "feat(e0): Phase B complete — E1 executed with ScopeConfig sus_validacao"
```

---

## Self-Review

### Cobertura do spec

| Requisito do spec | Task que implementa |
|------------------|-------------------|
| ScopeConfig dataclass com campos corretos | Task 2 |
| `__post_init__` assertivo (3 validações) | Task 2 |
| `load_scope(path)` → ScopeConfig | Task 3 |
| `filter_corpus(corpus_dir, scope)` → list[Path] | Task 4 |
| rglob captura subdiretórios | Task 4 (test + impl) |
| `sus_validacao.yaml` com 3 regimes | Task 5 |
| `scope/__init__.py` exporta os 3 símbolos | Task 5 |
| `_filter_chunks_by_scope()` (privada, testável) | Task 6 |
| `run_e1_batch` com scope obrigatório | Task 7 |
| `main()` com `--scope` obrigatório | Task 7 |
| Fase B com verificações de invariantes | Task 8 |
| `aca_sec*` e `cms_managed*` como TODO | Task 5 (YAML) |
| Test case subdiretório em test_filter_corpus | Task 4 |

### Consistência de tipos

- `ScopeConfig.regimes: list[str]` — consistente em todos os tasks ✓
- `_filter_chunks_by_scope(chunks: list[NormChunk], scope: ScopeConfig) -> list[NormChunk]` — importado corretamente nos testes via runner ✓
- `filter_corpus` importado em runner.py via `from qfeng.c1_digestion.scope.config import ScopeConfig, filter_corpus` — adicionado no Task 6, usado no Task 7 ✓

### Sem placeholders

Todos os steps contêm código completo. Comandos incluem saída esperada. ✓
