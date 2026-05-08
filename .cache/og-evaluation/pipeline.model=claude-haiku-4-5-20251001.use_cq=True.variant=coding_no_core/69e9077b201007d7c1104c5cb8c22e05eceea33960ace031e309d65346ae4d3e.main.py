"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What is the Yellowtail Dam and where is it located?
2. When was the Yellowtail Dam authorized, constructed, and completed?
3. What are the primary purposes of the Yellowtail Dam?
4. Which river does the Yellowtail Dam cross?
5. Who owns and operates the Yellowtail Dam?
6. What is the reservoir associated with the Yellowtail Dam called?
7. Which Native American tribe was involved in the negotiations for the Yellowtail Dam project?
8. What geographic areas does Bighorn Lake extend into?
9. What type of dam is the Yellowtail Dam?
10. How has the Yellowtail Dam affected the Bighorn River downstream?
11. What recreational activities are supported by the Yellowtail Dam?
12. What water allocation controversies exist regarding the Yellowtail Dam reservoir?
13. What ecological impacts has the Yellowtail Dam caused on the river?
14. How long did the construction of the Yellowtail Dam take?
15. What was the original vision for the Yellowtail Dam project regarding the Crow Nation?
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
    # Entity Classes
    class GeographicArea(Thing): pass
    class Country(GeographicArea): pass
    class State(GeographicArea): pass
    class Reservation(GeographicArea): pass

    class Dam(Thing): pass
    class ConcreteArchDam(Dam): pass

    class River(Thing): pass

    class Reservoir(Thing): pass

    class Organization(Thing): pass

    class NativeAmericanTribe(Thing): pass

    # Object Properties
    class locatedIn(ObjectProperty):
        domain = [Dam, Reservoir, Reservation]
        range = [GeographicArea]

    class spansRiver(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [River]

    class hasReservoir(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [Reservoir]

    class ownedBy(ObjectProperty, FunctionalProperty):
        domain = [Dam, Reservoir]
        range = [Organization]

    class extendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [GeographicArea]

    class negotiatedWith(ObjectProperty):
        domain = [Dam]
        range = [NativeAmericanTribe]

    class inhabits(ObjectProperty):
        domain = [NativeAmericanTribe]
        range = [Reservation]

    # Data Properties
    class authorizedInYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class constructionStartYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class completedInYear(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class constructionDurationYears(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class hasPurpose(DataProperty):
        domain = [Dam]
        range = [str]

    class originalVision(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]

    class affectsDownstreamAs(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]

    class hasWaterAllocationControversy(DataProperty, FunctionalProperty):
        domain = [Reservoir]
        range = [str]

    class hasEcologicalImpact(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [str]

    # Named Instances
    yellowtail_dam = ConcreteArchDam("YellowtailDam")
    yellowtail_dam.label = "Yellowtail Dam"

    bighorn_river = River("BighornRiver")
    bighorn_river.label = "Bighorn River"

    montana = State("Montana")
    montana.label = "Montana"

    wyoming = State("Wyoming")
    wyoming.label = "Wyoming"

    united_states = Country("UnitedStates")
    united_states.label = "United States"

    bighorn_lake = Reservoir("BighornLake")
    bighorn_lake.label = "Bighorn Lake"

    bor = Organization("USBureauOfReclamation")
    bor.label = "U.S. Bureau of Reclamation"

    crow_nation = NativeAmericanTribe("CrowNation")
    crow_nation.label = "Crow Nation"

    crow_reservation = Reservation("CrowIndianReservation")
    crow_reservation.label = "Crow Indian Reservation"

    # Property Assignments
    yellowtail_dam.locatedIn = [montana, united_states]
    yellowtail_dam.spansRiver = bighorn_river
    yellowtail_dam.hasReservoir = bighorn_lake
    yellowtail_dam.ownedBy = bor
    yellowtail_dam.authorizedInYear = 1944
    yellowtail_dam.constructionStartYear = 1961
    yellowtail_dam.completedInYear = 1967
    yellowtail_dam.constructionDurationYears = 6
    yellowtail_dam.hasPurpose = ["irrigation", "hydroelectric power", "recreation"]
    yellowtail_dam.negotiatedWith = [crow_nation]
    yellowtail_dam.originalVision = "shared facility that would provide profits for both sides"
    yellowtail_dam.affectsDownstreamAs = "transformed the lower river into one of Montana's premier trout streams"
    yellowtail_dam.hasEcologicalImpact = "ecological damage wrought on river both above and below the dam"

    bighorn_lake.ownedBy = bor
    bighorn_lake.extendsInto = [montana, wyoming]
    bighorn_lake.locatedIn = [montana, wyoming]
    bighorn_lake.hasWaterAllocationControversy = "between Montana and Wyoming"

    crow_nation.inhabits = [crow_reservation]

    crow_reservation.locatedIn = [montana]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
