"""
=== TASK INPUT ===
Source text:
The United Nations Security Council " veto power " refers to the power of the permanent members of the UN Security Council ( China , France , Russia , United Kingdom , and United States ) to veto any " substantive " resolution . A permanent member 's abstention or absence does not prevent a draft resolution from being adopted . This veto power does not apply to " procedural " votes , as determined by the permanent members themselves . A permanent member can also block the selection of a Secretary - General , although a formal veto is unnecessary since the vote is taken behind closed doors . The unconditional veto possessed by the five governments has been seen by critics as the most undemocratic character of the UN . Critics also claim that veto power is the main cause for international inaction on war crimes and crimes against humanity . However , the United States refused to join the United Nations in 1945 unless it was given a veto . The absence of the United States from the League of Nations contributed to its ineffectiveness . Supporters of the veto power regard it as a promoter of international stability , a check against military interventions , and a critical safeguard against U.S. domination .

1. Which countries are permanent members of the United Nations Security Council?
2. What type of resolutions can permanent members of the UN Security Council veto?
3. Does a permanent member's abstention prevent a draft resolution from being adopted?
4. Does the veto power apply to procedural votes?
5. Who determines whether a vote is procedural or substantive?
6. Can a permanent member block the selection of a Secretary-General?
7. Is a formal veto required to block the selection of a Secretary-General?
8. What criticisms have been raised against the veto power?
9. What role did the veto power play in the United States' decision to join the United Nations in 1945?
10. How did the absence of the United States from the League of Nations affect that organization?
11. What arguments do supporters of the veto power make in its favor?
12. What impact does the veto power have on international action regarding war crimes and crimes against humanity?
13. How many permanent members does the UN Security Council have?
14. Is the vote for the selection of a Secretary-General taken publicly or behind closed doors?
15. What is the relationship between the veto power and the prevention of U.S. domination?
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
    # ── Entity Classes ───────────────────────────────────────────────────────

    class InternationalOrganisation(Thing): pass

    class SecurityCouncil(InternationalOrganisation): pass

    class Country(Thing): pass

    class PermanentMember(Country): pass

    class VetoPower(Thing): pass

    class Resolution(Thing): pass

    class SubstantiveResolution(Resolution): pass

    class ProceduralVote(Resolution): pass

    class DraftResolution(Resolution): pass

    class Vote(Thing): pass

    class SecretVote(Vote): pass

    class OfficialPosition(Thing): pass

    class SecretaryGeneral(OfficialPosition): pass

    class Selection(Thing): pass

    class SecretaryGeneralSelection(Selection): pass

    class Criticism(Thing): pass

    class SupportArgument(Thing): pass

    class WarCrime(Thing): pass

    class CrimeAgainstHumanity(Thing): pass

    class MilitaryIntervention(Thing): pass

    class InternationalInaction(Thing): pass

    class InternationalStability(Thing): pass

    class Domination(Thing): pass

    class Year(Thing): pass

    # ── Object Properties ────────────────────────────────────────────────────

    class hasPermanentMember(ObjectProperty):
        domain = [SecurityCouncil]
        range  = [PermanentMember]

    class isPermanentMemberOf(ObjectProperty):
        domain = [PermanentMember]
        range  = [SecurityCouncil]

    class memberOf(ObjectProperty):
        domain = [Country]
        range  = [InternationalOrganisation]

    class vetoAppliesTo(ObjectProperty):
        domain = [VetoPower]
        range  = [Resolution]

    class determinedBy(ObjectProperty):
        domain = [ProceduralVote]
        range  = [PermanentMember]

    class canBlock(ObjectProperty):
        domain = [PermanentMember]
        range  = [Selection]

    class hasCriticism(ObjectProperty):
        domain = [VetoPower]
        range  = [Criticism]

    class hasSupportArgument(ObjectProperty):
        domain = [VetoPower]
        range  = [SupportArgument]

    class causeOf(ObjectProperty):
        domain = [VetoPower]
        range  = [InternationalInaction]

    class inactionRegarding(ObjectProperty):
        domain = [InternationalInaction]
        range  = [Thing]

    class promoterOf(ObjectProperty):
        domain = [VetoPower]
        range  = [InternationalStability]

    class checkAgainst(ObjectProperty):
        domain = [VetoPower]
        range  = [MilitaryIntervention]

    class safeguardAgainst(ObjectProperty):
        domain = [VetoPower]
        range  = [Domination]

    class heldVetoAsJoiningCondition(ObjectProperty):
        domain = [Country]
        range  = [InternationalOrganisation]

    class absenceContributedToIneffectivenessOf(ObjectProperty):
        domain = [Country]
        range  = [InternationalOrganisation]

    # ── Data Properties ──────────────────────────────────────────────────────

    class permanentMemberCount(DataProperty, FunctionalProperty):
        domain = [SecurityCouncil]
        range  = [int]

    class abstentionPreventsAdoption(DataProperty, FunctionalProperty):
        domain = [VetoPower]
        range  = [bool]

    class vetoApplicable(DataProperty, FunctionalProperty):
        domain = [Resolution]
        range  = [bool]

    class requiresFormalVeto(DataProperty, FunctionalProperty):
        domain = [SecretaryGeneralSelection]
        range  = [bool]

    class heldBehindClosedDoors(DataProperty, FunctionalProperty):
        domain = [Vote]
        range  = [bool]

    class yearValue(DataProperty, FunctionalProperty):
        domain = [Year]
        range  = [int]

    class joinedInYear(DataProperty, FunctionalProperty):
        domain = [Country]
        range  = [int]

    # ── Named Individuals ────────────────────────────────────────────────────

    # International organisations
    united_nations = InternationalOrganisation("UnitedNations")
    united_nations.label = "United Nations"

    un_security_council = SecurityCouncil("UNSecurityCouncil")
    un_security_council.label = "United Nations Security Council"

    league_of_nations = InternationalOrganisation("LeagueOfNations")
    league_of_nations.label = "League of Nations"

    # Permanent members of the UNSC
    china = PermanentMember("China")
    china.label = "China"

    france = PermanentMember("France")
    france.label = "France"

    russia = PermanentMember("Russia")
    russia.label = "Russia"

    united_kingdom = PermanentMember("UnitedKingdom")
    united_kingdom.label = "United Kingdom"

    united_states = PermanentMember("UnitedStates")
    united_states.label = "United States"

    # Veto power
    veto_power_inst = VetoPower("VetoPowerInst")
    veto_power_inst.label = "veto power"

    # Resolution types
    substantive_res = SubstantiveResolution("SubstantiveResolutionInst")
    substantive_res.label = "substantive resolution"

    procedural_vote_inst = ProceduralVote("ProceduralVoteInst")
    procedural_vote_inst.label = "procedural vote"

    draft_res = DraftResolution("DraftResolutionInst")
    draft_res.label = "draft resolution"

    # Secretary-General selection and its vote
    sg_selection = SecretaryGeneralSelection("SGSelection")
    sg_selection.label = "selection of a Secretary-General"

    sg_vote = SecretVote("SGSelectionVote")
    sg_vote.label = "vote for the selection of a Secretary-General"

    # Year 1945
    year_1945 = Year("Y1945")
    year_1945.label = "1945"
    year_1945.yearValue = 1945

    # Criticisms of veto power
    criticism_undemocratic = Criticism("CriticismUndemocratic")
    criticism_undemocratic.label = "most undemocratic character of the UN"

    criticism_inaction = Criticism("CriticismInaction")
    criticism_inaction.label = "main cause for international inaction on war crimes and crimes against humanity"

    # Support arguments for veto power
    support_stability = SupportArgument("SupportStability")
    support_stability.label = "promoter of international stability"

    support_military = SupportArgument("SupportMilitaryCheck")
    support_military.label = "check against military interventions"

    support_domination = SupportArgument("SupportUSDomination")
    support_domination.label = "critical safeguard against U.S. domination"

    # Other referenced concepts
    war_crimes = WarCrime("WarCrimesInst")
    war_crimes.label = "war crimes"

    crimes_humanity = CrimeAgainstHumanity("CrimesAgainstHumanityInst")
    crimes_humanity.label = "crimes against humanity"

    intl_inaction = InternationalInaction("InternationalInactionInst")
    intl_inaction.label = "international inaction"

    intl_stability = InternationalStability("InternationalStabilityInst")
    intl_stability.label = "international stability"

    us_domination = Domination("USDomination")
    us_domination.label = "U.S. domination"

    military_intervention = MilitaryIntervention("MilitaryInterventionInst")
    military_intervention.label = "military interventions"

    # ── Assertions ───────────────────────────────────────────────────────────

    # UNSC permanent members (CQ1, CQ13)
    un_security_council.hasPermanentMember = [china, france, russia, united_kingdom, united_states]
    un_security_council.permanentMemberCount = 5

    china.isPermanentMemberOf         = [un_security_council]
    france.isPermanentMemberOf        = [un_security_council]
    russia.isPermanentMemberOf        = [un_security_council]
    united_kingdom.isPermanentMemberOf = [un_security_council]
    united_states.isPermanentMemberOf  = [un_security_council]

    china.memberOf         = [united_nations]
    france.memberOf        = [united_nations]
    russia.memberOf        = [united_nations]
    united_kingdom.memberOf = [united_nations]
    united_states.memberOf  = [united_nations]

    # Veto applies to substantive resolutions only (CQ2, CQ4)
    veto_power_inst.vetoAppliesTo = [substantive_res]
    substantive_res.vetoApplicable  = True
    procedural_vote_inst.vetoApplicable = False

    # Abstention / absence does not prevent adoption of a draft resolution (CQ3)
    veto_power_inst.abstentionPreventsAdoption = False

    # Procedural vs. substantive determined by permanent members themselves (CQ5)
    procedural_vote_inst.determinedBy = [china, france, russia, united_kingdom, united_states]

    # Permanent members can block SG selection; no formal veto needed; behind closed doors (CQ6, CQ7, CQ14)
    china.canBlock         = [sg_selection]
    france.canBlock        = [sg_selection]
    russia.canBlock        = [sg_selection]
    united_kingdom.canBlock = [sg_selection]
    united_states.canBlock  = [sg_selection]
    sg_selection.requiresFormalVeto = False
    sg_vote.heldBehindClosedDoors   = True

    # Criticisms of veto power (CQ8)
    veto_power_inst.hasCriticism = [criticism_undemocratic, criticism_inaction]

    # Support arguments for veto power (CQ11, CQ15)
    veto_power_inst.hasSupportArgument = [support_stability, support_military, support_domination]

    # Veto power as cause of international inaction on war crimes / crimes against humanity (CQ12)
    veto_power_inst.causeOf = [intl_inaction]
    intl_inaction.inactionRegarding = [war_crimes, crimes_humanity]

    # Veto power attributes cited by supporters (CQ11, CQ15)
    veto_power_inst.promoterOf    = [intl_stability]
    veto_power_inst.checkAgainst  = [military_intervention]
    veto_power_inst.safeguardAgainst = [us_domination]

    # US refused to join UN in 1945 unless given a veto (CQ9)
    united_states.heldVetoAsJoiningCondition = [united_nations]
    united_states.joinedInYear = 1945

    # Absence of US from League of Nations contributed to its ineffectiveness (CQ10)
    united_states.absenceContributedToIneffectivenessOf = [league_of_nations]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
