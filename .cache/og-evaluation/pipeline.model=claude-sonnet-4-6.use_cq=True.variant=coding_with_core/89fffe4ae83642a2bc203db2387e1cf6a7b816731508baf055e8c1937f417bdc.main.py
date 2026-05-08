"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. Which countries are permanent members of the UN Security Council?
2. What type of resolutions can permanent members of the UN Security Council veto?
3. Does a permanent member's abstention prevent a draft resolution from being adopted?
4. Does the veto power apply to procedural votes?
5. Who determines whether a vote is procedural or substantive?
6. Can a permanent member block the selection of a Secretary-General?
7. Is a formal veto required to block the selection of a Secretary-General?
8. What criticisms have been raised against the veto power?
9. What conditions did the United States set for joining the United Nations in 1945?
10. How did the absence of the United States affect the League of Nations?
11. What arguments do supporters of the veto power make in its favor?
12. What role does veto power play in relation to international stability?
13. What is the relationship between veto power and military interventions?
14. What crimes have critics associated with the negative effects of veto power?
15. How is the vote for the selection of a Secretary-General conducted?
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
    Society, SocialAgent, NonAgentiveSocialObject,
    Accomplishment, State, TimeInterval,
)


with core:
    # ── Entity classes ─────────────────────────────────────────────────────────

    class InternationalOrganisation(Society):
        pass

    class SecurityCouncil(InternationalOrganisation):
        pass

    class MemberState(Society):
        pass

    class PermanentMemberState(MemberState):
        pass

    class VetoPower(NonAgentiveSocialObject):
        pass

    class Resolution(NonAgentiveSocialObject):
        pass

    class SubstantiveResolution(Resolution):
        pass

    class DraftResolution(Resolution):
        pass

    class ProceduralVote(Accomplishment):
        pass

    class SecretaryGeneral(SocialAgent):
        pass

    class SecretaryGeneralSelection(Accomplishment):
        pass

    class MilitaryIntervention(Accomplishment):
        pass

    class WarCrime(Accomplishment):
        pass

    class CrimeAgainstHumanity(Accomplishment):
        pass

    class InternationalInaction(State):
        pass

    class InternationalStability(State):
        pass

    # ── Properties ─────────────────────────────────────────────────────────────

    class hasPermanentMember(ObjectProperty):
        domain = [SecurityCouncil]
        range  = [PermanentMemberState]

    class exercisedBy(ObjectProperty):
        domain = [VetoPower]
        range  = [PermanentMemberState]

    class vetoAppliesToResolutionType(ObjectProperty):
        domain = [VetoPower]
        range  = [SubstantiveResolution]

    class voteTypeDeterminedBy(ObjectProperty):
        domain = [ProceduralVote]
        range  = [PermanentMemberState]

    class canBlockSelection(ObjectProperty):
        domain = [PermanentMemberState]
        range  = [SecretaryGeneralSelection]

    class causesInactionOn(ObjectProperty):
        domain = [VetoPower]
        range  = [InternationalInaction]

    class actsAsCheckAgainst(ObjectProperty):
        domain = [VetoPower]
        range  = [MilitaryIntervention]

    class promotesInternationalStability(ObjectProperty):
        domain = [VetoPower]
        range  = [InternationalStability]

    class conditionForMembership(ObjectProperty):
        domain = [MemberState]
        range  = [NonAgentiveSocialObject]

    class absenceContributedToIneffectivenessOf(ObjectProperty):
        domain = [MemberState]
        range  = [InternationalOrganisation]

    class membershipGrantedIn(ObjectProperty):
        domain = [MemberState]
        range  = [TimeInterval]

    class conductedBehindClosedDoors(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralSelection]
        range  = [bool]

    class requiresFormalVeto(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralSelection]
        range  = [bool]

    class abstentionPreventsDraftResolutionAdoption(DataProperty, FunctionalProperty):
        domain = [VetoPower]
        range  = [bool]

    # ── Named individuals ──────────────────────────────────────────────────────

    china = PermanentMemberState("China")
    china.label = "China"

    france = PermanentMemberState("France")
    france.label = "France"

    russia = PermanentMemberState("Russia")
    russia.label = "Russia"

    unitedKingdom = PermanentMemberState("United_Kingdom")
    unitedKingdom.label = "United Kingdom"

    unitedStates = PermanentMemberState("United_States")
    unitedStates.label = "United States"

    unitedNations = InternationalOrganisation("United_Nations")
    unitedNations.label = "United Nations"

    unSecurityCouncil = SecurityCouncil("UN_Security_Council")
    unSecurityCouncil.label = "UN Security Council"

    leagueOfNations = InternationalOrganisation("League_of_Nations")
    leagueOfNations.label = "League of Nations"

    year1945 = TimeInterval("1945")
    year1945.label = "1945"

    unVetoPower = VetoPower("UN_Security_Council_veto_power")
    unVetoPower.label = "UN Security Council veto power"

    sgSelection = SecretaryGeneralSelection("UN_Secretary_General_Selection")
    sgSelection.label = "UN Secretary-General Selection"
    sgSelection.conductedBehindClosedDoors = True
    sgSelection.requiresFormalVeto = False

    unSecurityCouncil.hasPermanentMember.append(china)
    unSecurityCouncil.hasPermanentMember.append(france)
    unSecurityCouncil.hasPermanentMember.append(russia)
    unSecurityCouncil.hasPermanentMember.append(unitedKingdom)
    unSecurityCouncil.hasPermanentMember.append(unitedStates)

    unVetoPower.exercisedBy.append(china)
    unVetoPower.exercisedBy.append(france)
    unVetoPower.exercisedBy.append(russia)
    unVetoPower.exercisedBy.append(unitedKingdom)
    unVetoPower.exercisedBy.append(unitedStates)

    unVetoPower.abstentionPreventsDraftResolutionAdoption = False

    unitedStates.conditionForMembership.append(unVetoPower)
    unitedStates.absenceContributedToIneffectivenessOf.append(leagueOfNations)
    unitedStates.membershipGrantedIn.append(year1945)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
