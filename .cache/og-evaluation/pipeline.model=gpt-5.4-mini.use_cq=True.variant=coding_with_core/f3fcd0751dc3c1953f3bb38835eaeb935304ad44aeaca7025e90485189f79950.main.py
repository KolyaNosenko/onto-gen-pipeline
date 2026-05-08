"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

1. Who is Georgy Fotev?  
2. What is Georgy Fotev’s date of birth?  
3. What is Georgy Fotev’s nationality?  
4. What is Georgy Fotev’s profession or occupation?  
5. What are the main scientific areas of Georgy Fotev’s work?  
6. What is the main research focus of Georgy Fotev?  
7. What major theme appears in Georgy Fotev’s works besides the nature of sociology?  
8. In which disciplinary fields has Georgy Fotev published?  
9. What books did Georgy Fotev write?  
10. What do Georgy Fotev’s books “The long night of communism in Bulgaria” and “Bulgarian melancholy” address?  
11. What political office did Georgy Fotev hold?  
12. During which years did Georgy Fotev serve as Minister of Education and Science?  
13. What academic title does Georgy Fotev hold at New Bulgarian University?  
14. What award did Georgy Fotev receive in 2003?  
15. Which institution awarded Georgy Fotev the Distinguished Service Award?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from datetime import date

from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core
from og_sandbox_with_core.core.entities import (
    Abstract,
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    SocialObject,
    TimeInterval,
)


with core:
    class Person(AgentivePhysicalObject):
        pass

    class University(SocialObject):
        pass

    class ScientificArea(Abstract):
        pass

    class ResearchFocus(Abstract):
        pass

    class Theme(Abstract):
        pass

    class Topic(Abstract):
        pass

    class PublicationField(ScientificArea):
        pass

    class Book(NonAgentivePhysicalObject):
        pass

    class Award(NonAgentiveSocialObject):
        pass

    class Sociologist(Person):
        pass

    class BulgarianSociologist(Sociologist):
        pass

    class MinisterOfEducationAndScience(Person):
        pass

    class ProfessorEmeritus(Person):
        pass

    class birthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [date]

    class nationality(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class hasScientificArea(ObjectProperty):
        domain = [Person]
        range = [ScientificArea]

    class mainResearchFocus(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [ResearchFocus]

    class majorTheme(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Theme]

    class hasPublicationField(ObjectProperty):
        domain = [Person]
        range = [PublicationField]

    class wroteBook(ObjectProperty):
        domain = [Person]
        range = [Book]

    class addressesTopic(ObjectProperty):
        domain = [Book]
        range = [Topic]

    class servedDuring(ObjectProperty, FunctionalProperty):
        domain = [MinisterOfEducationAndScience]
        range = [TimeInterval]

    class professorEmeritusOf(ObjectProperty, FunctionalProperty):
        domain = [ProfessorEmeritus]
        range = [University]

    class receivedAward(ObjectProperty):
        domain = [Person]
        range = [Award]

    class awardedBy(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range = [University]

    class awardedIn(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range = [TimeInterval]

    Sociologist.is_a.append(hasScientificArea.some(ScientificArea))
    MinisterOfEducationAndScience.is_a.append(servedDuring.some(TimeInterval))
    ProfessorEmeritus.is_a.append(professorEmeritusOf.some(University))
    Book.is_a.append(addressesTopic.some(Topic))
    Award.is_a.append(awardedBy.some(University))
    Award.is_a.append(awardedIn.some(TimeInterval))

    GeorgyFotev = BulgarianSociologist("GeorgyFotev")
    Person("GeorgyFotev")
    Sociologist("GeorgyFotev")
    GeorgyFotev.label = "Georgy Fotev"
    GeorgyFotev.birthDate = date(1941, 8, 24)
    GeorgyFotev.nationality = "Bulgarian"
    MinisterOfEducationAndScience("GeorgyFotev")
    ProfessorEmeritus("GeorgyFotev")

    TheoryOfSociology = ScientificArea("TheoryOfSociology")
    TheoryOfSociology.label = "theory of sociology"
    HistoryOfSociology = ScientificArea("HistoryOfSociology")
    HistoryOfSociology.label = "history of sociology"
    DisciplinaryFieldsOfModernSociology = ScientificArea("DisciplinaryFieldsOfModernSociology")
    DisciplinaryFieldsOfModernSociology.label = "disciplinary fields of modern sociology"
    GeorgyFotev.hasScientificArea.append(TheoryOfSociology)
    GeorgyFotev.hasScientificArea.append(HistoryOfSociology)
    GeorgyFotev.hasScientificArea.append(DisciplinaryFieldsOfModernSociology)

    NatureOfSociologyAsAMultipleParadigmScience = ResearchFocus("NatureOfSociologyAsAMultipleParadigmScience")
    NatureOfSociologyAsAMultipleParadigmScience.label = "the nature of sociology as a multiple paradigm science"
    GeorgyFotev.mainResearchFocus = NatureOfSociologyAsAMultipleParadigmScience

    DialogueAsBaseAndHorizonOfMultipleParadigmSociology = Theme("DialogueAsBaseAndHorizonOfMultipleParadigmSociology")
    DialogueAsBaseAndHorizonOfMultipleParadigmSociology.label = "dialogue as a base and horizon of multiple paradigm sociology"
    GeorgyFotev.majorTheme = DialogueAsBaseAndHorizonOfMultipleParadigmSociology

    HistoricalSociology = PublicationField("HistoricalSociology")
    HistoricalSociology.label = "historical sociology"
    SociologyOfPolitics = PublicationField("SociologyOfPolitics")
    SociologyOfPolitics.label = "sociology of politics"
    Ethnosociology = PublicationField("Ethnosociology")
    Ethnosociology.label = "ethnosociology"
    CrisisOfLegitimacy = PublicationField("CrisisOfLegitimacy")
    CrisisOfLegitimacy.label = "the crisis of legitimacy"
    SociologyOfValues = PublicationField("SociologyOfValues")
    SociologyOfValues.label = "sociology of values"
    GeorgyFotev.hasPublicationField.append(HistoricalSociology)
    GeorgyFotev.hasPublicationField.append(SociologyOfPolitics)
    GeorgyFotev.hasPublicationField.append(Ethnosociology)
    GeorgyFotev.hasPublicationField.append(CrisisOfLegitimacy)
    GeorgyFotev.hasPublicationField.append(SociologyOfValues)

    TheLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    TheLongNightOfCommunismInBulgaria.label = "The long night of communism in Bulgaria"
    BulgarianMelancholy = Book("BulgarianMelancholy")
    BulgarianMelancholy.label = "Bulgarian melancholy"
    DramaticFateOfTheBulgarianNationalSociety = Topic("DramaticFateOfTheBulgarianNationalSociety")
    DramaticFateOfTheBulgarianNationalSociety.label = "the dramatic fate of the Bulgarian national society"
    TheLongNightOfCommunismInBulgaria.addressesTopic.append(DramaticFateOfTheBulgarianNationalSociety)
    BulgarianMelancholy.addressesTopic.append(DramaticFateOfTheBulgarianNationalSociety)
    GeorgyFotev.wroteBook.append(TheLongNightOfCommunismInBulgaria)
    GeorgyFotev.wroteBook.append(BulgarianMelancholy)

    NewBulgarianUniversity = University("NewBulgarianUniversity")
    NewBulgarianUniversity.label = "New Bulgarian University"
    GeorgyFotev.professorEmeritusOf = NewBulgarianUniversity

    MinisterOfEducationAndScienceTenure1991_1992 = TimeInterval("MinisterOfEducationAndScienceTenure1991_1992")
    MinisterOfEducationAndScienceTenure1991_1992.label = "1991 - 1992"
    GeorgyFotev.servedDuring = MinisterOfEducationAndScienceTenure1991_1992

    DistinguishedServiceAward = Award("DistinguishedServiceAward")
    DistinguishedServiceAward.label = "Distinguished Service Award"
    AmericanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    AmericanUniversityInBulgaria.label = "American University in Bulgaria"
    GeorgyFotev.receivedAward.append(DistinguishedServiceAward)
    DistinguishedServiceAward.awardedBy = AmericanUniversityInBulgaria
    Year2003 = TimeInterval("Year2003")
    Year2003.label = "2003"
    DistinguishedServiceAward.awardedIn = Year2003


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
