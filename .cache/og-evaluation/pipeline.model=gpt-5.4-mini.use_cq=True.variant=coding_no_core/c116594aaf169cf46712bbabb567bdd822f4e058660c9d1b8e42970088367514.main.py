"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

1. On which island is Store Torungen Lighthouse located?
2. In which municipality is Store Torungen Lighthouse located?
3. In which county is Store Torungen Lighthouse located?
4. In which country is Store Torungen Lighthouse located?
5. What type of place is Store Torungen Lighthouse?
6. Which other lighthouse, together with Store Torungen Lighthouse, marks the entrance to Arendal?
7. What route or geographic passage do Store Torungen Lighthouse and Lille Torungen Lighthouse mark the entrance from?
8. In what year were Store Torungen Lighthouse and Lille Torungen Lighthouse built?
9. Were Store Torungen Lighthouse and Lille Torungen Lighthouse built with the same specifications?
10. Why are Store Torungen Lighthouse and Lille Torungen Lighthouse considered “twin” lighthouses?
11. Which municipality’s coat of arms included the two Torungen lighthouses?
12. Which of the two Torungen lighthouses is still standing?
13. Is the remaining Torungen lighthouse still in use?
14. Is the site of Store Torungen Lighthouse accessible by means other than boat?
15. Is the island and site of Store Torungen Lighthouse open to the public?
16. During which period is the tower of Store Torungen Lighthouse open daily?
17. What facility associated with Store Torungen Lighthouse is available to rent for overnight accommodations?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    class SpatialEntity(Thing):
        pass

    class Region(SpatialEntity):
        pass

    class Structure(SpatialEntity):
        pass

    class Site(SpatialEntity):
        pass

    class Lighthouse(Structure):
        pass

    class CoastalLighthouse(Lighthouse):
        pass

    class Island(Region):
        pass

    class Municipality(Region):
        pass

    class County(Region):
        pass

    class Country(Region):
        pass

    class Town(Region):
        pass

    class Route(SpatialEntity):
        pass

    class GeographicPassage(Route):
        pass

    class Tower(Structure):
        pass

    class LighthouseTower(Tower):
        pass

    class House(Structure):
        pass

    class LighthouseKeepersHouse(House):
        pass

    class LighthouseSite(Site):
        pass

    class Year(Thing):
        pass

    class Season(Thing):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [SpatialEntity]
        range = [SpatialEntity]

    class hasPart(ObjectProperty):
        domain = [SpatialEntity]
        range = [SpatialEntity]

    class marksEntranceFrom(ObjectProperty):
        domain = [Lighthouse]
        range = [Route]

    class marksEntranceTo(ObjectProperty):
        domain = [Lighthouse]
        range = [Town]

    class sameSpecificationsAs(ObjectProperty, SymmetricProperty):
        domain = [CoastalLighthouse]
        range = [CoastalLighthouse]

    class featuredOnCoatOfArmsOf(ObjectProperty):
        domain = [Lighthouse]
        range = [Municipality]

    class builtInYear(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [Year]

    class openDailyDuring(ObjectProperty, FunctionalProperty):
        domain = [LighthouseTower]
        range = [Season]

    class openToPublic(DataProperty, FunctionalProperty):
        domain = [LighthouseSite, Island]
        range = [bool]

    class accessibleOnlyByBoat(DataProperty, FunctionalProperty):
        domain = [LighthouseSite]
        range = [bool]

    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class inUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class availableForRentForOvernightAccommodations(DataProperty, FunctionalProperty):
        domain = [LighthouseKeepersHouse]
        range = [bool]

    class TwinLighthouse(CoastalLighthouse):
        is_a = [sameSpecificationsAs.some(CoastalLighthouse)]

    StoreTorungenLighthouse = TwinLighthouse("StoreTorungenLighthouse")
    StoreTorungenLighthouse.label = "Store Torungen Lighthouse"

    LilleTorungenLighthouse = TwinLighthouse("LilleTorungenLighthouse")
    LilleTorungenLighthouse.label = "Lille Torungen Lighthouse"

    StoreTorungenSite = LighthouseSite("StoreTorungenSite")
    StoreTorungenSite.label = "the site of the Store Torungen Lighthouse"

    StoreTorungenTower = LighthouseTower("StoreTorungenTower")
    StoreTorungenTower.label = "the tower"

    StoreTorungenKeepersHouse = LighthouseKeepersHouse("StoreTorungenKeepersHouse")
    StoreTorungenKeepersHouse.label = "the lighthouse keepers house"

    StoreTorungenIsland = Island("StoreTorungenIsland")
    StoreTorungenIsland.label = "the island of Store Torungen"

    ArendalMunicipality = Municipality("ArendalMunicipality")
    ArendalMunicipality.label = "the municipality of Arendal"

    AustAgderCounty = County("AustAgderCounty")
    AustAgderCounty.label = "Aust - Agder county"

    NorwayCountry = Country("NorwayCountry")
    NorwayCountry.label = "Norway"

    ArendalTown = Town("ArendalTown")
    ArendalTown.label = "the mainland town of Arendal"

    HisoyMunicipality = Municipality("HisoyMunicipality")
    HisoyMunicipality.label = "the local municipality of Hisøy"

    SkaggerakPassage = GeographicPassage("SkaggerakPassage")
    SkaggerakPassage.label = "Skaggerak"

    Year1844 = Year("Year1844")
    Year1844.label = "1844"

    SummerSeason = Season("SummerSeason")
    SummerSeason.label = "the summers"

    StoreTorungenLighthouse.locatedIn = [StoreTorungenSite]
    StoreTorungenSite.locatedIn = [StoreTorungenIsland]
    StoreTorungenIsland.locatedIn = [ArendalMunicipality]
    ArendalMunicipality.locatedIn = [AustAgderCounty]
    AustAgderCounty.locatedIn = [NorwayCountry]

    StoreTorungenLighthouse.hasPart = [StoreTorungenTower, StoreTorungenKeepersHouse]
    StoreTorungenTower.locatedIn = [StoreTorungenSite]
    StoreTorungenKeepersHouse.locatedIn = [StoreTorungenSite]

    StoreTorungenLighthouse.marksEntranceFrom = [SkaggerakPassage]
    LilleTorungenLighthouse.marksEntranceFrom = [SkaggerakPassage]
    StoreTorungenLighthouse.marksEntranceTo = [ArendalTown]
    LilleTorungenLighthouse.marksEntranceTo = [ArendalTown]

    StoreTorungenLighthouse.sameSpecificationsAs = [LilleTorungenLighthouse]

    StoreTorungenLighthouse.builtInYear = Year1844
    LilleTorungenLighthouse.builtInYear = Year1844

    StoreTorungenLighthouse.featuredOnCoatOfArmsOf = [HisoyMunicipality]
    LilleTorungenLighthouse.featuredOnCoatOfArmsOf = [HisoyMunicipality]

    StoreTorungenSite.openToPublic = True
    StoreTorungenIsland.openToPublic = True
    StoreTorungenSite.accessibleOnlyByBoat = True

    StoreTorungenTower.openDailyDuring = SummerSeason
    StoreTorungenKeepersHouse.availableForRentForOvernightAccommodations = True

    LilleTorungenLighthouse.stillStanding = True
    LilleTorungenLighthouse.inUse = False


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
