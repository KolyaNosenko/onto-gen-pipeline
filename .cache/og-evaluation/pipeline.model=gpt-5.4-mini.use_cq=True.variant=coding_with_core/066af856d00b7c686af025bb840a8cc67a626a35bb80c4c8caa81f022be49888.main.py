"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What is Collins Street?
2. In which city, state, and country is Collins Street located?
3. When was Collins Street laid out?
4. In which survey or grid was Collins Street first laid out?
5. Who was Collins Street named after?
6. What role did David Collins hold?
7. What settlement was led by David Collins in 1803?
8. What colloquial name is given to the eastern end of Collins Street?
9. Since when has the eastern end of Collins Street been known as the “Paris End”?
10. Why is the eastern end of Collins Street called the “Paris End”?
11. What notable features are associated with the “Paris End” of Collins Street?
12. Where were the first sidewalk cafes in Melbourne located?
13. Which area of Collins Street became the financial heart of Melbourne in the 19th century?
14. Which types of organizations were preferred to be located around Queen Street on Collins Street in the 19th century?
15. What kinds of buildings are found along Collins Street today?
16. Does the tradition of Collins Street as a prestigious location continue today?
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
    Abstract,
    AgentivePhysicalObject,
    Event,
    PhysicalObject,
    SocialObject,
    SpaceRegion,
    TimeInterval,
)

# TODO (optional): import the core properties you actually subclass.
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class Street(PhysicalObject):
        pass

    class MajorStreet(Street):
        pass

    class Place(SocialObject):
        pass

    class City(Place):
        pass

    class State(Place):
        pass

    class Country(Place):
        pass

    class Settlement(Place):
        pass

    class Organisation(SocialObject):
        pass

    class Bank(Organisation):
        pass

    class InsuranceCompany(Organisation):
        pass

    class ShoppingBoutique(Organisation):
        pass

    class SidewalkCafe(Organisation):
        pass

    class StreetTree(PhysicalObject):
        pass

    class Building(PhysicalObject):
        pass

    class HeritageBuilding(Building):
        pass

    class OfficeBlock(Building):
        pass

    class Skyscraper(Building):
        pass

    class StreetSection(SpaceRegion):
        pass

    class Survey(Event):
        pass

    class Grid(Abstract):
        pass

    class SettlementEstablishment(Event):
        pass

    class Person(AgentivePhysicalObject):
        pass

    class Role(Abstract):
        pass

    class Nickname(Abstract):
        pass

    class Designation(Abstract):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Or([PhysicalObject, SocialObject, SpaceRegion, Event])]
        range = [Or([PhysicalObject, SocialObject, SpaceRegion, Event])]

    locatedIn.label = ["located in"]

    class laidOutIn(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [Or([Survey, Grid])]

    laidOutIn.label = ["laid out in"]

    class basedOnGrid(ObjectProperty, FunctionalProperty):
        domain = [Survey]
        range = [Grid]

    basedOnGrid.label = ["based on grid"]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [Person]

    namedAfter.label = ["named after"]

    class hasRole(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Role]

    hasRole.label = ["has role"]

    class led(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [SettlementEstablishment]

    led.label = ["led"]

    class resultedIn(ObjectProperty, FunctionalProperty):
        domain = [SettlementEstablishment]
        range = [Settlement]

    resultedIn.label = ["resulted in"]

    class hasColloquialName(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Nickname]

    hasColloquialName.label = ["has colloquial name"]

    class since(ObjectProperty, FunctionalProperty):
        domain = [Or([Nickname, Designation])]
        range = [TimeInterval]

    since.label = ["since"]

    class dueTo(ObjectProperty):
        domain = [StreetSection]
        range = [Or([PhysicalObject, Organisation])]

    dueTo.label = ["due to"]

    class preferredHomeOf(ObjectProperty):
        domain = [StreetSection]
        range = [Organisation]

    preferredHomeOf.label = ["preferred home of"]

    class becameKnownAs(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Designation]

    becameKnownAs.label = ["became known as"]

    class centeredAround(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Street]

    centeredAround.label = ["centered around"]

    class locatedAlong(ObjectProperty):
        domain = [Building]
        range = [Street]

    locatedAlong.label = ["located along"]

    class traditionContinuesToday(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]

    traditionContinuesToday.label = ["tradition continues today"]

    CollinsStreet = MajorStreet("CollinsStreet")
    CollinsStreet.label = "Collins Street"
    Melbourne = City("Melbourne")
    Melbourne.label = "Melbourne"
    Victoria = State("Victoria")
    Victoria.label = "Victoria"
    Australia = Country("Australia")
    Australia.label = "Australia"
    FirstSurveyOfMelbourne = Survey("FirstSurveyOfMelbourne")
    FirstSurveyOfMelbourne.label = "the first survey of Melbourne"
    Original1837HoddleGrid = Grid("Original1837HoddleGrid")
    Original1837HoddleGrid.label = "the original 1837 Hoddle Grid"
    Year1837 = TimeInterval("Year1837")
    Year1837.label = "1837"
    DavidCollins = Person("DavidCollins")
    DavidCollins.label = "David Collins"
    LieutenantGovernor = Role("LieutenantGovernor")
    LieutenantGovernor.label = "Lieutenant-Governor"
    SettlementEstablishmentAtSorrentoIn1803 = SettlementEstablishment("SettlementEstablishmentAtSorrentoIn1803")
    SettlementEstablishmentAtSorrentoIn1803.label = "establishing a short-lived settlement at Sorrento in 1803"
    Year1803 = TimeInterval("Year1803")
    Year1803.label = "1803"
    ShortLivedSettlementAtSorrentoIn1803 = Settlement("ShortLivedSettlementAtSorrentoIn1803")
    ShortLivedSettlementAtSorrentoIn1803.label = "a short-lived settlement at Sorrento in 1803"
    Sorrento = Settlement("Sorrento")
    Sorrento.label = "Sorrento"
    EasternEndOfCollinsStreet = StreetSection("EasternEndOfCollinsStreet")
    EasternEndOfCollinsStreet.label = "the eastern end of Collins Street"
    ParisEnd = Nickname("ParisEnd")
    ParisEnd.label = "Paris End"
    The1950s = TimeInterval("The1950s")
    The1950s.label = "the 1950s"
    HeritageBuildings = HeritageBuilding("HeritageBuildings")
    HeritageBuildings.label = "numerous heritage buildings"
    OldStreetTrees = StreetTree("OldStreetTrees")
    OldStreetTrees.label = "old street trees"
    HighEndShoppingBoutiques = ShoppingBoutique("HighEndShoppingBoutiques")
    HighEndShoppingBoutiques.label = "high-end shopping boutiques"
    FirstSidewalkCafesInTheCity = SidewalkCafe("FirstSidewalkCafesInTheCity")
    FirstSidewalkCafesInTheCity.label = "the first sidewalk cafes in the city"
    BlocksFurtherWestCentredAroundQueenStreet = StreetSection("BlocksFurtherWestCentredAroundQueenStreet")
    BlocksFurtherWestCentredAroundQueenStreet.label = "Blocks further west centred around Queen Street"
    QueenStreet = Street("QueenStreet")
    QueenStreet.label = "Queen Street"
    FinancialHeartOfMelbourneInThe19thCentury = Designation("FinancialHeartOfMelbourneInThe19thCentury")
    FinancialHeartOfMelbourneInThe19thCentury.label = "the financial heart of Melbourne in the 19th century"
    NineteenthCentury = TimeInterval("NineteenthCentury")
    NineteenthCentury.label = "the 19th century"
    MajorBanks = Bank("MajorBanks")
    MajorBanks.label = "major banks"
    InsuranceCompanies = InsuranceCompany("InsuranceCompanies")
    InsuranceCompanies.label = "insurance companies"
    MostPrestigiousOfficeBlocks = OfficeBlock("MostPrestigiousOfficeBlocks")
    MostPrestigiousOfficeBlocks.label = "the most prestigious office blocks"
    Skyscrapers = Skyscraper("Skyscrapers")
    Skyscrapers.label = "skyscrapers found along its length"
    MostDesiredAddressInTheCity = Designation("MostDesiredAddressInTheCity")
    MostDesiredAddressInTheCity.label = "the most desired address in the city"

    CollinsStreet.locatedIn = [Melbourne, Victoria, Australia]
    Melbourne.locatedIn = [Victoria, Australia]
    Victoria.locatedIn = [Australia]
    FirstSurveyOfMelbourne.locatedIn = [Melbourne]
    FirstSurveyOfMelbourne.temporallyLocatedAt = Year1837
    FirstSurveyOfMelbourne.basedOnGrid = Original1837HoddleGrid
    CollinsStreet.laidOutIn = FirstSurveyOfMelbourne
    CollinsStreet.namedAfter = DavidCollins
    DavidCollins.hasRole = LieutenantGovernor
    DavidCollins.led = SettlementEstablishmentAtSorrentoIn1803
    SettlementEstablishmentAtSorrentoIn1803.temporallyLocatedAt = Year1803
    SettlementEstablishmentAtSorrentoIn1803.locatedIn = [Sorrento]
    SettlementEstablishmentAtSorrentoIn1803.resultedIn = ShortLivedSettlementAtSorrentoIn1803
    ShortLivedSettlementAtSorrentoIn1803.locatedIn = [Sorrento]
    EasternEndOfCollinsStreet.locatedIn = [CollinsStreet]
    EasternEndOfCollinsStreet.hasColloquialName = ParisEnd
    ParisEnd.since = The1950s
    EasternEndOfCollinsStreet.dueTo = [HeritageBuildings, OldStreetTrees, HighEndShoppingBoutiques, FirstSidewalkCafesInTheCity]
    HeritageBuildings.locatedIn = [EasternEndOfCollinsStreet]
    OldStreetTrees.locatedIn = [EasternEndOfCollinsStreet]
    HighEndShoppingBoutiques.locatedIn = [EasternEndOfCollinsStreet]
    FirstSidewalkCafesInTheCity.locatedIn = [EasternEndOfCollinsStreet]
    CollinsStreet.becameKnownAs = MostDesiredAddressInTheCity
    BlocksFurtherWestCentredAroundQueenStreet.locatedIn = [CollinsStreet]
    BlocksFurtherWestCentredAroundQueenStreet.centeredAround = QueenStreet
    BlocksFurtherWestCentredAroundQueenStreet.becameKnownAs = FinancialHeartOfMelbourneInThe19thCentury
    FinancialHeartOfMelbourneInThe19thCentury.since = NineteenthCentury
    BlocksFurtherWestCentredAroundQueenStreet.preferredHomeOf = [MajorBanks, InsuranceCompanies]
    MajorBanks.locatedIn = [BlocksFurtherWestCentredAroundQueenStreet]
    InsuranceCompanies.locatedIn = [BlocksFurtherWestCentredAroundQueenStreet]
    MostPrestigiousOfficeBlocks.locatedAlong = [CollinsStreet]
    Skyscrapers.locatedAlong = [CollinsStreet]
    CollinsStreet.traditionContinuesToday = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
