"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. What is the veto power in the context of the United Nations Security Council?
2. Which countries are the permanent members of the UN Security Council?
3. Which members of the UN Security Council possess veto power?
4. On what types of resolutions can a permanent member exercise veto power?
5. Can a permanent member veto a procedural vote in the UN Security Council?
6. Who determines whether a vote is procedural or substantive?
7. Does a permanent member’s abstention prevent a draft resolution from being adopted?
8. Does a permanent member’s absence prevent a draft resolution from being adopted?
9. Can a permanent member block the selection of the UN Secretary-General?
10. Is a formal veto required to block the selection of a Secretary-General?
11. Why is a formal veto unnecessary in the selection of a Secretary-General?
12. Which five governments possess the unconditional veto?
13. What criticisms have been made against the UN Security Council veto power?
14. Why do critics consider the veto power undemocratic?
15. How do critics relate veto power to international inaction on war crimes?
16. How do critics relate veto power to international inaction on crimes against humanity?
17. Why did the United States refuse to join the United Nations in 1945 unless it was granted a veto?
18. How did the absence of the United States from the League of Nations affect that organization?
19. What arguments do supporters make in favor of veto power?
20. How is veto power said to promote international stability?
21. How is veto power considered a check against military interventions?
22. How is veto power viewed as a safeguard against U.S. domination?
23. Under what conditions can a substantive resolution be blocked in the Security Council?
24. What is the relationship between permanent membership in the Security Council and veto power?
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
    Event, NonAgentiveSocialObject, Society, State, TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class InternationalOrganization(Society):
        pass


    class SecurityCouncil(InternationalOrganization):
        pass


    class Country(Society):
        pass


    class PermanentMemberState(Country):
        pass


    class InstitutionalPower(NonAgentiveSocialObject):
        pass


    class VetoPower(InstitutionalPower):
        pass


    class UnconditionalVetoPower(VetoPower):
        pass


    class Resolution(NonAgentiveSocialObject):
        pass


    class DraftResolution(Resolution):
        pass


    class SubstantiveResolution(DraftResolution):
        pass


    class Vote(Event):
        pass


    class ProceduralVote(Vote):
        pass


    class BehindClosedDoorsVote(Vote):
        pass


    class SelectionProcess(Event):
        pass


    class SecretaryGeneralSelection(SelectionProcess):
        pass


    class Office(NonAgentiveSocialObject):
        pass


    class SecretaryGeneralOffice(Office):
        pass


    class FormalVeto(NonAgentiveSocialObject):
        pass


    class PoliticalAssessment(NonAgentiveSocialObject):
        pass


    class PoliticalOutcome(NonAgentiveSocialObject):
        pass


    class CrimeCategory(NonAgentiveSocialObject):
        pass


    class CouncilMemberStatus(State):
        pass


    class PermanentMemberAbstention(CouncilMemberStatus):
        pass


    class PermanentMemberAbsence(CouncilMemberStatus):
        pass


    class JoinRefusal(Event):
        pass


    class OrganizationalAbsence(State):
        pass


    class CalendarYear(TimeInterval):
        pass


    class permanentMemberOf(ObjectProperty):
        domain = [PermanentMemberState]
        range = [SecurityCouncil]


    class hasInstitutionalPower(ObjectProperty):
        domain = [SecurityCouncil]
        range = [InstitutionalPower]


    class holdsPower(ObjectProperty):
        domain = [PermanentMemberState]
        range = [InstitutionalPower]


    class appliesTo(ObjectProperty):
        domain = [VetoPower]
        range = [Resolution]


    class doesNotApplyTo(ObjectProperty):
        domain = [VetoPower]
        range = [Vote]


    class canBeVetoedBy(ObjectProperty):
        domain = [SubstantiveResolution]
        range = [PermanentMemberState]


    class classificationDeterminedBy(ObjectProperty):
        domain = [ProceduralVote]
        range = [PermanentMemberState]


    class canBeAdoptedDespite(ObjectProperty):
        domain = [DraftResolution]
        range = [CouncilMemberStatus]


    class selectsOffice(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [SecretaryGeneralOffice]


    class canBeBlockedBy(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [PermanentMemberState]


    class carriedOutBy(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [BehindClosedDoorsVote]


    class doesNotRequire(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [FormalVeto]


    class performedBy(ObjectProperty):
        domain = [JoinRefusal, OrganizationalAbsence]
        range = [Country]


    class towardOrganization(ObjectProperty):
        domain = [JoinRefusal, OrganizationalAbsence]
        range = [InternationalOrganization]


    class motivatedBy(ObjectProperty):
        domain = [JoinRefusal]
        range = [InstitutionalPower]


    class contributedToIneffectivenessOf(ObjectProperty):
        domain = [OrganizationalAbsence]
        range = [InternationalOrganization]


    class criticizedAs(ObjectProperty):
        domain = [VetoPower]
        range = [PoliticalAssessment]


    class criticizedForCausingInactionOn(ObjectProperty):
        domain = [VetoPower]
        range = [CrimeCategory]


    class seenAsPromoting(ObjectProperty):
        domain = [VetoPower]
        range = [PoliticalOutcome]


    class seenAsCheckingAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [PoliticalOutcome]


    class seenAsSafeguardingAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [PoliticalOutcome]


    SecurityCouncil.is_a.append(partOf.some(InternationalOrganization))
    PermanentMemberState.is_a.append(permanentMemberOf.some(SecurityCouncil))
    PermanentMemberState.is_a.append(holdsPower.some(UnconditionalVetoPower))
    DraftResolution.is_a.append(canBeAdoptedDespite.some(PermanentMemberAbstention))
    DraftResolution.is_a.append(canBeAdoptedDespite.some(PermanentMemberAbsence))
    SubstantiveResolution.is_a.append(canBeVetoedBy.some(PermanentMemberState))
    ProceduralVote.is_a.append(classificationDeterminedBy.some(PermanentMemberState))
    SecretaryGeneralSelection.is_a.append(selectsOffice.some(SecretaryGeneralOffice))
    SecretaryGeneralSelection.is_a.append(canBeBlockedBy.some(PermanentMemberState))
    SecretaryGeneralSelection.is_a.append(carriedOutBy.some(BehindClosedDoorsVote))
    SecretaryGeneralSelection.is_a.append(doesNotRequire.some(FormalVeto))
    UnconditionalVetoPower.is_a.append(appliesTo.some(SubstantiveResolution))
    UnconditionalVetoPower.is_a.append(doesNotApplyTo.some(ProceduralVote))
    JoinRefusal.is_a.append(performedBy.some(Country))
    JoinRefusal.is_a.append(towardOrganization.some(InternationalOrganization))
    JoinRefusal.is_a.append(motivatedBy.some(InstitutionalPower))
    OrganizationalAbsence.is_a.append(performedBy.some(Country))
    OrganizationalAbsence.is_a.append(towardOrganization.some(InternationalOrganization))
    OrganizationalAbsence.is_a.append(contributedToIneffectivenessOf.some(InternationalOrganization))

    unitedNations = InternationalOrganization("UnitedNations")
    unitedNations.label = "United Nations"

    unitedNationsSecurityCouncil = SecurityCouncil("UnitedNationsSecurityCouncil")
    unitedNationsSecurityCouncil.label = [
        "United Nations Security Council",
        "UN Security Council",
    ]
    unitedNationsSecurityCouncil.partOf.append(unitedNations)

    china = PermanentMemberState("China")
    china.label = "China"
    china.permanentMemberOf.append(unitedNationsSecurityCouncil)

    france = PermanentMemberState("France")
    france.label = "France"
    france.permanentMemberOf.append(unitedNationsSecurityCouncil)

    russia = PermanentMemberState("Russia")
    russia.label = "Russia"
    russia.permanentMemberOf.append(unitedNationsSecurityCouncil)

    unitedKingdom = PermanentMemberState("UnitedKingdom")
    unitedKingdom.label = "United Kingdom"
    unitedKingdom.permanentMemberOf.append(unitedNationsSecurityCouncil)

    unitedStates = PermanentMemberState("UnitedStates")
    unitedStates.label = ["United States", "U.S."]
    unitedStates.permanentMemberOf.append(unitedNationsSecurityCouncil)

    unitedNationsSecurityCouncilVetoPower = UnconditionalVetoPower(
        "UnitedNationsSecurityCouncilVetoPower"
    )
    unitedNationsSecurityCouncilVetoPower.label = (
        'United Nations Security Council " veto power "'
    )
    unitedNationsSecurityCouncil.hasInstitutionalPower.append(
        unitedNationsSecurityCouncilVetoPower
    )

    for permanentMember in [china, france, russia, unitedKingdom, unitedStates]:
        permanentMember.holdsPower.append(unitedNationsSecurityCouncilVetoPower)

    secretaryGeneral = SecretaryGeneralOffice("SecretaryGeneralOfficeInstance")
    secretaryGeneral.label = "Secretary - General"

    secretaryGeneralSelection = SecretaryGeneralSelection(
        "SelectionOfSecretaryGeneral"
    )
    secretaryGeneralSelection.label = "selection of a Secretary - General"
    secretaryGeneralSelection.selectsOffice.append(secretaryGeneral)
    secretaryGeneralSelection.canBeBlockedBy.extend(
        [china, france, russia, unitedKingdom, unitedStates]
    )

    formalVeto = FormalVeto("FormalVetoInstance")
    formalVeto.label = "formal veto"
    secretaryGeneralSelection.doesNotRequire.append(formalVeto)

    behindClosedDoorsVote = BehindClosedDoorsVote(
        "VoteTakenBehindClosedDoors"
    )
    behindClosedDoorsVote.label = "the vote is taken behind closed doors"
    secretaryGeneralSelection.carriedOutBy.append(behindClosedDoorsVote)

    mostUndemocraticCharacter = PoliticalAssessment(
        "MostUndemocraticCharacterOfUN"
    )
    mostUndemocraticCharacter.label = "the most undemocratic character of the UN"
    unitedNationsSecurityCouncilVetoPower.criticizedAs.append(
        mostUndemocraticCharacter
    )

    warCrimes = CrimeCategory("WarCrimes")
    warCrimes.label = "war crimes"
    crimesAgainstHumanity = CrimeCategory("CrimesAgainstHumanity")
    crimesAgainstHumanity.label = "crimes against humanity"
    unitedNationsSecurityCouncilVetoPower.criticizedForCausingInactionOn.extend(
        [warCrimes, crimesAgainstHumanity]
    )

    internationalStability = PoliticalOutcome("InternationalStability")
    internationalStability.label = "international stability"
    unitedNationsSecurityCouncilVetoPower.seenAsPromoting.append(
        internationalStability
    )

    militaryInterventions = PoliticalOutcome("MilitaryInterventions")
    militaryInterventions.label = "military interventions"
    unitedNationsSecurityCouncilVetoPower.seenAsCheckingAgainst.append(
        militaryInterventions
    )

    unitedStatesDomination = PoliticalOutcome("USDomination")
    unitedStatesDomination.label = "U.S. domination"
    unitedNationsSecurityCouncilVetoPower.seenAsSafeguardingAgainst.append(
        unitedStatesDomination
    )

    year1945 = CalendarYear("Year1945")
    year1945.label = "1945"

    unitedStatesJoinRefusal = JoinRefusal(
        "UnitedStatesRefusedToJoinTheUnitedNationsIn1945"
    )
    unitedStatesJoinRefusal.label = (
        "United States refused to join the United Nations in 1945"
    )
    unitedStatesJoinRefusal.performedBy.append(unitedStates)
    unitedStatesJoinRefusal.towardOrganization.append(unitedNations)
    unitedStatesJoinRefusal.motivatedBy.append(
        unitedNationsSecurityCouncilVetoPower
    )
    unitedStatesJoinRefusal.temporallyLocatedAt = year1945

    leagueOfNations = InternationalOrganization("LeagueOfNations")
    leagueOfNations.label = "League of Nations"

    absenceOfUnitedStatesFromLeagueOfNations = OrganizationalAbsence(
        "AbsenceOfUnitedStatesFromLeagueOfNations"
    )
    absenceOfUnitedStatesFromLeagueOfNations.label = (
        "absence of the United States from the League of Nations"
    )
    absenceOfUnitedStatesFromLeagueOfNations.performedBy.append(unitedStates)
    absenceOfUnitedStatesFromLeagueOfNations.towardOrganization.append(
        leagueOfNations
    )
    absenceOfUnitedStatesFromLeagueOfNations.contributedToIneffectivenessOf.append(
        leagueOfNations
    )


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
