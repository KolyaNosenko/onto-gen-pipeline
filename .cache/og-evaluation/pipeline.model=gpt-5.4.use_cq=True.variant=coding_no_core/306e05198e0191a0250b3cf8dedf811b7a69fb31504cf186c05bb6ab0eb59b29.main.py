"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

What is a monarchy in Oceania?
How many monarchies are there in Oceania?
Which sovereign states in Oceania are monarchies?
What makes a state in Oceania a self-governing sovereign monarchy?
Who is the head of state in each monarchy of Oceania?
Is the head of state in each Oceania monarchy an individual hereditary ruler?
Which monarchies in Oceania are constitutional monarchies?
What does it mean for a monarchy in Oceania to be constitutional?
How is the sovereign determined in the monarchies of Oceania?
Does the sovereign in Oceania monarchies usually remain in office until death or abdication?
Are the powers of the sovereign in Oceania monarchies limited by laws and customs?
Which monarchies in Oceania share Queen Elizabeth II as head of state?
How many independent states in Oceania share Queen Elizabeth II as head of state?
Are the monarchies that share Queen Elizabeth II part of the Commonwealth realms?
Which monarchies in Oceania are Commonwealth realms?
Are all monarchies in Oceania members of the Commonwealth of Nations?
Which monarchy in Oceania does not share its monarch with another state?
Is Tonga the only sovereign monarchy in Oceania with a unique monarch?
Which countries in Oceania have dependencies within the region and outside it?
Do Australia and New Zealand have dependencies in Oceania?
Which non-sovereign constituent monarchs are recognized in the region?
How many non-sovereign constituent monarchs are recognized by New Zealand, Papua New Guinea, and France?
Which states recognize non-sovereign constituent monarchs in Oceania?
Are there non-sovereign constituent monarchs recognized by New Zealand?
Are there non-sovereign constituent monarchs recognized by Papua New Guinea?
Are there non-sovereign constituent monarchs recognized by France?
What is the relationship between the monarchies of Oceania and the Commonwealth of Nations?
What is the relationship between the Commonwealth realms and the monarchies of Oceania?
Which monarchies in Oceania are sovereign and which are non-sovereign constituent monarchies?
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
    class GeopoliticalEntity(Thing):
        pass

    class Region(GeopoliticalEntity):
        pass

    class PoliticalGrouping(Thing):
        pass

    class State(GeopoliticalEntity):
        pass

    class SovereignState(State):
        pass

    class SelfGoverningState(State):
        pass

    class Monarchy(State):
        pass

    class Dependency(GeopoliticalEntity):
        pass

    class Person(Thing):
        pass

    class HereditaryHead(Person):
        pass

    class Sovereign(HereditaryHead):
        pass

    class locatedIn(ObjectProperty):
        domain = [GeopoliticalEntity]
        range = [Region]

    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [HereditaryHead]

    class hasSovereign(ObjectProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [Sovereign]

    class supremePowerResidesWith(ObjectProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [HereditaryHead]

    class memberOf(ObjectProperty):
        domain = [State]
        range = [PoliticalGrouping]

    class hasWithinRegionDependency(ObjectProperty):
        domain = [State]
        range = [Dependency]

    class hasOutsideRegionDependency(ObjectProperty):
        domain = [State]
        range = [Dependency]

    class recognizesConstituentMonarchy(ObjectProperty):
        domain = [State]
        range = [Monarchy]

    class sharesMonarchWith(ObjectProperty, SymmetricProperty):
        domain = [State]
        range = [State]

    class monarchyCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class sharedHeadOfStateStateCount(DataProperty, FunctionalProperty):
        domain = [Sovereign]
        range = [int]

    class recognizedConstituentMonarchyCount(DataProperty, FunctionalProperty):
        domain = [Region]
        range = [int]

    class hasDependenciesWithinRegion(DataProperty, FunctionalProperty):
        domain = [State]
        range = [bool]

    class hasDependenciesOutsideRegion(DataProperty, FunctionalProperty):
        domain = [State]
        range = [bool]

    class recognizesNonSovereignConstituentMonarchies(DataProperty, FunctionalProperty):
        domain = [State]
        range = [bool]

    class inheritsOfficeHereditarily(DataProperty, FunctionalProperty):
        domain = [Sovereign]
        range = [bool]

    class remainsInOfficeUntilDeathOrAbdication(DataProperty, FunctionalProperty):
        domain = [Sovereign]
        range = [bool]

    class isBoundByLawsAndCustoms(DataProperty, FunctionalProperty):
        domain = [Sovereign]
        range = [bool]

    class hasUniqueMonarchAmongOceaniaStates(DataProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [bool]

    class ConstitutionalMonarchy(Monarchy):
        is_a = [hasSovereign.some(Sovereign)]

    class SovereignMonarchy(ConstitutionalMonarchy, SovereignState):
        pass

    class OceaniaMonarchy(SovereignMonarchy, SelfGoverningState):
        is_a = [
            locatedIn.some(Region),
            hasHeadOfState.some(HereditaryHead),
            supremePowerResidesWith.some(HereditaryHead),
        ]

    class CommonwealthRealmMonarchy(OceaniaMonarchy):
        is_a = [memberOf.some(PoliticalGrouping)]

    class NonSovereignConstituentMonarchy(Monarchy):
        is_a = [locatedIn.some(Region)]

    Oceania = Region("Oceania")
    Oceania.label = "Oceania"
    Oceania.monarchyCount = 6
    Oceania.recognizedConstituentMonarchyCount = 5

    QueenElizabethII = Sovereign("QueenElizabethII")
    QueenElizabethII.label = "Queen Elizabeth II"
    QueenElizabethII.sharedHeadOfStateStateCount = 5
    QueenElizabethII.inheritsOfficeHereditarily = True
    QueenElizabethII.remainsInOfficeUntilDeathOrAbdication = True
    QueenElizabethII.isBoundByLawsAndCustoms = True

    TheCommonwealthRealms = PoliticalGrouping("TheCommonwealthRealms")
    TheCommonwealthRealms.label = "the Commonwealth realms"

    TheCommonwealthOfNations = PoliticalGrouping("TheCommonwealthOfNations")
    TheCommonwealthOfNations.label = "the Commonwealth of Nations"

    Australia = CommonwealthRealmMonarchy("Australia")
    Australia.label = "Australia"
    Australia.locatedIn = [Oceania]
    Australia.hasHeadOfState = QueenElizabethII
    Australia.hasSovereign = QueenElizabethII
    Australia.supremePowerResidesWith = QueenElizabethII
    Australia.memberOf = [TheCommonwealthRealms, TheCommonwealthOfNations]
    Australia.hasDependenciesWithinRegion = True
    Australia.hasDependenciesOutsideRegion = True

    NewZealand = CommonwealthRealmMonarchy("NewZealand")
    NewZealand.label = "New Zealand"
    NewZealand.locatedIn = [Oceania]
    NewZealand.hasHeadOfState = QueenElizabethII
    NewZealand.hasSovereign = QueenElizabethII
    NewZealand.supremePowerResidesWith = QueenElizabethII
    NewZealand.memberOf = [TheCommonwealthRealms, TheCommonwealthOfNations]
    NewZealand.hasDependenciesWithinRegion = True
    NewZealand.hasDependenciesOutsideRegion = True
    NewZealand.recognizesNonSovereignConstituentMonarchies = True

    PapuaNewGuinea = CommonwealthRealmMonarchy("PapuaNewGuinea")
    PapuaNewGuinea.label = "Papua New Guinea"
    PapuaNewGuinea.locatedIn = [Oceania]
    PapuaNewGuinea.hasHeadOfState = QueenElizabethII
    PapuaNewGuinea.hasSovereign = QueenElizabethII
    PapuaNewGuinea.supremePowerResidesWith = QueenElizabethII
    PapuaNewGuinea.memberOf = [TheCommonwealthRealms, TheCommonwealthOfNations]
    PapuaNewGuinea.recognizesNonSovereignConstituentMonarchies = True

    Tonga = OceaniaMonarchy("Tonga")
    Tonga.label = "Tonga"
    Tonga.locatedIn = [Oceania]
    Tonga.memberOf = [TheCommonwealthOfNations]
    Tonga.hasUniqueMonarchAmongOceaniaStates = True

    France = State("France")
    France.label = "France"
    France.recognizesNonSovereignConstituentMonarchies = True

    Australia.sharesMonarchWith = [NewZealand, PapuaNewGuinea]
    NewZealand.sharesMonarchWith = [Australia, PapuaNewGuinea]
    PapuaNewGuinea.sharesMonarchWith = [Australia, NewZealand]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
