"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What river does Yellowtail Dam cross?
2. In which state is Yellowtail Dam located?
3. What type of dam is Yellowtail Dam?
4. When was Yellowtail Dam completed?
5. When was Yellowtail Dam authorized?
6. When did construction of Yellowtail Dam begin?
7. How many years did it take to construct Yellowtail Dam?
8. What are the primary purposes of Yellowtail Dam?
9. Who owns Yellowtail Dam and its reservoir?
10. What is the name of the reservoir created by Yellowtail Dam?
11. Which Native American tribe was involved in negotiations for the Yellowtail Dam project?
12. What reservation surrounds the Yellowtail Dam area?
13. Into which state does the reservoir extend upstream?
14. What secondary purposes does Yellowtail Dam serve today?
15. What ecological impact has Yellowtail Dam had on the Bighorn River?
16. What has the regulation of the Bighorn River transformed the lower river into?
17. What controversies are associated with Yellowtail Dam?
18. Between which states is there controversy over water allocation in the reservoir?
19. Who originally envisioned the Yellowtail Dam as a shared facility?
20. To whom was the land eventually sold for the Yellowtail Dam project?
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
    # ── Classes ──────────────────────────────────────────────────────────────
    class Dam(Thing): pass
    class ConcreteArchDam(Dam): pass

    class River(Thing): pass
    class TroutStream(River): pass

    class Reservoir(Thing): pass

    class GeographicArea(Thing): pass
    class State(GeographicArea): pass
    class Country(GeographicArea): pass
    class Reservation(GeographicArea): pass

    class Organization(Thing): pass
    class GovernmentAgency(Organization): pass
    class Tribe(Organization): pass

    class Purpose(Thing): pass
    class IrrigationPurpose(Purpose): pass
    class HydroelectricPurpose(Purpose): pass
    class RecreationPurpose(Purpose): pass

    class Controversy(Thing): pass
    class EcologicalImpact(Thing): pass

    # ── Object Properties ────────────────────────────────────────────────────
    class crossesRiver(ObjectProperty):
        domain = [Dam]
        range  = [River]

    class locatedIn(ObjectProperty):
        domain = [Thing]
        range  = [GeographicArea]

    class hasReservoir(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range  = [Reservoir]

    class ownedBy(ObjectProperty):
        domain = [Thing]
        range  = [Organization]

    class hasPurpose(ObjectProperty):
        domain = [Dam]
        range  = [Purpose]

    class involvedInNegotiation(ObjectProperty):
        domain = [Dam]
        range  = [Organization]

    class surroundedByReservation(ObjectProperty):
        domain = [Dam]
        range  = [Reservation]

    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range  = [State]

    class regulatesRiver(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range  = [River]

    class transformedInto(ObjectProperty, FunctionalProperty):
        domain = [River]
        range  = [TroutStream]

    class hasControversy(ObjectProperty):
        domain = [Dam]
        range  = [Controversy]

    class concernsState(ObjectProperty):
        domain = [Controversy]
        range  = [State]

    class envisionedBy(ObjectProperty):
        domain = [Dam]
        range  = [Organization]

    class landSoldTo(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range  = [Organization]

    class hasEcologicalImpact(ObjectProperty):
        domain = [Dam]
        range  = [EcologicalImpact]

    # ── Data Properties ──────────────────────────────────────────────────────
    class damType(DataProperty, FunctionalProperty):
        domain = [Dam]
        range  = [str]

    class authorizationYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range  = [int]

    class groundbreakingYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range  = [int]

    class completionYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range  = [int]

    class constructionDurationYears(DataProperty, FunctionalProperty):
        domain = [Dam]
        range  = [int]

    # ── Individuals ──────────────────────────────────────────────────────────
    yellowtailDam = ConcreteArchDam("YellowtailDam")
    yellowtailDam.label = "Yellowtail Dam"

    bighornRiver = River("BighornRiver")
    bighornRiver.label = "Bighorn River"

    lowerBighornTroutStream = TroutStream("LowerBighornTroutStream")
    lowerBighornTroutStream.label = "lower Bighorn River"

    bighornLake = Reservoir("BighornLake")
    bighornLake.label = "Bighorn Lake"

    montana = State("Montana")
    montana.label = "Montana"

    wyoming = State("Wyoming")
    wyoming.label = "Wyoming"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    bureauOfReclamation = GovernmentAgency("USBureauOfReclamation")
    bureauOfReclamation.label = "U.S. Bureau of Reclamation"

    federalGovernment = GovernmentAgency("FederalGovernment")
    federalGovernment.label = "federal government"

    crowNation = Tribe("CrowNation")
    crowNation.label = "Crow Nation"

    crowIndianReservation = Reservation("CrowIndianReservation")
    crowIndianReservation.label = "Crow Indian Reservation"

    irrigationPurpose = IrrigationPurpose("Irrigation")
    irrigationPurpose.label = "Irrigation"

    hydroelectricPurpose = HydroelectricPurpose("HydroelectricPower")
    hydroelectricPurpose.label = "Hydroelectric Power Generation"

    recreationPurpose = RecreationPurpose("Recreation")
    recreationPurpose.label = "Recreation"

    waterAllocationControversy = Controversy("WaterAllocationControversy")
    waterAllocationControversy.label = "Water Allocation Controversy"

    ecologicalDamageControversy = Controversy("EcologicalDamageControversy")
    ecologicalDamageControversy.label = "Ecological Damage Controversy"

    lowerRiverTransformation = EcologicalImpact("LowerRiverTransformation")
    lowerRiverTransformation.label = "transformation of lower Bighorn River into premier trout stream"

    ecologicalDamageImpact = EcologicalImpact("EcologicalDamageImpact")
    ecologicalDamageImpact.label = "ecological damage to river above and below the dam"

    # ── Assertions ───────────────────────────────────────────────────────────
    yellowtailDam.damType                   = "concrete arch"
    yellowtailDam.authorizationYear         = 1944
    yellowtailDam.groundbreakingYear        = 1961
    yellowtailDam.completionYear            = 1967
    yellowtailDam.constructionDurationYears = 6

    yellowtailDam.crossesRiver            = [bighornRiver]
    yellowtailDam.locatedIn               = [montana, unitedStates]
    yellowtailDam.hasReservoir            = bighornLake
    yellowtailDam.ownedBy                 = [bureauOfReclamation]
    yellowtailDam.hasPurpose              = [irrigationPurpose, hydroelectricPurpose, recreationPurpose]
    yellowtailDam.involvedInNegotiation   = [crowNation, federalGovernment]
    yellowtailDam.surroundedByReservation = [crowIndianReservation]
    yellowtailDam.regulatesRiver          = bighornRiver
    yellowtailDam.hasControversy          = [waterAllocationControversy, ecologicalDamageControversy]
    yellowtailDam.envisionedBy            = [federalGovernment, crowNation]
    yellowtailDam.landSoldTo              = bureauOfReclamation
    yellowtailDam.hasEcologicalImpact     = [lowerRiverTransformation, ecologicalDamageImpact]

    bighornLake.ownedBy    = [bureauOfReclamation]
    bighornLake.locatedIn  = [montana]
    bighornLake.extendsInto = [wyoming]

    waterAllocationControversy.concernsState  = [montana, wyoming]
    ecologicalDamageControversy.concernsState = [montana, wyoming]

    crowIndianReservation.locatedIn = [montana]

    bighornRiver.transformedInto = lowerBighornTroutStream


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
