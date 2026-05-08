"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

- What is Milton?
- In which region of New South Wales is Milton located?
- Which local government area is Milton within?
- When was Milton founded?
- After whom was Milton named?
- What role did Milton play during the 19th century?
- What is the current population of Milton?
- What are the main commercial centres of the Milton-Ulladulla district?
- Which highway runs through the centre of Milton?
- Why is Milton a popular stopping place for travellers?
- What factors have contributed to Milton’s recent resurgence?
- What new types of businesses have recently located in Milton?
- What new housing developments are being built around Milton?
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
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Process,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class GeographicEntity(NonAgentiveSocialObject):
        pass

    class Settlement(GeographicEntity):
        pass

    class Town(Settlement):
        pass

    class City(GeographicEntity):
        pass

    class District(GeographicEntity):
        pass

    class GeographicRegion(GeographicEntity):
        pass

    class State(GeographicRegion):
        pass

    class Country(GeographicRegion):
        pass

    class RegionalCentre(GeographicEntity):
        pass

    class ImportantRegionalCentre(RegionalCentre):
        pass

    class CommercialCentre(GeographicEntity):
        pass

    class MainCommercialCentre(CommercialCentre):
        pass

    class Person(AgentivePhysicalObject):
        pass

    class PostMaster(Person):
        pass

    class Traveller(Person):
        pass

    class Industry(NonAgentiveSocialObject):
        pass

    class TourismIndustry(Industry):
        pass

    class Business(NonAgentiveSocialObject):
        pass

    class Store(Business):
        pass

    class BoutiqueStore(Store):
        pass

    class Cafe(Business):
        pass

    class BedAndBreakfastBusiness(Business):
        pass

    class HousingEstate(NonAgentivePhysicalObject):
        pass

    class Highway(NonAgentivePhysicalObject):
        pass

    class Resurgence(Process):
        pass

    class ResidentInflux(Process):
        pass

    class foundedInYear(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [int]

    class currentPopulation(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [int]

    class namedAfter(ObjectProperty):
        domain = [Town]
        range = [Person]

    class becameImportantRegionalCentreDuring(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [TimeInterval]

    class mainCommercialCentreOf(ObjectProperty):
        domain = [Town]
        range = [District]

    class runsThrough(ObjectProperty):
        domain = [Highway]
        range = [Town]

    class popularStoppingPlaceFor(ObjectProperty):
        domain = [Town]
        range = [Traveller]

    class influencedBy(ObjectProperty):
        domain = [Town]
        range = [NonAgentiveSocialObject, Process]

    class hasBusiness(ObjectProperty):
        domain = [Town]
        range = [Business]

    class hasHousingEstate(ObjectProperty):
        domain = [Town]
        range = [HousingEstate]

    Milton = Town("MiltonTown")
    Milton.label = "Milton"
    SouthCoastRegion = GeographicRegion("SouthCoastRegion")
    SouthCoastRegion.label = "South Coast region"
    NewSouthWales = State("NewSouthWales")
    NewSouthWales.label = "New South Wales"
    Australia = Country("AustraliaCountry")
    Australia.label = "Australia"
    CityOfShoalhaven = City("CityOfShoalhaven")
    CityOfShoalhaven.label = "City of Shoalhaven"
    MiltonUlladullaDistrict = District("MiltonUlladullaDistrict")
    MiltonUlladullaDistrict.label = "Milton - Ulladulla district"
    GeorgeKnight = PostMaster("GeorgeKnight")
    GeorgeKnight.label = "George Knight"
    PrincesHighway = Highway("PrincesHighway")
    PrincesHighway.label = "Princes Highway"
    NineteenthCentury = TimeInterval("NineteenthCentury")
    NineteenthCentury.label = "19th Century"

    Milton.partOf.append(SouthCoastRegion)
    SouthCoastRegion.partOf.append(NewSouthWales)
    NewSouthWales.partOf.append(Australia)
    Milton.partOf.append(CityOfShoalhaven)
    Milton.partOf.append(MiltonUlladullaDistrict)
    Milton.namedAfter.append(GeorgeKnight)
    Milton.becameImportantRegionalCentreDuring = NineteenthCentury
    Milton.foundedInYear = 1860
    Milton.currentPopulation = 1663
    Milton.is_a.append(ImportantRegionalCentre)
    Milton.is_a.append(MainCommercialCentre)
    Milton.is_a.append(popularStoppingPlaceFor.some(Traveller))
    Milton.is_a.append(influencedBy.some(TourismIndustry))
    Milton.is_a.append(influencedBy.some(ResidentInflux))
    Milton.is_a.append(hasBusiness.some(BoutiqueStore))
    Milton.is_a.append(hasBusiness.some(Cafe))
    Milton.is_a.append(hasBusiness.some(BedAndBreakfastBusiness))
    Milton.is_a.append(hasHousingEstate.some(HousingEstate))
    PrincesHighway.runsThrough.append(Milton)
    Milton.mainCommercialCentreOf.append(MiltonUlladullaDistrict)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
