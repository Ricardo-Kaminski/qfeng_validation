"""
Append uma seção corretiva ao briefing apontando que o DIAGRAM_INSERTION_PROSE.md
já existe (parcial) e o que falta nele.
"""
from pathlib import Path

PATCH = '''

---

## 9. CORREÇÃO IMPORTANTE — `DIAGRAM_INSERTION_PROSE.md` parcialmente pronto

Verificado em 24/abr/2026 às 20:58: o arquivo
`artefatos/briefings/DIAGRAM_INSERTION_PROSE.md` (4891 bytes, criado às 09:51 do
mesmo dia) JÁ CONTÉM os 5 blocos de prosa de conexão para D1–D5 (INS-1 a INS-5).

O que ESTÁ pronto:
- INS-1 a INS-5: parágrafo de prosa de conexão (texto que vai DEPOIS do parágrafo-
  âncora e ANTES do Diagram correspondente)
- Cada bloco identifica a frase-âncora pelo seu início (ex.: "This paper presents
  the Q-FENG C1 pipeline")

O que FALTA acrescentar antes da inserção via Claude Code:
- Frase-âncora COMPLETA e LITERAL (não só os primeiros termos) para uso com
  python-docx find/replace
- Caption (texto da legenda) para cada um dos 5+2 diagramas
- Texto de payoff (parágrafo a inserir DEPOIS do diagrama, quando aplicável —
  pelo menos para D2, D4 e D5)
- Blocos completos para D7 (Bn-1, Diagram6_Neurosymbolic_Thermo) e
  D8 (Bn-2, Diagram9_Equity_Map) — atualmente ausentes

Recomendação para a próxima sessão:
1. Abrir DIAGRAM_INSERTION_PROSE.md
2. Para cada bloco D1–D5: adicionar a frase-âncora literal (extraível de
  paper_dump.md no mesmo diretório), a caption, e o payoff
3. Adicionar blocos novos para D7 e D8
4. Validar contra o paper_dump.md que cada frase-âncora aparece UMA SÓ VEZ no
  paper (requisito do find/replace via python-docx)

Antes de iniciar, confirmar com Ricardo se a Via C++ (8 diagramas) ainda é a
escolhida ou se ele opta pela Via C+ (7) ou Via Mínima (5).
'''

p = Path(r"C:\Workspace\academico\qfeng_validacao\artefatos\briefings\BRIEFING_PAPER1_FIGURAS_24ABR2026.md")
existing = p.read_text(encoding="utf-8")
p.write_text(existing + PATCH, encoding="utf-8")
print("APPENDED. final size:", p.stat().st_size, "bytes")
