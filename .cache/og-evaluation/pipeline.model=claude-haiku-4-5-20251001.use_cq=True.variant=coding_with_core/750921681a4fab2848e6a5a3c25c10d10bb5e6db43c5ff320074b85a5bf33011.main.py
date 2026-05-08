"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

1. Where is Falck Group located?
2. When was Falck Group founded?
3. Who founded Falck Group?
4. What was the original name of Falck Group?
5. What are the main industrial plants of Falck Group and where are they located?
6. What products did Falck Group produce during its steel industry period?
7. When did Falck Group change its name to Acciaiere e Ferriere Lombarde Falck?
8. When did Falck Group's last furnaces close?
9. What caused the decline of Falck Group in the mid-seventies?
10. When did Falck Group transition to renewable energy production?
11. How long did Falck Group operate in the steel industry?
12. Who runs Falck Group at the end of the nineties?
13. What is Falck Renewables?
14. Is Falck Renewables a subsidiary of Falck Group?
15. What types of renewable energy does Falck Group produce?
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
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    Society,
    SpaceRegion,
)


with core:
    # Domain entity classes
    class Company(Society):
        pass

    class Person(AgentivePhysicalObject):
        pass

    class Location(SpaceRegion):
        pass

    class IndustrialPlant(NonAgentivePhysicalObject):
        pass

    # Domain properties
    class locatedIn(ObjectProperty):
        domain = [Company, IndustrialPlant]
        range = [Location]

    class foundedBy(ObjectProperty):
        domain = [Company]
        range = [Person]

    class foundedAtPlace(ObjectProperty):
        domain = [Company]
        range = [Location]

    class foundationYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class hasPlant(ObjectProperty):
        domain = [Company]
        range = [IndustrialPlant]

    class hasSubsidiary(ObjectProperty):
        domain = [Company]
        range = [Company]

    class originalName(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]

    class nameChangeYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class newName(DataProperty):
        domain = [Company]
        range = [str]

    class lastFurnaceClosureYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class declineStartYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class renewableEnergyTransitionYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class steelProductionStartYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class steelProductionEndYear(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [int]

    class producedProducts(DataProperty):
        domain = [Company]
        range = [str]

    class managedByFamily(DataProperty):
        domain = [Company]
        range = [str]

    # Named instances from the source text
    sesto = Location("SestoSanGiovanni")
    sesto.label = "Sesto San Giovanni"

    milan = Location("Milan")
    milan.label = "Milan"

    giorgio = Person("GiorgioEnricoFalck")
    giorgio.label = "Giorgio Enrico Falck"

    falck_group = Company("FalckGroup")
    falck_group.label = "Falck Group"
    falck_group.locatedIn = [sesto]
    falck_group.foundedBy = [giorgio]
    falck_group.foundedAtPlace = [milan]
    falck_group.foundationYear = 1906
    falck_group.originalName = "Società anonima Acciaierie e Ferriere Lombarde"
    falck_group.nameChangeYear = 1931
    falck_group.newName = ["Acciaiere e Ferriere Lombarde Falck"]
    falck_group.lastFurnaceClosureYear = 1995
    falck_group.declineStartYear = 1975
    falck_group.renewableEnergyTransitionYear = 1998
    falck_group.steelProductionStartYear = 1906
    falck_group.steelProductionEndYear = 1995
    falck_group.producedProducts = ["steel", "related products (processed and semi-finished)"]
    falck_group.managedByFamily = ["Falck family"]

    falck_renewables = Company("FalckRenewables")
    falck_renewables.label = "Falck Renewables"
    falck_group.hasSubsidiary = [falck_renewables]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
