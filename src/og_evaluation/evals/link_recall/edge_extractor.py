
from __future__ import annotations

import re
from collections import defaultdict

import rdflib
from rdflib.namespace import RDFS, SKOS

_DECAMEL_LOWER_TO_UPPER = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")
_DECAMEL_ACRONYM_BOUNDARY = re.compile(r"(?<=[A-Z])(?=[A-Z][a-z])")
_WS_RUN = re.compile(r"\s+")

_LABEL_PROPERTIES = (
    RDFS.label,
    SKOS.altLabel,
    rdflib.URIRef("http://schema.org/name"),
)


def _local_name(uri: rdflib.URIRef) -> str:
    s = str(uri)
    for sep in ("#", "/"):
        idx = s.rfind(sep)
        if idx >= 0 and idx < len(s) - 1:
            return s[idx + 1 :]
    return s


def _decamelize(name: str) -> str:
    if not name:
        return ""
    spaced = _DECAMEL_LOWER_TO_UPPER.sub(" ", name)
    spaced = _DECAMEL_ACRONYM_BOUNDARY.sub(" ", spaced)
    spaced = spaced.replace("_", " ")
    return _WS_RUN.sub(" ", spaced).strip()


def normalize_form(text: str) -> str:
    return _WS_RUN.sub(" ", text).strip().lower()


def _label_forms_of(
    uri: rdflib.URIRef, label_lookup: dict[rdflib.URIRef, set[str]]
) -> set[str]:
    forms: set[str] = set()
    local = _local_name(uri)
    if local:
        forms.add(local)
    decamelized = _decamelize(local)
    if decamelized:
        forms.add(decamelized)
    for label in label_lookup.get(uri, set()):
        forms.add(label)
    return {normalize_form(f) for f in forms if f}


def extract_edges(turtle: str) -> set[frozenset[str]]:
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

    edges: set[frozenset[str]] = set()
    for subject, _predicate, obj in graph:
        if not isinstance(subject, rdflib.URIRef) or not isinstance(obj, rdflib.URIRef):
            continue
        s_forms = _label_forms_of(subject, label_lookup)
        o_forms = _label_forms_of(obj, label_lookup)
        for s_form in s_forms:
            for o_form in o_forms:
                if s_form == o_form:
                    continue
                edges.add(frozenset({s_form, o_form}))
    return edges
