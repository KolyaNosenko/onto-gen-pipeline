"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

1. What type of lighthouse is Store Torungen Lighthouse?
2. On which island is Store Torungen Lighthouse located?
3. In which municipality is Store Torungen Lighthouse located?
4. In which county is Store Torungen Lighthouse located?
5. In which country is Store Torungen Lighthouse located?
6. Which lighthouse is located near Store Torungen Lighthouse?
7. What entrance do Store Torungen Lighthouse and Lille Torungen Lighthouse mark?
8. Through what route do the lighthouses mark the entrance to Arendal?
9. In what year were Store Torungen Lighthouse and Lille Torungen Lighthouse built?
10. Did Store Torungen Lighthouse and Lille Torungen Lighthouse have the same specifications when built?
11. Why are Store Torungen Lighthouse and Lille Torungen Lighthouse considered “twin” lighthouses?
12. Which municipality’s coat of arms included the two Torungen lighthouses?
13. In which municipality were the lighthouses located when they were placed on the coat of arms?
14. Is Store Torungen Lighthouse still standing?
15. Is Lille Torungen Lighthouse still standing?
16. Is Lille Torungen Lighthouse still in use?
17. How can the site of Store Torungen Lighthouse be accessed?
18. Is the island and site of Store Torungen Lighthouse open to the public?
19. When is the tower of Store Torungen Lighthouse open to visitors?
20. What accommodation is available at the lighthouse keeper’s house?
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

from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject,
    PhysicalRegion,
    SocialObject,
    Society,
)


with core:
    class Lighthouse(NonAgentivePhysicalObject):
        pass

    class CoastalLighthouse(Lighthouse):
        pass

    class Island(PhysicalRegion):
        pass

    class Sea(PhysicalRegion):
        pass

    class Route(PhysicalRegion):
        pass

    class Entrance(PhysicalRegion):
        pass

    class Site(PhysicalRegion):
        pass

    class Tower(NonAgentivePhysicalObject):
        pass

    class House(NonAgentivePhysicalObject):
        pass

    class LighthouseKeepersHouse(House):
        pass

    class Municipality(SocialObject):
        pass

    class County(SocialObject):
        pass

    class Town(SocialObject):
        pass

    class Country(Society):
        pass

    class locatedOnIsland(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse, Site]
        range = [Island]

    class locatedInMunicipality(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse, Island, Site]
        range = [Municipality]

    class locatedInCounty(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse, Island, Site]
        range = [County]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse, Island, Site]
        range = [Country]

    class historicallyLocatedInMunicipality(ObjectProperty):
        domain = [Lighthouse]
        range = [Municipality]

    class sameSpecificationsWith(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class featuredOnCoatOfArmsOf(ObjectProperty):
        domain = [Lighthouse]
        range = [Municipality]

    class near(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class marksEntranceTo(ObjectProperty):
        domain = [Lighthouse]
        range = [Entrance]

    class throughRoute(ObjectProperty, FunctionalProperty):
        domain = [Entrance]
        range = [Route]

    class startsFromSea(ObjectProperty, FunctionalProperty):
        domain = [Route]
        range = [Sea]

    class endsAtTown(ObjectProperty, FunctionalProperty):
        domain = [Route]
        range = [Town]

    class hasSite(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [Site]

    class hasTower(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [Tower]

    class hasKeepersHouse(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [LighthouseKeepersHouse]

    class builtYear(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [int]

    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class inUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class wasReplaced(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class openToPublic(DataProperty, FunctionalProperty):
        domain = [Site, Island]
        range = [bool]

    class accessMethod(DataProperty, FunctionalProperty):
        domain = [Site]
        range = [str]

    class openSchedule(DataProperty, FunctionalProperty):
        domain = [Tower]
        range = [str]

    class availableAccommodation(DataProperty, FunctionalProperty):
        domain = [LighthouseKeepersHouse]
        range = [str]

    StoreTorungenLighthouse = CoastalLighthouse("StoreTorungenLighthouse")
    StoreTorungenLighthouse.label = "Store Torungen Lighthouse"

    LilleTorungenLighthouse = CoastalLighthouse("LilleTorungenLighthouse")
    LilleTorungenLighthouse.label = "Lille Torungen Lighthouse"

    StoreTorungen = Island("StoreTorungenIsland")
    StoreTorungen.label = "Store Torungen"

    ArendalMunicipality = Municipality("ArendalMunicipality")
    ArendalMunicipality.label = "Arendal"

    ArendalTown = Town("ArendalTown")
    ArendalTown.label = "Arendal"

    AustAgderCounty = County("AustAgderCounty")
    AustAgderCounty.label = "Aust - Agder county"

    Norway = Country("Norway")
    Norway.label = "Norway"

    HisoyMunicipality = Municipality("HisoyMunicipality")
    HisoyMunicipality.label = "Hisøy"

    Skaggerak = Sea("Skaggerak")
    Skaggerak.label = "Skaggerak"

    ArendalEntrance = Entrance("ArendalEntrance")
    ArendalEntrance.label = "the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal"

    OutlyingIslandsRoute = Route("OutlyingIslandsRoute")
    OutlyingIslandsRoute.label = "through the outlying islands to the mainland town of Arendal"

    StoreTorungenLighthouseSite = Site("StoreTorungenLighthouseSite")
    StoreTorungenLighthouseSite.label = "site of the Store Torungen Lighthouse"

    StoreTorungenLighthouseTower = Tower("StoreTorungenLighthouseTower")
    StoreTorungenLighthouseTower.label = "tower of the Store Torungen Lighthouse"

    StoreTorungenLighthouseKeepersHouse = LighthouseKeepersHouse("StoreTorungenLighthouseKeepersHouse")
    StoreTorungenLighthouseKeepersHouse.label = "lighthouse keepers house of the Store Torungen Lighthouse"

    StoreTorungenLighthouse.locatedOnIsland = StoreTorungen
    StoreTorungenLighthouse.locatedInMunicipality = ArendalMunicipality
    StoreTorungenLighthouse.locatedInCounty = AustAgderCounty
    StoreTorungenLighthouse.locatedInCountry = Norway
    StoreTorungenLighthouse.hasSite = StoreTorungenLighthouseSite
    StoreTorungenLighthouse.hasTower = StoreTorungenLighthouseTower
    StoreTorungenLighthouse.hasKeepersHouse = StoreTorungenLighthouseKeepersHouse
    StoreTorungenLighthouse.builtYear = 1844
    StoreTorungenLighthouse.stillStanding = False
    StoreTorungenLighthouse.wasReplaced = True
    StoreTorungenLighthouse.featuredOnCoatOfArmsOf.append(HisoyMunicipality)
    StoreTorungenLighthouse.historicallyLocatedInMunicipality.append(HisoyMunicipality)
    StoreTorungenLighthouse.sameSpecificationsWith.append(LilleTorungenLighthouse)
    StoreTorungenLighthouse.near.append(LilleTorungenLighthouse)
    StoreTorungenLighthouse.marksEntranceTo.append(ArendalEntrance)

    LilleTorungenLighthouse.builtYear = 1844
    LilleTorungenLighthouse.stillStanding = True
    LilleTorungenLighthouse.inUse = False
    LilleTorungenLighthouse.wasReplaced = True
    LilleTorungenLighthouse.featuredOnCoatOfArmsOf.append(HisoyMunicipality)
    LilleTorungenLighthouse.historicallyLocatedInMunicipality.append(HisoyMunicipality)
    LilleTorungenLighthouse.sameSpecificationsWith.append(StoreTorungenLighthouse)
    LilleTorungenLighthouse.near.append(StoreTorungenLighthouse)
    LilleTorungenLighthouse.marksEntranceTo.append(ArendalEntrance)

    StoreTorungen.locatedInMunicipality = ArendalMunicipality
    StoreTorungen.locatedInCounty = AustAgderCounty
    StoreTorungen.locatedInCountry = Norway
    StoreTorungen.openToPublic = True

    ArendalMunicipality.locatedInCounty = AustAgderCounty
    ArendalMunicipality.locatedInCountry = Norway

    StoreTorungenLighthouseSite.locatedOnIsland = StoreTorungen
    StoreTorungenLighthouseSite.locatedInMunicipality = ArendalMunicipality
    StoreTorungenLighthouseSite.locatedInCounty = AustAgderCounty
    StoreTorungenLighthouseSite.locatedInCountry = Norway
    StoreTorungenLighthouseSite.openToPublic = True
    StoreTorungenLighthouseSite.accessMethod = "only by boat"

    ArendalEntrance.throughRoute = OutlyingIslandsRoute
    OutlyingIslandsRoute.startsFromSea = Skaggerak
    OutlyingIslandsRoute.endsAtTown = ArendalTown

    StoreTorungenLighthouseTower.openSchedule = "daily during the summers"
    StoreTorungenLighthouseKeepersHouse.availableAccommodation = "overnight accommodations"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
