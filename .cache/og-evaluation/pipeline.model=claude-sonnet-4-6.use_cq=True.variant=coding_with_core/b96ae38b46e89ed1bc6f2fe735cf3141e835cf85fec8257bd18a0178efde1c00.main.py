"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. How many monarchies exist in Oceania?
2. What defines a monarchy as a constitutional monarchy?
3. Which monarchies in Oceania share Queen Elizabeth II as their head of state?
4. What is the name of the global grouping of states that share Queen Elizabeth II as head of state?
5. Which monarchy in Oceania does not share a monarch with another state?
6. Are all monarchies in Oceania members of the Commonwealth of Nations?
7. Which countries in Oceania have dependencies within the region?
8. Which countries in Oceania have dependencies outside the region?
9. How many non-sovereign constituent monarchies are recognized in Oceania?
10. Which countries recognize non-sovereign constituent monarchs in Oceania?
11. What is the process by which a sovereign inherits their office in a constitutional monarchy?
12. Under what circumstances can a sovereign leave their office in a constitutional monarchy?
13. What laws and customs bind the exercise of powers of a sovereign in a constitutional monarchy?
14. Which sovereign states in Oceania are part of the Commonwealth realms?
15. What is the relationship between the Commonwealth realms and the Commonwealth of Nations in Oceania?
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
    SpaceRegion,
    Society,
    SocialAgent,
)


with core:
    # --- entity classes ---

    class GeographicRegion(SpaceRegion):
        pass

    class PoliticalEntity(Society):
        pass

    class SovereignState(PoliticalEntity):
        pass

    class Monarchy(SovereignState):
        pass

    class ConstitutionalMonarchy(Monarchy):
        pass

    class Monarch(SocialAgent):
        pass

    class InternationalOrganisation(Society):
        pass

    class GlobalGrouping(InternationalOrganisation):
        pass

    class DependentTerritory(PoliticalEntity):
        pass

    class NonSovereignConstituentMonarchy(DependentTerritory):
        pass

    # --- properties ---

    class locatedIn(ObjectProperty):
        domain = [PoliticalEntity]
        range = [GeographicRegion]

    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        domain = [Monarchy]
        range = [Monarch]

    class memberOf(ObjectProperty):
        domain = [PoliticalEntity]
        range = [InternationalOrganisation]

    class hasDependency(ObjectProperty):
        domain = [SovereignState]
        range = [DependentTerritory]

    class recognizes(ObjectProperty):
        domain = [SovereignState]
        range = [NonSovereignConstituentMonarchy]

    class numberOfMonarchies(DataProperty, FunctionalProperty):
        domain = [GeographicRegion]
        range = [int]

    class numberOfNonSovereignConstituentMonarchies(DataProperty, FunctionalProperty):
        domain = [GeographicRegion]
        range = [int]

    # constitutional monarchies must have a head of state
    ConstitutionalMonarchy.is_a.append(hasHeadOfState.some(Monarch))

    # --- named individuals ---

    oceania = GeographicRegion("Oceania")
    oceania.label = "Oceania"
    oceania.numberOfMonarchies = 6
    oceania.numberOfNonSovereignConstituentMonarchies = 5

    queenElizabethII = Monarch("QueenElizabethII")
    queenElizabethII.label = "Queen Elizabeth II"

    tonga = ConstitutionalMonarchy("Tonga")
    tonga.label = "Tonga"

    australia = ConstitutionalMonarchy("Australia")
    australia.label = "Australia"

    newZealand = ConstitutionalMonarchy("NewZealand")
    newZealand.label = "New Zealand"

    papuaNewGuinea = ConstitutionalMonarchy("PapuaNewGuinea")
    papuaNewGuinea.label = "Papua New Guinea"

    france = SovereignState("France")
    france.label = "France"

    commonwealthRealms = GlobalGrouping("CommonwealthRealms")
    commonwealthRealms.label = "Commonwealth realms"

    commonwealthOfNations = InternationalOrganisation("CommonwealthOfNations")
    commonwealthOfNations.label = "Commonwealth of Nations"

    # geographic location
    tonga.locatedIn.append(oceania)
    australia.locatedIn.append(oceania)
    newZealand.locatedIn.append(oceania)
    papuaNewGuinea.locatedIn.append(oceania)

    # shared head of state: five monarchies share Queen Elizabeth II
    australia.hasHeadOfState = queenElizabethII
    newZealand.hasHeadOfState = queenElizabethII
    papuaNewGuinea.hasHeadOfState = queenElizabethII

    # Commonwealth realms: the five states sharing Queen Elizabeth II
    australia.memberOf.append(commonwealthRealms)
    newZealand.memberOf.append(commonwealthRealms)
    papuaNewGuinea.memberOf.append(commonwealthRealms)

    # all Oceanian monarchies are members of the Commonwealth of Nations
    tonga.memberOf.append(commonwealthOfNations)
    australia.memberOf.append(commonwealthOfNations)
    newZealand.memberOf.append(commonwealthOfNations)
    papuaNewGuinea.memberOf.append(commonwealthOfNations)

    # recognizes: New Zealand, Papua New Guinea and France each recognise
    # non-sovereign constituent monarchies (five total); specific names
    # are not given in the source text so no individual instances are created.


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
