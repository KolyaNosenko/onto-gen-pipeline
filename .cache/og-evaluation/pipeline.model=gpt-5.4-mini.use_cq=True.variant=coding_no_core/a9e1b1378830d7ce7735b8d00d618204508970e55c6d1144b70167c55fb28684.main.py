"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. Who co-authored the book *My Vision — Challenges in the Race for Excellence*?
2. What is the Arabic title of *My Vision — Challenges in the Race for Excellence*?
3. Who is the author of *My Vision — Challenges in the Race for Excellence*?
4. What positions does Mohammed bin Rashid Al Maktoum hold?
5. What is the role of Dubai in relation to Mohammed bin Rashid Al Maktoum?
6. What is the title of the book that presents the vision of His Highness regarding development and excellence in the UAE and Dubai?
7. What is the main theme or vision presented in the book?
8. How many pages does the book contain?
9. What is the physical size or format of the book?
10. How many sets of photographs are included in the book?
11. What types of photographs are included in the book?
12. Are there any personal images in the book that were published for the first time?
13. How many parts does the book include?
14. What are the five parts of the book?
15. Does the book relate the story of development and excellence in Dubai?
16. What regions or entities are discussed in the context of development and excellence in the book?
17. Who is the ruler of Dubai mentioned in the book description?
18. Who is the Vice President of the United Arab Emirates mentioned in the book description?
19. What is the relationship between the book and Dubai’s development experience?
20. Is the book associated with public images, personal images, or both?
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
    class Book(Thing):
        pass

    class Person(Thing):
        pass

    class Region(Thing):
        pass

    class Country(Region):
        pass

    class Emirate(Region):
        pass

    class Position(Thing):
        pass

    class Title(Thing):
        pass

    class Vision(Thing):
        pass

    class DevelopmentExperience(Thing):
        pass

    class PhotographSet(Thing):
        pass

    class PublicPhotographSet(PhotographSet):
        pass

    class PersonalPhotographSet(PhotographSet):
        pass

    class Photograph(Thing):
        pass

    class PublicPhotograph(Photograph):
        pass

    class PersonalPhotograph(Photograph):
        pass

    class BookPart(Thing):
        pass

    class coAuthoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]

    class authoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]

    class hasTitle(ObjectProperty):
        domain = [Book]
        range = [Title]

    class hasArabicTitle(ObjectProperty, FunctionalProperty):
        domain = [Book]
        range = [Title]

    class hasPosition(ObjectProperty):
        domain = [Person]
        range = [Position]

    class rulerOf(ObjectProperty):
        domain = [Person]
        range = [Emirate]

    class vicePresidentOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class primeMinisterOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class mentionsRegion(ObjectProperty):
        domain = [Book]
        range = [Region]

    class presentsVision(ObjectProperty):
        domain = [Book]
        range = [Vision]

    class aboutDevelopmentExperience(ObjectProperty):
        domain = [Book]
        range = [DevelopmentExperience]

    class includesPhotographSet(ObjectProperty):
        domain = [Book]
        range = [PhotographSet]

    class containsPhotograph(ObjectProperty):
        domain = [PhotographSet]
        range = [Photograph]

    class includesPart(ObjectProperty):
        domain = [Book]
        range = [BookPart]

    class hasPageCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasPhysicalSize(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasPhotographSetCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasPartCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class containsPreviouslyUnpublishedPersonalImages(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]

    Book.is_a = [
        coAuthoredBy.some(Person),
        authoredBy.some(Person),
        hasTitle.some(Title),
        hasArabicTitle.some(Title),
        mentionsRegion.some(Country),
        mentionsRegion.some(Emirate),
        presentsVision.some(Vision),
        aboutDevelopmentExperience.some(DevelopmentExperience),
        includesPhotographSet.some(PublicPhotographSet),
        includesPhotographSet.some(PersonalPhotographSet),
        includesPart.some(BookPart),
    ]
    PublicPhotographSet.is_a = [containsPhotograph.some(PublicPhotograph)]
    PersonalPhotographSet.is_a = [containsPhotograph.some(PersonalPhotograph)]

    myVisionBook = Book("MyVisionChallengesInTheRaceForExcellenceBook")
    myVisionBook.label = "My Vision — Challenges in the Race for Excellence"

    mainEnglishTitle = Title("MyVisionChallengesInTheRaceForExcellenceTitle")
    mainEnglishTitle.label = "My Vision — Challenges in the Race for Excellence"

    quotedEnglishTitle = Title("MyVisionChallengesInTheRaceForExcellenceQuotedTitle")
    quotedEnglishTitle.label = "My vision .. Challenges in the Race for Excellence"

    arabicTitle = Title("ArabicTitleRuyati")
    arabicTitle.label = "رؤيتي .. التحديات في سباق التميز"

    mohammedBinRashidAlMaktoum = Person("MohammedBinRashidAlMaktoumPerson")
    mohammedBinRashidAlMaktoum.label = "Mohammed bin Rashid Al Maktoum"

    hisHighnessSheikhMohammedBinRashid = Person("HisHighnessSheikhMohammedBinRashidPerson")
    hisHighnessSheikhMohammedBinRashid.label = "His Highness Sheikh Mohammed bin Rashid"

    unitedArabEmirates = Country("UnitedArabEmiratesCountry")
    unitedArabEmirates.label = "United Arab Emirates"

    uae = Country("UAECountry")
    uae.label = "UAE"

    dubai = Emirate("DubaiEmirate")
    dubai.label = "Dubai"

    rulerOfDubaiLower = Position("RulerOfDubaiLowerPosition")
    rulerOfDubaiLower.label = "ruler of Dubai"

    vicePresidentUaeHyphenated = Position("VicePresidentOfTheUnitedArabEmiratesHyphenatedPosition")
    vicePresidentUaeHyphenated.label = "Vice - President of the United Arab Emirates"

    vicePresidentUaePlain = Position("VicePresidentOfTheUnitedArabEmiratesPlainPosition")
    vicePresidentUaePlain.label = "Vice President of the United Arab Emirates"

    primeMinisterUae = Position("PrimeMinisterOfTheUnitedArabEmiratesPosition")
    primeMinisterUae.label = "Prime Minister of the United Arab Emirates"

    rulerOfDubaiCapitalized = Position("RulerOfDubaiCapitalizedPosition")
    rulerOfDubaiCapitalized.label = "Ruler of Dubai"

    myVisionBook.hasTitle = [mainEnglishTitle, quotedEnglishTitle]
    myVisionBook.hasArabicTitle = arabicTitle
    myVisionBook.coAuthoredBy = [mohammedBinRashidAlMaktoum]
    myVisionBook.authoredBy = [hisHighnessSheikhMohammedBinRashid]
    myVisionBook.mentionsRegion = [unitedArabEmirates, uae, dubai]
    myVisionBook.hasPageCount = 223
    myVisionBook.hasPhysicalSize = "medium size"
    myVisionBook.hasPhotographSetCount = 2
    myVisionBook.hasPartCount = 5
    myVisionBook.containsPreviouslyUnpublishedPersonalImages = True

    mohammedBinRashidAlMaktoum.hasPosition = [rulerOfDubaiLower, vicePresidentUaeHyphenated]
    mohammedBinRashidAlMaktoum.rulerOf = [dubai]
    mohammedBinRashidAlMaktoum.vicePresidentOf = [unitedArabEmirates, uae]

    hisHighnessSheikhMohammedBinRashid.hasPosition = [vicePresidentUaePlain, primeMinisterUae, rulerOfDubaiCapitalized]
    hisHighnessSheikhMohammedBinRashid.rulerOf = [dubai]
    hisHighnessSheikhMohammedBinRashid.vicePresidentOf = [unitedArabEmirates, uae]
    hisHighnessSheikhMohammedBinRashid.primeMinisterOf = [unitedArabEmirates, uae]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
