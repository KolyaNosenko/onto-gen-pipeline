from owlready2 import World
from rdflib import Graph
from og_agents.config import AppConfig
from io import BytesIO
import os
import sqlite3

class OntologyStorage:
    _config: AppConfig
    _world: World

    def __init__(self, config: AppConfig):
        self._config = config

        # Set WAL mode via a dedicated connection BEFORE owlready2 opens
        # the file: WAL is persisted in the DB header, so subsequent
        # owlready2 connections inherit it. Without WAL, owlready2's
        # default DELETE journal mode blocks any second connection in
        # the same process (e.g. multiple Streamlit pages) with
        # `database is locked`.
        db_path = self._config.db.file_path
        if os.path.exists(db_path):
            try:
                with sqlite3.connect(db_path, timeout=5.0) as con:
                    mode = con.execute("PRAGMA journal_mode").fetchone()
                    if mode and mode[0].lower() != "wal":
                        con.execute("PRAGMA journal_mode=WAL")
            except sqlite3.OperationalError:
                # An existing owlready2 connection in DELETE-mode holds a
                # write lock and prevents the upgrade. The DB will keep
                # its current journal mode for this run; this call should
                # not break OntologyStorage construction.
                pass

        world = World()
        # exclusive=False prevents owlready2 from issuing
        # `PRAGMA locking_mode=EXCLUSIVE`, which would otherwise hold the
        # SQLite file open for the entire lifetime of this connection
        # and block any other OntologyStorage instance in the same
        # process (e.g. multi-page Streamlit apps).
        world.set_backend(filename=db_path, backend="sqlite", exclusive=False)
        world.graph.db.execute("PRAGMA busy_timeout=5000")
        self._world = world

    def create_from_ttl(self, ontology_ttl: str):
        rdf_graph = Graph()
        rdf_graph.parse(data=ontology_ttl, format="turtle")

        rdf_graph.serialize(
            self._config.db.tutle_fallback_path,
            format="turtle"
        )

        rdfxml_bytes = rdf_graph.serialize(format="xml")

        if isinstance(rdfxml_bytes, str):
            rdfxml_bytes = rdfxml_bytes.encode("utf-8")

        onto = self._world.get_ontology(self._config.ontology_name)

        onto.load(fileobj=BytesIO(rdfxml_bytes))

        self._world.save()
        print('Ontology saved to', self._config.db.file_path)

    def load(self):
        return self._world.get_ontology(self._config.ontology_name)

    def get_world_as_rdf_graph(self):
        return self._world.as_rdflib_graph()

    def destroy(self):
        onto = self.load()
        onto.destroy()

        self._world.save()

        if os.path.exists(self._config.db.tutle_fallback_path):
            os.remove(self._config.db.tutle_fallback_path)


    def is_exist(self):
        onto = self.load()

        return (
            next(onto.classes(), None) is not None or
            next(onto.object_properties(), None) is not None or
            next(onto.data_properties(), None) is not None or
            next(onto.individuals(), None) is not None
        )
