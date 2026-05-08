"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

What is the veto power in the United Nations Security Council?

Which member states are the permanent members of the UN Security Council that possess veto power?

What kinds of Security Council resolutions can a permanent member veto?

Does a permanent member’s abstention prevent a draft resolution from being adopted?

Does a permanent member’s absence prevent a draft resolution from being adopted?

Does the veto power apply to procedural votes?

Who determines whether a Security Council vote is procedural?

Can a permanent member block the selection of a Secretary-General?

Is a formal veto required to block the selection of a Secretary-General?

Why is the veto power considered by critics to be undemocratic?

What is the claimed relationship between veto power and international inaction on war crimes and crimes against humanity?

Why did the United States refuse to join the United Nations in 1945 without veto power?

How did the absence of the United States from the League of Nations affect that organization?

What arguments do supporters give in favor of the veto power?

How is the veto power said to contribute to international stability?

How is the veto power described as a check against military interventions?

How is the veto power described as a safeguard against U.S. domination?
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
    class State(Thing):
        pass

    class Country(State):
        pass

    class MemberState(Country):
        pass

    class PermanentMember(MemberState):
        pass

    class Organization(Thing):
        pass

    class SecurityCouncil(Organization):
        pass

    class Resolution(Thing):
        pass

    class DraftResolution(Resolution):
        pass

    class SubstantiveResolution(Resolution):
        pass

    class Vote(Thing):
        pass

    class ProceduralVote(Vote):
        pass

    class Selection(Thing):
        pass

    class SecretaryGeneral(Thing):
        pass

    class SecretaryGeneralSelection(Selection):
        pass

    class Power(Thing):
        pass

    class VetoPower(Power):
        pass

    class Critic(Thing):
        pass

    class Supporter(Thing):
        pass

    class Inaction(Thing):
        pass

    class InternationalInaction(Inaction):
        pass

    class InternationalCrime(Thing):
        pass

    class WarCrime(InternationalCrime):
        pass

    class CrimeAgainstHumanity(InternationalCrime):
        pass

    class Stability(Thing):
        pass

    class InternationalStability(Stability):
        pass

    class Intervention(Thing):
        pass

    class MilitaryIntervention(Intervention):
        pass

    class Domination(Thing):
        pass

    class Character(Thing):
        pass

    class UndemocraticCharacter(Character):
        pass

    class Ineffectiveness(Thing):
        pass

    class Year(Thing):
        pass

    class Abstention(Thing):
        pass

    class Absence(Thing):
        pass

    class hasMember(ObjectProperty):
        domain = [SecurityCouncil]
        range = [MemberState]

    class memberOf(ObjectProperty, FunctionalProperty):
        domain = [MemberState]
        range = [SecurityCouncil]

    class hasVetoPower(ObjectProperty, FunctionalProperty):
        domain = [PermanentMember]
        range = [VetoPower]

    class canVeto(ObjectProperty):
        domain = [VetoPower]
        range = [Resolution]

    class doesNotApplyTo(ObjectProperty):
        domain = [VetoPower]
        range = [Vote]

    class determinedBy(ObjectProperty):
        domain = [ProceduralVote]
        range = [PermanentMember]

    class canBlockSelectionOf(ObjectProperty):
        domain = [PermanentMember]
        range = [SecretaryGeneralSelection]

    class refusedToJoin(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Organization]

    class absentFrom(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Organization]

    class contributedTo(ObjectProperty):
        domain = [Absence]
        range = [Thing]

    class mainCauseFor(ObjectProperty):
        domain = [VetoPower]
        range = [InternationalInaction]

    class concerns(ObjectProperty):
        domain = [InternationalInaction]
        range = [InternationalCrime]

    class regardsAs(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class promoterOf(ObjectProperty):
        domain = [VetoPower]
        range = [InternationalStability]

    class checkAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [MilitaryIntervention]

    class safeguardAgainst(ObjectProperty):
        domain = [VetoPower]
        range = [Domination]

    class doesNotPrevent(ObjectProperty):
        domain = [Thing]
        range = [DraftResolution]

    class yearNumber(DataProperty, FunctionalProperty):
        domain = [Year]
        range = [int]

    class refusedToJoinInYear(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [int]

    class takenBehindClosedDoors(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralSelection]
        range = [bool]

    class formalVetoRequired(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralSelection]
        range = [bool]

    class isUnconditional(DataProperty, FunctionalProperty):
        domain = [VetoPower]
        range = [bool]

    SecurityCouncil.is_a = [hasMember.some(PermanentMember)]
    PermanentMember.is_a = [memberOf.some(SecurityCouncil), hasVetoPower.some(VetoPower), canBlockSelectionOf.some(SecretaryGeneralSelection)]
    VetoPower.is_a = [canVeto.only(SubstantiveResolution), doesNotApplyTo.only(ProceduralVote)]
    ProceduralVote.is_a = [determinedBy.some(PermanentMember)]
    Abstention.is_a = [doesNotPrevent.some(DraftResolution)]
    Absence.is_a = [doesNotPrevent.some(DraftResolution)]
    InternationalInaction.is_a = [concerns.some(WarCrime), concerns.some(CrimeAgainstHumanity)]

    UnitedNationsSecurityCouncilBody = SecurityCouncil("UnitedNationsSecurityCouncilBody")
    UnitedNationsSecurityCouncilBody.label = ["United Nations Security Council", "UN Security Council"]

    UnitedNationsOrganization = Organization("UnitedNationsOrganization")
    UnitedNationsOrganization.label = ["United Nations", "UN"]

    LeagueOfNationsOrganization = Organization("LeagueOfNationsOrganization")
    LeagueOfNationsOrganization.label = "League of Nations"

    ChinaState = PermanentMember("ChinaState")
    ChinaState.label = "China"

    FranceState = PermanentMember("FranceState")
    FranceState.label = "France"

    RussiaState = PermanentMember("RussiaState")
    RussiaState.label = "Russia"

    UnitedKingdomState = PermanentMember("UnitedKingdomState")
    UnitedKingdomState.label = "United Kingdom"

    UnitedStatesState = PermanentMember("UnitedStatesState")
    UnitedStatesState.label = "United States"

    VetoPowerItem = VetoPower("VetoPowerItem")
    VetoPowerItem.label = "veto power"
    VetoPowerItem.isUnconditional = True

    DraftResolutionItem = DraftResolution("DraftResolutionItem")
    DraftResolutionItem.label = "draft resolution"

    SubstantiveResolutionItem = SubstantiveResolution("SubstantiveResolutionItem")
    SubstantiveResolutionItem.label = "substantive resolution"

    ProceduralVotesItem = ProceduralVote("ProceduralVotesItem")
    ProceduralVotesItem.label = "procedural votes"

    SecretaryGeneralSelectionItem = SecretaryGeneralSelection("SecretaryGeneralSelectionItem")
    SecretaryGeneralSelectionItem.label = "selection of a Secretary-General"
    SecretaryGeneralSelectionItem.takenBehindClosedDoors = True
    SecretaryGeneralSelectionItem.formalVetoRequired = False

    InternationalInactionItem = InternationalInaction("InternationalInactionItem")
    InternationalInactionItem.label = "international inaction on war crimes and crimes against humanity"

    WarCrimesItem = WarCrime("WarCrimesItem")
    WarCrimesItem.label = "war crimes"

    CrimesAgainstHumanityItem = CrimeAgainstHumanity("CrimesAgainstHumanityItem")
    CrimesAgainstHumanityItem.label = "crimes against humanity"

    InternationalStabilityItem = InternationalStability("InternationalStabilityItem")
    InternationalStabilityItem.label = "international stability"

    MilitaryInterventionsItem = MilitaryIntervention("MilitaryInterventionsItem")
    MilitaryInterventionsItem.label = "military interventions"

    USDominationItem = Domination("USDominationItem")
    USDominationItem.label = "U.S. domination"

    UndemocraticCharacterItem = UndemocraticCharacter("UndemocraticCharacterItem")
    UndemocraticCharacterItem.label = "the most undemocratic character of the UN"

    CriticsGroup = Critic("CriticsGroup")
    CriticsGroup.label = "critics"

    SupportersGroup = Supporter("SupportersGroup")
    SupportersGroup.label = "supporters"

    AbstentionItem = Abstention("AbstentionItem")
    AbstentionItem.label = "abstention"

    AbsenceItem = Absence("AbsenceItem")
    AbsenceItem.label = "absence"

    UnitedStatesAbsenceFromLeagueOfNations = Absence("UnitedStatesAbsenceFromLeagueOfNations")
    UnitedStatesAbsenceFromLeagueOfNations.label = "the absence of the United States from the League of Nations"

    IneffectivenessItem = Ineffectiveness("IneffectivenessItem")
    IneffectivenessItem.label = "ineffectiveness"

    Year1945 = Year("Year1945")
    Year1945.label = "1945"
    Year1945.yearNumber = 1945

    UnitedNationsSecurityCouncilBody.hasMember = [ChinaState, FranceState, RussiaState, UnitedKingdomState, UnitedStatesState]

    for member in [ChinaState, FranceState, RussiaState, UnitedKingdomState, UnitedStatesState]:
        member.memberOf = UnitedNationsSecurityCouncilBody
        member.hasVetoPower = VetoPowerItem
        member.canBlockSelectionOf = [SecretaryGeneralSelectionItem]

    UnitedStatesState.refusedToJoin = UnitedNationsOrganization
    UnitedStatesState.absentFrom = LeagueOfNationsOrganization
    UnitedStatesState.refusedToJoinInYear = 1945

    VetoPowerItem.canVeto = [SubstantiveResolutionItem]
    VetoPowerItem.doesNotApplyTo = [ProceduralVotesItem]
    VetoPowerItem.mainCauseFor = [InternationalInactionItem]
    VetoPowerItem.promoterOf = [InternationalStabilityItem]
    VetoPowerItem.checkAgainst = [MilitaryInterventionsItem]
    VetoPowerItem.safeguardAgainst = [USDominationItem]

    ProceduralVotesItem.determinedBy = [ChinaState, FranceState, RussiaState, UnitedKingdomState, UnitedStatesState]

    AbstentionItem.doesNotPrevent = [DraftResolutionItem]
    AbsenceItem.doesNotPrevent = [DraftResolutionItem]
    UnitedStatesAbsenceFromLeagueOfNations.absentFrom = LeagueOfNationsOrganization
    UnitedStatesAbsenceFromLeagueOfNations.contributedTo = [IneffectivenessItem]
    UnitedStatesAbsenceFromLeagueOfNations.label = "the absence of the United States from the League of Nations"

    CriticsGroup.regardsAs = [UndemocraticCharacterItem, InternationalInactionItem]
    SupportersGroup.regardsAs = [InternationalStabilityItem, MilitaryInterventionsItem, USDominationItem]



graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
