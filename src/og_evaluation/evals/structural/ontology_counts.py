
from __future__ import annotations

from collections import deque
from dataclasses import asdict, dataclass

import rdflib
from rdflib.namespace import OWL, RDF, RDFS


@dataclass(frozen=True)
class StructuralCounts:
    n_classes: int
    n_object_properties: int
    n_data_properties: int
    n_annotation_properties: int
    n_properties: int  # object + data + annotation
    n_non_is_a_properties: int  # object + data (без annotation) = |P| у Tartir
    n_individuals: int
    n_subclass_axioms: int
    n_axioms: int  # total triple count — proxy for richness
    n_classes_with_instances: int
    n_classes_with_multiple_parents: int
    n_data_property_domain_triples: int
    n_root_classes: int  # без оголошених батьків у subclass-DAG
    n_leaf_classes: int  # без оголошених дітей у subclass-DAG
    n_orphan_classes: int  # без батьків і без дітей (disconnected)
    n_taxonomy_components: int  # weakly-connected components у DAG
    has_taxonomy_cycle: bool
    n_cycle_classes: int  # класи, що лежать у циклі або downstream
    max_taxonomy_depth: int | None
    max_taxonomy_breadth: int | None
    relationship_richness: float | None
    inheritance_richness: float | None
    attribute_richness: float | None
    class_richness: float | None
    average_population: float | None
    mean_taxonomy_depth: float | None
    tangledness: float | None

    def as_dict(self) -> dict:
        return asdict(self)


def count_structural(prediction_ttl: str) -> StructuralCounts | None:
    if not prediction_ttl or not prediction_ttl.strip():
        return None
    graph = rdflib.Graph()
    try:
        graph.parse(data=prediction_ttl, format="turtle")
    except Exception:  # pylint: disable=broad-except
        return None

    classes: set = {
        c for c in graph.subjects(RDF.type, OWL.Class)
        if isinstance(c, rdflib.URIRef) and c != OWL.Thing
    }
    object_properties = set(graph.subjects(RDF.type, OWL.ObjectProperty))
    data_properties = set(graph.subjects(RDF.type, OWL.DatatypeProperty))
    annotation_properties = set(graph.subjects(RDF.type, OWL.AnnotationProperty))
    individuals = set(graph.subjects(RDF.type, OWL.NamedIndividual))

    subclass_pairs: set[tuple] = {
        (s, o)
        for s, o in graph.subject_objects(RDFS.subClassOf)
        if isinstance(s, rdflib.URIRef) and isinstance(o, rdflib.URIRef)
        and s in classes and o in classes
    }

    n_classes = len(classes)
    n_object_properties = len(object_properties)
    n_data_properties = len(data_properties)
    n_annotation_properties = len(annotation_properties)
    n_properties = (
        n_object_properties + n_data_properties + n_annotation_properties
    )
    n_non_is_a_properties = n_object_properties + n_data_properties
    n_individuals = len(individuals)
    n_subclass_axioms = len(subclass_pairs)
    n_axioms = len(graph)

    classes_with_instances = {
        c for c in classes
        if any(True for _ in graph.subjects(RDF.type, c))
    }
    n_classes_with_instances = len(classes_with_instances)

    parent_count: dict = {}
    for child, _parent in subclass_pairs:
        parent_count[child] = parent_count.get(child, 0) + 1
    n_classes_with_multiple_parents = sum(
        1 for v in parent_count.values() if v >= 2
    )

    n_data_property_domain_triples = sum(
        1
        for dp, _domain in graph.subject_objects(RDFS.domain)
        if dp in data_properties
    )

    parents_of: dict = {c: set() for c in classes}
    children_of: dict = {c: set() for c in classes}
    for child, parent in subclass_pairs:
        parents_of[child].add(parent)
        children_of[parent].add(child)

    roots = {c for c in classes if not parents_of[c]}
    leaves = {c for c in classes if not children_of[c]}
    orphans = roots & leaves
    n_root_classes = len(roots)
    n_leaf_classes = len(leaves)
    n_orphan_classes = len(orphans)

    n_taxonomy_components = _count_components(classes, subclass_pairs)

    max_depth, mean_depth, max_breadth, n_cycle_classes = _taxonomy_shape(
        classes, subclass_pairs
    )
    has_cycle = n_cycle_classes > 0

    if n_classes > 0:
        inheritance_richness: float | None = n_subclass_axioms / n_classes
        class_richness: float | None = n_classes_with_instances / n_classes
        average_population: float | None = n_individuals / n_classes
        attribute_richness: float | None = (
            n_data_property_domain_triples / n_classes
        )
        tangledness: float | None = (
            n_classes_with_multiple_parents / n_classes
        )
    else:
        inheritance_richness = None
        class_richness = None
        average_population = None
        attribute_richness = None
        tangledness = None

    rr_denominator = n_subclass_axioms + n_non_is_a_properties
    relationship_richness: float | None = (
        n_non_is_a_properties / rr_denominator if rr_denominator > 0 else None
    )

    return StructuralCounts(
        n_classes=n_classes,
        n_object_properties=n_object_properties,
        n_data_properties=n_data_properties,
        n_annotation_properties=n_annotation_properties,
        n_properties=n_properties,
        n_non_is_a_properties=n_non_is_a_properties,
        n_individuals=n_individuals,
        n_subclass_axioms=n_subclass_axioms,
        n_axioms=n_axioms,
        n_classes_with_instances=n_classes_with_instances,
        n_classes_with_multiple_parents=n_classes_with_multiple_parents,
        n_data_property_domain_triples=n_data_property_domain_triples,
        n_root_classes=n_root_classes,
        n_leaf_classes=n_leaf_classes,
        n_orphan_classes=n_orphan_classes,
        n_taxonomy_components=n_taxonomy_components,
        has_taxonomy_cycle=has_cycle,
        n_cycle_classes=n_cycle_classes,
        max_taxonomy_depth=max_depth,
        max_taxonomy_breadth=max_breadth,
        relationship_richness=relationship_richness,
        inheritance_richness=inheritance_richness,
        attribute_richness=attribute_richness,
        class_richness=class_richness,
        average_population=average_population,
        mean_taxonomy_depth=mean_depth,
        tangledness=tangledness,
    )


def _taxonomy_shape(
    classes: set, subclass_pairs: set[tuple]
) -> tuple[int | None, float | None, int | None, int]:
    if not classes:
        return None, None, None, 0

    children: dict = {}
    in_degree: dict = {c: 0 for c in classes}
    for child, parent in subclass_pairs:
        children.setdefault(parent, set()).add(child)
        in_degree[child] = in_degree.get(child, 0) + 1

    depth: dict = {c: 0 for c in classes if in_degree[c] == 0}
    queue: deque = deque(depth.keys())

    while queue:
        node = queue.popleft()
        for child in children.get(node, set()):
            candidate = depth[node] + 1
            if candidate > depth.get(child, -1):
                depth[child] = candidate
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    n_cycle_classes = sum(1 for c in classes if in_degree[c] > 0)
    if n_cycle_classes > 0:
        return None, None, None, n_cycle_classes

    depths = list(depth.values())
    breadth_by_level: dict[int, int] = {}
    for d in depths:
        breadth_by_level[d] = breadth_by_level.get(d, 0) + 1
    return (
        max(depths),
        sum(depths) / len(depths),
        max(breadth_by_level.values()),
        0,
    )


def _count_components(classes: set, subclass_pairs: set[tuple]) -> int:
    if not classes:
        return 0
    parent: dict = {c: c for c in classes}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for child, par in subclass_pairs:
        union(child, par)

    return len({find(c) for c in classes})
