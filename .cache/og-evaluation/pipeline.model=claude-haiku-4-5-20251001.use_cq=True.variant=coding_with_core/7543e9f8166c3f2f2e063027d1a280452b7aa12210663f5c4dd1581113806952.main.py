"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

1. What is the location of Store Torungen Lighthouse?
2. Which lighthouse marks the entrance to Arendal along with Store Torungen Lighthouse?
3. When were Store Torungen Lighthouse and Lille Torungen Lighthouse built?
4. What county is Store Torungen Lighthouse located in?
5. Which municipality contains the island of Store Torungen?
6. What body of water does the lighthouse mark the entrance from?
7. Why are Store Torungen Lighthouse and Lille Torungen Lighthouse considered "twin" lighthouses?
8. Which of the two lighthouses is still standing today?
9. Is Store Torungen Lighthouse still in use?
10. How can one access the site of Store Torungen Lighthouse?
11. What accommodations are available at Store Torungen Lighthouse?
12. When is the tower of Store Torungen Lighthouse open to the public?
13. On which coat-of-arms did the two lighthouses appear?
14. What is the current status of Lille Torungen Lighthouse?
15. What facilities are available for public use at the Store Torungen Lighthouse site?
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
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject

from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, NonPhysicalObject, TimeInterval
)

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # TODO: declare your domain entity classes here.
    # Each MUST be a subclass of a class from `og_sandbox_with_core.core.entities`
    # (or of another domain class that ultimately roots in one). Direct
    # subclassing of `Thing` is forbidden — pick the most specific core
    # ancestor that fits.

    class Lighthouse(NonAgentivePhysicalObject):
        """A coastal structure that marks sea entrances and aids navigation."""
        pass
    
    class Place(NonPhysicalObject):
        """A geographic or administrative location (municipality, county, country, town)."""
        pass
    
    class BodyOfWater(NonAgentivePhysicalObject):
        """A body of water such as sea, strait, or ocean."""
        pass
    
    class Island(NonAgentivePhysicalObject):
        """A geographic island."""
        pass
    
    class Building(NonAgentivePhysicalObject):
        """A built structure."""
        pass

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. If a core property matches the text's semantics, subclass it;
    # otherwise declare a fresh ObjectProperty / DataProperty with explicit
    # domain / range.

    class locatedOn(ObjectProperty):
        """Indicates that an entity is located on a geographic feature like an island."""
        domain = [Lighthouse, Building]
        range = [Island]
    
    class locatedIn(ObjectProperty):
        """Indicates spatial containment in a geographic or administrative place."""
        domain = [Lighthouse, Island, Building, Place]
        range = [Place]
    
    class marksEntranceFrom(ObjectProperty):
        """Indicates that a lighthouse marks an entrance from a body of water."""
        domain = [Lighthouse]
        range = [BodyOfWater]
    
    class marksEntranceTo(ObjectProperty):
        """Indicates that a lighthouse marks an entrance to a place."""
        domain = [Lighthouse]
        range = [Place]
    
    class twinWith(ObjectProperty, SymmetricProperty):
        """Indicates a symmetric twin relationship between lighthouses with same specifications."""
        domain = [Lighthouse]
        range = [Lighthouse]
    
    class builtInYear(DataProperty, FunctionalProperty):
        """The year in which an entity was constructed."""
        domain = [Lighthouse, Building]
        range = [int]
    
    class stillStanding(DataProperty, FunctionalProperty):
        """Indicates whether a structure is still standing."""
        domain = [Lighthouse, Building]
        range = [bool]
    
    class currentlyInUse(DataProperty, FunctionalProperty):
        """Indicates whether an entity is currently in use."""
        domain = [Lighthouse, Building]
        range = [bool]
    
    class depictedOnCoatOfArmsOf(ObjectProperty):
        """Indicates that an entity is depicted on the coat of arms of a place."""
        domain = [Lighthouse]
        range = [Place]
    
    class accessibleBy(DataProperty):
        """Indicates the method by which an entity is accessible."""
        domain = [Lighthouse, Island]
        range = [str]
    
    class openToPublic(DataProperty, FunctionalProperty):
        """Indicates whether an entity is open to the public."""
        domain = [Island, Building]
        range = [bool]
    
    class openingSchedule(DataProperty, FunctionalProperty):
        """Describes the schedule when an entity is open."""
        domain = [Building]
        range = [str]
    
    class availableForRent(DataProperty, FunctionalProperty):
        """Indicates whether an entity is available for rent."""
        domain = [Building]
        range = [bool]

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    # Lighthouses
    store_torungen_lighthouse = Lighthouse("StoreTorungenLighthouse")
    store_torungen_lighthouse.label = "Store Torungen Lighthouse"
    store_torungen_lighthouse.builtInYear = 1844
    store_torungen_lighthouse.stillStanding = False
    store_torungen_lighthouse.currentlyInUse = False
    store_torungen_lighthouse.accessibleBy = ["boat"]
    
    lille_torungen_lighthouse = Lighthouse("LilleTorungenLighthouse")
    lille_torungen_lighthouse.label = "Lille Torungen Lighthouse"
    lille_torungen_lighthouse.builtInYear = 1844
    lille_torungen_lighthouse.stillStanding = True
    lille_torungen_lighthouse.currentlyInUse = False
    
    # Geographic locations
    store_torungen_island = Island("StoreTorungenIsland")
    store_torungen_island.label = "Store Torungen"
    store_torungen_island.openToPublic = True
    store_torungen_island.accessibleBy = ["boat"]
    
    arendal = Place("ArendalPlace")
    arendal.label = "Arendal"
    
    aust_agder = Place("AustAgderPlace")
    aust_agder.label = "Aust - Agder"
    
    norway = Place("NorwayPlace")
    norway.label = "Norway"
    
    hisoy = Place("HisoyPlace")
    hisoy.label = "Hisøy"
    
    skaggerak = BodyOfWater("SkaggerakBW")
    skaggerak.label = "Skaggerak"
    
    # Buildings and facilities
    tower = Building("TowerStoreTorungen")
    tower.label = "tower"
    tower.openToPublic = True
    tower.openingSchedule = "daily during the summers"
    
    lighthouse_keepers_house = Building("LighthouseKeepersHouseStoreTorungen")
    lighthouse_keepers_house.label = "lighthouse keepers house"
    lighthouse_keepers_house.availableForRent = True
    
    # Relationships: spatial containment and location
    store_torungen_lighthouse.locatedOn = [store_torungen_island]
    store_torungen_lighthouse.locatedIn = [aust_agder]
    store_torungen_island.locatedIn = [arendal]
    arendal.locatedIn = [aust_agder]
    aust_agder.locatedIn = [norway]
    
    # Relationships: navigation and marking entrance
    store_torungen_lighthouse.marksEntranceFrom = [skaggerak]
    store_torungen_lighthouse.marksEntranceTo = [arendal]
    lille_torungen_lighthouse.marksEntranceTo = [arendal]
    
    # Relationships: twin lighthouses
    store_torungen_lighthouse.twinWith = [lille_torungen_lighthouse]
    lille_torungen_lighthouse.twinWith = [store_torungen_lighthouse]
    
    # Relationships: heraldic depiction
    store_torungen_lighthouse.depictedOnCoatOfArmsOf = [hisoy]
    lille_torungen_lighthouse.depictedOnCoatOfArmsOf = [hisoy]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
