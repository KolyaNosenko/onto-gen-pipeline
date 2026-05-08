"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

What is Milton?
In which region is Milton located?
In which state is Milton located?
In which country is Milton located?
Within which local government area or city is Milton situated?
When was Milton founded?
After whom or what was Milton named?
Who was George Knight?
What role did George Knight have in relation to Milton?
What was Milton’s significance during the 19th century?
Is Milton an important regional centre?
What are the main commercial centres of the Milton-Ulladulla district?
Is Milton one of the two main commercial centres of the Milton-Ulladulla district?
What is the population of Milton?
Through which town does the Princes Highway run?
What is the relationship between Milton and the Princes Highway?
Why is Milton a popular stopping place for travellers?
What factors have contributed to Milton’s recent resurgence?
How has the local tourism industry influenced Milton?
Why have new residents been moving to the Milton district?
What types of new developments are occurring on the fringes of Milton?
What kinds of new businesses have opened in Milton?
Are new housing estates being developed in Milton?
Are boutique stores located in Milton?
Are cafes located in Milton?
Are bed and breakfast businesses located in Milton?
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

    class Region(Place):
        pass

    class LocalGovernmentArea(Place):
        pass

    class District(Place):
        pass

    class PopulatedPlace(Place):
        pass

    class Town(PopulatedPlace):
        pass

    class Village(PopulatedPlace):
        pass

    class RegionalCentre(PopulatedPlace):
        pass

    class ImportantRegionalCentre(RegionalCentre):
        pass

    class CommercialCentre(PopulatedPlace):
        pass

    class MainCommercialCentre(CommercialCentre):
        pass

    class TransportationRoute(Thing):
        pass

    class Highway(TransportationRoute):
        pass

    class Person(Thing):
        pass

    class PostMaster(Person):
        pass

    class PropertyAsset(Thing):
        pass

    class TimeReference(Thing):
        pass

    class Year(TimeReference):
        pass

    class Century(TimeReference):
        pass

    class Quantity(Thing):
        pass

    class PopulationQuantity(Quantity):
        pass

    class Industry(Thing):
        pass

    class TourismIndustry(Industry):
        pass

    class Traveller(Person):
        pass

    class Resident(Person):
        pass

    class Development(Thing):
        pass

    class HousingEstate(Development):
        pass

    class Business(Thing):
        pass

    class BoutiqueStore(Business):
        pass

    class Cafe(Business):
        pass

    class BedAndBreakfastBusiness(Business):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class withinLocalGovernmentArea(ObjectProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [LocalGovernmentArea]

    class foundedIn(ObjectProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [Year]

    class namedAfterPropertyOf(ObjectProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [Person]

    class becameImportantRegionalCentreDuring(ObjectProperty):
        domain = [RegionalCentre]
        range = [Century]

    class hasMainCommercialCentre(ObjectProperty):
        domain = [District]
        range = [MainCommercialCentre]

    class hasPopulation(ObjectProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [PopulationQuantity]

    class runsThrough(ObjectProperty):
        domain = [TransportationRoute]
        range = [PopulatedPlace]

    class isPopularStoppingPlaceOn(ObjectProperty):
        domain = [PopulatedPlace]
        range = [TransportationRoute]

    class numericValue(DataProperty, FunctionalProperty):
        domain = [Year, PopulationQuantity]
        range = [int]

    class mainCommercialCentreCount(DataProperty, FunctionalProperty):
        domain = [District]
        range = [int]

    class hasRecentResurgence(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    class recentResurgenceDriver(DataProperty):
        domain = [PopulatedPlace]
        range = [str]

    class residentInfluxMotivation(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [str]

    class isPopularStoppingPlaceForTravellers(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    class stoppingPlaceReason(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [str]

    class newDevelopmentType(DataProperty):
        domain = [PopulatedPlace]
        range = [str]

    class newBusinessType(DataProperty):
        domain = [PopulatedPlace]
        range = [str]

    class hasHousingEstateDevelopmentOnFringes(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    class hasBoutiqueStores(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    class hasCafes(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    class hasBedAndBreakfastBusinesses(DataProperty, FunctionalProperty):
        domain = [PopulatedPlace]
        range = [bool]

    Milton = Town("Milton")
    Milton.label = "Milton"
    Milton.is_a.append(Village)
    Milton.is_a.append(ImportantRegionalCentre)
    Milton.is_a.append(MainCommercialCentre)

    SouthCoastRegion = Region("SouthCoastRegion")
    SouthCoastRegion.label = "South Coast region"

    NewSouthWales = State("NewSouthWales")
    NewSouthWales.label = "New South Wales"

    Australia = Country("Australia")
    Australia.label = "Australia"

    CityOfShoalhaven = LocalGovernmentArea("CityOfShoalhaven")
    CityOfShoalhaven.label = "City of Shoalhaven"

    GeorgeKnight = PostMaster("GeorgeKnight")
    GeorgeKnight.label = "George Knight"

    Year1860 = Year("Year1860")
    Year1860.label = "1860"
    Year1860.numericValue = 1860

    NineteenthCentury = Century("NineteenthCentury")
    NineteenthCentury.label = "19th Century"

    MiltonUlladullaDistrict = District("MiltonUlladullaDistrict")
    MiltonUlladullaDistrict.label = "Milton - Ulladulla district"

    PrincesHighway = Highway("PrincesHighway")
    PrincesHighway.label = "Princes Highway"

    Population1663 = PopulationQuantity("Population1663")
    Population1663.label = "1,663"
    Population1663.numericValue = 1663

    Milton.locatedIn = [SouthCoastRegion, NewSouthWales, Australia]
    Milton.withinLocalGovernmentArea = CityOfShoalhaven
    Milton.foundedIn = Year1860
    Milton.namedAfterPropertyOf = GeorgeKnight
    Milton.becameImportantRegionalCentreDuring = [NineteenthCentury]
    Milton.hasPopulation = Population1663
    Milton.isPopularStoppingPlaceOn = [PrincesHighway]
    Milton.hasRecentResurgence = True
    Milton.recentResurgenceDriver = [
        "local tourism industry",
        "an influx of residents to the district seeking a seachange",
    ]
    Milton.residentInfluxMotivation = "seeking a seachange"
    Milton.isPopularStoppingPlaceForTravellers = True
    Milton.stoppingPlaceReason = "the Princes Highway runs through the centre of town"
    Milton.newDevelopmentType = ["new housing estates"]
    Milton.newBusinessType = [
        "boutique stores",
        "cafes",
        "bed and breakfast type businesses",
    ]
    Milton.hasHousingEstateDevelopmentOnFringes = True
    Milton.hasBoutiqueStores = True
    Milton.hasCafes = True
    Milton.hasBedAndBreakfastBusinesses = True

    SouthCoastRegion.locatedIn = [NewSouthWales, Australia]
    NewSouthWales.locatedIn = [Australia]
    PrincesHighway.runsThrough = [Milton]
    MiltonUlladullaDistrict.hasMainCommercialCentre = [Milton]
    MiltonUlladullaDistrict.mainCommercialCentreCount = 2


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
