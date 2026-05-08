"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

1. Who is Georgy Fotev and what is his nationality?
2. What are the main research interests and scientific focus areas of Georgy Fotev?
3. What is Georgy Fotev's perspective on sociology as a discipline?
4. What specific sociological fields has Georgy Fotev published work in?
5. What are the titles and subject matters of Georgy Fotev's major publications?
6. What books has Georgy Fotev written about Bulgarian society?
7. What government positions has Georgy Fotev held and during which periods?
8. What is Georgy Fotev's current academic affiliation?
9. What awards and honors has Georgy Fotev received and when?
10. Which institutions have awarded Georgy Fotev recognition?
11. What is the relationship between dialogue and multiple paradigm sociology in Georgy Fotev's work?
12. When was Georgy Fotev born?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
from datetime import date
from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    # Entity classes
    class Person(Thing): pass
    class Sociologist(Person): pass
    class Country(Thing): pass
    class Institution(Thing): pass
    class University(Institution): pass
    class Publication(Thing): pass
    class Book(Publication): pass
    class Position(Thing): pass
    class MinisterialPosition(Position): pass
    class AcademicPosition(Position): pass
    class Award(Thing): pass
    class SociologicalField(Thing): pass
    class SociologicalConcept(Thing): pass
    
    # Object properties
    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Country]
    
    class hasResearchInterest(ObjectProperty):
        domain = [Person]
        range = [SociologicalField, SociologicalConcept]
    
    class hasPublished(ObjectProperty):
        domain = [Person]
        range = [Publication]
    
    class heldPosition(ObjectProperty):
        domain = [Person]
        range = [Position]
    
    class affiliatedWith(ObjectProperty):
        domain = [Person]
        range = [Institution]
    
    class receivedAward(ObjectProperty):
        domain = [Person]
        range = [Award]
    
    class awardedBy(ObjectProperty):
        domain = [Award]
        range = [Institution]
    
    class positionAt(ObjectProperty):
        domain = [Position]
        range = [Institution]
    
    class baseFor(ObjectProperty):
        domain = [SociologicalConcept]
        range = [SociologicalConcept]
    
    class horizonFor(ObjectProperty):
        domain = [SociologicalConcept]
        range = [SociologicalConcept]
    
    # Data properties
    class birthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [date]
    
    class positionTitle(DataProperty, FunctionalProperty):
        domain = [Position]
        range = [str]
    
    class startYear(DataProperty, FunctionalProperty):
        domain = [Position]
        range = [int]
    
    class endYear(DataProperty, FunctionalProperty):
        domain = [Position]
        range = [int]
    
    class awardYear(DataProperty, FunctionalProperty):
        domain = [Award]
        range = [int]
    
    # Instances - Person
    georgyFotev = Sociologist("GeorgyFotev")
    georgyFotev.label = "Georgy Fotev"
    georgyFotev.birthDate = date(1941, 8, 24)
    
    # Instances - Country
    bulgaria = Country("Bulgaria")
    bulgaria.label = "Bulgaria"
    
    # Instances - Institutions
    newBulgarianUniversity = University("NewBulgarianUniversity")
    newBulgarianUniversity.label = "New Bulgarian University"
    
    americanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    americanUniversityInBulgaria.label = "American University in Bulgaria"
    
    # Set Georgy's nationality and affiliations
    georgyFotev.hasNationality = bulgaria
    georgyFotev.affiliatedWith = [newBulgarianUniversity]
    
    # Instances - Positions
    ministerOfEducationAndScience = MinisterialPosition("MinisterOfEducationAndScience")
    ministerOfEducationAndScience.label = "Minister of Education and Science"
    ministerOfEducationAndScience.positionTitle = "Minister of Education and Science"
    ministerOfEducationAndScience.startYear = 1991
    ministerOfEducationAndScience.endYear = 1992
    
    professorEmeritus = AcademicPosition("ProfessorEmeritus")
    professorEmeritus.label = "Professor Emeritus"
    professorEmeritus.positionTitle = "Professor Emeritus"
    professorEmeritus.positionAt = [newBulgarianUniversity]
    
    georgyFotev.heldPosition = [ministerOfEducationAndScience, professorEmeritus]
    
    # Instances - Books
    theLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    theLongNightOfCommunismInBulgaria.label = "The long night of communism in Bulgaria"
    
    bulgarianMelancholy = Book("BulgarianMelancholy")
    bulgarianMelancholy.label = "Bulgarian melancholy"
    
    georgyFotev.hasPublished = [theLongNightOfCommunismInBulgaria, bulgarianMelancholy]
    
    # Instances - Sociological Fields
    historicalSociology = SociologicalField("HistoricalSociology")
    historicalSociology.label = "Historical Sociology"
    
    sociologyOfPolitics = SociologicalField("SociologyOfPolitics")
    sociologyOfPolitics.label = "Sociology of Politics"
    
    ethnosociology = SociologicalField("Ethnosociology")
    ethnosociology.label = "Ethnosociology"
    
    crisisOfLegitimacy = SociologicalField("CrisisOfLegitimacy")
    crisisOfLegitimacy.label = "Crisis of Legitimacy"
    
    sociologyOfValues = SociologicalField("SociologyOfValues")
    sociologyOfValues.label = "Sociology of Values"
    
    theoryAndHistoryOfSociology = SociologicalField("TheoryAndHistoryOfSociology")
    theoryAndHistoryOfSociology.label = "Theory and History of Sociology"
    
    modernSociology = SociologicalField("ModernSociology")
    modernSociology.label = "Modern Sociology"
    
    # Instances - Sociological Concepts
    multipleparadigmSociology = SociologicalConcept("MultipleparadigmSociology")
    multipleparadigmSociology.label = "Multiple paradigm sociology"
    
    dialogue = SociologicalConcept("Dialogue")
    dialogue.label = "Dialogue"
    
    dialogue.baseFor = [multipleparadigmSociology]
    dialogue.horizonFor = [multipleparadigmSociology]
    
    # Set Georgy's research interests
    georgyFotev.hasResearchInterest = [historicalSociology, sociologyOfPolitics, ethnosociology,
                                        crisisOfLegitimacy, sociologyOfValues, theoryAndHistoryOfSociology,
                                        modernSociology, multipleparadigmSociology, dialogue]
    
    # Instances - Award
    distinguishedServiceAward = Award("DistinguishedServiceAward")
    distinguishedServiceAward.label = "Distinguished Service Award"
    distinguishedServiceAward.awardYear = 2003
    distinguishedServiceAward.awardedBy = [americanUniversityInBulgaria]
    
    georgyFotev.receivedAward = [distinguishedServiceAward]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
