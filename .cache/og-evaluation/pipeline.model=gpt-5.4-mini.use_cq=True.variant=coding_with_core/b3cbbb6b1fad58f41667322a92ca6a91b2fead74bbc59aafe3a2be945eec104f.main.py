"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

1. What is the Wilshire Grand Center?
2. Where is the Wilshire Grand Center located?
3. In which district and city is the Wilshire Grand Center situated?
4. In which state is the Wilshire Grand Center located?
5. What is the tallest building in Los Angeles?
6. What is the tallest building in California?
7. What is the tallest building west of the Mississippi River?
8. What is the tallest building outside of New York City, Chicago, and Philadelphia?
9. What is the 11th tallest building in the United States?
10. How does the height of the Wilshire Grand Center compare to the U.S. Bank Tower?
11. What type of complex is the Wilshire Grand Center part of?
12. What facilities or functions are included in the Wilshire Grand Center complex?
13. What is the estimated cost of developing the Wilshire Grand Center complex?
14. What are the planned retail areas in the Wilshire Grand Center development?
15. How much Class A office space is included in the Wilshire Grand Center development?
16. How many hotel rooms are planned for the Wilshire Grand Center development?
17. What is the hotel component of the Wilshire Grand Center tower?
18. How many rooms and suites does the InterContinental component comprise?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, AsymmetricProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
)


with core:
    class GeographicPlace(NonAgentiveSocialObject):
        pass

    class District(GeographicPlace):
        pass

    class City(GeographicPlace):
        pass

    class State(GeographicPlace):
        pass

    class Country(GeographicPlace):
        pass

    class River(NonAgentivePhysicalObject):
        pass

    class Building(NonAgentivePhysicalObject):
        pass

    class Tower(Building):
        pass

    class Skyscraper(Tower):
        pass

    class Complex(Building):
        pass

    class Hotel(Building):
        pass

    class RetailArea(NonAgentivePhysicalObject):
        pass

    class ObservationDeck(NonAgentivePhysicalObject):
        pass

    class ShoppingMall(Building):
        pass

    class OfficeComplex(Building):
        pass

    class OfficeSpace(NonAgentivePhysicalObject):
        pass

    class ClassAOfficeSpace(OfficeSpace):
        pass

    class HotelRoom(NonAgentivePhysicalObject):
        pass

    class Suite(NonAgentivePhysicalObject):
        pass

    class locatedIn(ObjectProperty):
        domain = [Or([Building, GeographicPlace])]
        range = [GeographicPlace]

    class tallestIn(ObjectProperty):
        domain = [Building]
        range = [GeographicPlace]

    class tallestWestOf(ObjectProperty):
        domain = [Building]
        range = [River]

    class tallestOutsideOf(ObjectProperty):
        domain = [Building]
        range = [City]

    class tallerThan(ObjectProperty, AsymmetricProperty):
        domain = [Building]
        range = [Building]

    class componentOf(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [Building]

    class includes(ObjectProperty):
        domain = [Building]
        range = [NonAgentivePhysicalObject]

    includes.inverse_property = componentOf

    class estimatedCost(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [float]

    class plannedHotelRoomCount(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [int]

    class roomsAndSuitesCount(DataProperty, FunctionalProperty):
        domain = [Hotel]
        range = [int]

    class heightRankInUnitedStates(DataProperty, FunctionalProperty):
        domain = [Skyscraper]
        range = [int]

    class MixedUseComplex(Complex):
        is_a = [
            includes.some(Hotel),
            includes.some(RetailArea),
            includes.some(ObservationDeck),
            includes.some(ShoppingMall),
            includes.some(OfficeComplex),
            includes.some(OfficeSpace),
            includes.some(ClassAOfficeSpace),
            includes.some(HotelRoom),
            includes.some(Suite),
        ]

    financialDistrict = District("FinancialDistrict")
    financialDistrict.label = "Financial District"

    downtownLosAngeles = District("DowntownLosAngeles")
    downtownLosAngeles.label = "Downtown Los Angeles"

    losAngeles = City("LosAngeles")
    losAngeles.label = "Los Angeles"

    california = State("California")
    california.label = "California"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    mississippiRiver = River("MississippiRiver")
    mississippiRiver.label = "Mississippi River"

    newYorkCity = City("NewYorkCity")
    newYorkCity.label = "New York City"

    chicago = City("Chicago")
    chicago.label = "Chicago"

    philadelphia = City("Philadelphia")
    philadelphia.label = "Philadelphia"

    usBankTower = Tower("USBankTower")
    usBankTower.label = "U.S. Bank Tower"

    wilshireGrandCenter = Skyscraper("WilshireGrandCenter")
    wilshireGrandCenter.label = "Wilshire Grand Center"
    wilshireGrandCenter.locatedIn.extend([financialDistrict, downtownLosAngeles, losAngeles, california])
    wilshireGrandCenter.tallestIn.extend([losAngeles, california])
    wilshireGrandCenter.tallestWestOf.append(mississippiRiver)
    wilshireGrandCenter.tallestOutsideOf.extend([newYorkCity, chicago, philadelphia])
    wilshireGrandCenter.tallerThan.append(usBankTower)
    wilshireGrandCenter.estimatedCost = 1200000000.0
    wilshireGrandCenter.plannedHotelRoomCount = 900
    wilshireGrandCenter.heightRankInUnitedStates = 11
    wilshireGrandCenter.is_a.append(componentOf.some(MixedUseComplex))

    intercontinental = Hotel("InterContinental")
    intercontinental.label = "InterContinental"
    intercontinental.componentOf.append(wilshireGrandCenter)
    intercontinental.roomsAndSuitesCount = 900

    financialDistrict.locatedIn.append(downtownLosAngeles)
    downtownLosAngeles.locatedIn.append(losAngeles)
    losAngeles.locatedIn.append(california)



graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
