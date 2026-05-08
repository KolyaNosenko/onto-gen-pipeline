"""
=== TASK INPUT ===
Source text:
The United States Attorney General ( A.G. ) is the head of the United States Department of Justice per , concerned with all legal affairs , and is the chief lawyer of the United States government . In cases of the federal death penalty , the power to seek the death penalty rests with the Attorney General . Under the Appointments Clause of the Constitution , the Attorney General is nominated by the President and appointed with the advice and consent of the Senate . The Constitution provides that civil officers of the United States , which would include the Attorney General , may be impeached by Congress for treason , bribery , or " high crimes and misdemeanors " . The Attorney General may be removed at will by the President under the Supreme Court decision Myers v. United States , which found that the President may remove executive branch officials without the consent of the Senate or any other entity . The common law further suggests that the President has the power to remove an official engaged in purely executive functions or an official whose duties immediately affect the President 's ability to fulfill his constitutional responsibilities , ( Bowsher v. Synar , 1986 ) .

1. Who is the head of the United States Department of Justice?
2. What are the primary responsibilities of the Attorney General?
3. How is the Attorney General nominated and appointed?
4. What constitutional grounds exist for impeaching the Attorney General?
5. Who has the power to seek the federal death penalty?
6. Under what circumstances can the President remove the Attorney General?
7. What was the significance of the Myers v. United States Supreme Court decision regarding executive removal?
8. What legal principles from Bowsher v. Synar apply to the removal of executive officials?
9. What role does the Senate play in the appointment of the Attorney General?
10. Is the Attorney General considered a civil officer of the United States under the Constitution?
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
    # Entity classes
    class Organization(Thing):
        """An organization"""
        pass
    
    class Government(Organization):
        """A government"""
        pass
    
    class Department(Organization):
        """A government department"""
        pass
    
    class GovernmentBody(Organization):
        """A legislative or executive body of government"""
        pass
    
    class Court(Organization):
        """A court"""
        pass
    
    class Document(Thing):
        """A legal or official document"""
        pass
    
    class Officer(Thing):
        """A government officer"""
        pass
    
    class CivilOfficer(Officer):
        """A civil officer of the United States"""
        pass
    
    class ExecutiveOfficer(Officer):
        """An executive branch officer"""
        pass
    
    class AttorneyGeneral(CivilOfficer, ExecutiveOfficer):
        """The Attorney General - head of the Department of Justice"""
        pass
    
    class President(Thing):
        """The President of the United States"""
        pass
    
    class LegalCase(Thing):
        """A legal case or court decision"""
        pass
    
    # Object Properties
    class headOf(ObjectProperty):
        """Relation: X is head of Y"""
        domain = [AttorneyGeneral]
        range = [Department]
    
    class chiefLawyerOf(ObjectProperty):
        """Relation: X is the chief lawyer of Y"""
        domain = [AttorneyGeneral]
        range = [Government]
    
    class nominatedBy(ObjectProperty):
        """Relation: X is nominated by Y"""
        domain = [AttorneyGeneral]
        range = [President]
    
    class appointedWith(ObjectProperty):
        """Relation: X is appointed with the advice/consent of Y"""
        domain = [AttorneyGeneral]
        range = [GovernmentBody]
    
    class canBeRemovedBy(ObjectProperty):
        """Relation: X can be removed by Y"""
        domain = [ExecutiveOfficer]
        range = [President]
    
    class decidedIn(ObjectProperty):
        """Relation: case decided in court"""
        domain = [LegalCase]
        range = [Court]
    
    # Data Properties
    class concernedWith(DataProperty):
        """Data property: areas of concern"""
        domain = [AttorneyGeneral]
        range = [str]
    
    class impeachmentGrounds(DataProperty):
        """Data property: grounds for impeachment"""
        domain = [CivilOfficer]
        range = [str]
    
    class hasPowerToSeek(DataProperty):
        """Data property: power to seek penalties"""
        domain = [AttorneyGeneral]
        range = [str]
    
    class removalRuleEstablished(DataProperty):
        """Data property: removal rule established by case"""
        domain = [LegalCase]
        range = [str]
    
    class yearDecided(DataProperty, FunctionalProperty):
        """Functional data property: year case was decided"""
        domain = [LegalCase]
        range = [int]
    
    # Instances of named entities
    ag = AttorneyGeneral("AGRole")
    ag.label = "United States Attorney General ( A.G. )"
    
    president = President("PresidentRole")
    president.label = "President"
    
    doj = Department("DOJ")
    doj.label = "United States Department of Justice"
    
    usg = Government("USGovernment")
    usg.label = "United States government"
    
    senate = GovernmentBody("Senate")
    senate.label = "Senate"
    
    congress = GovernmentBody("Congress")
    congress.label = "Congress"
    
    constitution = Document("Constitution")
    constitution.label = "Constitution"
    
    supreme_court = Court("SupremeCourt")
    supreme_court.label = "Supreme Court"
    
    myers = LegalCase("MyersVUnitedStates")
    myers.label = "Myers v. United States"
    
    bowsher = LegalCase("BowsherVSynar")
    bowsher.label = "Bowsher v. Synar"
    
    # Relationships from the text
    # Attorney General is head of Department of Justice
    ag.headOf = [doj]
    
    # Attorney General is concerned with legal affairs
    ag.concernedWith = ["legal affairs"]
    
    # Attorney General is chief lawyer of the government
    ag.chiefLawyerOf = [usg]
    
    # Attorney General has power to seek federal death penalty
    ag.hasPowerToSeek = ["federal death penalty"]
    
    # Attorney General is nominated by President
    ag.nominatedBy = [president]
    
    # Attorney General is appointed with Senate's advice and consent
    ag.appointedWith = [senate]
    
    # Attorney General can be removed by President
    ag.canBeRemovedBy = [president]
    
    # Civil officers can be impeached for specified grounds
    ag.impeachmentGrounds = ["treason", "bribery", "high crimes and misdemeanors"]
    
    # Myers v. United States Supreme Court case - decided in Supreme Court
    myers.decidedIn = [supreme_court]
    myers.removalRuleEstablished = ["President may remove executive officials without consent of Senate or any other entity"]
    
    # Bowsher v. Synar Supreme Court case - decided in Supreme Court, year 1986
    bowsher.decidedIn = [supreme_court]
    bowsher.removalRuleEstablished = ["President has power to remove officials engaged in purely executive functions or whose duties affect President's ability to fulfill constitutional responsibilities"]
    bowsher.yearDecided = 1986


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
