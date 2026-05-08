"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What is Yellowtail Dam and where is it located?
2. When was Yellowtail Dam authorized, built, and completed?
3. What are the primary purposes of Yellowtail Dam?
4. Who owns and operates Yellowtail Dam?
5. What river does Yellowtail Dam cross?
6. What is the reservoir associated with Yellowtail Dam called?
7. What type of dam structure is Yellowtail Dam?
8. Which Native American tribe was involved in the negotiations for Yellowtail Dam?
9. What lands does the Bighorn Lake reservoir extend into?
10. What secondary purposes does Yellowtail Dam serve today?
11. How has Yellowtail Dam affected the Bighorn River downstream?
12. What controversies exist regarding Yellowtail Dam?
13. What ecological impacts has Yellowtail Dam had on the river ecosystem?
14. How long did the construction of Yellowtail Dam take?
15. What benefits were expected for the Crow Nation from the Yellowtail Dam project?
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
    NonAgentivePhysicalObject, PhysicalEndurant, SpaceRegion, Society
)


with core:
    # Entity Classes
    class Dam(NonAgentivePhysicalObject):
        """A structure built across a river to control water flow"""
        pass

    class River(PhysicalEndurant):
        """A flowing body of water"""
        pass

    class Reservoir(PhysicalEndurant):
        """A body of water created by a dam"""
        pass

    class Territory(SpaceRegion):
        """A geographic territory or region"""
        pass

    class Tribe(Society):
        """A tribal society"""
        pass

    class GovernmentOrganization(Society):
        """A government organization"""
        pass

    # ObjectProperties
    class owns(ObjectProperty):
        domain = [GovernmentOrganization]
        range = [Dam]

    class operatedBy(ObjectProperty):
        domain = [Dam]
        range = [GovernmentOrganization]

    class crosses(ObjectProperty):
        domain = [Dam]
        range = [River]

    class hasReservoir(ObjectProperty):
        domain = [Dam]
        range = [Reservoir]

    class locatedIn(ObjectProperty):
        domain = [Dam, River, Reservoir, Tribe]
        range = [Territory]

    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [Territory]

    class affects(ObjectProperty):
        domain = [Dam]
        range = [River]

    # DataProperties
    class damType(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]

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
        domain = [Dam]
        range = [int]

    class primaryPurpose(DataProperty):
        domain = [Dam]
        range = [str]

    class secondaryPurpose(DataProperty):
        domain = [Dam]
        range = [str]

    class hasControversy(DataProperty):
        domain = [Dam]
        range = [str]

    class ecologicalImpact(DataProperty):
        domain = [Dam]
        range = [str]

    class riverEffect(DataProperty):
        domain = [Dam]
        range = [str]

    class expectedBenefit(DataProperty):
        domain = [Dam]
        range = [str]

    # Named Instances
    yellowtail_dam = Dam("YellowtailDam")
    yellowtail_dam.label = "Yellowtail Dam"
    yellowtail_dam.damType = "concrete arch"
    yellowtail_dam.authorizedYear = 1944
    yellowtail_dam.groundbreakingYear = 1961
    yellowtail_dam.completedYear = 1967
    yellowtail_dam.constructionDurationYears = 6
    yellowtail_dam.primaryPurpose = ["irrigation", "hydroelectric power generation", "regulation of river flow"]
    yellowtail_dam.secondaryPurpose = ["recreation"]
    yellowtail_dam.hasControversy = ["water allocation between Montana and Wyoming", "ecological damage"]
    yellowtail_dam.ecologicalImpact = ["ecological damage wrought on the river"]
    yellowtail_dam.riverEffect = ["transformed the lower river into one of Montana's premier trout streams"]
    yellowtail_dam.expectedBenefit = ["provide profits for both sides"]

    bighorn_river = River("BighornRiver")
    bighorn_river.label = "Bighorn River"

    bighorn_lake = Reservoir("BighornLake")
    bighorn_lake.label = "Bighorn Lake"

    bureau = GovernmentOrganization("USBureauOfReclamation")
    bureau.label = "U.S. Bureau of Reclamation"

    crow_nation = Tribe("CrowNation")
    crow_nation.label = "Crow Nation"

    montana = Territory("Montana")
    montana.label = "Montana"

    wyoming = Territory("Wyoming")
    wyoming.label = "Wyoming"

    usa = Territory("UnitedStates")
    usa.label = "United States"

    reservation = Territory("CrowIndianReservation")
    reservation.label = "Crow Indian Reservation"

    # Relations
    yellowtail_dam.locatedIn = [montana]
    yellowtail_dam.crosses = [bighorn_river]
    yellowtail_dam.hasReservoir = [bighorn_lake]
    yellowtail_dam.operatedBy = [bureau]

    bureau.owns = [yellowtail_dam]

    bighorn_river.locatedIn = [montana]

    bighorn_lake.extendsInto = [wyoming]
    bighorn_lake.locatedIn = [montana]

    crow_nation.locatedIn = [reservation]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
