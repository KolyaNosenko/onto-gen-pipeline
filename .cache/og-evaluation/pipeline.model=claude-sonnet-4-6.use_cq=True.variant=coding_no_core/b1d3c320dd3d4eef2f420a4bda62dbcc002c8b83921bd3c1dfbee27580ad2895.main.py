"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

1. What is the height of the Wilshire Grand Center?
2. Where is the Wilshire Grand Center located?
3. What is the tallest building in Los Angeles?
4. What is the tallest building in California?
5. What is the tallest building west of the Mississippi River?
6. What is the ranking of the Wilshire Grand Center among the tallest buildings in the United States?
7. Which building's height does the Wilshire Grand Center surpass?
8. What types of facilities are included in the Wilshire Grand Center complex?
9. What is the estimated cost of developing the Wilshire Grand Center complex?
10. How many hotel rooms does the Wilshire Grand Center have?
11. What hotel brand operates in the Wilshire Grand Center?
12. What type of office space is available in the Wilshire Grand Center?
13. In which district of Los Angeles is the Wilshire Grand Center situated?
14. Which cities have taller buildings than the Wilshire Grand Center?
15. What is the purpose of the Wilshire Grand Center development in relation to Downtown Los Angeles?
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
    # ── Entity Classes ─────────────────────────────────────────────
    class Place(Thing): pass
    class Country(Place): pass
    class State(Place): pass
    class City(Place): pass
    class District(Place): pass
    class River(Place): pass

    class Building(Thing): pass
    class Skyscraper(Building): pass

    class Facility(Thing): pass
    class Hotel(Facility): pass
    class RetailSpace(Facility): pass
    class ObservationDeck(Facility): pass
    class ShoppingMall(Facility): pass
    class OfficeSpace(Facility): pass
    class ClassAOfficeSpace(OfficeSpace): pass

    class Organisation(Thing): pass
    class HotelBrand(Organisation): pass

    # ── Object Properties ──────────────────────────────────────────
    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range  = [Place]

    class surpassesInHeight(ObjectProperty):
        domain = [Skyscraper]
        range  = [Building]

    class isTallestBuildingIn(ObjectProperty):
        domain = [Skyscraper]
        range  = [Place]

    class isTallestBuildingWestOf(ObjectProperty):
        domain = [Skyscraper]
        range  = [River]

    class cityWithTallerBuilding(ObjectProperty):
        domain = [Skyscraper]
        range  = [City]

    class includesFacility(ObjectProperty):
        domain = [Skyscraper]
        range  = [Facility]

    class hotelOperatedBy(ObjectProperty, FunctionalProperty):
        domain = [Hotel]
        range  = [HotelBrand]

    class expectedToRevitalize(ObjectProperty):
        domain = [Skyscraper]
        range  = [Place]

    # ── Data Properties ────────────────────────────────────────────
    class usHeightRanking(DataProperty, FunctionalProperty):
        domain = [Skyscraper]
        range  = [int]

    class estimatedDevelopmentCost(DataProperty, FunctionalProperty):
        domain = [Skyscraper]
        range  = [str]

    class numberOfHotelRooms(DataProperty, FunctionalProperty):
        domain = [Skyscraper]
        range  = [int]

    class officeSpaceClass(DataProperty, FunctionalProperty):
        domain = [OfficeSpace]
        range  = [str]

    # ── Named Individuals ──────────────────────────────────────────
    # Geographic places
    united_states = Country("UnitedStates")
    united_states.label = "United States"

    california = State("California")
    california.label = "California"

    los_angeles = City("LosAngeles")
    los_angeles.label = "Los Angeles"

    downtown_los_angeles = District("DowntownLosAngeles")
    downtown_los_angeles.label = "Downtown Los Angeles"

    financial_district = District("FinancialDistrict")
    financial_district.label = "Financial District"

    mississippi_river = River("MississippiRiver")
    mississippi_river.label = "Mississippi River"

    new_york_city = City("NewYorkCity")
    new_york_city.label = "New York City"

    chicago = City("Chicago")
    chicago.label = "Chicago"

    philadelphia = City("Philadelphia")
    philadelphia.label = "Philadelphia"

    # Buildings
    wilshire_grand_center = Skyscraper("WilshireGrandCenter")
    wilshire_grand_center.label = "Wilshire Grand Center"

    us_bank_tower = Skyscraper("USBankTower")
    us_bank_tower.label = "U.S. Bank Tower"

    # Hotel brand
    intercontinental = HotelBrand("InterContinental")
    intercontinental.label = "InterContinental"

    # Facility components of the Wilshire Grand Center complex
    wgc_hotel = Hotel("WGCHotel")
    wgc_retail = RetailSpace("WGCRetail")
    wgc_observation_deck = ObservationDeck("WGCObservationDeck")
    wgc_shopping_mall = ShoppingMall("WGCShoppingMall")
    wgc_office = ClassAOfficeSpace("WGCOfficeSpace")
    wgc_office.officeSpaceClass = "Class A"

    # Geographic containment (transitive locatedIn chain)
    financial_district.locatedIn = [downtown_los_angeles]
    downtown_los_angeles.locatedIn = [los_angeles]
    los_angeles.locatedIn = [california]
    california.locatedIn = [united_states]

    # Wilshire Grand Center facts
    wilshire_grand_center.locatedIn = [financial_district]
    wilshire_grand_center.surpassesInHeight = [us_bank_tower]
    wilshire_grand_center.isTallestBuildingIn = [los_angeles, california]
    wilshire_grand_center.isTallestBuildingWestOf = [mississippi_river]
    wilshire_grand_center.cityWithTallerBuilding = [new_york_city, chicago, philadelphia]
    wilshire_grand_center.includesFacility = [wgc_hotel, wgc_retail, wgc_observation_deck, wgc_shopping_mall, wgc_office]
    wilshire_grand_center.expectedToRevitalize = [downtown_los_angeles]
    wilshire_grand_center.usHeightRanking = 11
    wilshire_grand_center.estimatedDevelopmentCost = "$1.2 billion"
    wilshire_grand_center.numberOfHotelRooms = 900

    # Hotel operated by InterContinental
    wgc_hotel.hotelOperatedBy = intercontinental


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
