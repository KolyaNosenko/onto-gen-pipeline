"""
=== TASK INPUT ===
Source text:
Wilshire Grand Center is a skyscraper in the Financial District of Downtown Los Angeles , California . It is the tallest building in Los Angeles , the tallest building in California , the tallest building west of the Mississippi River and outside of New York City , Chicago , and Philadelphia , and the 11th tallest building in the United States . Its height surpasses the U.S. Bank Tower by . The building is part of a mixed - use hotel , retail , observation decks , shopping mall , and office complex , expected to revitalize downtown Los Angeles and the area surrounding the building . The development of the complex is estimated to cost $ 1.2 billion . The plans include of retail , of Class A office space and 900 hotel rooms . InterContinental is the tower 's hotel component , comprising 900 rooms and suites .

1. What is the height of Wilshire Grand Center?
2. Where is Wilshire Grand Center located?
3. Is Wilshire Grand Center the tallest building in California?
4. What is the ranking of Wilshire Grand Center among the tallest buildings in the United States?
5. Which building does Wilshire Grand Center surpass in height?
6. What types of facilities are included in the Wilshire Grand Center complex?
7. What is the estimated development cost of Wilshire Grand Center?
8. How many hotel rooms does the InterContinental hotel component have?
9. How much retail space is planned for Wilshire Grand Center?
10. How much Class A office space is included in the development?
11. What is the purpose of the Wilshire Grand Center development?
12. Which hotel operates the tower's hotel component?
13. Is Wilshire Grand Center the tallest building west of the Mississippi River?
14. What geographic regions does Wilshire Grand Center exceed in terms of building height?
15. What mixed-use components are part of the Wilshire Grand Center complex?
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

from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, PhysicalQuality, AbstractQuality, SpaceRegion, Society
)
from og_sandbox_with_core.core.properties import directQualityOf


with core:
    # Entity classes
    class Building(NonAgentivePhysicalObject):
        """A building structure."""
        pass

    class Skyscraper(Building):
        """A tall building, typically for office/residential/hotel use."""
        pass

    class HotelBrand(Society):
        """A hotel company or brand that operates hotels."""
        pass

    class HotelComponent(NonAgentivePhysicalObject):
        """A hotel component within a larger complex."""
        pass

    class MixedUseComplex(NonAgentivePhysicalObject):
        """A complex with multiple uses (hotel, retail, offices, etc.)."""
        pass

    class GeographicRegion(SpaceRegion):
        """A geographic region or area."""
        pass

    class Height(PhysicalQuality):
        """A physical quality representing the height of a building."""
        pass

    class RankingPosition(AbstractQuality):
        """An abstract quality representing a ranking or position."""
        pass

    class DevelopmentCost(AbstractQuality):
        """An abstract quality representing the cost of development."""
        pass

    # Object Properties
    class locatedIn(ObjectProperty):
        """A spatial relation indicating where something is located."""
        domain = [Building, HotelComponent, MixedUseComplex, GeographicRegion]
        range = [GeographicRegion]

    class tallestBuildingIn(ObjectProperty):
        """Indicates that a building is the tallest in a given region."""
        domain = [Building, Skyscraper]
        range = [GeographicRegion]

    class surpassesInHeight(ObjectProperty):
        """Indicates that one building surpasses another in height."""
        domain = [Building, Skyscraper]
        range = [Building, Skyscraper]

    class operatedBy(ObjectProperty):
        """Indicates that a hotel component is operated by a hotel brand."""
        domain = [HotelComponent, HotelBrand]
        range = [HotelBrand]

    class includesComponent(ObjectProperty):
        """Indicates that a complex includes a specific component."""
        domain = [MixedUseComplex]
        range = [Building, HotelComponent, NonAgentivePhysicalObject]

    class hasHeight(ObjectProperty):
        """Relates a building to its height quality."""
        domain = [Building, Skyscraper]
        range = [Height]

    class hasCost(ObjectProperty):
        """Relates a development to its cost quality."""
        domain = [MixedUseComplex]
        range = [DevelopmentCost]

    class hasRanking(ObjectProperty):
        """Relates a building to its ranking quality."""
        domain = [Building, Skyscraper]
        range = [RankingPosition]

    # Data Properties
    class numberOfRooms(DataProperty, FunctionalProperty):
        """The number of rooms in a hotel component."""
        domain = [HotelComponent]
        range = [int]

    class developmentCostValue(DataProperty, FunctionalProperty):
        """The cost of development in billions of USD."""
        domain = [DevelopmentCost]
        range = [float]

    class rankingValue(DataProperty, FunctionalProperty):
        """The numeric ranking value."""
        domain = [RankingPosition]
        range = [int]

    # Named instances - Geographic Regions
    los_angeles = GeographicRegion("LosAngeles")
    los_angeles.label = "Los Angeles"

    california = GeographicRegion("California")
    california.label = "California"

    financial_district = GeographicRegion("FinancialDistrict")
    financial_district.label = "Financial District"

    downtown_los_angeles = GeographicRegion("DowntownLosAngeles")
    downtown_los_angeles.label = "Downtown Los Angeles"

    mississippi_river = GeographicRegion("MississippiRiver")
    mississippi_river.label = "Mississippi River"

    new_york_city = GeographicRegion("NewYorkCity")
    new_york_city.label = "New York City"

    chicago = GeographicRegion("Chicago")
    chicago.label = "Chicago"

    philadelphia = GeographicRegion("Philadelphia")
    philadelphia.label = "Philadelphia"

    united_states = GeographicRegion("UnitedStates")
    united_states.label = "United States"

    # Named instances - Buildings
    wilshire_grand_center = Skyscraper("WilshireGrandCenter")
    wilshire_grand_center.label = "Wilshire Grand Center"
    wilshire_grand_center.locatedIn.append(financial_district)
    wilshire_grand_center.locatedIn.append(downtown_los_angeles)
    wilshire_grand_center.locatedIn.append(california)
    wilshire_grand_center.tallestBuildingIn.append(los_angeles)
    wilshire_grand_center.tallestBuildingIn.append(california)
    wilshire_grand_center.tallestBuildingIn.append(united_states)

    us_bank_tower = Building("USBankTower")
    us_bank_tower.label = "U.S. Bank Tower"

    wilshire_grand_center.surpassesInHeight.append(us_bank_tower)

    # Named instances - Hotel and Complex
    intercontinental = HotelBrand("InterContinental")
    intercontinental.label = "InterContinental"

    hotel_component = HotelComponent("InterContinentalHotelComponent")
    hotel_component.label = "InterContinental"
    hotel_component.numberOfRooms = 900
    hotel_component.operatedBy.append(intercontinental)

    mixed_use_complex = MixedUseComplex("WilshireGrandComplex")
    mixed_use_complex.label = "Wilshire Grand Center complex"
    mixed_use_complex.includesComponent.append(wilshire_grand_center)
    mixed_use_complex.includesComponent.append(hotel_component)

    # Development cost
    development_cost = DevelopmentCost("WilshireGrandDevelopmentCost")
    development_cost.label = "Wilshire Grand Center development cost"
    development_cost.developmentCostValue = 1.2

    mixed_use_complex.hasCost.append(development_cost)

    # Ranking
    ranking = RankingPosition("WilshireGrandRanking")
    ranking.label = "Wilshire Grand Center ranking in United States"
    ranking.rankingValue = 11

    wilshire_grand_center.hasRanking.append(ranking)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
