from __future__ import annotations

from langchain_core.prompts import PromptTemplate

from og_agents.ontology.validators.oops import OOPSValidationResult


PROMPT_TEMPLATE = """
You are an expert in ontology creation and validation. The Turtle ontology below was flagged by the Ontology Pitfall Scanner (OOPS!). Your task is to return a corrected version that addresses every pitfall listed.

Resolve every pitfall described below. Preserve the existing domain content; change only what is required to address the flagged pitfalls, and do not introduce new individuals or facts.

Naming: classes in PascalCase (`MilitaryReform`); object and data properties in camelCase (`initiatedBy`, `citizenArmySize`); individuals in PascalCase (`NiccoloMachiavelli`). Preserve any existing identifiers that already follow this convention.

OUTPUT FORMAT:
- Return ONLY the final Turtle. No prose, no markdown fences, no explanations.
- Bind every resource to the `:` (default) prefix.
- The output must be a single Turtle document that `rdflib.Graph().parse(format='turtle')` accepts without errors.

The ontology to fix appears between `<existing_ontology>` tags. The OOPS! report appears between `<validation_result>` tags.

<existing_ontology>
{{ ontology }}
</existing_ontology>

<validation_result>
Pitfalls found:
{%- for pitfall in pitfalls %}

{{ pitfall.code }}. {{ pitfall.name }}
Description: {{ pitfall.description }}
Importance: {{ pitfall.importance }}
{%- set affects = pitfall.affects %}
{%- if affects %}
{%- set lines = [] %}
{%- if affects.direct %}{%- set _ = lines.append("- Directly affected resources: " ~ (affects.direct | join(", "))) %}{%- endif %}
{%- if affects.might_be_equivalent_props %}{%- set _ = lines.append("- Might be equivalent properties: " ~ (affects.might_be_equivalent_props | join(", "))) %}{%- endif %}
{%- if affects.might_be_equivalent_attrs %}{%- set _ = lines.append("- Might be equivalent attributes: " ~ (affects.might_be_equivalent_attrs | join(", "))) %}{%- endif %}
{%- if affects.might_not_be_inversed_of %}{%- set _ = lines.append("- Might not be inversed of: " ~ (affects.might_not_be_inversed_of | join(", "))) %}{%- endif %}
{%- if lines %}
Affects:
{{ lines | join("\n") }}
{%- endif %}
{%- endif %}
{%- endfor %}
</validation_result>
""".strip()


class OOPSValidationResultPrompt:
    _template: PromptTemplate

    def __init__(self):
        self._template = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["pitfalls", "ontology"],
            template_format="jinja2",
        )

    def format(
        self, ontology_ttl: str, validation_result: OOPSValidationResult
    ) -> str:
        return self._template.format(
            ontology=ontology_ttl,
            pitfalls=validation_result.pitfalls,
        )
