"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

What monarchies are located in Oceania?
How many sovereign monarchies are there in Oceania?
Which states in Oceania are self-governing sovereign monarchies?
What defines a monarchy in Oceania as a self-governing sovereign state?
Who is the head of state of each monarchy in Oceania?
Which monarchies in Oceania are constitutional monarchies?
What are the characteristics of a constitutional monarchy in Oceania?
How is the sovereign selected in the monarchies of Oceania?
Does the sovereign in each Oceania monarchy hold office until death or abdication?
Are the powers of the sovereign in Oceania monarchies limited by laws and customs?
Which Oceania monarchies share Queen Elizabeth II as head of state?
How many monarchies in Oceania share Queen Elizabeth II as their head of state?
Which Oceania monarchies are part of the Commonwealth realms?
Are all monarchies in Oceania members of the Commonwealth of Nations?
Which sovereign monarchy in Oceania does not share a monarch with another state?
Does Tonga share its monarch with any other state?
What is the relationship between the monarchies of Oceania and the Commonwealth of Nations?
What is the relationship between the Commonwealth realms and the monarchies of Oceania?
Which countries in Oceania have dependencies within the region and outside it?
Do Australia and New Zealand have dependencies within Oceania?
Do Australia and New Zealand have dependencies outside Oceania?
How many non-sovereign constituent monarchs are recognized in the region?
Which countries recognize non-sovereign constituent monarchs in Oceania?
Which non-sovereign constituent monarchs are recognized by New Zealand, Papua New Guinea, and France?
Are there non-sovereign constituent monarchs in Oceania?
Which monarchy in Oceania is unique in not sharing its monarch with another state?
Are all sovereign monarchies in Oceania hereditary?
Is the head of state in every Oceania monarchy an individual hereditary sovereign?
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
    AgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
)


with core:
    class GeographicRegion(SpaceRegion):
        pass


    class Country(Society):
        pass


    class SovereignState(Country):
        pass


    class Dependency(Country):
        pass


    class Monarchy(SovereignState):
        pass


    class ConstitutionalMonarchy(Monarchy):
        pass


    class NonSovereignConstituentMonarchy(Dependency):
        pass


    class PoliticalGrouping(Society):
        pass


    class MonarchyCollection(NonAgentiveSocialObject):
        pass


    class Monarch(AgentivePhysicalObject):
        pass


    class HereditaryMonarch(Monarch):
        pass


    class locatedIn(ObjectProperty):
        domain = [Country, MonarchyCollection]
        range = [GeographicRegion]


    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [Monarch]


    class memberOf(ObjectProperty):
        domain = [Country]
        range = [PoliticalGrouping]


    class recognizedBy(ObjectProperty):
        domain = [MonarchyCollection]
        range = [Country]


    class monarchyCount(DataProperty, FunctionalProperty):
        domain = [GeographicRegion]
        range = [int]


    class memberCount(DataProperty, FunctionalProperty):
        domain = [PoliticalGrouping, MonarchyCollection]
        range = [int]


    class isSelfGoverning(DataProperty, FunctionalProperty):
        domain = [SovereignState]
        range = [bool]


    class allMonarchiesMemberOfCommonwealthOfNations(DataProperty, FunctionalProperty):
        domain = [GeographicRegion]
        range = [bool]


    class sharesMonarchWithAnotherState(DataProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [bool]


    class inheritsOfficeHereditarily(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]


    class holdsOfficeUntilDeathOrAbdication(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]


    class exercisesPowersUnderLawsAndCustoms(DataProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [bool]


    class hasDependenciesWithinRegion(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]


    class hasDependenciesOutsideRegion(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]


    class headOfStateMonarchyCount(DataProperty, FunctionalProperty):
        domain = [Monarch]
        range = [int]


    Monarchy.is_a.append(hasHeadOfState.some(HereditaryMonarch))
    Monarchy.is_a.append(locatedIn.some(GeographicRegion))
    NonSovereignConstituentMonarchy.is_a.append(locatedIn.some(GeographicRegion))

    oceania = GeographicRegion("Oceania")
    oceania.label = "Oceania"
    oceania.monarchyCount = 6
    oceania.allMonarchiesMemberOfCommonwealthOfNations = True

    queenElizabethIi = HereditaryMonarch("QueenElizabethII")
    queenElizabethIi.label = "Queen Elizabeth II"
    queenElizabethIi.headOfStateMonarchyCount = 5

    commonwealthRealms = PoliticalGrouping("CommonwealthRealms")
    commonwealthRealms.label = "Commonwealth realms"
    commonwealthRealms.memberCount = 5

    commonwealthOfNations = PoliticalGrouping("CommonwealthOfNations")
    commonwealthOfNations.label = "Commonwealth of Nations"

    australia = ConstitutionalMonarchy("Australia")
    australia.label = "Australia"
    australia.locatedIn = [oceania]
    australia.hasHeadOfState = queenElizabethIi
    australia.memberOf = [commonwealthRealms, commonwealthOfNations]
    australia.isSelfGoverning = True
    australia.sharesMonarchWithAnotherState = True
    australia.inheritsOfficeHereditarily = True
    australia.holdsOfficeUntilDeathOrAbdication = True
    australia.exercisesPowersUnderLawsAndCustoms = True
    australia.hasDependenciesWithinRegion = True
    australia.hasDependenciesOutsideRegion = True

    newZealand = ConstitutionalMonarchy("NewZealand")
    newZealand.label = "New Zealand"
    newZealand.locatedIn = [oceania]
    newZealand.hasHeadOfState = queenElizabethIi
    newZealand.memberOf = [commonwealthRealms, commonwealthOfNations]
    newZealand.isSelfGoverning = True
    newZealand.sharesMonarchWithAnotherState = True
    newZealand.inheritsOfficeHereditarily = True
    newZealand.holdsOfficeUntilDeathOrAbdication = True
    newZealand.exercisesPowersUnderLawsAndCustoms = True
    newZealand.hasDependenciesWithinRegion = True
    newZealand.hasDependenciesOutsideRegion = True

    papuaNewGuinea = ConstitutionalMonarchy("PapuaNewGuinea")
    papuaNewGuinea.label = "Papua New Guinea"
    papuaNewGuinea.locatedIn = [oceania]
    papuaNewGuinea.hasHeadOfState = queenElizabethIi
    papuaNewGuinea.memberOf = [commonwealthRealms, commonwealthOfNations]
    papuaNewGuinea.isSelfGoverning = True
    papuaNewGuinea.sharesMonarchWithAnotherState = True
    papuaNewGuinea.inheritsOfficeHereditarily = True
    papuaNewGuinea.holdsOfficeUntilDeathOrAbdication = True
    papuaNewGuinea.exercisesPowersUnderLawsAndCustoms = True

    tonga = ConstitutionalMonarchy("Tonga")
    tonga.label = "Tonga"
    tonga.locatedIn = [oceania]
    tonga.memberOf = [commonwealthOfNations]
    tonga.isSelfGoverning = True
    tonga.sharesMonarchWithAnotherState = False
    tonga.inheritsOfficeHereditarily = True
    tonga.holdsOfficeUntilDeathOrAbdication = True
    tonga.exercisesPowersUnderLawsAndCustoms = True

    france = Country("France")
    france.label = "France"

    fiveNonSovereignConstituentMonarchs = MonarchyCollection("FiveNonSovereignConstituentMonarchs")
    fiveNonSovereignConstituentMonarchs.label = "five non - sovereign constituent monarchs"
    fiveNonSovereignConstituentMonarchs.locatedIn = [oceania]
    fiveNonSovereignConstituentMonarchs.memberCount = 5
    fiveNonSovereignConstituentMonarchs.recognizedBy = [newZealand, papuaNewGuinea, france]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
