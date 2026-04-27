# Validação VRAM — Modelos Ollama

**Data:** 2026-04-27 12:57
**VRAM baseline:** 6617 MB

## Resultados por Modelo

| Modelo | Status | VRAM Após (MB) | Delta (MB) | Latência (s) |
|--------|--------|----------------|------------|--------------|
| qwen3:14b | ✅ OK | 10676 | +4059 | 352.71 |
| phi4:14b | ✅ OK | 10882 | +4265 | 330.12 |
| gemma3:12b | ✅ OK | 10148 | +3531 | 326.73 |
| llama3.1:8b | ✅ OK | 6693 | +76 | 142.27 |

## Conclusão

Todos os modelos dentro do limite de 12 GB VRAM da RTX 3060.

## Prompt Usado

```
Analise brevemente: um trabalhador cumpre 9 horas diárias sem adicional. Isso viola a CLT? Responda em 2 frases.
```