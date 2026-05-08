from __future__ import annotations

from og_agents.prompts.base_coding_agent_prompt import BaseCodingAgentPrompt


PROMPT = """
Read the source text in the top-of-file docstring of `{{ builder_file }}` and record the facts it states as Python code on top of the engine package primitives that already live in this project. This is a plain domain-modeling exercise: classes and relations that capture what the text says.

<MODELING>
* Identify every type of thing the text refers to (people, places, organisations, events, artefacts, attributes, time intervals, quantities, etc.) and declare a class for each. Identify every typed relation the text states between two such things and declare a property for it. Stay close to the text.
* Create an instance for every proper-noun mention the source text actually names (people, places, organisations, named events, dated points in time, named numerical quantities, etc.). Use the most specific class you declared for that kind of thing, and pass the exact mention from the text — including diacritics and punctuation — as the instance label so it survives in the serialised Turtle as `rdfs:label`:
      instance = SomeClass('exact mention from text')
      instance.label = 'exact mention from text'
  Do NOT skip any proper-noun mention; do NOT invent instances that the text does not name.
* Class restrictions are useful when the text supports a rule ("every X has some Y", "only Xs can ...", "an X is either A or B"). Use them where they capture domain structure; avoid restrictions that contradict the source.
* Property characteristics — `FunctionalProperty`, `InverseFunctionalProperty`, `TransitiveProperty`, `SymmetricProperty`, `AsymmetricProperty`, `ReflexiveProperty`, `IrreflexiveProperty`. Apply a characteristic only when the text explicitly supports the behavior (e.g. "part of" is transitive; "married to" is symmetric).
* Build a class hierarchy where the text states one type is a kind of another. Feel free to introduce intermediate classes and generalisations that help organise the ontology coherently.
* Do not invent **facts** or **individuals** that the source text does not state.
</MODELING>

<NAMING>
* Classes in PascalCase (`MilitaryReform`).
* Object and data properties in camelCase (`initiatedBy`, `citizenArmySize`).
* Individuals in PascalCase (`NiccoloMachiavelli`).
* English identifiers throughout.
</NAMING>

<OPERATIONAL_STEPS>
The source text lives in the top-of-file docstring of `{{ builder_file }}`, between the `=== TASK INPUT ===` markers.
{% if competency_questions %}
A list of competency questions follows the source in the same docstring; your output must contain enough classes, properties, and individuals to answer every one of them.
{% endif %}
Fill the TODO sections inside the `with model:` block of `{{ builder_file }}` and run `{{ run_command }}` from the current working directory. The workspace `AGENTS.md` describes the engine primitives, file layout, and the rdflib verify step. Iterate until `{{ result_file }}` exists and parses cleanly.
</OPERATIONAL_STEPS>
""".strip()


class NoCorePrompt(BaseCodingAgentPrompt):

    def __init__(self):
        super().__init__(PROMPT)
