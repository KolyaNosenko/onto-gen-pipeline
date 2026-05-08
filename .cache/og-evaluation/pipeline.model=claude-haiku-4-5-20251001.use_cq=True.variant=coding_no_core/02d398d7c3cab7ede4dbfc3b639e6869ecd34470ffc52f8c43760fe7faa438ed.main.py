"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. Which countries are permanent members of the UN Security Council?

2. What types of resolutions can permanent members veto?

3. Does a permanent member's abstention prevent a draft resolution from being adopted?

4. To which votes does veto power not apply?

5. Can permanent members block the selection of a Secretary-General?

6. What are the criticisms of the UN Security Council veto power?

7. Why did the United States require veto power to join the United Nations?

8. What role did the absence of the United States play in the League of Nations?

9. What arguments do supporters make in favor of veto power?

10. Is veto power applied to procedural votes?

11. Who determines whether a vote is procedural or substantive?

12. What is considered the most undemocratic character of the UN according to critics?
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
    # Entity classes
    class Country(Thing):
        pass
    
    class Organization(Thing):
        pass
    
    class UnitedNations(Organization):
        pass
    
    class LeagueOfNations(Organization):
        pass
    
    class SecurityCouncil(Thing):
        pass
    
    class Vote(Thing):
        pass
    
    class SubstantiveVote(Vote):
        pass
    
    class ProceduralVote(Vote):
        pass
    
    class VetoPower(Thing):
        pass
    
    class Position(Thing):
        pass
    
    class SecretaryGeneralPosition(Position):
        pass
    
    class Criticism(Thing):
        pass
    
    class Argument(Thing):
        pass
    
    # Object Properties
    class hasPermanentMember(ObjectProperty):
        domain = [SecurityCouncil]
        range = [Country]
    
    class canVeto(ObjectProperty):
        domain = [Country]
        range = [SubstantiveVote]
    
    class canBlockSelection(ObjectProperty):
        domain = [Country]
        range = [SecretaryGeneralPosition]
    
    class determinedBy(ObjectProperty):
        domain = [Vote]
        range = [Country]
    
    class hasCriticism(ObjectProperty):
        domain = [VetoPower]
        range = [Criticism]
    
    class hasArgument(ObjectProperty):
        domain = [VetoPower]
        range = [Argument]
    
    class contributedToIneffectiveness(ObjectProperty):
        domain = [Country]
        range = [Organization]
    
    class associatedWith(ObjectProperty):
        domain = [VetoPower]
        range = [SecurityCouncil]
    
    # Data Properties
    class abstentionPreventsAdoption(DataProperty, FunctionalProperty):
        domain = [SecurityCouncil]
        range = [bool]
    
    class absencePreventsAdoption(DataProperty, FunctionalProperty):
        domain = [SecurityCouncil]
        range = [bool]
    
    class formalVetoRequired(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralPosition]
        range = [bool]
    
    # Instances - Countries (Permanent Members)
    china = Country("China")
    
    france = Country("France")
    
    russia = Country("Russia")
    
    unitedKingdom = Country("UnitedKingdom")
    unitedKingdom.label = "United Kingdom"
    
    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"
    
    # Instances - Organizations
    un = UnitedNations("UN_Instance")
    un.label = "United Nations"
    
    league = LeagueOfNations("LON_Instance")
    league.label = "League of Nations"
    
    # Instances - Security Council
    sc = SecurityCouncil("UNSecurityCouncil")
    sc.label = "UN Security Council"
    
    # Instances - Veto Power
    veto = VetoPower("VetoPowerInstance")
    
    # Instances - Secretary-General Position
    sgPosition = SecretaryGeneralPosition("SG_Position")
    sgPosition.label = "Secretary-General"
    
    # Relationships - UN Security Council and permanent members
    sc.hasPermanentMember = [china, france, russia, unitedKingdom, unitedStates]
    
    # Relationships - Permanent members can block Secretary-General selection
    china.canBlockSelection = [sgPosition]
    france.canBlockSelection = [sgPosition]
    russia.canBlockSelection = [sgPosition]
    unitedKingdom.canBlockSelection = [sgPosition]
    unitedStates.canBlockSelection = [sgPosition]
    
    # Data properties for Security Council
    sc.abstentionPreventsAdoption = False
    sc.absencePreventsAdoption = False
    
    # Data properties for Secretary-General position
    sgPosition.formalVetoRequired = False
    
    # Veto power association
    veto.associatedWith = [sc]
    
    # Instances - Criticisms
    undemocratic = Criticism("UndemocraticCharacter")
    undemocratic.label = "Most undemocratic character of the UN"
    
    inaction = Criticism("CausesInaction")
    inaction.label = "Main cause for international inaction on war crimes and crimes against humanity"
    
    veto.hasCriticism = [undemocratic, inaction]
    
    # Instances - Supporting Arguments
    stability = Argument("PromotesStability")
    stability.label = "Promoter of international stability"
    
    intervention = Argument("ChecksAgainstInterventions")
    intervention.label = "Check against military interventions"
    
    domination = Argument("SafeguardAgainstDomination")
    domination.label = "Safeguard against U.S. domination"
    
    veto.hasArgument = [stability, intervention, domination]
    
    # Historical fact - US absence from League of Nations
    unitedStates.contributedToIneffectiveness = [league]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
