"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

Competency questions — natural-language queries the ontology should
support; your output must contain enough classes, properties, and
individuals to answer every one of them:
1. What type of place is Milton?
2. In which region of New South Wales is Milton located?
3. Which local government area includes Milton?
4. In what year was Milton founded?
5. After whom or what was Milton named?
6. During which century did Milton become an important regional centre?
7. Is Milton one of the main commercial centres of the Milton-Ulladulla district?
8. What is the population of Milton?
9. Which major highway runs through the centre of Milton?
10. Why is Milton a popular stopping place for travellers?
11. What recent changes has Milton undergone?
12. What factors have influenced Milton’s recent resurgence?
13. Are new housing estates being developed on the fringes of Milton?
14. What kinds of new businesses have located in Milton?
15. Does Milton attract residents seeking a seachange?
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

    class Town(Place):
        pass

    class RegionalCentre(Place):
        pass

    class CommercialCentre(Place):
        pass

    class Region(Place):
        pass

    class State(Place):
        pass

    class Country(Place):
        pass

    class LocalGovernmentArea(Place):
        pass

    class District(Place):
        pass

    class Property(Place):
        pass

    class Person(Thing):
        pass

    class PostMaster(Person):
        pass

    class Traveller(Person):
        pass

    class Resident(Person):
        pass

    class Highway(Thing):
        pass

    class Business(Thing):
        pass

    class BoutiqueStore(Business):
        pass

    class Cafe(Business):
        pass

    class BedAndBreakfastBusiness(Business):
        pass

    class HousingEstate(Thing):
        pass

    class Industry(Thing):
        pass

    class Phenomenon(Thing):
        pass

    class Resurgence(Phenomenon):
        pass

    class Influx(Phenomenon):
        pass

    class Seachange(Thing):
        pass

    class Year(Thing):
        pass

    class Century(Thing):
        pass

    class PopulationCount(Thing):
        pass

    class locatedInRegion(ObjectProperty):
        domain = [Town]
        range = [Region]

    class locatedInState(ObjectProperty):
        domain = [Region]
        range = [State]

    class locatedInCountry(ObjectProperty):
        domain = [State]
        range = [Country]

    class withinLocalGovernmentArea(ObjectProperty):
        domain = [Town]
        range = [LocalGovernmentArea]

    class inDistrict(ObjectProperty):
        domain = [Town]
        range = [District]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [Property]

    class propertyOf(ObjectProperty, FunctionalProperty):
        domain = [Property]
        range = [Person]

    class foundedIn(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [Year]

    class becameImportantRegionalCentreDuring(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [Century]

    class mainCommercialCentreOf(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [District]

    class population(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [PopulationCount]

    class runsThroughCentreOf(ObjectProperty, FunctionalProperty):
        domain = [Highway]
        range = [Town]

    class popularStoppingPlaceFor(ObjectProperty):
        domain = [Town]
        range = [Traveller]

    class travelsOn(ObjectProperty, FunctionalProperty):
        domain = [Traveller]
        range = [Highway]

    class hasRecentResurgence(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [Resurgence]

    class influencedBy(ObjectProperty):
        domain = [Phenomenon]
        range = [Thing]

    class seeks(ObjectProperty, FunctionalProperty):
        domain = [Influx]
        range = [Seachange]

    class developedOnFringesOf(ObjectProperty, FunctionalProperty):
        domain = [HousingEstate]
        range = [Town]

    class locatedInTown(ObjectProperty, FunctionalProperty):
        domain = [Business]
        range = [Town]

    class attracts(ObjectProperty):
        domain = [Town]
        range = [Influx]

    milton = Town("Milton")
    milton.label = "Milton"
    milton.is_a.append(CommercialCentre)
    milton.is_a.append(RegionalCentre)

    southCoastRegion = Region("SouthCoastRegion")
    southCoastRegion.label = "South Coast region"

    newSouthWales = State("NewSouthWales")
    newSouthWales.label = "New South Wales"

    australia = Country("Australia")
    australia.label = "Australia"

    cityOfShoalhaven = LocalGovernmentArea("CityOfShoalhaven")
    cityOfShoalhaven.label = "City of Shoalhaven"

    miltonUlladullaDistrict = District("MiltonUlladullaDistrict")
    miltonUlladullaDistrict.label = "Milton - Ulladulla district"

    georgeKnight = PostMaster("GeorgeKnight")
    georgeKnight.label = "George Knight"

    princesHighway = Highway("PrincesHighway")
    princesHighway.label = "Princes Highway"

    year1860 = Year("Year1860")
    year1860.label = "1860"

    nineteenthCentury = Century("NineteenthCentury")
    nineteenthCentury.label = "19th Century"

    population1663 = PopulationCount("Population1663")
    population1663.label = "1,663"

    miltonNamedAfterProperty = Property("MiltonNamedAfterProperty")
    miltonNamedAfterProperty.label = "the property of post master George Knight"

    miltonResurgence = Resurgence("MiltonResurgence")
    miltonResurgence.label = "a resurgence"

    localTourismIndustry = Industry("LocalTourismIndustry")
    localTourismIndustry.label = "the local tourism industry"

    residentsInflux = Influx("ResidentsInflux")
    residentsInflux.label = "an influx of residents to the district seeking a seachange"

    aSeachange = Seachange("ASeachange")
    aSeachange.label = "a seachange"

    travellers = Traveller("Travellers")
    travellers.label = "travellers"

    newHousingEstates = HousingEstate("NewHousingEstates")
    newHousingEstates.label = "new housing estates"

    newBoutiqueStores = BoutiqueStore("NewBoutiqueStores")
    newBoutiqueStores.label = "new boutique stores"

    cafes = Cafe("Cafes")
    cafes.label = "cafes"

    bedAndBreakfastBusinesses = BedAndBreakfastBusiness("BedAndBreakfastBusinesses")
    bedAndBreakfastBusinesses.label = "bed and breakfast type businesses"

    milton.locatedInRegion = [southCoastRegion]
    southCoastRegion.locatedInState = [newSouthWales]
    newSouthWales.locatedInCountry = [australia]
    milton.withinLocalGovernmentArea = [cityOfShoalhaven]
    milton.inDistrict = [miltonUlladullaDistrict]
    milton.foundedIn = year1860
    milton.namedAfter = miltonNamedAfterProperty
    milton.becameImportantRegionalCentreDuring = nineteenthCentury
    milton.mainCommercialCentreOf = miltonUlladullaDistrict
    milton.population = population1663
    milton.hasRecentResurgence = miltonResurgence
    milton.popularStoppingPlaceFor = [travellers]
    milton.attracts = [residentsInflux]

    miltonNamedAfterProperty.propertyOf = georgeKnight
    miltonResurgence.influencedBy = [localTourismIndustry, residentsInflux]
    residentsInflux.seeks = aSeachange
    travellers.travelsOn = princesHighway
    princesHighway.runsThroughCentreOf = milton
    newHousingEstates.developedOnFringesOf = milton
    newBoutiqueStores.locatedInTown = milton
    cafes.locatedInTown = milton
    bedAndBreakfastBusinesses.locatedInTown = milton


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
