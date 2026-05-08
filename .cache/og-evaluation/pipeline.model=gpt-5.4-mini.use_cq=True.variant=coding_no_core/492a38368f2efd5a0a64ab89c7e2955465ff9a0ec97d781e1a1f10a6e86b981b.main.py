"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is the alternative name of Verbena?
2. In which county is Verbena located?
3. In which state is Verbena located?
4. Is Verbena an incorporated or unincorporated community?
5. What is Verbena named after?
6. During which historical period did Verbena develop into a popular resort location?
7. For which group of people did Verbena become a popular resort location?
8. What event(s) contributed to Verbena’s development as a resort location?
9. What types of historic buildings are found in Verbena?
10. Which of Verbena’s historic buildings have undergone recent renovation and restoration?
11. What transportation infrastructure was Verbena built beside?
12. Which company currently owns the railroad beside which Verbena was built?
13. What facilities did Verbena have in its heyday?
14. Which of Verbena’s historic buildings still stands today?
15. On which road is the Verbena United Methodist Church located?
16. Near what part of town is the Verbena United Methodist Church located?
17. What was Verbena’s population according to the 1890 U.S. Census?
18. Was Verbena the largest community in Chilton County in 1890?
19. What was the largest community in Chilton County according to the 1890 census?
20. What was Verbena’s status in relation to Chilton County’s communities in 1890?
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

    class Community(Place):
        pass

    class UnincorporatedCommunity(Community):
        pass

    class City(Community):
        pass

    class County(Place):
        pass

    class State(Place):
        pass

    class Country(Place):
        pass

    class ResortLocation(Place):
        pass

    class PopularResortLocation(ResortLocation):
        pass

    class Citizenry(Thing):
        pass

    class MoreAffluentCitizenry(Citizenry):
        pass

    class Organization(Thing):
        pass

    class TransportationCompany(Organization):
        pass

    class Census(Organization):
        pass

    class Infrastructure(Thing):
        pass

    class TransportInfrastructure(Infrastructure):
        pass

    class Railroad(TransportInfrastructure):
        pass

    class Road(TransportInfrastructure):
        pass

    class Building(Thing):
        pass

    class HistoricBuilding(Building):
        pass

    class Facility(Building):
        pass

    class StatelyHome(HistoricBuilding):
        pass

    class RenovatedRestoredStatelyHome(StatelyHome):
        pass

    class Hotel(Facility):
        pass

    class Bank(Facility):
        pass

    class PostOffice(Facility):
        pass

    class GeneralStore(Facility):
        pass

    class Church(Building):
        pass

    class Event(Thing):
        pass

    class Outbreak(Event):
        pass

    class YellowFeverOutbreaks(Outbreak):
        pass

    class TimePeriod(Thing):
        pass

    class HistoricalPeriod(TimePeriod):
        pass

    class Late19thAndEarly20thCenturies(HistoricalPeriod):
        pass

    class Year(TimePeriod):
        pass

    class TownCenter(Place):
        pass

    class RailroadCurrentlyOwnedByCSXTransportation(Railroad):
        pass

    class MoreAffluentCitizenryOfMontgomery(MoreAffluentCitizenry):
        pass

    class alsoKnownAs(ObjectProperty, SymmetricProperty):
        domain = [Thing]
        range = [Thing]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class capitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [State]

    class namedAfterText(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class developedInto(ObjectProperty):
        domain = [Community]
        range = [ResortLocation]

    class developedDuring(ObjectProperty):
        domain = [Community]
        range = [Event]

    class popularWith(ObjectProperty):
        domain = [Place]
        range = [Citizenry]

    class fromPlace(ObjectProperty, FunctionalProperty):
        domain = [Citizenry]
        range = [Place]

    class builtBeside(ObjectProperty):
        domain = [Community]
        range = [TransportInfrastructure]

    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [Railroad]
        range = [Organization]

    class hasHistoricBuilding(ObjectProperty):
        domain = [Place]
        range = [HistoricBuilding]

    class hasFacility(ObjectProperty):
        domain = [Community]
        range = [Facility]

    class locatedOn(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Road]

    class near(ObjectProperty):
        domain = [Thing]
        range = [Place]

    class occurredDuring(ObjectProperty):
        domain = [Event]
        range = [TimePeriod]

    class conductedIn(ObjectProperty, FunctionalProperty):
        domain = [Census]
        range = [Year]

    class populationAccordingTo(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range = [Census]

    class largestCommunityIn(ObjectProperty):
        domain = [Community]
        range = [County]

    class hasPopulation(DataProperty, FunctionalProperty):
        domain = [Community]
        range = [int]

    class numberOfHotels(DataProperty, FunctionalProperty):
        domain = [Community]
        range = [int]

    class recentlyRenovated(DataProperty, FunctionalProperty):
        domain = [HistoricBuilding]
        range = [bool]

    class recentlyRestored(DataProperty, FunctionalProperty):
        domain = [HistoricBuilding]
        range = [bool]

    class stillStands(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [bool]

    Verbena = UnincorporatedCommunity("Verbena")
    Verbena.label = "Verbena"
    Summerfield = UnincorporatedCommunity("Summerfield")
    Summerfield.label = "Summerfield"
    ChiltonCounty = County("ChiltonCounty")
    ChiltonCounty.label = "Chilton County"
    Alabama = State("Alabama")
    Alabama.label = "Alabama"
    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"
    Montgomery = City("Montgomery")
    Montgomery.label = "Montgomery"
    CSXTransportation = TransportationCompany("CSXTransportation")
    CSXTransportation.label = "CSX Transportation"
    VerbenaUnitedMethodistChurch = Church("VerbenaUnitedMethodistChurch")
    VerbenaUnitedMethodistChurch.label = "Verbena United Methodist Church"
    CountyRoad59 = Road("CountyRoad59")
    CountyRoad59.label = "County Road 59"
    USCensus = Census("USCensus")
    USCensus.label = "U.S. Census"
    Year1890 = Year("Year1890")
    Year1890.label = "1890"

    Verbena.alsoKnownAs = [Summerfield]
    Verbena.locatedIn = [ChiltonCounty, Alabama, UnitedStates]
    ChiltonCounty.locatedIn = [Alabama, UnitedStates]
    Alabama.locatedIn = [UnitedStates]
    Montgomery.locatedIn = [Alabama, UnitedStates]
    Montgomery.capitalOf = Alabama
    Verbena.namedAfterText = "the indigenous flower"
    Verbena.populationAccordingTo = USCensus
    Verbena.hasPopulation = 756
    Verbena.numberOfHotels = 2
    Verbena.largestCommunityIn = [ChiltonCounty]
    Verbena.is_a.append(developedInto.some(PopularResortLocation))
    Verbena.is_a.append(developedDuring.some(YellowFeverOutbreaks))
    Verbena.is_a.append(popularWith.some(MoreAffluentCitizenryOfMontgomery))
    Verbena.is_a.append(hasHistoricBuilding.some(StatelyHome))
    Verbena.is_a.append(hasHistoricBuilding.some(RenovatedRestoredStatelyHome))
    Verbena.is_a.append(hasFacility.some(Hotel))
    Verbena.is_a.append(hasFacility.some(Bank))
    Verbena.is_a.append(hasFacility.some(PostOffice))
    Verbena.is_a.append(hasFacility.some(GeneralStore))
    Verbena.is_a.append(builtBeside.some(RailroadCurrentlyOwnedByCSXTransportation))

    RailroadCurrentlyOwnedByCSXTransportation.is_a.append(ownedBy.value(CSXTransportation))
    MoreAffluentCitizenryOfMontgomery.is_a.append(fromPlace.value(Montgomery))
    YellowFeverOutbreaks.is_a.append(occurredDuring.some(Late19thAndEarly20thCenturies))
    RenovatedRestoredStatelyHome.is_a.append(recentlyRenovated.value(True))
    RenovatedRestoredStatelyHome.is_a.append(recentlyRestored.value(True))
    VerbenaUnitedMethodistChurch.locatedOn = CountyRoad59
    VerbenaUnitedMethodistChurch.locatedIn = [Verbena]
    VerbenaUnitedMethodistChurch.is_a.append(HistoricBuilding)
    VerbenaUnitedMethodistChurch.is_a.append(near.some(TownCenter))
    VerbenaUnitedMethodistChurch.stillStands = True
    USCensus.conductedIn = Year1890


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
