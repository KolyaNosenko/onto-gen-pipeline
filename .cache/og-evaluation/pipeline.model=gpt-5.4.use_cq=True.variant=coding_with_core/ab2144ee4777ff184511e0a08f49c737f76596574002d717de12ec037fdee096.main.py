"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

What is Georgy Fotev’s date of birth?
What nationality is Georgy Fotev?
What is Georgy Fotev’s profession?
In which scientific areas has Georgy Fotev worked?
What are the main research interests of Georgy Fotev?
How does Georgy Fotev characterize the nature of sociology?
What role does dialogue play in Georgy Fotev’s view of multiple paradigm sociology?
In which disciplinary fields of modern sociology has Georgy Fotev published?
Has Georgy Fotev published works in historical sociology?
Has Georgy Fotev published works in sociology of politics?
Has Georgy Fotev published works in ethnosociology?
Has Georgy Fotev published works on the crisis of legitimacy?
Has Georgy Fotev published works in sociology of values?
What books by Georgy Fotev address the fate of Bulgarian national society?
What is the title of Georgy Fotev’s book about communism in Bulgaria?
What is the title of Georgy Fotev’s book about Bulgarian national melancholy?
What themes are illuminated by Georgy Fotev’s books “The long night of communism in Bulgaria” and “Bulgarian melancholy”?
Did Georgy Fotev hold a government office?
What government position did Georgy Fotev hold?
During which years was Georgy Fotev Minister of Education and Science?
At which university is Georgy Fotev professor emeritus?
Did Georgy Fotev receive any awards?
What award did Georgy Fotev receive in 2003?
Which institution granted Georgy Fotev the Distinguished Service Award?
When was Georgy Fotev awarded the Distinguished Service Award?
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
    NonAgentiveSocialObject,
    SocialObject,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class Person(AgentivePhysicalObject):
        label = ["Person"]


    class Sociologist(Person):
        label = ["Sociologist"]


    class Country(Society):
        label = ["Country"]


    class NationalSociety(Society):
        label = ["National Society"]


    class University(Society):
        label = ["University"]


    class ScientificArea(SocialObject):
        label = ["Scientific Area"]


    class DisciplinaryField(ScientificArea):
        label = ["Disciplinary Field"]


    class ResearchInterest(SocialObject):
        label = ["Research Interest"]


    class ScientificCharacterization(SocialObject):
        label = ["Scientific Characterization"]


    class DialogueConcept(SocialObject):
        label = ["Dialogue Concept"]


    class ScientificWork(NonAgentiveSocialObject):
        label = ["Scientific Work"]


    class Book(ScientificWork):
        label = ["Book"]


    class BookTheme(SocialObject):
        label = ["Book Theme"]


    class GovernmentOffice(NonAgentiveSocialObject):
        label = ["Government Office"]


    class Award(NonAgentiveSocialObject):
        label = ["Award"]


    class CalendarDate(TimeInterval):
        label = ["Calendar Date"]


    class CalendarYear(TimeInterval):
        label = ["Calendar Year"]


    class YearRange(TimeInterval):
        label = ["Year Range"]


    class hasNationality(ObjectProperty):
        domain = [Person]
        range = [Country]
        label = ["has nationality"]


    class hasScientificWorkInArea(ObjectProperty):
        domain = [Person]
        range = [ScientificArea]
        label = ["has scientific work in area"]


    class hasResearchInterest(ObjectProperty):
        domain = [Person]
        range = [ResearchInterest]
        label = ["has research interest"]


    class characterizesSociologyAs(ObjectProperty):
        domain = [Person]
        range = [ScientificCharacterization]
        label = ["characterizes sociology as"]


    class hasPublicationInField(ObjectProperty):
        domain = [Person]
        range = [DisciplinaryField]
        label = ["has publication in field"]


    class authorOf(ObjectProperty):
        domain = [Person]
        range = [ScientificWork]
        label = ["author of"]


    class illuminatesTheme(ObjectProperty):
        domain = [ScientificWork]
        range = [BookTheme]
        label = ["illuminates theme"]


    class concernsSociety(ObjectProperty):
        domain = [BookTheme]
        range = [NationalSociety]
        label = ["concerns society"]


    class heldGovernmentOffice(ObjectProperty):
        domain = [Person]
        range = [GovernmentOffice]
        label = ["held government office"]


    class professorEmeritusAt(ObjectProperty):
        domain = [Person]
        range = [University]
        label = ["professor emeritus at"]


    class receivedAward(ObjectProperty):
        domain = [Person]
        range = [Award]
        label = ["received award"]


    class grantedBy(ObjectProperty):
        domain = [Award]
        range = [University]
        label = ["granted by"]


    class baseOf(ObjectProperty):
        domain = [DialogueConcept]
        range = [ScientificArea]
        label = ["base of"]


    class horizonOf(ObjectProperty):
        domain = [DialogueConcept]
        range = [ScientificArea]
        label = ["horizon of"]


    class disciplinaryFieldOf(partOf):
        domain = [DisciplinaryField]
        range = [ScientificArea]
        label = ["disciplinary field of"]


    class hasDateOfBirth(temporallyLocatedAt):
        domain = [Person]
        range = [CalendarDate]
        label = ["has date of birth"]


    class heldOfficeDuring(temporallyLocatedAt):
        domain = [GovernmentOffice]
        range = [YearRange]
        label = ["held office during"]


    class awardedIn(temporallyLocatedAt):
        domain = [Award]
        range = [CalendarYear]
        label = ["awarded in"]


    class yearNumber(DataProperty, FunctionalProperty):
        domain = [CalendarYear]
        range = [int]
        label = ["year number"]


    class startYear(DataProperty, FunctionalProperty):
        domain = [YearRange]
        range = [int]
        label = ["start year"]


    class endYear(DataProperty, FunctionalProperty):
        domain = [YearRange]
        range = [int]
        label = ["end year"]


    class dateValue(DataProperty, FunctionalProperty):
        domain = [CalendarDate]
        range = [str]
        label = ["date value"]


    Sociologist.is_a.append(hasScientificWorkInArea.some(ScientificArea))
    Book.is_a.append(illuminatesTheme.some(BookTheme))
    Award.is_a.append(grantedBy.some(University))

    GeorgyFotev = Sociologist("GeorgyFotev")
    GeorgyFotev.label = ["Georgy Fotev", "G.Fotev"]

    Bulgaria = Country("Bulgaria")
    Bulgaria.label = "Bulgaria"

    NewBulgarianUniversity = University("NewBulgarianUniversity")
    NewBulgarianUniversity.label = "New Bulgarian University"

    AmericanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    AmericanUniversityInBulgaria.label = "American University in Bulgaria"

    DistinguishedServiceAward = Award("DistinguishedServiceAward")
    DistinguishedServiceAward.label = "Distinguished Service Award"

    TheLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    TheLongNightOfCommunismInBulgaria.label = "The long night of communism in Bulgaria"

    BulgarianMelancholy = Book("BulgarianMelancholy")
    BulgarianMelancholy.label = "Bulgarian melancholy"

    August241941 = CalendarDate("August24_1941")
    August241941.label = "August 24 , 1941"
    August241941.dateValue = "1941-08-24"

    Years19911992 = YearRange("Years1991_1992")
    Years19911992.label = "1991 - 1992"
    Years19911992.startYear = 1991
    Years19911992.endYear = 1992

    Year2003 = CalendarYear("Year2003")
    Year2003.label = "2003"
    Year2003.yearNumber = 2003

    MinisterOfEducationAndScience = GovernmentOffice("MinisterOfEducationAndScience")
    MinisterOfEducationAndScience.label = "Minister of Education and Science"

    TheoryOfSociology = ScientificArea("TheoryOfSociology")
    TheoryOfSociology.label = "theory of sociology"

    HistoryOfSociology = ScientificArea("HistoryOfSociology")
    HistoryOfSociology.label = "history of sociology"

    ModernSociology = ScientificArea("ModernSociology")
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

    MultipleParadigmScience = ScientificCharacterization("MultipleParadigmScience")
    MultipleParadigmScience.label = "multiple paradigm science"

    MultipleParadigmSociology = ScientificArea("MultipleParadigmSociology")
    MultipleParadigmSociology.label = "multiple paradigm sociology"

    Dialogue = DialogueConcept("Dialogue")
    Dialogue.label = "dialogue"

    NatureOfSociologyAsAMultipleParadigmScience = ResearchInterest(
        "NatureOfSociologyAsAMultipleParadigmScience"
    )
    NatureOfSociologyAsAMultipleParadigmScience.label = (
        "the nature of sociology as a multiple paradigm science"
    )

    DialogueAsABaseAndHorizonOfMultipleParadigmSociology = ResearchInterest(
        "DialogueAsABaseAndHorizonOfMultipleParadigmSociology"
    )
    DialogueAsABaseAndHorizonOfMultipleParadigmSociology.label = (
        "the dialogue as a base and horizon of multiple paradigm sociology"
    )

    TheDramaticFateOfTheBulgarianNationalSociety = BookTheme(
        "TheDramaticFateOfTheBulgarianNationalSociety"
    )
    TheDramaticFateOfTheBulgarianNationalSociety.label = (
        "the dramatic fate of the Bulgarian national society"
    )

    BulgarianNationalSociety = NationalSociety("BulgarianNationalSociety")
    BulgarianNationalSociety.label = "the Bulgarian national society"

    GeorgyFotev.hasDateOfBirth = August241941
    GeorgyFotev.hasNationality = [Bulgaria]
    GeorgyFotev.hasScientificWorkInArea = [
        TheoryOfSociology,
        HistoryOfSociology,
        ModernSociology,
    ]
    GeorgyFotev.hasResearchInterest = [
        NatureOfSociologyAsAMultipleParadigmScience,
        DialogueAsABaseAndHorizonOfMultipleParadigmSociology,
    ]
    GeorgyFotev.characterizesSociologyAs = [MultipleParadigmScience]
    GeorgyFotev.hasPublicationInField = [
        HistoricalSociology,
        SociologyOfPolitics,
        Ethnosociology,
        CrisisOfLegitimacy,
        SociologyOfValues,
    ]
    GeorgyFotev.authorOf = [
        TheLongNightOfCommunismInBulgaria,
        BulgarianMelancholy,
    ]
    GeorgyFotev.heldGovernmentOffice = [MinisterOfEducationAndScience]
    GeorgyFotev.professorEmeritusAt = [NewBulgarianUniversity]
    GeorgyFotev.receivedAward = [DistinguishedServiceAward]

    HistoricalSociology.disciplinaryFieldOf = [ModernSociology]
    SociologyOfPolitics.disciplinaryFieldOf = [ModernSociology]
    Ethnosociology.disciplinaryFieldOf = [ModernSociology]
    CrisisOfLegitimacy.disciplinaryFieldOf = [ModernSociology]
    SociologyOfValues.disciplinaryFieldOf = [ModernSociology]

    Dialogue.baseOf = [MultipleParadigmSociology]
    Dialogue.horizonOf = [MultipleParadigmSociology]

    TheLongNightOfCommunismInBulgaria.illuminatesTheme = [
        TheDramaticFateOfTheBulgarianNationalSociety,
    ]
    BulgarianMelancholy.illuminatesTheme = [
        TheDramaticFateOfTheBulgarianNationalSociety,
    ]
    TheDramaticFateOfTheBulgarianNationalSociety.concernsSociety = [
        BulgarianNationalSociety,
    ]

    MinisterOfEducationAndScience.heldOfficeDuring = Years19911992
    DistinguishedServiceAward.grantedBy = [AmericanUniversityInBulgaria]
    DistinguishedServiceAward.awardedIn = Year2003


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
