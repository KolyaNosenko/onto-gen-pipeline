"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

What is Collins Street?
Where is Collins Street located?
In which city is Collins Street located?
In which state is Collins Street located?
In which country is Collins Street located?
Is Collins Street a major street in the centre of Melbourne?
When was Collins Street laid out?
Was Collins Street part of the original 1837 Hoddle Grid?
In what survey was Collins Street laid out?
When did Collins Street become the most desired address in Melbourne?
After whom was Collins Street named?
Who was David Collins?
What role did David Collins hold?
What group did David Collins lead?
What settlement did David Collins help establish?
Where was the settlement established by David Collins located?
When was the settlement at Sorrento established?
Was the settlement at Sorrento short-lived?
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
Did major banks have offices on Collins Street in the 19th century?
Did insurance companies have offices on Collins Street in the 19th century?
Does Collins Street continue to be associated with major financial institutions today?
Are prestigious office blocks located along Collins Street?
Are skyscrapers located along Collins Street?
Which street in Melbourne is associated with both heritage shopping precincts and financial institutions?
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
    class Place(Thing):
        pass

    class Country(Place):
        pass

    class State(Place):
        pass

    class City(Place):
        pass

    class Town(Place):
        pass

    class Street(Place):
        pass

    class MajorStreet(Street):
        pass

    class StreetSection(Place):
        pass

    class Survey(Thing):
        pass

    class UrbanGridSurvey(Survey):
        pass

    class Person(Thing):
        pass

    class GovernmentOfficial(Person):
        pass

    class LieutenantGovernor(GovernmentOfficial):
        pass

    class Group(Thing):
        pass

    class SettlerGroup(Group):
        pass

    class Settlement(Place):
        pass

    class ShortLivedSettlement(Settlement):
        pass

    class TimePeriod(Thing):
        pass

    class Year(TimePeriod):
        pass

    class Decade(TimePeriod):
        pass

    class Century(TimePeriod):
        pass

    class UrbanFeature(Thing):
        pass

    class HeritageBuilding(UrbanFeature):
        pass

    class StreetTree(UrbanFeature):
        pass

    class ShoppingBoutique(UrbanFeature):
        pass

    class Cafe(UrbanFeature):
        pass

    class SidewalkCafe(Cafe):
        pass

    class Institution(Thing):
        pass

    class FinancialInstitution(Institution):
        pass

    class Bank(FinancialInstitution):
        pass

    class InsuranceCompany(FinancialInstitution):
        pass

    class Building(UrbanFeature):
        pass

    class OfficeBlock(Building):
        pass

    class Skyscraper(Building):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class inCentreOf(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [City]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class laidOutInSurvey(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range = [Survey]

    class surveyOf(ObjectProperty, FunctionalProperty):
        domain = [Survey]
        range = [City]

    class occurredIn(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [TimePeriod]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Person]

    class led(ObjectProperty):
        domain = [Person]
        range = [Group]

    class helpedEstablish(ObjectProperty):
        domain = [Person]
        range = [Settlement]

    class knownSince(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [TimePeriod]

    class hasSection(ObjectProperty):
        domain = [Street]
        range = [StreetSection]

    class centredAround(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [Street]

    class financialHeartOf(ObjectProperty):
        domain = [StreetSection]
        range = [City]

    class preferredHomeOf(ObjectProperty):
        domain = [Place]
        range = [Institution]

    class hasFeature(ObjectProperty):
        domain = [Place]
        range = [UrbanFeature]

    class locationOf(ObjectProperty):
        domain = [Place]
        range = [UrbanFeature]

    class hasStructure(ObjectProperty):
        domain = [Place]
        range = [Building]

    class mostDesiredAddressOf(ObjectProperty):
        domain = [Street]
        range = [City]

    class mostDesiredAddressTimeDescription(DataProperty, FunctionalProperty):
        domain = [Street]
        range = [str]

    class colloquialNameReasonDescription(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range = [str]

    class currentAssociationDescription(DataProperty, FunctionalProperty):
        domain = [Place]
        range = [str]

    class ParisEndPrecinct(StreetSection):
        is_a = [
            partOf.some(Street),
            knownSince.some(Decade),
            hasFeature.some(HeritageBuilding),
            hasFeature.some(StreetTree),
            hasFeature.some(ShoppingBoutique),
            locationOf.some(SidewalkCafe),
        ]

    class FinancialStreetSection(StreetSection):
        is_a = [
            partOf.some(Street),
            centredAround.some(Street),
            financialHeartOf.some(City),
            occurredIn.some(Century),
            preferredHomeOf.some(Bank),
            preferredHomeOf.some(InsuranceCompany),
            hasStructure.some(OfficeBlock),
            hasStructure.some(Skyscraper),
        ]

    australia = Country("AustraliaCountry")
    australia.label = "Australia"

    victoria = State("VictoriaState")
    victoria.label = "Victoria"
    victoria.locatedIn = [australia]

    melbourne = City("MelbourneCity")
    melbourne.label = "Melbourne"
    melbourne.locatedIn = [victoria, australia]

    sorrento = Town("SorrentoTown")
    sorrento.label = "Sorrento"
    sorrento.locatedIn = [victoria, australia]

    queenStreet = Street("QueenStreetIndividual")
    queenStreet.label = "Queen Street"
    queenStreet.locatedIn = [melbourne, victoria, australia]

    year1803 = Year("Year1803")
    year1803.label = "1803"

    year1837 = Year("Year1837")
    year1837.label = "1837"

    the1950s = Decade("The1950s")
    the1950s.label = "1950s"

    nineteenthCentury = Century("NineteenthCentury")
    nineteenthCentury.label = "19th century"

    hoddleGrid = UrbanGridSurvey("Original1837HoddleGrid")
    hoddleGrid.label = ["the original 1837 Hoddle Grid", "Hoddle Grid", "first survey of Melbourne"]
    hoddleGrid.surveyOf = melbourne
    hoddleGrid.occurredIn = year1837

    davidCollins = LieutenantGovernor("DavidCollinsPerson")
    davidCollins.label = ["David Collins", "Lieutenant - Governor David Collins"]

    settlerGroup = SettlerGroup("SettlerGroupForSorrento")
    settlerGroup.label = "group of settlers"

    sorrentoSettlement = ShortLivedSettlement("SorrentoSettlement")
    sorrentoSettlement.label = "short - lived settlement at Sorrento"
    sorrentoSettlement.locatedIn = [sorrento, victoria, australia]
    sorrentoSettlement.occurredIn = year1803

    collinsStreet = MajorStreet("CollinsStreetIndividual")
    collinsStreet.label = "Collins Street"
    collinsStreet.locatedIn = [melbourne, victoria, australia]
    collinsStreet.inCentreOf = melbourne
    collinsStreet.laidOutInSurvey = hoddleGrid
    collinsStreet.partOf = [hoddleGrid]
    collinsStreet.namedAfter = davidCollins
    collinsStreet.mostDesiredAddressOf = [melbourne]
    collinsStreet.mostDesiredAddressTimeDescription = "soon after it was laid out"

    parisEnd = ParisEndPrecinct("ParisEndSection")
    parisEnd.label = ["' Paris End '", "Paris End", "eastern end of Collins Street"]
    parisEnd.partOf = [collinsStreet]
    parisEnd.knownSince = the1950s
    parisEnd.colloquialNameReasonDescription = (
        "due to its numerous heritage buildings, old street trees, "
        "high - end shopping boutiques, and as the location for the first "
        "sidewalk cafes in the city"
    )

    westernBlocks = FinancialStreetSection("WesternBlocksOfCollinsStreet")
    westernBlocks.label = "Blocks further west centred around Queen Street"
    westernBlocks.partOf = [collinsStreet]
    westernBlocks.centredAround = queenStreet
    westernBlocks.financialHeartOf = [melbourne]
    westernBlocks.occurredIn = nineteenthCentury
    westernBlocks.currentAssociationDescription = (
        "the tradition continues today with the most prestigious office "
        "blocks and skyscrapers found along its length"
    )

    collinsStreet.hasSection = [parisEnd, westernBlocks]
    davidCollins.led = [settlerGroup]
    davidCollins.helpedEstablish = [sorrentoSettlement]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
