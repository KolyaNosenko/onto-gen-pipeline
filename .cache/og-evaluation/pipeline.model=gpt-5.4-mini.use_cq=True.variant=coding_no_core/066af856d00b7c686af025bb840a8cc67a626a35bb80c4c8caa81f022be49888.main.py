"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What city and state is Collins Street located in?
2. In which country is Collins Street located?
3. What type of street is Collins Street?
4. In what survey or city plan was Collins Street laid out?
5. When was the original Hoddle Grid created?
6. Why did Collins Street become a desired address in Melbourne?
7. Who was Collins Street named after?
8. What role did Lieutenant-Governor David Collins have?
9. What settlement did David Collins help establish?
10. Where was the settlement led by David Collins located?
11. What is the eastern end of Collins Street colloquially known as?
12. Since when has the eastern end of Collins Street been known as the “Paris End”?
13. Why is the eastern end of Collins Street called the “Paris End”?
14. What features are found at the eastern end of Collins Street?
15. What was the first location in Melbourne for sidewalk cafes?
16. Which street blocks became the financial heart of Melbourne in the 19th century?
17. Which street or area centered around Queen Street became the financial heart of Melbourne?
18. What kinds of businesses were historically preferred on blocks centered around Queen Street?
19. Does Collins Street still contain prestigious office blocks and skyscrapers?
20. Where along Collins Street are the most prestigious office blocks and skyscrapers found?
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
    class Location(Thing):
        pass

    class Country(Location):
        pass

    class State(Location):
        pass

    class City(Location):
        pass

    class Street(Location):
        pass

    class MajorStreet(Street):
        pass

    class StreetSection(Location):
        pass

    class BlockArea(Location):
        pass

    class Settlement(Location):
        pass

    class SurveyPlan(Thing):
        pass

    class Person(Thing):
        pass

    class LieutenantGovernor(Person):
        pass

    class Organization(Thing):
        pass

    class Bank(Organization):
        pass

    class InsuranceCompany(Organization):
        pass

    class Boutique(Organization):
        pass

    class Cafe(Organization):
        pass

    class Building(Thing):
        pass

    class HeritageBuilding(Building):
        pass

    class OfficeBlock(Building):
        pass

    class Skyscraper(Building):
        pass

    class StreetTree(Thing):
        pass

    class Collection(Thing):
        pass

    class Nickname(Thing):
        pass

    class locatedInCity(ObjectProperty, FunctionalProperty):
        domain = [Location]
        range = [City]

    class locatedInState(ObjectProperty, FunctionalProperty):
        domain = [Location]
        range = [State]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [Location]
        range = [Country]

    class inCentreOf(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [City]

    class laidOutIn(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [SurveyPlan]

    class surveyedCity(ObjectProperty, FunctionalProperty):
        domain = [SurveyPlan]
        range = [City]

    class createdYear(DataProperty, FunctionalProperty):
        domain = [SurveyPlan]
        range = [int]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [Person]

    class helpedEstablish(ObjectProperty):
        domain = [Person]
        range = [Settlement]

    class locatedAt(ObjectProperty, FunctionalProperty):
        domain = [Settlement]
        range = [Location]

    class establishedYear(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [int]

    class partOfStreet(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Street]

    class colloquiallyKnownAs(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Nickname]

    class knownSince(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [str]

    class dueToFeature(ObjectProperty):
        domain = [StreetSection]
        range = [Collection]

    class firstLocationFor(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Collection]

    class centeredAround(ObjectProperty, FunctionalProperty):
        domain = [BlockArea]
        range = [Street]

    class becameFinancialHeartOf(ObjectProperty, FunctionalProperty):
        domain = [BlockArea]
        range = [City]

    class sinceCentury(DataProperty, FunctionalProperty):
        domain = [BlockArea]
        range = [str]

    class preferredHomeOf(ObjectProperty):
        domain = [BlockArea]
        range = [Collection]

    class foundAt(ObjectProperty, FunctionalProperty):
        domain = [Collection]
        range = [Location]

    class foundAlong(ObjectProperty, FunctionalProperty):
        domain = [Collection]
        range = [Street]

    collinsStreet = MajorStreet("CollinsStreet")
    collinsStreet.label = "Collins Street"

    melbourne = City("Melbourne")
    melbourne.label = "Melbourne"

    victoria = State("Victoria")
    victoria.label = "Victoria"

    australia = Country("Australia")
    australia.label = "Australia"

    hoddleGrid = SurveyPlan("HoddleGridOriginal1837")
    hoddleGrid.label = "the original 1837 Hoddle Grid"
    hoddleGrid.surveyedCity = melbourne
    hoddleGrid.createdYear = 1837

    davidCollins = LieutenantGovernor("DavidCollins")
    davidCollins.label = "Lieutenant-Governor David Collins"

    sorrento = Location("Sorrento")
    sorrento.label = "Sorrento"

    shortLivedSettlement = Settlement("ShortLivedSettlementAtSorrento")
    shortLivedSettlement.label = "a short-lived settlement at Sorrento"
    shortLivedSettlement.locatedAt = sorrento
    shortLivedSettlement.establishedYear = 1803
    davidCollins.helpedEstablish = [shortLivedSettlement]

    parisEnd = Nickname("ParisEnd")
    parisEnd.label = "the ' Paris End '"

    collinsStreetEasternEnd = StreetSection("CollinsStreetEasternEnd")
    collinsStreetEasternEnd.label = "the eastern end of Collins Street"
    collinsStreetEasternEnd.partOfStreet = collinsStreet
    collinsStreetEasternEnd.colloquiallyKnownAs = parisEnd
    collinsStreetEasternEnd.knownSince = "the 1950s"

    numerousHeritageBuildings = Collection("NumerousHeritageBuildings")
    numerousHeritageBuildings.label = "numerous heritage buildings"
    numerousHeritageBuildings.foundAt = collinsStreetEasternEnd

    oldStreetTrees = Collection("OldStreetTrees")
    oldStreetTrees.label = "old street trees"
    oldStreetTrees.foundAt = collinsStreetEasternEnd

    highEndShoppingBoutiques = Collection("HighEndShoppingBoutiques")
    highEndShoppingBoutiques.label = "high-end shopping boutiques"
    highEndShoppingBoutiques.foundAt = collinsStreetEasternEnd

    firstSidewalkCafes = Collection("FirstSidewalkCafesInTheCity")
    firstSidewalkCafes.label = "the first sidewalk cafes in the city"
    firstSidewalkCafes.foundAt = collinsStreetEasternEnd
    collinsStreetEasternEnd.firstLocationFor = firstSidewalkCafes
    collinsStreetEasternEnd.dueToFeature = [
        numerousHeritageBuildings,
        oldStreetTrees,
        highEndShoppingBoutiques,
        firstSidewalkCafes,
    ]

    queenStreet = Street("QueenStreet")
    queenStreet.label = "Queen Street"

    queenStreetBlocks = BlockArea("BlocksFurtherWestAroundQueenStreet")
    queenStreetBlocks.label = "Blocks further west centred around Queen Street"
    queenStreetBlocks.partOfStreet = collinsStreet
    queenStreetBlocks.centeredAround = queenStreet
    queenStreetBlocks.becameFinancialHeartOf = melbourne
    queenStreetBlocks.sinceCentury = "19th century"

    majorBanksAndInsuranceCompanies = Collection("MajorBanksAndInsuranceCompanies")
    majorBanksAndInsuranceCompanies.label = "major banks and insurance companies"
    majorBanksAndInsuranceCompanies.foundAt = queenStreetBlocks
    queenStreetBlocks.preferredHomeOf = [majorBanksAndInsuranceCompanies]

    mostPrestigiousOfficeBlocksAndSkyscrapers = Collection("MostPrestigiousOfficeBlocksAndSkyscrapers")
    mostPrestigiousOfficeBlocksAndSkyscrapers.label = "the most prestigious office blocks and skyscrapers"
    mostPrestigiousOfficeBlocksAndSkyscrapers.foundAlong = collinsStreet

    collinsStreet.locatedInCity = melbourne
    collinsStreet.locatedInState = victoria
    collinsStreet.locatedInCountry = australia
    collinsStreet.inCentreOf = melbourne
    collinsStreet.laidOutIn = hoddleGrid
    collinsStreet.namedAfter = davidCollins

    melbourne.locatedInState = victoria
    melbourne.locatedInCountry = australia

    victoria.locatedInCountry = australia


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
