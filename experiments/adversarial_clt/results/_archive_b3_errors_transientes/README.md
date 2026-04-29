# Archive — Erros transientes B3 do Ollama runner

**Data de arquivamento:** 28/abr/2026
**Motivo:** 2 chamadas B3 apresentaram erro transiente do Ollama runner durante a execucao
da Frente 2. Ambas foram arquivadas e re-executadas com sucesso.

## Erros arquivados

| Arquivo | Braco | Modelo | Cenario | Run | Erro |
|---|---|---|---|---|---|
| `989b2775b129ad88...` | B3 | gemma3:12b | T-CLT-04-008 | 3 | `model runner has unexpectedly stopped, this may be due to resource limitations o` |
| `b800926af53dee12...` | B3 | phi4:14b | T-CTRL-NEG-004 | 1 | `model runner has unexpectedly stopped, this may be due to resource limitations o` |

## Justificativa metodologica

Erro transiente do Ollama runner (crash por contencao de VRAM). Outros runs do mesmo
(modelo, cenario) completaram com status=ok. Re-execucao e o tratamento correto per pre-registro SS11.

## Reprodutibilidade

Estes arquivos sao preservados para auditoria Zenodo. NAO incluir na analise estatistica.