"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

What is Verbena also known as?
What type of settlement is Verbena?
In which county is Verbena located?
In which part of Chilton County is Verbena located?
In which state is Verbena located?
In which country is Verbena located?
What was Verbena named after?
How did Verbena develop historically?
Who were the primary visitors or residents associated with Verbena’s resort period?
From which city did the affluent citizens who visited Verbena come?
What role did yellow fever outbreaks play in Verbena’s development?
During which time period did Verbena become a popular resort location?
What historic features of Verbena reflect its resort past?
Which homes in Verbena have undergone recent renovation and restoration?
What transportation infrastructure was Verbena built beside?
Who currently owns the railroad beside which Verbena was built?
What establishments existed in Verbena during its heyday?
How many hotels did Verbena have in its heyday?
Did Verbena have a bank during its heyday?
Did Verbena have a post office during its heyday?
Did Verbena have a general store during its heyday?
Which historic buildings in Verbena are no longer standing or are boarded up?
Which notable building still stands in Verbena today?
Where is the Verbena United Methodist Church located?
Is the Verbena United Methodist Church near the town center?
What was the population of Verbena according to the 1890 U.S. Census?
Was Verbena the largest community in Chilton County in 1890?
How did Verbena rank among communities in Chilton County in 1890?
What relationship does Montgomery have to the state of Alabama?
What is the historical significance of Verbena within Chilton County?
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

    class AdministrativeArea(Location):
        pass

    class Country(AdministrativeArea):
        pass

    class State(AdministrativeArea):
        pass

    class County(AdministrativeArea):
        pass

    class Settlement(Location):
        pass

    class Community(Settlement):
        pass

    class UnincorporatedCommunity(Community):
        pass

    class City(Settlement):
        pass

    class PlaceName(Thing):
        pass

    class Organization(Thing):
        pass

    class Company(Organization):
        pass

    class StatisticalSurvey(Thing):
        pass

    class Census(StatisticalSurvey):
        pass

    class TimeEntity(Thing):
        pass

    class TimePeriod(TimeEntity):
        pass

    class Year(TimeEntity):
        pass

    class Event(Thing):
        pass

    class DiseaseOutbreak(Event):
        pass

    class YellowFeverOutbreak(DiseaseOutbreak):
        pass

    class Infrastructure(Thing):
        pass

    class TransportationInfrastructure(Infrastructure):
        pass

    class Railroad(TransportationInfrastructure):
        pass

    class Road(TransportationInfrastructure):
        pass

    class Building(Thing):
        pass

    class Home(Building):
        pass

    class StatelyHome(Home):
        pass

    class Establishment(Building):
        pass

    class Hotel(Establishment):
        pass

    class Bank(Establishment):
        pass

    class PostOffice(Establishment):
        pass

    class GeneralStore(Establishment):
        pass

    class Church(Building):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Location]

    class alsoKnownAs(ObjectProperty):
        domain = [Settlement]
        range = [PlaceName]

    class capitalOf(ObjectProperty):
        domain = [City]
        range = [State]

    class resortVisitorsFrom(ObjectProperty):
        domain = [Settlement]
        range = [City]

    class developedDuring(ObjectProperty):
        domain = [Settlement]
        range = [TimePeriod]

    class developmentAssociatedWith(ObjectProperty):
        domain = [Settlement]
        range = [DiseaseOutbreak]

    class adjacentRailroadOwnedBy(ObjectProperty):
        domain = [Settlement]
        range = [Company]

    class populationReportedBy(ObjectProperty):
        domain = [Settlement]
        range = [Census]

    class populationReferenceYear(ObjectProperty):
        domain = [Settlement]
        range = [Year]

    class largestCommunityIn(ObjectProperty):
        domain = [Settlement]
        range = [County]

    class rankingReferenceYear(ObjectProperty):
        domain = [Settlement]
        range = [Year]

    class locatedOnRoad(ObjectProperty):
        domain = [Building]
        range = [Road]

    class locatedInPartDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class namedAfterDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class developedIntoDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class resortVisitorDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class historicFeatureDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class renovatedFeatureDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class builtBesideInfrastructureDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class heydayEstablishmentsDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class hotelCountInHeyday(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [int]

    class hadBankInHeyday(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [bool]

    class hadPostOfficeInHeyday(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [bool]

    class hadGeneralStoreInHeyday(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [bool]

    class currentConditionDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [bool]

    class nearTownCenter(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [bool]

    class populationCount(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [int]

    class communityRankInCounty(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [int]

    class historicalSignificanceDescription(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range = [str]

    UnincorporatedCommunity.is_a.append(locatedIn.some(County))
    County.is_a.append(locatedIn.some(State))
    State.is_a.append(locatedIn.some(Country))
    Church.is_a.append(locatedOnRoad.some(Road))

    verbena = UnincorporatedCommunity("Verbena")
    verbena.label = "Verbena"

    summerfield = PlaceName("Summerfield")
    summerfield.label = "Summerfield"

    chilton_county = County("ChiltonCounty")
    chilton_county.label = "Chilton County"

    alabama = State("Alabama")
    alabama.label = "Alabama"

    united_states = Country("UnitedStates")
    united_states.label = "United States"

    montgomery = City("Montgomery")
    montgomery.label = "Montgomery"

    csx_transportation = Company("CSXTransportation")
    csx_transportation.label = "CSX Transportation"

    verbena_united_methodist_church = Church("VerbenaUnitedMethodistChurch")
    verbena_united_methodist_church.label = "Verbena United Methodist Church"

    county_road_59 = Road("CountyRoad59")
    county_road_59.label = "County Road 59"

    us_census = Census("USCensus")
    us_census.label = "U.S. Census"

    year_1890 = Year("Year1890")
    year_1890.label = "1890"

    late_19th_and_early_20th_centuries = TimePeriod("Late19thAndEarly20thCenturies")
    late_19th_and_early_20th_centuries.label = "late 19th and early 20th centuries"

    yellow_fever_outbreaks = YellowFeverOutbreak("YellowFeverOutbreaks")
    yellow_fever_outbreaks.label = "yellow fever outbreaks"

    chilton_county.locatedIn = [alabama]
    alabama.locatedIn = [united_states]
    montgomery.locatedIn = [alabama]
    montgomery.capitalOf = [alabama]

    verbena.alsoKnownAs = [summerfield]
    verbena.locatedIn = [chilton_county]
    verbena.locatedInPartDescription = "southeastern"
    verbena.namedAfterDescription = "the indigenous flower"
    verbena.developedIntoDescription = "a popular resort location"
    verbena.resortVisitorDescription = "the more affluent citizenry of Montgomery"
    verbena.resortVisitorsFrom = [montgomery]
    verbena.developmentAssociatedWith = [yellow_fever_outbreaks]
    verbena.developedDuring = [late_19th_and_early_20th_centuries]
    verbena.historicFeatureDescription = "stately homes"
    verbena.renovatedFeatureDescription = "some stately homes"
    verbena.builtBesideInfrastructureDescription = "railroad"
    verbena.adjacentRailroadOwnedBy = [csx_transportation]
    verbena.heydayEstablishmentsDescription = "two hotels, a bank, a post office, and a general store"
    verbena.hotelCountInHeyday = 2
    verbena.hadBankInHeyday = True
    verbena.hadPostOfficeInHeyday = True
    verbena.hadGeneralStoreInHeyday = True
    verbena.currentConditionDescription = "Many of those buildings are gone or boarded up today"
    verbena.populationCount = 756
    verbena.populationReportedBy = [us_census]
    verbena.populationReferenceYear = [year_1890]
    verbena.largestCommunityIn = [chilton_county]
    verbena.rankingReferenceYear = [year_1890]
    verbena.communityRankInCounty = 1
    verbena.historicalSignificanceDescription = "the largest community in Chilton County in 1890"

    verbena_united_methodist_church.locatedIn = [verbena]
    verbena_united_methodist_church.locatedOnRoad = [county_road_59]
    verbena_united_methodist_church.stillStanding = True
    verbena_united_methodist_church.nearTownCenter = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
