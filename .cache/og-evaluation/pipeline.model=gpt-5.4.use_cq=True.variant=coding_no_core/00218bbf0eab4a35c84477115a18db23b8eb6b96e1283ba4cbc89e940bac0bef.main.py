"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

What is the name of the company described in the document?
Where is Falck Group located?
In which city was Falck Group founded?
In what year was Falck Group founded?
Who founded Falck Group?
What was the original name of Falck Group at the time of its foundation?
What name did the company adopt in 1931?
What industry was Falck Group originally associated with?
Is Falck Group one of the oldest companies in the steel industry?
What were the first and most important industrial plants of the company?
Where were the first and most important industrial plants built?
What products did Falck Group produce during its steel industry period?
For how long did Falck Group produce steel and related products?
When did the company begin to decline?
What event caused or coincided with the decline of the company in the mid-seventies?
When did Falck Group close its last furnaces?
When did Falck Group shift from steel production to renewable energy production?
To which type of energy production did Falck Group turn in the 1990s?
Through which subsidiary did Falck Group enter the renewable energy sector?
Is Falck Group still run by the Falck family?
What is the relationship between Falck Group and Falck Renewables?
What historical sequence of names did Falck Group have over time?
What is the relationship between the company’s founding location and the location of its main industrial plants?
What major industrial transformation did Falck Group undergo between its foundation and the end of the 1990s?
Which family is associated with the long-term management of Falck Group?
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

    class Family(Thing):
        pass

    class Person(Thing):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class Nationality(Thing):
        pass

    class IndustrySector(Thing):
        pass

    class Facility(Thing):
        pass

    class IndustrialPlantGroup(Facility):
        pass

    class ProductGroup(Thing):
        pass

    class EnergySource(Thing):
        pass

    class ProductionActivity(Thing):
        pass

    class Event(Thing):
        pass

    class Crisis(Event):
        pass

    class Name(Thing):
        pass

    class CompanyName(Name):
        pass

    class TemporalEntity(Thing):
        pass

    class TimePeriod(TemporalEntity):
        pass

    class Year(TimePeriod):
        pass

    class Decade(TimePeriod):
        pass

    class RelativeTimePeriod(TimePeriod):
        pass

    class Duration(TemporalEntity):
        pass

    class hasNationality(ObjectProperty):
        domain = [Organization]
        range = [Nationality]

    class locatedIn(ObjectProperty):
        domain = [Organization]
        range = [Place]

    class foundedInPlace(ObjectProperty):
        domain = [Company]
        range = [City]

    class foundedInTime(ObjectProperty):
        domain = [Company]
        range = [TimePeriod]

    class foundedBy(ObjectProperty):
        domain = [Company]
        range = [Person]

    class foundedUnderName(ObjectProperty):
        domain = [Company]
        range = [CompanyName]

    class hadCompanyName(ObjectProperty):
        domain = [Company]
        range = [CompanyName]

    class adoptedName(ObjectProperty):
        domain = [Company]
        range = [CompanyName]

    class renamedInTime(ObjectProperty):
        domain = [Company]
        range = [TimePeriod]

    class nameSucceededBy(ObjectProperty):
        domain = [CompanyName]
        range = [CompanyName]

    class associatedWithIndustry(ObjectProperty):
        domain = [Company]
        range = [IndustrySector]

    class hasMainIndustrialPlants(ObjectProperty):
        domain = [Company]
        range = [IndustrialPlantGroup]

    class builtIn(ObjectProperty):
        domain = [IndustrialPlantGroup]
        range = [Place]

    class producedProductGroup(ObjectProperty):
        domain = [Company]
        range = [ProductGroup]

    class producedForDuration(ObjectProperty):
        domain = [Company]
        range = [Duration]

    class beganToDeclineIn(ObjectProperty):
        domain = [Company]
        range = [TimePeriod]

    class declinedBecauseOf(ObjectProperty):
        domain = [Company]
        range = [Crisis]

    class occurredInTime(ObjectProperty):
        domain = [Event]
        range = [TimePeriod]

    class lastFurnacesClosedIn(ObjectProperty):
        domain = [Company]
        range = [TimePeriod]

    class turnedToProductionActivity(ObjectProperty):
        domain = [Company]
        range = [ProductionActivity]

    class usedEnergySource(ObjectProperty):
        domain = [ProductionActivity]
        range = [EnergySource]

    class turnedToInTime(ObjectProperty):
        domain = [Company]
        range = [TimePeriod]

    class hasSubsidiary(ObjectProperty):
        domain = [Company]
        range = [Subsidiary]

    class subsidiaryOf(ObjectProperty):
        domain = [Subsidiary]
        range = [Company]

    class enteredRenewableEnergyThrough(ObjectProperty):
        domain = [Company]
        range = [Subsidiary]

    class runBy(ObjectProperty):
        domain = [Company]
        range = [Family]

    class isOneOfOldestCompaniesInIndustry(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [bool]

    class productFormDescription(DataProperty, FunctionalProperty):
        domain = [ProductGroup]
        range = [str]

    class industrialTransformationDescription(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]

    FalckGroup = Company("FalckGroup")
    FalckGroup.label = "Falck Group"

    Italian = Nationality("Italian")
    Italian.label = "Italian"

    SestoSanGiovanni = City("SestoSanGiovanni")
    SestoSanGiovanni.label = "Sesto San Giovanni"

    Milan = City("Milan")
    Milan.label = "Milan"

    GiorgioEnricoFalck = Person("GiorgioEnricoFalck")
    GiorgioEnricoFalck.label = "Giorgio Enrico Falck"

    SocietaAnonimaAcciaierieEFerriereLombarde = CompanyName("SocietaAnonimaAcciaierieEFerriereLombarde")
    SocietaAnonimaAcciaierieEFerriereLombarde.label = "Società anonima Acciaierie e Ferriere Lombarde"

    AcciaiereEFerriereLombardeFalck = CompanyName("AcciaiereEFerriereLombardeFalck")
    AcciaiereEFerriereLombardeFalck.label = "Acciaiere e Ferriere Lombarde Falck"

    SteelIndustry = IndustrySector("TheSteelIndustry")
    SteelIndustry.label = "the steel industry"

    FirstAndMostImportantIndustrialPlants = IndustrialPlantGroup("FirstAndMostImportantIndustrialPlants")
    FirstAndMostImportantIndustrialPlants.label = "the first and most important industrial plants"

    SteelAndRelatedProducts = ProductGroup("SteelAndRelatedProducts")
    SteelAndRelatedProducts.label = "steel and related products"

    RenewableSources = EnergySource("RenewableSources")
    RenewableSources.label = "renewable sources"

    ProductionOfEnergyFromRenewableSources = ProductionActivity("ProductionOfEnergyFromRenewableSources")
    ProductionOfEnergyFromRenewableSources.label = "the production of energy from renewable sources"

    Year1906 = Year("Year1906")
    Year1906.label = "1906"

    Year1931 = Year("Year1931")
    Year1931.label = "1931"

    Year1995 = Year("Year1995")
    Year1995.label = "1995"

    The1990s = Decade("The1990s")
    The1990s.label = "the 1990s"

    MidSeventies = RelativeTimePeriod("MidSeventies")
    MidSeventies.label = "the mid - seventies"

    TheEndOfTheNineties = RelativeTimePeriod("TheEndOfTheNineties")
    TheEndOfTheNineties.label = "the end of the nineties"

    OverSeventyYears = Duration("OverSeventyYears")
    OverSeventyYears.label = "over seventy years"

    CrisisInTheMidSeventies = Crisis("CrisisInTheMidSeventies")
    CrisisInTheMidSeventies.label = "the crisis in the mid - seventies"

    FalckRenewables = Subsidiary("FalckRenewables")
    FalckRenewables.label = "Falck Renewables"

    FalckFamily = Family("FalckFamily")
    FalckFamily.label = "Falck family"

    FalckGroup.hasNationality = [Italian]
    FalckGroup.locatedIn = [SestoSanGiovanni]
    FalckGroup.foundedInPlace = [Milan]
    FalckGroup.foundedInTime = [Year1906]
    FalckGroup.foundedBy = [GiorgioEnricoFalck]
    FalckGroup.foundedUnderName = [SocietaAnonimaAcciaierieEFerriereLombarde]
    FalckGroup.hadCompanyName = [SocietaAnonimaAcciaierieEFerriereLombarde, AcciaiereEFerriereLombardeFalck]
    FalckGroup.adoptedName = [AcciaiereEFerriereLombardeFalck]
    FalckGroup.renamedInTime = [Year1931]
    FalckGroup.associatedWithIndustry = [SteelIndustry]
    FalckGroup.isOneOfOldestCompaniesInIndustry = True
    FalckGroup.hasMainIndustrialPlants = [FirstAndMostImportantIndustrialPlants]
    FalckGroup.producedProductGroup = [SteelAndRelatedProducts]
    FalckGroup.producedForDuration = [OverSeventyYears]
    FalckGroup.beganToDeclineIn = [MidSeventies]
    FalckGroup.declinedBecauseOf = [CrisisInTheMidSeventies]
    FalckGroup.lastFurnacesClosedIn = [Year1995]
    FalckGroup.turnedToProductionActivity = [ProductionOfEnergyFromRenewableSources]
    FalckGroup.turnedToInTime = [The1990s, TheEndOfTheNineties]
    FalckGroup.hasSubsidiary = [FalckRenewables]
    FalckGroup.enteredRenewableEnergyThrough = [FalckRenewables]
    FalckGroup.runBy = [FalckFamily]
    FalckGroup.industrialTransformationDescription = "from steel and related products to the production of energy from renewable sources"

    SocietaAnonimaAcciaierieEFerriereLombarde.nameSucceededBy = [AcciaiereEFerriereLombardeFalck]

    FirstAndMostImportantIndustrialPlants.builtIn = [SestoSanGiovanni]

    SteelAndRelatedProducts.productFormDescription = "both processed and semi - finished"

    ProductionOfEnergyFromRenewableSources.usedEnergySource = [RenewableSources]

    CrisisInTheMidSeventies.occurredInTime = [MidSeventies]

    FalckRenewables.subsidiaryOf = [FalckGroup]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
