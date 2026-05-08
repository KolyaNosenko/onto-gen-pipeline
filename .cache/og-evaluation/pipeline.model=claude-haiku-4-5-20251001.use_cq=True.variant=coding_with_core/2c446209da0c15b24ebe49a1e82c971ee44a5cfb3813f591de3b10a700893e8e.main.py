"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

1. What is Milton and where is it located?
2. In which region of New South Wales is Milton situated?
3. What administrative area does Milton belong to?
4. When was Milton founded?
5. Who was Milton named after?
6. What was the occupation of the person Milton was named after?
7. What role did Milton play during the 19th Century?
8. What is the current population of Milton?
9. What are the main commercial centres in the Milton-Ulladulla district?
10. Which highway runs through the centre of Milton?
11. What industries have influenced Milton's recent resurgence?
12. What types of businesses have recently opened in Milton?
13. What new developments are occurring on the fringes of Milton?
14. Why are residents moving to the Milton district?
15. Is Milton a stopping place for travellers, and if so, on which route?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, AgentivePhysicalObject,
    SpaceRegion, TimeInterval
)

# TODO (optional): import the core properties you actually subclass.
from og_sandbox_with_core.core.properties import partOf


with core:
    # Entity classes
    class Person(AgentivePhysicalObject):
        """A human person with agency and intentions."""
        pass
    
    class Town(NonAgentivePhysicalObject):
        """A town or settlement."""
        pass
    
    class CoastalRegion(SpaceRegion):
        """A geographic coastal region."""
        pass
    
    class State(SpaceRegion):
        """A state or major geographic division of a country."""
        pass
    
    class Country(SpaceRegion):
        """A country or nation."""
        pass
    
    class CityArea(SpaceRegion):
        """A city or metropolitan administrative area."""
        pass
    
    class LocalDistrict(SpaceRegion):
        """A local district or geographic subdivision."""
        pass
    
    class Highway(NonAgentivePhysicalObject):
        """A highway or major road."""
        pass

    # Properties
    class namedAfter(ObjectProperty):
        """Relates a town to the person or entity it was named after."""
        domain = [Town]
        range = [Person]
    
    class hasOccupation(DataProperty, FunctionalProperty):
        """The occupation or profession of a person."""
        domain = [Person]
        range = [str]
    
    class hasPopulation(DataProperty, FunctionalProperty):
        """The population of a town or city."""
        domain = [Town]
        range = [int]
    
    class runsThrough(ObjectProperty):
        """A highway that runs through a location."""
        domain = [Highway]
        range = [Town]
    
    class foundedIn(ObjectProperty, FunctionalProperty):
        """The year or time period when a town was founded."""
        domain = [Town]
        range = [TimeInterval]
    
    class becameImportantDuring(ObjectProperty, FunctionalProperty):
        """The time period when a town became important or gained significance."""
        domain = [Town]
        range = [TimeInterval]

    # Named individuals
    milton = Town("Milton")
    milton.label = "Milton"
    
    southCoast = CoastalRegion("SouthCoast")
    southCoast.label = "South Coast"
    
    newSouthWales = State("NewSouthWales")
    newSouthWales.label = "New South Wales"
    
    australia = Country("Australia")
    australia.label = "Australia"
    
    cityOfShoalhaven = CityArea("CityOfShoalhaven")
    cityOfShoalhaven.label = "City of Shoalhaven"
    
    georgeKnight = Person("GeorgeKnight")
    georgeKnight.label = "George Knight"
    
    miltonUlladulla = LocalDistrict("MiltonUlladulla")
    miltonUlladulla.label = "Milton-Ulladulla"
    
    princesHighway = Highway("PrincesHighway")
    princesHighway.label = "Princes Highway"
    
    year1860 = TimeInterval("1860")
    year1860.label = "1860"
    
    nineteenthCentury = TimeInterval("19thCentury")
    nineteenthCentury.label = "19th Century"
    
    # Establish relationships
    milton.partOf.append(southCoast)
    milton.partOf.append(cityOfShoalhaven)
    milton.partOf.append(miltonUlladulla)
    
    southCoast.partOf.append(newSouthWales)
    
    newSouthWales.partOf.append(australia)
    
    milton.namedAfter.append(georgeKnight)
    
    georgeKnight.hasOccupation = "post master"
    
    milton.hasPopulation = 1663
    
    princesHighway.runsThrough.append(milton)
    
    milton.foundedIn = year1860
    
    milton.becameImportantDuring = nineteenthCentury


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
