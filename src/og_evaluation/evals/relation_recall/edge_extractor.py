
from __future__ import annotations

from collections import defaultdict

import rdflib
from rdflib.namespace import OWL, RDF, RDFS, SKOS

from og_evaluation.evals.link_recall.edge_extractor import (
    _LABEL_PROPERTIES,
    _label_forms_of,
)


# Predicates that describe ontology *structure*, not domain facts.
# Triples with these predicates are excluded from the typed-edge set so
# the metric does not count `:Niccolo a :Person` as a relation match for
# the gold P27=country_of_citizenship triple.
_STRUCTURAL_PREDICATES: frozenset[str] = frozenset(
    str(uri)
    for uri in (
        # rdf
        RDF.type,
        RDF.first,
        RDF.rest,
        RDF.value,
        # rdfs
        RDFS.label,
        RDFS.comment,
        RDFS.subClassOf,
        RDFS.subPropertyOf,
        RDFS.domain,
        RDFS.range,
        RDFS.seeAlso,
        RDFS.isDefinedBy,
        # owl
        OWL.equivalentClass,
        OWL.equivalentProperty,
        OWL.disjointWith,
        OWL.sameAs,
        OWL.differentFrom,
        OWL.inverseOf,
        OWL.propertyChainAxiom,
        OWL.complementOf,
        OWL.unionOf,
        OWL.intersectionOf,
        OWL.someValuesFrom,
        OWL.allValuesFrom,
        OWL.hasValue,
        OWL.onProperty,
        OWL.cardinality,
        OWL.minCardinality,
        OWL.maxCardinality,
        OWL.qualifiedCardinality,
        OWL.minQualifiedCardinality,
        OWL.maxQualifiedCardinality,
        OWL.onClass,
        OWL.onDataRange,
        OWL.imports,
        OWL.versionInfo,
        OWL.priorVersion,
        # skos
        SKOS.prefLabel,
        SKOS.altLabel,
        SKOS.broader,
        SKOS.narrower,
        SKOS.related,
    )
) | frozenset({"http://schema.org/name"})


def extract_typed_edges(turtle: str) -> set[tuple[frozenset[str], str]]:
    if not turtle or not turtle.strip():
        return set()
    graph = rdflib.Graph()
    try:
        graph.parse(data=turtle, format="turtle")
    except Exception:  # pylint: disable=broad-except
        return set()

    label_lookup: dict[rdflib.URIRef, set[str]] = defaultdict(set)
    for label_property in _LABEL_PROPERTIES:
        for subject, _, value in graph.triples((None, label_property, None)):
            if not isinstance(subject, rdflib.URIRef):
                continue
            if isinstance(value, rdflib.Literal):
                text = str(value).strip()
                if text:
                    label_lookup[subject].add(text)

    edges: set[tuple[frozenset[str], str]] = set()
    for subject, predicate, obj in graph:
        if not isinstance(subject, rdflib.URIRef):
            continue
        if not isinstance(obj, rdflib.URIRef):
            continue
        if not isinstance(predicate, rdflib.URIRef):
            continue
        if str(predicate) in _STRUCTURAL_PREDICATES:
            continue
        s_forms = _label_forms_of(subject, label_lookup)
        o_forms = _label_forms_of(obj, label_lookup)
        p_forms = _label_forms_of(predicate, label_lookup)
        for s_form in s_forms:
            for o_form in o_forms:
                if s_form == o_form:
                    continue
                pair = frozenset({s_form, o_form})
                for p_form in p_forms:
                    edges.add((pair, p_form))
    return edges
