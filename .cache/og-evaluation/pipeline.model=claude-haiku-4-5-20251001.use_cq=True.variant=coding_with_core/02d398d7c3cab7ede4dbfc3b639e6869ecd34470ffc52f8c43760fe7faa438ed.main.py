"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. Which countries have veto power in the UN Security Council?
2. What types of resolutions can be vetoed by permanent members?
3. Does a permanent member's abstention prevent the adoption of a draft resolution?
4. Does veto power apply to procedural votes?
5. Can a permanent member block the selection of a Secretary-General?
6. What are the criticisms of the UN veto power system?
7. What role did veto power play in the United States' decision to join the United Nations?
8. How did the absence of the United States affect the League of Nations?
9. What arguments do supporters make in favor of veto power?
10. Is veto power considered a check against military interventions?
11. How many permanent members possess veto power in the UN Security Council?
12. What is the difference between substantive and procedural votes regarding veto power?
13. Do absent permanent members prevent resolution adoption through their absence?
14. Is the UN veto power considered democratic or undemocratic?
15. What connection exists between veto power and international inaction on war crimes?
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
from og_sandbox_with_core.core.entities import (
    SocialAgent, Society, NonPhysicalObject, Event, Stative, AbstractQuality
)

# TODO (optional): import the core properties you actually subclass.
# (not used in this domain)


with core:
    # ============== ENTITY CLASSES ==============
    
    class Country(SocialAgent):
        """A sovereign nation state"""
        pass
    
    class UN(Society):
        """The United Nations organization"""
        pass
    
    class UNSecurityCouncil(Society):
        """The United Nations Security Council"""
        pass
    
    class LeagueOfNations(Society):
        """The League of Nations organization"""
        pass
    
    class VetoPower(AbstractQuality):
        """The power to veto resolutions in the UN Security Council"""
        pass
    
    class Resolution(NonPhysicalObject):
        """A resolution voted on"""
        pass
    
    class SubstantiveResolution(Resolution):
        """A substantive resolution that can be vetoed"""
        pass
    
    class ProceduralVote(Resolution):
        """A procedural vote that cannot be vetoed"""
        pass
    
    class WarCrime(Event):
        """A war crime"""
        pass
    
    class CrimeAgainstHumanity(Event):
        """A crime against humanity"""
        pass
    
    class MilitaryIntervention(Event):
        """A military intervention"""
        pass
    
    class InternationalInaction(Stative):
        """Inaction by the international community"""
        pass
    
    class SecretaryGeneralSelection(NonPhysicalObject):
        """The selection of a Secretary-General"""
        pass
    
    # ============== OBJECT PROPERTIES ==============
    
    class isPermanentMemberOf(ObjectProperty):
        """A country is a permanent member of the UN Security Council"""
        domain = [Country]
        range = [UNSecurityCouncil]
    
    class possessesVetoPower(ObjectProperty):
        """A country possesses veto power"""
        domain = [Country]
        range = [VetoPower]
    
    class causesInaction(ObjectProperty):
        """Veto power causes international inaction"""
        domain = [VetoPower]
        range = [InternationalInaction]
    
    class representsCheckAgainst(ObjectProperty):
        """Veto power represents a check against something"""
        domain = [VetoPower]
        range = [MilitaryIntervention]
    
    class canBlockSelection(ObjectProperty):
        """A country can block the selection of something"""
        domain = [Country]
        range = [NonPhysicalObject]
    
    class wasRequiredFor(ObjectProperty):
        """Something was required for a country"""
        domain = [VetoPower]
        range = [Country]
    
    class contributedToIneffectiveness(ObjectProperty):
        """A country's absence contributed to ineffectiveness of an organization"""
        domain = [Country]
        range = [Society]
    
    # ============== DATA PROPERTIES ==============
    
    class isConsideredUndemocratic(DataProperty, FunctionalProperty):
        """Whether something is considered undemocratic"""
        domain = [VetoPower]
        range = [bool]
    
    class promotesStability(DataProperty, FunctionalProperty):
        """Whether something promotes stability"""
        domain = [VetoPower]
        range = [bool]
    
    # ============== INSTANCES ==============
    
    # Countries (Permanent Members)
    china = Country("China")
    china.label = "China"
    
    france = Country("France")
    france.label = "France"
    
    russia = Country("Russia")
    russia.label = "Russia"
    
    unitedKingdom = Country("UnitedKingdom")
    unitedKingdom.label = "United Kingdom"
    
    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"
    
    # Organizations
    un = UN("UnitedNations")
    un.label = "United Nations"
    
    unSecurityCouncil = UNSecurityCouncil("UNSecurityCouncilInstance")
    unSecurityCouncil.label = "United Nations Security Council"
    
    leagueOfNations = LeagueOfNations("LeagueOfNationsInstance")
    leagueOfNations.label = "League of Nations"
    
    # Veto Power
    vetoPower = VetoPower("VetoPowerInstance")
    vetoPower.label = "veto power"
    
    # Secretary-General Selection
    secretaryGeneralSelection = SecretaryGeneralSelection("SecretaryGeneralSelectionInstance")
    secretaryGeneralSelection.label = "Selection of Secretary-General"
    
    # International Inaction
    internationalInaction = InternationalInaction("InternationalInactionInstance")
    internationalInaction.label = "International inaction on war crimes and crimes against humanity"
    
    # ============== RELATIONSHIPS ==============
    
    # Countries are permanent members of UN Security Council
    china.isPermanentMemberOf.append(unSecurityCouncil)
    france.isPermanentMemberOf.append(unSecurityCouncil)
    russia.isPermanentMemberOf.append(unSecurityCouncil)
    unitedKingdom.isPermanentMemberOf.append(unSecurityCouncil)
    unitedStates.isPermanentMemberOf.append(unSecurityCouncil)
    
    # Countries possess veto power
    china.possessesVetoPower.append(vetoPower)
    france.possessesVetoPower.append(vetoPower)
    russia.possessesVetoPower.append(vetoPower)
    unitedKingdom.possessesVetoPower.append(vetoPower)
    unitedStates.possessesVetoPower.append(vetoPower)
    
    # Veto power characteristics
    vetoPower.isConsideredUndemocratic = True
    vetoPower.promotesStability = True
    
    # Veto power effects
    vetoPower.causesInaction.append(internationalInaction)
    
    # Veto is a check against military interventions
    militaryIntervention = MilitaryIntervention("MilitaryInterventionInstance")
    militaryIntervention.label = "Military interventions"
    vetoPower.representsCheckAgainst.append(militaryIntervention)
    
    # Permanent members can block Secretary-General selection
    for country in [china, france, russia, unitedKingdom, unitedStates]:
        country.canBlockSelection.append(secretaryGeneralSelection)
    
    # Veto power was required for US to join UN
    vetoPower.wasRequiredFor.append(unitedStates)
    
    # US absence from League of Nations contributed to its ineffectiveness
    unitedStates.contributedToIneffectiveness.append(leagueOfNations)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
