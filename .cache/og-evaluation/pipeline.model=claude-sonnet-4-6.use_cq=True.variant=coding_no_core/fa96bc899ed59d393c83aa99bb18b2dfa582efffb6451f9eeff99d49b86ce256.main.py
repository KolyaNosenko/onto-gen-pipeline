"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

1. What are the scientific research areas of a given sociologist?
2. What is the main focus of research interests of a specific scholar?
3. What publications has a given researcher authored?
4. What academic or governmental positions has a person held?
5. During which period did a person serve in a specific ministerial role?
6. What awards has a given academic received?
7. From which institution was a specific award granted?
8. In what year was a given award presented to a person?
9. At which university does a person hold an emeritus professorship?
10. What disciplinary fields does a researcher's work cover?
11. What is the date of birth of a given sociologist?
12. What nationality is a specific academic?
13. What themes are addressed in a researcher's published books?
14. Which books has a specific author written?
15. What role did a person hold in the field of education policy?
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
    # ── Entity classes ───────────────────────────────────────────────────────
    class Person(Thing): pass
    class Academic(Person): pass
    class Sociologist(Academic): pass

    class Publication(Thing): pass
    class Book(Publication): pass

    class ResearchArea(Thing): pass
    class DisciplinaryField(Thing): pass
    class ResearchTheme(Thing): pass

    class Organisation(Thing): pass
    class University(Organisation): pass

    class Position(Thing): pass
    class AcademicPosition(Position): pass
    class GovernmentalPosition(Position): pass
    class MinisterialRole(GovernmentalPosition): pass

    class Award(Thing): pass
    class Nationality(Thing): pass

    # ── Object properties ────────────────────────────────────────────────────
    class hasResearchArea(ObjectProperty):
        domain = [Sociologist]
        range  = [ResearchArea]

    class hasDisciplinaryField(ObjectProperty):
        domain = [Academic]
        range  = [DisciplinaryField]

    class hasResearchFocus(ObjectProperty, FunctionalProperty):
        domain = [Academic]
        range  = [ResearchTheme]

    class hasResearchTheme(ObjectProperty):
        domain = [Academic]
        range  = [ResearchTheme]

    class hasTheme(ObjectProperty):
        domain = [Publication]
        range  = [ResearchTheme]

    class authored(ObjectProperty):
        domain = [Person]
        range  = [Publication]

    class holdsPosition(ObjectProperty):
        domain = [Person]
        range  = [Position]

    class holdsEmeritusAt(ObjectProperty):
        domain = [Academic]
        range  = [University]

    class hasAward(ObjectProperty):
        domain = [Person]
        range  = [Award]

    class grantedBy(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range  = [Organisation]

    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range  = [Nationality]

    # ── Data properties ──────────────────────────────────────────────────────
    class dateOfBirth(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class serviceStartYear(DataProperty, FunctionalProperty):
        domain = [GovernmentalPosition]
        range  = [int]

    class serviceEndYear(DataProperty, FunctionalProperty):
        domain = [GovernmentalPosition]
        range  = [int]

    class awardYear(DataProperty, FunctionalProperty):
        domain = [Award]
        range  = [int]

    # ── Individuals ──────────────────────────────────────────────────────────

    # Nationality
    Bulgarian = Nationality("Bulgarian")
    Bulgarian.label = "Bulgarian"

    # Person
    GeorgyFotev = Sociologist("GeorgyFotev")
    GeorgyFotev.label = "Georgy Fotev"
    GeorgyFotev.dateOfBirth = "August 24, 1941"
    GeorgyFotev.hasNationality = Bulgarian

    # Research areas  ("theory and history of sociology")
    TheoryOfSociology = ResearchArea("TheoryOfSociology")
    TheoryOfSociology.label = "theory of sociology"

    HistoryOfSociology = ResearchArea("HistoryOfSociology")
    HistoryOfSociology.label = "history of sociology"

    GeorgyFotev.hasResearchArea = [TheoryOfSociology, HistoryOfSociology]

    # Disciplinary fields
    ModernSociology = DisciplinaryField("ModernSociology")
    ModernSociology.label = "modern sociology"

    HistoricalSociology = DisciplinaryField("HistoricalSociology")
    HistoricalSociology.label = "historical sociology"

    SociologyOfPolitics = DisciplinaryField("SociologyOfPolitics")
    SociologyOfPolitics.label = "sociology of politics"

    Ethnosociology = DisciplinaryField("Ethnosociology")
    Ethnosociology.label = "ethnosociology"

    CrisisOfLegitimacy = DisciplinaryField("CrisisOfLegitimacy")
    CrisisOfLegitimacy.label = "the crisis of legitimacy"

    SociologyOfValues = DisciplinaryField("SociologyOfValues")
    SociologyOfValues.label = "sociology of values"

    GeorgyFotev.hasDisciplinaryField = [
        ModernSociology, HistoricalSociology, SociologyOfPolitics,
        Ethnosociology, CrisisOfLegitimacy, SociologyOfValues,
    ]

    # Research themes
    NatureOfSociologyAsMultipleParadigmScience = ResearchTheme("NatureOfSociologyAsMultipleParadigmScience")
    NatureOfSociologyAsMultipleParadigmScience.label = "the nature of sociology as a multiple paradigm science"

    DialogueAsBaseAndHorizon = ResearchTheme("DialogueAsBaseAndHorizon")
    DialogueAsBaseAndHorizon.label = "the dialogue as a base and horizon of multiple paradigm sociology"

    DramaticFateOfBulgarianNationalSociety = ResearchTheme("DramaticFateOfBulgarianNationalSociety")
    DramaticFateOfBulgarianNationalSociety.label = "dramatic fate of the Bulgarian national society"

    GeorgyFotev.hasResearchFocus = NatureOfSociologyAsMultipleParadigmScience
    GeorgyFotev.hasResearchTheme = [DialogueAsBaseAndHorizon]

    # Books
    TheLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    TheLongNightOfCommunismInBulgaria.label = "The long night of communism in Bulgaria"
    TheLongNightOfCommunismInBulgaria.hasTheme = [DramaticFateOfBulgarianNationalSociety]

    BulgarianMelancholy = Book("BulgarianMelancholy")
    BulgarianMelancholy.label = "Bulgarian melancholy"
    BulgarianMelancholy.hasTheme = [DramaticFateOfBulgarianNationalSociety]

    GeorgyFotev.authored = [TheLongNightOfCommunismInBulgaria, BulgarianMelancholy]

    # Universities
    NewBulgarianUniversity = University("NewBulgarianUniversity")
    NewBulgarianUniversity.label = "New Bulgarian University"

    AmericanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    AmericanUniversityInBulgaria.label = "American University in Bulgaria"

    # Positions
    MinisterOfEducationAndSciencePos = MinisterialRole("MinisterOfEducationAndSciencePos")
    MinisterOfEducationAndSciencePos.label = "Minister of Education and Science"
    MinisterOfEducationAndSciencePos.serviceStartYear = 1991
    MinisterOfEducationAndSciencePos.serviceEndYear = 1992

    ProfessorEmeritusPos = AcademicPosition("ProfessorEmeritusPos")
    ProfessorEmeritusPos.label = "professor emeritus"

    GeorgyFotev.holdsPosition = [MinisterOfEducationAndSciencePos, ProfessorEmeritusPos]
    GeorgyFotev.holdsEmeritusAt = [NewBulgarianUniversity]

    # Award
    DistinguishedServiceAward = Award("DistinguishedServiceAward")
    DistinguishedServiceAward.label = "Distinguished Service Award"
    DistinguishedServiceAward.awardYear = 2003
    DistinguishedServiceAward.grantedBy = AmericanUniversityInBulgaria

    GeorgyFotev.hasAward = [DistinguishedServiceAward]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
