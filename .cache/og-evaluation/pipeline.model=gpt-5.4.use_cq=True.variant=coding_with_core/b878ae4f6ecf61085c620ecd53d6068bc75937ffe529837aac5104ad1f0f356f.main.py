"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

What is Milton?
In which region is Milton located?
In which state is Milton located?
In which country is Milton located?
Within which local government area is Milton situated?
When was Milton founded?
After whom or what was Milton named?
Who was George Knight?
What role did George Knight have in relation to Milton’s naming?
What was Milton’s significance during the 19th century?
Is Milton an important regional centre?
What is Milton’s current role in the Milton-Ulladulla district?
How many main commercial centres are there in the Milton-Ulladulla district?
What is the population of Milton?
Is Milton a popular stopping place for travellers?
Which highway runs through Milton?
Where does the Princes Highway pass in relation to the town?
What factors have influenced Milton’s recent resurgence?
How has the local tourism industry affected Milton?
Has Milton experienced an influx of new residents?
Why have residents moved to the Milton district?
What types of new developments are occurring on the fringes of Milton?
What kinds of new businesses have opened in Milton?
Are boutique stores present in Milton?
Are cafes present in Milton?
Are bed and breakfast businesses located in Milton?
How has Milton changed in recent years?
What administrative and geographic entities contain Milton?
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
    AgentivePhysicalObject,
    Event,
    NonAgentivePhysicalObject,
    Process,
    SocialObject,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class GeographicEntity(NonAgentivePhysicalObject):
        pass


    class AdministrativeArea(GeographicEntity):
        pass


    class Settlement(GeographicEntity):
        pass


    class Town(Settlement):
        pass


    class Region(GeographicEntity):
        pass


    class State(AdministrativeArea):
        pass


    class Country(AdministrativeArea):
        pass


    class LocalGovernmentArea(AdministrativeArea):
        pass


    class District(GeographicEntity):
        pass


    class TransportRoute(NonAgentivePhysicalObject):
        pass


    class Highway(TransportRoute):
        pass


    class Person(AgentivePhysicalObject):
        pass


    class PostMaster(Person):
        pass


    class Traveller(Person):
        pass


    class Resident(Person):
        pass


    class PropertyEstate(NonAgentivePhysicalObject):
        pass


    class CommercialCentre(Town):
        pass


    class MainCommercialCentre(CommercialCentre):
        pass


    class RegionalCentre(Town):
        pass


    class ImportantRegionalCentre(RegionalCentre):
        pass


    class PopularStoppingPlace(Town):
        pass


    class IndustrySector(SocialObject):
        pass


    class TourismIndustry(IndustrySector):
        pass


    class HousingEstate(NonAgentivePhysicalObject):
        pass


    class BoutiqueStore(NonAgentivePhysicalObject):
        pass


    class Cafe(NonAgentivePhysicalObject):
        pass


    class BedAndBreakfastBusiness(NonAgentivePhysicalObject):
        pass


    class Founding(Event):
        pass


    class Resurgence(Process):
        pass


    class PopulationInflux(Process):
        pass


    class HousingDevelopment(Process):
        pass


    class locatedIn(partOf):
        domain = [GeographicEntity]
        range = [GeographicEntity]


    class foundedIn(ObjectProperty):
        domain = [Town]
        range = [TimeInterval]


    class namedAfterPropertyOf(ObjectProperty):
        domain = [Town]
        range = [Person]


    class commercialCentreOf(ObjectProperty):
        domain = [CommercialCentre]
        range = [District]


    class importantRegionalCentreDuring(ObjectProperty):
        domain = [RegionalCentre]
        range = [TimeInterval]


    class stoppingPlaceOn(ObjectProperty):
        domain = [PopularStoppingPlace]
        range = [Highway]


    class runsThroughTownCentreOf(ObjectProperty):
        domain = [Highway]
        range = [Town]


    class populationCount(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [int]


    class mainCommercialCentreCount(DataProperty, FunctionalProperty):
        domain = [District]
        range = [int]


    class namingSourceDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class significanceDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class currentRoleDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class popularStoppingPlaceForTravellers(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class highwayPassageDescription(DataProperty, FunctionalProperty):
        domain = [Highway]
        range = [str]


    class recentResurgenceInfluenceDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class influencedByLocalTourismIndustry(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class experiencedResidentInflux(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class residentInfluxReasonDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class newDevelopmentDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class newBusinessDescription(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [str]


    class hasNewHousingEstates(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class hasBoutiqueStores(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class hasCafes(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    class hasBedAndBreakfastBusinesses(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [bool]


    Town.is_a.append(locatedIn.some(GeographicEntity))
    CommercialCentre.is_a.append(commercialCentreOf.some(District))
    ImportantRegionalCentre.is_a.append(importantRegionalCentreDuring.some(TimeInterval))
    PopularStoppingPlace.is_a.append(stoppingPlaceOn.some(Highway))

    Milton = Town("Milton")
    Milton.label = "Milton"
    Milton.is_a.append(MainCommercialCentre)
    Milton.is_a.append(ImportantRegionalCentre)
    Milton.is_a.append(PopularStoppingPlace)

    SouthCoastRegion = Region("SouthCoastRegion")
    SouthCoastRegion.label = "South Coast region"

    NewSouthWales = State("NewSouthWales")
    NewSouthWales.label = "New South Wales"

    Australia = Country("Australia")
    Australia.label = "Australia"

    CityOfShoalhaven = LocalGovernmentArea("CityOfShoalhaven")
    CityOfShoalhaven.label = "City of Shoalhaven"

    MiltonUlladullaDistrict = District("MiltonUlladullaDistrict")
    MiltonUlladullaDistrict.label = "Milton - Ulladulla district"

    GeorgeKnight = PostMaster("GeorgeKnight")
    GeorgeKnight.label = "George Knight"

    PrincesHighway = Highway("PrincesHighway")
    PrincesHighway.label = "Princes Highway"

    Year1860 = TimeInterval("Year1860")
    Year1860.label = "1860"

    NineteenthCentury = TimeInterval("NineteenthCentury")
    NineteenthCentury.label = "19th Century"

    SouthCoastRegion.locatedIn.append(NewSouthWales)
    NewSouthWales.locatedIn.append(Australia)

    Milton.locatedIn.append(SouthCoastRegion)
    Milton.locatedIn.append(NewSouthWales)
    Milton.locatedIn.append(Australia)
    Milton.locatedIn.append(CityOfShoalhaven)
    Milton.locatedIn.append(MiltonUlladullaDistrict)
    Milton.foundedIn.append(Year1860)
    Milton.namedAfterPropertyOf.append(GeorgeKnight)
    Milton.commercialCentreOf.append(MiltonUlladullaDistrict)
    Milton.importantRegionalCentreDuring.append(NineteenthCentury)
    Milton.populationCount = 1663
    Milton.namingSourceDescription = "the property of post master George Knight"
    Milton.significanceDescription = "an important regional centre during the 19th Century"
    Milton.currentRoleDescription = "one of the two main commercial centres of the Milton - Ulladulla district"
    Milton.popularStoppingPlaceForTravellers = True
    Milton.stoppingPlaceOn.append(PrincesHighway)
    Milton.recentResurgenceInfluenceDescription = (
        "the local tourism industry and an influx of residents to the district seeking a seachange"
    )
    Milton.influencedByLocalTourismIndustry = True
    Milton.experiencedResidentInflux = True
    Milton.residentInfluxReasonDescription = "seeking a seachange"
    Milton.newDevelopmentDescription = (
        "Several new housing estates are being developed on the fringes of the village"
    )
    Milton.newBusinessDescription = (
        "new boutique stores, cafes and bed and breakfast type businesses have located in the town"
    )
    Milton.hasNewHousingEstates = True
    Milton.hasBoutiqueStores = True
    Milton.hasCafes = True
    Milton.hasBedAndBreakfastBusinesses = True

    MiltonUlladullaDistrict.mainCommercialCentreCount = 2

    PrincesHighway.runsThroughTownCentreOf.append(Milton)
    PrincesHighway.highwayPassageDescription = "runs through the centre of town"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
