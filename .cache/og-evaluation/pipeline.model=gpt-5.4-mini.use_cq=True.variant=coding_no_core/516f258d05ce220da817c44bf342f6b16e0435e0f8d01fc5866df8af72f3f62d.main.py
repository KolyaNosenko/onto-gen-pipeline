"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

Who is the head of the United States Department of Justice?

What role does the United States Attorney General play in relation to legal affairs of the United States government?

Who is the chief lawyer of the United States government?

Who has the power to seek the death penalty in federal death penalty cases?

Under what constitutional process is the Attorney General nominated and appointed?

Who nominates the Attorney General?

Who appoints the Attorney General?

Which legislative body must give advice and consent for the Attorney General’s appointment?

Can the Attorney General be impeached by Congress?

For what offenses can the Attorney General be impeached by Congress?

Who has the power to remove the Attorney General?

May the President remove the Attorney General at will?

What Supreme Court case supports the President’s power to remove executive branch officials without Senate consent?

What common-law principle is suggested regarding the President’s power to remove officials with purely executive functions?

What common-law principle is suggested regarding the President’s power to remove officials whose duties affect the President’s ability to fulfill constitutional responsibilities?
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
    class Country(Thing):
        pass

    class Government(Thing):
        pass

    class GovernmentBody(Thing):
        pass

    class Office(Thing):
        pass

    class ExecutiveOffice(Office):
        pass

    class ExecutiveBranchOfficial(Thing):
        pass

    class CivilOfficer(Thing):
        pass

    class RemovalTarget(Thing):
        pass

    class AttorneyGeneralOffice(ExecutiveOffice, ExecutiveBranchOfficial, CivilOfficer, RemovalTarget):
        pass

    class PresidentOffice(ExecutiveOffice, ExecutiveBranchOfficial):
        pass

    class LegislativeBody(GovernmentBody):
        pass

    class SenateBody(LegislativeBody):
        pass

    class CongressBody(LegislativeBody):
        pass

    class JudicialBody(GovernmentBody):
        pass

    class SupremeCourtInstitution(JudicialBody):
        pass

    class Department(GovernmentBody):
        pass

    class JusticeDepartment(Department):
        pass

    class ConstitutionalDocument(Thing):
        pass

    class ConstitutionalClause(Thing):
        pass

    class AppointmentsClauseProvision(ConstitutionalClause):
        pass

    class CourtCase(Thing):
        pass

    class MyersVUnitedStatesCase(CourtCase):
        pass

    class BowsherVSynarCase(CourtCase):
        pass

    class Year(Thing):
        pass

    class LegalAffair(Thing):
        pass

    class DeathPenaltyCase(Thing):
        pass

    class ImpeachmentOffense(Thing):
        pass

    class Treason(ImpeachmentOffense):
        pass

    class Bribery(ImpeachmentOffense):
        pass

    class HighCrimesAndMisdemeanors(ImpeachmentOffense):
        pass

    class OfficialEngagedInPurelyExecutiveFunctions(RemovalTarget):
        pass

    class OfficialWhoseDutiesImmediatelyAffectPresidentAbility(RemovalTarget):
        pass

    class partOf(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class headOf(ObjectProperty):
        domain = [Office]
        range = [GovernmentBody]

    class concernedWith(ObjectProperty):
        domain = [Office]
        range = [Thing]

    class chiefLawyerOf(ObjectProperty):
        domain = [Office]
        range = [Government]

    class hasPowerToSeek(ObjectProperty):
        domain = [Office]
        range = [Thing]

    class underProcess(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class nominatedBy(ObjectProperty):
        domain = [Office]
        range = [Thing]

    class appointedBy(ObjectProperty):
        domain = [Office]
        range = [Thing]

    class appointedWithAdviceAndConsentOf(ObjectProperty):
        domain = [Office]
        range = [LegislativeBody]

    class mayBeImpeachedBy(ObjectProperty):
        domain = [CivilOfficer]
        range = [LegislativeBody]

    class mayBeImpeachedFor(ObjectProperty):
        domain = [CivilOfficer]
        range = [ImpeachmentOffense]

    class removedBy(ObjectProperty):
        domain = [Office]
        range = [Thing]

    class decidedBy(ObjectProperty):
        domain = [CourtCase]
        range = [JudicialBody]

    class inYear(ObjectProperty):
        domain = [CourtCase]
        range = [Year]

    class supportsRemovalPower(ObjectProperty):
        domain = [CourtCase]
        range = [Thing]

    class canRemove(ObjectProperty):
        domain = [PresidentOffice]
        range = [RemovalTarget]

    class UnitedStatesCountry(Country):
        pass

    UnitedStates = UnitedStatesCountry("UnitedStates")
    UnitedStates.label = "United States"

    UnitedStatesGovernment = Government("UnitedStatesGovernment")
    UnitedStatesGovernment.label = "United States government"

    UnitedStatesDepartmentOfJustice = JusticeDepartment("UnitedStatesDepartmentOfJustice")
    UnitedStatesDepartmentOfJustice.label = "United States Department of Justice"

    UnitedStatesAttorneyGeneral = AttorneyGeneralOffice("UnitedStatesAttorneyGeneral")
    UnitedStatesAttorneyGeneral.label = "United States Attorney General ( A.G. )"

    President = PresidentOffice("President")
    President.label = "President"

    Senate = SenateBody("Senate")
    Senate.label = "Senate"

    Congress = CongressBody("Congress")
    Congress.label = "Congress"

    Constitution = ConstitutionalDocument("Constitution")
    Constitution.label = "Constitution"

    AppointmentsClause = AppointmentsClauseProvision("AppointmentsClause")
    AppointmentsClause.label = "Appointments Clause"

    SupremeCourt = SupremeCourtInstitution("SupremeCourt")
    SupremeCourt.label = "Supreme Court"

    MyersVUnitedStates = MyersVUnitedStatesCase("MyersVUnitedStates")
    MyersVUnitedStates.label = "Myers v. United States"

    BowsherVSynar = BowsherVSynarCase("BowsherVSynar")
    BowsherVSynar.label = "Bowsher v. Synar"

    Year1986 = Year("Year1986")
    Year1986.label = "1986"

    CivilOfficer.is_a.append(mayBeImpeachedBy.some(CongressBody))
    CivilOfficer.is_a.append(mayBeImpeachedFor.some(Treason))
    CivilOfficer.is_a.append(mayBeImpeachedFor.some(Bribery))
    CivilOfficer.is_a.append(mayBeImpeachedFor.some(HighCrimesAndMisdemeanors))

    AttorneyGeneralOffice.is_a.append(headOf.some(JusticeDepartment))
    AttorneyGeneralOffice.is_a.append(concernedWith.some(LegalAffair))
    AttorneyGeneralOffice.is_a.append(chiefLawyerOf.some(Government))
    AttorneyGeneralOffice.is_a.append(hasPowerToSeek.some(DeathPenaltyCase))
    AttorneyGeneralOffice.is_a.append(nominatedBy.some(PresidentOffice))
    AttorneyGeneralOffice.is_a.append(appointedBy.some(PresidentOffice))
    AttorneyGeneralOffice.is_a.append(appointedWithAdviceAndConsentOf.some(SenateBody))
    AttorneyGeneralOffice.is_a.append(removedBy.some(PresidentOffice))
    AttorneyGeneralOffice.is_a.append(underProcess.some(AppointmentsClauseProvision))

    PresidentOffice.is_a.append(canRemove.some(ExecutiveBranchOfficial))
    PresidentOffice.is_a.append(canRemove.some(OfficialEngagedInPurelyExecutiveFunctions))
    PresidentOffice.is_a.append(canRemove.some(OfficialWhoseDutiesImmediatelyAffectPresidentAbility))

    AppointmentsClauseProvision.is_a.append(partOf.some(ConstitutionalDocument))

    MyersVUnitedStatesCase.is_a.append(decidedBy.some(SupremeCourtInstitution))
    MyersVUnitedStatesCase.is_a.append(supportsRemovalPower.some(PresidentOffice))

    BowsherVSynarCase.is_a.append(decidedBy.some(SupremeCourtInstitution))
    BowsherVSynarCase.is_a.append(supportsRemovalPower.some(PresidentOffice))

    UnitedStatesAttorneyGeneral.headOf = [UnitedStatesDepartmentOfJustice]
    UnitedStatesAttorneyGeneral.chiefLawyerOf = [UnitedStatesGovernment]
    UnitedStatesAttorneyGeneral.nominatedBy = [President]
    UnitedStatesAttorneyGeneral.appointedBy = [President]
    UnitedStatesAttorneyGeneral.appointedWithAdviceAndConsentOf = [Senate]
    UnitedStatesAttorneyGeneral.mayBeImpeachedBy = [Congress]
    UnitedStatesAttorneyGeneral.removedBy = [President]
    UnitedStatesAttorneyGeneral.underProcess = [AppointmentsClause]
    President.canRemove = [UnitedStatesAttorneyGeneral]
    AppointmentsClause.partOf = [Constitution]
    MyersVUnitedStates.decidedBy = [SupremeCourt]
    MyersVUnitedStates.supportsRemovalPower = [President]
    BowsherVSynar.decidedBy = [SupremeCourt]
    BowsherVSynar.supportsRemovalPower = [President]
    BowsherVSynar.inYear = [Year1986]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
