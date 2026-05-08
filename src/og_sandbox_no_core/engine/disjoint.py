# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-or-later
# Vendored from Owlready2 0.49 (J.-B. Lamy). Modified for og-agents.
# See /NOTICE.md and /LICENSES/LGPL-3.0-Owlready2.txt for attribution.
from og_sandbox_no_core.engine.namespace       import *
from og_sandbox_no_core.engine.entity          import *
from og_sandbox_no_core.engine.prop            import *
from og_sandbox_no_core.engine.class_construct import *


class AllDisjoint(object):
  def __init__(self, entities, ontology = None, bnode = None):
    #if not CURRENT_NAMESPACES[-1] is None: self.ontology = CURRENT_NAMESPACES[-1].ontology
    #else:                                  self.ontology = ontology or entities[0].namespace.ontology
    self.ontology = (CURRENT_NAMESPACES.get() and CURRENT_NAMESPACES.get()[-1]) or ontology or entities[0].namespace.ontology
    
    # For AllDisjoint, storid can be either:
    #   * a blank node, when at least 3 entities are involved
    #   * a triple, when only 2 entities, e.g. (entity1.storid, owl_disjointwith, entity2.storid)
    
    if   isinstance(entities, int):
      assert isinstance(bnode, int)
      self.storid      = bnode
      self._list_bnode = entities
    elif isinstance(entities, tuple):
      self.storid      = entities
    else:
      self.storid      = bnode
      self._list_bnode = None
      self.entities = self.Properties = self.individuals = CallbackList(entities, self, AllDisjoint._callback)
      
    if not LOADING: self._create_triples()
    
  def __getattr__(self, attr):
    if attr == "entities":
      if isinstance(self.storid, int):
        r = self.ontology._parse_list(self._list_bnode)
      else:
        r = [self.ontology.world._to_python(self.storid[0]), self.ontology.world._to_python(self.storid[2])]
      r = CallbackList(r, self, AllDisjoint._callback)
      setattr(self, attr,r)
      return r
    return super().__getattribute__(attr)
  
  def _callback(self, old):
    if self.ontology:
      self._destroy_triples()
      self._create_triples ()
      
  def _destroy_triples(self):
    if   isinstance(self.storid, int):
      self.ontology._del_obj_triple_spo(self.storid, None, None)
      self.ontology._del_list(self._list_bnode)
    elif isinstance(self.storid, tuple):
      self.ontology._del_obj_triple_spo(*self.storid)
      
  def destroy(self): self._destroy_triples()
  
  def _create_triples(self):
    for entity in self.entities:
      if isinstance(entity, Construct): entity._set_ontology(self.ontology)
      
    if len(self.entities) == 2:
      if   isinstance(self.entities[0], ThingClass):
        self.storid = (self.entities[0].storid, owl_disjointwith, self.entities[1].storid)
        self.ontology._add_obj_triple_spo(*self.storid)
        return
      elif isinstance(self.entities[0], PropertyClass):
        self.storid = (self.entities[0].storid, owl_propdisjointwith, self.entities[1].storid)
        self.ontology._add_obj_triple_spo(*self.storid)
        return
      # It seems that there is no 1-1 relation for individuals
      # => continue
      
    if len(self.entities) >= 2:
      if not isinstance(self.storid, int): self.storid      = self.ontology.world.new_blank_node()
      if not self._list_bnode:             self._list_bnode = self.ontology.world.new_blank_node()
      
      if   isinstance(self.entities[0], ThingClass):
        self.ontology._add_obj_triple_spo(self.storid, rdf_type, owl_alldisjointclasses)
        self.ontology._add_obj_triple_spo(self.storid, owl_members, self._list_bnode)
        
      elif isinstance(self.entities[0], PropertyClass):
        self.ontology._add_obj_triple_spo(self.storid, rdf_type, owl_alldisjointproperties)
        self.ontology._add_obj_triple_spo(self.storid, owl_members, self._list_bnode)
        
      else: # Individuals
        self.ontology._add_obj_triple_spo(self.storid, rdf_type, owl_alldifferent)
        self.ontology._add_obj_triple_spo(self.storid, owl_distinctmembers, self._list_bnode)
        
      self.ontology._set_list(self._list_bnode, self.entities)
      
  def __repr__(self):
    if self.ontology != self.entities[0].namespace.ontology: onto = ", ontology = %s" % self.ontology
    else:                                                    onto = ""
    return "AllDisjoint([%s]%s)" % (", ".join(repr(Class) for Class in self.entities), onto)
    
AllDifferent = AllDisjoint


def partition(mother, children):
  mother.is_a.append(Or(children))
  AllDisjoint(children)

  
# class DisjointUnion(LogicalClassConstruct):
#   _owl_op = owl_disjointunion
#   is_a    = ()
  
#   def _satisfied_by(self, x):
#     for Class in self.Classes:
#       if Class._satisfied_by(x): return True
#     return False
  
#   def __repr__(self):
#     s = []
#     for x in self.Classes:
#       if isinstance(x, LogicalClassConstruct): s.append("(%s)" % x)
#       else:                                    s.append(repr(x))
#     return "%s([%s])" % (self.__class__.__name__, ", ".join(s))
