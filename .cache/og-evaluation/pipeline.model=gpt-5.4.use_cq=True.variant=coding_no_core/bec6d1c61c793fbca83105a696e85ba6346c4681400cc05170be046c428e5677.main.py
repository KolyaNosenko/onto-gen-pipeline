"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?
2. What legal affairs is the United States Attorney General concerned with?
3. Who is the chief lawyer of the United States government?
4. Who has the power to seek the federal death penalty?
5. Under which constitutional provision is the Attorney General nominated and appointed?
6. Who nominates the Attorney General?
7. Who appoints the Attorney General?
8. What role does the Senate have in the appointment of the Attorney General?
9. Is the Attorney General considered a civil officer of the United States?
10. Under what conditions may the Attorney General be impeached by Congress?
11. Which branch or institution has the power to impeach the Attorney General?
12. Can the Attorney General be removed by the President without the consent of the Senate?
13. Which Supreme Court decision established that the President may remove executive branch officials without Senate consent?
14. May the Attorney General be removed at will by the President?
15. What kinds of officials may the President remove under common law principles?
16. Does the Attorney General perform purely executive functions?
17. Do the duties of the Attorney General immediately affect the President’s ability to fulfill constitutional responsibilities?
18. Which court case suggests that the President has the power to remove an official whose duties immediately affect the President’s constitutional responsibilities?
19. What is the relationship between the Attorney General and the Department of Justice?
20. What are the constitutional and legal bases for appointing and removing the Attorney General?
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
    class PoliticalEntity(Thing):
        pass

    class Country(PoliticalEntity):
        pass

    class GovernmentInstitution(PoliticalEntity):
        pass

    class Government(GovernmentInstitution):
        pass

    class GovernmentDepartment(GovernmentInstitution):
        pass

    class GovernmentOffice(GovernmentInstitution):
        pass

    class ExecutiveBranchOfficial(GovernmentOffice):
        pass

    class PurelyExecutiveOfficial(ExecutiveBranchOfficial):
        pass

    class ResponsibilityAffectingOfficial(ExecutiveBranchOfficial):
        pass

    class CivilOfficer(ExecutiveBranchOfficial):
        pass

    class AttorneyGeneral(CivilOfficer, PurelyExecutiveOfficial, ResponsibilityAffectingOfficial):
        pass

    class PresidentOffice(ExecutiveBranchOfficial):
        pass

    class LegislativeBody(GovernmentInstitution):
        pass

    class Court(GovernmentInstitution):
        pass

    class LegalConcept(Thing):
        pass

    class LegalAffair(LegalConcept):
        pass

    class LegalPenalty(LegalConcept):
        pass

    class LegalBasis(LegalConcept):
        pass

    class ConstitutionalDocument(LegalBasis):
        pass

    class ConstitutionalProvision(LegalBasis):
        pass

    class LegalDoctrine(LegalBasis):
        pass

    class CourtDecision(LegalBasis):
        pass

    class SupremeCourtDecision(CourtDecision):
        pass

    class ImpeachmentGround(LegalConcept):
        pass

    class TimePoint(Thing):
        pass

    class headOf(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [GovernmentDepartment]

    class concernedWith(ObjectProperty):
        domain = [GovernmentOffice]
        range = [LegalAffair]

    class chiefLawyerOf(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [Government]

    class hasPowerToSeek(ObjectProperty):
        domain = [GovernmentOffice]
        range = [LegalPenalty]

    class nominatedBy(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [PresidentOffice]

    class appointedBy(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [PresidentOffice]

    class appointedUnder(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [ConstitutionalProvision]

    class appointedWithAdviceAndConsentOf(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [LegislativeBody]

    class officerOf(ObjectProperty, FunctionalProperty):
        domain = [CivilOfficer]
        range = [Country]

    class impeachableBy(ObjectProperty, FunctionalProperty):
        domain = [CivilOfficer]
        range = [LegislativeBody]

    class impeachableFor(ObjectProperty):
        domain = [CivilOfficer]
        range = [ImpeachmentGround]

    class removableAtWillBy(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [PresidentOffice]

    class removableWithoutConsentOf(ObjectProperty):
        domain = [GovernmentOffice]
        range = [GovernmentInstitution]

    class canRemove(ObjectProperty):
        domain = [PresidentOffice]
        range = [GovernmentOffice]

    class immediatelyAffectsAbilityOf(ObjectProperty, FunctionalProperty):
        domain = [ResponsibilityAffectingOfficial]
        range = [PresidentOffice]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class decidedBy(ObjectProperty, FunctionalProperty):
        domain = [CourtDecision]
        range = [Court]

    class decidedIn(ObjectProperty, FunctionalProperty):
        domain = [CourtDecision]
        range = [TimePoint]

    class basisForAppointmentOf(ObjectProperty):
        domain = [LegalBasis]
        range = [GovernmentOffice]

    class basisForRemovalOf(ObjectProperty):
        domain = [LegalBasis]
        range = [GovernmentOffice]

    class supportsRemovalWithoutConsentOf(ObjectProperty):
        domain = [CourtDecision]
        range = [GovernmentInstitution]

    class performsPurelyExecutiveFunctions(DataProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [bool]

    class dutiesImmediatelyAffectPresidentialResponsibilities(DataProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [bool]

    AttorneyGeneral.is_a.append(headOf.some(GovernmentDepartment))
    AttorneyGeneral.is_a.append(concernedWith.some(LegalAffair))
    AttorneyGeneral.is_a.append(concernedWith.only(LegalAffair))
    AttorneyGeneral.is_a.append(chiefLawyerOf.some(Government))
    AttorneyGeneral.is_a.append(hasPowerToSeek.some(LegalPenalty))
    AttorneyGeneral.is_a.append(nominatedBy.some(PresidentOffice))
    AttorneyGeneral.is_a.append(appointedBy.some(PresidentOffice))
    AttorneyGeneral.is_a.append(appointedUnder.some(ConstitutionalProvision))
    AttorneyGeneral.is_a.append(appointedWithAdviceAndConsentOf.some(LegislativeBody))
    AttorneyGeneral.is_a.append(officerOf.some(Country))
    AttorneyGeneral.is_a.append(impeachableBy.some(LegislativeBody))
    AttorneyGeneral.is_a.append(impeachableFor.some(ImpeachmentGround))
    AttorneyGeneral.is_a.append(removableAtWillBy.some(PresidentOffice))
    PresidentOffice.is_a.append(canRemove.some(Or([PurelyExecutiveOfficial, ResponsibilityAffectingOfficial])))
    ConstitutionalProvision.is_a.append(partOf.some(ConstitutionalDocument))
    SupremeCourtDecision.is_a.append(decidedBy.some(Court))

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    UnitedStatesGovernment = Government("UnitedStatesGovernment")
    UnitedStatesGovernment.label = "United States government"

    UnitedStatesDepartmentOfJustice = GovernmentDepartment("UnitedStatesDepartmentOfJustice")
    UnitedStatesDepartmentOfJustice.label = "United States Department of Justice"

    UnitedStatesAttorneyGeneral = AttorneyGeneral("UnitedStatesAttorneyGeneral")
    UnitedStatesAttorneyGeneral.label = [
        "United States Attorney General ( A.G. )",
        "Attorney General",
        "A.G.",
    ]

    AllLegalAffairs = LegalAffair("AllLegalAffairs")
    AllLegalAffairs.label = "all legal affairs"

    FederalDeathPenalty = LegalPenalty("FederalDeathPenalty")
    FederalDeathPenalty.label = "federal death penalty"

    AppointmentsClauseOfTheConstitution = ConstitutionalProvision("AppointmentsClauseOfTheConstitution")
    AppointmentsClauseOfTheConstitution.label = "Appointments Clause of the Constitution"

    Constitution = ConstitutionalDocument("Constitution")
    Constitution.label = ["the Constitution", "The Constitution"]

    President = PresidentOffice("President")
    President.label = "President"

    Senate = LegislativeBody("Senate")
    Senate.label = "Senate"

    Congress = LegislativeBody("Congress")
    Congress.label = "Congress"

    SupremeCourt = Court("SupremeCourt")
    SupremeCourt.label = "Supreme Court"

    MyersVUnitedStates = SupremeCourtDecision("MyersVUnitedStates")
    MyersVUnitedStates.label = "Myers v. United States"

    CommonLaw = LegalDoctrine("CommonLaw")
    CommonLaw.label = "common law"

    BowsherVSynar = CourtDecision("BowsherVSynar")
    BowsherVSynar.label = "Bowsher v. Synar"

    Year1986 = TimePoint("Year1986")
    Year1986.label = "1986"

    Treason = ImpeachmentGround("Treason")
    Treason.label = "treason"

    Bribery = ImpeachmentGround("Bribery")
    Bribery.label = "bribery"

    HighCrimesAndMisdemeanors = ImpeachmentGround("HighCrimesAndMisdemeanors")
    HighCrimesAndMisdemeanors.label = '"high crimes and misdemeanors"'

    UnitedStatesAttorneyGeneral.headOf = UnitedStatesDepartmentOfJustice
    UnitedStatesAttorneyGeneral.concernedWith = [AllLegalAffairs]
    UnitedStatesAttorneyGeneral.chiefLawyerOf = UnitedStatesGovernment
    UnitedStatesAttorneyGeneral.hasPowerToSeek = [FederalDeathPenalty]
    UnitedStatesAttorneyGeneral.nominatedBy = President
    UnitedStatesAttorneyGeneral.appointedBy = President
    UnitedStatesAttorneyGeneral.appointedUnder = AppointmentsClauseOfTheConstitution
    UnitedStatesAttorneyGeneral.appointedWithAdviceAndConsentOf = Senate
    UnitedStatesAttorneyGeneral.officerOf = UnitedStates
    UnitedStatesAttorneyGeneral.impeachableBy = Congress
    UnitedStatesAttorneyGeneral.impeachableFor = [Treason, Bribery, HighCrimesAndMisdemeanors]
    UnitedStatesAttorneyGeneral.removableAtWillBy = President
    UnitedStatesAttorneyGeneral.removableWithoutConsentOf = [Senate]
    UnitedStatesAttorneyGeneral.immediatelyAffectsAbilityOf = President
    UnitedStatesAttorneyGeneral.performsPurelyExecutiveFunctions = True
    UnitedStatesAttorneyGeneral.dutiesImmediatelyAffectPresidentialResponsibilities = True

    AppointmentsClauseOfTheConstitution.partOf = [Constitution]
    AppointmentsClauseOfTheConstitution.basisForAppointmentOf = [UnitedStatesAttorneyGeneral]

    President.canRemove = [UnitedStatesAttorneyGeneral]

    MyersVUnitedStates.decidedBy = SupremeCourt
    MyersVUnitedStates.basisForRemovalOf = [UnitedStatesAttorneyGeneral]
    MyersVUnitedStates.supportsRemovalWithoutConsentOf = [Senate]

    CommonLaw.basisForRemovalOf = [UnitedStatesAttorneyGeneral]

    BowsherVSynar.basisForRemovalOf = [UnitedStatesAttorneyGeneral]
    BowsherVSynar.decidedIn = Year1986


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
