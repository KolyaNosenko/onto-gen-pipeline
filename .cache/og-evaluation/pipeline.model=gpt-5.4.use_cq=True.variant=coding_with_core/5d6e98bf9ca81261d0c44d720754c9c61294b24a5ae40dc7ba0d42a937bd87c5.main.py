"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

What is Yellowtail Dam?
Where is Yellowtail Dam located?
Across which river is Yellowtail Dam built?
In which state is Yellowtail Dam situated?
What type of dam is Yellowtail Dam?
When was Yellowtail Dam constructed?
When was Yellowtail Dam authorized?
When did groundbreaking for Yellowtail Dam occur?
When was Yellowtail Dam completed?
How many years did the construction of Yellowtail Dam take?
What are the primary purposes of Yellowtail Dam?
Does Yellowtail Dam regulate the flow of the Bighorn River for irrigation?
Does Yellowtail Dam generate hydroelectric power?
What reservoir is associated with Yellowtail Dam?
Who owns Yellowtail Dam?
Who owns Bighorn Lake?
Which government agency owns Yellowtail Dam and its reservoir?
What negotiations led to the Yellowtail Dam project?
Which parties were involved in the negotiations for the Yellowtail Dam project?
What Native American tribe was involved in the Yellowtail Dam project?
Where is the Crow Indian Reservation in relation to Yellowtail Dam and Bighorn Lake?
Was Yellowtail Dam originally envisioned as a shared facility?
What benefits was the Yellowtail Dam project originally intended to provide to the federal government and the Crow Nation?
Was the land for the Yellowtail Dam project eventually sold to the U.S. Bureau of Reclamation?
Does any part of Bighorn Lake lie within the Crow Indian Reservation?
Does Bighorn Lake extend into Wyoming?
What additional functions does Yellowtail Dam serve today besides irrigation and hydroelectric generation?
Does Yellowtail Dam support recreational activities above and below the dam?
How has regulation by Yellowtail Dam affected the lower Bighorn River?
Has Yellowtail Dam transformed the lower Bighorn River into a premier trout stream?
What controversies are associated with Yellowtail Dam?
Is there controversy over the allocation of water in Bighorn Lake between Montana and Wyoming?
What ecological damage has been associated with Yellowtail Dam?
Has Yellowtail Dam caused ecological impacts both upstream and downstream?
Which states are involved in the water allocation controversy related to Yellowtail Dam?
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
    Accomplishment,
    AgentiveSocialObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    SocialAgent,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class GeographicRegion(SpaceRegion):
        pass


    class Country(GeographicRegion):
        pass


    class State(GeographicRegion):
        pass


    class Reservation(GeographicRegion):
        pass


    class WaterBody(NonAgentivePhysicalObject):
        pass


    class River(WaterBody):
        pass


    class Reservoir(WaterBody):
        pass


    class TroutStream(River):
        pass


    class Dam(NonAgentivePhysicalObject):
        pass


    class ConcreteArchDam(Dam):
        pass


    class Organization(SocialAgent):
        pass


    class Government(Organization):
        pass


    class GovernmentAgency(Organization):
        pass


    class NativeAmericanTribe(Society):
        pass


    class DamProject(NonAgentiveSocialObject):
        pass


    class Negotiation(Accomplishment):
        pass


    class Controversy(NonAgentiveSocialObject):
        pass


    class WaterAllocationControversy(Controversy):
        pass


    class EcologicalDamage(Controversy):
        pass


    class builtAcross(ObjectProperty):
        domain = [Dam]
        range = [River]


    class locatedIn(ObjectProperty):
        domain = [NonAgentivePhysicalObject, SpaceRegion]
        range = [SpaceRegion]


    class ownedBy(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [Organization]


    class hasReservoir(ObjectProperty):
        domain = [Dam]
        range = [Reservoir]


    class regulatesFlowOf(ObjectProperty):
        domain = [Dam]
        range = [River]


    class hasProject(ObjectProperty):
        domain = [Dam]
        range = [DamProject]


    class resultedFromNegotiation(ObjectProperty):
        domain = [DamProject]
        range = [Negotiation]


    class involvedParty(ObjectProperty):
        domain = [Negotiation]
        range = [AgentiveSocialObject]


    class homelandReservation(ObjectProperty):
        domain = [NativeAmericanTribe]
        range = [Reservation]


    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [State]


    class liesWithin(ObjectProperty):
        domain = [Reservoir]
        range = [Reservation]


    class soldTo(ObjectProperty):
        domain = [DamProject]
        range = [Organization]


    class waterAllocationContestedBetween(ObjectProperty):
        domain = [Reservoir]
        range = [State]


    class authorizedIn(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]


    class groundbreakingIn(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]


    class completedIn(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]


    class constructionEra(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]


    class locationDescription(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]


    class constructionDurationYears(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]


    class primaryPurposeDescription(DataProperty):
        domain = [Dam]
        range = [str]


    class additionalFunctionDescription(DataProperty):
        domain = [Dam]
        range = [str]


    class originallyEnvisionedAsSharedFacility(DataProperty, FunctionalProperty):
        domain = [DamProject]
        range = [bool]


    class intendedBenefitDescription(DataProperty):
        domain = [DamProject]
        range = [str]


    class transformedLowerRiverIntoPremierTroutStream(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [bool]


    class hasWaterAllocationControversy(DataProperty, FunctionalProperty):
        domain = [Reservoir]
        range = [bool]


    class ecologicalDamageDescription(DataProperty):
        domain = [Dam]
        range = [str]


    class ecologicalDamageAboveAndBelowDam(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [bool]


    yellowtailDam = ConcreteArchDam("YellowtailDam")
    yellowtailDam.label = "Yellowtail Dam"

    bighornRiver = River("BighornRiver")
    bighornRiver.label = "Bighorn River"

    montana = State("Montana")
    montana.label = "Montana"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    bighornLake = Reservoir("BighornLake")
    bighornLake.label = "Bighorn Lake"

    bureauOfReclamation = GovernmentAgency("USBureauOfReclamation")
    bureauOfReclamation.label = ["U.S. Bureau of Reclamation", "Reclamation"]

    federalGovernment = Government("FederalGovernment")
    federalGovernment.label = "federal government"

    crowNation = NativeAmericanTribe("CrowNation")
    crowNation.label = "Crow Nation"

    crowIndianReservation = Reservation("CrowIndianReservation")
    crowIndianReservation.label = "Crow Indian Reservation"

    wyoming = State("Wyoming")
    wyoming.label = "Wyoming"

    project = DamProject("TheProject")
    project.label = "The project"

    negotiations = Negotiation("Negotiations")
    negotiations.label = "negotiations"

    year1944 = TimeInterval("Year1944")
    year1944.label = "1944"

    year1961 = TimeInterval("Year1961")
    year1961.label = "1961"

    year1967 = TimeInterval("Year1967")
    year1967.label = "1967"

    mid1960s = TimeInterval("Mid1960s")
    mid1960s.label = "mid-1960s"

    yellowtailDam.builtAcross = [bighornRiver]
    yellowtailDam.locatedIn = [montana]
    yellowtailDam.ownedBy = [bureauOfReclamation]
    yellowtailDam.hasReservoir = [bighornLake]
    yellowtailDam.regulatesFlowOf = [bighornRiver]
    yellowtailDam.hasProject = [project]
    yellowtailDam.authorizedIn = year1944
    yellowtailDam.groundbreakingIn = year1961
    yellowtailDam.completedIn = year1967
    yellowtailDam.constructionEra = mid1960s
    yellowtailDam.locationDescription = "south central Montana"
    yellowtailDam.constructionDurationYears = 6
    yellowtailDam.primaryPurposeDescription = [
        "regulate the flow of the Bighorn for irrigation purposes",
        "generate hydroelectric power",
    ]
    yellowtailDam.additionalFunctionDescription = [
        "recreation above and below the structure",
    ]
    yellowtailDam.transformedLowerRiverIntoPremierTroutStream = True
    yellowtailDam.ecologicalDamageDescription = [
        "ecological damage on the river both above and below the dam",
    ]
    yellowtailDam.ecologicalDamageAboveAndBelowDam = True

    montana.locatedIn = [unitedStates]
    wyoming.locatedIn = [unitedStates]

    bighornLake.ownedBy = [bureauOfReclamation]
    bighornLake.extendsInto = [wyoming]
    bighornLake.liesWithin = [crowIndianReservation]
    bighornLake.waterAllocationContestedBetween = [montana, wyoming]
    bighornLake.hasWaterAllocationControversy = True

    crowNation.homelandReservation = [crowIndianReservation]

    project.resultedFromNegotiation = [negotiations]
    project.soldTo = [bureauOfReclamation]
    project.originallyEnvisionedAsSharedFacility = True
    project.intendedBenefitDescription = ["profits for both sides"]

    negotiations.involvedParty = [federalGovernment, crowNation]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
