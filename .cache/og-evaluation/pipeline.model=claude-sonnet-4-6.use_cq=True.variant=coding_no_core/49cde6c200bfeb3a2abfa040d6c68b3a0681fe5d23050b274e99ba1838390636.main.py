"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

Here are the competency questions derived from the document:

1. Who are the authors of the book "My Vision — Challenges in the Race for Excellence"?
2. What is the Arabic title of the book "My Vision — Challenges in the Race for Excellence"?
3. What official positions does Mohammed bin Rashid Al Maktoum hold?
4. Who is the ruler of Dubai?
5. Who is the Vice President and Prime Minister of the United Arab Emirates?
6. How many pages does the book "My Vision — Challenges in the Race for Excellence" contain?
7. How many parts does the book "My Vision — Challenges in the Race for Excellence" consist of?
8. How many sets of photographs are included in the book "My Vision — Challenges in the Race for Excellence"?
9. What is the main theme or vision presented in the book "My Vision — Challenges in the Race for Excellence"?
10. What types of photographs are included in the book "My Vision — Challenges in the Race for Excellence"?
11. What role did Dubai transition from, according to the book "My Vision — Challenges in the Race for Excellence"?
12. Which country is associated with the development experience described in the book "My Vision — Challenges in the Race for Excellence"?
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
    # --- Entity classes ---
    class Book(Thing): pass
    class Person(Thing): pass
    class Place(Thing): pass
    class City(Place): pass
    class Country(Place): pass
    class PhotographCollection(Thing): pass
    class PublicPhotographCollection(PhotographCollection): pass
    class PersonalPhotographCollection(PhotographCollection): pass

    # --- Object properties ---
    class hasAuthor(ObjectProperty):
        domain = [Book]
        range  = [Person]

    class containsPhotographCollection(ObjectProperty):
        domain = [Book]
        range  = [PhotographCollection]

    class isRulerOf(ObjectProperty):
        domain = [Person]
        range  = [City]

    class isVicePresidentOf(ObjectProperty):
        domain = [Person]
        range  = [Country]

    class isPrimeMinisterOf(ObjectProperty):
        domain = [Person]
        range  = [Country]

    class associatedWithCountry(ObjectProperty):
        domain = [Book]
        range  = [Country]

    class associatedWithCity(ObjectProperty):
        domain = [Book]
        range  = [City]

    # --- Data properties ---
    class hasArabicTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range  = [str]

    class hasPageCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range  = [int]

    class hasPartCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range  = [int]

    class hasPhotographSetCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range  = [int]

    class hasTheme(DataProperty):
        domain = [Book]
        range  = [str]

    class hasFormerEconomicRole(DataProperty, FunctionalProperty):
        domain = [Place]
        range  = [str]

    # --- Individuals ---
    MyVisionBook = Book("MyVisionBook")
    MyVisionBook.label              = "My Vision — Challenges in the Race for Excellence"
    MyVisionBook.hasArabicTitle     = "رؤيتي .. التحديات في سباق التميز"
    MyVisionBook.hasPageCount       = 223
    MyVisionBook.hasPartCount       = 5
    MyVisionBook.hasPhotographSetCount = 2
    MyVisionBook.hasTheme           = ["development based on excellence"]

    MohammedBinRashidAlMaktoum = Person("MohammedBinRashidAlMaktoum")
    MohammedBinRashidAlMaktoum.label = "Mohammed bin Rashid Al Maktoum"

    DubaiCity = City("Dubai")
    DubaiCity.label                 = "Dubai"
    DubaiCity.hasFormerEconomicRole = "regional economic"

    UAECountry = Country("UnitedArabEmirates")
    UAECountry.label                 = "United Arab Emirates"
    UAECountry.hasFormerEconomicRole = "regional economic"

    PublicPhotosCollection = PublicPhotographCollection("PublicPhotosCollection")
    PublicPhotosCollection.label = "book public images"

    PersonalPhotosCollection = PersonalPhotographCollection("PersonalPhotosCollection")
    PersonalPhotosCollection.label = "personal writer"

    MyVisionBook.hasAuthor                    = [MohammedBinRashidAlMaktoum]
    MyVisionBook.associatedWithCountry        = [UAECountry]
    MyVisionBook.associatedWithCity           = [DubaiCity]
    MyVisionBook.containsPhotographCollection = [PublicPhotosCollection, PersonalPhotosCollection]

    MohammedBinRashidAlMaktoum.isRulerOf        = [DubaiCity]
    MohammedBinRashidAlMaktoum.isVicePresidentOf = [UAECountry]
    MohammedBinRashidAlMaktoum.isPrimeMinisterOf = [UAECountry]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
