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
What is the tallest building in Los Angeles?
What is the tallest building in California?
What is the tallest building west of the Mississippi River?
What is the tallest building outside of New York City, Chicago, and Philadelphia?
What is the ranking of Wilshire Grand Center among the tallest buildings in the United States?
Which building does Wilshire Grand Center surpass in height?
By how much does Wilshire Grand Center surpass the U.S. Bank Tower in height?
What type of complex is Wilshire Grand Center part of?
What are the functional components of the Wilshire Grand Center complex?
Does the Wilshire Grand Center complex include hotel facilities?
Does the Wilshire Grand Center complex include retail space?
Does the Wilshire Grand Center complex include observation decks?
Does the Wilshire Grand Center complex include a shopping mall?
Does the Wilshire Grand Center complex include office space?
What is the estimated development cost of the Wilshire Grand Center complex?
How much retail space is included in the plans for Wilshire Grand Center?
How much Class A office space is included in the plans for Wilshire Grand Center?
How many hotel rooms are included in the plans for Wilshire Grand Center?
What is the hotel component of Wilshire Grand Center?
Which hotel brand is associated with the tower component of Wilshire Grand Center?
How many rooms and suites does the InterContinental hotel in Wilshire Grand Center comprise?
What is the expected impact of the Wilshire Grand Center complex on downtown Los Angeles?
What area is expected to be revitalized by the Wilshire Grand Center development?
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

from og_sandbox_with_core.core.entities import NonAgentivePhysicalObject, SpaceRegion
from og_sandbox_with_core.core.properties import partOf


with core:
    class Building(NonAgentivePhysicalObject):
        pass

    class Skyscraper(Building):
        pass

    class MixedUseComplex(NonAgentivePhysicalObject):
        pass

    class MixedUseSkyscraperComplex(Skyscraper, MixedUseComplex):
        pass

    class HotelComponent(NonAgentivePhysicalObject):
        pass

    class RetailSpace(NonAgentivePhysicalObject):
        pass

    class ObservationDeck(NonAgentivePhysicalObject):
        pass

    class ShoppingMall(NonAgentivePhysicalObject):
        pass

    class OfficeSpace(NonAgentivePhysicalObject):
        pass

    class ClassAOfficeSpace(OfficeSpace):
        pass

    class District(SpaceRegion):
        pass

    class DowntownArea(SpaceRegion):
        pass

    class City(SpaceRegion):
        pass

    class State(SpaceRegion):
        pass

    class Country(SpaceRegion):
        pass

    class River(NonAgentivePhysicalObject):
        pass

    class geographicPartOf(partOf):
        domain = [SpaceRegion]
        range = [SpaceRegion]

    class locatedIn(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [SpaceRegion]

    class hasComponent(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [NonAgentivePhysicalObject]

    class tallestBuildingIn(ObjectProperty):
        domain = [Building]
        range = [SpaceRegion]

    class tallestBuildingWestOf(ObjectProperty):
        domain = [Building]
        range = [River]

    class tallestBuildingOutsideOf(ObjectProperty):
        domain = [Building]
        range = [City]

    class surpassesInHeight(ObjectProperty):
        domain = [Building]
        range = [Building]

    class expectedToRevitalize(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [SpaceRegion]

    class tallestBuildingRankInUnitedStates(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [int]

    class estimatedDevelopmentCost(DataProperty, FunctionalProperty):
        domain = [NonAgentivePhysicalObject]
        range = [str]

    class plannedHotelRoomCount(DataProperty, FunctionalProperty):
        domain = [NonAgentivePhysicalObject]
        range = [int]

    class roomAndSuiteCount(DataProperty, FunctionalProperty):
        domain = [HotelComponent]
        range = [int]

    class expectedRevitalizationAreaDescription(DataProperty, FunctionalProperty):
        domain = [NonAgentivePhysicalObject]
        range = [str]

    MixedUseComplex.is_a.append(hasComponent.some(HotelComponent))
    MixedUseComplex.is_a.append(hasComponent.some(RetailSpace))
    MixedUseComplex.is_a.append(hasComponent.some(ObservationDeck))
    MixedUseComplex.is_a.append(hasComponent.some(ShoppingMall))
    MixedUseComplex.is_a.append(hasComponent.some(ClassAOfficeSpace))

    WilshireGrandCenter = MixedUseSkyscraperComplex("WilshireGrandCenter")
    WilshireGrandCenter.label = "Wilshire Grand Center"

    FinancialDistrict = District("FinancialDistrict")
    FinancialDistrict.label = "Financial District"

    DowntownLosAngeles = DowntownArea("DowntownLosAngeles")
    DowntownLosAngeles.label = "Downtown Los Angeles"

    LosAngeles = City("LosAngeles")
    LosAngeles.label = "Los Angeles"

    California = State("California")
    California.label = "California"

    MississippiRiver = River("MississippiRiver")
    MississippiRiver.label = "Mississippi River"

    NewYorkCity = City("NewYorkCity")
    NewYorkCity.label = "New York City"

    Chicago = City("Chicago")
    Chicago.label = "Chicago"

    Philadelphia = City("Philadelphia")
    Philadelphia.label = "Philadelphia"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    USBankTower = Skyscraper("USBankTower")
    USBankTower.label = "U.S. Bank Tower"

    InterContinental = HotelComponent("InterContinental")
    InterContinental.label = "InterContinental"

    FinancialDistrict.geographicPartOf.append(DowntownLosAngeles)
    DowntownLosAngeles.geographicPartOf.append(LosAngeles)
    LosAngeles.geographicPartOf.append(California)
    California.geographicPartOf.append(UnitedStates)

    WilshireGrandCenter.locatedIn.append(FinancialDistrict)
    WilshireGrandCenter.locatedIn.append(DowntownLosAngeles)
    WilshireGrandCenter.locatedIn.append(LosAngeles)
    WilshireGrandCenter.locatedIn.append(California)

    WilshireGrandCenter.tallestBuildingIn.append(LosAngeles)
    WilshireGrandCenter.tallestBuildingIn.append(California)
    WilshireGrandCenter.tallestBuildingWestOf.append(MississippiRiver)
    WilshireGrandCenter.tallestBuildingOutsideOf.append(NewYorkCity)
    WilshireGrandCenter.tallestBuildingOutsideOf.append(Chicago)
    WilshireGrandCenter.tallestBuildingOutsideOf.append(Philadelphia)
    WilshireGrandCenter.tallestBuildingRankInUnitedStates = 11
    WilshireGrandCenter.surpassesInHeight.append(USBankTower)
    WilshireGrandCenter.hasComponent.append(InterContinental)
    WilshireGrandCenter.estimatedDevelopmentCost = "$1.2 billion"
    WilshireGrandCenter.plannedHotelRoomCount = 900
    WilshireGrandCenter.expectedToRevitalize.append(DowntownLosAngeles)
    WilshireGrandCenter.expectedRevitalizationAreaDescription = "the area surrounding the building"

    InterContinental.roomAndSuiteCount = 900


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
