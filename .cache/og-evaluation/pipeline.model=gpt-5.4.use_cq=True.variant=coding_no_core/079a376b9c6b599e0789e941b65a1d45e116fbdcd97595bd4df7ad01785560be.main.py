"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. What is the title of the book co-authored by Mohammed bin Rashid Al Maktoum?
2. What is the Arabic title of the book "My Vision — Challenges in the Race for Excellence"?
3. Who are the authors or co-authors of the book "My Vision — Challenges in the Race for Excellence"?
4. What official positions are held by Mohammed bin Rashid Al Maktoum?
5. Which country is Mohammed bin Rashid Al Maktoum associated with as Vice-President and Prime Minister?
6. Which emirate is Mohammed bin Rashid Al Maktoum the ruler of?
7. What is the main vision presented in the book?
8. What development experience is described in the book?
9. On what principles is the development experience in the book based?
10. What transformation of the UAE and Dubai is described in the book?
11. What role of the UAE and Dubai is discussed in relation to the regional economy?
12. How many pages does the book contain?
13. What is the physical size or format of the book?
14. How many sets of photographs are included in the book?
15. What is the relationship between the photographs and the content of the book?
16. What story is told through the content and photographs of the book?
17. What are the two groups of images included in the book?
18. Which images in the book are related to the public life of the author?
19. Which images in the book are related to the personal life of the author?
20. Are any of the images in the book published for the first time?
21. How many parts does the book include?
22. What are the main parts or sections of the book?
23. What subjects are covered in the five parts of the book?
24. What themes of excellence are discussed in the book?
25. How does the book describe the development of Dubai?
26. How does the book describe the development of the UAE?
27. What connection does the book make between excellence and development?
28. What role does Mohammed bin Rashid Al Maktoum play in the narrative of the book?
29. Is the book associated with both Dubai and the United Arab Emirates?
30. What kind of visual materials accompany the textual content of the book?
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

    class Place(Thing):
        pass

    class Country(Place):
        pass

    class Emirate(Place):
        pass

    class WrittenWork(Thing):
        pass

    class Book(WrittenWork):
        pass

    class VisualMaterial(Thing):
        pass

    class PhotographSet(VisualMaterial):
        pass

    class ImageGroup(PhotographSet):
        pass

    class OfficialPosition(Thing):
        pass

    class hasAuthor(ObjectProperty):
        domain = [Book]
        range = [Person]

    class coAuthoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]

    class holdsPosition(ObjectProperty):
        domain = [Person]
        range = [OfficialPosition]

    class officeOf(ObjectProperty):
        domain = [OfficialPosition]
        range = [Place]

    class vicePresidentOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class primeMinisterOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class rulerOf(ObjectProperty):
        domain = [Person]
        range = [Emirate]

    class associatedWithPlace(ObjectProperty):
        domain = [Book]
        range = [Place]

    class describesDevelopmentOf(ObjectProperty):
        domain = [Book]
        range = [Place]

    class hasPhotographSet(ObjectProperty):
        domain = [Book]
        range = [PhotographSet]

    class complementsContentOf(ObjectProperty):
        domain = [PhotographSet]
        range = [Book]

    class relatedToPublicLifeOf(ObjectProperty):
        domain = [ImageGroup]
        range = [Person]

    class relatedToPersonalLifeOf(ObjectProperty):
        domain = [ImageGroup]
        range = [Person]

    class hasArabicTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

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

    class presentsVisionDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class describesDevelopmentExperienceDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class basedOnPrincipleDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class describesTransformationDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class discussesRegionalEconomicRoleDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class visualMaterialsRelationDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class tellsStoryDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class someImagesPublishedForFirstTime(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]

    Book.is_a.append(hasAuthor.some(Person))
    Book.is_a.append(hasPhotographSet.some(PhotographSet))
    OfficialPosition.is_a.append(officeOf.some(Place))

    myVisionBook = Book("MyVisionChallengesInTheRaceForExcellence")
    myVisionBook.label = [
        "My Vision — Challenges in the Race for Excellence",
        "My vision .. Challenges in the Race for Excellence",
        "رؤيتي .. التحديات في سباق التميز",
    ]

    mohammedBinRashidAlMaktoum = Person("MohammedBinRashidAlMaktoum")
    mohammedBinRashidAlMaktoum.label = [
        "Mohammed bin Rashid Al Maktoum",
        "His Highness Sheikh Mohammed bin Rashid",
    ]

    unitedArabEmirates = Country("UnitedArabEmirates")
    unitedArabEmirates.label = ["United Arab Emirates", "UAE"]

    dubai = Emirate("Dubai")
    dubai.label = "Dubai"

    vicePresidentPosition = OfficialPosition("VicePresidentPosition")
    vicePresidentPosition.label = ["Vice - President", "Vice President"]

    primeMinisterPosition = OfficialPosition("PrimeMinisterPosition")
    primeMinisterPosition.label = "Prime Minister"

    rulerOfDubaiPosition = OfficialPosition("RulerOfDubaiPosition")
    rulerOfDubaiPosition.label = ["ruler of Dubai", "Ruler of Dubai"]

    publicImageGroup = ImageGroup("PublicImageGroup")
    publicImageGroup.label = "book public images"

    personalImageGroup = ImageGroup("PersonalImageGroup")
    personalImageGroup.label = "personal writer"

    myVisionBook.hasAuthor = [mohammedBinRashidAlMaktoum]
    myVisionBook.coAuthoredBy = [mohammedBinRashidAlMaktoum]
    myVisionBook.associatedWithPlace = [unitedArabEmirates, dubai]
    myVisionBook.describesDevelopmentOf = [unitedArabEmirates, dubai]
    myVisionBook.hasPhotographSet = [publicImageGroup, personalImageGroup]
    myVisionBook.hasArabicTitle = "رؤيتي .. التحديات في سباق التميز"
    myVisionBook.hasPageCount = 223
    myVisionBook.hasPhysicalSize = "medium size"
    myVisionBook.hasPhotographSetCount = 2
    myVisionBook.hasPartCount = 5
    myVisionBook.presentsVisionDescription = "the vision of the experience of development"
    myVisionBook.describesDevelopmentExperienceDescription = "the experience of development"
    myVisionBook.basedOnPrincipleDescription = "excellence"
    myVisionBook.describesTransformationDescription = "move in the UAE and Dubai from their role as a regional economic"
    myVisionBook.discussesRegionalEconomicRoleDescription = "their role as a regional economic"
    myVisionBook.visualMaterialsRelationDescription = "the photographs join the content of the book"
    myVisionBook.tellsStoryDescription = "the whole story development of excellence in Dubai"
    myVisionBook.someImagesPublishedForFirstTime = True

    mohammedBinRashidAlMaktoum.holdsPosition = [
        vicePresidentPosition,
        primeMinisterPosition,
        rulerOfDubaiPosition,
    ]
    mohammedBinRashidAlMaktoum.vicePresidentOf = [unitedArabEmirates]
    mohammedBinRashidAlMaktoum.primeMinisterOf = [unitedArabEmirates]
    mohammedBinRashidAlMaktoum.rulerOf = [dubai]

    vicePresidentPosition.officeOf = [unitedArabEmirates]
    primeMinisterPosition.officeOf = [unitedArabEmirates]
    rulerOfDubaiPosition.officeOf = [dubai]

    publicImageGroup.complementsContentOf = [myVisionBook]
    publicImageGroup.relatedToPublicLifeOf = [mohammedBinRashidAlMaktoum]

    personalImageGroup.complementsContentOf = [myVisionBook]
    personalImageGroup.relatedToPersonalLifeOf = [mohammedBinRashidAlMaktoum]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
