"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

1. What is the nationality/location of the Falck Group?
2. When was the Falck Group founded?
3. Who founded the Falck Group?
4. What was the original name of the Falck Group at its founding?
5. Where were the first industrial plants of the Falck Group built?
6. When did the Falck Group change its name, and what was the new name?
7. What industry was the Falck Group originally part of?
8. What products did the Falck Group produce during its steel industry years?
9. When did the Falck Group close its last furnaces?
10. When did the Falck Group transition to renewable energy production?
11. Which subsidiary did the Falck Group use to produce renewable energy?
12. Which family has been running the Falck Group?
13. In what city was the Falck Group originally founded?
14. How long did the Falck Group produce steel and related products?
15. What caused the decline of the Falck Group's steel production?
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
    # --- Entity classes ---
    class Company(Thing): pass
    class Person(Thing): pass
    class Family(Thing): pass
    class City(Thing): pass
    class Industry(Thing): pass
    class IndustrialPlant(Thing): pass
    class Furnace(IndustrialPlant): pass
    class Product(Thing): pass
    class SteelProduct(Product): pass
    class ProcessedProduct(SteelProduct): pass
    class SemiFinishedProduct(SteelProduct): pass
    class EnergySource(Thing): pass
    class RenewableEnergySource(EnergySource): pass

    # --- Object properties ---
    class locatedIn(ObjectProperty):
        domain = [Company]
        range  = [City]

    class foundedBy(ObjectProperty):
        domain = [Company]
        range  = [Person]

    class foundedInCity(ObjectProperty):
        domain = [Company]
        range  = [City]

    class hasSubsidiary(ObjectProperty):
        domain = [Company]
        range  = [Company]

    class runBy(ObjectProperty):
        domain = [Company]
        range  = [Family]

    class partOfIndustry(ObjectProperty):
        domain = [Company]
        range  = [Industry]

    class produces(ObjectProperty):
        domain = [Company]
        range  = [Product]

    class hasIndustrialPlant(ObjectProperty):
        domain = [Company]
        range  = [IndustrialPlant]

    class plantLocatedIn(ObjectProperty):
        domain = [IndustrialPlant]
        range  = [City]

    class producesEnergyFrom(ObjectProperty):
        domain = [Company]
        range  = [EnergySource]

    # --- Data properties ---
    class hasNationality(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    class foundingYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [int]

    class originalName(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    class nameChangedYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [int]

    class nameAfterChange(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    class steelProductionDuration(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    class declineCause(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    class lastFurnaceClosureYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [int]

    class transitionToRenewableDecade(DataProperty, FunctionalProperty):
        domain = [Company]
        range  = [str]

    # --- Named individuals ---

    # Cities
    sestoSanGiovanni = City("SestoSanGiovanni")
    sestoSanGiovanni.label = "Sesto San Giovanni"

    milanCity = City("Milan")
    milanCity.label = "Milan"

    # Person
    giorgioEnricoFalck = Person("GiorgioEnricoFalck")
    giorgioEnricoFalck.label = "Giorgio Enrico Falck"

    # Family
    falckFamily = Family("FalckFamily")
    falckFamily.label = "Falck family"

    # Industry
    steelIndustry = Industry("SteelIndustry")
    steelIndustry.label = "steel industry"

    # Products
    steelInst = SteelProduct("SteelInst")
    steelInst.label = "steel"

    processedProductsInst = ProcessedProduct("ProcessedProductsInst")
    processedProductsInst.label = "processed products"

    semiFinishedProductsInst = SemiFinishedProduct("SemiFinishedProductsInst")
    semiFinishedProductsInst.label = "semi-finished products"

    # Renewable energy source
    renewableEnergyInst = RenewableEnergySource("RenewableEnergyInst")
    renewableEnergyInst.label = "renewable energy"

    # Industrial plant
    firstIndustrialPlantsInst = IndustrialPlant("FirstIndustrialPlantsInst")
    firstIndustrialPlantsInst.label = "first industrial plants"
    firstIndustrialPlantsInst.plantLocatedIn = [sestoSanGiovanni]

    # Subsidiary company
    falckRenewables = Company("FalckRenewables")
    falckRenewables.label = "Falck Renewables"

    # Main company and its facts
    falckGroup = Company("FalckGroup")
    falckGroup.label = "Falck Group"
    falckGroup.hasNationality = "Italian"
    falckGroup.locatedIn = [sestoSanGiovanni]
    falckGroup.foundingYear = 1906
    falckGroup.foundedBy = [giorgioEnricoFalck]
    falckGroup.foundedInCity = [milanCity]
    falckGroup.originalName = "Società anonima Acciaierie e Ferriere Lombarde"
    falckGroup.nameChangedYear = 1931
    falckGroup.nameAfterChange = "Acciaiere e Ferriere Lombarde Falck"
    falckGroup.partOfIndustry = [steelIndustry]
    falckGroup.produces = [steelInst, processedProductsInst, semiFinishedProductsInst]
    falckGroup.steelProductionDuration = "over seventy years"
    falckGroup.declineCause = "crisis in the mid-seventies"
    falckGroup.lastFurnaceClosureYear = 1995
    falckGroup.transitionToRenewableDecade = "end of the nineties"
    falckGroup.runBy = [falckFamily]
    falckGroup.hasSubsidiary = [falckRenewables]
    falckGroup.hasIndustrialPlant = [firstIndustrialPlantsInst]
    falckGroup.producesEnergyFrom = [renewableEnergyInst]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
