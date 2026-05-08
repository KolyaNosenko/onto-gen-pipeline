# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-or-later
# Vendored from Owlready2 0.49 (J.-B. Lamy). Modified for og-agents.
# See /NOTICE.md and /LICENSES/LGPL-3.0-Owlready2.txt for attribution.
VERSION = "0.49"

JAVA_EXE = "java"

from og_sandbox_no_core.engine.base            import *

from og_sandbox_no_core.engine.namespace       import *
from og_sandbox_no_core.engine.entity          import *
from og_sandbox_no_core.engine.prop            import *
from og_sandbox_no_core.engine.prop            import _FUNCTIONAL_FOR_CACHE
from og_sandbox_no_core.engine.individual      import *
from og_sandbox_no_core.engine.class_construct import *
from og_sandbox_no_core.engine.disjoint        import *
from og_sandbox_no_core.engine.annotation      import *
from og_sandbox_no_core.engine.close           import *

# Use `from og_sandbox_no_core.engine import X` instead of
# `import og_sandbox_no_core.engine.X` — during execution of this __init__.py
# attribute access on the partially-initialised package (e.g.
# `og_sandbox_no_core.engine.namespace.X = Y`) raises AttributeError. The
# `from ... import` form resolves submodules via sys.modules.
from og_sandbox_no_core.engine import (
  namespace as _ns,
  entity as _ent,
  prop as _prop_mod,
  class_construct as _cc,
  triplelite as _tl,
  disjoint as _disjoint,
  annotation as _ann,
  individual as _ind,
)
_tl.Or                     = Or
_ns.EntityClass             = EntityClass
_ns.ThingClass              = ThingClass
_ns.DatatypeClass           = DatatypeClass
_ns.Datatype                = Datatype
_ns.PropertyClass           = PropertyClass
_ns.AnnotationPropertyClass = AnnotationPropertyClass
_ns.ObjectPropertyClass     = ObjectPropertyClass
_ns.DataPropertyClass       = DataPropertyClass
_ns.ObjectProperty          = ObjectProperty
_ns.DataProperty            = DataProperty
_ns.AnnotationProperty      = AnnotationProperty
_ns.Thing                   = Thing
_ns.Property                = Property
_ns.Or                      = Or
_ns.And                     = And
_ns.Not                     = Not
_ns.Restriction             = Restriction
_ns.OneOf                   = OneOf
_ns.FusionClass             = FusionClass
_ns.AllDisjoint             = AllDisjoint
_ns.ConstrainedDatatype     = ConstrainedDatatype
_ns.Inverse                 = Inverse
_ns.IndividualValueList     = IndividualValueList
_ent.Thing              = Thing
_ent.Nothing            = Nothing
_ent.Construct          = Construct
_ent.And                = And
_ent.Or                 = Or
_ent.Not                = Not
_ent.OneOf              = OneOf
_ent.Restriction        = Restriction
_ent.ObjectPropertyClass= ObjectPropertyClass
_ent.ObjectProperty     = ObjectProperty
_ent.DataProperty       = DataProperty
_ent.AnnotationProperty = AnnotationProperty
_ent.ReasoningPropertyClass = ReasoningPropertyClass
_ent.FunctionalProperty = FunctionalProperty
#_ent.ValueList          = ValueList
_ent.AllDisjoint        = AllDisjoint
_ent.Inverse            = Inverse
_ent._FUNCTIONAL_FOR_CACHE = _FUNCTIONAL_FOR_CACHE
_ent._property_value_restrictions = _prop_mod._property_value_restrictions
_ent._inherited_properties_value_restrictions = _prop_mod._inherited_properties_value_restrictions
_disjoint.Or = Or
_prop_mod.Restriction             = Restriction
_prop_mod.ConstrainedDatatype     = ConstrainedDatatype
_prop_mod.Construct               = Construct
_prop_mod.AnnotationProperty      = AnnotationProperty
_prop_mod.Thing                   = Thing
_prop_mod.PropertyChain           = PropertyChain
_prop_mod._check_superclasses     = True
_prop_mod.ThingClass              = ThingClass
_prop_mod.And                     = And
_prop_mod.Or                      = Or
_prop_mod.OneOf                   = OneOf
_prop_mod.NamedIndividual         = NamedIndividual

_ann.Construct         = Construct

_ind.Construct           = Construct
_ind.TransitiveProperty  = TransitiveProperty
_ind.SymmetricProperty   = SymmetricProperty
_ind.ReflexiveProperty   = ReflexiveProperty
_ind.InverseFunctionalProperty = InverseFunctionalProperty
_ind.AnnotationPropertyClass   = AnnotationPropertyClass
_cc.Thing       = Thing
_cc.ThingClass  = ThingClass
_cc.EntityClass = EntityClass

LOADING.__exit__()

# Not real property
owl_world._props.pop("Property", None)
owl_world._props.pop("ObjectProperty", None)
owl_world._props.pop("DatatypeProperty", None)
owl_world._props.pop("FunctionalProperty", None)
owl_world._props.pop("InverseFunctionalProperty", None)
owl_world._props.pop("TransitiveProperty", None)
owl_world._props.pop("SymmetricProperty", None)
owl_world._props.pop("AsymmetricProperty", None)
owl_world._props.pop("ReflexiveProperty", None)
owl_world._props.pop("IrreflexiveProperty", None)
owl_world._props.pop("AnnotationProperty", None)

default_world = IRIS = World()
get_ontology  = default_world.get_ontology
get_namespace = default_world.get_namespace


def default_render_func(entity):
  if isinstance(entity.storid, int) and (entity.storid < 0): return "_:%s" % (-entity.storid)
  return "%s.%s" % (entity.namespace.name, entity.name)

def set_render_func(func):
  type.__setattr__(EntityClass, "__repr__", func)
  type.__setattr__(Thing      , "__repr__", func)
  
set_render_func(default_render_func)
