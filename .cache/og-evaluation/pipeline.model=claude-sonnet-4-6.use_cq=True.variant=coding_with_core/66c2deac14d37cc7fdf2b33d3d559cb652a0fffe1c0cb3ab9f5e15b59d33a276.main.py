"""
=== TASK INPUT ===
Source text:
Yellowtail Dam is a dam across the Bighorn River in south central Montana in the United States . The mid-1960s era concrete arch dam serves to regulate the flow of the Bighorn for irrigation purposes and to generate hydroelectric power . The dam and its reservoir , Bighorn Lake , are owned by the U.S. Bureau of Reclamation . The project was the result of negotiations between the federal government and the Crow Nation , the tribe of Native Americans that lived on the surrounding Crow Indian Reservation , and was originally envisioned as a shared facility that would provide profits for both sides . Eventually , the land was sold to Reclamation , although much of the reservoir , which extends upstream into Wyoming , lies in the reservation . The dam was authorized in 1944 and groundbreaking was in 1961 ; it was completed in 1967 after six years of construction . Today aside from its original purposes the dam serves for recreation both above and below the structure . Regulation of the Bighorn provided by the Yellowtail Dam has transformed the lower river into one of Montana 's premier trout streams . However , there has been significant controversy surrounding the allocation of water in the reservoir between Montana and Wyoming , and the ecological damage wrought on of river both above and below the dam .

1. What is the primary purpose of Yellowtail Dam?
2. Which river does Yellowtail Dam cross?
3. In which state is Yellowtail Dam located?
4. What type of dam is Yellowtail Dam?
5. When was Yellowtail Dam authorized?
6. When did construction of Yellowtail Dam begin?
7. When was Yellowtail Dam completed?
8. How many years did it take to construct Yellowtail Dam?
9. What is the name of the reservoir created by Yellowtail Dam?
10. Who owns Yellowtail Dam and its reservoir?
11. Which Native American tribe was involved in negotiations regarding the construction of Yellowtail Dam?
12. What reservation surrounds the area of Yellowtail Dam?
13. Into which state does the reservoir extend upstream?
14. What recreational benefits does Yellowtail Dam provide?
15. What environmental controversy is associated with Yellowtail Dam?
16. What water allocation dispute exists in relation to Yellowtail Dam?
17. How has the regulation of the Bighorn River affected the lower river ecosystem?
18. What was the original agreement between the federal government and the Crow Nation regarding the dam?
19. What secondary purposes does Yellowtail Dam serve beyond its original functions?
20. What decade was Yellowtail Dam built in?
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
    NonAgentivePhysicalObject,
    Feature,
    Society,
    NonAgentiveSocialObject,
    TimeInterval,
)

with core:
    # ── Entity classes ────────────────────────────────────────────────────────

    class Dam(NonAgentivePhysicalObject):
        """A dam structure built to impound or regulate water."""

    class ConcreteArchDam(Dam):
        """A dam constructed from concrete in an arch form."""

    class River(Feature):
        """A natural watercourse, existentially dependent on its terrain."""

    class Reservoir(NonAgentivePhysicalObject):
        """An artificial lake created by a dam."""

    class Country(Society):
        """A sovereign nation-state."""

    class USState(Society):
        """A component state of the United States."""

    class GovernmentAgency(Society):
        """A body that is part of a government."""

    class NativeAmericanTribe(Society):
        """A recognised Native American tribal nation."""

    class NativeAmericanReservation(NonAgentiveSocialObject):
        """A legally designated territory set aside for a Native American tribe."""

    # ── Object properties ────────────────────────────────────────────────────

    class crossesRiver(ObjectProperty):
        domain = [Dam]
        range = [River]

    class regulatesFlowOf(ObjectProperty):
        domain = [Dam]
        range = [River]

    class locatedInState(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [USState]

    class locatedInCountry(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [Country]

    class createsReservoir(ObjectProperty):
        domain = [Dam]
        range = [Reservoir]

    class ownedBy(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range = [Society]

    class authorizedInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]

    class groundbreakingInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]

    class completedInYear(ObjectProperty, FunctionalProperty):
        domain = [Dam]
        range = [TimeInterval]

    class negotiationsWithTribe(ObjectProperty):
        domain = [Dam]
        range = [NativeAmericanTribe]

    class reservoirExtendsInto(ObjectProperty):
        domain = [Reservoir]
        range = [USState]

    class partiallyInReservation(ObjectProperty):
        domain = [Reservoir]
        range = [NativeAmericanReservation]

    class waterAllocationDisputeInvolves(ObjectProperty):
        domain = [Reservoir]
        range = [USState]

    # ── Data properties ──────────────────────────────────────────────────────

    class constructionDurationYears(DataProperty, FunctionalProperty):
        domain = [Dam]
        range = [int]

    class hasPurpose(DataProperty):
        domain = [Dam]
        range = [str]

    # ── Named individuals ────────────────────────────────────────────────────

    yellowtailDam = ConcreteArchDam("YellowtailDam")
    yellowtailDam.label = "Yellowtail Dam"

    bighornRiver = River("BighornRiver")
    bighornRiver.label = "Bighorn River"

    montana = USState("Montana")
    montana.label = "Montana"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    bighornLake = Reservoir("BighornLake")
    bighornLake.label = "Bighorn Lake"

    bureauOfReclamation = GovernmentAgency("USBureauOfReclamation")
    bureauOfReclamation.label = "U.S. Bureau of Reclamation"

    crowNation = NativeAmericanTribe("CrowNation")
    crowNation.label = "Crow Nation"

    crowIndianReservation = NativeAmericanReservation("CrowIndianReservation")
    crowIndianReservation.label = "Crow Indian Reservation"

    wyoming = USState("Wyoming")
    wyoming.label = "Wyoming"

    year1944 = TimeInterval("Year1944")
    year1944.label = "1944"

    year1961 = TimeInterval("Year1961")
    year1961.label = "1961"

    year1967 = TimeInterval("Year1967")
    year1967.label = "1967"

    # ── Fact assertions ──────────────────────────────────────────────────────

    yellowtailDam.crossesRiver.append(bighornRiver)
    yellowtailDam.regulatesFlowOf.append(bighornRiver)
    yellowtailDam.locatedInState.append(montana)
    yellowtailDam.locatedInCountry.append(unitedStates)
    yellowtailDam.createsReservoir.append(bighornLake)
    yellowtailDam.ownedBy.append(bureauOfReclamation)
    yellowtailDam.authorizedInYear = year1944
    yellowtailDam.groundbreakingInYear = year1961
    yellowtailDam.completedInYear = year1967
    yellowtailDam.constructionDurationYears = 6
    yellowtailDam.negotiationsWithTribe.append(crowNation)
    yellowtailDam.hasPurpose.append("irrigation")
    yellowtailDam.hasPurpose.append("hydroelectric power generation")
    yellowtailDam.hasPurpose.append("recreation")

    bighornLake.ownedBy.append(bureauOfReclamation)
    bighornLake.locatedInState.append(montana)
    bighornLake.reservoirExtendsInto.append(wyoming)
    bighornLake.partiallyInReservation.append(crowIndianReservation)
    bighornLake.waterAllocationDisputeInvolves.append(montana)
    bighornLake.waterAllocationDisputeInvolves.append(wyoming)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
