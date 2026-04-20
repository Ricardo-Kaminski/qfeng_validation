"""Prompt templates for E2 deontic extraction.

Defines the system and user prompts used by the LLM to extract
Hohfeldian deontic atoms from normative text chunks.
"""

from __future__ import annotations

from jinja2 import Template

SYSTEM_PROMPT = """\
You are a legal-normative analyst specialized in deontic logic and \
Hohfeldian analysis. Your task is to extract structured deontic \
propositions from normative text.

For each normative chunk, identify ALL deontic propositions and \
return them as a JSON array. Each proposition must include:

1. **modality** — One of:
   - "obligation": a duty imposed on an agent (shall, must, deve, deverá)
   - "prohibition": a forbidden action (shall not, é vedado, proibido)
   - "permission": an allowed action (may, pode, é facultado)
   - "faculty": a discretionary power (poderá, is authorized to)

2. **agent** — Who bears the duty/right (use snake_case):
   e.g. "state", "municipality", "deployer", "provider", "developer", \
"employer", "authority", "sus_manager"

3. **patient** — Who/what is affected (use snake_case):
   e.g. "citizen", "patient", "worker", "data_subject", "ai_system", \
"child", "public"

4. **action** — The mandated/prohibited/permitted action (use snake_case):
   e.g. "provide_healthcare", "ensure_transparency", "conduct_impact_assessment"

5. **conditions** — Array of conditions that gate this proposition. \
Each condition has:
   - "variable": what is being tested (snake_case)
   - "operator": one of >, >=, <, <=, ==, !=, in
   - "value": the threshold or category

6. **threshold** — Numeric thresholds as key-value pairs, or null:
   e.g. {"fpl_percentage": "<=138", "icu_occupancy": ">0.85"}

7. **consequence** — What happens on violation, or null:
   e.g. "administrative_penalty", "mandado_seguranca", "license_revocation"

8. **temporality** — One of:
   - "unconditional": always applies
   - "when_triggered": applies when conditions are met
   - "periodic": applies on a recurring basis
   - "anticipatory": preventive/precautionary

9. **strength** — Normative hierarchy level:
   - "constitutional": fundamental law
   - "statutory": primary legislation
   - "regulatory": administrative regulation
   - "operational": operational guidelines/plans

10. **confidence** — Your confidence in the extraction (0.0–1.0). \
Use 0.9+ for clear, unambiguous propositions. Use 0.5–0.8 for \
propositions requiring interpretation. Use <0.5 for uncertain extractions.

IMPORTANT RULES:
- Return ONLY a valid JSON array of objects.
- Do NOT include any text before or after the JSON array.
- Each object must have ALL fields listed above.
- Use snake_case for all string identifiers.
- If the text contains no deontic propositions, return an empty array [].
- Preserve the normative intent precisely; do not generalize or infer \
beyond what the text states.
- Generate the MINIMUM number of DeonticAtoms that faithfully represent \
the normative content. A single sentence listing multiple agents \
(pessoas, família, empresas, sociedade) sharing the SAME obligation \
is ONE atom with agent='collective' or agent='non_state_actors' — \
NOT four separate atoms. Only split into multiple atoms when the \
chunk contains genuinely distinct normative propositions with \
different actions or patients.
"""

_USER_TEMPLATE = Template("""\
## Normative Chunk

**Source:** {{ source }}
**Regime:** {{ regime }}
**Hierarchy:** {{ hierarchy }}
**Chunk Type:** {{ chunk_type }}
**Language:** {{ language }}

### Text
{{ text }}

{% if concurrent_texts %}
### Concurrent Normative Provisions
The following provisions from other sources regulate the same domain. \
Consider them for context but extract atoms ONLY from the main text above.

{% for ct in concurrent_texts %}
- **{{ ct.source }}** ({{ ct.hierarchy }}): {{ ct.text[:200] }}...
{% endfor %}
{% endif %}

### Instructions
Extract all deontic propositions from the **Text** section above.
Return a JSON array of objects with fields: modality, agent, patient, \
action, conditions, threshold, consequence, temporality, strength, confidence.
""")


def render_user_prompt(
    source: str,
    regime: str,
    hierarchy: str,
    chunk_type: str,
    language: str,
    text: str,
    concurrent_texts: list[dict[str, str]] | None = None,
) -> str:
    """Renderiza o prompt de usuário com os dados do chunk.

    Args:
        source: Nome-fonte do documento.
        regime: Regime normativo.
        hierarchy: Caminho hierárquico formatado.
        chunk_type: Tipo do chunk (obligation, definition, etc.).
        language: Idioma do texto.
        text: Texto normativo do chunk.
        concurrent_texts: Textos concorrentes para contexto (opcional).

    Returns:
        Prompt renderizado pronto para envio ao LLM.
    """
    return _USER_TEMPLATE.render(
        source=source,
        regime=regime,
        hierarchy=hierarchy,
        chunk_type=chunk_type,
        language=language,
        text=text,
        concurrent_texts=concurrent_texts or [],
    )
