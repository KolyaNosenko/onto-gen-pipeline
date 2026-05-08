"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What is Yellowtail Dam?
2. Where is Yellowtail Dam located?
3. Across which river is Yellowtail Dam built?
4. In which state and region is Yellowtail Dam situated?
5. What type of dam is Yellowtail Dam?
6. During which era was Yellowtail Dam constructed?
7. What are the primary purposes of Yellowtail Dam?
8. Does Yellowtail Dam regulate the flow of the Bighorn River for irrigation?
9. Does Yellowtail Dam generate hydroelectric power?
10. What reservoir is associated with Yellowtail Dam?
11. Who owns Yellowtail Dam?
12. Who owns Bighorn Lake?
13. Which government agency owns the dam and its reservoir?
14. What parties were involved in the negotiations that led to the project?
15. What role did the federal government play in the creation of Yellowtail Dam?
16. What role did the Crow Nation play in the project?
17. On what reservation did the surrounding tribe live?
18. Was Yellowtail Dam originally envisioned as a shared facility?
19. What benefits was the shared facility expected to provide to both sides?
20. Was the land for the project eventually sold to the U.S. Bureau of Reclamation?
21. Does part of the reservoir lie within the Crow Indian Reservation?
22. Does Bighorn Lake extend upstream into Wyoming?
23. In which states does the reservoir associated with Yellowtail Dam extend?
24. When was Yellowtail Dam authorized?
25. When did groundbreaking for Yellowtail Dam occur?
26. When was Yellowtail Dam completed?
27. How many years did the construction of Yellowtail Dam take?
28. What recreational uses does Yellowtail Dam support today?
29. Does recreation occur both above and below the dam?
30. How has regulation by Yellowtail Dam affected the lower Bighorn River?
31. Has Yellowtail Dam contributed to making the lower Bighorn River a premier trout stream in Montana?
32. What controversies are associated with Yellowtail Dam?
33. Is there controversy over water allocation in Bighorn Lake between Montana and Wyoming?
34. What ecological damage has been caused by Yellowtail Dam?
35. Has the river above the dam experienced ecological damage?
36. Has the river below the dam experienced ecological damage?
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
    class Place(Thing):
        pass

    class PoliticalEntity(Thing):
        pass

    class Country(Place, PoliticalEntity):
        pass

    class State(Place, PoliticalEntity):
        pass

    class Region(Place):
        pass

    class Reservation(Place):
        pass

    class RelativeLocation(Place):
        pass

    class WaterBody(Place):
        pass

    class River(WaterBody):
        pass

    class RiverSection(River):
        pass

    class TroutStream(RiverSection):
        pass

    class PremierTroutStream(TroutStream):
        pass

    class Reservoir(WaterBody):
        pass

    class Organization(Thing):
        pass

    class Government(Organization, PoliticalEntity):
        pass

    class GovernmentAgency(Organization):
        pass

    class IndigenousNation(PoliticalEntity):
        pass

    class NativeAmericanTribe(IndigenousNation):
        pass

    class Facility(Thing):
        pass

    class Dam(Facility):
        pass

    class ConcreteArchDam(Dam):
        pass

    class Purpose(Thing):
        pass

    class IrrigationPurpose(Purpose):
        pass

    class HydroelectricPowerGenerationPurpose(Purpose):
        pass

    class RecreationPurpose(Purpose):
        pass

    class TimeEntity(Thing):
        pass

    class Era(TimeEntity):
        pass

    class Year(TimeEntity):
        pass

    class Duration(TimeEntity):
        pass

    class Issue(Thing):
        pass

    class Controversy(Issue):
        pass

    class WaterAllocationControversy(Controversy):
        pass

    class EcologicalDamage(Issue):
        pass

    class locatedIn(ObjectProperty):
        domain = [Thing]
        range = [Place]

    class acrossRiver(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [River]

    class regulatesFlowOf(ObjectProperty):
        domain = [Dam]
        range = [River]

    class hasReservoir(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Reservoir]

    class ownedBy(ObjectProperty):
        domain = [Thing]
        range = [Organization]

    class hasPurpose(ObjectProperty):
        domain = [Dam]
        range = [Purpose]

    class resultedFromNegotiationsWithParty(ObjectProperty):
        domain = [Dam]
        range = [PoliticalEntity]

    class expectedProfitBeneficiary(ObjectProperty):
        domain = [Dam]
        range = [PoliticalEntity]

    class livedOn(ObjectProperty):
        domain = [IndigenousNation]
        range = [Reservation]

    class landSoldTo(ObjectProperty):
        domain = [Dam]
        range = [Organization]

    class partiallyLiesIn(ObjectProperty):
        domain = [Reservoir]
        range = [Place]

    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [Place]

    class authorizedInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Year]

    class groundbreakingInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Year]

    class completedInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Year]

    class constructedDuringEra(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Era]

    class constructionDuration(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Duration]

    class supportsRecreationAt(ObjectProperty):
        domain = [Dam]
        range = [RelativeLocation]

    class transformedRiverSection(ObjectProperty):
        domain = [Dam]
        range = [RiverSection]

    class partOfRiver(ObjectProperty, FunctionalProperty):
        domain = [RiverSection]
        range = [River]

    class associatedIssue(ObjectProperty):
        domain = [Dam]
        range = [Issue]

    class controversyBetween(ObjectProperty):
        domain = [WaterAllocationControversy]
        range = [State]

    class affects(ObjectProperty):
        domain = [Issue]
        range = [RiverSection]

    class causedBy(ObjectProperty, FunctionalProperty):
        domain = [Issue]
        range = [Dam]

    class hasYearValue(DataProperty, FunctionalProperty):
        domain = [Year]
        range = [int]

    class hasDurationYears(DataProperty, FunctionalProperty):
        domain = [Duration]
        range = [int]

    class ReservoirDam(Dam):
        is_a = [hasReservoir.some(Reservoir)]

    class IrrigationDam(Dam):
        is_a = [hasPurpose.some(IrrigationPurpose)]

    class HydroelectricDam(Dam):
        is_a = [hasPurpose.some(HydroelectricPowerGenerationPurpose)]

    class RecreationalDam(Dam):
        is_a = [hasPurpose.some(RecreationPurpose)]

    SouthCentralMontana = Region("SouthCentralMontana")
    SouthCentralMontana.label = "south central Montana"

    Montana = State("Montana")
    Montana.label = "Montana"

    Wyoming = State("Wyoming")
    Wyoming.label = "Wyoming"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    BighornRiver = River("BighornRiver")
    BighornRiver.label = ["Bighorn River", "Bighorn"]

    YellowtailDam = ConcreteArchDam("YellowtailDam")
    YellowtailDam.label = "Yellowtail Dam"

    BighornLake = Reservoir("BighornLake")
    BighornLake.label = "Bighorn Lake"

    USBureauOfReclamation = GovernmentAgency("USBureauOfReclamation")
    USBureauOfReclamation.label = ["U.S. Bureau of Reclamation", "Reclamation"]

    FederalGovernment = Government("FederalGovernment")
    FederalGovernment.label = "federal government"

    CrowNation = NativeAmericanTribe("CrowNation")
    CrowNation.label = "Crow Nation"

    CrowIndianReservation = Reservation("CrowIndianReservation")
    CrowIndianReservation.label = "Crow Indian Reservation"

    Mid1960sEra = Era("Mid1960sEra")
    Mid1960sEra.label = "mid-1960s era"

    Year1944 = Year("Year1944")
    Year1944.label = "1944"
    Year1944.hasYearValue = 1944

    Year1961 = Year("Year1961")
    Year1961.label = "1961"
    Year1961.hasYearValue = 1961

    Year1967 = Year("Year1967")
    Year1967.label = "1967"
    Year1967.hasYearValue = 1967

    SixYears = Duration("SixYears")
    SixYears.label = "six years"
    SixYears.hasDurationYears = 6

    IrrigationPurposes = IrrigationPurpose("IrrigationPurposes")
    IrrigationPurposes.label = "irrigation purposes"

    HydroelectricPower = HydroelectricPowerGenerationPurpose("HydroelectricPower")
    HydroelectricPower.label = "hydroelectric power"

    Recreation = RecreationPurpose("Recreation")
    Recreation.label = "recreation"

    AboveStructure = RelativeLocation("AboveStructure")
    AboveStructure.label = "above the structure"

    BelowStructure = RelativeLocation("BelowStructure")
    BelowStructure.label = "below the structure"

    RiverAboveDam = RiverSection("RiverAboveDam")
    RiverAboveDam.label = "river above the dam"

    RiverBelowDam = PremierTroutStream("RiverBelowDam")
    RiverBelowDam.label = ["lower river", "river below the dam"]

    WaterAllocationInReservoir = WaterAllocationControversy("WaterAllocationInReservoir")
    WaterAllocationInReservoir.label = "allocation of water in the reservoir"

    EcologicalDamageWrought = EcologicalDamage("EcologicalDamageWrought")
    EcologicalDamageWrought.label = "ecological damage"

    SouthCentralMontana.locatedIn = [Montana]
    Montana.locatedIn = [UnitedStates]
    Wyoming.locatedIn = [UnitedStates]

    CrowNation.livedOn = [CrowIndianReservation]

    YellowtailDam.locatedIn = [SouthCentralMontana, Montana, UnitedStates]
    YellowtailDam.acrossRiver = BighornRiver
    YellowtailDam.regulatesFlowOf = [BighornRiver]
    YellowtailDam.hasReservoir = BighornLake
    YellowtailDam.ownedBy = [USBureauOfReclamation]
    YellowtailDam.hasPurpose = [IrrigationPurposes, HydroelectricPower, Recreation]
    YellowtailDam.resultedFromNegotiationsWithParty = [FederalGovernment, CrowNation]
    YellowtailDam.expectedProfitBeneficiary = [FederalGovernment, CrowNation]
    YellowtailDam.landSoldTo = [USBureauOfReclamation]
    YellowtailDam.authorizedInYear = Year1944
    YellowtailDam.groundbreakingInYear = Year1961
    YellowtailDam.completedInYear = Year1967
    YellowtailDam.constructedDuringEra = Mid1960sEra
    YellowtailDam.constructionDuration = SixYears
    YellowtailDam.supportsRecreationAt = [AboveStructure, BelowStructure]
    YellowtailDam.transformedRiverSection = [RiverBelowDam]
    YellowtailDam.associatedIssue = [WaterAllocationInReservoir, EcologicalDamageWrought]

    BighornLake.ownedBy = [USBureauOfReclamation]
    BighornLake.partiallyLiesIn = [CrowIndianReservation]
    BighornLake.extendsInto = [Wyoming]

    RiverAboveDam.partOfRiver = BighornRiver
    RiverBelowDam.partOfRiver = BighornRiver
    RiverBelowDam.locatedIn = [Montana]

    WaterAllocationInReservoir.controversyBetween = [Montana, Wyoming]

    EcologicalDamageWrought.affects = [RiverAboveDam, RiverBelowDam]
    EcologicalDamageWrought.causedBy = YellowtailDam


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
