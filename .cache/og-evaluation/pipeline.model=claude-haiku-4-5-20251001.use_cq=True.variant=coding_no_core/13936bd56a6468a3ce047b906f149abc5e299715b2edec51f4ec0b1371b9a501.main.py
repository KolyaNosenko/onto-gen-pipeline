"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What is Collins Street and where is it located?
2. When was Collins Street laid out and as part of which survey?
3. Who was Collins Street named after and what was their role?
4. What settlement did Lieutenant-Governor David Collins establish and when?
5. Why is the eastern end of Collins Street called the 'Paris End'?
6. Since when has the eastern end of Collins Street been known as the 'Paris End'?
7. What are the characteristics of the eastern end of Collins Street?
8. Which area of Collins Street became the financial heart of Melbourne in the 19th century?
9. What types of institutions were located in the western blocks of Collins Street?
10. Which street is the financial center of Collins Street centered around?
11. What architectural and commercial features define Collins Street today?
12. How has Collins Street's significance and character changed from the 19th century to present day?
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
    class Street(Thing):
        pass

    class City(Thing):
        pass

    class Region(Thing):
        pass

    class Country(Thing):
        pass

    class Person(Thing):
        pass

    class Settlement(Thing):
        pass

    class StreetArea(Thing):
        pass

    class UrbanSurvey(Thing):
        pass

    class Institution(Thing):
        pass

    class Bank(Institution):
        pass

    class InsuranceCompany(Institution):
        pass

    # Object Properties
    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Street, City, Region]
        range = [City, Region, Country]

    class namedAfter(ObjectProperty):
        domain = [Street]
        range = [Person]

    class laidOutIn(ObjectProperty):
        domain = [Street]
        range = [UrbanSurvey]

    class establishedSettlement(ObjectProperty):
        domain = [Person]
        range = [Settlement]

    class hasArea(ObjectProperty):
        domain = [Street]
        range = [StreetArea]

    # Data Properties
    class year(DataProperty, FunctionalProperty):
        domain = [UrbanSurvey, Settlement]
        range = [int]

    class knownSince(DataProperty, FunctionalProperty):
        domain = [StreetArea]
        range = [int]

    class characterizedBy(DataProperty):
        domain = [StreetArea]
        range = [str]

    # Instances
    australia = Country("Australia")
    australia.label = "Australia"
    
    sorrento = Settlement("Sorrento")
    sorrento.label = "Sorrento"
    
    parisEnd = StreetArea("ParisEnd")
    parisEnd.label = "Paris End"
    
    queenst = Street("QueenStreet")
    queenst.label = "Queen Street"
    
    victoria = Region("Victoria")
    victoria.label = "Victoria"
    
    hoddle = UrbanSurvey("HoddleGrid")
    hoddle.label = "Hoddle Grid"
    
    melbourne = City("Melbourne")
    melbourne.label = "Melbourne"
    
    davidCollins = Person("DavidCollins")
    davidCollins.label = "David Collins"
    
    collinsSt = Street("CollinsStreet")
    collinsSt.label = "Collins Street"

    # Assign properties
    collinsSt.locatedIn = [melbourne]
    collinsSt.namedAfter = [davidCollins]
    collinsSt.laidOutIn = [hoddle]
    collinsSt.hasArea = [parisEnd]

    melbourne.locatedIn = [victoria]
    victoria.locatedIn = [australia]

    hoddle.year = 1837

    davidCollins.label = ["David Collins", "Lieutenant-Governor David Collins"]
    davidCollins.establishedSettlement = [sorrento]

    sorrento.year = 1803

    parisEnd.knownSince = 1950
    parisEnd.characterizedBy = ["heritage buildings", "old street trees", "high-end shopping boutiques", "sidewalk cafes"]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
