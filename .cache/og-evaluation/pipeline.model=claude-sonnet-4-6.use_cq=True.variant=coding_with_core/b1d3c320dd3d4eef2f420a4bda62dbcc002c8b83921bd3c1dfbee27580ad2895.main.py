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
7. Which building's height does the Wilshire Grand Center surpass in Los Angeles?
8. What types of facilities are included in the Wilshire Grand Center complex?
9. What is the estimated cost of developing the Wilshire Grand Center complex?
10. How many hotel rooms does the Wilshire Grand Center contain?
11. What hotel brand operates within the Wilshire Grand Center?
12. What type of office space is available in the Wilshire Grand Center?
13. Which cities have taller buildings than the Wilshire Grand Center in the United States?
14. What is the purpose of the Wilshire Grand Center development in relation to downtown Los Angeles?
15. How many rooms and suites does the InterContinental hotel component of the Wilshire Grand Center comprise?
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

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, Feature, Society,
)

# TODO (optional): import the core properties you actually subclass.
# (no core properties subclassed; fresh properties declared below)


with core:
    # ── Entity classes (base) ──────────────────────────────────────────

    class Building(NonAgentivePhysicalObject):
        """A structure with a roof and walls, such as a house or factory."""

    class Skyscraper(Building):
        """An exceptionally tall multi-storey building."""

    class GeographicDistrict(Feature):
        """A named subdivision or area within a city or region."""

    class City(Society):
        """A large human settlement with administrative identity."""

    class USState(Society):
        """A constituent state of the United States of America."""

    class Country(Society):
        """A nation-state with recognised sovereignty."""

    class River(Feature):
        """A natural flowing watercourse."""

    class HotelFacility(NonAgentivePhysicalObject):
        """A facility providing lodging and related services within a building."""

    class RetailSpace(NonAgentivePhysicalObject):
        """An area within a building used for retail commerce."""

    class OfficeSpace(NonAgentivePhysicalObject):
        """An area within a building used for office work."""

    class ObservationDeck(NonAgentivePhysicalObject):
        """A platform or floor open to visitors for panoramic views."""

    class ShoppingMall(NonAgentivePhysicalObject):
        """An enclosed shopping complex containing multiple retail outlets."""

    # ── Properties ────────────────────────────────────────────────────

    class locatedIn(ObjectProperty, TransitiveProperty):
        """Relates a physical or social entity to a containing geographic entity."""
        domain = [Building, Feature, Society]
        range  = [Feature, Society]

    class hasComponent(ObjectProperty):
        """Relates a building to a physical component or facility it contains."""
        domain = [Building]
        range  = [NonAgentivePhysicalObject]

    class isTallestBuildingIn(ObjectProperty):
        """Relates a building to the geographic jurisdiction in which it is the tallest."""
        domain = [Building]
        range  = [Society]

    class isTallestBuildingWestOf(ObjectProperty):
        """Relates a building to a river west of which it is the tallest building."""
        domain = [Building]
        range  = [River]

    class hasTallerBuildingsIn(ObjectProperty):
        """Relates a building to a city that contains at least one taller building."""
        domain = [Building]
        range  = [City]

    class surpassesInHeight(ObjectProperty):
        """Relates a taller building to a shorter one that it exceeds in height."""
        domain = [Building]
        range  = [Building]

    class nationalHeightRanking(DataProperty, FunctionalProperty):
        """Ordinal rank of a building by height among all buildings in the country."""
        domain = [Building]
        range  = [int]

    class estimatedDevelopmentCost(DataProperty, FunctionalProperty):
        """Estimated total cost to develop the complex, in billions of US dollars."""
        domain = [NonAgentivePhysicalObject]
        range  = [float]

    class hotelRoomCount(DataProperty, FunctionalProperty):
        """Number of hotel rooms contained in a building."""
        domain = [Building]
        range  = [int]

    class roomsAndSuitesCount(DataProperty, FunctionalProperty):
        """Total number of rooms and suites in a hotel facility."""
        domain = [HotelFacility]
        range  = [int]

    class officeSpaceClass(DataProperty, FunctionalProperty):
        """Classification grade of office space (e.g. 'Class A')."""
        domain = [OfficeSpace]
        range  = [str]

    class developmentPurpose(DataProperty):
        """Stated goal or expected effect of developing the building or complex."""
        domain = [NonAgentivePhysicalObject]
        range  = [str]

    # ── Entity classes with property-based restrictions ────────────────

    class MixedUseSkyscraper(Skyscraper):
        """A skyscraper containing hotel, retail, office, observation, and mall uses."""
        is_a = [
            hasComponent.some(HotelFacility),
            hasComponent.some(RetailSpace),
            hasComponent.some(OfficeSpace),
            hasComponent.some(ObservationDeck),
            hasComponent.some(ShoppingMall),
        ]

    # ── Named individuals ──────────────────────────────────────────────

    # Geographic entities
    losAngeles = City("LosAngeles")
    losAngeles.label = "Los Angeles"

    california = USState("California")
    california.label = "California"

    newYorkCity = City("NewYorkCity")
    newYorkCity.label = "New York City"

    chicago = City("Chicago")
    chicago.label = "Chicago"

    philadelphia = City("Philadelphia")
    philadelphia.label = "Philadelphia"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    financialDistrict = GeographicDistrict("FinancialDistrict")
    financialDistrict.label = "Financial District"

    downtownLosAngeles = GeographicDistrict("DowntownLosAngeles")
    downtownLosAngeles.label = "Downtown Los Angeles"

    mississippiRiver = River("MississippiRiver")
    mississippiRiver.label = "Mississippi River"

    # Location hierarchy (transitivity propagates upward)
    financialDistrict.locatedIn.append(downtownLosAngeles)
    downtownLosAngeles.locatedIn.append(losAngeles)
    losAngeles.locatedIn.append(california)
    california.locatedIn.append(unitedStates)

    # Buildings
    wilshireGrandCenter = MixedUseSkyscraper("WilshireGrandCenter")
    wilshireGrandCenter.label = "Wilshire Grand Center"

    usBankTower = Building("USBankTower")
    usBankTower.label = "U.S. Bank Tower"

    usBankTower.locatedIn.append(losAngeles)

    # Hotel facility
    intercontinental = HotelFacility("InterContinental")
    intercontinental.label = "InterContinental"

    # Office space (Class A)
    classAOfficeSpace = OfficeSpace("ClassAOfficeSpace")
    classAOfficeSpace.label = "Class A office space"
    classAOfficeSpace.officeSpaceClass = "Class A"

    # Property assertions on Wilshire Grand Center
    wilshireGrandCenter.locatedIn.append(financialDistrict)
    wilshireGrandCenter.isTallestBuildingIn.append(losAngeles)
    wilshireGrandCenter.isTallestBuildingIn.append(california)
    wilshireGrandCenter.isTallestBuildingWestOf.append(mississippiRiver)
    wilshireGrandCenter.hasTallerBuildingsIn.append(newYorkCity)
    wilshireGrandCenter.hasTallerBuildingsIn.append(chicago)
    wilshireGrandCenter.hasTallerBuildingsIn.append(philadelphia)
    wilshireGrandCenter.surpassesInHeight.append(usBankTower)
    wilshireGrandCenter.nationalHeightRanking = 11
    wilshireGrandCenter.estimatedDevelopmentCost = 1.2
    wilshireGrandCenter.hotelRoomCount = 900
    wilshireGrandCenter.hasComponent.append(intercontinental)
    wilshireGrandCenter.hasComponent.append(classAOfficeSpace)
    wilshireGrandCenter.developmentPurpose.append("revitalize downtown Los Angeles")

    intercontinental.roomsAndSuitesCount = 900


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
