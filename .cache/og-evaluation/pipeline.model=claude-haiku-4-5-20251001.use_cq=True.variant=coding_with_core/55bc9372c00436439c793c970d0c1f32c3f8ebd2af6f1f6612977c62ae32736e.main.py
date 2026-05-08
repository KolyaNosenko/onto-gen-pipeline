"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. Which monarchies exist in Oceania?

2. What is the form of government in Oceania's monarchies?

3. Which Oceanian monarchies share Queen Elizabeth II as their head of state?

4. Which Oceanian monarchies are Commonwealth realms?

5. Which Oceanian monarchies are members of the Commonwealth of Nations?

6. Which Oceanian monarchy does not share a monarch with another state?

7. What is the succession process for monarchs in Oceania's constitutional monarchies?

8. Which countries have dependencies in Oceania?

9. How many non-sovereign constituent monarchs are recognized in the Oceania region?

10. Which countries recognize non-sovereign constituent monarchs in Oceania?

11. What is the relationship between Oceanian monarchies and the Commonwealth of Nations?

12. What are the powers and constraints of Oceanian monarchs?

13. Under what circumstances can an Oceanian monarch leave office?

14. Is Tonga a Commonwealth realm?

15. Do all Oceanian monarchies share the same head of state?
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

# TODO: import the core entity classes you actually subclass.
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject
from og_sandbox_with_core.core.entities import Society, AgentivePhysicalObject, SpaceRegion

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # TODO: declare your domain entity classes here.
    # Each MUST be a subclass of a class from `og_sandbox_with_core.core.entities`
    # (or of another domain class that ultimately roots in one). Direct
    # subclassing of `Thing` is forbidden — pick the most specific core
    # ancestor that fits.

    class Monarch(AgentivePhysicalObject):
        """An individual who serves as head of state in a monarchy."""
        pass

    class Monarchy(Society):
        """A sovereign state where supreme power resides with an individual hereditary head."""
        pass

    class ConstitutionalMonarchy(Monarchy):
        """A monarchy wherein the sovereign is bound by laws and customs in the exercise of their powers."""
        pass

    class Organization(Society):
        """A formal association or grouping of states."""
        pass

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. If a core property matches the text's semantics, subclass it;
    # otherwise declare a fresh ObjectProperty / DataProperty with explicit
    # domain / range.

    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        domain = [ConstitutionalMonarchy]
        range = [Monarch]

    class memberOf(ObjectProperty):
        domain = [ConstitutionalMonarchy]
        range = [Organization]

    class locatedIn(ObjectProperty):
        domain = [Monarchy]
        range = [SpaceRegion]

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    # Geographic region
    oceaniaRegion = SpaceRegion("OceaniaRegion")
    oceaniaRegion.label = "Oceania"

    # Heads of state
    queenElizabethII = Monarch("QueenElizabethII")
    queenElizabethII.label = "Queen Elizabeth II"

    # Organizations (must be defined before they are referenced)
    commonwealthrealms = Organization("CommonwealthRealms")
    commonwealthrealms.label = "Commonwealth realms"

    commonwealthofnations = Organization("CommonwealthOfNations")
    commonwealthofnations.label = "Commonwealth of Nations"

    # Oceanian monarchies
    tonga = ConstitutionalMonarchy("TongaKingdom")
    tonga.label = "Tonga"
    tonga.locatedIn.append(oceaniaRegion)
    tonga.memberOf.append(commonwealthofnations)

    # Other countries mentioned
    australia = Society("AustraliaState")
    australia.label = "Australia"

    newzealand = Society("NewZealandState")
    newzealand.label = "New Zealand"

    papuanewguinea = Society("PapuaNewGuineaState")
    papuanewguinea.label = "Papua New Guinea"

    france = Society("FranceState")
    france.label = "France"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
