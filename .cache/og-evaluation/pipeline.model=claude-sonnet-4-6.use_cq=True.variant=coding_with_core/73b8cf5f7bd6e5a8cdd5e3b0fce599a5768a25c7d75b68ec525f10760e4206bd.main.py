"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is the alternative name for Verbena?
2. In which county is Verbena located?
3. In which state is Verbena located?
4. What type of community is Verbena?
5. Where is Verbena situated within Chilton County?
6. After what was Verbena named?
7. Why did Verbena develop into a popular resort location?
8. Which city's affluent citizens used Verbena as a resort location?
9. What is the capital of Alabama?
10. During which time period did yellow fever outbreaks occur that influenced Verbena's development?
11. What types of buildings were present in Verbena during its heyday?
12. Which railroad company currently owns the railroad beside which Verbena was built?
13. Which religious building still stands in Verbena?
14. On which road is the Verbena United Methodist Church located?
15. What was the population of Verbena according to the U.S. Census in 1890?
16. What was Verbena's population ranking within Chilton County in 1890?
17. What has happened to many of the original buildings in Verbena?
18. What types of renovation have some of Verbena's historic homes undergone?
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
    Society,
    Accomplishment,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── Entity classes ────────────────────────────────────────────────────

    class HumanSettlement(NonAgentiveSocialObject):
        pass

    class UnincorporatedCommunity(HumanSettlement):
        pass

    class City(HumanSettlement):
        pass

    class AdministrativeDivision(NonAgentiveSocialObject):
        pass

    class County(AdministrativeDivision):
        pass

    class FederalState(AdministrativeDivision):
        pass

    class Nation(AdministrativeDivision):
        pass

    class Building(NonAgentivePhysicalObject):
        pass

    class Hotel(Building):
        pass

    class BankBuilding(Building):
        pass

    class PostOffice(Building):
        pass

    class GeneralStore(Building):
        pass

    class Church(Building):
        pass

    class ResidentialBuilding(Building):
        pass

    class Railroad(NonAgentivePhysicalObject):
        pass

    class Road(NonAgentivePhysicalObject):
        pass

    class TransportationCompany(Society):
        pass

    class Flower(NonAgentivePhysicalObject):
        pass

    class DiseaseOutbreak(Accomplishment):
        pass

    class CensusEvent(Accomplishment):
        pass

    class BuildingRenovation(Accomplishment):
        pass

    class BuildingRestoration(Accomplishment):
        pass

    # ── Object / Data properties ──────────────────────────────────────────

    class alternativeName(DataProperty, FunctionalProperty):
        domain = [HumanSettlement]
        range = [str]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [HumanSettlement, AdministrativeDivision, Building, Railroad]
        range = [AdministrativeDivision, HumanSettlement]

    class hasCapital(ObjectProperty, FunctionalProperty):
        domain = [FederalState]
        range = [City]

    class namedAfter(ObjectProperty):
        domain = [HumanSettlement]
        range = [Flower]

    class ownedBy(ObjectProperty):
        domain = [Railroad]
        range = [TransportationCompany]

    class locatedBeside(ObjectProperty):
        domain = [HumanSettlement]
        range = [Railroad]

    class locatedOn(ObjectProperty):
        domain = [Building]
        range = [Road]

    class hasBuilding(ObjectProperty):
        domain = [HumanSettlement]
        range = [Building]

    class hasPopulation(DataProperty, FunctionalProperty):
        domain = [HumanSettlement]
        range = [int]

    class populationRanking(DataProperty, FunctionalProperty):
        domain = [HumanSettlement]
        range = [int]

    class locatedInRegion(DataProperty, FunctionalProperty):
        domain = [HumanSettlement]
        range = [str]

    class servedAsResortFor(ObjectProperty):
        domain = [UnincorporatedCommunity]
        range = [City]

    class developedAsResortDueTo(ObjectProperty):
        domain = [HumanSettlement]
        range = [DiseaseOutbreak]

    class recordedBy(ObjectProperty):
        domain = [HumanSettlement]
        range = [CensusEvent]

    class hasCensusYear(DataProperty, FunctionalProperty):
        domain = [CensusEvent]
        range = [int]

    class underwentWork(ObjectProperty):
        domain = [Building]
        range = [BuildingRenovation, BuildingRestoration]

    # ── Named instances ───────────────────────────────────────────────────

    verbena = UnincorporatedCommunity("Verbena")
    verbena.label = "Verbena"
    verbena.alternativeName = "Summerfield"
    verbena.locatedInRegion = "southeastern"
    verbena.hasPopulation = 756
    verbena.populationRanking = 1

    chiltonCounty = County("ChiltonCounty")
    chiltonCounty.label = "Chilton County"

    alabama = FederalState("Alabama")
    alabama.label = "Alabama"

    unitedStates = Nation("UnitedStates")
    unitedStates.label = "United States"

    montgomery = City("Montgomery")
    montgomery.label = "Montgomery"

    verbenaFlower = Flower("VerbenaFlower")
    verbenaFlower.label = "Verbena"

    csxTransportation = TransportationCompany("CSXTransportation")
    csxTransportation.label = "CSX Transportation"

    verbenaRailroad = Railroad("VerbenaRailroad")
    verbenaRailroad.label = "railroad"

    verbenaUnitedMethodistChurch = Church("VerbenaUnitedMethodistChurch")
    verbenaUnitedMethodistChurch.label = "Verbena United Methodist Church"

    countyRoad59 = Road("CountyRoad59")
    countyRoad59.label = "County Road 59"

    yellowFeverOutbreaks = DiseaseOutbreak("YellowFeverOutbreaks")
    yellowFeverOutbreaks.label = "yellow fever outbreaks"

    late19thEarly20thCenturies = TimeInterval("Late19thEarly20thCenturies")
    late19thEarly20thCenturies.label = "late 19th and early 20th centuries"

    usCensus1890 = CensusEvent("USCensus1890")
    usCensus1890.label = "U.S. Census in 1890"
    usCensus1890.hasCensusYear = 1890

    year1890 = TimeInterval("Year1890")
    year1890.label = "1890"

    # ── Property value assignments ────────────────────────────────────────

    verbena.locatedIn.append(chiltonCounty)
    verbena.locatedIn.append(alabama)
    verbena.locatedIn.append(unitedStates)
    verbena.namedAfter.append(verbenaFlower)
    verbena.servedAsResortFor.append(montgomery)
    verbena.developedAsResortDueTo.append(yellowFeverOutbreaks)
    verbena.locatedBeside.append(verbenaRailroad)
    verbena.hasBuilding.append(verbenaUnitedMethodistChurch)
    verbena.recordedBy.append(usCensus1890)

    chiltonCounty.locatedIn.append(alabama)

    alabama.locatedIn.append(unitedStates)
    alabama.hasCapital = montgomery

    montgomery.locatedIn.append(alabama)

    verbenaRailroad.ownedBy.append(csxTransportation)

    verbenaUnitedMethodistChurch.locatedOn.append(countyRoad59)
    verbenaUnitedMethodistChurch.locatedIn.append(verbena)

    yellowFeverOutbreaks.temporallyLocatedAt = late19thEarly20thCenturies
    usCensus1890.temporallyLocatedAt = year1890


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
