"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

1. What was the original name of Austin, Texas?
2. In which county is Austin, Texas located?
3. Who was the Vice President of the Republic of Texas that proposed relocating the capital?
4. When did Mirabeau B. Lamar visit the area that would become Austin?
5. What was the reason for Mirabeau B. Lamar's visit to the area?
6. Where was the capital of the Republic of Texas located before it was moved to Austin?
7. What geographical feature is mentioned as being near the proposed capital location?
8. In what year was the site officially chosen as the capital of the Republic of Texas?
9. Was Austin the first capital location of the Republic of Texas?
10. Why was the city renamed from Waterloo to Austin?
11. Who was Stephen F. Austin?
12. What was Stephen F. Austin's role in the Republic of Texas?
13. In which part of Texas is Austin located?
14. What is the name of the bridge mentioned in relation to Austin's location?
15. On which bank of the Colorado River is Austin situated?
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
    # Entity classes
    class City(Thing):
        pass

    class County(Thing):
        pass

    class State(Thing):
        pass

    class GeoPoliticalEntity(Thing):
        pass

    class Person(Thing):
        pass

    class River(Thing):
        pass

    class Bridge(Thing):
        pass

    class Expedition(Thing):
        pass

    # Object Properties
    class locatedIn(ObjectProperty):
        domain = [City]
        range = [County, State]

    class partOf(ObjectProperty):
        domain = [County]
        range = [State]

    class wasCapitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [GeoPoliticalEntity]

    class isCapitalOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [GeoPoliticalEntity]

    class proposedNewCapital(ObjectProperty):
        domain = [Person]
        range = [City]

    class visitedDuring(ObjectProperty):
        domain = [Person]
        range = [Expedition]

    class renamedInHonorOf(ObjectProperty):
        domain = [City]
        range = [Person]

    class locatedNearBridge(ObjectProperty):
        domain = [City]
        range = [Bridge]

    class situatedOnRiver(ObjectProperty):
        domain = [City]
        range = [River]

    # Data Properties
    class hasOriginalName(DataProperty, FunctionalProperty):
        domain = [City]
        range = [str]

    class hasCurrentName(DataProperty, FunctionalProperty):
        domain = [City]
        range = [str]

    class situatedOnBank(DataProperty, FunctionalProperty):
        domain = [City]
        range = [str]

    class locatedInRegion(DataProperty, FunctionalProperty):
        domain = [City]
        range = [str]

    class chosenAsCapitalYear(DataProperty, FunctionalProperty):
        domain = [City]
        range = [int]

    class capitalLocationOrder(DataProperty, FunctionalProperty):
        domain = [City]
        range = [int]

    class isFinalCapitalLocation(DataProperty, FunctionalProperty):
        domain = [City]
        range = [bool]

    class hasRole(DataProperty):
        domain = [Person]
        range = [str]

    class hasEpithet(DataProperty):
        domain = [Person]
        range = [str]

    class expeditionPeriodStart(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range = [int]

    class expeditionPeriodEnd(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range = [int]

    class expeditionPurpose(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range = [str]

    # Named instances from the source text
    texas = State("TexasState")
    texas.label = "Texas"

    travis_county = County("TravisCounty")
    travis_county.label = "Travis County"
    travis_county.partOf = [texas]

    republic_of_texas = GeoPoliticalEntity("RepublicOfTexasPol")
    republic_of_texas.label = "Republic of Texas"

    stephen_f_austin = Person("StephenFAustin")
    stephen_f_austin.label = "Stephen F. Austin"
    stephen_f_austin.hasRole = ["first secretary of state"]
    stephen_f_austin.hasEpithet = ["Father of Texas"]

    colorado_river = River("ColoradoRiver")
    colorado_river.label = "Colorado River"

    ann_w_richards_congress_avenue_bridge = Bridge("AnnWRichardsCongressAvenueBridge")
    ann_w_richards_congress_avenue_bridge.label = "Ann W. Richards Congress Avenue Bridge"

    buffalo_hunting_expedition = Expedition("BuffaloHuntingExpedition")
    buffalo_hunting_expedition.label = "buffalo - hunting expedition"
    buffalo_hunting_expedition.expeditionPeriodStart = 1837
    buffalo_hunting_expedition.expeditionPeriodEnd = 1838
    buffalo_hunting_expedition.expeditionPurpose = "buffalo hunting"

    austin = City("AustinCity")
    austin.label = "Austin"
    austin.hasOriginalName = "Waterloo"
    austin.hasCurrentName = "Austin"
    austin.chosenAsCapitalYear = 1839
    austin.capitalLocationOrder = 7
    austin.isFinalCapitalLocation = True
    austin.situatedOnBank = "north"
    austin.locatedInRegion = "central"
    austin.locatedIn = [travis_county, texas]
    austin.isCapitalOf = republic_of_texas
    austin.renamedInHonorOf = [stephen_f_austin]
    austin.locatedNearBridge = [ann_w_richards_congress_avenue_bridge]
    austin.situatedOnRiver = [colorado_river]

    houston = City("HoustonCity")
    houston.label = "Houston"
    houston.wasCapitalOf = republic_of_texas

    mirabeau_b_lamar = Person("Mirabeau")
    mirabeau_b_lamar.label = "Mirabeau B. Lamar"
    mirabeau_b_lamar.hasRole = ["Vice President"]
    mirabeau_b_lamar.visitedDuring = [buffalo_hunting_expedition]
    mirabeau_b_lamar.proposedNewCapital = [austin]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
