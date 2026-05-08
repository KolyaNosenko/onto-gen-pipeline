"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

What is Store Torungen Lighthouse?
Where is Store Torungen Lighthouse located?
On which island is Store Torungen Lighthouse situated?
In which municipality is Store Torungen Lighthouse located?
In which county is Store Torungen Lighthouse located?
Which country is Store Torungen Lighthouse in?
What type of lighthouse is Store Torungen Lighthouse?
Which lighthouse is near Store Torungen Lighthouse?
What is the relationship between Store Torungen Lighthouse and Lille Torungen Lighthouse?
What do Store Torungen Lighthouse and Lille Torungen Lighthouse mark?
What entrance do Store Torungen Lighthouse and Lille Torungen Lighthouse mark to Arendal?
When was Store Torungen Lighthouse built?
When was Lille Torungen Lighthouse built?
Were Store Torungen Lighthouse and Lille Torungen Lighthouse built with the same specifications?
Are Store Torungen Lighthouse and Lille Torungen Lighthouse considered twin lighthouses?
Which town do the twin lighthouses mark the way to?
Which municipality included the two lighthouses on its coat of arms?
In which municipality were the two lighthouses located when they appeared on the coat of arms?
Were Store Torungen Lighthouse and Lille Torungen Lighthouse both replaced over time?
Which of the two twin lighthouses is still standing?
Is Lille Torungen Lighthouse still in use?
Is Store Torungen Lighthouse still standing?
How can the site of Store Torungen Lighthouse be accessed?
Is the island of Store Torungen open to the public?
Is the site of Store Torungen Lighthouse open to the public?
When is the tower of Store Torungen Lighthouse open?
Is the tower of Store Torungen Lighthouse open daily during the summer?
Is the lighthouse keeper's house at Store Torungen Lighthouse available for overnight accommodations?
What facilities are available to visitors at Store Torungen Lighthouse?
Can the lighthouse keeper's house at Store Torungen Lighthouse be rented?
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
    NonAgentiveSocialObject,
    TimeInterval,
)


with core:
    class Place(NonAgentiveSocialObject):
        pass


    class AdministrativeArea(Place):
        pass


    class Country(AdministrativeArea):
        pass


    class County(AdministrativeArea):
        pass


    class Municipality(AdministrativeArea):
        pass


    class Town(Place):
        pass


    class NaturalFeature(NonAgentivePhysicalObject):
        pass


    class Island(NaturalFeature):
        pass


    class SeaArea(NaturalFeature):
        pass


    class Vessel(NonAgentivePhysicalObject):
        pass


    class Boat(Vessel):
        pass


    class BuiltStructure(NonAgentivePhysicalObject):
        pass


    class Lighthouse(BuiltStructure):
        pass


    class CoastalLighthouse(Lighthouse):
        pass


    class TwinLighthouse(Lighthouse):
        pass


    class LighthouseTower(BuiltStructure):
        pass


    class LighthouseKeepersHouse(BuiltStructure):
        pass


    class CoatOfArms(NonAgentiveSocialObject):
        pass


    class CalendarYear(TimeInterval):
        pass


    class locatedOnIsland(ObjectProperty):
        domain = [Lighthouse]
        range = [Island]


    class locatedInMunicipality(ObjectProperty):
        domain = [NonAgentivePhysicalObject, Place]
        range = [Municipality]


    class historicallyLocatedInMunicipality(ObjectProperty):
        domain = [Lighthouse]
        range = [Municipality]


    class locatedInCounty(ObjectProperty):
        domain = [NonAgentivePhysicalObject, Place]
        range = [County]


    class locatedInCountry(ObjectProperty):
        domain = [NonAgentivePhysicalObject, Place]
        range = [Country]


    class nearbyLighthouse(ObjectProperty):
        domain = [Lighthouse]
        range = [Lighthouse]


    class twinWith(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]


    class marksEntranceFromSea(ObjectProperty):
        domain = [Lighthouse]
        range = [SeaArea]


    class marksWayToTown(ObjectProperty):
        domain = [Lighthouse]
        range = [Town]


    class builtInYear(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [CalendarYear]


    class builtWithSameSpecificationsAs(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]


    class featuredOnCoatOfArmsOf(ObjectProperty):
        domain = [Lighthouse]
        range = [Municipality]


    class openToPublic(DataProperty, FunctionalProperty):
        domain = [Island]
        range = [bool]


    class siteOpenToPublic(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class siteAccessMode(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [str]


    class siteAccessibleOnlyByBoat(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class towerOpenSchedule(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [str]


    class towerOpenDailyDuringSummers(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class keepersHouseAvailableToRent(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class keepersHouseForOvernightAccommodations(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class wasReplacedOverTime(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    class inUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]


    StoreTorungenInd = Island("StoreTorungenIsland")
    StoreTorungenInd.label = "Store Torungen"

    ArendalInd = Municipality("Arendal")
    ArendalInd.label = "Arendal"
    ArendalInd.is_a.append(Town)

    AustAgderCountyInd = County("AustAgderCounty")
    AustAgderCountyInd.label = "Aust - Agder county"

    NorwayInd = Country("Norway")
    NorwayInd.label = "Norway"

    SkaggerakInd = SeaArea("Skaggerak")
    SkaggerakInd.label = "Skaggerak"

    Year1844Ind = CalendarYear("Year1844")
    Year1844Ind.label = "1844"

    HisoyInd = Municipality("HisoyMunicipality")
    HisoyInd.label = "Hisøy"

    StoreTorungenLighthouseInd = CoastalLighthouse("StoreTorungenLighthouse")
    StoreTorungenLighthouseInd.label = "Store Torungen Lighthouse"
    StoreTorungenLighthouseInd.is_a.append(TwinLighthouse)

    LilleTorungenLighthouseInd = TwinLighthouse("LilleTorungenLighthouse")
    LilleTorungenLighthouseInd.label = "Lille Torungen Lighthouse"

    StoreTorungenInd.locatedInMunicipality.append(ArendalInd)
    StoreTorungenInd.openToPublic = True

    ArendalInd.locatedInCounty.append(AustAgderCountyInd)
    AustAgderCountyInd.locatedInCountry.append(NorwayInd)

    StoreTorungenLighthouseInd.locatedOnIsland.append(StoreTorungenInd)
    StoreTorungenLighthouseInd.locatedInMunicipality.append(ArendalInd)
    StoreTorungenLighthouseInd.locatedInCounty.append(AustAgderCountyInd)
    StoreTorungenLighthouseInd.locatedInCountry.append(NorwayInd)
    StoreTorungenLighthouseInd.nearbyLighthouse.append(LilleTorungenLighthouseInd)
    StoreTorungenLighthouseInd.twinWith.append(LilleTorungenLighthouseInd)
    StoreTorungenLighthouseInd.marksEntranceFromSea.append(SkaggerakInd)
    StoreTorungenLighthouseInd.marksWayToTown.append(ArendalInd)
    StoreTorungenLighthouseInd.builtInYear = Year1844Ind
    StoreTorungenLighthouseInd.builtWithSameSpecificationsAs.append(LilleTorungenLighthouseInd)
    StoreTorungenLighthouseInd.featuredOnCoatOfArmsOf.append(HisoyInd)
    StoreTorungenLighthouseInd.historicallyLocatedInMunicipality.append(HisoyInd)
    StoreTorungenLighthouseInd.siteOpenToPublic = True
    StoreTorungenLighthouseInd.siteAccessMode = "only by boat"
    StoreTorungenLighthouseInd.siteAccessibleOnlyByBoat = True
    StoreTorungenLighthouseInd.towerOpenSchedule = "daily during the summers"
    StoreTorungenLighthouseInd.towerOpenDailyDuringSummers = True
    StoreTorungenLighthouseInd.keepersHouseAvailableToRent = True
    StoreTorungenLighthouseInd.keepersHouseForOvernightAccommodations = True
    StoreTorungenLighthouseInd.wasReplacedOverTime = True
    StoreTorungenLighthouseInd.stillStanding = False

    LilleTorungenLighthouseInd.nearbyLighthouse.append(StoreTorungenLighthouseInd)
    LilleTorungenLighthouseInd.twinWith.append(StoreTorungenLighthouseInd)
    LilleTorungenLighthouseInd.marksEntranceFromSea.append(SkaggerakInd)
    LilleTorungenLighthouseInd.marksWayToTown.append(ArendalInd)
    LilleTorungenLighthouseInd.builtInYear = Year1844Ind
    LilleTorungenLighthouseInd.builtWithSameSpecificationsAs.append(StoreTorungenLighthouseInd)
    LilleTorungenLighthouseInd.featuredOnCoatOfArmsOf.append(HisoyInd)
    LilleTorungenLighthouseInd.historicallyLocatedInMunicipality.append(HisoyInd)
    LilleTorungenLighthouseInd.wasReplacedOverTime = True
    LilleTorungenLighthouseInd.stillStanding = True
    LilleTorungenLighthouseInd.inUse = False


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
