"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

Who is the head of the United States Department of Justice?
What legal affairs is the United States Attorney General concerned with?
Who is the chief lawyer of the United States government?
Who has the power to seek the federal death penalty?
How is the United States Attorney General nominated and appointed?
Who nominates the Attorney General?
What role does the Senate play in the appointment of the Attorney General?
Under which constitutional clause is the Attorney General appointed?
Can the Attorney General be impeached by Congress?
For what reasons may the Attorney General be impeached by Congress?
Is the Attorney General considered a civil officer of the United States?
Who has the authority to remove the Attorney General from office?
Can the President remove the Attorney General without the consent of the Senate?
Which Supreme Court decision established that the President may remove executive branch officials without Senate consent?
What legal basis supports the President’s power to remove an official engaged in purely executive functions?
What kinds of official duties immediately affect the President’s ability to fulfill constitutional responsibilities?
Does the Attorney General perform purely executive functions?
What is the relationship between the Attorney General and the Department of Justice?
What is the relationship between the Attorney General and the President in terms of appointment and removal?
What constitutional and legal grounds govern the appointment, impeachment, and removal of the Attorney General?
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
    NonAgentiveSocialObject,
    SocialAgent,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class NationState(Society):
        pass


    class Government(Society):
        pass


    class LegalInstitution(Society):
        pass


    class GovernmentOrganization(LegalInstitution):
        pass


    class GovernmentDepartment(GovernmentOrganization):
        pass


    class Court(LegalInstitution):
        pass


    class LegislativeBody(LegalInstitution):
        pass


    class GovernmentOfficial(SocialAgent):
        pass


    class CivilOfficer(GovernmentOfficial):
        pass


    class ExecutiveBranchOfficial(CivilOfficer):
        pass


    class PresidentOffice(ExecutiveBranchOfficial):
        pass


    class AttorneyGeneral(ExecutiveBranchOfficial):
        pass


    class LegalMatter(NonAgentiveSocialObject):
        pass


    class LegalAffair(LegalMatter):
        pass


    class LegalPenalty(LegalMatter):
        pass


    class DeathPenalty(LegalPenalty):
        pass


    class FederalDeathPenalty(DeathPenalty):
        pass


    class LegalGround(NonAgentiveSocialObject):
        pass


    class ImpeachmentGround(LegalGround):
        pass


    class LegalSource(NonAgentiveSocialObject):
        pass


    class LegalDocument(LegalSource):
        pass


    class ConstitutionDocument(LegalDocument):
        pass


    class ConstitutionalClause(LegalSource):
        pass


    class AppointmentsClauseClass(ConstitutionalClause):
        pass


    class LegalDoctrine(LegalSource):
        pass


    class CommonLawDoctrine(LegalDoctrine):
        pass


    class JudicialDecision(LegalSource):
        pass


    class SupremeCourtDecision(JudicialDecision):
        pass


    class OfficialFunction(NonAgentiveSocialObject):
        pass


    class PurelyExecutiveFunction(OfficialFunction):
        pass


    class OfficialDuty(NonAgentiveSocialObject):
        pass


    class DutyAffectingPresidentialResponsibilities(OfficialDuty):
        pass


    class ConstitutionalResponsibility(NonAgentiveSocialObject):
        pass


    class OfficialEngagedInPurelyExecutiveFunctions(ExecutiveBranchOfficial):
        pass


    class OfficialWhoseDutiesAffectPresidentialResponsibilities(ExecutiveBranchOfficial):
        pass


    class RemovableExecutiveOfficial(ExecutiveBranchOfficial):
        pass


    class Year(TimeInterval):
        pass


    class headsOrganization(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [GovernmentOrganization]


    class concernedWith(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegalAffair]


    class chiefLawyerOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [Government]


    class hasPowerToSeekPenalty(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegalPenalty]


    class nominatedBy(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [PresidentOffice]


    class appointedBy(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [PresidentOffice]


    class appointedWithAdviceAndConsentOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegislativeBody]


    class appointedUnderClause(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [ConstitutionalClause]


    class civilOfficerOf(ObjectProperty):
        domain = [CivilOfficer]
        range = [NationState]


    class mayBeImpeachedBy(ObjectProperty):
        domain = [CivilOfficer]
        range = [LegislativeBody]


    class impeachableFor(ObjectProperty):
        domain = [CivilOfficer]
        range = [ImpeachmentGround]


    class mayBeRemovedBy(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [PresidentOffice]


    class removalDoesNotRequireConsentOf(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [LegalInstitution]


    class removalAuthorityEstablishedBy(ObjectProperty):
        domain = [GovernmentOfficial]
        range = [JudicialDecision]


    class removalPowerSupportedBy(ObjectProperty):
        domain = [ExecutiveBranchOfficial]
        range = [LegalDoctrine]


    class issuedByCourt(ObjectProperty):
        domain = [JudicialDecision]
        range = [Court]


    class citesDecision(ObjectProperty):
        domain = [LegalDoctrine]
        range = [JudicialDecision]


    class partOfLegalSource(ObjectProperty):
        domain = [LegalSource]
        range = [LegalSource]


    class engagedInFunction(ObjectProperty):
        domain = [ExecutiveBranchOfficial]
        range = [OfficialFunction]


    class hasDuty(ObjectProperty):
        domain = [ExecutiveBranchOfficial]
        range = [OfficialDuty]


    class immediatelyAffectsAbilityToFulfill(ObjectProperty):
        domain = [OfficialDuty]
        range = [ConstitutionalResponsibility]


    class decidedAt(temporallyLocatedAt):
        domain = [JudicialDecision]
        range = [TimeInterval]


    class concernScopeDescription(DataProperty, FunctionalProperty):
        domain = [AttorneyGeneral]
        range = [str]


    class establishesRuleDescription(DataProperty, FunctionalProperty):
        domain = [JudicialDecision]
        range = [str]


    class supportsRemovalPowerDescription(DataProperty, FunctionalProperty):
        domain = [LegalDoctrine]
        range = [str]


    CivilOfficer.is_a.append(civilOfficerOf.some(NationState))
    AttorneyGeneral.is_a.extend([
        headsOrganization.some(GovernmentDepartment),
        concernedWith.some(LegalAffair),
        concernedWith.only(LegalAffair),
        chiefLawyerOf.some(Government),
        hasPowerToSeekPenalty.some(FederalDeathPenalty),
        nominatedBy.some(PresidentOffice),
        appointedBy.some(PresidentOffice),
        appointedWithAdviceAndConsentOf.some(LegislativeBody),
        appointedUnderClause.some(AppointmentsClauseClass),
        mayBeImpeachedBy.some(LegislativeBody),
        impeachableFor.some(ImpeachmentGround),
        mayBeRemovedBy.some(PresidentOffice),
        removalDoesNotRequireConsentOf.some(LegalInstitution),
    ])
    AppointmentsClauseClass.is_a.append(partOfLegalSource.some(ConstitutionDocument))
    SupremeCourtDecision.is_a.append(issuedByCourt.some(Court))
    OfficialEngagedInPurelyExecutiveFunctions.is_a.append(
        engagedInFunction.some(PurelyExecutiveFunction)
    )
    DutyAffectingPresidentialResponsibilities.is_a.append(
        immediatelyAffectsAbilityToFulfill.some(ConstitutionalResponsibility)
    )
    OfficialWhoseDutiesAffectPresidentialResponsibilities.is_a.append(
        hasDuty.some(DutyAffectingPresidentialResponsibilities)
    )
    RemovableExecutiveOfficial.equivalent_to = [
        Or([
            OfficialEngagedInPurelyExecutiveFunctions,
            OfficialWhoseDutiesAffectPresidentialResponsibilities,
        ])
    ]
    RemovableExecutiveOfficial.is_a.extend([
        mayBeRemovedBy.some(PresidentOffice),
        removalPowerSupportedBy.some(CommonLawDoctrine),
    ])

    united_states = NationState("UnitedStates")
    united_states.label = "United States"

    united_states_attorney_general = AttorneyGeneral("UnitedStatesAttorneyGeneral")
    united_states_attorney_general.label = [
        "United States Attorney General",
        "United States Attorney General ( A.G. )",
        "Attorney General",
        "A.G.",
    ]
    united_states_attorney_general.concernScopeDescription = "all legal affairs"

    united_states_department_of_justice = GovernmentDepartment(
        "UnitedStatesDepartmentOfJustice"
    )
    united_states_department_of_justice.label = "United States Department of Justice"

    united_states_government = Government("UnitedStatesGovernment")
    united_states_government.label = "United States government"

    federal_death_penalty = FederalDeathPenalty("FederalDeathPenaltyInstance")
    federal_death_penalty.label = "federal death penalty"

    appointments_clause = AppointmentsClauseClass("AppointmentsClause")
    appointments_clause.label = "Appointments Clause"

    constitution = ConstitutionDocument("ConstitutionDocumentInstance")
    constitution.label = "Constitution"

    president = PresidentOffice("PresidentOfficeInstance")
    president.label = "President"

    senate = LegislativeBody("SenateBody")
    senate.label = "Senate"

    congress = LegislativeBody("CongressBody")
    congress.label = "Congress"

    supreme_court = Court("SupremeCourt")
    supreme_court.label = "Supreme Court"

    myers_v_united_states = SupremeCourtDecision("MyersVUnitedStates")
    myers_v_united_states.label = "Myers v. United States"
    myers_v_united_states.establishesRuleDescription = (
        "the President may remove executive branch officials without the consent of the Senate or any other entity"
    )

    common_law = CommonLawDoctrine("CommonLaw")
    common_law.label = "common law"
    common_law.supportsRemovalPowerDescription = (
        "the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President's ability to fulfill his constitutional responsibilities"
    )

    bowsher_v_synar = SupremeCourtDecision("BowsherVSynar")
    bowsher_v_synar.label = "Bowsher v. Synar"

    year_1986 = Year("Year1986")
    year_1986.label = "1986"

    treason = ImpeachmentGround("TreasonGround")
    treason.label = "treason"

    bribery = ImpeachmentGround("BriberyGround")
    bribery.label = "bribery"

    high_crimes_and_misdemeanors = ImpeachmentGround("HighCrimesAndMisdemeanorsGround")
    high_crimes_and_misdemeanors.label = '"high crimes and misdemeanors"'

    united_states_attorney_general.headsOrganization.append(
        united_states_department_of_justice
    )
    united_states_attorney_general.chiefLawyerOf.append(united_states_government)
    united_states_attorney_general.hasPowerToSeekPenalty.append(federal_death_penalty)
    united_states_attorney_general.nominatedBy.append(president)
    united_states_attorney_general.appointedBy.append(president)
    united_states_attorney_general.appointedWithAdviceAndConsentOf.append(senate)
    united_states_attorney_general.appointedUnderClause.append(appointments_clause)
    united_states_attorney_general.mayBeImpeachedBy.append(congress)
    united_states_attorney_general.impeachableFor.extend([
        treason,
        bribery,
        high_crimes_and_misdemeanors,
    ])
    united_states_attorney_general.mayBeRemovedBy.append(president)
    united_states_attorney_general.removalDoesNotRequireConsentOf.append(senate)
    united_states_attorney_general.removalAuthorityEstablishedBy.append(
        myers_v_united_states
    )

    appointments_clause.partOfLegalSource.append(constitution)
    myers_v_united_states.issuedByCourt.append(supreme_court)
    bowsher_v_synar.issuedByCourt.append(supreme_court)
    bowsher_v_synar.decidedAt = year_1986
    common_law.citesDecision.append(bowsher_v_synar)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
