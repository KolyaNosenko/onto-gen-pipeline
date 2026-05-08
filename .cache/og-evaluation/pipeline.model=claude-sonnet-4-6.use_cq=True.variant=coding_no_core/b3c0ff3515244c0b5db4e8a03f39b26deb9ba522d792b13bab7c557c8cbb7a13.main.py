"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

1. What region is Milton located in?
2. In which state of Australia is Milton situated?
3. What local government area does Milton belong to?
4. When was Milton founded?
5. After whom or what was Milton named?
6. Who was George Knight and what was his role in Milton's history?
7. What was Milton's significance during the 19th Century?
8. What is the current population of Milton?
9. What are the two main commercial centres of the Milton-Ulladulla district?
10. Which highway runs through the centre of Milton?
11. Why is Milton a popular stopping place for travellers?
12. What industry has influenced Milton's resurgence in recent years?
13. What types of new businesses have been established in Milton?
14. What type of residential developments are being built on the fringes of Milton?
15. What phenomenon has led to an influx of new residents to the Milton district?
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
    # ── Entity classes ──────────────────────────────────────────────────────
    class Place(Thing): pass
    class Settlement(Place): pass
    class Town(Settlement): pass
    class Region(Place): pass
    class State(Place): pass
    class Country(Place): pass
    class LocalGovernmentArea(Place): pass
    class District(Place): pass
    class TransportRoute(Thing): pass
    class Highway(TransportRoute): pass
    class Industry(Thing): pass
    class Person(Thing): pass
    class LandProperty(Thing): pass
    class TimePeriod(Thing): pass
    class BusinessEstablishment(Thing): pass
    class BoutiqueStore(BusinessEstablishment): pass
    class Cafe(BusinessEstablishment): pass
    class BedAndBreakfast(BusinessEstablishment): pass
    class HousingEstate(Thing): pass
    class SocialPhenomenon(Thing): pass

    # ── Object properties ───────────────────────────────────────────────────
    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    class withinLocalGovernmentArea(ObjectProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [LocalGovernmentArea]

    class namedAfter(ObjectProperty, FunctionalProperty):
        domain = [Town]
        range  = [LandProperty]

    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [LandProperty]
        range  = [Person]

    class isCommercialCentreOf(ObjectProperty):
        domain = [Settlement]
        range  = [District]

    class traversedBy(ObjectProperty):
        domain = [Settlement]
        range  = [Highway]

    class influencedBy(ObjectProperty):
        domain = [Settlement]
        range  = [Industry]

    class becameSignificantDuring(ObjectProperty):
        domain = [Town]
        range  = [TimePeriod]

    class hasNewBusinessType(ObjectProperty):
        domain = [Settlement]
        range  = [BusinessEstablishment]

    class hasHousingDevelopment(ObjectProperty):
        domain = [Settlement]
        range  = [HousingEstate]

    class experiencedPhenomenon(ObjectProperty):
        domain = [District]
        range  = [SocialPhenomenon]

    # ── Data properties ─────────────────────────────────────────────────────
    class foundedIn(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [int]

    class hasPopulation(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [int]

    class hasOccupation(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class historicalRole(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [str]

    # ── Named individuals ───────────────────────────────────────────────────
    milton_inst = Town("Milton_town")
    milton_inst.label = "Milton"

    south_coast = Region("South_Coast_region")
    south_coast.label = "South Coast"

    new_south_wales = State("New_South_Wales_state")
    new_south_wales.label = "New South Wales"

    australia = Country("Australia_country")
    australia.label = "Australia"

    city_of_shoalhaven = LocalGovernmentArea("City_of_Shoalhaven_lga")
    city_of_shoalhaven.label = "City of Shoalhaven"

    milton_ulladulla_district = District("Milton_Ulladulla_district")
    milton_ulladulla_district.label = "Milton-Ulladulla district"

    george_knight = Person("George_Knight_person")
    george_knight.label = "George Knight"
    george_knight.hasOccupation = "post master"

    george_knight_property = LandProperty("George_Knight_property")
    george_knight_property.label = "George Knight's property"

    ulladulla = Town("Ulladulla_town")
    ulladulla.label = "Ulladulla"

    princes_highway = Highway("Princes_Highway")
    princes_highway.label = "Princes Highway"

    tourism_industry = Industry("Tourism_industry")
    tourism_industry.label = "tourism industry"

    century_19th = TimePeriod("19th_Century")
    century_19th.label = "19th Century"

    boutique_stores = BoutiqueStore("Boutique_Stores")
    boutique_stores.label = "boutique stores"

    cafes_inst = Cafe("Cafes")
    cafes_inst.label = "cafes"

    bed_and_breakfast = BedAndBreakfast("Bed_and_Breakfast")
    bed_and_breakfast.label = "bed and breakfast"

    housing_estates = HousingEstate("Housing_Estates")
    housing_estates.label = "housing estates"

    seachange = SocialPhenomenon("Seachange")
    seachange.label = "seachange"

    # ── Facts ────────────────────────────────────────────────────────────────
    milton_inst.locatedIn = [south_coast]
    south_coast.locatedIn = [new_south_wales]
    new_south_wales.locatedIn = [australia]
    milton_inst.withinLocalGovernmentArea = city_of_shoalhaven
    milton_inst.foundedIn = 1860
    milton_inst.namedAfter = george_knight_property
    george_knight_property.ownedBy = george_knight
    milton_inst.hasPopulation = 1663
    milton_inst.isCommercialCentreOf = [milton_ulladulla_district]
    ulladulla.isCommercialCentreOf = [milton_ulladulla_district]
    milton_inst.traversedBy = [princes_highway]
    milton_inst.influencedBy = [tourism_industry]
    milton_inst.historicalRole = "important regional centre"
    milton_inst.becameSignificantDuring = [century_19th]
    milton_inst.hasNewBusinessType = [boutique_stores, cafes_inst, bed_and_breakfast]
    milton_inst.hasHousingDevelopment = [housing_estates]
    milton_ulladulla_district.experiencedPhenomenon = [seachange]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
