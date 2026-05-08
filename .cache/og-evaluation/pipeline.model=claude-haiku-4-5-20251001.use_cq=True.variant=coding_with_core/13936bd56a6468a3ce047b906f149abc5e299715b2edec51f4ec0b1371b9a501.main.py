"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What is Collins Street and where is it located?
2. When was Collins Street laid out and what was the original plan called?
3. Who was Collins Street named after and what did that person do?
4. Why is the eastern end of Collins Street known as the 'Paris End'?
5. When did the 'Paris End' designation become commonly used?
6. What types of buildings and features characterize the 'Paris End' of Collins Street?
7. Which street became the financial heart of Melbourne in the 19th century?
8. What types of institutions were historically located along Collins Street?
9. What is the current status of Collins Street as a financial district?
10. What architectural and commercial features distinguish different sections of Collins Street?
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
    NonAgentivePhysicalObject, Society, AgentivePhysicalObject,
    NonPhysicalObject, Accomplishment
)
from og_sandbox_with_core.core.properties import partOf


with core:
    # Entity classes
    
    class Street(NonAgentivePhysicalObject):
        """A major thoroughfare in a city."""
        pass
    
    class City(Society):
        """An urban settlement."""
        pass
    
    class Region(Society):
        """A geographic region within a country."""
        pass
    
    class Country(Society):
        """A sovereign nation."""
        pass
    
    class UrbanPlan(NonPhysicalObject):
        """A design or plan for urban layout."""
        pass
    
    class UrbanGridPlan(UrbanPlan):
        """A grid-based plan for urban layout."""
        pass
    
    class StreetSection(NonAgentivePhysicalObject):
        """A section or portion of a street."""
        pass
    
    class Building(NonAgentivePhysicalObject):
        """A constructed structure."""
        pass
    
    class HeritageBuilding(Building):
        """A building of cultural or historical significance."""
        pass
    
    class ShoppingBoutique(Building):
        """A small high-end retail shop."""
        pass
    
    class SidewalkCafe(Building):
        """An outdoor cafe on the street."""
        pass
    
    class OfficeBlock(Building):
        """A building containing offices."""
        pass
    
    class Skyscraper(Building):
        """A tall multi-story building."""
        pass
    
    class StreetTree(NonAgentivePhysicalObject):
        """A tree planted along a street."""
        pass
    
    class FinancialInstitution(Society):
        """An organization dealing with financial services."""
        pass
    
    class Bank(FinancialInstitution):
        """A financial institution that provides banking services."""
        pass
    
    class InsuranceCompany(FinancialInstitution):
        """A financial institution that provides insurance services."""
        pass
    
    class UrbanSettlement(Accomplishment):
        """An event of establishing a settlement."""
        pass

    # Properties
    
    class locatedIn(ObjectProperty, FunctionalProperty):
        """Relation indicating that something is located in a place."""
        domain = [Street, Society]
        range = [Society]
    
    class namedAfter(ObjectProperty, FunctionalProperty):
        """Relation indicating that something is named after someone."""
        domain = [Street]
        range = [AgentivePhysicalObject]
    
    class basedOn(ObjectProperty, FunctionalProperty):
        """Relation indicating that something is based on a plan or design."""
        domain = [Street]
        range = [UrbanPlan]
    
    class laidOutYear(DataProperty, FunctionalProperty):
        """The year a street was laid out."""
        domain = [Street]
        range = [int]
    
    class designatedSince(DataProperty, FunctionalProperty):
        """The year or period since which something is known by a designation."""
        domain = [StreetSection]
        range = [int]

    # Instances
    
    collins_street = Street("CollinsStreet")
    collins_street.label = "Collins Street"
    collins_street.laidOutYear = 1837
    
    melbourne = City("Melbourne")
    melbourne.label = "Melbourne"
    
    victoria = Region("Victoria")
    victoria.label = "Victoria"
    
    australia = Country("Australia")
    australia.label = "Australia"
    
    david_collins = AgentivePhysicalObject("DavidCollins")
    david_collins.label = "David Collins"
    
    sorrento = City("Sorrento")
    sorrento.label = "Sorrento"
    
    queen_street = Street("QueenStreet")
    queen_street.label = "Queen Street"
    
    hoddle_grid = UrbanGridPlan("HoddleGrid")
    hoddle_grid.label = "Hoddle Grid"
    
    paris_end = StreetSection("ParisEnd")
    paris_end.label = "Paris End"
    paris_end.designatedSince = 1950
    
    # Relationships - Location hierarchy
    collins_street.locatedIn = melbourne
    melbourne.locatedIn = victoria
    victoria.locatedIn = australia
    sorrento.locatedIn = australia
    queen_street.locatedIn = melbourne
    
    # Relationships - Naming and Design
    collins_street.namedAfter = david_collins
    collins_street.basedOn = hoddle_grid
    
    # Relationships - Spatial structure
    paris_end.partOf = [collins_street]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
