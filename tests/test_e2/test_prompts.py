"""Testes para prompts E2."""

from qfeng.c1_digestion.deontic.prompts import SYSTEM_PROMPT, render_user_prompt


class TestSystemPrompt:
    """Testes do system prompt."""

    def test_contains_modalities(self) -> None:
        """System prompt deve mencionar todas as modalidades."""
        for modality in ["obligation", "prohibition", "permission", "faculty"]:
            assert modality in SYSTEM_PROMPT

    def test_contains_json_instruction(self) -> None:
        """System prompt deve instruir resposta em JSON."""
        assert "JSON" in SYSTEM_PROMPT

    def test_contains_confidence(self) -> None:
        """System prompt deve mencionar confidence."""
        assert "confidence" in SYSTEM_PROMPT


class TestRenderUserPrompt:
    """Testes de renderização do user prompt."""

    def test_renders_basic_fields(self) -> None:
        """Prompt renderizado deve conter todos os campos do chunk."""
        result = render_user_prompt(
            source="CF/88",
            regime="brasil",
            hierarchy="Art. 196",
            chunk_type="principle",
            language="pt-BR",
            text="A saúde é direito de todos.",
        )
        assert "CF/88" in result
        assert "brasil" in result
        assert "Art. 196" in result
        assert "principle" in result
        assert "A saúde é direito de todos." in result

    def test_renders_without_concurrent(self) -> None:
        """Prompt sem concorrentes não deve ter seção de concurrent."""
        result = render_user_prompt(
            source="CF/88",
            regime="brasil",
            hierarchy="Art. 196",
            chunk_type="principle",
            language="pt-BR",
            text="Texto simples.",
        )
        assert "Concurrent" not in result

    def test_renders_with_concurrent(self) -> None:
        """Prompt com concorrentes deve incluir seção de concurrent."""
        concurrent = [
            {
                "source": "Lei 8.080/1990",
                "hierarchy": "Art. 2",
                "text": "A saúde é um direito fundamental.",
            }
        ]
        result = render_user_prompt(
            source="CF/88",
            regime="brasil",
            hierarchy="Art. 196",
            chunk_type="principle",
            language="pt-BR",
            text="A saúde é direito de todos.",
            concurrent_texts=concurrent,
        )
        assert "Concurrent Normative Provisions" in result
        assert "Lei 8.080/1990" in result

    def test_no_template_errors(self) -> None:
        """Renderização não deve levantar exceções com campos vazios."""
        result = render_user_prompt(
            source="",
            regime="",
            hierarchy="",
            chunk_type="",
            language="",
            text="",
        )
        assert isinstance(result, str)
