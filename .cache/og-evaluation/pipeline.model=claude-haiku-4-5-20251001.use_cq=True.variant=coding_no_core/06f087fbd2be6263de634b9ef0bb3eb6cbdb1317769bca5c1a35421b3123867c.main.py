"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

1. What is the tallest building in Los Angeles?
2. What is the height of Wilshire Grand Center compared to U.S. Bank Tower?
3. Where is Wilshire Grand Center located?
4. What is the ranking of Wilshire Grand Center among the tallest buildings in the United States?
5. What are the components of the Wilshire Grand Center complex?
6. What is the estimated development cost of Wilshire Grand Center?
7. How many hotel rooms does the InterContinental hotel at Wilshire Grand Center have?
8. What is the total amount of Class A office space in Wilshire Grand Center?
9. What is the tallest building in California?
10. What is the tallest building west of the Mississippi River outside of New York City, Chicago, and Philadelphia?
11. What mixed-use facilities are included in Wilshire Grand Center?
12. Which hotel operator manages the hotel component of Wilshire Grand Center?
13. Does Wilshire Grand Center include retail and shopping facilities?
14. What is the purpose of the Wilshire Grand Center development in Downtown Los Angeles?
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
    # Entity Classes
    class Building(Thing):
        pass
    
    class Skyscraper(Building):
        pass
    
    class Location(Thing):
        pass
    
    class City(Location):
        pass
    
    class State(Location):
        pass
    
    class District(Location):
        pass
    
    class Region(Location):
        pass
    
    class GeographicFeature(Location):
        pass
    
    class MixedUseComplex(Thing):
        pass
    
    class Component(Thing):
        pass
    
    class Hotel(Component):
        pass
    
    class RetailFacility(Component):
        pass
    
    class ObservationDeck(Component):
        pass
    
    class ShoppingMall(Component):
        pass
    
    class OfficeSpace(Component):
        pass
    
    # Object Properties
    class locatedIn(ObjectProperty):
        domain = [Building]
        range = [Location]
    
    class locatedInRegion(ObjectProperty, TransitiveProperty):
        domain = [Location]
        range = [Location]
    
    class isPartOf(ObjectProperty):
        domain = [Building]
        range = [MixedUseComplex]
    
    class includes(ObjectProperty):
        domain = [MixedUseComplex]
        range = [Component]
    
    class tallerThan(ObjectProperty):
        domain = [Building]
        range = [Building]
    
    class isTallestBuildingIn(ObjectProperty):
        domain = [Building]
        range = [Location]
    
    # Data Properties
    class rankingAmongTallestBuildings(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [int]
    
    class numberOfHotelRooms(DataProperty, FunctionalProperty):
        domain = [Hotel]
        range = [int]
    
    class developmentCost(DataProperty, FunctionalProperty):
        domain = [MixedUseComplex]
        range = [str]
    
    # Named Individuals - Locations
    LosAngeles = City("LosAngeles")
    LosAngeles.label = "Los Angeles"
    
    California = State("California")
    California.label = "California"
    
    UnitedStates = State("UnitedStates")
    UnitedStates.label = "United States"
    
    MississippiRiver = GeographicFeature("MississippiRiver")
    MississippiRiver.label = "Mississippi River"
    
    NewYorkCity = City("NewYorkCity")
    NewYorkCity.label = "New York City"
    
    Chicago = City("Chicago")
    Chicago.label = "Chicago"
    
    Philadelphia = City("Philadelphia")
    Philadelphia.label = "Philadelphia"
    
    DowntownLosAngeles = District("DowntownLosAngeles")
    DowntownLosAngeles.label = "Downtown Los Angeles"
    
    FinancialDistrict = District("FinancialDistrict")
    FinancialDistrict.label = "Financial District"
    
    WestOfMississippiExcludingNYCChicagoPhilly = Region("WestOfMississippiExcludingNYCChicagoPhilly")
    WestOfMississippiExcludingNYCChicagoPhilly.label = "West of Mississippi River excluding New York City, Chicago, and Philadelphia"
    
    # Named Individuals - Buildings
    WilshireGrandCenter = Skyscraper("WilshireGrandCenter")
    WilshireGrandCenter.label = "Wilshire Grand Center"
    
    USBankTower = Building("USBankTower")
    USBankTower.label = "U.S. Bank Tower"
    
    # Named Individuals - Complex
    WilshireGrandComplex = MixedUseComplex("WilshireGrandComplex")
    WilshireGrandComplex.label = "Wilshire Grand Complex"
    
    # Named Individuals - Hotel
    InterContinentalHotel = Hotel("InterContinentalHotel")
    InterContinentalHotel.label = "InterContinental"
    
    # Establish location hierarchy
    FinancialDistrict.locatedInRegion = [DowntownLosAngeles]
    DowntownLosAngeles.locatedInRegion = [LosAngeles]
    LosAngeles.locatedInRegion = [California]
    California.locatedInRegion = [UnitedStates]
    
    # Establish building locations and relationships
    WilshireGrandCenter.locatedIn = [FinancialDistrict]
    WilshireGrandCenter.isPartOf = [WilshireGrandComplex]
    
    # Building comparisons
    WilshireGrandCenter.tallerThan = [USBankTower]
    WilshireGrandCenter.isTallestBuildingIn = [LosAngeles, California, WestOfMississippiExcludingNYCChicagoPhilly]
    WilshireGrandCenter.rankingAmongTallestBuildings = 11
    
    # Complex relationships
    WilshireGrandComplex.includes = [InterContinentalHotel]
    WilshireGrandComplex.developmentCost = "$1.2 billion"
    
    # Hotel details
    InterContinentalHotel.numberOfHotelRooms = 900


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
