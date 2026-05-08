# AGENTS.md — `og_sandbox_no_core/`

## What this sandbox is

A self-contained Python package whose only job is to turn natural-language
text into an RDF/Turtle file. The runner sends a task message describing
a source text (and optionally a list of competency questions) and expects
the directory to produce an `output.txt` Turtle artefact when
`python main.py` is executed. Every module the script needs is already
present locally — there is no network, no `pip install`, no `pytest`.

## Files

- **`main.py`** — the only file you edit. It opens with imports from the
  local `engine` package, declares
  `model = get_ontology("https://og.example.org/ontology")`, and ends
  with
  `default_world.as_rdflib_graph().serialize(destination="output.txt", format="turtle")`.
  Between those two fixed parts there is a `with model:` block holding
  three TODOs (entity classes, properties, named individuals). Keep the
  imports, the `get_ontology` line, and the serialize tail untouched.
- **`engine/`** — the local OWL Engine. The names re-exported from
  `engine/__init__.py` are the surface the skeleton uses; do not edit
  anything inside.
- **`output.txt`** — the Turtle file your run produces. Overwritten on
  every execution of `main.py`.

The source text and any competency questions are inserted into the
top-of-file docstring of `main.py` between `=== TASK INPUT ===` and
`=== END TASK INPUT ===` markers at the start of every run. They
remain in place across edits, so they are always reachable by viewing
`main.py`.

## OWL Engine primitives

The names below are imported by the skeleton and are everything you need
to model a domain.

**`Thing`** — the root entity class. Every domain class subclasses
`Thing` directly or transitively. Class definitions live inside
`with model:` so the ontology context picks them up:

```python
with model:
    class Person(Thing): pass
    class City(Thing): pass
```

**`ObjectProperty`** — a relation between two entity classes. Domain and
range are declared as class attributes. Multiple sources or targets in
either list mean "any of these"; for a single class write a one-element
list:

```python
with model:
    class livesIn(ObjectProperty):
        domain = [Person]
        range  = [City]
```

**`DataProperty`** — a relation from an entity to a primitive. The
range list contains Python primitive types: `str`, `int`, `float`,
`bool`, or `datetime.date`. Mix in `FunctionalProperty` when each
subject can carry only one value of that attribute:

```python
with model:
    class hasAge(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [int]

alice.hasAge = 30
```

Without `FunctionalProperty` the same rules as for object properties
apply — assign a list, or `.append()`, not a bare scalar.

**Property characteristics** — `FunctionalProperty`,
`InverseFunctionalProperty`, `TransitiveProperty`, `SymmetricProperty`,
`AsymmetricProperty`, `ReflexiveProperty`, `IrreflexiveProperty`. Each
is a marker class mixed into the property's bases when the source text
supports the behaviour. A `FunctionalProperty` flips the value semantics
(see below).

**Individual creation** — calling a class as `SomeClass("LocalName")`
creates (or returns) an individual whose IRI is
`https://og.example.org/ontology#LocalName`. Calling the same
constructor twice with the same string returns the *same* object — the
engine deduplicates by IRI inside a world. Pass no argument to get an
auto-generated name like `someclass_1`.

**Assigning property values** — non-functional properties hold lists,
functional ones hold a single value. With

```python
class Person(Thing): pass
class livesIn(ObjectProperty):
    domain = [Person]; range = [City]

alice = Person("Alice"); rome = City("Rome")
```

write `alice.livesIn = [rome]` or `alice.livesIn.append(rome)`. A bare
`alice.livesIn = rome` raises `ValueError`. If `livesIn` were declared
as `(ObjectProperty, FunctionalProperty)` the scalar form would be
correct and the list form would be wrong.

**Labels** — `label` is a built-in `AnnotationProperty` rooted at
`rdfs:label`. Assigning a string replaces all previous labels:

```python
alice.label = "Alice Iqbal"
```

The engine stores it as a one-element list internally; reading
`alice.label` returns `["Alice Iqbal"]`. To attach more than one,
assign a list explicitly: `alice.label = ["Alice", "A. Iqbal"]`.

**Class restrictions** — go inside the class body via `is_a`
(sufficient) or `equivalent_to` (necessary-and-sufficient), and combine
the constructors `Or`, `And`, `Not`, plus the property restrictions
`prop.some(Class)` and `prop.only(Class)`:

```python
class Parent(Person):
    is_a = [hasChild.some(Person)]

class NonPlaceboDrug(Drug):
    equivalent_to = [Drug & has_for_active_principle.some(ActivePrinciple)]
```

`A & B` is `And([A, B])`, `A | B` is `Or([A, B])`, and `Not(X)` negates
a class expression.

**Serialization** — the skeleton's tail already runs
`default_world.as_rdflib_graph().serialize(destination="output.txt", format="turtle")`.
You should not call it again.

## Verify

```bash
python main.py
python -c "import rdflib; rdflib.Graph().parse('output.txt', format='turtle')"
```

`output.txt` must exist, be non-empty, and round-trip through rdflib.

## Repo-specific gotcha

The task brief asks you to put the exact source-text mention into the
individual's local name (the constructor argument). If you have already
declared a class with the same local name, the engine will dedup by
IRI: your second `MyClass("MyClass")` returns the existing class object,
not a fresh individual, and `output.txt` ends up structurally
inconsistent. Keep the human-readable mention in `instance.label`; pick
a distinct local name for the constructor (e.g. suffix it).
