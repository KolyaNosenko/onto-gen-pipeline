"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. What are the monarchies in Oceania?
2. Which states in Oceania are self-governing sovereign states with an individual hereditary head recognized as head of state?
3. Which monarchies in Oceania are constitutional monarchies?
4. What is the definition of a constitutional monarchy used for the monarchies in Oceania?
5. Which monarchies in Oceania share Queen Elizabeth II as their head of state?
6. Which states in Oceania are part of the Commonwealth realms?
7. Which monarchies in Oceania are members of the Commonwealth of Nations?
8. Which monarchy in Oceania does not share a monarch with any other state?
9. What is the only sovereign monarchy in Oceania that does not share a monarch with another state?
10. Which countries in Oceania have dependencies within the region and outside it?
11. Which non-sovereign constituent monarchs are recognized by New Zealand?
12. Which non-sovereign constituent monarchs are recognized by Papua New Guinea?
13. Which non-sovereign constituent monarchs are recognized by France?
14. How many monarchies are there in Oceania?
15. How many monarchies in Oceania share Queen Elizabeth II as head of state?
16. Are all monarchies in Oceania members of the Commonwealth of Nations?
17. Are all monarchies in Oceania constitutional monarchies?
18. Is Tonga the only sovereign monarchy in Oceania that does not share a monarch with another state?
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
    class Region(Thing):
        pass

    class Organization(Thing):
        pass

    class Country(Thing):
        pass

    class SovereignState(Country):
        pass

    class Person(Thing):
        pass

    class HeadOfState(Person):
        pass

    class HereditaryHead(HeadOfState):
        pass

    class Monarch(HereditaryHead):
        pass

    class Law(Thing):
        pass

    class Custom(Thing):
        pass

    class Dependency(Thing):
        pass

    class RegionalDependency(Dependency):
        pass

    class ExternalDependency(Dependency):
        pass

    class NonSovereignConstituentMonarchGroup(Thing):
        pass

    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [HeadOfState]

    class locatedIn(ObjectProperty):
        domain = [Country]
        range = [Region]

    class memberOf(ObjectProperty):
        domain = [Country]
        range = [Organization]

    class isBoundBy(ObjectProperty):
        domain = [SovereignState]
        range = [Thing]

    class hasDependency(ObjectProperty):
        domain = [Country]
        range = [Dependency]

    class recognizes(ObjectProperty):
        domain = [Country]
        range = [NonSovereignConstituentMonarchGroup]

    class monarchyCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class sharedHeadOfStateCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class Monarchy(SovereignState):
        is_a = [hasHeadOfState.some(HereditaryHead)]

    class ConstitutionalMonarchy(Monarchy):
        is_a = [isBoundBy.some(Law), isBoundBy.some(Custom)]

    class SovereignMonarchy(ConstitutionalMonarchy):
        pass

    class RecognizingCountry(Country):
        is_a = [recognizes.some(NonSovereignConstituentMonarchGroup)]

    class RecognizingConstitutionalMonarchy(ConstitutionalMonarchy):
        is_a = [recognizes.some(NonSovereignConstituentMonarchGroup)]

    class DependentConstitutionalMonarchy(ConstitutionalMonarchy):
        is_a = [hasDependency.some(RegionalDependency), hasDependency.some(ExternalDependency)]

    class DependentRecognizingConstitutionalMonarchy(DependentConstitutionalMonarchy, RecognizingConstitutionalMonarchy):
        pass

    Oceania = Region("Oceania")
    Oceania.label = "Oceania"
    Oceania.monarchyCount = 6
    Oceania.sharedHeadOfStateCount = 5

    CommonwealthRealms = Organization("CommonwealthRealms")
    CommonwealthRealms.label = "Commonwealth realms"

    CommonwealthOfNations = Organization("CommonwealthOfNations")
    CommonwealthOfNations.label = "Commonwealth of Nations"

    QueenElizabethII = Monarch("QueenElizabethII")
    QueenElizabethII.label = "Queen Elizabeth II"

    FiveNonSovereignConstituentMonarchs = NonSovereignConstituentMonarchGroup("FiveNonSovereignConstituentMonarchs")
    FiveNonSovereignConstituentMonarchs.label = "five non-sovereign constituent monarchs"

    Australia = DependentConstitutionalMonarchy("Australia")
    Australia.label = "Australia"
    Australia.locatedIn = [Oceania]
    Australia.hasHeadOfState = QueenElizabethII
    Australia.memberOf = [CommonwealthRealms, CommonwealthOfNations]

    NewZealand = DependentRecognizingConstitutionalMonarchy("NewZealand")
    NewZealand.label = "New Zealand"
    NewZealand.locatedIn = [Oceania]
    NewZealand.hasHeadOfState = QueenElizabethII
    NewZealand.memberOf = [CommonwealthRealms, CommonwealthOfNations]
    NewZealand.recognizes = [FiveNonSovereignConstituentMonarchs]

    PapuaNewGuinea = RecognizingConstitutionalMonarchy("PapuaNewGuinea")
    PapuaNewGuinea.label = "Papua New Guinea"
    PapuaNewGuinea.locatedIn = [Oceania]
    PapuaNewGuinea.hasHeadOfState = QueenElizabethII
    PapuaNewGuinea.memberOf = [CommonwealthRealms, CommonwealthOfNations]
    PapuaNewGuinea.recognizes = [FiveNonSovereignConstituentMonarchs]

    Tonga = SovereignMonarchy("Tonga")
    Tonga.label = "Tonga"
    Tonga.locatedIn = [Oceania]
    Tonga.memberOf = [CommonwealthOfNations]

    France = RecognizingCountry("France")
    France.label = "France"
    France.recognizes = [FiveNonSovereignConstituentMonarchs]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
