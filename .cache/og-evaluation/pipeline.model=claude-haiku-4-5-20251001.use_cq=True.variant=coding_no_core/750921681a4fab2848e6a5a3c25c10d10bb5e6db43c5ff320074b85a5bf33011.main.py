"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

1. Where is Falck Group located?

2. When was Falck Group founded?

3. Who founded Falck Group?

4. What was the original name of Falck Group?

5. What industry was Falck Group originally involved in?

6. What products did Falck Group manufacture?

7. When did Falck Group change its name to Acciaiere e Ferriere Lombarde Falck?

8. Where were the first industrial plants of Falck Group built?

9. When did the last furnaces of Falck Group close?

10. What caused the decline of Falck Group in the mid-seventies?

11. When did Falck Group transition to renewable energy production?

12. Which subsidiary company does Falck Group use for renewable energy production?

13. Who currently runs Falck Group?

14. For how many years did Falck Group produce steel and related products?

15. What types of steel products did Falck Group produce?
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
    class Location(Thing):
        pass

    class Company(Thing):
        pass

    class Person(Thing):
        pass

    class Family(Thing):
        pass

    class ManufacturingPlant(Thing):
        pass

    # Object Properties
    class foundedBy(ObjectProperty):
        domain = [Company]
        range = [Person]

    class foundedIn(ObjectProperty):
        domain = [Company]
        range = [Location]

    class locatedIn(ObjectProperty):
        domain = [Company]
        range = [Location]

    class hasPlant(ObjectProperty):
        domain = [Company]
        range = [ManufacturingPlant]

    class plantLocation(ObjectProperty):
        domain = [ManufacturingPlant]
        range = [Location]

    class runBy(ObjectProperty):
        domain = [Company]
        range = [Family]

    class hasSubsidiary(ObjectProperty):
        domain = [Company]
        range = [Company]

    # Data Properties
    class foundedYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class originalName(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]

    class nameChangedYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class newName(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]

    class producedProduct(DataProperty):
        domain = [Company]
        range = [str]

    class lastFurnaceClosureYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class transitionYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class productionDurationYears(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class industry(DataProperty):
        domain = [Company]
        range = [str]

    # Instances
    falck_group = Company("FalckGroup")
    falck_group.label = "Falck Group"
    falck_group.foundedYear = 1906
    falck_group.originalName = "Società anonima Acciaierie e Ferriere Lombarde"
    falck_group.nameChangedYear = 1931
    falck_group.newName = "Acciaiere e Ferriere Lombarde Falck"
    falck_group.lastFurnaceClosureYear = 1995
    falck_group.producedProduct = ["steel", "processed products", "semi-finished products"]
    falck_group.productionDurationYears = 70
    falck_group.transitionYear = 1998
    falck_group.industry = ["steel industry", "renewable energy"]

    sesto_san_giovanni = Location("SestoSanGiovanni")
    sesto_san_giovanni.label = "Sesto San Giovanni"

    milan = Location("Milan")
    milan.label = "Milan"

    giorgio_enrico_falck = Person("GiorgioEnricoFalck")
    giorgio_enrico_falck.label = "Giorgio Enrico Falck"

    falck_family = Family("FalckFamily")
    falck_family.label = "Falck family"

    falck_renewables = Company("FalckRenewables")
    falck_renewables.label = "Falck Renewables"

    first_plants = ManufacturingPlant("FirstPlants")
    first_plants.label = "first industrial plants"
    first_plants.plantLocation = [sesto_san_giovanni]

    # Set object properties
    falck_group.foundedBy = [giorgio_enrico_falck]
    falck_group.foundedIn = [milan]
    falck_group.locatedIn = [sesto_san_giovanni]
    falck_group.runBy = [falck_family]
    falck_group.hasSubsidiary = [falck_renewables]
    falck_group.hasPlant = [first_plants]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
