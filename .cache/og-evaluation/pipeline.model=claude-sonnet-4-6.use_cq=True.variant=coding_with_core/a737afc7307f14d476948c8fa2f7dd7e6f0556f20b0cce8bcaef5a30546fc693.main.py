"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

Here are the competency questions derived from the document:

1. Where is Falck Group located?
2. What country is Falck Group based in?
3. When was Falck Group founded?
4. What industry was Falck Group originally part of?
5. Who founded Falck Group?
6. What was the original name of Falck Group?
7. Where were the first industrial plants of Falck Group built?
8. When did Falck Group change its name to Acciaiere e Ferriere Lombarde Falck?
9. What products did Falck Group produce during its steel era?
10. How long did Falck Group produce steel and related products?
11. When did the crisis begin that caused Falck Group to decline?
12. When did Falck Group close its last furnaces?
13. What sector did Falck Group transition to in the 1990s?
14. Which family has been running Falck Group?
15. What is the name of the subsidiary through which Falck Group produces renewable energy?
16. When did Falck Group turn to the production of renewable energy?
17. In which city was Falck Group originally founded?
18. What type of energy does Falck Renewables produce?
19. What is the relationship between Falck Group and Falck Renewables?
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
    Society,
    AgentivePhysicalObject,
    SpaceRegion,
    NonAgentiveSocialObject,
    TimeInterval,
)


with core:
    # ------------------------------------------------------------------ #
    # Entity classes                                                       #
    # ------------------------------------------------------------------ #

    class Company(Society):
        """A commercial organisation (e.g. an industrial group)."""

    class Subsidiary(Company):
        """A company that is a subsidiary of another Company."""

    class Person(AgentivePhysicalObject):
        """A human individual."""

    class City(SpaceRegion):
        """A city as a geographic spatial region."""

    class Country(SpaceRegion):
        """A sovereign state as a geographic spatial region."""

    class Family(Society):
        """A family regarded as a collective social agent."""

    class IndustrySector(NonAgentiveSocialObject):
        """A recognised branch of economic activity (e.g. steel industry)."""

    # ------------------------------------------------------------------ #
    # Properties                                                           #
    # ------------------------------------------------------------------ #

    class locatedIn(ObjectProperty, FunctionalProperty):
        """Headquarters / main location of a Company."""
        domain = [Company]
        range  = [City]

    class basedInCountry(ObjectProperty, FunctionalProperty):
        """Country in which a Company is based."""
        domain = [Company]
        range  = [Country]

    class foundedInYear(ObjectProperty, FunctionalProperty):
        """Year in which a Company was established."""
        domain = [Company]
        range  = [TimeInterval]

    class foundedInCity(ObjectProperty, FunctionalProperty):
        """City in which a Company was originally founded."""
        domain = [Company]
        range  = [City]

    class foundedBy(ObjectProperty):
        """Person(s) who founded a Company."""
        domain = [Company]
        range  = [Person]

    class originalName(DataProperty, FunctionalProperty):
        """The name under which a Company was originally incorporated."""
        domain = [Company]
        range  = [str]

    class nameChangedTo(DataProperty, FunctionalProperty):
        """The new name adopted when a Company formally changed its name."""
        domain = [Company]
        range  = [str]

    class nameChangedIn(ObjectProperty, FunctionalProperty):
        """Year in which a Company changed its official name."""
        domain = [Company]
        range  = [TimeInterval]

    class operatesInSector(ObjectProperty):
        """Sector(s) in which a Company operates (past or present)."""
        domain = [Company]
        range  = [IndustrySector]

    class transitionedToSector(ObjectProperty, FunctionalProperty):
        """The sector a Company transitioned its main activity to."""
        domain = [Company]
        range  = [IndustrySector]

    class transitionedToSectorIn(ObjectProperty, FunctionalProperty):
        """Time interval during which a Company transitioned to a new sector."""
        domain = [Company]
        range  = [TimeInterval]

    class firstPlantsBuiltIn(ObjectProperty, FunctionalProperty):
        """City where a Company built its first and most important industrial plants."""
        domain = [Company]
        range  = [City]

    class producedProductType(DataProperty):
        """Type(s) of product a Company produced (as plain text descriptions)."""
        domain = [Company]
        range  = [str]

    class steelProductionDuration(DataProperty, FunctionalProperty):
        """How long a Company was active in steel production."""
        domain = [Company]
        range  = [str]

    class crisisStartedIn(ObjectProperty, FunctionalProperty):
        """Time interval when the crisis that caused a Company to decline began."""
        domain = [Company]
        range  = [TimeInterval]

    class lastFurnacesClosedIn(ObjectProperty, FunctionalProperty):
        """Year when a Company closed its last furnaces."""
        domain = [Company]
        range  = [TimeInterval]

    class runBy(ObjectProperty):
        """Family or collective entity that runs / controls a Company."""
        domain = [Company]
        range  = [Family]

    class hasSubsidiary(ObjectProperty):
        """Subsidiary company(-ies) belonging to a parent Company."""
        domain = [Company]
        range  = [Company]

    class producesEnergyType(DataProperty, FunctionalProperty):
        """Type of energy produced by a Company (e.g. 'renewable')."""
        domain = [Company]
        range  = [str]

    # ------------------------------------------------------------------ #
    # Named instances                                                      #
    # ------------------------------------------------------------------ #

    # --- Cities ---
    sesto_san_giovanni = City("SestoSanGiovanni")
    sesto_san_giovanni.label = "Sesto San Giovanni"

    milan = City("Milan")
    milan.label = "Milan"

    # --- Country ---
    italy = Country("Italy")
    italy.label = "Italy"

    # --- Industry sectors ---
    steel_industry = IndustrySector("SteelIndustry")
    steel_industry.label = "steel industry"

    renewable_energy_sector = IndustrySector("RenewableEnergySector")
    renewable_energy_sector.label = "renewable energy"

    # --- Person ---
    giorgio_enrico_falck = Person("GiorgioEnricoFalck")
    giorgio_enrico_falck.label = "Giorgio Enrico Falck"

    # --- Family ---
    falck_family = Family("FalckFamily")
    falck_family.label = "Falck family"

    # --- Time intervals ---
    year_1906 = TimeInterval("Year1906")
    year_1906.label = "1906"

    year_1931 = TimeInterval("Year1931")
    year_1931.label = "1931"

    year_1995 = TimeInterval("Year1995")
    year_1995.label = "1995"

    mid_seventies = TimeInterval("TheMidSeventies")
    mid_seventies.label = "mid-seventies"

    the_nineties = TimeInterval("TheNineties")
    the_nineties.label = "1990s"

    # --- Companies ---
    falck_renewables = Subsidiary("FalckRenewables")
    falck_renewables.label = "Falck Renewables"
    falck_renewables.producesEnergyType = "renewable"

    falck_group = Company("FalckGroup")
    falck_group.label = "Falck Group"
    falck_group.locatedIn            = sesto_san_giovanni
    falck_group.basedInCountry       = italy
    falck_group.foundedInYear        = year_1906
    falck_group.foundedInCity        = milan
    falck_group.foundedBy            = [giorgio_enrico_falck]
    falck_group.originalName         = "Società anonima Acciaierie e Ferriere Lombarde"
    falck_group.nameChangedTo        = "Acciaiere e Ferriere Lombarde Falck"
    falck_group.nameChangedIn        = year_1931
    falck_group.operatesInSector     = [steel_industry, renewable_energy_sector]
    falck_group.transitionedToSector = renewable_energy_sector
    falck_group.transitionedToSectorIn = the_nineties
    falck_group.firstPlantsBuiltIn   = sesto_san_giovanni
    falck_group.producedProductType  = ["steel", "related products"]
    falck_group.steelProductionDuration = "over seventy years"
    falck_group.crisisStartedIn      = mid_seventies
    falck_group.lastFurnacesClosedIn = year_1995
    falck_group.runBy                = [falck_family]
    falck_group.hasSubsidiary        = [falck_renewables]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
