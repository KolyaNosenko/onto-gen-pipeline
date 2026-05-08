"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

1. What is the location of Milton within New South Wales?

2. When was Milton founded?

3. Who was Milton named after?

4. What was the occupation of George Knight?

5. What is the current population of Milton?

6. Which region is Milton located in?

7. What administrative area does Milton belong to?

8. What are the main commercial centres of the Milton-Ulladulla district?

9. Which highway runs through Milton's town centre?

10. What factors have contributed to Milton's recent resurgence?

11. What types of businesses have recently opened in Milton?

12. What new developments are occurring on the fringes of Milton?

13. Why has Milton become a popular stopping place for travellers?

14. What role did Milton play during the 19th Century?

15. What is driving the influx of residents to the Milton district?
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
    # Entity classes
    class Country(Thing): pass
    class State(Thing): pass
    class Region(Thing): pass
    class AdministrativeArea(Thing): pass
    class District(Thing): pass
    class Town(Thing): pass
    class CommercialCentre(Town): pass
    class Highway(Thing): pass
    class Person(Thing): pass
    class Occupation(Thing): pass
    class Property(Thing): pass
    class HousingEstate(Thing): pass
    class BusinessType(Thing): pass
    class BoutiqueStore(BusinessType): pass
    class Cafe(BusinessType): pass
    class BedAndBreakfast(BusinessType): pass
    class TimePeriod(Thing): pass

    # Object properties
    class locatedIn(ObjectProperty):
        domain = [Town]
        range = [Region, State, Country, AdministrativeArea, District]

    class locatedWithin(ObjectProperty):
        domain = [State]
        range = [Country]

    class mainCommercialCentreOf(ObjectProperty):
        domain = [CommercialCentre]
        range = [District]

    class runsThrough(ObjectProperty):
        domain = [Highway]
        range = [Town]

    class owns(ObjectProperty):
        domain = [Person]
        range = [Property]

    class hasOccupation(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Occupation]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range = [Person, Property]

    class importantCentreDuring(ObjectProperty):
        domain = [Town]
        range = [TimePeriod]

    class operatesIn(ObjectProperty):
        domain = [BusinessType]
        range = [Town]

    class developingNear(ObjectProperty):
        domain = [HousingEstate]
        range = [Town]

    # Data properties
    class foundedInYear(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [int]

    class population(DataProperty, FunctionalProperty):
        domain = [Town]
        range = [int]

    # Create individuals - geographic locations
    australia = Country("Australia")
    australia.label = "Australia"

    new_south_wales = State("NewSouthWales")
    new_south_wales.label = "New South Wales"
    new_south_wales.locatedWithin = [australia]

    south_coast = Region("SouthCoast")
    south_coast.label = "South Coast"

    city_of_shoalhaven = AdministrativeArea("CityOfShoalhaven")
    city_of_shoalhaven.label = "City of Shoalhaven"

    milton_ulladulla = District("MiltonUlladulla")
    milton_ulladulla.label = "Milton - Ulladulla district"

    # Milton town
    milton = CommercialCentre("Milton")
    milton.label = "Milton"
    milton.foundedInYear = 1860
    milton.population = 1663
    milton.locatedIn = [south_coast, new_south_wales, city_of_shoalhaven, milton_ulladulla]
    milton.mainCommercialCentreOf = [milton_ulladulla]

    # Infrastructure
    princes_highway = Highway("PrincesHighway")
    princes_highway.label = "Princes Highway"
    princes_highway.runsThrough = [milton]

    # People and occupations
    george_knight = Person("GeorgeKnight")
    george_knight.label = "George Knight"

    postmaster = Occupation("Postmaster")
    postmaster.label = "postmaster"
    george_knight.hasOccupation = postmaster

    # Property of George Knight (unnamed in text)
    knight_property = Property()
    george_knight.owns = [knight_property]
    milton.namedAfter = knight_property

    # Time period
    nineteenth_century = TimePeriod("NineteenthCentury")
    nineteenth_century.label = "19th Century"
    milton.importantCentreDuring = [nineteenth_century]

    # Business types operating in Milton
    boutique_stores = BoutiqueStore("BoutiqueStores")
    boutique_stores.label = "boutique stores"
    boutique_stores.operatesIn = [milton]

    cafes = Cafe("Cafes")
    cafes.label = "cafes"
    cafes.operatesIn = [milton]

    bed_and_breakfasts = BedAndBreakfast("BedAndBreakfasts")
    bed_and_breakfasts.label = "bed and breakfast type businesses"
    bed_and_breakfasts.operatesIn = [milton]

    # Housing estates developing near Milton
    housing_estates = HousingEstate("NewHousingEstates")
    housing_estates.label = "new housing estates"
    housing_estates.developingNear = [milton]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
