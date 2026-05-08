"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

What is the name of the dam described in the document?

On which river is Yellowtail Dam located?

In which geographic region and country is Yellowtail Dam located?

What type of dam is Yellowtail Dam?

What are the original purposes of Yellowtail Dam?

What additional purpose does Yellowtail Dam serve today besides its original purposes?

Who owns Yellowtail Dam and its reservoir?

What is the name of the reservoir associated with Yellowtail Dam?

What is the name of the tribe involved in negotiations over the dam project?

On what reservation did the Crow Nation live?

Was Yellowtail Dam originally envisioned as a shared facility, and if so, shared between which parties?

Was the land for the project eventually sold, and to whom?

In what year was Yellowtail Dam authorized?

In what year did groundbreaking for Yellowtail Dam occur?

In what year was Yellowtail Dam completed?

How long did construction of Yellowtail Dam take?

Does the reservoir extend into another state, and if so, which one?

What recreational uses does Yellowtail Dam support?

How has the regulation of the Bighorn River by Yellowtail Dam affected the lower river?

What controversy exists regarding the water in the reservoir?

What ecological impacts are associated with Yellowtail Dam?

Where is Yellowtail Dam located relative to the Crow Indian Reservation?
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
    class Location(Thing):
        pass

    class GeographicRegion(Location):
        pass

    class Country(Location):
        pass

    class State(Location):
        pass

    class River(Location):
        pass

    class Lake(Location):
        pass

    class Reservoir(Lake):
        pass

    class Reservation(Location):
        pass

    class Organization(Thing):
        pass

    class Government(Organization):
        pass

    class Bureau(Organization):
        pass

    class Tribe(Organization):
        pass

    class Project(Thing):
        pass

    class Dam(Thing):
        pass

    class ArchDam(Dam):
        pass

    class ConcreteArchDam(ArchDam):
        pass

    class Purpose(Thing):
        pass

    class Controversy(Thing):
        pass

    class EnvironmentalImpact(Thing):
        pass

    class WaterAllocationControversy(Controversy):
        pass

    class EcologicalDamage(EnvironmentalImpact):
        pass

    class locatedInRegion(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [GeographicRegion]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Country]

    class locatedInState(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [State]

    class locatedInReservation(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Reservation]

    class acrossRiver(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [River]

    class hasReservoir(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Reservoir]

    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Organization]

    class livesOnReservation(ObjectProperty, FunctionalProperty):
        domain = [Tribe]
        range = [Reservation]

    class extendsIntoState(ObjectProperty, FunctionalProperty):
        domain = [Reservoir]
        range = [State]

    class originalPurpose(ObjectProperty):
        domain = [Dam]
        range = [Purpose]

    class currentPurpose(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Purpose]

    class regulatesFlowOf(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [River]

    class negotiatedWith(ObjectProperty):
        domain = [Project]
        range = [Organization]

    class landSoldTo(ObjectProperty, FunctionalProperty):
        domain = [Project]
        range = [Organization]

    class relatedDam(ObjectProperty, FunctionalProperty):
        domain = [Project]
        range = [Dam]

    class hasControversy(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Controversy]

    class hasImpact(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [EnvironmentalImpact]

    class originallyEnvisionedAsDescription(DataProperty, FunctionalProperty):
        domain = [Project]
        range = [str]

    class recreationLocationDescription(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]

    class lowerRiverTransformationDescription(DataProperty, FunctionalProperty):
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

    YellowtailDam = ConcreteArchDam("YellowtailDam")
    YellowtailDam.label = "Yellowtail Dam"

    BighornRiver = River("BighornRiver")
    BighornRiver.label = ["Bighorn River", "Bighorn"]

    SouthCentralMontana = GeographicRegion("SouthCentralMontana")
    SouthCentralMontana.label = "south central Montana"

    Montana = State("Montana")
    Montana.label = "Montana"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    BighornLake = Reservoir("BighornLake")
    BighornLake.label = "Bighorn Lake"

    USBureauOfReclamation = Bureau("USBureauOfReclamation")
    USBureauOfReclamation.label = ["U.S. Bureau of Reclamation", "Reclamation"]

    FederalGovernment = Government("FederalGovernment")
    FederalGovernment.label = "federal government"

    CrowNation = Tribe("CrowNation")
    CrowNation.label = "Crow Nation"

    CrowIndianReservation = Reservation("CrowIndianReservation")
    CrowIndianReservation.label = "Crow Indian Reservation"

    Wyoming = State("Wyoming")
    Wyoming.label = "Wyoming"

    YellowtailDamProject = Project("YellowtailDamProject")
    YellowtailDamProject.label = "The project"

    IrrigationPurposes = Purpose("IrrigationPurposes")
    IrrigationPurposes.label = "irrigation purposes"

    HydroelectricPowerUse = Purpose("HydroelectricPowerUse")
    HydroelectricPowerUse.label = "hydroelectric power"

    RecreationUse = Purpose("RecreationUse")
    RecreationUse.label = "recreation"

    WaterAllocationControversyBetweenMontanaAndWyoming = WaterAllocationControversy("WaterAllocationControversyBetweenMontanaAndWyoming")
    WaterAllocationControversyBetweenMontanaAndWyoming.label = "significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming"

    EcologicalDamageAboveAndBelowDam = EcologicalDamage("EcologicalDamageAboveAndBelowDam")
    EcologicalDamageAboveAndBelowDam.label = "ecological damage wrought on river both above and below the dam"

    YellowtailDam.locatedInRegion = SouthCentralMontana
    YellowtailDam.locatedInState = Montana
    YellowtailDam.locatedInCountry = UnitedStates
    YellowtailDam.acrossRiver = BighornRiver
    YellowtailDam.hasReservoir = BighornLake
    YellowtailDam.ownedBy = USBureauOfReclamation
    YellowtailDam.regulatesFlowOf = BighornRiver
    YellowtailDam.originalPurpose = [IrrigationPurposes, HydroelectricPowerUse]
    YellowtailDam.currentPurpose = RecreationUse
    YellowtailDam.recreationLocationDescription = "both above and below the structure"
    YellowtailDam.lowerRiverTransformationDescription = "one of Montana's premier trout streams"
    YellowtailDam.hasControversy = WaterAllocationControversyBetweenMontanaAndWyoming
    YellowtailDam.hasImpact = EcologicalDamageAboveAndBelowDam
    YellowtailDam.authorizedYear = 1944
    YellowtailDam.groundbreakingYear = 1961
    YellowtailDam.completedYear = 1967
    YellowtailDam.constructionDurationYears = 6

    SouthCentralMontana.locatedInState = Montana
    Montana.locatedInCountry = UnitedStates

    BighornLake.ownedBy = USBureauOfReclamation
    BighornLake.locatedInReservation = CrowIndianReservation
    BighornLake.extendsIntoState = Wyoming

    CrowNation.livesOnReservation = CrowIndianReservation

    YellowtailDamProject.negotiatedWith = [FederalGovernment, CrowNation]
    YellowtailDamProject.originallyEnvisionedAsDescription = "a shared facility that would provide profits for both sides"
    YellowtailDamProject.landSoldTo = USBureauOfReclamation
    YellowtailDamProject.relatedDam = YellowtailDam


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
