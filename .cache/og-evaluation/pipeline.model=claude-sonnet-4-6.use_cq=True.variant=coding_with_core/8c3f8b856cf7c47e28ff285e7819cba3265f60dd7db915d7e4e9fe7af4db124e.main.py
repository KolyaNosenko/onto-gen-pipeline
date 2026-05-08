"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?
2. What is the role of the United States Attorney General in relation to the federal death penalty?
3. Who has the power to seek the death penalty in federal cases?
4. How is the Attorney General appointed?
5. Who nominates the Attorney General?
6. What body must give advice and consent for the appointment of the Attorney General?
7. Under which constitutional clause is the Attorney General nominated and appointed?
8. For what offenses can the Attorney General be impeached?
9. Who has the power to impeach the Attorney General?
10. Who has the power to remove the Attorney General?
11. Is the consent of the Senate required for the President to remove the Attorney General?
12. What Supreme Court decision established that the President may remove executive branch officials without Senate consent?
13. What legal case established the President's power to remove officials engaged in purely executive functions?
14. What is the primary legal responsibility of the Attorney General?
15. Is the Attorney General considered a civil officer of the United States?
16. What court ruling supports the President's authority to remove officials whose duties affect the President's constitutional responsibilities?
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
    SocialAgent,
    Society,
    NonAgentiveSocialObject,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import presentAt


with core:
    # ------------------------------------------------------------------ #
    # Entity classes                                                       #
    # ------------------------------------------------------------------ #

    class GovernmentOfficial(SocialAgent):
        """A role held by a person in government, carrying official duties."""

    class CivilOfficer(GovernmentOfficial):
        """A civil officer of the United States, subject to impeachment."""

    class ExecutiveBranchOfficial(CivilOfficer):
        """An official of the executive branch, removable by the President."""

    class AttorneyGeneral(ExecutiveBranchOfficial):
        """The head of the United States Department of Justice."""

    class FederalDepartment(Society):
        """A department of the United States federal government."""

    class Government(Society):
        """The United States government as a whole."""

    class LegislativeBody(Society):
        """A legislative institution (Senate, Congress)."""

    class Court(Society):
        """A judicial institution (Supreme Court)."""

    class LegalDocument(NonAgentiveSocialObject):
        """A formal legal text (constitution, statute, etc.)."""

    class ConstitutionalProvision(LegalDocument):
        """A specific clause or provision of a constitutional document."""

    class CourtCase(NonAgentiveSocialObject):
        """A judicial decision or case (e.g. Myers v. United States)."""

    class LegalPenalty(NonAgentiveSocialObject):
        """A penalty defined and regulated by law."""

    class ImpeachableOffense(NonAgentiveSocialObject):
        """A ground listed in the Constitution for impeachment."""

    # ------------------------------------------------------------------ #
    # Object properties                                                    #
    # ------------------------------------------------------------------ #

    class isHeadOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [Society]

    class isChiefLawyerOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [Society]

    class isCivilOfficerOf(ObjectProperty):
        domain = [CivilOfficer]
        range = [Government]

    class nominatedBy(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [GovernmentOfficial]

    class appointedWithConsentOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegislativeBody]

    class authorizedUnder(ObjectProperty):
        """Nomination / appointment of an official is authorised under a legal document."""
        domain = [GovernmentOfficial]
        range = [LegalDocument]

    class canBeImpeachedBy(ObjectProperty):
        domain = [CivilOfficer]
        range = [LegislativeBody]

    class impeachableFor(ObjectProperty):
        domain = [CivilOfficer]
        range = [ImpeachableOffense]

    class canBeRemovedBy(ObjectProperty):
        domain = [ExecutiveBranchOfficial]
        range = [GovernmentOfficial]

    class removalEstablishedBy(ObjectProperty):
        """Removal authority established / supported by a court case."""
        domain = [ExecutiveBranchOfficial]
        range = [CourtCase]

    class hasPowerToSeek(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegalPenalty]

    class isProvisionOf(ObjectProperty):
        domain = [ConstitutionalProvision]
        range = [LegalDocument]

    # Post-hoc class restrictions (properties are now defined)
    AttorneyGeneral.is_a.append(isHeadOf.some(FederalDepartment))
    AttorneyGeneral.is_a.append(isChiefLawyerOf.some(Government))

    # ------------------------------------------------------------------ #
    # Named individuals                                                    #
    # ------------------------------------------------------------------ #

    ag = AttorneyGeneral("AttorneyGeneral_inst")
    ag.label = "United States Attorney General"

    doj = FederalDepartment("UnitedStatesDepartmentOfJustice")
    doj.label = "United States Department of Justice"

    usgov = Government("UnitedStatesGovernment")
    usgov.label = "United States government"

    president = GovernmentOfficial("UnitedStatesPresident")
    president.label = "President"

    senate = LegislativeBody("UnitedStatesSenate")
    senate.label = "Senate"

    congress = LegislativeBody("UnitedStatesCongress")
    congress.label = "Congress"

    supreme_court = Court("UnitedStatesSupremeCourt")
    supreme_court.label = "Supreme Court"

    constitution = LegalDocument("UnitedStatesConstitution")
    constitution.label = "Constitution"

    appointments_clause = ConstitutionalProvision("AppointmentsClause")
    appointments_clause.label = "Appointments Clause"

    myers_v_us = CourtCase("MyersVUnitedStates")
    myers_v_us.label = "Myers v. United States"

    bowsher_v_synar = CourtCase("BowsherVSynar")
    bowsher_v_synar.label = "Bowsher v. Synar"

    federal_death_penalty = LegalPenalty("FederalDeathPenalty")
    federal_death_penalty.label = "federal death penalty"

    year_1986 = TimeInterval("Year1986")
    year_1986.label = "1986"

    treason = ImpeachableOffense("Treason_inst")
    treason.label = "treason"

    bribery = ImpeachableOffense("Bribery_inst")
    bribery.label = "bribery"

    high_crimes = ImpeachableOffense("HighCrimesAndMisdemeanors_inst")
    high_crimes.label = "high crimes and misdemeanors"

    # Property assertions
    ag.isHeadOf.append(doj)
    ag.isChiefLawyerOf.append(usgov)
    ag.isCivilOfficerOf.append(usgov)
    ag.nominatedBy.append(president)
    ag.appointedWithConsentOf.append(senate)
    ag.authorizedUnder.append(appointments_clause)
    ag.canBeImpeachedBy.append(congress)
    ag.impeachableFor.append(treason)
    ag.impeachableFor.append(bribery)
    ag.impeachableFor.append(high_crimes)
    ag.canBeRemovedBy.append(president)
    ag.removalEstablishedBy.append(myers_v_us)
    ag.removalEstablishedBy.append(bowsher_v_synar)
    ag.hasPowerToSeek.append(federal_death_penalty)

    appointments_clause.isProvisionOf.append(constitution)
    bowsher_v_synar.presentAt.append(year_1986)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
