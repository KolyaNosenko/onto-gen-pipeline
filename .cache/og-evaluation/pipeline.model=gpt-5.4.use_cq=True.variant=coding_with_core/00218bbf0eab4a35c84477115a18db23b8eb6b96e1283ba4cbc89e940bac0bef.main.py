"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

What is the name of the company described in the document?
Where is Falck Group located?
In which city is Falck Group located?
In which country is Falck Group located?
When was Falck Group founded?
Who founded Falck Group?
In which city was Falck Group founded?
What was the original name of Falck Group at the time of its foundation?
What name did the company adopt in 1931?
When did the company change its name to Acciaiere e Ferriere Lombarde Falck?
What industry was Falck Group originally part of?
Is Falck Group one of the oldest companies in the steel industry?
What products did Falck Group produce during its steel industry period?
Did Falck Group produce both processed and semi-finished steel products?
For how many years did Falck Group produce steel and related products?
Where were the first and most important industrial plants of the company built?
When did Falck Group begin to decline?
What event caused the decline of Falck Group in the mid-seventies?
When did the last furnaces of Falck Group close?
In which decade did Falck Group shift from steel production to renewable energy production?
To what type of production did Falck Group turn in the 1990s?
Through which subsidiary did Falck Group enter the renewable energy sector?
Is Falck Renewables a subsidiary of Falck Group?
Who was running Falck Group when it turned to renewable energy production?
Is Falck Group still run by the Falck family at the end of the nineties?
What is the relationship between Falck Group and Falck Renewables?
What historical names has Falck Group had over time?
What are the major historical phases in the evolution of Falck Group’s business activities?
What is the timeline of key events in the history of Falck Group?
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
    Event,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class Person(AgentivePhysicalObject):
        pass


    class Family(Society):
        pass


    class Company(Society):
        pass


    class SubsidiaryCompany(Company):
        pass


    class City(SpaceRegion):
        pass


    class Country(SpaceRegion):
        pass


    class Industry(NonAgentiveSocialObject):
        pass


    class CorporateName(NonAgentiveSocialObject):
        pass


    class BusinessActivityType(NonAgentiveSocialObject):
        pass


    class RenewableEnergyProductionType(BusinessActivityType):
        pass


    class Product(NonAgentivePhysicalObject):
        pass


    class SteelProduct(Product):
        pass


    class RelatedProduct(Product):
        pass


    class IndustrialPlant(NonAgentivePhysicalObject):
        pass


    class Furnace(NonAgentivePhysicalObject):
        pass


    class CorporateEvent(Event):
        pass


    class FoundationEvent(CorporateEvent):
        pass


    class NameChangeEvent(CorporateEvent):
        pass


    class DeclineEvent(CorporateEvent):
        pass


    class TransitionEvent(CorporateEvent):
        pass


    class FurnaceClosureEvent(CorporateEvent):
        pass


    class EconomicCrisis(CorporateEvent):
        pass


    class headquartersInCity(ObjectProperty):
        domain = [Company]
        range = [City]


    class locatedInCountry(ObjectProperty):
        domain = [Company, City]
        range = [Country]


    class hasHistoricalName(ObjectProperty):
        domain = [Company]
        range = [CorporateName]


    class originalName(ObjectProperty):
        domain = [Company]
        range = [CorporateName]


    class changedNameTo(ObjectProperty):
        domain = [Company, NameChangeEvent]
        range = [CorporateName]


    class changedNameIn(ObjectProperty):
        domain = [Company, NameChangeEvent]
        range = [TimeInterval]


    class foundedBy(ObjectProperty):
        domain = [Company, FoundationEvent]
        range = [Person]


    class foundedInCity(ObjectProperty):
        domain = [Company, FoundationEvent]
        range = [City]


    class foundedInTime(ObjectProperty):
        domain = [Company, FoundationEvent]
        range = [TimeInterval]


    class operatesInIndustry(ObjectProperty):
        domain = [Company]
        range = [Industry]


    class oneOfOldestCompaniesIn(ObjectProperty):
        domain = [Company]
        range = [Industry]


    class producedProduct(ObjectProperty):
        domain = [Company]
        range = [Product]


    class producedFor(ObjectProperty):
        domain = [Company]
        range = [TimeInterval]


    class hasIndustrialPlant(ObjectProperty):
        domain = [Company]
        range = [IndustrialPlant]


    class builtInCity(ObjectProperty):
        domain = [IndustrialPlant]
        range = [City]


    class hasLastFurnaces(ObjectProperty):
        domain = [Company]
        range = [Furnace]


    class closedInTime(ObjectProperty):
        domain = [Furnace, FurnaceClosureEvent]
        range = [TimeInterval]


    class turnedToProductionOf(ObjectProperty):
        domain = [Company, TransitionEvent]
        range = [BusinessActivityType]


    class turnedToProductionIn(ObjectProperty):
        domain = [Company, TransitionEvent]
        range = [TimeInterval]


    class runBy(ObjectProperty):
        domain = [Company, TransitionEvent]
        range = [Family]


    class throughSubsidiary(ObjectProperty):
        domain = [Company, TransitionEvent]
        range = [SubsidiaryCompany]


    class subsidiaryOf(ObjectProperty):
        domain = [SubsidiaryCompany]
        range = [Company]


    class declineCausedBy(ObjectProperty):
        domain = [Company, DeclineEvent]
        range = [EconomicCrisis]


    class beganDeclineIn(ObjectProperty):
        domain = [Company, DeclineEvent]
        range = [TimeInterval]


    class hasKeyEvent(ObjectProperty):
        domain = [Company]
        range = [CorporateEvent]


    class aboutCompany(ObjectProperty):
        domain = [CorporateEvent]
        range = [Company]


    class eventUsesName(ObjectProperty):
        domain = [FoundationEvent, NameChangeEvent]
        range = [CorporateName]


    class aboutFurnace(ObjectProperty):
        domain = [FurnaceClosureEvent]
        range = [Furnace]


    class isOneOfOldestCompanies(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [bool]


    class producedProcessedProducts(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [bool]


    class producedSemiFinishedProducts(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [bool]


    FalckGroup = Company("FalckGroupCompany")
    FalckGroup.label = "Falck Group"

    ItalianCountry = Country("ItalianCountry")
    ItalianCountry.label = "Italian"

    SestoSanGiovanni = City("SestoSanGiovanniCity")
    SestoSanGiovanni.label = "Sesto San Giovanni"

    Milan = City("MilanCity")
    Milan.label = "Milan"

    GiorgioEnricoFalck = Person("GiorgioEnricoFalckPerson")
    GiorgioEnricoFalck.label = "Giorgio Enrico Falck"

    SocietaAnonimaAcciaierieEFerriereLombarde = CorporateName(
        "SocietaAnonimaAcciaierieEFerriereLombardeName"
    )
    SocietaAnonimaAcciaierieEFerriereLombarde.label = (
        "Società anonima Acciaierie e Ferriere Lombarde"
    )

    AcciaiereEFerriereLombardeFalck = CorporateName(
        "AcciaiereEFerriereLombardeFalckName"
    )
    AcciaiereEFerriereLombardeFalck.label = "Acciaiere e Ferriere Lombarde Falck"

    SteelIndustry = Industry("SteelIndustry")
    SteelIndustry.label = "steel industry"

    Steel = SteelProduct("SteelProductInstance")
    Steel.label = "steel"

    RelatedProducts = RelatedProduct("RelatedProducts")
    RelatedProducts.label = "related products"

    OverSeventyYears = TimeInterval("OverSeventyYears")
    OverSeventyYears.label = "over seventy years"

    FirstAndMostImportantIndustrialPlants = IndustrialPlant(
        "FirstAndMostImportantIndustrialPlants"
    )
    FirstAndMostImportantIndustrialPlants.label = (
        "The first and most important industrial plants"
    )

    MidSeventiesCrisis = EconomicCrisis("MidSeventiesCrisis")
    MidSeventiesCrisis.label = "the crisis in the mid - seventies"

    LastFurnaces = Furnace("LastFurnaces")
    LastFurnaces.label = "last furnaces"

    FalckFamily = Family("FalckFamily")
    FalckFamily.label = "Falck family"

    FalckRenewables = SubsidiaryCompany("FalckRenewablesCompany")
    FalckRenewables.label = "Falck Renewables"

    Year1906 = TimeInterval("Year1906")
    Year1906.label = "1906"

    Year1931 = TimeInterval("Year1931")
    Year1931.label = "1931"

    Year1995 = TimeInterval("Year1995")
    Year1995.label = "1995"

    The1990s = TimeInterval("The1990s")
    The1990s.label = "the 1990s"

    EndOfTheNineties = TimeInterval("EndOfTheNineties")
    EndOfTheNineties.label = "the end of the nineties"

    MidSeventies = TimeInterval("MidSeventies")
    MidSeventies.label = "the mid - seventies"

    EnergyFromRenewableSourcesProduction = RenewableEnergyProductionType(
        "EnergyFromRenewableSourcesProduction"
    )
    EnergyFromRenewableSourcesProduction.label = (
        "the production of energy from renewable sources"
    )

    RenewableEnergyProduction = RenewableEnergyProductionType(
        "RenewableEnergyProduction"
    )
    RenewableEnergyProduction.label = "the production of renewable energy"

    Foundation1906 = FoundationEvent("Foundation1906")
    Foundation1906.label = (
        "founded in 1906 in Milan by Giorgio Enrico Falck under the name "
        "Società anonima Acciaierie e Ferriere Lombarde"
    )

    NameChange1931 = NameChangeEvent("NameChange1931")
    NameChange1931.label = "changed its name to Acciaiere e Ferriere Lombarde Falck"

    DeclineMidSeventies = DeclineEvent("DeclineMidSeventies")
    DeclineMidSeventies.label = "began to decline"

    TransitionInThe1990s = TransitionEvent("TransitionInThe1990s")
    TransitionInThe1990s.label = "turned to the production of energy from renewable sources"

    TransitionAtEndOfTheNineties = TransitionEvent("TransitionAtEndOfTheNineties")
    TransitionAtEndOfTheNineties.label = "turned to the production of renewable energy"

    Closure1995 = FurnaceClosureEvent("Closure1995")
    Closure1995.label = "last furnaces closed in 1995"

    FalckGroup.headquartersInCity.append(SestoSanGiovanni)
    FalckGroup.locatedInCountry.append(ItalianCountry)
    FalckGroup.foundedBy.append(GiorgioEnricoFalck)
    FalckGroup.foundedInCity.append(Milan)
    FalckGroup.foundedInTime.append(Year1906)
    FalckGroup.originalName.append(SocietaAnonimaAcciaierieEFerriereLombarde)
    FalckGroup.changedNameTo.append(AcciaiereEFerriereLombardeFalck)
    FalckGroup.changedNameIn.append(Year1931)
    FalckGroup.hasHistoricalName.append(SocietaAnonimaAcciaierieEFerriereLombarde)
    FalckGroup.hasHistoricalName.append(AcciaiereEFerriereLombardeFalck)
    FalckGroup.operatesInIndustry.append(SteelIndustry)
    FalckGroup.oneOfOldestCompaniesIn.append(SteelIndustry)
    FalckGroup.isOneOfOldestCompanies = True
    FalckGroup.producedProduct.append(Steel)
    FalckGroup.producedProduct.append(RelatedProducts)
    FalckGroup.producedFor.append(OverSeventyYears)
    FalckGroup.producedProcessedProducts = True
    FalckGroup.producedSemiFinishedProducts = True
    FalckGroup.hasIndustrialPlant.append(FirstAndMostImportantIndustrialPlants)
    FalckGroup.hasLastFurnaces.append(LastFurnaces)
    FalckGroup.beganDeclineIn.append(MidSeventies)
    FalckGroup.declineCausedBy.append(MidSeventiesCrisis)
    FalckGroup.turnedToProductionOf.append(EnergyFromRenewableSourcesProduction)
    FalckGroup.turnedToProductionOf.append(RenewableEnergyProduction)
    FalckGroup.turnedToProductionIn.append(The1990s)
    FalckGroup.turnedToProductionIn.append(EndOfTheNineties)
    FalckGroup.runBy.append(FalckFamily)
    FalckGroup.throughSubsidiary.append(FalckRenewables)

    SestoSanGiovanni.locatedInCountry.append(ItalianCountry)
    FirstAndMostImportantIndustrialPlants.builtInCity.append(SestoSanGiovanni)
    LastFurnaces.closedInTime.append(Year1995)
    FalckRenewables.subsidiaryOf.append(FalckGroup)

    Foundation1906.aboutCompany.append(FalckGroup)
    Foundation1906.foundedBy.append(GiorgioEnricoFalck)
    Foundation1906.foundedInCity.append(Milan)
    Foundation1906.foundedInTime.append(Year1906)
    Foundation1906.eventUsesName.append(SocietaAnonimaAcciaierieEFerriereLombarde)
    Foundation1906.temporallyLocatedAt = Year1906

    NameChange1931.aboutCompany.append(FalckGroup)
    NameChange1931.eventUsesName.append(AcciaiereEFerriereLombardeFalck)
    NameChange1931.changedNameTo.append(AcciaiereEFerriereLombardeFalck)
    NameChange1931.changedNameIn.append(Year1931)
    NameChange1931.temporallyLocatedAt = Year1931

    DeclineMidSeventies.aboutCompany.append(FalckGroup)
    DeclineMidSeventies.declineCausedBy.append(MidSeventiesCrisis)
    DeclineMidSeventies.beganDeclineIn.append(MidSeventies)
    DeclineMidSeventies.temporallyLocatedAt = MidSeventies

    TransitionInThe1990s.aboutCompany.append(FalckGroup)
    TransitionInThe1990s.turnedToProductionOf.append(EnergyFromRenewableSourcesProduction)
    TransitionInThe1990s.turnedToProductionIn.append(The1990s)
    TransitionInThe1990s.temporallyLocatedAt = The1990s

    TransitionAtEndOfTheNineties.aboutCompany.append(FalckGroup)
    TransitionAtEndOfTheNineties.turnedToProductionOf.append(RenewableEnergyProduction)
    TransitionAtEndOfTheNineties.turnedToProductionIn.append(EndOfTheNineties)
    TransitionAtEndOfTheNineties.runBy.append(FalckFamily)
    TransitionAtEndOfTheNineties.throughSubsidiary.append(FalckRenewables)
    TransitionAtEndOfTheNineties.temporallyLocatedAt = EndOfTheNineties

    Closure1995.aboutCompany.append(FalckGroup)
    Closure1995.aboutFurnace.append(LastFurnaces)
    Closure1995.closedInTime.append(Year1995)
    Closure1995.temporallyLocatedAt = Year1995

    FalckGroup.hasKeyEvent.append(Foundation1906)
    FalckGroup.hasKeyEvent.append(NameChange1931)
    FalckGroup.hasKeyEvent.append(DeclineMidSeventies)
    FalckGroup.hasKeyEvent.append(TransitionInThe1990s)
    FalckGroup.hasKeyEvent.append(TransitionAtEndOfTheNineties)
    FalckGroup.hasKeyEvent.append(Closure1995)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
