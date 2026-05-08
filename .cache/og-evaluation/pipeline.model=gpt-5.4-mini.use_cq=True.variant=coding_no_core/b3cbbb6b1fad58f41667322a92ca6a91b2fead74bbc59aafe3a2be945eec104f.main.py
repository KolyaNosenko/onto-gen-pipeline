"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

1. What is the Wilshire Grand Center, and where is it located?
2. Is the Wilshire Grand Center a skyscraper?
3. What is the tallest building in Los Angeles?
4. What is the tallest building in California?
5. What is the tallest building west of the Mississippi River?
6. What is the tallest building outside of New York City, Chicago, and Philadelphia?
7. What is the 11th tallest building in the United States?
8. How does the height of the Wilshire Grand Center compare to the U.S. Bank Tower?
9. What type of complex is the Wilshire Grand Center part of?
10. What components are included in the Wilshire Grand Center complex?
11. What is the estimated cost of developing the Wilshire Grand Center complex?
12. How much retail space is planned for the complex?
13. How much Class A office space is planned for the complex?
14. How many hotel rooms are included in the plans for the complex?
15. What is the hotel component of the Wilshire Grand Center tower?
16. How many rooms and suites does the InterContinental tower component comprise?
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

    class GeographicFeature(Place):
        pass

    class District(Place):
        pass

    class City(Place):
        pass

    class State(Place):
        pass

    class Country(Place):
        pass

    class River(GeographicFeature):
        pass

    class Building(Thing):
        pass

    class Tower(Building):
        pass

    class Skyscraper(Tower):
        pass

    class Complex(Thing):
        pass

    class MixedUseComplex(Complex):
        pass

    class Hotel(Thing):
        pass

    class HotelComponent(Hotel):
        pass

    class RetailSpace(Thing):
        pass

    class ObservationDeck(Thing):
        pass

    class ShoppingMall(Complex):
        pass

    class OfficeComplex(Complex):
        pass

    class OfficeSpace(Thing):
        pass

    class Room(Thing):
        pass

    class HotelRoom(Room):
        pass

    class Suite(Room):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Place]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class hasComponent(ObjectProperty):
        domain = [Complex]
        range = [Thing]

    class comprises(ObjectProperty):
        domain = [HotelComponent]
        range = [Room]

    class tallerThan(ObjectProperty):
        domain = [Building]
        range = [Building]

    class westOf(ObjectProperty):
        domain = [Thing]
        range = [River]

    class outsideOf(ObjectProperty):
        domain = [Thing]
        range = [City]

    class tallestIn(ObjectProperty):
        domain = [Building]
        range = [Place]

    class hotelComponent(ObjectProperty, FunctionalProperty):
        domain = [Tower]
        range = [HotelComponent]

    class estimatedCost(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [float]

    class plannedRetailSpace(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class plannedOfficeSpace(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class plannedHotelRooms(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [int]

    class roomAndSuiteCount(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [int]

    class buildingRankInUnitedStates(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [int]

    MixedUseComplex.is_a.extend([
        hasComponent.some(HotelComponent),
        hasComponent.some(RetailSpace),
        hasComponent.some(ObservationDeck),
        hasComponent.some(ShoppingMall),
        hasComponent.some(OfficeComplex),
        hasComponent.some(OfficeSpace),
        hasComponent.some(HotelRoom),
    ])

    wilshireGrandCenter = Skyscraper("WilshireGrandCenter")
    wilshireGrandCenter.label = "Wilshire Grand Center"

    financialDistrict = District("FinancialDistrict")
    financialDistrict.label = "Financial District"

    downtownLosAngeles = District("DowntownLosAngeles")
    downtownLosAngeles.label = "Downtown Los Angeles"

    losAngeles = City("LosAngeles")
    losAngeles.label = "Los Angeles"

    california = State("California")
    california.label = "California"

    mississippiRiver = River("MississippiRiver")
    mississippiRiver.label = "Mississippi River"

    newYorkCity = City("NewYorkCity")
    newYorkCity.label = "New York City"

    chicago = City("Chicago")
    chicago.label = "Chicago"

    philadelphia = City("Philadelphia")
    philadelphia.label = "Philadelphia"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    usBankTower = Skyscraper("USBankTower")
    usBankTower.label = "U.S. Bank Tower"

    intercontinental = HotelComponent("InterContinental")
    intercontinental.label = "InterContinental"

    wilshireGrandCenter.locatedIn = [financialDistrict]
    financialDistrict.locatedIn = [downtownLosAngeles]
    downtownLosAngeles.locatedIn = [losAngeles]
    losAngeles.locatedIn = [california]

    wilshireGrandCenter.tallestIn = [losAngeles, california, unitedStates]
    wilshireGrandCenter.westOf = [mississippiRiver]
    wilshireGrandCenter.outsideOf = [newYorkCity, chicago, philadelphia]
    wilshireGrandCenter.tallerThan = [usBankTower]
    wilshireGrandCenter.estimatedCost = 1200000000.0
    wilshireGrandCenter.plannedRetailSpace = "retail"
    wilshireGrandCenter.plannedOfficeSpace = "Class A office space"
    wilshireGrandCenter.plannedHotelRooms = 900
    wilshireGrandCenter.buildingRankInUnitedStates = 11
    wilshireGrandCenter.hotelComponent = intercontinental
    wilshireGrandCenter.is_a.append(partOf.some(MixedUseComplex))

    intercontinental.partOf = [wilshireGrandCenter]
    intercontinental.roomAndSuiteCount = 900
    intercontinental.is_a.append(comprises.some(HotelRoom))
    intercontinental.is_a.append(comprises.some(Suite))


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
