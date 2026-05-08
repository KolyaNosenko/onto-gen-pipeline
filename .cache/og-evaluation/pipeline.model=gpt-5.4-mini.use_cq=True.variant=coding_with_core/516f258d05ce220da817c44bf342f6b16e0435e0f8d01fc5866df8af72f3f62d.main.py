"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?
2. What is the role of the United States Attorney General in relation to legal affairs?
3. Who is the chief lawyer of the United States government?
4. Who has the power to seek the death penalty in federal death penalty cases?
5. Who nominates the Attorney General?
6. Who appoints the Attorney General with advice and consent of the Senate?
7. Can the Attorney General be impeached by Congress?
8. For what grounds can the Attorney General be impeached by Congress?
9. Can the President remove the Attorney General at will?
10. Does the President need the consent of the Senate to remove executive branch officials?
11. Under what conditions does common law suggest the President has the power to remove an official?
12. Is the Attorney General a civil officer of the United States?
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
from og_sandbox_with_core.core.properties import constantPartOf


from og_sandbox_with_core.core.entities import (
    Abstract,
    Event,
    SocialAgent,
    SocialObject,
)


with core:
    class GovernmentOrganization(SocialObject):
        pass


    class GovernmentDepartment(GovernmentOrganization):
        pass


    class GovernmentBody(GovernmentOrganization):
        pass


    class LegislativeBody(GovernmentBody):
        pass


    class Court(GovernmentBody):
        pass


    class LegalDocument(SocialObject):
        pass


    class ConstitutionalDocument(LegalDocument):
        pass


    class ConstitutionalClause(LegalDocument):
        pass


    class LegalAffair(Abstract):
        pass


    class LegalRule(Abstract):
        pass


    class LegalDoctrine(Abstract):
        pass


    class CourtDecision(Event):
        pass


    class SupremeCourtDecision(CourtDecision):
        pass


    class LegalCase(CourtDecision):
        pass


    class FederalDeathPenaltyCase(LegalCase):
        pass


    class ImpeachmentGround(Abstract):
        pass


    class CivilOfficerOfTheUnitedStates(SocialAgent):
        pass


    class ExecutiveBranchOfficial(CivilOfficerOfTheUnitedStates):
        pass


    class AttorneyGeneralRole(ExecutiveBranchOfficial):
        pass


    class PresidentRole(ExecutiveBranchOfficial):
        pass


    class headOf(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [GovernmentDepartment]


    class concernedWith(ObjectProperty):
        domain = [GovernmentDepartment]
        range = [LegalAffair]


    class chiefLawyerOf(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [GovernmentOrganization]


    class hasPowerToSeekDeathPenaltyIn(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [FederalDeathPenaltyCase]


    class nominatedBy(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [PresidentRole]


    class appointedBy(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [PresidentRole]


    class confirmedBy(ObjectProperty):
        domain = [AttorneyGeneralRole]
        range = [LegislativeBody]


    class mayBeImpeachedBy(ObjectProperty):
        domain = [CivilOfficerOfTheUnitedStates]
        range = [LegislativeBody]


    class mayBeImpeachedFor(ObjectProperty):
        domain = [CivilOfficerOfTheUnitedStates]
        range = [ImpeachmentGround]


    class mayBeRemovedAtWillBy(ObjectProperty):
        domain = [ExecutiveBranchOfficial]
        range = [PresidentRole]


    class consentNotRequiredFrom(ObjectProperty):
        domain = [PresidentRole]
        range = [GovernmentOrganization]


    class decidedBy(ObjectProperty):
        domain = [CourtDecision]
        range = [Court]


    class providesThat(ObjectProperty):
        domain = [LegalDocument]
        range = [LegalRule]


    class foundThat(ObjectProperty):
        domain = [CourtDecision]
        range = [LegalRule]


    class suggestsThat(ObjectProperty):
        domain = [LegalDoctrine]
        range = [LegalRule]


    UnitedStatesAttorneyGeneral = AttorneyGeneralRole("UnitedStatesAttorneyGeneral")
    UnitedStatesAttorneyGeneral.label = ["United States Attorney General", "A.G."]

    UnitedStatesDepartmentOfJustice = GovernmentDepartment("UnitedStatesDepartmentOfJustice")
    UnitedStatesDepartmentOfJustice.label = "United States Department of Justice"

    UnitedStatesGovernment = GovernmentOrganization("UnitedStatesGovernment")
    UnitedStatesGovernment.label = "United States government"

    President = PresidentRole("President")
    President.label = "President"

    Senate = LegislativeBody("Senate")
    Senate.label = "Senate"

    Congress = LegislativeBody("Congress")
    Congress.label = "Congress"

    Constitution = ConstitutionalDocument("Constitution")
    Constitution.label = "Constitution"

    AppointmentsClause = ConstitutionalClause("AppointmentsClause")
    AppointmentsClause.label = "Appointments Clause"

    SupremeCourt = Court("SupremeCourt")
    SupremeCourt.label = "Supreme Court"

    MyersVUnitedStates = SupremeCourtDecision("MyersVUnitedStates")
    MyersVUnitedStates.label = "Myers v. United States"

    BowsherVSynar = SupremeCourtDecision("BowsherVSynar")
    BowsherVSynar.label = "Bowsher v. Synar, 1986"

    CommonLaw = LegalDoctrine("CommonLaw")
    CommonLaw.label = "common law"

    AllLegalAffairs = LegalAffair("AllLegalAffairs")
    AllLegalAffairs.label = "all legal affairs"

    FederalDeathPenaltyCases = FederalDeathPenaltyCase("FederalDeathPenaltyCases")
    FederalDeathPenaltyCases.label = "cases of the federal death penalty"

    AttorneyGeneralAppointmentRule = LegalRule("AttorneyGeneralAppointmentRule")
    AttorneyGeneralAppointmentRule.label = "the Attorney General is nominated by the President and appointed with the advice and consent of the Senate"

    CivilOfficersImpeachmentRule = LegalRule("CivilOfficersImpeachmentRule")
    CivilOfficersImpeachmentRule.label = 'civil officers of the United States may be impeached by Congress for treason, bribery, or "high crimes and misdemeanors"'

    PresidentRemovalRule = LegalRule("PresidentRemovalRule")
    PresidentRemovalRule.label = "the President may remove executive branch officials without the consent of the Senate or any other entity"

    CommonLawRemovalRule = LegalRule("CommonLawRemovalRule")
    CommonLawRemovalRule.label = "the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President's ability to fulfill his constitutional responsibilities"

    Treason = ImpeachmentGround("Treason")
    Treason.label = "treason"

    Bribery = ImpeachmentGround("Bribery")
    Bribery.label = "bribery"

    HighCrimesAndMisdemeanors = ImpeachmentGround("HighCrimesAndMisdemeanors")
    HighCrimesAndMisdemeanors.label = "high crimes and misdemeanors"

    UnitedStatesAttorneyGeneral.headOf.append(UnitedStatesDepartmentOfJustice)
    UnitedStatesAttorneyGeneral.chiefLawyerOf.append(UnitedStatesGovernment)
    UnitedStatesAttorneyGeneral.hasPowerToSeekDeathPenaltyIn.append(FederalDeathPenaltyCases)
    UnitedStatesAttorneyGeneral.nominatedBy.append(President)
    UnitedStatesAttorneyGeneral.appointedBy.append(President)
    UnitedStatesAttorneyGeneral.confirmedBy.append(Senate)
    UnitedStatesAttorneyGeneral.mayBeImpeachedBy.append(Congress)
    UnitedStatesAttorneyGeneral.mayBeImpeachedFor.extend([Treason, Bribery, HighCrimesAndMisdemeanors])
    UnitedStatesAttorneyGeneral.mayBeRemovedAtWillBy.append(President)

    UnitedStatesDepartmentOfJustice.concernedWith.append(AllLegalAffairs)

    Constitution.providesThat.append(CivilOfficersImpeachmentRule)
    AppointmentsClause.providesThat.append(AttorneyGeneralAppointmentRule)
    MyersVUnitedStates.foundThat.append(PresidentRemovalRule)
    CommonLaw.suggestsThat.append(CommonLawRemovalRule)

    UnitedStatesDepartmentOfJustice.constantPartOf.append(UnitedStatesGovernment)
    Congress.constantPartOf.append(UnitedStatesGovernment)
    Senate.constantPartOf.append(Congress)
    SupremeCourt.constantPartOf.append(UnitedStatesGovernment)
    AppointmentsClause.constantPartOf.append(Constitution)
    MyersVUnitedStates.decidedBy.append(SupremeCourt)
    BowsherVSynar.decidedBy.append(SupremeCourt)
    President.consentNotRequiredFrom.append(Senate)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
