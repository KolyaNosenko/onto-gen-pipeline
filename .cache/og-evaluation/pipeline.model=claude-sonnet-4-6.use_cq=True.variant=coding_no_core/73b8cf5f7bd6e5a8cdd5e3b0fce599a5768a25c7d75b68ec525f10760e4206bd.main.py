"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is the alternative name for Verbena?
2. In which county is Verbena located?
3. In which state is Verbena located?
4. What type of community is Verbena?
5. Where in Chilton County is Verbena situated?
6. After what was Verbena named?
7. Why did Verbena develop into a popular resort location?
8. Which city's affluent citizens used Verbena as a resort location?
9. What is the capital of Alabama?
10. During which period did yellow fever outbreaks occur that influenced Verbena's development?
11. What type of buildings line the streets of Verbena?
12. Which transportation company currently owns the railroad beside which Verbena was built?
13. What facilities did Verbena have during its heyday?
14. Which religious building still stands in Verbena?
15. On which road is the Verbena United Methodist Church located?
16. What was the population of Verbena according to the U.S. Census in 1890?
17. What was Verbena's population ranking within Chilton County in 1890?
18. Which census year recorded Verbena's population as 756?
19. Have any of the historic homes in Verbena undergone renovation or restoration?
20. What happened to many of the original buildings in Verbena?
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
    # ── CLASSES ──────────────────────────────────────────────────────────────
    class Place(Thing): pass
    class Country(Place): pass
    class State(Place): pass
    class County(Place): pass
    class Community(Place): pass
    class UnincorporatedCommunity(Community): pass
    class City(Place): pass
    class Road(Place): pass

    class Building(Thing): pass
    class Hotel(Building): pass
    class Bank(Building): pass
    class PostOffice(Building): pass
    class GeneralStore(Building): pass
    class ReligiousBuilding(Building): pass
    class Church(ReligiousBuilding): pass
    class StatelyHome(Building): pass

    class Flower(Thing): pass
    class DiseaseOutbreak(Thing): pass
    class Railroad(Thing): pass
    class TransportationCompany(Thing): pass
    class Census(Thing): pass
    class TimePeriod(Thing): pass

    # ── PROPERTIES ───────────────────────────────────────────────────────────
    class hasAlternativeName(DataProperty, FunctionalProperty):
        domain = [Community]
        range  = [str]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    class locatedInDirection(DataProperty, FunctionalProperty):
        domain = [Place]
        range  = [str]

    class isCapitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range  = [State]

    class namedAfter(ObjectProperty):
        domain = [Place]
        range  = [Flower]

    class attractedCitizensFrom(ObjectProperty):
        domain = [Community]
        range  = [City]

    class influencedDevelopmentBy(ObjectProperty):
        domain = [Community]
        range  = [DiseaseOutbreak]

    class occurredDuring(ObjectProperty, FunctionalProperty):
        domain = [DiseaseOutbreak]
        range  = [TimePeriod]

    class builtBeside(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range  = [Railroad]

    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [Railroad]
        range  = [TransportationCompany]

    class hasFacility(ObjectProperty):
        domain = [Community]
        range  = [Building]

    class locatedOnRoad(ObjectProperty, FunctionalProperty):
        domain = [Building]
        range  = [Road]

    class censusYear(DataProperty, FunctionalProperty):
        domain = [Census]
        range  = [int]

    class recordedPopulation(DataProperty, FunctionalProperty):
        domain = [Census]
        range  = [int]

    class surveyedCommunity(ObjectProperty, FunctionalProperty):
        domain = [Census]
        range  = [Community]

    class populationRanking(DataProperty, FunctionalProperty):
        domain = [Census]
        range  = [int]

    class hasUndergoneRenovation(DataProperty, FunctionalProperty):
        domain = [Building]
        range  = [bool]

    # ── INDIVIDUALS ──────────────────────────────────────────────────────────

    # Geographic places
    ChiltonCounty = County("ChiltonCounty")
    ChiltonCounty.label = "Chilton County"

    AlabamaState = State("AlabamaState")
    AlabamaState.label = "Alabama"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    MontgomeryCity = City("MontgomeryCity")
    MontgomeryCity.label = "Montgomery"

    CountyRoad59 = Road("CountyRoad59")
    CountyRoad59.label = "County Road 59"

    # The community itself
    VerbenaComm = UnincorporatedCommunity("VerbenaComm")
    VerbenaComm.label = "Verbena"
    VerbenaComm.hasAlternativeName = "Summerfield"
    VerbenaComm.locatedInDirection = "southeastern"
    VerbenaComm.locatedIn = [ChiltonCounty]

    # Geographic hierarchy
    ChiltonCounty.locatedIn = [AlabamaState]
    AlabamaState.locatedIn  = [UnitedStates]
    MontgomeryCity.locatedIn  = [AlabamaState]
    MontgomeryCity.isCapitalOf = AlabamaState

    # Flower after which the community was named
    VerbenaFlowerInst = Flower("VerbenaFlowerInst")
    VerbenaFlowerInst.label = "Verbena"
    VerbenaComm.namedAfter = [VerbenaFlowerInst]

    # Disease outbreaks and the time period they occurred in
    YellowFeverOutbreaks = DiseaseOutbreak("YellowFeverOutbreaks")
    YellowFeverOutbreaks.label = "yellow fever outbreaks"

    LateNineteenthEarlyTwentieth = TimePeriod("LateNineteenthEarlyTwentieth")
    LateNineteenthEarlyTwentieth.label = "late 19th and early 20th centuries"

    YellowFeverOutbreaks.occurredDuring = LateNineteenthEarlyTwentieth
    VerbenaComm.influencedDevelopmentBy = [YellowFeverOutbreaks]
    VerbenaComm.attractedCitizensFrom   = [MontgomeryCity]

    # Railroad and its owner
    CsxTransportation = TransportationCompany("CsxTransportation")
    CsxTransportation.label = "CSX Transportation"

    VerbenaRailroad = Railroad("VerbenaRailroad")
    VerbenaRailroad.ownedBy = CsxTransportation
    VerbenaComm.builtBeside = VerbenaRailroad

    # Named building
    VerbenaUnitedMethodistChurch = Church("VerbenaUnitedMethodistChurch")
    VerbenaUnitedMethodistChurch.label = "Verbena United Methodist Church"
    VerbenaUnitedMethodistChurch.locatedOnRoad = CountyRoad59

    # Unnamed facilities asserted to exist in the text
    VerbenaHotel1        = Hotel("VerbenaHotel1")
    VerbenaHotel2        = Hotel("VerbenaHotel2")
    VerbenaBank          = Bank("VerbenaBank")
    VerbenaPostOffice    = PostOffice("VerbenaPostOffice")
    VerbenaGeneralStore  = GeneralStore("VerbenaGeneralStore")

    # Stately homes (text asserts renovation/restoration on some)
    VerbenaStatelyHome = StatelyHome("VerbenaStatelyHome")
    VerbenaStatelyHome.hasUndergoneRenovation = True

    VerbenaComm.hasFacility = [
        VerbenaUnitedMethodistChurch,
        VerbenaHotel1, VerbenaHotel2,
        VerbenaBank,
        VerbenaPostOffice,
        VerbenaGeneralStore,
        VerbenaStatelyHome,
    ]

    # 1890 U.S. Census data
    USCensus1890 = Census("USCensus1890")
    USCensus1890.label            = "U.S. Census in 1890"
    USCensus1890.censusYear       = 1890
    USCensus1890.recordedPopulation = 756
    USCensus1890.surveyedCommunity  = VerbenaComm
    USCensus1890.populationRanking  = 1


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
