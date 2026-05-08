"""
=== TASK INPUT ===
Source text:
There are six monarchies in Oceania ; that is : self - governing sovereign states in Oceania where supreme power resides with an individual hereditary head , who is recognised as the head of state . Each is a constitutional monarchy , wherein the sovereign inherits his or her office , usually keeps it until death or abdication , and is bound by laws and customs in the exercise of their powers . Five of these independent states share Queen Elizabeth II as their respective head of state , making them part of a global grouping known as the Commonwealth realms ; in addition , all monarchies of Oceania are members of the Commonwealth of Nations . The only sovereign monarchy in Oceania that does not share a monarch with another state is Tonga . Australia and New Zealand have dependencies within the region and outside it , although five non - sovereign constituent monarchs are recognized by New Zealand , Papua New Guinea and France .

1. What are the six monarchies in Oceania?

2. Which monarchies in Oceania share Queen Elizabeth II as their head of state?

3. What is the definition of a constitutional monarchy?

4. Which Oceania monarchies are members of the Commonwealth of Nations?

5. Which Oceania monarchies are Commonwealth realms?

6. Is Tonga a sovereign monarchy, and does it share its monarch with other states?

7. What are the dependencies of Australia and New Zealand in Oceania?

8. Which non-sovereign constituent monarchies are recognized by New Zealand, Papua New Guinea, and France?

9. How many independent monarchies are there in Oceania that share a head of state with another nation?

10. What are the characteristics of a constitutional monarchy in Oceania?

11. Which Oceania monarchies have hereditary heads of state?

12. What is the relationship between Oceania monarchies and the Commonwealth realms?
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
    # Entity Classes: Monarchies and Related Entities
    class Monarchy(Thing):
        """A self-governing sovereign state with a hereditary head of state"""
        pass
    
    class ConstituionalMonarchy(Monarchy):
        """A monarchy where the sovereign is bound by laws and customs"""
        pass
    
    class SovereignMonarchy(Monarchy):
        """An independent, self-governing monarchy"""
        pass
    
    class OceaniaMonarchy(ConstituionalMonarchy, SovereignMonarchy):
        """A sovereign constitutional monarchy in Oceania"""
        pass
    
    class CommonwealthRealm(OceaniaMonarchy):
        """An Oceania monarchy that shares Queen Elizabeth II as head of state"""
        pass
    
    class NonSovereignMonarchy(Monarchy):
        """A non-independent, constituent monarchy"""
        pass
    
    class Monarch(Thing):
        """A person who serves as the hereditary head of state of a monarchy"""
        pass
    
    class Region(Thing):
        """A geographical area"""
        pass
    
    class Organization(Thing):
        """An international organization or grouping of states"""
        pass
    
    # Domain Properties
    class hasHeadOfState(ObjectProperty, FunctionalProperty):
        """Relates a monarchy to its hereditary head of state"""
        domain = [Monarchy]
        range = [Monarch]
    
    class isMemberOf(ObjectProperty):
        """Relates a monarchy to an international organization it is a member of"""
        domain = [Monarchy]
        range = [Organization]
    
    class isInRegion(ObjectProperty, FunctionalProperty):
        """Relates a monarchy to its geographical region"""
        domain = [Monarchy]
        range = [Region]
    
    class hasDependency(ObjectProperty):
        """Relates a monarchy to its dependent territories"""
        domain = [Monarchy]
        range = [Thing]
    
    class isRecognizedBy(ObjectProperty):
        """Relates a non-sovereign monarchy to entities that recognize it"""
        domain = [NonSovereignMonarchy]
        range = [Thing]
    
    # Named Individuals: Regions, Persons, and Organizations
    oceania = Region("Oceania")
    oceania.label = "Oceania"
    
    queen_elizabeth_ii = Monarch("QueenElizabethII")
    queen_elizabeth_ii.label = "Queen Elizabeth II"
    
    commonwealth_of_nations = Organization("CommonwealthOfNations")
    commonwealth_of_nations.label = "Commonwealth of Nations"
    
    commonwealth_realms_org = Organization("CommonwealthRealms")
    commonwealth_realms_org.label = "Commonwealth realms"
    
    # Named Individuals: The Oceania Monarchies (Explicitly Mentioned)
    tonga = OceaniaMonarchy("Tonga")
    tonga.label = "Tonga"
    tonga.isInRegion = oceania
    tonga.isMemberOf = [commonwealth_of_nations]
    
    australia = CommonwealthRealm("Australia")
    australia.label = "Australia"
    australia.isInRegion = oceania
    australia.hasHeadOfState = queen_elizabeth_ii
    australia.isMemberOf = [commonwealth_of_nations, commonwealth_realms_org]
    
    new_zealand = CommonwealthRealm("NewZealand")
    new_zealand.label = "New Zealand"
    new_zealand.isInRegion = oceania
    new_zealand.hasHeadOfState = queen_elizabeth_ii
    new_zealand.isMemberOf = [commonwealth_of_nations, commonwealth_realms_org]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
