"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

Who is Georgy Fotev?  
When was Georgy Fotev born?  
What is Georgy Fotev’s nationality?  
What is Georgy Fotev’s profession or occupation?  
In which scientific areas has Georgy Fotev worked?  
What is the main research focus of Georgy Fotev?  
What major theme appears in Georgy Fotev’s works?  
In which fields has Georgy Fotev published?  
What books did Georgy Fotev write?  
What topics do Georgy Fotev’s books “The long night of communism in Bulgaria” and “Bulgarian melancholy” address?  
What government position did Georgy Fotev hold?  
During which years did Georgy Fotev serve as Minister of Education and Science?  
What is Georgy Fotev’s academic title at New Bulgarian University?  
What award did Georgy Fotev receive in 2003?  
Which institution awarded Georgy Fotev the Distinguished Service Award?
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
    class Person(Thing):
        pass

    class Scientist(Person):
        pass

    class Sociologist(Scientist):
        pass

    class Organization(Thing):
        pass

    class University(Organization):
        pass

    class Country(Thing):
        pass

    class Award(Thing):
        pass

    class GovernmentPosition(Thing):
        pass

    class AcademicTitle(Thing):
        pass

    class Book(Thing):
        pass

    class Field(Thing):
        pass

    class ResearchFocus(Thing):
        pass

    class ResearchTheme(Thing):
        pass

    class Topic(Thing):
        pass

    # Properties
    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Country]

    class bornOn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class worksInField(ObjectProperty):
        domain = [Person]
        range = [Field]

    class publishesInField(ObjectProperty):
        domain = [Person]
        range = [Field]

    class hasResearchFocus(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [ResearchFocus]

    class hasMajorTheme(ObjectProperty):
        domain = [Person]
        range = [ResearchTheme]

    class wroteBook(ObjectProperty):
        domain = [Person]
        range = [Book]

    class hasTopic(ObjectProperty):
        domain = [Book]
        range = [Topic]

    class heldPosition(ObjectProperty):
        domain = [Person]
        range = [GovernmentPosition]

    class positionStartYear(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range = [int]

    class positionEndYear(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range = [int]

    class hasAcademicTitle(ObjectProperty):
        domain = [Person]
        range = [AcademicTitle]

    class affiliatedWith(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [University]

    class receivedAward(ObjectProperty):
        domain = [Person]
        range = [Award]

    class awardedBy(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range = [Organization]

    class awardedInYear(DataProperty, FunctionalProperty):
        domain = [Award]
        range = [int]

    # Individuals
    GeorgyFotev = Person("GeorgyFotev")
    GeorgyFotev.label = ["Georgy Fotev", "G.Fotev"]
    GeorgyFotev.is_a = [Sociologist]
    GeorgyFotev.hasNationality = Country("Bulgaria")
    GeorgyFotev.hasNationality.label = "Bulgaria"
    GeorgyFotev.bornOn = "August 24, 1941"

    TheoryOfSociology = Field("TheoryOfSociology")
    TheoryOfSociology.label = "theory of sociology"
    HistoryOfSociology = Field("HistoryOfSociology")
    HistoryOfSociology.label = "history of sociology"
    ModernSociology = Field("ModernSociology")
    ModernSociology.label = "modern sociology"
    HistoricalSociology = Field("HistoricalSociology")
    HistoricalSociology.label = "historical sociology"
    SociologyOfPolitics = Field("SociologyOfPolitics")
    SociologyOfPolitics.label = "sociology of politics"
    Ethnosociology = Field("Ethnosociology")
    Ethnosociology.label = "ethnosociology"
    CrisisOfLegitimacy = Field("CrisisOfLegitimacy")
    CrisisOfLegitimacy.label = "the crisis of legitimacy"
    SociologyOfValues = Field("SociologyOfValues")
    SociologyOfValues.label = "sociology of values"

    NatureOfSociologyAsAMultipleParadigmScience = ResearchFocus("NatureOfSociologyAsAMultipleParadigmScience")
    NatureOfSociologyAsAMultipleParadigmScience.label = "the nature of sociology as a multiple paradigm science"
    DialogueAsBaseAndHorizonOfMultipleParadigmSociology = ResearchTheme("DialogueAsBaseAndHorizonOfMultipleParadigmSociology")
    DialogueAsBaseAndHorizonOfMultipleParadigmSociology.label = "the dialogue as a base and horizon of multiple paradigm sociology"
    DramaticFateOfBulgarianNationalSociety = Topic("DramaticFateOfBulgarianNationalSociety")
    DramaticFateOfBulgarianNationalSociety.label = "the dramatic fate of the Bulgarian national society"

    TheLongNightOfCommunismInBulgaria = Book("TheLongNightOfCommunismInBulgaria")
    TheLongNightOfCommunismInBulgaria.label = '"The long night of communism in Bulgaria"'
    BulgarianMelancholy = Book("BulgarianMelancholy")
    BulgarianMelancholy.label = '"Bulgarian melancholy"'

    MinisterOfEducationAndScience = GovernmentPosition("MinisterOfEducationAndScience")
    MinisterOfEducationAndScience.label = "Minister of Education and Science"
    MinisterOfEducationAndScience.positionStartYear = 1991
    MinisterOfEducationAndScience.positionEndYear = 1992

    ProfessorEmeritus = AcademicTitle("ProfessorEmeritus")
    ProfessorEmeritus.label = "professor emeritus"

    NewBulgarianUniversity = University("NewBulgarianUniversity")
    NewBulgarianUniversity.label = "New Bulgarian University"

    AmericanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    AmericanUniversityInBulgaria.label = "American University in Bulgaria"

    DistinguishedServiceAward = Award("DistinguishedServiceAward")
    DistinguishedServiceAward.label = "Distinguished Service Award"
    DistinguishedServiceAward.awardedBy = AmericanUniversityInBulgaria
    DistinguishedServiceAward.awardedInYear = 2003

    GeorgyFotev.worksInField = [TheoryOfSociology, HistoryOfSociology, ModernSociology]
    GeorgyFotev.publishesInField = [HistoricalSociology, SociologyOfPolitics, Ethnosociology, CrisisOfLegitimacy, SociologyOfValues]
    GeorgyFotev.hasResearchFocus = NatureOfSociologyAsAMultipleParadigmScience
    GeorgyFotev.hasMajorTheme = [DialogueAsBaseAndHorizonOfMultipleParadigmSociology]
    GeorgyFotev.wroteBook = [TheLongNightOfCommunismInBulgaria, BulgarianMelancholy]
    GeorgyFotev.heldPosition = [MinisterOfEducationAndScience]
    GeorgyFotev.hasAcademicTitle = [ProfessorEmeritus]
    GeorgyFotev.affiliatedWith = NewBulgarianUniversity
    GeorgyFotev.receivedAward = [DistinguishedServiceAward]

    TheLongNightOfCommunismInBulgaria.hasTopic = [DramaticFateOfBulgarianNationalSociety]
    BulgarianMelancholy.hasTopic = [DramaticFateOfBulgarianNationalSociety]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
