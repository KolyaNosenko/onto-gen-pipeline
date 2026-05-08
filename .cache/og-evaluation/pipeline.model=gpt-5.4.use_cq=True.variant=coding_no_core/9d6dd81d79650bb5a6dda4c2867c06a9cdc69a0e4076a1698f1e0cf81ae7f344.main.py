"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

What is Wilshire Grand Center?
Where is Wilshire Grand Center located?
In which district of Downtown Los Angeles is Wilshire Grand Center situated?
In which city is Wilshire Grand Center located?
In which state is Wilshire Grand Center located?
Is Wilshire Grand Center a skyscraper?
What is the height ranking of Wilshire Grand Center in Los Angeles?
Is Wilshire Grand Center the tallest building in Los Angeles?
Is Wilshire Grand Center the tallest building in California?
Is Wilshire Grand Center the tallest building west of the Mississippi River?
Is Wilshire Grand Center the tallest building outside of New York City, Chicago, and Philadelphia?
What is the ranking of Wilshire Grand Center among the tallest buildings in the United States?
Which building’s height does Wilshire Grand Center surpass?
By how much does Wilshire Grand Center surpass the U.S. Bank Tower in height?
What type of complex is Wilshire Grand Center part of?
What are the functional components of the Wilshire Grand Center complex?
Does the Wilshire Grand Center complex include a hotel?
Does the Wilshire Grand Center complex include retail space?
Does the Wilshire Grand Center complex include observation decks?
Does the Wilshire Grand Center complex include a shopping mall?
Does the Wilshire Grand Center complex include office space?
What is the estimated development cost of the Wilshire Grand Center complex?
What is the expected impact of the Wilshire Grand Center complex on downtown Los Angeles?
What surrounding area is expected to be revitalized by the Wilshire Grand Center development?
How much retail space is included in the plans for Wilshire Grand Center?
How much Class A office space is included in the plans for Wilshire Grand Center?
How many hotel rooms are included in the plans for Wilshire Grand Center?
What is the hotel component of Wilshire Grand Center called?
How many rooms and suites does the InterContinental component comprise?
Is InterContinental the hotel component of Wilshire Grand Center?
What kinds of uses are combined in the Wilshire Grand Center mixed-use development?
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

    class City(Place):
        pass

    class District(Place):
        pass

    class River(Place):
        pass

    class BuiltEntity(Thing):
        pass

    class Building(BuiltEntity):
        pass

    class Skyscraper(Building):
        pass

    class Tower(Building):
        pass

    class Complex(BuiltEntity):
        pass

    class MixedUseComplex(Complex):
        pass

    class FunctionalComponent(Thing):
        pass

    class HotelComponent(FunctionalComponent):
        pass

    class RetailSpace(FunctionalComponent):
        pass

    class ObservationDeck(FunctionalComponent):
        pass

    class ShoppingMall(FunctionalComponent):
        pass

    class OfficeSpace(FunctionalComponent):
        pass

    class ClassAOfficeSpace(OfficeSpace):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Place]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class hasComponent(ObjectProperty):
        domain = [Complex]
        range = [FunctionalComponent]

    class hasHotelComponent(ObjectProperty, FunctionalProperty):
        domain = [Building, Complex]
        range = [HotelComponent]

    class tallestIn(ObjectProperty):
        domain = [Building]
        range = [Place]

    class tallestWestOf(ObjectProperty):
        domain = [Building]
        range = [River]

    class tallestOutsideOf(ObjectProperty):
        domain = [Building]
        range = [City]

    class surpassesHeightOf(ObjectProperty):
        domain = [Building]
        range = [Building]

    class expectedToRevitalize(ObjectProperty):
        domain = [Complex]
        range = [Place]

    class hasHeightRankInUnitedStates(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [int]

    class hasEstimatedDevelopmentCost(DataProperty, FunctionalProperty):
        domain = [Complex]
        range = [str]

    class hasPlannedHotelRoomCount(DataProperty, FunctionalProperty):
        domain = [Complex]
        range = [int]

    class hasRoomAndSuiteCount(DataProperty, FunctionalProperty):
        domain = [HotelComponent]
        range = [int]

    class hasExpectedImpactDescription(DataProperty, FunctionalProperty):
        domain = [Complex]
        range = [str]

    class hasSurroundingAreaDescription(DataProperty, FunctionalProperty):
        domain = [Complex]
        range = [str]

    MixedUseComplex.is_a.append(hasComponent.some(HotelComponent))
    MixedUseComplex.is_a.append(hasComponent.some(RetailSpace))
    MixedUseComplex.is_a.append(hasComponent.some(ObservationDeck))
    MixedUseComplex.is_a.append(hasComponent.some(ShoppingMall))
    MixedUseComplex.is_a.append(hasComponent.some(OfficeSpace))

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    California = State("California")
    California.label = "California"
    California.locatedIn = [UnitedStates]

    LosAngeles = City("LosAngeles")
    LosAngeles.label = "Los Angeles"
    LosAngeles.locatedIn = [California]

    DowntownLosAngeles = District("DowntownLosAngeles")
    DowntownLosAngeles.label = "Downtown Los Angeles"
    DowntownLosAngeles.locatedIn = [LosAngeles, California]

    FinancialDistrict = District("FinancialDistrict")
    FinancialDistrict.label = "Financial District"
    FinancialDistrict.locatedIn = [DowntownLosAngeles, LosAngeles, California]

    MississippiRiver = River("MississippiRiver")
    MississippiRiver.label = "Mississippi River"

    NewYorkCity = City("NewYorkCity")
    NewYorkCity.label = "New York City"

    Chicago = City("Chicago")
    Chicago.label = "Chicago"

    Philadelphia = City("Philadelphia")
    Philadelphia.label = "Philadelphia"

    WilshireGrandCenter = Skyscraper("WilshireGrandCenter")
    WilshireGrandCenter.label = "Wilshire Grand Center"
    WilshireGrandCenter.locatedIn = [
        FinancialDistrict,
        DowntownLosAngeles,
        LosAngeles,
        California,
        UnitedStates,
    ]
    WilshireGrandCenter.tallestIn = [LosAngeles, California]
    WilshireGrandCenter.tallestWestOf = [MississippiRiver]
    WilshireGrandCenter.tallestOutsideOf = [NewYorkCity, Chicago, Philadelphia]
    WilshireGrandCenter.hasHeightRankInUnitedStates = 11

    USBankTower = Tower("USBankTower")
    USBankTower.label = "U.S. Bank Tower"
    WilshireGrandCenter.surpassesHeightOf = [USBankTower]

    WilshireGrandCenterComplex = MixedUseComplex("WilshireGrandCenterComplex")
    WilshireGrandCenterComplex.label = "Wilshire Grand Center complex"
    WilshireGrandCenterComplex.locatedIn = [
        FinancialDistrict,
        DowntownLosAngeles,
        LosAngeles,
        California,
        UnitedStates,
    ]
    WilshireGrandCenterComplex.hasComponent = []
    WilshireGrandCenterComplex.hasEstimatedDevelopmentCost = "$ 1.2 billion"
    WilshireGrandCenterComplex.hasPlannedHotelRoomCount = 900
    WilshireGrandCenterComplex.expectedToRevitalize = [DowntownLosAngeles]
    WilshireGrandCenterComplex.hasExpectedImpactDescription = (
        "revitalize downtown Los Angeles and the area surrounding the building"
    )
    WilshireGrandCenterComplex.hasSurroundingAreaDescription = "the area surrounding the building"

    WilshireGrandCenter.partOf = [WilshireGrandCenterComplex]

    InterContinental = HotelComponent("InterContinental")
    InterContinental.label = "InterContinental"
    InterContinental.partOf = [WilshireGrandCenter, WilshireGrandCenterComplex]
    InterContinental.hasRoomAndSuiteCount = 900

    WilshireGrandCenter.hasHotelComponent = InterContinental
    WilshireGrandCenterComplex.hasHotelComponent = InterContinental
    WilshireGrandCenterComplex.hasComponent.append(InterContinental)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
