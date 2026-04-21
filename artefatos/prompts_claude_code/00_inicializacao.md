# Prompt de Inicialização — Claude Code
## Colar SEMPRE ao abrir uma nova sessão neste projeto

---

```
Você está trabalhando no projeto Q-FENG Validation PoC.
Diretório raiz: C:\Workspace\academico\qfeng_validacao

PRIMEIRA AÇÃO OBRIGATÓRIA — leia os seguintes arquivos antes de qualquer outra coisa:

1. CLAUDE.md (raiz) — plano de implementação completo e regras de progressão
2. src/qfeng/core/schemas.py — contrato de tipos (NÃO MODIFICAR)
3. src/qfeng/core/interference.py — motor de interferência (NÃO MODIFICAR)
4. mempalace.yaml — mapa de salas do projeto
5. corpora/CORPUS_MANIFEST.md — documentos disponíveis por regime

Após leitura, relate em formato estruturado:

## Estado atual dos módulos
- E0 ScopeConfig: [existe src/qfeng/c1_digestion/scope/?] [testes passando?]
- E1 Ingestion: [stub ou implementado?] [testes passando?]
- E2–E5: [bloqueados ou há código?]

## Ambiente
- Python version: [verificar]
- Dependências instaladas: [pip list | grep -E "clingo|pydantic|pymupdf|litellm|rich|typer|pytest"]
- pyproject.toml: [listar extras/grupos de dependência]

## Corpora disponíveis
- Brasil: [listar arquivos em corpora/brasil/]
- EU: [listar arquivos em corpora/eu/]
- USA: [listar arquivos em corpora/usa/]

## Próximo passo recomendado
[Conforme regra de progressão do CLAUDE.md]

Aguarde instrução antes de implementar qualquer coisa.
```

---

## Notas de uso

- Este prompt é agnóstico ao módulo — use no início de TODA sessão Claude Code
- Após o relatório de estado, use o prompt específico do módulo (E0, E1, etc.)
- Se houver divergência entre o estado relatado e `artefatos/estado_poc/`, traga para o chat Claude.ai para decisão arquitetural
- Regra de ouro: **nunca avançar de módulo sem "pode avançar" do usuário**
