"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

1. What are the scientific fields in which a sociologist conducts their research?
2. What is the primary focus of a researcher's academic interests?
3. What publications has a sociologist authored?
4. What government positions has a person held, and during what time period?
5. At which university does a professor hold an emeritus position?
6. What awards has a person received, and from which institution?
7. In what year was a person born?
8. What is the nationality of a given sociologist?
9. What major themes are explored in a researcher's body of work?
10. Which books has an author written that address the history of a specific national society?
11. What academic titles or honors has a person been granted?
12. In which disciplinary fields of sociology has a researcher published work?
13. What is the relationship between a person's ministerial role and their academic career?
14. From which institution was a person awarded a distinguished service recognition?
15. What is the nature of the sociological science a researcher specializes in?
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
    AgentivePhysicalObject,
    MentalObject,
    NonAgentiveSocialObject,
    SocialAgent,
    Society,
    TimeInterval,
)


with core:
    # ── Entity Classes ────────────────────────────────────────────────

    class Sociologist(AgentivePhysicalObject):
        """A person who practises sociology as a profession."""

    class Publication(NonAgentiveSocialObject):
        """A scholarly publication (article, chapter, book, etc.)."""

    class Book(Publication):
        """A book-length scholarly publication."""

    class ScientificField(NonAgentiveSocialObject):
        """An academic or scientific discipline or sub-field."""

    class ResearchTopic(MentalObject):
        """A conceptual topic or theme that a researcher focuses on;
        existentially depends on the researcher."""

    class GovernmentPosition(SocialAgent):
        """An individual government ministerial or official role."""

    class University(Society):
        """A higher-education and research institution."""

    class NationalSociety(Society):
        """A national collective society (a people / nation)."""

    class AcademicTitle(NonAgentiveSocialObject):
        """An academic rank or honorary title (e.g. professor emeritus)."""

    class Award(NonAgentiveSocialObject):
        """An award or honour bestowed on a person by an institution."""

    # ── Object & Data Properties ──────────────────────────────────────

    class hasScientificField(ObjectProperty):
        """Relates a sociologist to a scientific field in which they work
        or publish."""
        domain = [Sociologist]
        range  = [ScientificField]

    class hasFocus(ObjectProperty, FunctionalProperty):
        """The primary research focus of a sociologist (at most one)."""
        domain = [Sociologist]
        range  = [ResearchTopic]

    class hasResearchTheme(ObjectProperty):
        """A major theme explored in a researcher's body of work."""
        domain = [Sociologist]
        range  = [ResearchTopic]

    class authored(ObjectProperty):
        """Relates a person to a publication they wrote."""
        domain = [AgentivePhysicalObject]
        range  = [Publication]

    class heldPosition(ObjectProperty):
        """Relates a person to a government position they have held."""
        domain = [AgentivePhysicalObject]
        range  = [GovernmentPosition]

    class positionDuring(ObjectProperty):
        """Relates a government position to the time interval it was held."""
        domain = [GovernmentPosition]
        range  = [TimeInterval]

    class holdsAcademicTitleAt(ObjectProperty):
        """Relates a person to the university at which they hold an
        academic title."""
        domain = [AgentivePhysicalObject]
        range  = [University]

    class hasAcademicTitle(ObjectProperty):
        """Relates a person to an academic title or rank they hold."""
        domain = [AgentivePhysicalObject]
        range  = [AcademicTitle]

    class receivedAward(ObjectProperty):
        """Relates a person to an award they have received."""
        domain = [AgentivePhysicalObject]
        range  = [Award]

    class awardedBy(ObjectProperty):
        """Relates an award to the institution that granted it."""
        domain = [Award]
        range  = [University]

    class awardedIn(ObjectProperty):
        """Relates an award to the time interval in which it was granted."""
        domain = [Award]
        range  = [TimeInterval]

    class addressesNationalSociety(ObjectProperty):
        """Relates a book to the national society whose history or fate it
        discusses."""
        domain = [Book]
        range  = [NationalSociety]

    class hasNationality(DataProperty, FunctionalProperty):
        """The nationality of a person, expressed as a string."""
        domain = [AgentivePhysicalObject]
        range  = [str]

    class birthYear(DataProperty, FunctionalProperty):
        """The birth year of a person as an integer."""
        domain = [AgentivePhysicalObject]
        range  = [int]

    class birthDate(DataProperty, FunctionalProperty):
        """The full birth date of a person as a string."""
        domain = [AgentivePhysicalObject]
        range  = [str]

    # ── Named Individuals ─────────────────────────────────────────────

    # Person
    GeorgyFotev = Sociologist("GeorgyFotev")
    GeorgyFotev.label       = "Georgy Fotev"
    GeorgyFotev.birthDate   = "August 24, 1941"
    GeorgyFotev.birthYear   = 1941
    GeorgyFotev.hasNationality = "Bulgarian"

    # Books
    TheLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    TheLongNightOfCommunismInBulgaria.label = "The long night of communism in Bulgaria"

    BulgarianMelancholy = Book("BulgarianMelancholy")
    BulgarianMelancholy.label = "Bulgarian melancholy"

    # Scientific fields
    TheoryAndHistoryOfSociology = ScientificField("TheoryAndHistoryOfSociology")
    TheoryAndHistoryOfSociology.label = "theory and history of sociology"

    DisciplinaryFieldsOfModernSociology = ScientificField("DisciplinaryFieldsOfModernSociology")
    DisciplinaryFieldsOfModernSociology.label = "disciplinary fields of modern sociology"

    HistoricalSociology = ScientificField("HistoricalSociology")
    HistoricalSociology.label = "historical sociology"

    SociologyOfPoliticsField = ScientificField("SociologyOfPoliticsField")
    SociologyOfPoliticsField.label = "sociology of politics"

    EthnosociologyField = ScientificField("EthnosociologyField")
    EthnosociologyField.label = "ethnosociology"

    CrisisOfLegitimacyField = ScientificField("CrisisOfLegitimacyField")
    CrisisOfLegitimacyField.label = "crisis of legitimacy"

    SociologyOfValuesField = ScientificField("SociologyOfValuesField")
    SociologyOfValuesField.label = "sociology of values"

    # Research topics
    NatureOfSociologyAsMultipleParadigmScience = ResearchTopic(
        "NatureOfSociologyAsMultipleParadigmScience"
    )
    NatureOfSociologyAsMultipleParadigmScience.label = (
        "nature of sociology as a multiple paradigm science"
    )

    DialogueAsBaseAndHorizon = ResearchTopic("DialogueAsBaseAndHorizon")
    DialogueAsBaseAndHorizon.label = (
        "dialogue as a base and horizon of multiple paradigm sociology"
    )

    # Government position
    MinisterOfEducationAndSciencePos = GovernmentPosition(
        "MinisterOfEducationAndSciencePos"
    )
    MinisterOfEducationAndSciencePos.label = "Minister of Education and Science"

    # Time intervals
    Interval19911992 = TimeInterval("Interval19911992")
    Interval19911992.label = "1991 - 1992"

    Year2003 = TimeInterval("Year2003")
    Year2003.label = "2003"

    # Universities
    NewBulgarianUniversity = University("NewBulgarianUniversity")
    NewBulgarianUniversity.label = "New Bulgarian University"

    AmericanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    AmericanUniversityInBulgaria.label = "American University in Bulgaria"

    # Academic title
    ProfessorEmeritusTitle = AcademicTitle("ProfessorEmeritusTitle")
    ProfessorEmeritusTitle.label = "professor emeritus"

    # Award
    DistinguishedServiceAwardInst = Award("DistinguishedServiceAwardInst")
    DistinguishedServiceAwardInst.label = "Distinguished Service Award"

    # National society
    BulgarianNationalSociety = NationalSociety("BulgarianNationalSociety")
    BulgarianNationalSociety.label = "Bulgarian national society"

    # ── Property Assertions ───────────────────────────────────────────

    GeorgyFotev.hasScientificField = [
        TheoryAndHistoryOfSociology,
        DisciplinaryFieldsOfModernSociology,
        HistoricalSociology,
        SociologyOfPoliticsField,
        EthnosociologyField,
        CrisisOfLegitimacyField,
        SociologyOfValuesField,
    ]
    GeorgyFotev.hasFocus        = NatureOfSociologyAsMultipleParadigmScience
    GeorgyFotev.hasResearchTheme = [DialogueAsBaseAndHorizon]
    GeorgyFotev.authored         = [TheLongNightOfCommunismInBulgaria, BulgarianMelancholy]
    GeorgyFotev.heldPosition     = [MinisterOfEducationAndSciencePos]
    GeorgyFotev.holdsAcademicTitleAt = [NewBulgarianUniversity]
    GeorgyFotev.hasAcademicTitle     = [ProfessorEmeritusTitle]
    GeorgyFotev.receivedAward        = [DistinguishedServiceAwardInst]

    MinisterOfEducationAndSciencePos.positionDuring = [Interval19911992]

    DistinguishedServiceAwardInst.awardedBy = [AmericanUniversityInBulgaria]
    DistinguishedServiceAwardInst.awardedIn = [Year2003]

    TheLongNightOfCommunismInBulgaria.addressesNationalSociety = [BulgarianNationalSociety]
    BulgarianMelancholy.addressesNationalSociety               = [BulgarianNationalSociety]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
