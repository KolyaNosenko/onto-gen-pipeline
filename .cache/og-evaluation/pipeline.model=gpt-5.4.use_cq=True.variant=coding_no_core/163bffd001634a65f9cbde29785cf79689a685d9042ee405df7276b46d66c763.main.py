"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. What is the veto power in the United Nations Security Council?
2. Which countries are the permanent members of the UN Security Council?
3. Which members of the UN Security Council have veto power?
4. On what type of resolutions can a permanent member exercise veto power?
5. Can a permanent member veto a substantive resolution?
6. Does veto power apply to procedural votes in the UN Security Council?
7. Who determines whether a vote is procedural or substantive?
8. Does a permanent member’s abstention prevent a draft resolution from being adopted?
9. Does a permanent member’s absence prevent a draft resolution from being adopted?
10. Under what conditions can a draft resolution still be adopted despite a permanent member not voting in favor?
11. Can a permanent member block the selection of a UN Secretary-General?
12. Is a formal veto required to block the selection of a Secretary-General?
13. How is the vote for selecting the UN Secretary-General conducted?
14. Why is a formal veto unnecessary in the selection of the Secretary-General?
15. Which feature of the UN Security Council has been criticized as undemocratic?
16. What criticisms have been made of the veto power?
17. How do critics relate veto power to international inaction on war crimes?
18. How do critics relate veto power to international inaction on crimes against humanity?
19. Why did the United States refuse to join the United Nations in 1945 without a veto?
20. What reason is given for the ineffectiveness of the League of Nations?
21. How do supporters justify the existence of veto power?
22. In what way is veto power considered a promoter of international stability?
23. How is veto power viewed as a check against military interventions?
24. How is veto power described as a safeguard against U.S. domination?
25. What is the relationship between permanent membership and veto power in the UN Security Council?
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
    class Organization(Thing):
        pass

    class InternationalOrganization(Organization):
        pass

    class Council(Organization):
        pass

    class Country(Thing):
        pass

    class PermanentMemberCountry(Country):
        pass

    class Power(Thing):
        pass

    class VetoPowerRight(Power):
        pass

    class UnconditionalVetoPower(VetoPowerRight):
        pass

    class Resolution(Thing):
        pass

    class DraftResolution(Resolution):
        pass

    class SubstantiveResolution(DraftResolution):
        pass

    class Vote(Thing):
        pass

    class ProceduralVote(Vote):
        pass

    class BehindClosedDoorsVote(Vote):
        pass

    class SelectionProcess(Thing):
        pass

    class NonFormalVetoSelection(SelectionProcess):
        pass

    class SecretaryGeneralSelection(NonFormalVetoSelection):
        pass

    class Office(Thing):
        pass

    class SecretaryGeneralOffice(Office):
        pass

    class TimePoint(Thing):
        pass

    class Year(TimePoint):
        pass

    class Criticism(Thing):
        pass

    class UndemocraticCharacteristic(Criticism):
        pass

    class InternationalInaction(Thing):
        pass

    class InternationalInactionOnWarCrimes(InternationalInaction):
        pass

    class InternationalInactionOnCrimesAgainstHumanity(InternationalInaction):
        pass

    class WarCrime(Thing):
        pass

    class CrimeAgainstHumanity(Thing):
        pass

    class SupportiveEffect(Thing):
        pass

    class InternationalStability(SupportiveEffect):
        pass

    class MilitaryIntervention(Thing):
        pass

    class USDomination(Thing):
        pass

    class partOfOrganization(ObjectProperty, TransitiveProperty):
        domain = [Organization]
        range = [Organization]

    class hasPermanentMember(ObjectProperty):
        domain = [Council]
        range = [PermanentMemberCountry]

    class permanentMemberOf(ObjectProperty):
        domain = [PermanentMemberCountry]
        range = [Council]

    class hasVetoPower(ObjectProperty):
        domain = [Country]
        range = [VetoPowerRight]

    class heldBy(ObjectProperty):
        domain = [VetoPowerRight]
        range = [PermanentMemberCountry]

    class canVeto(ObjectProperty):
        domain = [PermanentMemberCountry]
        range = [Resolution]

    class appliesToResolutionType(ObjectProperty):
        domain = [VetoPowerRight]
        range = [Resolution]

    class doesNotApplyToVoteType(ObjectProperty):
        domain = [VetoPowerRight]
        range = [Vote]

    class classificationDeterminedBy(ObjectProperty):
        domain = [Vote]
        range = [PermanentMemberCountry]

    class canBeAdoptedDespiteAbstentionBy(ObjectProperty):
        domain = [DraftResolution]
        range = [PermanentMemberCountry]

    class canBeAdoptedDespiteAbsenceBy(ObjectProperty):
        domain = [DraftResolution]
        range = [PermanentMemberCountry]

    class canBlockSelectionOf(ObjectProperty):
        domain = [PermanentMemberCountry]
        range = [SecretaryGeneralSelection]

    class canBeBlockedBy(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [PermanentMemberCountry]

    class selectsOffice(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [SecretaryGeneralOffice]

    class conductedByVoteType(ObjectProperty):
        domain = [SelectionProcess]
        range = [Vote]

    class criticizedAs(ObjectProperty):
        domain = [VetoPowerRight]
        range = [Criticism]

    class causes(ObjectProperty):
        domain = [VetoPowerRight]
        range = [InternationalInaction]

    class concerns(ObjectProperty):
        domain = [InternationalInaction]
        range = [Thing]

    class promotes(ObjectProperty):
        domain = [VetoPowerRight]
        range = [InternationalStability]

    class checksAgainst(ObjectProperty):
        domain = [VetoPowerRight]
        range = [MilitaryIntervention]

    class safeguardsAgainst(ObjectProperty):
        domain = [VetoPowerRight]
        range = [USDomination]

    class refusedToJoin(ObjectProperty):
        domain = [Country]
        range = [InternationalOrganization]

    class requiredForJoining(ObjectProperty):
        domain = [Country]
        range = [Power]

    class refusalOccurredIn(ObjectProperty, FunctionalProperty):
        domain = [Country]
        range = [Year]

    class absenceFromContributedToIneffectivenessOf(ObjectProperty):
        domain = [Country]
        range = [InternationalOrganization]

    PermanentMemberCountry.is_a.append(permanentMemberOf.some(Council))
    PermanentMemberCountry.is_a.append(hasVetoPower.some(VetoPowerRight))
    PermanentMemberCountry.is_a.append(canVeto.some(SubstantiveResolution))
    PermanentMemberCountry.is_a.append(canVeto.only(SubstantiveResolution))
    PermanentMemberCountry.is_a.append(canBlockSelectionOf.some(SecretaryGeneralSelection))

    VetoPowerRight.is_a.append(heldBy.only(PermanentMemberCountry))
    VetoPowerRight.is_a.append(appliesToResolutionType.some(SubstantiveResolution))
    VetoPowerRight.is_a.append(appliesToResolutionType.only(SubstantiveResolution))
    VetoPowerRight.is_a.append(doesNotApplyToVoteType.some(ProceduralVote))
    VetoPowerRight.is_a.append(doesNotApplyToVoteType.only(ProceduralVote))
    VetoPowerRight.is_a.append(criticizedAs.some(UndemocraticCharacteristic))
    VetoPowerRight.is_a.append(causes.some(InternationalInactionOnWarCrimes))
    VetoPowerRight.is_a.append(causes.some(InternationalInactionOnCrimesAgainstHumanity))
    VetoPowerRight.is_a.append(promotes.some(InternationalStability))
    VetoPowerRight.is_a.append(checksAgainst.some(MilitaryIntervention))
    VetoPowerRight.is_a.append(safeguardsAgainst.some(USDomination))

    ProceduralVote.is_a.append(classificationDeterminedBy.some(PermanentMemberCountry))
    ProceduralVote.is_a.append(classificationDeterminedBy.only(PermanentMemberCountry))

    DraftResolution.is_a.append(canBeAdoptedDespiteAbstentionBy.some(PermanentMemberCountry))
    DraftResolution.is_a.append(canBeAdoptedDespiteAbsenceBy.some(PermanentMemberCountry))

    SecretaryGeneralSelection.is_a.append(canBeBlockedBy.some(PermanentMemberCountry))
    SecretaryGeneralSelection.is_a.append(selectsOffice.some(SecretaryGeneralOffice))
    SecretaryGeneralSelection.is_a.append(conductedByVoteType.some(BehindClosedDoorsVote))

    InternationalInactionOnWarCrimes.is_a.append(concerns.some(WarCrime))
    InternationalInactionOnCrimesAgainstHumanity.is_a.append(concerns.some(CrimeAgainstHumanity))

    UnitedNations = InternationalOrganization("UnitedNations")
    UnitedNations.label = "United Nations"

    UnitedNationsSecurityCouncil = Council("UnitedNationsSecurityCouncil")
    UnitedNationsSecurityCouncil.label = [
        "United Nations Security Council",
        "UN Security Council",
    ]
    UnitedNationsSecurityCouncil.partOfOrganization = [UnitedNations]

    China = PermanentMemberCountry("China")
    China.label = "China"
    China.permanentMemberOf = [UnitedNationsSecurityCouncil]

    France = PermanentMemberCountry("France")
    France.label = "France"
    France.permanentMemberOf = [UnitedNationsSecurityCouncil]

    Russia = PermanentMemberCountry("Russia")
    Russia.label = "Russia"
    Russia.permanentMemberOf = [UnitedNationsSecurityCouncil]

    UnitedKingdom = PermanentMemberCountry("UnitedKingdom")
    UnitedKingdom.label = "United Kingdom"
    UnitedKingdom.permanentMemberOf = [UnitedNationsSecurityCouncil]

    UnitedStates = PermanentMemberCountry("UnitedStates")
    UnitedStates.label = ["United States", "U.S."]
    UnitedStates.permanentMemberOf = [UnitedNationsSecurityCouncil]

    UnitedNationsSecurityCouncil.hasPermanentMember = [
        China,
        France,
        Russia,
        UnitedKingdom,
        UnitedStates,
    ]

    VetoPower = UnconditionalVetoPower("SecurityCouncilVetoPower")
    VetoPower.label = "veto power"
    VetoPower.heldBy = [China, France, Russia, UnitedKingdom, UnitedStates]

    China.hasVetoPower = [VetoPower]
    France.hasVetoPower = [VetoPower]
    Russia.hasVetoPower = [VetoPower]
    UnitedKingdom.hasVetoPower = [VetoPower]
    UnitedStates.hasVetoPower = [VetoPower]

    LeagueOfNations = InternationalOrganization("LeagueOfNations")
    LeagueOfNations.label = "League of Nations"

    Year1945 = Year("Year1945")
    Year1945.label = "1945"

    UnitedStates.refusedToJoin = [UnitedNations]
    UnitedStates.requiredForJoining = [VetoPower]
    UnitedStates.refusalOccurredIn = Year1945
    UnitedStates.absenceFromContributedToIneffectivenessOf = [LeagueOfNations]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
