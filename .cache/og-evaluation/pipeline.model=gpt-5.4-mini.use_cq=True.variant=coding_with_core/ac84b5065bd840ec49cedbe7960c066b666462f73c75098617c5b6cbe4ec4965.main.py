"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. Which self-governing sovereign states in Oceania are monarchies?
2. How many monarchies are there in Oceania?
3. Which Oceania monarchies are constitutional monarchies?
4. Who is the hereditary head of state for each monarchy in Oceania?
5. Which monarchies in Oceania share Queen Elizabeth II as head of state?
6. Which Oceania monarchies are part of the Commonwealth realms?
7. Are all monarchies in Oceania members of the Commonwealth of Nations?
8. Which monarchy in Oceania does not share a monarch with any other state?
9. Which state is the only sovereign monarchy in Oceania that does not share a monarch with another state?
10. What laws and customs constrain the exercise of power in Oceania’s constitutional monarchies?
11. Which Oceania states have dependencies within the region and outside it?
12. Which non-sovereign constituent monarchs are recognized by New Zealand, Papua New Guinea, and France?
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
    NonAgentiveSocialObject,
    Region,
    SocialAgent,
    Society,
)


with core:
    class SovereignState(Society):
        pass

    class Monarchy(SovereignState):
        pass

    class ConstitutionalMonarchy(Monarchy):
        pass

    class Monarch(SocialAgent):
        pass

    class ConstituentMonarch(Monarch):
        pass

    class Dependency(NonAgentivePhysicalObject):
        pass

    class Law(NonAgentiveSocialObject):
        pass

    class Custom(NonAgentiveSocialObject):
        pass

    class stateInRegion(ObjectProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [Region]

    class headOfState(ObjectProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [Monarch]

    class memberOf(ObjectProperty):
        domain = [SovereignState]
        range = [Society]

    class hasDependency(ObjectProperty):
        domain = [SovereignState]
        range = [Dependency]

    class dependencyLocatedIn(ObjectProperty, FunctionalProperty):
        domain = [Dependency]
        range = [Region]

    class recognizedBy(ObjectProperty):
        domain = [ConstituentMonarch]
        range = [SovereignState]

    class boundBy(ObjectProperty):
        domain = [ConstitutionalMonarchy]
        range = [Or([Law, Custom])]

    Monarchy.is_a.append(headOfState.some(Monarch))
    ConstitutionalMonarchy.is_a.append(boundBy.some(Law))
    ConstitutionalMonarchy.is_a.append(boundBy.some(Custom))

    Oceania = Region("Oceania")
    Oceania.label = "Oceania"

    CommonwealthRealms = Society("CommonwealthRealms")
    CommonwealthRealms.label = "Commonwealth realms"

    CommonwealthOfNations = Society("CommonwealthOfNations")
    CommonwealthOfNations.label = "Commonwealth of Nations"

    QueenElizabethII = Monarch("QueenElizabethII")
    QueenElizabethII.label = "Queen Elizabeth II"

    Australia = SovereignState("Australia")
    Australia.label = "Australia"
    Australia.stateInRegion = Oceania

    NewZealand = SovereignState("NewZealand")
    NewZealand.label = "New Zealand"
    NewZealand.stateInRegion = Oceania

    PapuaNewGuinea = SovereignState("PapuaNewGuinea")
    PapuaNewGuinea.label = "Papua New Guinea"

    France = SovereignState("France")
    France.label = "France"

    oceanic_monarchies = []
    for _ in range(5):
        monarchy = SovereignState()
        monarchy.is_a.append(Monarchy)
        monarchy.is_a.append(ConstitutionalMonarchy)
        monarchy.stateInRegion = Oceania
        monarchy.headOfState = QueenElizabethII
        monarchy.memberOf.append(CommonwealthRealms)
        monarchy.memberOf.append(CommonwealthOfNations)
        oceanic_monarchies.append(monarchy)

    Tonga = SovereignState("Tonga")
    Tonga.label = "Tonga"
    Tonga.is_a.append(Monarchy)
    Tonga.is_a.append(ConstitutionalMonarchy)
    Tonga.stateInRegion = Oceania
    Tonga.memberOf.append(CommonwealthOfNations)

    tongaMonarch = Monarch()
    Tonga.headOfState = tongaMonarch

    externalRegion = Region()

    for state in (Australia, NewZealand):
        internalDependency = Dependency()
        internalDependency.dependencyLocatedIn = Oceania
        state.hasDependency.append(internalDependency)

        externalDependency = Dependency()
        externalDependency.dependencyLocatedIn = externalRegion
        state.hasDependency.append(externalDependency)

    law = Law()
    custom = Custom()
    for monarchy in oceanic_monarchies + [Tonga]:
        monarchy.boundBy.append(law)
        monarchy.boundBy.append(custom)

    constituent_monarchs = []
    for _ in range(5):
        constituentMonarch = Monarch()
        constituentMonarch.is_a.append(ConstituentMonarch)
        constituentMonarch.recognizedBy.append(NewZealand)
        constituentMonarch.recognizedBy.append(PapuaNewGuinea)
        constituentMonarch.recognizedBy.append(France)
        constituent_monarchs.append(constituentMonarch)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
