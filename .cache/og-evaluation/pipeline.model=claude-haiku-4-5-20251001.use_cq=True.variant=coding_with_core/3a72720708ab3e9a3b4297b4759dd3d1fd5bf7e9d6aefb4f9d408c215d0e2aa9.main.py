"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is Verbena also known as?
2. Where is Verbena located?
3. What county and state is Verbena in?
4. Why was Verbena named?
5. What was Verbena's primary function during the late 19th and early 20th centuries?
6. What historical events led to Verbena's popularity as a resort location?
7. What types of buildings can be found in Verbena?
8. Which railroad company currently owns the railroad in Verbena?
9. What infrastructure and services did Verbena have during its heyday?
10. Which buildings from Verbena's heyday are still standing today?
11. What is the name and location of the church in Verbena?
12. What was Verbena's population according to the 1890 U.S. Census?
13. Was Verbena the largest community in Chilton County in 1890?
14. What is the current status of historical buildings in Verbena?
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

# Import core entity classes
from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, AgentiveSocialObject,
)


with core:
    # Entity Classes
    class UnincorporatedCommunity(NonAgentivePhysicalObject):
        """An unincorporated community is a place without formal incorporation."""
        pass
    
    class County(NonAgentivePhysicalObject):
        """A county is an administrative division."""
        pass
    
    class State(NonAgentivePhysicalObject):
        """A state is a geopolitical entity."""
        pass
    
    class City(NonAgentivePhysicalObject):
        """A city is an urban settlement."""
        pass
    
    class Building(NonAgentivePhysicalObject):
        """A building is a constructed structure."""
        pass
    
    class Hotel(Building):
        """A hotel is a commercial building for lodging."""
        pass
    
    class Bank(Building):
        """A bank is a financial institution building."""
        pass
    
    class PostOffice(Building):
        """A post office is a building for mail services."""
        pass
    
    class GeneralStore(Building):
        """A general store is a commercial building selling diverse goods."""
        pass
    
    class Church(Building):
        """A church is a religious building."""
        pass
    
    class StatelySoalHome(Building):
        """A stately home is a large and impressive private residence."""
        pass
    
    class Road(NonAgentivePhysicalObject):
        """A road is a route for transportation."""
        pass
    
    class Railroad(NonAgentivePhysicalObject):
        """A railroad is a transportation infrastructure."""
        pass
    
    class TransportationCompany(AgentiveSocialObject):
        """A transportation company operates transportation services."""
        pass

    # Object Properties
    class locatedIn(ObjectProperty):
        """Indicates spatial location of an entity within another."""
        domain = [UnincorporatedCommunity, County, Building, Road, Railroad, City, State]
        range = [UnincorporatedCommunity, County, Road, City, State]
    
    class locatedOn(ObjectProperty):
        """Indicates that an entity is situated on another (e.g., building on road)."""
        domain = [Building, Road]
        range = [Road]
    
    class ownedBy(ObjectProperty):
        """Indicates ownership relationship."""
        domain = [Railroad]
        range = [TransportationCompany]

    # Data Properties
    class population(DataProperty, FunctionalProperty):
        """Records the population of a community at a specific time."""
        domain = [UnincorporatedCommunity, City, County]
        range = [int]

    # Named Individuals
    # Place: Verbena
    verbena = UnincorporatedCommunity("Verbena")
    verbena.label = ["Verbena", "Summerfield"]
    
    # County and State
    chilton_county = County("ChiltonCounty")
    chilton_county.label = "Chilton County"
    
    alabama = State("Alabama")
    alabama.label = "Alabama"
    
    # City: Montgomery
    montgomery = City("Montgomery")
    montgomery.label = "Montgomery"
    
    # Transportation Company
    csx = TransportationCompany("CSXTransportation")
    csx.label = "CSX Transportation"
    
    # Road
    county_road_59 = Road("CountyRoad59")
    county_road_59.label = "County Road 59"
    
    # Railroad
    railroad = Railroad("VerbenaRailroad")
    railroad.label = "railroad near Verbena"
    
    # Church (specifically named)
    church = Church("VerbenaUnitedMethodistChurch")
    church.label = "Verbena United Methodist Church"
    
    # Buildings during heyday (inferred from text)
    hotel_1 = Hotel("VerbenaHotel_1")
    hotel_1.label = "hotel in Verbena"
    
    hotel_2 = Hotel("VerbenaHotel_2")
    hotel_2.label = "hotel in Verbena"
    
    bank = Bank("VerbenaBank")
    bank.label = "bank in Verbena"
    
    post_office = PostOffice("VerbenaPostOffice")
    post_office.label = "post office in Verbena"
    
    general_store = GeneralStore("VerbenaGeneralStore")
    general_store.label = "general store in Verbena"

    # Spatial Relationships
    verbena.locatedIn.append(chilton_county)
    chilton_county.locatedIn.append(alabama)
    montgomery.locatedIn.append(alabama)
    
    # Population data
    verbena.population = 756
    
    # Railroad and ownership
    railroad.locatedIn.append(verbena)
    railroad.ownedBy.append(csx)
    
    # Church location
    church.locatedIn.append(verbena)
    church.locatedOn.append(county_road_59)
    
    # Buildings in Verbena
    hotel_1.locatedIn.append(verbena)
    hotel_2.locatedIn.append(verbena)
    bank.locatedIn.append(verbena)
    post_office.locatedIn.append(verbena)
    general_store.locatedIn.append(verbena)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
