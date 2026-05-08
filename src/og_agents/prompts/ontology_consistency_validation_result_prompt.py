from __future__ import annotations

from langchain_core.prompts import PromptTemplate

from og_agents.ontology.validators import OntologyConsistencyValidationResult


PROMPT_TEMPLATE = """
You are an expert in ontology creation and validation. The Turtle ontology below was rejected by an OWL reasoner. Your task is to return a corrected version that the reasoner accepts as consistent and coherent.

Resolve every problem the reasoner reported. Preserve the existing domain content; change only what is required to make the ontology consistent and coherent, and do not introduce new individuals or facts.

Naming: classes in PascalCase (`MilitaryReform`); object and data properties in camelCase (`initiatedBy`, `citizenArmySize`); individuals in PascalCase (`NiccoloMachiavelli`). Preserve any existing identifiers that already follow this convention.

OUTPUT FORMAT:
- Return ONLY the final Turtle. No prose, no markdown fences, no explanations.
- Bind every resource to the `:` (default) prefix.
- The output must be a single Turtle document that `rdflib.Graph().parse(format='turtle')` accepts without errors.

The ontology to fix appears between `<existing_ontology>` tags. The reasoner's report appears between `<validation_result>` tags.

<existing_ontology>
{ontology}
</existing_ontology>

<validation_result>
{error_message}
</validation_result>
""".strip()


class OntologyConsistencyValidationResultPrompt:
    _template: PromptTemplate

    def __init__(self):
        self._template = PromptTemplate.from_template(PROMPT_TEMPLATE)

    def format(
        self,
        ontology_ttl: str,
        validation_result: OntologyConsistencyValidationResult,
    ) -> str:
        return self._template.format(
            ontology=ontology_ttl,
            error_message=validation_result.error_message,
        )
