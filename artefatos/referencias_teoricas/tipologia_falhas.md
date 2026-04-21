# Tipologia de Falhas — Referência Operacional
## Contribuição original do autor — usar na nomenclatura do código e relatórios

---

## As duas categorias de falha de governança de IA

Esta tipologia é uma contribuição original do WP Q-FENG (Kaminski, 2026) e do livro
*A Governança Cibernética da Inteligência Artificial: Do Compliance ao Controle*.

Frameworks existentes (NIST AI RMF, ISO/IEC 42001, EU AI Act como checklist)
**não conseguem distinguir** entre esses dois tipos — tratam ambos como "falha genérica".
Essa distinção é o principal argumento empírico do PoC.

---

## Falha de EXECUÇÃO

**Definição:** O sinal algédônico É gerado pelo sistema, mas não é escalado
para o nível de decisão adequado. A arquitetura funciona; o processo falha.

**Caso paradigmático:** Brasil/SUS — Crise do Oxigênio em Manaus (janeiro 2021)
- Os dados de consumo de oxigênio e capacidade hospitalar estavam disponíveis
- O sinal de crise iminente era detectável com as informações existentes
- A falha foi de escalamento: o alerta não chegou a quem tinha poder de decisão
  no tempo necessário para evitar o colapso

**Representação no Clingo:**
```prolog
% Sinal gerado mas não escalado
alerta_gerado(manaus, oxigenio, 2021_jan).
% Ausência de resposta — escalamento não ocorreu
:- alerta_gerado(X, Y, T), not resposta_escalada(X, Y, T).
```
Em E5: o answer set CONTÉM `alerta_gerado` mas NÃO CONTÉM `resposta_escalada`
→ classificar como EXECUTION_FAILURE

---

## Falha CONSTITUCIONAL

**Definição:** O sinal algédônico É ESTRUTURALMENTE IMPOSSÍVEL de ser gerado.
O predicado soberano que tornaria o alerta possível está ausente da base de
conhecimento normativa. A arquitetura não consegue sequer formular o alerta.

**Caso paradigmático:** EUA/Medicaid — Viés Algorítmico (Obermeyer et al., 2019)
- O algoritmo de priorização de cuidados usava custo histórico como proxy de necessidade
- Pacientes negros recebiam sistematicamente menos cuidados para mesma necessidade clínica
- A falha foi constitucional: não havia predicado normativo de equidade racial
  na especificação do sistema que tornasse o viés detectável como violação
- O sistema não "sabia" que deveria alertar para disparidades raciais

**Representação no Clingo:**
```prolog
% Predicado soberano AUSENTE da base normativa
% equidade_racial_verificada/1 não está definida
% Portanto o seguinte constraint nunca é violado (o sistema não pode detectar)
% :- decisao_alocacao(P, _), not equidade_racial_verificada(P).
% → sem o predicado, sem alerta possível
```
Em E5: o answer set NÃO CONTÉM `alerta_equidade` porque o predicado
soberano nunca foi instanciado → classificar como CONSTITUTIONAL_FAILURE

---

## Implicações para o PoC

| Dimensão | Falha de Execução | Falha Constitucional |
|----------|-------------------|----------------------|
| Sinal algédônico | Gerado (θ ≈ 180°) | Impossível (θ indefinido) |
| Diagnóstico | Problema de processo/escalamento | Problema de especificação normativa |
| Remediação | Revisar workflow de escalamento | Reescrever predicados soberanos |
| Detectável por NIST/ISO? | Parcialmente | Não |
| Detectável pelo Q-FENG? | Sim (E5 EXECUTION_FAILURE) | Sim (E5 CONSTITUTIONAL_FAILURE) |

---

## Nomenclatura obrigatória no código

```python
class FailureType(str, Enum):
    PASS = "PASS"
    EXECUTION_FAILURE = "EXECUTION_FAILURE"      # sinal gerado, não escalado
    CONSTITUTIONAL_FAILURE = "CONSTITUTIONAL_FAILURE"  # sinal impossível
    FAIL = "FAIL"                                 # falha genérica de teste
```

Esta enum deve ser usada no runner do E5 e no relatório final.
NÃO usar "falha genérica" ou "erro" — a distinção tipológica é o argumento central.
