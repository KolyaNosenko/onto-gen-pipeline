from __future__ import annotations

from langchain_core.prompts import PromptTemplate

from og_agents.ontology.validators import OntologyRDFSyntaxValidationResult


PROMPT_TEMPLATE = """
You are an expert in ontology creation and validation. The Turtle ontology below failed RDF syntax validation. Your task is to return a corrected version that parses cleanly.

Resolve every RDF Turtle syntax problem reported by the validator. Preserve the existing domain content; change only what is required to address the flagged issues, and do not introduce new individuals or facts.

Naming: classes in PascalCase (`MilitaryReform`); object and data properties in camelCase (`initiatedBy`, `citizenArmySize`); individuals in PascalCase (`NiccoloMachiavelli`). Preserve any existing identifiers that already follow this convention.

OUTPUT FORMAT:
- Return ONLY the final Turtle. No prose, no markdown fences, no explanations.
- Bind every resource to the `:` (default) prefix.
- The output must be a single Turtle document that `rdflib.Graph().parse(format='turtle')` accepts without errors.

The ontology to fix appears between `<existing_ontology>` tags. The validator's report appears between `<validation_result>` tags.

<existing_ontology>
{ontology}
</existing_ontology>

<validation_result>
{error_message}
</validation_result>
""".strip()


class OntologyRDFSyntaxValidationResultPrompt:
    _template: PromptTemplate

    def __init__(self):
        self._template = PromptTemplate.from_template(PROMPT_TEMPLATE)

    def format(
        self,
        ontology_ttl: str,
        validation_result: OntologyRDFSyntaxValidationResult,
    ) -> str:
        return self._template.format(
            ontology=ontology_ttl,
            error_message=validation_result.error_message,
        )
