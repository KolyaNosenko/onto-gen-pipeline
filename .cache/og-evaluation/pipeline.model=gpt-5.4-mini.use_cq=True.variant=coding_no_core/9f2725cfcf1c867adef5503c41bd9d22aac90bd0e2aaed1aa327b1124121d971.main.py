"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

1. Where is Falck Group located?
2. In which year was Falck Group founded?
3. In which city was Falck Group founded?
4. Who founded Falck Group?
5. Under what original name was Falck Group founded?
6. What is the current name of the company after the 1931 name change?
7. Where were the first and most important industrial plants built?
8. What industry is Falck Group one of the oldest companies in?
9. What products did Falck Group produce for over seventy years?
10. When did the company begin to decline?
11. In which year did Falck Group’s last furnaces close?
12. What did Falck Group turn to production of in the 1990s?
13. Through which subsidiary did Falck Group enter renewable energy production?
14. Which family was still running Falck Group at the end of the nineties?
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
    class Organization(Thing):
        pass

    class Company(Organization):
        pass

    class Subsidiary(Company):
        pass

    class Person(Thing):
        pass

    class Family(Thing):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class OrganizationName(Thing):
        pass

    class Industry(Thing):
        pass

    class Product(Thing):
        pass

    class ProductionActivity(Thing):
        pass

    class TemporalEntity(Thing):
        pass

    class TimePeriod(TemporalEntity):
        pass

    class Year(TimePeriod):
        pass

    class Duration(TemporalEntity):
        pass

    class IndustrialPlant(Thing):
        pass

    class Furnace(Thing):
        pass

    class locatedIn(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [City]

    class foundedInCity(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [City]

    class foundedInYear(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Year]

    class foundedBy(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Person]

    class hasOriginalName(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [OrganizationName]

    class hasCurrentName(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [OrganizationName]

    class nameChangedInYear(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Year]

    class builtInCity(ObjectProperty, FunctionalProperty):
        domain = [IndustrialPlant]
        range = [City]

    class inIndustry(ObjectProperty):
        domain = [Company]
        range = [Industry]

    class produced(ObjectProperty):
        domain = [Company]
        range = [Product]

    class producedForDuration(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Duration]

    class beganToDeclineDuring(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimePeriod]

    class closedInYear(ObjectProperty, FunctionalProperty):
        domain = [Furnace]
        range = [Year]

    class turnedToProductionOf(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [ProductionActivity]

    class turnedToDuring(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimePeriod]

    class throughSubsidiary(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Subsidiary]

    class runByFamily(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Family]

    class runByFamilyDuring(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimePeriod]

    FalckGroup = Company("FalckGroup")
    FalckGroup.label = "Falck Group"

    SestoSanGiovanni = City("SestoSanGiovanni")
    SestoSanGiovanni.label = "Sesto San Giovanni"

    Milan = City("Milan")
    Milan.label = "Milan"

    GiorgioEnricoFalck = Person("GiorgioEnricoFalck")
    GiorgioEnricoFalck.label = "Giorgio Enrico Falck"

    SocietaAnonimaAcciaierieEFerriereLombarde = OrganizationName(
        "SocietaAnonimaAcciaierieEFerriereLombarde"
    )
    SocietaAnonimaAcciaierieEFerriereLombarde.label = (
        "Società anonima Acciaierie e Ferriere Lombarde"
    )

    AcciaiereEFerriereLombardeFalck = OrganizationName(
        "AcciaiereEFerriereLombardeFalck"
    )
    AcciaiereEFerriereLombardeFalck.label = "Acciaiere e Ferriere Lombarde Falck"

    SteelIndustry = Industry("SteelIndustry")
    SteelIndustry.label = "the steel industry"

    SteelAndRelatedProducts = Product("SteelAndRelatedProducts")
    SteelAndRelatedProducts.label = "steel and related products , both processed and semi - finished"

    ProductionOfRenewableEnergy = ProductionActivity("ProductionOfRenewableEnergy")
    ProductionOfRenewableEnergy.label = "the production of energy from renewable sources"

    FirstAndMostImportantIndustrialPlants = IndustrialPlant(
        "FirstAndMostImportantIndustrialPlants"
    )
    FirstAndMostImportantIndustrialPlants.label = (
        "The first and most important industrial plants"
    )

    LastFurnaces = Furnace("LastFurnaces")
    LastFurnaces.label = "Its last furnaces"

    FalckFamily = Family("FalckFamily")
    FalckFamily.label = "Falck family"

    FalckRenewables = Subsidiary("FalckRenewables")
    FalckRenewables.label = "Falck Renewables"

    The1990s = TimePeriod("The1990s")
    The1990s.label = "the 1990s"

    EndOfTheNineties = TimePeriod("EndOfTheNineties")
    EndOfTheNineties.label = "the end of the nineties"

    MidSeventies = TimePeriod("MidSeventies")
    MidSeventies.label = "the mid - seventies"

    OverSeventyYears = Duration("OverSeventyYears")
    OverSeventyYears.label = "over seventy years"

    Year1906 = Year("Year1906")
    Year1906.label = "1906"

    Year1931 = Year("Year1931")
    Year1931.label = "1931"

    Year1995 = Year("Year1995")
    Year1995.label = "1995"

    FalckGroup.locatedIn = SestoSanGiovanni
    FalckGroup.foundedInYear = Year1906
    FalckGroup.foundedInCity = Milan
    FalckGroup.foundedBy = GiorgioEnricoFalck
    FalckGroup.hasOriginalName = SocietaAnonimaAcciaierieEFerriereLombarde
    FalckGroup.hasCurrentName = AcciaiereEFerriereLombardeFalck
    FalckGroup.nameChangedInYear = Year1931
    FalckGroup.inIndustry = [SteelIndustry]
    FalckGroup.produced = [SteelAndRelatedProducts]
    FalckGroup.producedForDuration = OverSeventyYears
    FalckGroup.beganToDeclineDuring = MidSeventies
    LastFurnaces.closedInYear = Year1995
    FalckGroup.turnedToProductionOf = ProductionOfRenewableEnergy
    FalckGroup.turnedToDuring = The1990s
    FalckGroup.throughSubsidiary = FalckRenewables
    FalckGroup.runByFamily = FalckFamily
    FalckGroup.runByFamilyDuring = EndOfTheNineties
    FirstAndMostImportantIndustrialPlants.builtInCity = SestoSanGiovanni


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
