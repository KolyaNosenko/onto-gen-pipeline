"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What is Yellowtail Dam located across?
2. In what region and country is Yellowtail Dam located?
3. What type of dam is Yellowtail Dam?
4. What river does Yellowtail Dam regulate?
5. What are the original purposes of Yellowtail Dam?
6. What power generation does Yellowtail Dam provide?
7. Who owns Yellowtail Dam and Bighorn Lake?
8. What is the name of the reservoir created by Yellowtail Dam?
9. Which federal agency owns the dam and its reservoir?
10. What Native American tribe was involved in the project negotiations for Yellowtail Dam?
11. On whose reservation is much of the reservoir located?
12. Was Yellowtail Dam originally envisioned as a shared facility?
13. What benefits was the shared facility expected to provide?
14. In what year was Yellowtail Dam authorized?
15. In what year did groundbreaking for Yellowtail Dam occur?
16. In what year was Yellowtail Dam completed?
17. How long did construction of Yellowtail Dam take?
18. What additional uses does Yellowtail Dam serve today beyond its original purposes?
19. How has regulation of the Bighorn River by Yellowtail Dam affected the lower river?
20. What controversy surrounds the reservoir associated with Yellowtail Dam?
21. What ecological impacts have been associated with Yellowtail Dam?
22. Does the reservoir extend into Wyoming?
23. What is the relationship between Yellowtail Dam and recreation in the surrounding area?
24. What was the result of the negotiations between the federal government and the Crow Nation regarding the dam project?
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
    Abstract,
    NonAgentivePhysicalObject,
    Process,
    Society,
    SocialAgent,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class Dam(NonAgentivePhysicalObject):
        pass

    class ConcreteArchDam(Dam):
        pass

    class River(NonAgentivePhysicalObject):
        pass

    class Reservoir(NonAgentivePhysicalObject):
        pass

    class Land(NonAgentivePhysicalObject):
        pass

    class Facility(NonAgentivePhysicalObject):
        pass

    class TroutStream(River):
        pass

    class Agency(SocialAgent):
        pass

    class Government(SocialAgent):
        pass

    class Tribe(Society):
        pass

    class GeographicRegion(SpaceRegion):
        pass

    class Country(GeographicRegion):
        pass

    class USState(GeographicRegion):
        pass

    class Reservation(GeographicRegion):
        pass

    class Project(Process):
        pass

    class Negotiation(Process):
        pass

    class Construction(Process):
        pass

    class Purpose(Abstract):
        pass

    class Controversy(Abstract):
        pass

    class Damage(Abstract):
        pass

    class locatedAcross(ObjectProperty):
        domain = [Dam]
        range = [River]

    class locatedIn(ObjectProperty):
        domain = [NonAgentivePhysicalObject, GeographicRegion]
        range = [GeographicRegion]

    class ownedBy(ObjectProperty):
        domain = [Dam, Reservoir, Land]
        range = [Agency]

    class regulatesFlowOf(ObjectProperty):
        domain = [Dam]
        range = [River]

    class createdReservoir(ObjectProperty):
        domain = [Dam]
        range = [Reservoir]

    class hasOriginalPurpose(ObjectProperty):
        domain = [Dam]
        range = [Purpose]

    class hasCurrentUse(ObjectProperty):
        domain = [Dam]
        range = [Purpose]

    class negotiatedBetween(ObjectProperty):
        domain = [Negotiation]
        range = [Government, Tribe]

    class resultedFrom(ObjectProperty):
        domain = [Project]
        range = [Negotiation]

    class originallyEnvisionedAs(ObjectProperty):
        domain = [Project]
        range = [Facility]

    class expectedToProvideProfitsFor(ObjectProperty):
        domain = [Facility]
        range = [Government, Tribe]

    class soldTo(ObjectProperty):
        domain = [Land]
        range = [Agency]

    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [USState]

    class liesIn(ObjectProperty):
        domain = [Reservoir]
        range = [Reservation]

    class transformedInto(ObjectProperty):
        domain = [River]
        range = [TroutStream]

    class concerns(ObjectProperty):
        domain = [Controversy]
        range = [Reservoir]

    class betweenStates(ObjectProperty):
        domain = [Controversy]
        range = [USState]

    class affects(ObjectProperty):
        domain = [Damage]
        range = [River]

    class authorizedYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class groundbreakingYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class completedYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class constructionDurationYears(DataProperty, FunctionalProperty):
        domain = [Construction]
        range = [int]

    YellowtailDam = ConcreteArchDam("YellowtailDam")
    YellowtailDam.label = "Yellowtail Dam"

    BighornRiver = River("BighornRiver")
    BighornRiver.label = "Bighorn River"

    SouthCentralMontana = GeographicRegion("SouthCentralMontana")
    SouthCentralMontana.label = "south central Montana"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    BighornLake = Reservoir("BighornLake")
    BighornLake.label = "Bighorn Lake"

    USBureauOfReclamation = Agency("USBureauOfReclamation")
    USBureauOfReclamation.label = ["U.S. Bureau of Reclamation", "Reclamation"]

    CrowNation = Tribe("CrowNation")
    CrowNation.label = "Crow Nation"

    CrowIndianReservation = Reservation("CrowIndianReservation")
    CrowIndianReservation.label = "Crow Indian Reservation"

    Montana = USState("Montana")
    Montana.label = "Montana"

    Wyoming = USState("Wyoming")
    Wyoming.label = "Wyoming"

    FederalGovernment = Government("FederalGovernment")
    FederalGovernment.label = "federal government"

    YellowtailDamProject = Project("YellowtailDamProject")
    YellowtailDamProject.label = "the project"

    Negotiations = Negotiation("Negotiations")
    Negotiations.label = "negotiations"

    SharedFacility = Facility("SharedFacility")
    SharedFacility.label = "a shared facility"

    IrrigationPurpose = Purpose("IrrigationPurpose")
    IrrigationPurpose.label = "irrigation purposes"

    HydroelectricPower = Purpose("HydroelectricPower")
    HydroelectricPower.label = "hydroelectric power"

    Recreation = Purpose("Recreation")
    Recreation.label = "recreation both above and below the structure"

    TheLand = Land("TheLand")
    TheLand.label = "the land"

    ConstructionOfYellowtailDam = Construction("ConstructionOfYellowtailDam")
    ConstructionOfYellowtailDam.label = "construction"

    SixYearsOfConstruction = TimeInterval("SixYearsOfConstruction")
    SixYearsOfConstruction.label = "six years of construction"

    WaterAllocationControversy = Controversy("WaterAllocationControversy")
    WaterAllocationControversy.label = (
        "significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming"
    )

    EcologicalDamage = Damage("EcologicalDamage")
    EcologicalDamage.label = "ecological damage"

    RiverAboveDam = River("RiverAboveDam")
    RiverAboveDam.label = "river above the dam"

    RiverBelowDam = River("RiverBelowDam")
    RiverBelowDam.label = "river below the dam"

    PremierTroutStream = TroutStream("PremierTroutStream")
    PremierTroutStream.label = "one of Montana's premier trout streams"

    YellowtailDam.locatedAcross.append(BighornRiver)
    YellowtailDam.locatedIn.append(SouthCentralMontana)
    YellowtailDam.locatedIn.append(Montana)
    YellowtailDam.locatedIn.append(UnitedStates)
    YellowtailDam.ownedBy.append(USBureauOfReclamation)
    YellowtailDam.regulatesFlowOf.append(BighornRiver)
    YellowtailDam.createdReservoir.append(BighornLake)
    YellowtailDam.hasOriginalPurpose.append(IrrigationPurpose)
    YellowtailDam.hasOriginalPurpose.append(HydroelectricPower)
    YellowtailDam.hasCurrentUse.append(Recreation)
    YellowtailDam.authorizedYear = 1944
    YellowtailDam.groundbreakingYear = 1961
    YellowtailDam.completedYear = 1967

    BighornRiver.locatedIn.append(SouthCentralMontana)
    BighornRiver.locatedIn.append(Montana)

    SouthCentralMontana.locatedIn.append(Montana)
    Montana.locatedIn.append(UnitedStates)
    Wyoming.locatedIn.append(UnitedStates)

    BighornLake.ownedBy.append(USBureauOfReclamation)
    BighornLake.liesIn.append(CrowIndianReservation)
    BighornLake.extendsInto.append(Wyoming)
    BighornLake.locatedIn.append(CrowIndianReservation)
    BighornLake.locatedIn.append(Wyoming)

    CrowIndianReservation.locatedIn.append(Montana)
    TheLand.locatedIn.append(CrowIndianReservation)
    TheLand.soldTo.append(USBureauOfReclamation)

    Negotiations.negotiatedBetween.append(FederalGovernment)
    Negotiations.negotiatedBetween.append(CrowNation)

    YellowtailDamProject.resultedFrom.append(Negotiations)
    YellowtailDamProject.originallyEnvisionedAs.append(SharedFacility)
    SharedFacility.expectedToProvideProfitsFor.append(FederalGovernment)
    SharedFacility.expectedToProvideProfitsFor.append(CrowNation)

    ConstructionOfYellowtailDam.temporallyLocatedAt = SixYearsOfConstruction
    ConstructionOfYellowtailDam.constructionDurationYears = 6

    WaterAllocationControversy.concerns.append(BighornLake)
    WaterAllocationControversy.betweenStates.append(Montana)
    WaterAllocationControversy.betweenStates.append(Wyoming)

    EcologicalDamage.affects.append(RiverAboveDam)
    EcologicalDamage.affects.append(RiverBelowDam)

    BighornRiver.transformedInto.append(PremierTroutStream)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
