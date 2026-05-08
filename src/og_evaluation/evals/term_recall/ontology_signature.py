
from __future__ import annotations

import re

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


def _emit_uri_forms(uri: rdflib.URIRef, sink: list[str], seen: set[str]) -> None:
    local = _local_name(uri)
    for form in (local, _decamelize(local)):
        if not form:
            continue
        if form in seen:
            continue
        seen.add(form)
        sink.append(form)


def extract_searchable_text(turtle: str) -> str:
    if not turtle or not turtle.strip():
        return ""
    graph = rdflib.Graph()
    try:
        graph.parse(data=turtle, format="turtle")
    except Exception:  # pylint: disable=broad-except
        return ""
    parts: list[str] = []
    seen: set[str] = set()
    # Pass 1 — preferred label literals.
    for label_property in _LABEL_PROPERTIES:
        for _, _, value in graph.triples((None, label_property, None)):
            if isinstance(value, rdflib.Literal):
                text = str(value).strip()
                if text and text not in seen:
                    seen.add(text)
                    parts.append(text)
    # Pass 2 — every URI's local-name (subjects, predicates, objects).
    for subject, predicate, obj in graph:
        for node in (subject, predicate, obj):
            if isinstance(node, rdflib.URIRef):
                _emit_uri_forms(node, parts, seen)
            elif isinstance(node, rdflib.Literal):
                text = str(node).strip()
                if text and text not in seen:
                    seen.add(text)
                    parts.append(text)
    return " ".join(parts)
