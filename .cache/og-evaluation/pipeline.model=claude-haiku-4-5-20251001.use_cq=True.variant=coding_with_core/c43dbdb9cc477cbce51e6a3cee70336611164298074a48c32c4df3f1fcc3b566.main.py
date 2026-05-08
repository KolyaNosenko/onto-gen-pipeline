"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?

2. What are the primary responsibilities of the Attorney General?

3. What is the process for appointing the Attorney General?

4. Who has the power to seek the federal death penalty?

5. Under what circumstances can the Attorney General be impeached?

6. Who has the authority to remove the Attorney General from office?

7. Can the President remove the Attorney General without Senate consent?

8. What constitutional basis allows the President to remove executive branch officials?

9. What are the grounds for impeaching civil officers of the United States?

10. What was the significance of the Myers v. United States Supreme Court decision regarding executive removal power?
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
    SocialAgent, Society, NonAgentiveSocialObject
)
from og_sandbox_with_core.core.properties import partOf


with core:
    # Entity classes
    class Attorney(SocialAgent):
        """Head of the Department of Justice, chief lawyer of government"""
        pass

    class GovernmentOfficer(SocialAgent):
        """An officer of the executive branch"""
        pass

    class Government(Society):
        """A government entity"""
        pass

    class GovernmentDepartment(Society):
        """A department of government"""
        pass

    class LegislativeBody(Society):
        """A legislative body such as Congress or the Senate"""
        pass

    class JudicialBody(Society):
        """A judicial body such as the Supreme Court"""
        pass

    class LegalDocument(NonAgentiveSocialObject):
        """A legal or constitutional document"""
        pass

    class ConstitutionalClause(NonAgentiveSocialObject):
        """A clause or provision of the Constitution"""
        pass

    class CourtDecision(NonAgentiveSocialObject):
        """A decision issued by the Supreme Court"""
        pass

    class ImpeachmentGround(NonAgentiveSocialObject):
        """A ground or basis for impeachment"""
        pass

    class LegalConcern(NonAgentiveSocialObject):
        """An area of legal concern or responsibility"""
        pass

    class LegalPower(NonAgentiveSocialObject):
        """A legal power or authority"""
        pass

    # Properties
    class headOf(ObjectProperty):
        """An entity is the head of an organization"""
        domain = [Attorney]
        range = [GovernmentDepartment]

    class chiefLawyerOf(ObjectProperty):
        """An entity is the chief lawyer of a government"""
        domain = [Attorney]
        range = [Government]

    class concernedWith(ObjectProperty):
        """An entity is concerned with an area of law"""
        domain = [Attorney]
        range = [LegalConcern]

    class hasPower(ObjectProperty):
        """An entity has a particular legal power"""
        domain = [Attorney]
        range = [LegalPower]

    class nominatedBy(ObjectProperty):
        """An entity is nominated by another"""
        domain = [Attorney]
        range = [GovernmentOfficer]

    class appointedWithConsentOf(ObjectProperty):
        """An entity is appointed with the consent of a legislative body"""
        domain = [Attorney]
        range = [LegislativeBody]

    class canBeRemovedBy(ObjectProperty):
        """An entity can be removed by another"""
        domain = [Attorney]
        range = [GovernmentOfficer]

    class canImpeachBy(ObjectProperty):
        """An entity can be impeached by a legislative body"""
        domain = [Attorney]
        range = [LegislativeBody]

    class impeachableFor(ObjectProperty):
        """An entity can be impeached on a specific ground"""
        domain = [Attorney]
        range = [ImpeachmentGround]

    class clauseOf(ObjectProperty):
        """A clause is part of a legal document"""
        domain = [ConstitutionalClause]
        range = [LegalDocument]

    class decidedBy(ObjectProperty):
        """A case or decision is decided by a judicial body"""
        domain = [CourtDecision]
        range = [JudicialBody]

    # Named instances
    # Attorney General
    attorney_general = Attorney("UnitedStatesAttorneyGeneral")
    attorney_general.label = "United States Attorney General ( A.G. )"

    # President
    president = GovernmentOfficer("President")
    president.label = "President"

    # Department of Justice
    doj = GovernmentDepartment("UnitedStatesDepartmentOfJustice")
    doj.label = "United States Department of Justice"
    attorney_general.headOf.append(doj)

    # United States government
    us_government = Government("UnitedStatesGovernment")
    us_government.label = "United States government"
    attorney_general.chiefLawyerOf.append(us_government)

    # Legal affairs
    legal_affairs = LegalConcern("LegalAffairs")
    legal_affairs.label = "legal affairs"
    attorney_general.concernedWith.append(legal_affairs)

    # Federal death penalty
    death_penalty = LegalPower("FederalDeathPenalty")
    death_penalty.label = "federal death penalty"
    attorney_general.hasPower.append(death_penalty)

    # Senate
    senate = LegislativeBody("Senate")
    senate.label = "Senate"
    attorney_general.appointedWithConsentOf.append(senate)

    # Congress
    congress = LegislativeBody("Congress")
    congress.label = "Congress"
    attorney_general.canImpeachBy.append(congress)

    # Appointment process
    attorney_general.nominatedBy.append(president)

    # Removal power
    attorney_general.canBeRemovedBy.append(president)

    # Impeachment grounds
    treason = ImpeachmentGround("Treason")
    treason.label = "Treason"
    attorney_general.impeachableFor.append(treason)

    bribery = ImpeachmentGround("Bribery")
    bribery.label = "Bribery"
    attorney_general.impeachableFor.append(bribery)

    high_crimes = ImpeachmentGround("HighCrimesAndMisdemeanors")
    high_crimes.label = "high crimes and misdemeanors"
    attorney_general.impeachableFor.append(high_crimes)

    # Constitution
    constitution = LegalDocument("Constitution")
    constitution.label = "Constitution"

    # Appointments Clause
    appointments_clause = ConstitutionalClause("AppointmentsClause")
    appointments_clause.label = "Appointments Clause"
    appointments_clause.clauseOf.append(constitution)

    # Supreme Court
    supreme_court = JudicialBody("SupremeCourt")
    supreme_court.label = "Supreme Court"

    # Myers v. United States case
    myers_case = CourtDecision("MyersVUnitedStates")
    myers_case.label = "Myers v. United States"
    myers_case.decidedBy.append(supreme_court)

    # Bowsher v. Synar case
    bowsher_case = CourtDecision("BowsherVSynar1986")
    bowsher_case.label = "Bowsher v. Synar, 1986"
    bowsher_case.decidedBy.append(supreme_court)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
