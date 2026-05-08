"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

What is Collins Street?
Where is Collins Street located?
In which city is Collins Street situated?
In which state is Collins Street situated?
In which country is Collins Street situated?
Is Collins Street a major street in the centre of Melbourne?
When was Collins Street laid out?
Was Collins Street part of the original 1837 Hoddle Grid?
What was the first survey of Melbourne called?
Did Collins Street become the most desired address in Melbourne soon after it was laid out?
After whom was Collins Street named?
Who was David Collins?
What role did David Collins hold?
What did David Collins lead in 1803?
Where did David Collins establish a short-lived settlement?
When was the settlement at Sorrento established?
Which part of Collins Street is known as the Paris End?
Since when has the eastern end of Collins Street been known as the Paris End?
Why is the eastern end of Collins Street called the Paris End?
Does the Paris End contain numerous heritage buildings?
Does the Paris End contain old street trees?
Does the Paris End contain high-end shopping boutiques?
Was the Paris End the location of the first sidewalk cafes in Melbourne?
Which section of Collins Street became the financial heart of Melbourne in the 19th century?
Around which street were the western blocks of Collins Street centred?
When did the western section of Collins Street become the financial heart of Melbourne?
What kinds of institutions preferred to locate on Collins Street in the 19th century?
Were major banks located on Collins Street in the 19th century?
Were insurance companies located on Collins Street in the 19th century?
Does Collins Street continue to be associated with major financial and commercial activity today?
Are the most prestigious office blocks in Melbourne found along Collins Street?
Are skyscrapers found along Collins Street?
Which street in Melbourne is associated with prestigious office blocks and skyscrapers?
What historical, commercial, and cultural characteristics are associated with Collins Street?
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
    Accomplishment,
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import constantPartOf, temporallyLocatedAt


with core:
    class Place(NonAgentivePhysicalObject):
        pass


    class Street(Place):
        pass


    class MajorStreet(Street):
        pass


    class StreetSection(Street):
        is_a = [constantPartOf.some(Street)]


    class EasternStreetEnd(StreetSection):
        pass


    class WesternStreetSection(StreetSection):
        pass


    class FinancialStreetSection(WesternStreetSection):
        pass


    class City(Place):
        pass


    class State(Place):
        pass


    class Country(Place):
        pass


    class Town(Place):
        pass


    class Person(AgentivePhysicalObject):
        pass


    class LieutenantGovernor(Person):
        pass


    class Organization(Society):
        pass


    class Bank(Organization):
        pass


    class InsuranceCompany(Organization):
        pass


    class Survey(Accomplishment):
        is_a = [temporallyLocatedAt.some(TimeInterval)]


    class HeritageBuilding(NonAgentivePhysicalObject):
        pass


    class StreetTree(NonAgentivePhysicalObject):
        pass


    class ShoppingBoutique(NonAgentivePhysicalObject):
        pass


    class SidewalkCafe(NonAgentivePhysicalObject):
        pass


    class OfficeBlock(NonAgentivePhysicalObject):
        pass


    class PrestigiousOfficeBlock(OfficeBlock):
        pass


    class Skyscraper(NonAgentivePhysicalObject):
        pass


    class locatedIn(constantPartOf):
        domain = [Place]
        range = [Place]


    class sectionOf(constantPartOf):
        domain = [StreetSection]
        range = [Street]


    class easternEndOf(sectionOf):
        domain = [EasternStreetEnd]
        range = [Street]


    class inCentreOf(locatedIn):
        domain = [Street]
        range = [City]


    class laidOutInSurvey(ObjectProperty):
        domain = [Street]
        range = [Survey]


    class surveyedPlace(ObjectProperty):
        domain = [Survey]
        range = [Place]


    class namedAfter(ObjectProperty):
        domain = [Place]
        range = [Person]


    class knownSince(ObjectProperty):
        domain = [StreetSection]
        range = [TimeInterval]


    class centredAround(ObjectProperty):
        domain = [StreetSection]
        range = [Street]


    class financialHeartOf(ObjectProperty):
        domain = [StreetSection]
        range = [City]


    class ledSettlementEstablishmentAt(ObjectProperty):
        domain = [Person]
        range = [Place]


    class ledSettlementEstablishmentIn(ObjectProperty):
        domain = [Person]
        range = [TimeInterval]


    class isMajor(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class becameMostDesiredAddressSoonAfterLayout(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class knownForHeritageBuildings(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [bool]


    class knownForOldStreetTrees(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [bool]


    class knownForHighEndShoppingBoutiques(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [bool]


    class locationOfFirstSidewalkCafesInCity(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [bool]


    class associatedWithMajorBanksInNineteenthCentury(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class associatedWithInsuranceCompaniesInNineteenthCentury(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class financialTraditionContinuesToday(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class hasPrestigiousOfficeBlocks(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class hasSkyscrapers(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [bool]


    class historicalCommercialCulturalCharacteristics(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [str]


    CollinsStreet = MajorStreet("CollinsStreet")
    CollinsStreet.label = "Collins Street"
    Melbourne = City("Melbourne")
    Melbourne.label = "Melbourne"
    Victoria = State("Victoria")
    Victoria.label = "Victoria"
    Australia = Country("Australia")
    Australia.label = "Australia"
    HoddleGrid = Survey("HoddleGrid")
    HoddleGrid.label = "Hoddle Grid"
    DavidCollins = LieutenantGovernor("DavidCollins")
    DavidCollins.label = "David Collins"
    Sorrento = Town("Sorrento")
    Sorrento.label = "Sorrento"
    ParisEnd = EasternStreetEnd("ParisEnd")
    ParisEnd.label = "Paris End"
    QueenStreet = Street("QueenStreet")
    QueenStreet.label = "Queen Street"
    Year1803 = TimeInterval("Year1803")
    Year1803.label = "1803"
    Year1837 = TimeInterval("Year1837")
    Year1837.label = "1837"
    The1950s = TimeInterval("The1950s")
    The1950s.label = "the 1950s"
    NineteenthCentury = TimeInterval("NineteenthCentury")
    NineteenthCentury.label = "the 19th century"

    CollinsStreet.isMajor = True
    CollinsStreet.inCentreOf.append(Melbourne)
    CollinsStreet.locatedIn.append(Melbourne)
    CollinsStreet.locatedIn.append(Victoria)
    CollinsStreet.locatedIn.append(Australia)
    CollinsStreet.laidOutInSurvey.append(HoddleGrid)
    CollinsStreet.namedAfter.append(DavidCollins)
    CollinsStreet.becameMostDesiredAddressSoonAfterLayout = True
    CollinsStreet.associatedWithMajorBanksInNineteenthCentury = True
    CollinsStreet.associatedWithInsuranceCompaniesInNineteenthCentury = True
    CollinsStreet.financialTraditionContinuesToday = True
    CollinsStreet.hasPrestigiousOfficeBlocks = True
    CollinsStreet.hasSkyscrapers = True
    CollinsStreet.historicalCommercialCulturalCharacteristics = (
        "major street; central Melbourne location; original 1837 Hoddle Grid layout; "
        "prestigious address; Paris End heritage buildings, street trees, boutiques, "
        "and first sidewalk cafes; nineteenth-century financial heart; prestigious "
        "office blocks and skyscrapers"
    )

    Melbourne.locatedIn.append(Victoria)
    Victoria.locatedIn.append(Australia)

    HoddleGrid.surveyedPlace.append(Melbourne)
    HoddleGrid.temporallyLocatedAt = Year1837

    DavidCollins.ledSettlementEstablishmentAt.append(Sorrento)
    DavidCollins.ledSettlementEstablishmentIn.append(Year1803)

    ParisEnd.easternEndOf.append(CollinsStreet)
    ParisEnd.knownSince.append(The1950s)
    ParisEnd.knownForHeritageBuildings = True
    ParisEnd.knownForOldStreetTrees = True
    ParisEnd.knownForHighEndShoppingBoutiques = True
    ParisEnd.locationOfFirstSidewalkCafesInCity = True

    QueenStreet.locatedIn.append(Melbourne)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
