"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?
2. What is the role of the Attorney General in cases involving the federal death penalty?
3. Who has the power to nominate the Attorney General?
4. What body must give advice and consent for the appointment of the Attorney General?
5. Under which constitutional clause is the Attorney General nominated and appointed?
6. For what offenses can the Attorney General be impeached by Congress?
7. Who has the power to remove the Attorney General from office?
8. Which Supreme Court decision established the President's power to remove executive branch officials without Senate consent?
9. Does the President require Senate consent to remove the Attorney General?
10. What legal case established the President's power to remove an official engaged in purely executive functions?
11. What is the primary legal responsibility of the Attorney General within the United States government?
12. Which category of government officials includes the Attorney General with respect to impeachment?
13. In what year was the Bowsher v. Synar case decided?
14. What constitutional provision allows for the impeachment of the Attorney General?
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
    # ── Entity classes ────────────────────────────────────────────────────────
    class GovernmentEntity(Thing): pass
    class Government(GovernmentEntity): pass
    class GovernmentPosition(GovernmentEntity): pass
    class GovernmentDepartment(GovernmentEntity): pass
    class GovernmentBody(GovernmentEntity): pass
    class JudicialBody(GovernmentBody): pass
    class LegalDocument(Thing): pass
    class ConstitutionalProvision(LegalDocument): pass
    class LegalCase(Thing): pass
    class SupremeCourtDecision(LegalCase): pass
    class CriminalOffense(Thing): pass
    class LegalProcedure(Thing): pass

    # ── Object properties ─────────────────────────────────────────────────────
    class isHeadOf(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [GovernmentDepartment]

    class isChiefLawyerOf(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [Government]

    class hasPowerToSeek(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [LegalProcedure]

    class nominatedBy(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [GovernmentPosition]

    class appointedWithConsentOf(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [GovernmentBody]

    class nominationGovernedBy(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [ConstitutionalProvision]

    class mayBeImpeachedBy(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [GovernmentBody]

    class canBeImpeachedFor(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [CriminalOffense]

    class mayBeRemovedBy(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [GovernmentPosition]

    class removalPowerEstablishedBy(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [LegalCase]

    # ── Data properties ───────────────────────────────────────────────────────
    class isConcernedWithLegalAffairs(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range  = [bool]

    class isCivilOfficer(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range  = [bool]

    class requiresSenateConsentForRemoval(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range  = [bool]

    class decidedInYear(DataProperty, FunctionalProperty):
        domain = [LegalCase]
        range  = [int]

    # ── Named individuals ─────────────────────────────────────────────────────
    ag = GovernmentPosition("AttorneyGeneral_inst")
    ag.label = "United States Attorney General"

    doj = GovernmentDepartment("USDepartmentOfJustice_inst")
    doj.label = "United States Department of Justice"

    usgov = Government("USGovernment_inst")
    usgov.label = "United States government"

    president = GovernmentPosition("President_inst")
    president.label = "President"

    senate = GovernmentBody("Senate_inst")
    senate.label = "Senate"

    congress = GovernmentBody("Congress_inst")
    congress.label = "Congress"

    supreme_court = JudicialBody("SupremeCourt_inst")
    supreme_court.label = "Supreme Court"

    appointments_clause = ConstitutionalProvision("AppointmentsClause_inst")
    appointments_clause.label = "Appointments Clause"

    constitution = LegalDocument("TheConstitution_inst")
    constitution.label = "the Constitution"

    myers_v_us = SupremeCourtDecision("MyersVUnitedStates_inst")
    myers_v_us.label = "Myers v. United States"

    bowsher_v_synar = LegalCase("BowsherVSynar_inst")
    bowsher_v_synar.label = "Bowsher v. Synar"

    treason = CriminalOffense("Treason_inst")
    treason.label = "treason"

    bribery = CriminalOffense("Bribery_inst")
    bribery.label = "bribery"

    high_crimes = CriminalOffense("HighCrimesAndMisdemeanors_inst")
    high_crimes.label = "high crimes and misdemeanors"

    federal_death_penalty = LegalProcedure("FederalDeathPenalty_inst")
    federal_death_penalty.label = "federal death penalty"

    # ── Property assertions ───────────────────────────────────────────────────
    ag.isHeadOf                       = [doj]
    ag.isChiefLawyerOf                = [usgov]
    ag.hasPowerToSeek                 = [federal_death_penalty]
    ag.nominatedBy                    = [president]
    ag.appointedWithConsentOf         = [senate]
    ag.nominationGovernedBy           = [appointments_clause]
    ag.mayBeImpeachedBy               = [congress]
    ag.canBeImpeachedFor              = [treason, bribery, high_crimes]
    ag.mayBeRemovedBy                 = [president]
    ag.removalPowerEstablishedBy      = [myers_v_us, bowsher_v_synar]
    ag.isConcernedWithLegalAffairs    = True
    ag.isCivilOfficer                 = True
    ag.requiresSenateConsentForRemoval = False

    bowsher_v_synar.decidedInYear     = 1986


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
