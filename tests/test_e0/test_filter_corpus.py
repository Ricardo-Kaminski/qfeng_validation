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
