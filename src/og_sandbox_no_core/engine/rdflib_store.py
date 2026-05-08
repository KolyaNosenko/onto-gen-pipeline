# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-or-later
# Vendored from Owlready2 0.49 (J.-B. Lamy). Modified for og-agents.
# See /NOTICE.md and /LICENSES/LGPL-3.0-Owlready2.txt for attribution.
import rdflib, rdflib.store
from rdflib import URIRef, BNode, Literal

import og_sandbox_no_core.engine.triplelite, og_sandbox_no_core.engine.namespace
from og_sandbox_no_core.engine.base import *
from og_sandbox_no_core.engine.base import _universal_abbrev_2_datatype

class TripleLiteRDFlibStore(rdflib.store.Store):
  context_aware = True
  
  def __init__(self, world):
    self.world      = world
    self.triplelite = world.graph
    self.non_int_bnode = {}
    super().__init__()
    
    self.__namespace = {}
    self.__prefix = {}
    
    self.main_graph            = TripleLiteRDFlibGraph(store = self)
    self.main_graph.onto       = None
    self.main_graph.triplelite = self.triplelite
    
    self.context_graphs = {}
    for onto, triplelite in self.triplelite.onto_2_subgraph.items():
      graph            = TripleLiteRDFlibGraph(store = self, identifier = URIRef(onto._base_iri))
      graph.onto       = onto
      graph.triplelite = triplelite
      self.context_graphs[onto] = graph
      
  def _add_onto(self, onto):
    graph            = TripleLiteRDFlibGraph(store = self, identifier = URIRef(onto._base_iri))
    graph.onto       = onto
    graph.triplelite = onto.graph
    self.context_graphs[onto] = graph
    
  def _2_python(self, x):
    if   isinstance(x, rdflib.term.URIRef ): return self.world[str(x)]
    elif isinstance(x, rdflib.term.BNode  ): return str(x)
    elif isinstance(x, rdflib.term.Literal): return x.toPython()
    
  def _bnode_2_owlready(self, bnode):
    try: return -int(bnode)
    except:
      bnode = str(bnode)
      r = self.non_int_bnode.get(bnode)
      if not r: r = self.non_int_bnode[bnode] = self.triplelite.new_blank_node()
      return r
    
  def _rdflib_2_owlready(self, spo):
    s,p,o = spo
    if   isinstance(s, rdflib.term.URIRef ): s = self.triplelite._abbreviate(str(s))
    elif isinstance(s, rdflib.term.BNode  ): s = self._bnode_2_owlready(s)
    if   isinstance(p, rdflib.term.URIRef ): p = self.triplelite._abbreviate(str(p))
    if   isinstance(o, rdflib.term.URIRef ): o = self.triplelite._abbreviate(str(o)); d = None
    elif isinstance(o, rdflib.term.BNode  ): o = self._bnode_2_owlready(o); d = None
    elif isinstance(o, rdflib.term.Literal):
      if o.language is None:
        if o.datatype:
          d = self.triplelite._abbreviate(str(o.datatype))
          if   isinstance(o.value, bool):         o = str(o)
          elif isinstance(o.value, (int, float)): o = o.value
          else:                                   o = str(o)
        else:
          d = 0
          o = str(o)
      else:
        d = "@%s" % o.language
        o = str(o)
    else:
      d = None
    return s,p,o,d
  
  def _owlready_2_rdflib(self, s,p,o,d = None):
    if   s < 0: s = BNode(-s)
    else:       s = URIRef(self.triplelite._unabbreviate(s))
    p = URIRef(self.triplelite._unabbreviate(p))
    if d is None:
      if o < 0: o = BNode(-o)
      else:     o = URIRef(self.triplelite._unabbreviate(o))
    else:
      if   isinstance(d, str) and d.startswith("@"): o = Literal(o, lang = d[1:])
      elif (d == "") or (d == 0):                    o = Literal(o)
      else:                                          o = Literal(o, datatype = URIRef(self.triplelite._unabbreviate(d)))
    return s,p,o
  
  def add(self, xxx_todo_changeme, context, quoted = False):
    if isinstance(context.triplelite, og_sandbox_no_core.engine.triplelite.SubGraph):
      ontology = context.triplelite.onto
    else:
      ontology = None
    self.world._add_quads_with_update(ontology, [(None, *self._rdflib_2_owlready(xxx_todo_changeme))])
    
  def remove(self, xxx_todo_changeme, context = None):
    self.world._del_triple_with_update(*self._rdflib_2_owlready(xxx_todo_changeme))
    
    
  def triples(self, triple_pattern, context = None):
    rs,rp,ro,rd = self._rdflib_2_owlready(triple_pattern)
    
    if   ro is None:
      for s,p,o,d in context.triplelite._get_triples_spod_spod(rs,rp,None, None):
        yield self._owlready_2_rdflib(s,p,o,d), context
      if rp:
        prop = self.world._entities.get(rp)
        if prop and prop._inverse_storid:
          for o,p,s in context.triplelite._get_obj_triples_spo_spo(None,prop._inverse_storid,rs):
            yield self._owlready_2_rdflib(s,rp,o,None), context
      else:
        for o,p,s in context.triplelite._get_obj_triples_spo_spo(None,None,rs):
          prop = self.world._entities.get(p)
          if prop and prop._inverse_storid:
            yield self._owlready_2_rdflib(s,prop._inverse_storid,o,None), context
            
    elif rd is None:
      for s,p,o in context.triplelite._get_obj_triples_spo_spo(rs,rp,ro):
        yield self._owlready_2_rdflib(s,p,o,None), context
      if rp:
        prop = self.world._entities.get(rp)
        if prop and prop._inverse_storid:
          for o,p,s in context.triplelite._get_obj_triples_spo_spo(ro,prop._inverse_storid,rs):
            yield self._owlready_2_rdflib(s,rp,o,None), context
      else:
        for o,p,s in context.triplelite._get_obj_triples_spo_spo(ro,None,rs):
          prop = self.world._entities.get(p)
          if prop and prop._inverse_storid:
            yield self._owlready_2_rdflib(s,prop._inverse_storid,o,None), context
        
    else:
      for s,p,o,d in context.triplelite._get_data_triples_spod_spod(rs,rp,ro, None):
        yield self._owlready_2_rdflib(s,p,o,d), context
            
      
  def __len__(self, context = None):
    return len(context.triplelite)
  
  def contexts(self, triple = None):
    if triple is None:
      return self.context_graphs.values()
    else:
      triple = self._rdflib_2_owlready(triple)
      for graph in self.context_graphs.values():
        if graph.triplelite.has_triple(*triple): yield graph
        
        
  def bind(self, prefix, namespace, override = True):
    if (not override) and (namespace in self.__prefix): return
    self.__prefix[namespace] = prefix
    self.__namespace[prefix] = namespace
    
  def namespace(self, prefix):
    return self.__namespace.get(prefix, None)

  def prefix(self, namespace):
    return self.__prefix.get(namespace, None)

  def namespaces(self):
    for prefix, namespace in self.__namespace.items():
      yield prefix, namespace
      
  def get_context(self, identifier_or_ontology):
    if isinstance(identifier_or_ontology, URIRef):
      identifier_or_ontology = str(identifier_or_ontology)
      for onto, graph in self.context_graphs.items():
        if identifier_or_ontology == onto._base_iri:
          return graph
      for onto, graph in self.context_graphs.items():
        if identifier_or_ontology == onto._base_iri[:-1]:
          return graph
      raise ValueError
    else:
      return self.context_graphs[identifier_or_ontology]
    
        
class TripleLiteRDFlibGraph(rdflib.Graph):
  onto = None
  def query_owlready(self, query, *args, **kargs):
    r = self.query(query, *args, **kargs)
    for line in r:
      try:
          iter_line = iter(line)
      except TypeError:
          yield line
          continue
      line2 = [self._rdflib_2_owlready(i) for i in iter_line]
      yield line2
      
  # def update(self, query, *args, **kargs):
  #   self.store._bn_needing_update = set()
  #   r = rdflib.Graph.update(self, query, *args, **kargs)
  #   for onto, bn in self.store._bn_needing_update:
  #     onto._reload_bnode(bn)
  #   return r
  
  def _rdflib_2_owlready(self, o):
    if   isinstance(o, rdflib.term.URIRef ):
      o = self.store.world[str(o)] or self.store.world._abbreviate(str(o))
      if isinstance(o, int):
        if o in _universal_abbrev_2_datatype: o = _universal_abbrev_2_datatype[o] 
    elif isinstance(o, rdflib.term.BNode  ):
      o = (self.onto or self.store.world)._parse_bnode(self.store._bnode_2_owlready(o))
    elif isinstance(o, rdflib.term.Literal):
      if o.language is None:
        if o.datatype:
          d = self.triplelite._abbreviate(str(o.datatype))
          #o = o.value
          o = str(o)
        else:
          d = ""
          o = str(o)
      else:
        d = "@%s" % o.language
        o = str(o)
      o = from_literal(o, d)
    return o

  def get_context(self, onto): return self.store.get_context(onto)
  
  def BNode(self): return BNode(-self.store.world.new_blank_node())
