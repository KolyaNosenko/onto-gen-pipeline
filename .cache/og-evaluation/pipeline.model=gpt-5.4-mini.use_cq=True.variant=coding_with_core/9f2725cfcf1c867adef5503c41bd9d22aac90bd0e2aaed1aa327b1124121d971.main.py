"""
=== TASK INPUT ===
Source text:
Falck Group is an Italian company located in Sesto San Giovanni . It was founded in 1906 and is one of the oldest companies in the steel industry . In the 1990s it turned to the production of energy from renewable sources . It was founded in 1906 in Milan by Giorgio Enrico Falck under the name Società anonima Acciaierie e Ferriere Lombarde . The first and most important industrial plants were built in Sesto San Giovanni . In 1931 the company changed its name to Acciaiere e Ferriere Lombarde Falck . The company produced steel and related products , both processed and semi - finished , for over seventy years until the crisis in the mid - seventies when the company began to decline . Its last furnaces closed in 1995 . At the end of the nineties the Falck Group , still run by the Falck family , turned to the production of renewable energy , through the subsidiary Falck Renewables .

1. Where is Falck Group located?  
2. In what year was Falck Group founded?  
3. In which city was Falck Group founded?  
4. Who founded Falck Group?  
5. What was the original name of Falck Group?  
6. What was the company’s name after the 1931 renaming?  
7. Where were the first and most important industrial plants of Falck Group built?  
8. What industry was Falck Group originally part of?  
9. What products did Falck Group produce during its steel-production period?  
10. For how many years did Falck Group produce steel and related products?  
11. When did Falck Group begin to decline?  
12. When did Falck Group’s last furnaces close?  
13. When did Falck Group turn to the production of renewable energy?  
14. Through which subsidiary did Falck Group enter the renewable energy sector?  
15. Was Falck Group still run by the Falck family when it turned to renewable energy?
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
    Abstract, PhysicalObject, SocialAgent, Society, SpaceRegion, TimeInterval,
)


with core:
    class CorporateName(Abstract):
        pass


    class Sector(Abstract):
        pass


    class Industry(Sector):
        pass


    class Company(Society):
        pass


    class Family(Society):
        pass


    class Subsidiary(Company):
        pass


    class City(SpaceRegion):
        pass


    class Person(SocialAgent):
        pass


    class IndustrialPlant(PhysicalObject):
        pass


    class Furnace(PhysicalObject):
        pass


    class Product(PhysicalObject):
        pass


    class locatedIn(ObjectProperty):
        domain = [Company, IndustrialPlant]
        range = [City]


    class foundedInTime(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimeInterval]


    class foundedInPlace(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [City]


    class foundedBy(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Person]


    class originalName(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [CorporateName]


    class renamedName(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [CorporateName]


    class renamedInTime(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimeInterval]


    class hasIndustrialPlant(ObjectProperty):
        domain = [Company]
        range = [IndustrialPlant]


    class builtIn(ObjectProperty, FunctionalProperty):
        domain = [IndustrialPlant]
        range = [City]


    class hasLastFurnaces(ObjectProperty):
        domain = [Company]
        range = [Furnace]


    class closedInTime(ObjectProperty, FunctionalProperty):
        domain = [Furnace]
        range = [TimeInterval]


    class originalIndustry(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Industry]


    class producedProduct(ObjectProperty):
        domain = [Company]
        range = [Product]


    class steelProductionDuration(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]


    class beganToDeclineInTime(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimeInterval]


    class turnedToSector(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Sector]


    class turnedToRenewableEnergyInTime(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimeInterval]


    class throughSubsidiary(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Subsidiary]


    class runBy(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Family]


    FalckGroup = Company("FalckGroup")
    FalckGroup.label = "Falck Group"

    SestoSanGiovanni = City("SestoSanGiovanni")
    SestoSanGiovanni.label = "Sesto San Giovanni"

    Milan = City("Milan")
    Milan.label = "Milan"

    GiorgioEnricoFalck = Person("GiorgioEnricoFalck")
    GiorgioEnricoFalck.label = "Giorgio Enrico Falck"

    SocietaAnonimaAcciaierieEFerriereLombarde = CorporateName(
        "SocietaAnonimaAcciaierieEFerriereLombarde"
    )
    SocietaAnonimaAcciaierieEFerriereLombarde.label = (
        "Società anonima Acciaierie e Ferriere Lombarde"
    )

    AcciaiereEFerriereLombardeFalck = CorporateName("AcciaiereEFerriereLombardeFalck")
    AcciaiereEFerriereLombardeFalck.label = "Acciaiere e Ferriere Lombarde Falck"

    FalckFamily = Family("FalckFamily")
    FalckFamily.label = "Falck family"

    FalckRenewables = Subsidiary("FalckRenewables")
    FalckRenewables.label = "Falck Renewables"

    SteelIndustry = Industry("SteelIndustry")
    SteelIndustry.label = "steel industry"

    RenewableEnergySector = Sector("RenewableEnergySector")
    RenewableEnergySector.label = "renewable energy sector"

    FirstIndustrialPlants = IndustrialPlant("FirstIndustrialPlants")
    FirstIndustrialPlants.label = "the first and most important industrial plants"

    LastFurnaces = Furnace("LastFurnaces")
    LastFurnaces.label = "its last furnaces"

    Steel = Product("Steel")
    Steel.label = "steel"

    RelatedProducts = Product("RelatedProducts")
    RelatedProducts.label = "related products, both processed and semi-finished"

    Year1906 = TimeInterval("Year1906")
    Year1906.label = "1906"

    Year1931 = TimeInterval("Year1931")
    Year1931.label = "1931"

    Year1995 = TimeInterval("Year1995")
    Year1995.label = "1995"

    The1990s = TimeInterval("The1990s")
    The1990s.label = "the 1990s"

    MidSeventies = TimeInterval("MidSeventies")
    MidSeventies.label = "the mid-seventies"

    EndOfTheNineties = TimeInterval("EndOfTheNineties")
    EndOfTheNineties.label = "the end of the nineties"

    FalckGroup.locatedIn = [SestoSanGiovanni]
    FalckGroup.foundedInTime = Year1906
    FalckGroup.foundedInPlace = Milan
    FalckGroup.foundedBy = GiorgioEnricoFalck
    FalckGroup.originalName = SocietaAnonimaAcciaierieEFerriereLombarde
    FalckGroup.renamedName = AcciaiereEFerriereLombardeFalck
    FalckGroup.renamedInTime = Year1931
    FalckGroup.hasIndustrialPlant = [FirstIndustrialPlants]
    FalckGroup.hasLastFurnaces = [LastFurnaces]
    FalckGroup.originalIndustry = SteelIndustry
    FalckGroup.producedProduct = [Steel, RelatedProducts]
    FalckGroup.steelProductionDuration = "over seventy years"
    FalckGroup.beganToDeclineInTime = MidSeventies
    FalckGroup.turnedToSector = RenewableEnergySector
    FalckGroup.turnedToRenewableEnergyInTime = EndOfTheNineties
    FalckGroup.throughSubsidiary = FalckRenewables
    FalckGroup.runBy = FalckFamily

    FirstIndustrialPlants.builtIn = SestoSanGiovanni
    LastFurnaces.closedInTime = Year1995


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
