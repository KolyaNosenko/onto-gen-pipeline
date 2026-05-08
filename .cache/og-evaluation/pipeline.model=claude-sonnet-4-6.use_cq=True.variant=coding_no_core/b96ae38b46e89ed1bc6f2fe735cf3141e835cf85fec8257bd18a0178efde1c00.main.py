"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. How many monarchies exist in Oceania?
2. What defines a constitutional monarchy in Oceania?
3. Which monarchies in Oceania share Queen Elizabeth II as their head of state?
4. What is the term for the group of states that share Queen Elizabeth II as their head of state?
5. Which monarchy in Oceania does not share its monarch with another state?
6. Which countries in Oceania are members of the Commonwealth of Nations?
7. Which countries have dependencies within the Oceania region?
8. How many non-sovereign constituent monarchies are recognized in Oceania?
9. Which countries recognize non-sovereign constituent monarchs in Oceania?
10. What are the conditions under which a sovereign in Oceania may leave their office?
11. Which sovereign states in Oceania are classified as Commonwealth realms?
12. What is the relationship between the monarchies of Oceania and the Commonwealth of Nations?
13. Does Australia have dependencies outside the Oceania region?
14. Which countries recognize the non-sovereign constituent monarchs alongside New Zealand?
15. What distinguishes Tonga from the other monarchies in Oceania?
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
    # ── ENTITY CLASSES ───────────────────────────────────────────────────────

    class Region(Thing): pass

    class Person(Thing): pass

    class Monarch(Person): pass

    class Organization(Thing): pass

    class InternationalOrganization(Organization): pass

    class GlobalGrouping(Organization): pass

    class State(Thing): pass

    class SovereignState(State): pass

    class Monarchy(SovereignState): pass

    class ConstitutionalMonarchy(Monarchy): pass

    class CommonwealthRealm(ConstitutionalMonarchy): pass

    class NonSovereignConstituentMonarchy(Monarchy): pass

    # ── OBJECT PROPERTIES ────────────────────────────────────────────────────

    class hasHeadOfState(ObjectProperty):
        domain = [Monarchy]
        range = [Monarch]

    class locatedIn(ObjectProperty):
        domain = [State]
        range = [Region]

    class memberOf(ObjectProperty):
        domain = [SovereignState]
        range = [Organization]

    class partOf(ObjectProperty):
        domain = [SovereignState]
        range = [GlobalGrouping]

    class hasDependencyIn(ObjectProperty):
        domain = [SovereignState]
        range = [Region]

    class sharesMonarchWith(ObjectProperty, SymmetricProperty):
        domain = [ConstitutionalMonarchy]
        range = [ConstitutionalMonarchy]

    class recognizesConstituentMonarchy(ObjectProperty):
        domain = [SovereignState]
        range = [NonSovereignConstituentMonarchy]

    # ── DATA PROPERTIES ──────────────────────────────────────────────────────

    class monarchyCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class nonSovereignConstituentMonarchyCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class officeIsInherited(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]

    class sovereignBoundByLawsAndCustoms(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]

    class sovereignLeavesOfficeBy(DataProperty):
        domain = [ConstitutionalMonarchy]
        range = [str]

    class hasDependenciesOutsideRegion(DataProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [bool]

    class isSoleMonarchy(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]

    class acknowledgesNonSovereignConstituentMonarchy(DataProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [bool]

    # ── CLASS RESTRICTIONS ───────────────────────────────────────────────────

    # Every monarchy has some hereditary head of state
    Monarchy.is_a.append(hasHeadOfState.some(Monarch))

    # ── INDIVIDUALS ──────────────────────────────────────────────────────────

    # Region
    OceaniaRegion = Region("OceaniaRegion")
    OceaniaRegion.label = "Oceania"
    OceaniaRegion.monarchyCount = 6
    OceaniaRegion.nonSovereignConstituentMonarchyCount = 5

    # International Organization
    CommonwealthOfNationsOrg = InternationalOrganization("CommonwealthOfNationsOrg")
    CommonwealthOfNationsOrg.label = "Commonwealth of Nations"

    # Global Grouping
    CommonwealthRealmsGrouping = GlobalGrouping("CommonwealthRealmsGrouping")
    CommonwealthRealmsGrouping.label = "Commonwealth realms"

    # Monarch
    QueenElizabethII = Monarch("QueenElizabethII")
    QueenElizabethII.label = "Queen Elizabeth II"

    # Tonga — the only sovereign monarchy in Oceania that does not share its monarch
    TongaState = ConstitutionalMonarchy("TongaState")
    TongaState.label = "Tonga"
    TongaState.locatedIn = [OceaniaRegion]
    TongaState.memberOf = [CommonwealthOfNationsOrg]
    TongaState.officeIsInherited = True
    TongaState.sovereignBoundByLawsAndCustoms = True
    TongaState.sovereignLeavesOfficeBy = ["death", "abdication"]
    TongaState.isSoleMonarchy = True

    # Australia — Commonwealth realm; dependencies both within and outside Oceania
    AustraliaState = CommonwealthRealm("AustraliaState")
    AustraliaState.label = "Australia"
    AustraliaState.locatedIn = [OceaniaRegion]
    AustraliaState.hasHeadOfState = [QueenElizabethII]
    AustraliaState.memberOf = [CommonwealthOfNationsOrg]
    AustraliaState.partOf = [CommonwealthRealmsGrouping]
    AustraliaState.hasDependencyIn = [OceaniaRegion]
    AustraliaState.hasDependenciesOutsideRegion = True
    AustraliaState.officeIsInherited = True
    AustraliaState.sovereignBoundByLawsAndCustoms = True
    AustraliaState.sovereignLeavesOfficeBy = ["death", "abdication"]
    AustraliaState.isSoleMonarchy = False

    # New Zealand — Commonwealth realm; dependencies in and outside Oceania;
    # recognizes non-sovereign constituent monarchies
    NewZealandState = CommonwealthRealm("NewZealandState")
    NewZealandState.label = "New Zealand"
    NewZealandState.locatedIn = [OceaniaRegion]
    NewZealandState.hasHeadOfState = [QueenElizabethII]
    NewZealandState.memberOf = [CommonwealthOfNationsOrg]
    NewZealandState.partOf = [CommonwealthRealmsGrouping]
    NewZealandState.hasDependencyIn = [OceaniaRegion]
    NewZealandState.hasDependenciesOutsideRegion = True
    NewZealandState.officeIsInherited = True
    NewZealandState.sovereignBoundByLawsAndCustoms = True
    NewZealandState.sovereignLeavesOfficeBy = ["death", "abdication"]
    NewZealandState.isSoleMonarchy = False
    NewZealandState.acknowledgesNonSovereignConstituentMonarchy = True

    # Papua New Guinea — recognizes non-sovereign constituent monarchies
    PapuaNewGuineaState = SovereignState("PapuaNewGuineaState")
    PapuaNewGuineaState.label = "Papua New Guinea"
    PapuaNewGuineaState.acknowledgesNonSovereignConstituentMonarchy = True

    # France — recognizes non-sovereign constituent monarchies
    FranceState = SovereignState("FranceState")
    FranceState.label = "France"
    FranceState.acknowledgesNonSovereignConstituentMonarchy = True

    # Symmetric sharesMonarchWith links among named Commonwealth realms
    AustraliaState.sharesMonarchWith = [NewZealandState]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
