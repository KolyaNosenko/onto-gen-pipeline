from __future__ import annotations

from langchain_core.prompts import PromptTemplate

from og_agents.documents import OntologySourceDocument


PROMPT_TEMPLATE = """
You are an ontology engineer. Read the source text below and encode the facts it states as a OWL ontology in Turtle syntax.

Identify every type of thing the text refers to (people, places, organisations, events, artefacts, attributes, time intervals, quantities, etc.) and declare a class for each. Identify every typed relation the text states between two such things and declare a property for it. Stay close to the text.

Then create a named individual for every proper-noun mention the source text actually names (people, places, organisations, named events, dated points in time, named numerical quantities, etc.). Each such mention MUST appear in the ontology as
    :Identifier a :ItsClass , owl:NamedIndividual ;
        rdfs:label "exact mention from text"^^xsd:string .
Use the most specific class you declared for that kind of thing. Use `rdfs:label` to preserve the exact surface form. Pick a stable `:Identifier` (PascalCase, no spaces). Do NOT skip any individuals mention; do NOT invent individuals that the text does not name.

Class restrictions (`equivalentClass` / `subClassOf` with `owl:Restriction`, `owl:someValuesFrom`, `owl:allValuesFrom`, `owl:unionOf`, `owl:intersectionOf`, `owl:complementOf`) are useful when the text supports a rule ("every X has some Y", "only Xs can ...", "an X is either A or B"). Use them where they capture domain structure; avoid restrictions that contradict the source.

Property characteristics: `owl:FunctionalProperty`, `owl:InverseFunctionalProperty`, `owl:TransitiveProperty`, `owl:SymmetricProperty`, `owl:AsymmetricProperty`, `owl:ReflexiveProperty`, `owl:IrreflexiveProperty`. Apply a characteristic only when the text explicitly supports the behavior (e.g. "part of" is transitive; "married to" is symmetric).

Build a class hierarchy where the text states one type is a kind of another. Feel free to introduce intermediate classes and generalisations that help organise the ontology coherently.
Do not invent **facts** or **individuals** that the source text does not state.

NAMING:
- classes in PascalCase (`MilitaryReform`);
- object and data properties in camelCase (`initiatedBy`, `citizenArmySize`);
- individuals in PascalCase (`NiccoloMachiavelli`).
- English identifiers throughout.

OUTPUT FORMAT:
- Return ONLY the final Turtle. No prose, no markdown fences, no explanations.
- Bind every resource to the `:` (default) prefix.
- Use these prefixes verbatim at the top:
    @prefix : <http://www.example.org/test#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> ..

## SOURCE TEXT:
{{ source_text }}

{% if competency_questions %}
Your output must contain enough classes, properties, and individuals to answer every competency question.

## COMPETENCY QUESTIONS:
{{ competency_questions }}
{% endif %}
""".strip()


class GenerateOntologyPrompt:
    _template: PromptTemplate

    def __init__(self):
        self._template = PromptTemplate(
            template=PROMPT_TEMPLATE,
            input_variables=["source_text", "competency_questions"],
            template_format="jinja2",
        )

    def format(
        self,
        competency_questions: str | None,
        documents: list[OntologySourceDocument],
    ) -> str:
        joined = "\n".join(
            doc.to_prompt_format(index)
            for index, doc in enumerate(documents)
        )
        return self._template.format(
            source_text=joined,
            competency_questions=(competency_questions or "").strip(),
        )
