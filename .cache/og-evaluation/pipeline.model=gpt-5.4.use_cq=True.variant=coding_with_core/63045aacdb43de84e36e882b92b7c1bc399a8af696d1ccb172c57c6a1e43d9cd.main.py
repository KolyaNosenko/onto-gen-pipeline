"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

What is Verbena also known as?
What type of community is Verbena?
Where is Verbena located?
In which county is Verbena situated?
In which state is Verbena located?
In which region of the county is Verbena located?
What country is Verbena part of?
What is the origin of the name Verbena?
Why did Verbena become a popular resort location?
For whom did Verbena become a popular resort location?
During which disease outbreaks did Verbena gain popularity as a resort?
In which historical period did the yellow fever outbreaks occur?
What historic features of Verbena reflect its past as a resort town?
Which homes in Verbena have undergone renovation and restoration?
Along what infrastructure was the town of Verbena built?
Which company currently owns the railroad beside Verbena?
What establishments existed in Verbena during its heyday?
How many hotels did Verbena have in its heyday?
Did Verbena have a bank in its heyday?
Did Verbena have a post office in its heyday?
Did Verbena have a general store in its heyday?
What happened to many of Verbena’s historic buildings?
Which historic building still stands in Verbena?
Where is the Verbena United Methodist Church located?
Near what part of town does the Verbena United Methodist Church stand?
What was the population of Verbena according to the 1890 U.S. Census?
How did Verbena’s population rank within Chilton County in 1890?
Which community was the largest in Chilton County in 1890?
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
    Society,
    NonAgentiveSocialObject,
    NonAgentivePhysicalObject,
    Accomplishment,
    TimeInterval,
)

# No core properties are subclassed in this model.


with core:
    class GeographicCommunity(Society):
        pass


    class ResortCommunity(GeographicCommunity):
        pass


    class UnincorporatedCommunity(GeographicCommunity):
        pass


    class Town(GeographicCommunity):
        pass


    class City(GeographicCommunity):
        pass


    class AdministrativeRegion(Society):
        pass


    class County(AdministrativeRegion):
        pass


    class State(AdministrativeRegion):
        pass


    class Country(AdministrativeRegion):
        pass


    class Organization(Society):
        pass


    class TransportationCompany(Organization):
        pass


    class Citizenry(Society):
        pass


    class PlaceName(NonAgentiveSocialObject):
        pass


    class Census(NonAgentiveSocialObject):
        pass


    class HistoricalPeriod(TimeInterval):
        pass


    class Infrastructure(NonAgentivePhysicalObject):
        pass


    class Railroad(Infrastructure):
        pass


    class Road(Infrastructure):
        pass


    class Plant(NonAgentivePhysicalObject):
        pass


    class Flower(Plant):
        pass


    class Building(NonAgentivePhysicalObject):
        pass


    class HistoricBuilding(Building):
        pass


    class Residence(HistoricBuilding):
        pass


    class StatelyHome(Residence):
        pass


    class CommercialBuilding(HistoricBuilding):
        pass


    class Hotel(CommercialBuilding):
        pass


    class Bank(CommercialBuilding):
        pass


    class PostOffice(CommercialBuilding):
        pass


    class GeneralStore(CommercialBuilding):
        pass


    class ReligiousBuilding(HistoricBuilding):
        pass


    class Church(ReligiousBuilding):
        pass


    class MethodistChurch(Church):
        pass


    class DiseaseOutbreak(Accomplishment):
        pass


    class YellowFeverOutbreak(DiseaseOutbreak):
        pass


    class Renovation(Accomplishment):
        pass


    class Restoration(Accomplishment):
        pass


    class hasAlternativeName(ObjectProperty):
        domain = [GeographicCommunity]
        range = [PlaceName]


    class locatedIn(ObjectProperty):
        domain = [Or([GeographicCommunity, NonAgentivePhysicalObject])]
        range = [Or([GeographicCommunity, AdministrativeRegion])]


    class stateCapitalOf(ObjectProperty):
        domain = [City]
        range = [State]


    class resortForResidentsOf(ObjectProperty):
        domain = [ResortCommunity]
        range = [City]


    class besideInfrastructureOwnedBy(ObjectProperty):
        domain = [GeographicCommunity]
        range = [TransportationCompany]


    class standsOn(ObjectProperty):
        domain = [Building]
        range = [Road]


    class populationReportedBy(ObjectProperty):
        domain = [GeographicCommunity]
        range = [Census]


    class populationAtTime(ObjectProperty):
        domain = [GeographicCommunity]
        range = [HistoricalPeriod]


    class largestCommunityIn(ObjectProperty):
        domain = [GeographicCommunity]
        range = [County]


    class countyRegionDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class nameOriginDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class popularityReasonDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class popularityPeriodDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class historicFeatureDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class renovatedOrRestoredHomesDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class builtBesideInfrastructureDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class heydayEstablishmentsDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class heydayHotelCount(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [int]


    class hadBankInHeyday(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [bool]


    class hadPostOfficeInHeyday(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [bool]


    class hadGeneralStoreInHeyday(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [bool]


    class currentHistoricBuildingsConditionDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    class nearTownPartDescription(DataProperty, FunctionalProperty):
        domain = [NonAgentivePhysicalObject]
        range = [str]


    class populationCount(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [int]


    class countyPopulationRankDescription(DataProperty, FunctionalProperty):
        domain = [GeographicCommunity]
        range = [str]


    Verbena = UnincorporatedCommunity("VerbenaCommunity")
    Verbena.label = "Verbena"
    Verbena.is_a.append(Town)
    Verbena.is_a.append(ResortCommunity)
    Verbena.countyRegionDescription = "southeastern"
    Verbena.nameOriginDescription = "the indigenous flower"
    Verbena.popularityReasonDescription = "yellow fever outbreaks"
    Verbena.popularityPeriodDescription = "the late 19th and early 20th centuries"
    Verbena.historicFeatureDescription = "many stately homes line the streets of the town"
    Verbena.renovatedOrRestoredHomesDescription = (
        "some of the stately homes have undergone recent renovation and restoration"
    )
    Verbena.builtBesideInfrastructureDescription = "the railroad"
    Verbena.heydayEstablishmentsDescription = (
        "two hotels, a bank, a post office, and a general store"
    )
    Verbena.heydayHotelCount = 2
    Verbena.hadBankInHeyday = True
    Verbena.hadPostOfficeInHeyday = True
    Verbena.hadGeneralStoreInHeyday = True
    Verbena.currentHistoricBuildingsConditionDescription = (
        "many of those buildings are gone or boarded up today"
    )
    Verbena.populationCount = 756
    Verbena.countyPopulationRankDescription = "largest community in Chilton County"

    Summerfield = PlaceName("SummerfieldName")
    Summerfield.label = "Summerfield"

    ChiltonCounty = County("ChiltonCounty")
    ChiltonCounty.label = "Chilton County"

    Alabama = State("AlabamaState")
    Alabama.label = "Alabama"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    Montgomery = City("MontgomeryCity")
    Montgomery.label = "Montgomery"

    CSXTransportation = TransportationCompany("CSXTransportationCompany")
    CSXTransportation.label = "CSX Transportation"

    VerbenaUnitedMethodistChurch = MethodistChurch("VerbenaUnitedMethodistChurchBuilding")
    VerbenaUnitedMethodistChurch.label = "Verbena United Methodist Church"
    VerbenaUnitedMethodistChurch.nearTownPartDescription = "the town's center"

    CountyRoad59 = Road("CountyRoad59")
    CountyRoad59.label = "County Road 59"

    USCensus = Census("USCensus")
    USCensus.label = "U.S. Census"

    Year1890 = HistoricalPeriod("Year1890")
    Year1890.label = "1890"

    Verbena.hasAlternativeName.append(Summerfield)
    Verbena.locatedIn.append(ChiltonCounty)
    Verbena.locatedIn.append(Alabama)
    Verbena.locatedIn.append(UnitedStates)
    Verbena.resortForResidentsOf.append(Montgomery)
    Verbena.besideInfrastructureOwnedBy.append(CSXTransportation)
    Verbena.populationReportedBy.append(USCensus)
    Verbena.populationAtTime.append(Year1890)
    Verbena.largestCommunityIn.append(ChiltonCounty)

    ChiltonCounty.locatedIn.append(Alabama)
    Alabama.locatedIn.append(UnitedStates)
    Montgomery.locatedIn.append(Alabama)
    Montgomery.stateCapitalOf.append(Alabama)

    VerbenaUnitedMethodistChurch.locatedIn.append(Verbena)
    VerbenaUnitedMethodistChurch.standsOn.append(CountyRoad59)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
