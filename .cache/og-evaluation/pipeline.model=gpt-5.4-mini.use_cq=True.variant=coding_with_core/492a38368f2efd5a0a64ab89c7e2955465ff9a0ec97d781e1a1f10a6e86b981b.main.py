"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is the official and alternative name of Verbena?
2. In which county, state, and country is Verbena located?
3. Is Verbena an incorporated municipality or an unincorporated community?
4. What is Verbena named after?
5. During which historical period did Verbena develop into a popular resort location?
6. Which city’s affluent citizens used Verbena as a resort location?
7. What major public health events influenced Verbena’s development as a resort location?
8. What type of buildings are characteristic of Verbena’s streets?
9. Which of Verbena’s historic buildings have undergone renovation or restoration?
10. Along which transportation infrastructure was Verbena built?
11. Which company currently owns the railroad beside which Verbena was built?
12. What businesses and services existed in Verbena during its heyday?
13. Which historic buildings in Verbena no longer exist or are boarded up today?
14. Which church still stands in Verbena today?
15. On which road is the Verbena United Methodist Church located?
16. Near what part of town is the Verbena United Methodist Church situated?
17. What was Verbena’s population according to the 1890 U.S. Census?
18. How did Verbena’s 1890 population compare to other communities in Chilton County?
19. When did Verbena have its largest historical population according to the document?
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
    Event,
    NonAgentivePhysicalObject,
    PhysicalObject,
    SocialAgent,
    SocialObject,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class Place(SocialObject):
        pass

    class Community(Place):
        pass

    class IncorporatedMunicipality(Community):
        pass

    class UnincorporatedCommunity(Community):
        is_a = [Not(IncorporatedMunicipality)]

    class County(Place):
        pass

    class State(Place):
        pass

    class Country(Place):
        pass

    class City(Place):
        pass

    class Flower(PhysicalObject):
        pass

    class HistoricalPeriod(TimeInterval):
        pass

    class Outbreak(Event):
        pass

    class Census(Event):
        is_a = [temporallyLocatedAt.some(TimeInterval)]

    class Renovation(Event):
        pass

    class Restoration(Event):
        pass

    class Railroad(NonAgentivePhysicalObject):
        pass

    class TransportationCompany(SocialAgent):
        pass

    class Building(NonAgentivePhysicalObject):
        pass

    class Home(Building):
        pass

    class StatelyHome(Home):
        pass

    class Hotel(Building):
        pass

    class Bank(Building):
        pass

    class PostOffice(Building):
        pass

    class GeneralStore(Building):
        pass

    class Church(Building):
        pass

    class Road(NonAgentivePhysicalObject):
        pass

    class TownCenter(SpaceRegion):
        pass

    class locatedInCounty(ObjectProperty):
        domain = [Community]
        range = [County]

    class locatedInState(ObjectProperty):
        domain = [Place]
        range = [State]

    class locatedInCountry(ObjectProperty):
        domain = [Place]
        range = [Country]

    class capitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [State]

    class namedAfter(ObjectProperty):
        domain = [Community]
        range = [Flower]

    class developedDuring(ObjectProperty):
        domain = [Community]
        range = [HistoricalPeriod]

    class resortLocationForCity(ObjectProperty):
        domain = [Community]
        range = [City]

    class influencedBy(ObjectProperty):
        domain = [Community]
        range = [Outbreak]

    class builtBeside(ObjectProperty):
        domain = [Community]
        range = [Railroad]

    class currentlyOwnedBy(ObjectProperty, FunctionalProperty):
        domain = [Railroad]
        range = [TransportationCompany]

    class hasBuilding(ObjectProperty):
        domain = [Community]
        range = [Building]

    class underwent(ObjectProperty):
        domain = [Building]
        range = [Event]

    class locatedOn(ObjectProperty):
        domain = [Church]
        range = [Road]

    class near(ObjectProperty):
        domain = [Church]
        range = [SpaceRegion]

    class censusOf(ObjectProperty):
        domain = [Census]
        range = [Community]

    class population(DataProperty, FunctionalProperty):
        domain = [Census]
        range = [int]

    class RenovatedStatelyHome(StatelyHome):
        is_a = [underwent.some(Renovation)]

    class RestoredStatelyHome(StatelyHome):
        is_a = [underwent.some(Restoration)]

    Verbena = UnincorporatedCommunity("Verbena")
    Verbena.label = "Verbena"

    Summerfield = UnincorporatedCommunity("Summerfield")
    Summerfield.label = "Summerfield"
    Summerfield.equivalent_to = [Verbena]

    ChiltonCounty = County("ChiltonCounty")
    ChiltonCounty.label = "Chilton County"

    Alabama = State("Alabama")
    Alabama.label = "Alabama"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    Montgomery = City("Montgomery")
    Montgomery.label = "Montgomery"
    Montgomery.capitalOf = Alabama

    CSXTransportation = TransportationCompany("CSXTransportation")
    CSXTransportation.label = "CSX Transportation"

    VerbenaRailroad = Railroad("VerbenaRailroad")
    VerbenaRailroad.label = "the railroad"
    VerbenaRailroad.currentlyOwnedBy = CSXTransportation

    TheIndigenousFlower = Flower("TheIndigenousFlower")
    TheIndigenousFlower.label = "the indigenous flower"

    Late19thAndEarly20thCenturies = HistoricalPeriod("Late19thAndEarly20thCenturies")
    Late19thAndEarly20thCenturies.label = "the late 19th and early 20th centuries"

    YellowFeverOutbreaks = Outbreak("YellowFeverOutbreaks")
    YellowFeverOutbreaks.label = "the yellow fever outbreaks"

    VerbenaUnitedMethodistChurch = Church("VerbenaUnitedMethodistChurch")
    VerbenaUnitedMethodistChurch.label = "Verbena United Methodist Church"

    CountyRoad59 = Road("CountyRoad59")
    CountyRoad59.label = "County Road 59"

    VerbenaTownCenter = TownCenter("VerbenaTownCenter")
    VerbenaTownCenter.label = "the town's center"

    Year1890 = TimeInterval("Year1890")
    Year1890.label = "1890"

    USCensus1890 = Census("USCensus1890")
    USCensus1890.label = "U.S. Census"
    USCensus1890.temporallyLocatedAt = Year1890
    USCensus1890.censusOf.append(Verbena)
    USCensus1890.population = 756

    Verbena.locatedInCounty.append(ChiltonCounty)
    Verbena.locatedInState.append(Alabama)
    Verbena.locatedInCountry.append(UnitedStates)
    Verbena.namedAfter.append(TheIndigenousFlower)
    Verbena.developedDuring.append(Late19thAndEarly20thCenturies)
    Verbena.resortLocationForCity.append(Montgomery)
    Verbena.influencedBy.append(YellowFeverOutbreaks)
    Verbena.builtBeside.append(VerbenaRailroad)
    Verbena.hasBuilding.append(VerbenaUnitedMethodistChurch)
    Verbena.is_a.append(hasBuilding.some(StatelyHome))
    Verbena.is_a.append(hasBuilding.some(RenovatedStatelyHome))
    Verbena.is_a.append(hasBuilding.some(RestoredStatelyHome))
    Verbena.is_a.append(hasBuilding.some(Hotel))
    Verbena.is_a.append(hasBuilding.some(Bank))
    Verbena.is_a.append(hasBuilding.some(PostOffice))
    Verbena.is_a.append(hasBuilding.some(GeneralStore))
    Verbena.is_a.append(hasBuilding.some(Church))
    ChiltonCounty.locatedInState.append(Alabama)
    Alabama.locatedInCountry.append(UnitedStates)
    Montgomery.locatedInState.append(Alabama)
    VerbenaUnitedMethodistChurch.locatedOn.append(CountyRoad59)
    VerbenaUnitedMethodistChurch.near.append(VerbenaTownCenter)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
