"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. Which countries are the permanent members of the United Nations Security Council?
2. What does the UN Security Council veto power refer to?
3. Which kinds of Security Council resolutions can a permanent member veto?
4. Do permanent members have veto power over procedural votes?
5. Does a permanent member’s abstention prevent a draft resolution from being adopted?
6. Does a permanent member’s absence prevent a draft resolution from being adopted?
7. Can a permanent member block the selection of a Secretary-General?
8. Is a formal veto necessary to block the selection of a Secretary-General?
9. How is the vote for selecting a Secretary-General taken?
10. Who determines whether a vote is procedural or substantive?
11. How many governments possess the unconditional veto in the UN Security Council?
12. How is the UN Security Council veto power viewed by critics?
13. What do critics claim is the main cause of international inaction on war crimes and crimes against humanity?
14. Why did the United States refuse to join the United Nations in 1945?
15. What effect did the absence of the United States from the League of Nations have?
16. How do supporters of the veto power justify it?
17. What role does the veto power play in promoting international stability?
18. How is the veto power considered a check against military interventions?
19. Why do supporters view the veto as a safeguard against U.S. domination?
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
    AbstractQuality,
    Event,
    SocialAgent,
    SocialObject,
    Society,
    State,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class Country(Society):
        pass

    class InternationalOrganization(SocialObject):
        pass

    class Council(InternationalOrganization):
        pass

    class SecurityCouncil(Council):
        pass

    class Power(SocialObject):
        pass

    class VetoPower(Power):
        pass

    class FormalVeto(Event):
        pass

    class Resolution(SocialObject):
        pass

    class SubstantiveResolution(Resolution):
        pass

    class DraftResolution(Resolution):
        pass

    class Vote(Event):
        pass

    class ProceduralVote(Vote):
        pass

    class Selection(Event):
        pass

    class SecretaryGeneralSelection(Selection):
        pass

    class ClosedDoorSituation(SocialObject):
        pass

    class Abstention(Event):
        pass

    class Absence(Event):
        pass

    class Crime(Event):
        pass

    class WarCrime(Crime):
        pass

    class CrimeAgainstHumanity(Crime):
        pass

    class InternationalInaction(State):
        pass

    class MilitaryIntervention(Event):
        pass

    class InternationalStability(State):
        pass

    class Domination(State):
        pass

    class Ineffectiveness(State):
        pass

    class UndemocraticCharacter(AbstractQuality):
        pass

    class SecretaryGeneral(SocialAgent):
        pass

    class Critic(SocialAgent):
        pass

    class Supporter(SocialAgent):
        pass

    class isPermanentMemberOf(ObjectProperty):
        domain = [Country]
        range = [SecurityCouncil]

    class possessesPower(ObjectProperty):
        domain = [Country]
        range = [VetoPower]

    class canVeto(ObjectProperty):
        domain = [Country]
        range = [SubstantiveResolution]

    class doesNotApplyTo(ObjectProperty):
        domain = [VetoPower]
        range = [ProceduralVote]

    class vetoes(ObjectProperty):
        domain = [VetoPower]
        range = [Resolution]

    class canBlockSelectionOf(ObjectProperty):
        domain = [Country]
        range = [SecretaryGeneralSelection]

    class doesNotRequire(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [FormalVeto]

    class doesNotPreventAdoptionOf(ObjectProperty):
        domain = [Abstention, Absence]
        range = [DraftResolution]

    class takenBehindClosedDoors(ObjectProperty):
        domain = [SecretaryGeneralSelection]
        range = [ClosedDoorSituation]

    class determinedBy(ObjectProperty):
        domain = [Vote]
        range = [Country]

    class performedBy(ObjectProperty):
        domain = [Event]
        range = [Country]

    class conditionedOn(ObjectProperty):
        domain = [Event]
        range = [VetoPower]

    class absentFrom(ObjectProperty):
        domain = [Absence]
        range = [InternationalOrganization]

    class contributedTo(ObjectProperty):
        domain = [Absence]
        range = [Ineffectiveness]

    class concerns(ObjectProperty):
        domain = [InternationalInaction]
        range = [Crime]

    class mainCauseOf(ObjectProperty):
        domain = [VetoPower]
        range = [InternationalInaction]

    class viewedAs(ObjectProperty):
        domain = [VetoPower]
        range = [UndemocraticCharacter]

    class characterOf(ObjectProperty):
        domain = [UndemocraticCharacter]
        range = [InternationalOrganization]

    class promotes(ObjectProperty):
        domain = [VetoPower]
        range = [InternationalStability]

    class checksAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [MilitaryIntervention]

    class safeguardsAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [Domination]

    class ineffectivenessOf(ObjectProperty):
        domain = [Ineffectiveness]
        range = [InternationalOrganization]

    Country.is_a.append(isPermanentMemberOf.some(SecurityCouncil))
    Country.is_a.append(possessesPower.some(VetoPower))
    Country.is_a.append(canVeto.some(SubstantiveResolution))
    Country.is_a.append(canBlockSelectionOf.some(SecretaryGeneralSelection))

    VetoPower.is_a.append(vetoes.some(SubstantiveResolution))
    VetoPower.is_a.append(doesNotApplyTo.some(ProceduralVote))
    VetoPower.is_a.append(mainCauseOf.some(InternationalInaction))
    VetoPower.is_a.append(viewedAs.some(UndemocraticCharacter))
    VetoPower.is_a.append(promotes.some(InternationalStability))
    VetoPower.is_a.append(checksAgainst.some(MilitaryIntervention))
    VetoPower.is_a.append(safeguardsAgainst.some(Domination))

    Abstention.is_a.append(doesNotPreventAdoptionOf.some(DraftResolution))
    Absence.is_a.append(doesNotPreventAdoptionOf.some(DraftResolution))
    SecretaryGeneralSelection.is_a.append(doesNotRequire.some(FormalVeto))
    SecretaryGeneralSelection.is_a.append(takenBehindClosedDoors.some(ClosedDoorSituation))
    ProceduralVote.is_a.append(determinedBy.some(Country))
    InternationalInaction.is_a.append(concerns.some(Crime))
    Ineffectiveness.is_a.append(ineffectivenessOf.some(InternationalOrganization))
    UndemocraticCharacter.is_a.append(characterOf.some(InternationalOrganization))

    UnitedNationsSecurityCouncil = SecurityCouncil("UnitedNationsSecurityCouncil")
    UnitedNationsSecurityCouncil.label = ["United Nations Security Council", "UN Security Council"]
    UnitedNations = InternationalOrganization("UnitedNations")
    UnitedNations.label = ["United Nations", "UN"]
    LeagueOfNations = InternationalOrganization("LeagueOfNations")
    LeagueOfNations.label = "League of Nations"
    China = Country("China")
    China.label = "China"
    France = Country("France")
    France.label = "France"
    Russia = Country("Russia")
    Russia.label = "Russia"
    UnitedKingdom = Country("UnitedKingdom")
    UnitedKingdom.label = "United Kingdom"
    UnitedStates = Country("UnitedStates")
    UnitedStates.label = ["United States", "U.S."]
    UnitedNationsSecurityCouncilVetoPower = VetoPower("UNSecurityCouncilVetoPower")
    UnitedNationsSecurityCouncilVetoPower.label = ["veto power", "unconditional veto"]
    SubstantiveResolutionMention = SubstantiveResolution("SubstantiveResolutionMention")
    SubstantiveResolutionMention.label = "substantive resolution"
    ProceduralVoteMention = ProceduralVote("ProceduralVoteMention")
    ProceduralVoteMention.label = "procedural votes"
    DraftResolutionMention = DraftResolution("DraftResolutionMention")
    DraftResolutionMention.label = "a draft resolution"
    SecretaryGeneralSelectionMention = SecretaryGeneralSelection("SecretaryGeneralSelectionMention")
    SecretaryGeneralSelectionMention.label = "the selection of a Secretary-General"
    FormalVetoMention = FormalVeto("FormalVetoMention")
    FormalVetoMention.label = "a formal veto"
    ClosedDoorsMention = ClosedDoorSituation("ClosedDoorsMention")
    ClosedDoorsMention.label = "behind closed doors"
    PermanentMemberAbstention = Abstention("PermanentMemberAbstention")
    PermanentMemberAbstention.label = "a permanent member's abstention"
    PermanentMemberAbsence = Absence("PermanentMemberAbsence")
    PermanentMemberAbsence.label = "a permanent member's absence"
    InternationalInactionOnWarCrimesAndCrimesAgainstHumanity = InternationalInaction("InternationalInactionOnWarCrimesAndCrimesAgainstHumanity")
    InternationalInactionOnWarCrimesAndCrimesAgainstHumanity.label = "international inaction on war crimes and crimes against humanity"
    WarCrimes = WarCrime("WarCrimes")
    WarCrimes.label = "war crimes"
    CrimesAgainstHumanity = CrimeAgainstHumanity("CrimesAgainstHumanity")
    CrimesAgainstHumanity.label = "crimes against humanity"
    MostUndemocraticCharacterOfUN = UndemocraticCharacter("MostUndemocraticCharacterOfUN")
    MostUndemocraticCharacterOfUN.label = "the most undemocratic character of the UN"
    InternationalStabilityClaim = InternationalStability("InternationalStabilityClaim")
    InternationalStabilityClaim.label = "international stability"
    MilitaryInterventionsClaim = MilitaryIntervention("MilitaryInterventionsClaim")
    MilitaryInterventionsClaim.label = "military interventions"
    USDominationClaim = Domination("USDominationClaim")
    USDominationClaim.label = "U.S. domination"
    UnitedStatesRefusalToJoinUnitedNationsIn1945 = Event("UnitedStatesRefusalToJoinUnitedNationsIn1945")
    UnitedStatesRefusalToJoinUnitedNationsIn1945.label = "the United States refused to join the United Nations in 1945 unless it was given a veto"
    Year1945 = TimeInterval("Year1945")
    Year1945.label = "1945"
    UnitedStatesAbsenceFromLeagueOfNations = Absence("UnitedStatesAbsenceFromLeagueOfNations")
    UnitedStatesAbsenceFromLeagueOfNations.label = "The absence of the United States from the League of Nations"
    LeagueOfNationsIneffectiveness = Ineffectiveness("LeagueOfNationsIneffectiveness")
    LeagueOfNationsIneffectiveness.label = "its ineffectiveness"

    UnitedNationsSecurityCouncil.partOf.append(UnitedNations)

    China.isPermanentMemberOf.append(UnitedNationsSecurityCouncil)
    France.isPermanentMemberOf.append(UnitedNationsSecurityCouncil)
    Russia.isPermanentMemberOf.append(UnitedNationsSecurityCouncil)
    UnitedKingdom.isPermanentMemberOf.append(UnitedNationsSecurityCouncil)
    UnitedStates.isPermanentMemberOf.append(UnitedNationsSecurityCouncil)

    China.possessesPower.append(UnitedNationsSecurityCouncilVetoPower)
    France.possessesPower.append(UnitedNationsSecurityCouncilVetoPower)
    Russia.possessesPower.append(UnitedNationsSecurityCouncilVetoPower)
    UnitedKingdom.possessesPower.append(UnitedNationsSecurityCouncilVetoPower)
    UnitedStates.possessesPower.append(UnitedNationsSecurityCouncilVetoPower)

    China.canVeto.append(SubstantiveResolutionMention)
    France.canVeto.append(SubstantiveResolutionMention)
    Russia.canVeto.append(SubstantiveResolutionMention)
    UnitedKingdom.canVeto.append(SubstantiveResolutionMention)
    UnitedStates.canVeto.append(SubstantiveResolutionMention)

    China.canBlockSelectionOf.append(SecretaryGeneralSelectionMention)
    France.canBlockSelectionOf.append(SecretaryGeneralSelectionMention)
    Russia.canBlockSelectionOf.append(SecretaryGeneralSelectionMention)
    UnitedKingdom.canBlockSelectionOf.append(SecretaryGeneralSelectionMention)
    UnitedStates.canBlockSelectionOf.append(SecretaryGeneralSelectionMention)

    UnitedNationsSecurityCouncilVetoPower.vetoes.append(SubstantiveResolutionMention)
    UnitedNationsSecurityCouncilVetoPower.doesNotApplyTo.append(ProceduralVoteMention)
    UnitedNationsSecurityCouncilVetoPower.mainCauseOf.append(InternationalInactionOnWarCrimesAndCrimesAgainstHumanity)
    UnitedNationsSecurityCouncilVetoPower.viewedAs.append(MostUndemocraticCharacterOfUN)
    UnitedNationsSecurityCouncilVetoPower.promotes.append(InternationalStabilityClaim)
    UnitedNationsSecurityCouncilVetoPower.checksAgainst.append(MilitaryInterventionsClaim)
    UnitedNationsSecurityCouncilVetoPower.safeguardsAgainst.append(USDominationClaim)

    InternationalInactionOnWarCrimesAndCrimesAgainstHumanity.concerns.append(WarCrimes)
    InternationalInactionOnWarCrimesAndCrimesAgainstHumanity.concerns.append(CrimesAgainstHumanity)
    MostUndemocraticCharacterOfUN.characterOf.append(UnitedNations)
    LeagueOfNationsIneffectiveness.ineffectivenessOf.append(LeagueOfNations)

    PermanentMemberAbstention.doesNotPreventAdoptionOf.append(DraftResolutionMention)
    PermanentMemberAbsence.doesNotPreventAdoptionOf.append(DraftResolutionMention)
    SecretaryGeneralSelectionMention.doesNotRequire.append(FormalVetoMention)
    SecretaryGeneralSelectionMention.takenBehindClosedDoors.append(ClosedDoorsMention)
    ProceduralVoteMention.determinedBy.extend([China, France, Russia, UnitedKingdom, UnitedStates])

    UnitedStatesRefusalToJoinUnitedNationsIn1945.performedBy.append(UnitedStates)
    UnitedStatesRefusalToJoinUnitedNationsIn1945.conditionedOn.append(UnitedNationsSecurityCouncilVetoPower)
    UnitedStatesRefusalToJoinUnitedNationsIn1945.temporallyLocatedAt = Year1945
    UnitedStatesAbsenceFromLeagueOfNations.performedBy.append(UnitedStates)
    UnitedStatesAbsenceFromLeagueOfNations.absentFrom.append(LeagueOfNations)
    UnitedStatesAbsenceFromLeagueOfNations.contributedTo.append(LeagueOfNationsIneffectiveness)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
