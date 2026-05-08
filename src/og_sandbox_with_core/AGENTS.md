# AGENTS.md — `og_sandbox_with_core/`

## What this sandbox is

A self-contained Python package whose only job is to turn natural-language
text into an RDF/Turtle file, layered on top of a foundational ontology.
The runner sends a task message describing a source text (and optionally
a list of competency questions) and expects the directory to produce an
`output.txt` Turtle artefact when `python main.py` is executed. Every
module the script needs is already present locally — there is no network,
no `pip install`, no `pytest`.

## Files

- **`main.py`** — the only file you edit. It opens with imports from the
  local `engine` package and the line
  `from og_sandbox_with_core.core import core`, then has a `with core:`
  block holding three TODOs (entity classes, properties, named
  individuals), and ends with
  `default_world.as_rdflib_graph().serialize(destination="output.txt", format="turtle")`.
  Keep the imports, the `from … import core` line, and the serialize
  tail untouched.
- **`engine/`** — the local OWL Engine. The names re-exported from
  `engine/__init__.py` are the surface the skeleton uses; read freely,
  do not edit.
- **`core/`** — a upper ontology declared on the engine.
  Importing the package has side effects: each module under
  `core/entities/` and `core/properties/` declares one OWL class or
  property inside its own `with core:` block; `core/axioms.py` and
  `core/property_chains.py` then attach cross-class restrictions and
  property-chain axioms. By the time `main.py` opens its own
  `with core:` block, every name from `core.entities.__all__` and
  `core.properties.__all__` is already defined on `core`.
- **`output.txt`** — the Turtle file your run produces (combined core +
  domain graph). Overwritten on every execution.

The source text and any competency questions are inserted into the
top-of-file docstring of `main.py` between `=== TASK INPUT ===` and
`=== END TASK INPUT ===` markers at the start of every run. They
remain in place across edits, so they are always reachable by viewing
`main.py` even after the conversation has condensed and the original
task message is no longer in your immediate working memory.

## How to subclass core

The task brief requires every domain entity class to be rooted in
`og_sandbox_with_core.core.entities.Particular` (transitively). The
authoritative menu of ancestor names is the `__all__` list in
`core/entities/__init__.py` (and `core/properties/__init__.py` for
properties); each per-name module under `core/entities/<name>.py` or
`core/properties/<name>.py` carries the docstring and class-level
restrictions, and `core/axioms.py` plus `core/property_chains.py`
carry the cross-class axioms.

When you import only the names you actually subclass:

```python
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject, Event, TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt
```

### Entity taxonomy

The 38 classes form a tree rooted at `Particular`. Reproduced verbatim
below so you can pick an ancestor without opening every module
separately:

```
Particular            (cannot be instantiated directly; everything subclasses below)
├── Endurant          (entity wholly present at any time it is present, retains identity)
│   ├── PhysicalEndurant       (has direct spatial quality)
│   │   ├── PhysicalObject     (with unity criterion: a person, a tree, an artefact)
│   │   │   ├── AgentivePhysicalObject     (has intentions, beliefs, desires)
│   │   │   └── NonAgentivePhysicalObject  (does not)
│   │   ├── AmountOfMatter     (no unity criterion: water, sand)
│   │   └── Feature            (with unity criterion, existentially dependent: a hole, a bump)
│   ├── NonPhysicalEndurant    (no direct spatial quality: democracy, a poem)
│   │   └── NonPhysicalObject  (with unity criterion)
│   │       ├── MentalObject   (depends on an agentive physical object: a memory, a plan)
│   │       └── SocialObject   (generically depends on a community: a law, a theory)
│   │           ├── AgentiveSocialObject     (with intentions, beliefs, desires)
│   │           │   ├── SocialAgent          (individual: teacher, president)
│   │           │   └── Society              (collective: a nation, a company)
│   │           └── NonAgentiveSocialObject  (no intentions: regulations, contracts)
│   ├── ArbitrarySum  (mereological sum of physical and non-physical endurants)
│   └── ConstantAtom  (endurant with no constant proper parts)
├── Perdurant         (entity that happens in time: a life, a game, a process)
│   ├── Event         (anti-cumulative perdurant)
│   │   ├── Accomplishment  (mereologically non-atomic: a conference, a war)
│   │   └── Achievement     (mereologically atomic, instantaneous: reaching a summit)
│   └── Stative       (cumulative perdurant)
│       ├── Process   (parts of different type: running, growing)
│       └── State     (parts of the same type: being asleep)
├── Quality           (inheres in an Endurant, Perdurant or other Quality, perceivable / measurable)
│   ├── AbstractQuality           (inheres in a non-physical endurant: an idea's complexity)
│   ├── PhysicalQuality           (inheres in a physical endurant: weight, colour)
│   │   └── SpatialLocation       (the spatial quality of a physical endurant)
│   └── TemporalQuality           (inheres in a perdurant: the duration of an event)
│       └── TemporalLocation      (the temporal quality of a perdurant)
├── Abstract          (no spatial nor temporal quality, not located in time/space)
│   └── Region        (an abstract entity classified by a quality type, with a mereology)
│       ├── AbstractRegion  (region for abstract qualities)
│       ├── PhysicalRegion  (region for physical qualities)
│       │   └── SpaceRegion (physical region, possibly disconnected, for spatial locations)
│       └── TemporalRegion  (region for temporal qualities: a time)
│           └── TimeInterval (a temporal region that is an interval or a sum of intervals)
└── Atom              (atomic Abstract or Perdurant — mereologically indivisible)
```

Pick the most specific class whose docstring matches the text; pick a
broader one when uncertain. New domain classes may sit anywhere in the
tree, with intermediate hops if that helps organise your hierarchy.

### Property families

The 17 ObjectProperties cluster into a small number of families.
Annotations in parentheses spell out characteristics that aren't
obvious from the name:

```
overlaps                    (symmetric)
└── partOf                  (transitive)
    ├── properPartOf        (transitive; the strict variant of partOf)
    ├── atomicPartOf        (the part is an Atom)
    └── temporalPartOf      (transitive; both arguments are perdurants)

constantlyOverlaps          (symmetric; time-invariant overlap)
└── constantPartOf          (transitive; time-invariant partOf)
    ├── constantProperPartOf  (transitive)
    └── constantAtomicPartOf

specificallyDependsOn       (transitive; existence dependence)
└── directQualityOf         (FUNCTIONAL — single value; connects a Quality to its bearer)

presentAt                   (multi-valued; entity is present during a time interval)
└── temporallyLocatedAt     (FUNCTIONAL — single value; the unique exact time interval)

qualeOf                     (inverse-functional; from temporal region to temporal quality)
constantQualeOf             (constant version of qualeOf)
constantConstituentOf       (transitive; constant constitution)
constantParticipantOf       (constant participation in a perdurant)
```

If a `core` property's semantics matches what the text states,
subclass it; the parent's `domain` / `range` will constrain your
subclass. Otherwise declare a fresh `ObjectProperty` /
`DataProperty` with explicit `domain` and `range`.

## OWL Engine primitives

The names below are imported by the skeleton and are everything you need
for *new* declarations (alongside the `core` ancestors).

**`ObjectProperty`** — a relation between two entity classes. Domain and
range are declared as class attributes. Multiple values in either list
mean "any of these"; for a single class write a one-element list:

```python
with core:
    class initiatedBy(ObjectProperty):
        domain = [Event]
        range  = [AgentivePhysicalObject]
```

To carry the semantics of a core property (`partOf`,
`temporallyLocatedAt`, …), subclass it instead of `ObjectProperty`
directly; the parent's domain / range constrain the subclass:

```python
with core:
    class reformsOf(partOf):
        domain = [Event]
        range  = [SocialObject]
```

**`DataProperty`** — a relation from an entity to a primitive. The range
list contains Python primitive types: `str`, `int`, `float`, `bool`, or
`datetime.date`. Mix in `FunctionalProperty` when each subject can
carry only one value of that attribute:

```python
with core:
    class citizenArmySize(DataProperty, FunctionalProperty):
        domain = [Society]
        range  = [int]

florence.citizenArmySize = 20000
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
auto-generated name.

**Assigning property values** — non-functional properties hold lists,
functional ones hold a single value:

```python
reforms = MilitaryReform("FlorentineReforms_1498_1512")
reforms.initiatedBy.append(machiavelli)
reforms.temporallyLocatedAt = [interval]
```

A bare scalar assignment to a non-functional property raises
`ValueError`. If a property is `FunctionalProperty` the scalar form is
correct and a list raises.

**Labels** — `label` is a built-in `AnnotationProperty` rooted at
`rdfs:label`. Assigning a string replaces all previous labels:

```python
machiavelli.label = "Niccolò Machiavelli"
```

The engine stores it as a one-element list internally; reading
`machiavelli.label` returns `["Niccolò Machiavelli"]`. To attach more
than one, assign a list explicitly.

**Class restrictions** — go inside the class body via `is_a` (sufficient)
or `equivalent_to` (necessary-and-sufficient), combined from `Or`,
`And`, `Not`, and the property restrictions `prop.some(Class)`,
`prop.only(Class)`:

```python
with core:
    class Parent(Person):
        is_a = [hasChild.some(Person)]
```

`A & B` is `And([A, B])`, `A | B` is `Or([A, B])`, `Not(X)` negates a
class expression.

**Serialization** — the skeleton's tail already calls
`default_world.as_rdflib_graph().serialize(destination="output.txt", format="turtle")`.
The serialised graph carries both core and domain triples.

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
