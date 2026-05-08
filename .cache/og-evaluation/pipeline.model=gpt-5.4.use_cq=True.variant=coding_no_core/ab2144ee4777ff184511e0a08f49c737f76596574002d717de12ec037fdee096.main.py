"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

What is Georgy Fotev’s date of birth?
What nationality is Georgy Fotev?
What is Georgy Fotev’s profession?
In which scientific areas has Georgy Fotev produced scholarly work?
What are the main research interests of Georgy Fotev?
How does Georgy Fotev characterize the nature of sociology?
What role does dialogue play in Georgy Fotev’s conception of multiple paradigm sociology?
In which disciplinary fields has Georgy Fotev published?
Has Georgy Fotev published works in historical sociology?
Has Georgy Fotev published works in sociology of politics?
Has Georgy Fotev published works in ethnosociology?
Has Georgy Fotev published works on the crisis of legitimacy?
Has Georgy Fotev published works in sociology of values?
What books by Georgy Fotev address the fate of Bulgarian national society?
What themes are explored in “The long night of communism in Bulgaria”?
What themes are explored in “Bulgarian melancholy”?
Did Georgy Fotev hold a government position in Bulgaria?
What public office did Georgy Fotev hold?
During which years was Georgy Fotev Minister of Education and Science?
Is Georgy Fotev affiliated with New Bulgarian University?
What academic title does Georgy Fotev hold at New Bulgarian University?
Did Georgy Fotev receive any awards?
What award did Georgy Fotev receive in 2003?
Which institution granted Georgy Fotev the Distinguished Service Award?
When was Georgy Fotev awarded the Distinguished Service Award from the American University in Bulgaria?
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
    class Person(Thing):
        pass

    class Sociologist(Person):
        pass

    class Country(Thing):
        pass

    class Nationality(Thing):
        pass

    class Organization(Thing):
        pass

    class University(Organization):
        pass

    class Publication(Thing):
        pass

    class Book(Publication):
        pass

    class ScholarlySubject(Thing):
        pass

    class ScientificArea(ScholarlySubject):
        pass

    class DisciplinaryField(ScholarlySubject):
        pass

    class ResearchTheme(ScholarlySubject):
        pass

    class ConceptualCharacterization(Thing):
        pass

    class PublicOffice(Thing):
        pass

    class AcademicTitle(Thing):
        pass

    class Award(Thing):
        pass

    class TimeEntity(Thing):
        pass

    class DateMention(TimeEntity):
        pass

    class Year(TimeEntity):
        pass

    class TimeInterval(TimeEntity):
        pass

    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Nationality]

    class birthDate(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [DateMention]

    class hasScholarlyWorkIn(ObjectProperty):
        domain = [Person]
        range = [ScholarlySubject]

    class hasResearchInterest(ObjectProperty):
        domain = [Person]
        range = [ResearchTheme]

    class characterizesNatureOfSociologyAs(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [ConceptualCharacterization]

    class regardsDialogueAs(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [ResearchTheme]

    class authored(ObjectProperty):
        domain = [Person]
        range = [Publication]

    class addressesTheme(ObjectProperty):
        domain = [Publication]
        range = [ResearchTheme]

    class holdsPublicOffice(ObjectProperty):
        domain = [Person]
        range = [PublicOffice]

    class publicOfficeInCountry(ObjectProperty, FunctionalProperty):
        domain = [PublicOffice]
        range = [Country]

    class heldPublicOfficeDuring(ObjectProperty):
        domain = [Person]
        range = [TimeInterval]

    class affiliatedWith(ObjectProperty):
        domain = [Person]
        range = [Organization]

    class holdsAcademicTitle(ObjectProperty):
        domain = [Person]
        range = [AcademicTitle]

    class professorEmeritusAt(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [University]

    class receivedAward(ObjectProperty):
        domain = [Person]
        range = [Award]

    class grantedBy(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range = [Organization]

    class awardedIn(ObjectProperty, FunctionalProperty):
        domain = [Award]
        range = [Year]

    georgyFotev = Sociologist("GeorgyFotevPerson")
    georgyFotev.label = ["Georgy Fotev", "G.Fotev"]

    bulgaria = Country("BulgariaCountry")
    bulgaria.label = "Bulgaria"

    bulgarianNationality = Nationality("BulgarianNationality")
    bulgarianNationality.label = "Bulgarian"

    august241941 = DateMention("August241941Date")
    august241941.label = "August 24 , 1941"

    years1991To1992 = TimeInterval("Years1991To1992")
    years1991To1992.label = "1991 - 1992"

    year2003 = Year("Year2003")
    year2003.label = "2003"

    theoryOfSociology = ScientificArea("TheoryOfSociologyArea")
    theoryOfSociology.label = "theory of sociology"

    historyOfSociology = ScientificArea("HistoryOfSociologyArea")
    historyOfSociology.label = "history of sociology"

    modernSociology = DisciplinaryField("ModernSociologyField")
    modernSociology.label = "modern sociology"

    historicalSociology = DisciplinaryField("HistoricalSociologyField")
    historicalSociology.label = "historical sociology"

    sociologyOfPolitics = DisciplinaryField("SociologyOfPoliticsField")
    sociologyOfPolitics.label = "sociology of politics"

    ethnosociology = DisciplinaryField("EthnosociologyField")
    ethnosociology.label = "ethnosociology"

    crisisOfLegitimacy = ResearchTheme("CrisisOfLegitimacyTheme")
    crisisOfLegitimacy.label = "the crisis of legitimacy"

    sociologyOfValues = DisciplinaryField("SociologyOfValuesField")
    sociologyOfValues.label = "sociology of values"

    natureOfSociologyAsMultipleParadigmScience = ResearchTheme(
        "NatureOfSociologyAsMultipleParadigmScienceTheme"
    )
    natureOfSociologyAsMultipleParadigmScience.label = (
        "the nature of sociology as a multiple paradigm science"
    )

    dialogueAsBaseAndHorizonOfMultipleParadigmSociology = ResearchTheme(
        "DialogueAsBaseAndHorizonOfMultipleParadigmSociologyTheme"
    )
    dialogueAsBaseAndHorizonOfMultipleParadigmSociology.label = (
        "the dialogue as a base and horizon of multiple paradigm sociology"
    )

    multipleParadigmScience = ConceptualCharacterization(
        "MultipleParadigmScienceCharacterization"
    )
    multipleParadigmScience.label = "multiple paradigm science"

    dramaticFateOfBulgarianNationalSociety = ResearchTheme(
        "DramaticFateOfBulgarianNationalSocietyTheme"
    )
    dramaticFateOfBulgarianNationalSociety.label = (
        "the dramatic fate of the Bulgarian national society"
    )

    ministerOfEducationAndScience = PublicOffice(
        "MinisterOfEducationAndScienceOffice"
    )
    ministerOfEducationAndScience.label = "Minister of Education and Science"

    professorEmeritus = AcademicTitle("ProfessorEmeritusTitle")
    professorEmeritus.label = "professor emeritus"

    newBulgarianUniversity = University("NewBulgarianUniversityInstance")
    newBulgarianUniversity.label = "New Bulgarian University"

    americanUniversityInBulgaria = University(
        "AmericanUniversityInBulgariaInstance"
    )
    americanUniversityInBulgaria.label = "American University in Bulgaria"

    distinguishedServiceAward = Award("DistinguishedServiceAwardInstance")
    distinguishedServiceAward.label = "Distinguished Service Award"

    theLongNightOfCommunismInBulgaria = Book(
        "TheLongNightOfCommunismInBulgariaBook"
    )
    theLongNightOfCommunismInBulgaria.label = [
        '" The long night of communism in Bulgaria "',
        "The long night of communism in Bulgaria",
    ]

    bulgarianMelancholy = Book("BulgarianMelancholyBook")
    bulgarianMelancholy.label = ['" Bulgarian melancholy "', "Bulgarian melancholy"]

    georgyFotev.hasNationality = bulgarianNationality
    georgyFotev.birthDate = august241941
    georgyFotev.hasScholarlyWorkIn = [
        theoryOfSociology,
        historyOfSociology,
        modernSociology,
        historicalSociology,
        sociologyOfPolitics,
        ethnosociology,
        crisisOfLegitimacy,
        sociologyOfValues,
    ]
    georgyFotev.hasResearchInterest = [
        natureOfSociologyAsMultipleParadigmScience,
        dialogueAsBaseAndHorizonOfMultipleParadigmSociology,
    ]
    georgyFotev.characterizesNatureOfSociologyAs = multipleParadigmScience
    georgyFotev.regardsDialogueAs = (
        dialogueAsBaseAndHorizonOfMultipleParadigmSociology
    )
    georgyFotev.authored = [
        theLongNightOfCommunismInBulgaria,
        bulgarianMelancholy,
    ]
    georgyFotev.holdsPublicOffice = [ministerOfEducationAndScience]
    georgyFotev.heldPublicOfficeDuring = [years1991To1992]
    georgyFotev.affiliatedWith = [newBulgarianUniversity]
    georgyFotev.holdsAcademicTitle = [professorEmeritus]
    georgyFotev.professorEmeritusAt = newBulgarianUniversity
    georgyFotev.receivedAward = [distinguishedServiceAward]

    ministerOfEducationAndScience.publicOfficeInCountry = bulgaria

    theLongNightOfCommunismInBulgaria.addressesTheme = [
        dramaticFateOfBulgarianNationalSociety
    ]
    bulgarianMelancholy.addressesTheme = [dramaticFateOfBulgarianNationalSociety]

    distinguishedServiceAward.grantedBy = americanUniversityInBulgaria
    distinguishedServiceAward.awardedIn = year2003


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
