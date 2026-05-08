"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. Who is the author of "My Vision — Challenges in the Race for Excellence"?

2. What is the role of Mohammed bin Rashid Al Maktoum in the United Arab Emirates?

3. What are the main topics covered in the book "My Vision — Challenges in the Race for Excellence"?

4. How many pages does the book "My Vision — Challenges in the Race for Excellence" contain?

5. What types of visual content are included in the book?

6. How many parts are included in the book's structure?

7. What is the book's vision based on?

8. What geographic regions are discussed in relation to economic development in the book?

9. Are personal photographs of the author included in the book?

10. What is the primary theme of the book regarding Dubai's development?
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
    # Domain entity classes
    class Person(Thing):
        pass
    
    class Place(Thing):
        pass
    
    class Country(Place):
        pass
    
    class City(Place):
        pass
    
    class Book(Thing):
        pass
    
    # Object properties
    class authoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]
    
    class rulerOf(ObjectProperty):
        domain = [Person]
        range = [Place]
    
    class vicePresidentOf(ObjectProperty):
        domain = [Person]
        range = [Country]
    
    class primeMinisterOf(ObjectProperty):
        domain = [Person]
        range = [Country]
    
    class locatedIn(ObjectProperty):
        domain = [Place]
        range = [Place]
    
    class discussesRegion(ObjectProperty):
        domain = [Book]
        range = [Place]
    
    # Data properties
    class numberOfPages(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]
    
    class numberOfParts(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]
    
    class basedOnConcept(DataProperty):
        domain = [Book]
        range = [str]
    
    class coversTopic(DataProperty):
        domain = [Book]
        range = [str]
    
    class visualContentTypes(DataProperty):
        domain = [Book]
        range = [str]
    
    # Named individuals
    # People
    mohammed = Person("MohammedBinRashidAlMaktoum")
    mohammed.label = "Mohammed bin Rashid Al Maktoum"
    
    # Places
    dubai = City("Dubai")
    dubai.label = "Dubai"
    
    uae = Country("UnitedArabEmirates")
    uae.label = "United Arab Emirates"
    
    # Book
    book = Book("MyVisionChallengesInTheRaceForExcellence")
    book.label = "My Vision — Challenges in the Race for Excellence"
    
    # Assign properties
    book.authoredBy = [mohammed]
    mohammed.rulerOf = [dubai]
    mohammed.vicePresidentOf = [uae]
    mohammed.primeMinisterOf = [uae]
    dubai.locatedIn = [uae]
    book.numberOfPages = 223
    book.numberOfParts = 5
    book.basedOnConcept = ["Excellence"]
    book.coversTopic = ["Development", "Excellence"]
    book.visualContentTypes = ["Public Images", "Personal Images"]
    book.discussesRegion = [dubai, uae]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
