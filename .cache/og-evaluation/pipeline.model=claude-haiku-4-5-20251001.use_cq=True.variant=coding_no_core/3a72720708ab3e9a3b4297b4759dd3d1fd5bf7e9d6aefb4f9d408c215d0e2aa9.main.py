"""
=== TASK INPUT ===
Source text:
Verbena , also known as Summerfield , is an unincorporated community in southeastern Chilton County , Alabama , United States . Named for the indigenous flower , Verbena developed into a popular resort location for the more affluent citizenry of Montgomery , the state 's capital , during the yellow fever outbreaks of the late 19th and early 20th centuries . Many stately homes , some of which have undergone recent renovation and restoration , line the streets of the town as a reminder of this historic past . The town was built beside the railroad currently owned by CSX Transportation . In its heyday , Verbena had two hotels , a bank , a post office , and a general store . Many of those buildings are gone or boarded up today , but the Verbena United Methodist Church still stands on County Road 59 near the town 's center . According to the U.S. Census in 1890 , Verbena showed a population of 756 , making it the largest community in Chilton County at that time .

1. What is Verbena also known as?
2. Where is Verbena located?
3. What county and state is Verbena in?
4. Why was Verbena named?
5. What type of community is Verbena?
6. During which time period did Verbena develop as a resort location?
7. Who primarily visited Verbena as a resort destination?
8. What triggered the development of Verbena as a resort?
9. What types of buildings can be found in Verbena?
10. Which railroad company currently owns the railroad in Verbena?
11. What facilities and services did Verbena have during its heyday?
12. Which buildings from Verbena's heyday still stand today?
13. What is the name of the church in Verbena and where is it located?
14. What was Verbena's population according to the 1890 U.S. Census?
15. What was Verbena's ranking among communities in Chilton County in 1890?
16. What is the current condition of historic buildings in Verbena?
17. What industries or economic activities supported Verbena in the past?
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
    # Domain entity classes
    class Community(Thing): pass
    class UnincorporatedCommunity(Community): pass
    class County(Thing): pass
    class State(Thing): pass
    class Country(Thing): pass
    class City(Thing): pass
    class Building(Thing): pass
    class Church(Building): pass
    class Hotel(Building): pass
    class Bank(Building): pass
    class PostOffice(Building): pass
    class GeneralStore(Building): pass
    class ResidentialBuilding(Building): pass
    class Railroad(Thing): pass
    class TransportationCompany(Thing): pass
    class Road(Thing): pass
    class Flower(Thing): pass
    
    # Domain properties
    class locatedInCounty(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range = [County]
    
    class locatedInState(ObjectProperty, FunctionalProperty):
        domain = [County]
        range = [State]
    
    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [State]
        range = [Country]
    
    class namedFor(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range = [Flower]
    
    class capitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [State]
    
    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [Railroad]
        range = [TransportationCompany]
    
    class locatedOn(ObjectProperty):
        domain = [Building]
        range = [Road]
    
    class hasBuilding(ObjectProperty):
        domain = [Community]
        range = [Building]
    
    class populationIn(DataProperty, FunctionalProperty):
        domain = [Community]
        range = [int]
    
    class isLargestInCounty(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range = [County]
    
    class developedDuring(DataProperty):
        domain = [Community]
        range = [str]
    
    class developedForVisitors(DataProperty):
        domain = [Community]
        range = [str]
    
    class builtBeside(ObjectProperty, FunctionalProperty):
        domain = [Community]
        range = [Railroad]
    
    class currentCondition(DataProperty):
        domain = [Building]
        range = [str]
    
    class hasResidences(DataProperty):
        domain = [Community]
        range = [str]
    
    # Named individual instances from source text
    united_states = Country("UnitedStates")
    united_states.label = "United States"
    
    alabama = State("Alabama")
    alabama.locatedInCountry = united_states
    
    chilton_county = County("ChiltonCounty")
    chilton_county.label = "Chilton County"
    chilton_county.locatedInState = alabama
    
    montgomery = City("Montgomery")
    montgomery.capitalOf = alabama
    
    verbena = UnincorporatedCommunity("Verbena")
    verbena.label = ["Verbena", "Summerfield"]
    verbena.locatedInCounty = chilton_county
    verbena.populationIn = 756
    verbena.isLargestInCounty = chilton_county
    verbena.developedDuring = ["late 19th and early 20th centuries"]
    verbena.developedForVisitors = ["more affluent citizenry of Montgomery"]
    verbena.hasResidences = ["many stately homes, some of which have undergone recent renovation and restoration"]
    
    verbena_flower = Flower("VerbenaFlower")
    verbena_flower.label = "Verbena"
    verbena.namedFor = verbena_flower
    
    csx = TransportationCompany("CSXTransportation")
    csx.label = "CSX Transportation"
    
    railroad = Railroad("VerbenaRailroad")
    railroad.ownedBy = csx
    
    verbena.builtBeside = railroad
    
    county_road_59 = Road("CountyRoad59")
    county_road_59.label = "County Road 59"
    
    church = Church("VerbenaUnitedMethodistChurch")
    church.label = "Verbena United Methodist Church"
    church.locatedOn = [county_road_59]
    church.currentCondition = ["still stands"]
    
    # Unnamed buildings from heyday (no proper-noun names in source text)
    hotel1 = Hotel()
    hotel2 = Hotel()
    bank = Bank()
    post_office = PostOffice()
    general_store = GeneralStore()
    
    # Current condition of buildings
    hotel1.currentCondition = ["gone or boarded up"]
    hotel2.currentCondition = ["gone or boarded up"]
    bank.currentCondition = ["gone or boarded up"]
    post_office.currentCondition = ["gone or boarded up"]
    general_store.currentCondition = ["gone or boarded up"]
    
    # Link buildings to community
    verbena.hasBuilding = [hotel1, hotel2, bank, post_office, general_store, church]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
