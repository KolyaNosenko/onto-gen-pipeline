"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. Who is the author of the book "My Vision — Challenges in the Race for Excellence"?

2. What is the Arabic title of the book authored by Mohammed bin Rashid Al Maktoum?

3. What official positions does Mohammed bin Rashid Al Maktoum hold?

4. How many pages does the book "My Vision — Challenges in the Race for Excellence" contain?

5. What is the primary theme or vision presented in the book?

6. How many parts does the book consist of?

7. What types of visual content are included in the book?

8. What is the geographical focus of the development experience described in the book?

9. Does the book include previously unpublished personal photographs of the author?

10. What is the relationship between the book's content and the development of Dubai and the UAE?

11. What role did Dubai and the UAE play as described in the author's vision?

12. What concept serves as the foundation of the vision presented in the book?
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

# TODO: import the core entity classes you actually subclass.
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject
from og_sandbox_with_core.core.entities import (
    NonPhysicalObject, NonAgentiveSocialObject, SocialAgent, Society
)

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # Domain entity classes
    class Book(NonPhysicalObject):
        """A published written work"""
        pass

    class BookPart(NonPhysicalObject):
        """A section or chapter of a book"""
        pass

    class Position(NonAgentiveSocialObject):
        """A role or title held by an individual"""
        pass

    class Photograph(NonPhysicalObject):
        """Visual content such as images or photographs"""
        pass

    class Concept(NonAgentiveSocialObject):
        """An abstract idea or theme"""
        pass

    class GeopoliticalPlace(Society):
        """A geographical region like a country or city"""
        pass

    # Data properties
    class hasTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasArabicTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class numberOfPages(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class numberOfParts(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class isPersonal(DataProperty, FunctionalProperty):
        domain = [Photograph]
        range = [bool]

    class isUnpublished(DataProperty, FunctionalProperty):
        domain = [Photograph]
        range = [bool]

    # Object properties
    class hasAuthor(ObjectProperty):
        domain = [Book]
        range = [SocialAgent]

    class hasPart(ObjectProperty):
        domain = [Book]
        range = [BookPart]

    class isAbout(ObjectProperty):
        domain = [Book]
        range = [Concept]

    class isBasedOn(ObjectProperty, FunctionalProperty):
        domain = [Book]
        range = [Concept]

    class isLocatedIn(ObjectProperty):
        domain = [Book]
        range = [GeopoliticalPlace]

    class holdsPosition(ObjectProperty):
        domain = [SocialAgent]
        range = [Position]

    class appearsIn(ObjectProperty):
        domain = [Photograph]
        range = [Book]

    # Book instance
    book = Book("MyVisionChallengesInTheRaceForExcellence")
    book.label = "My Vision — Challenges in the Race for Excellence"
    book.hasTitle = "My Vision — Challenges in the Race for Excellence"
    book.hasArabicTitle = "رؤيتي .. التحديات في سباق التميز"
    book.numberOfPages = 223
    book.numberOfParts = 5

    # Author instance
    author = SocialAgent("MohammedBinRashidAlMaktoum")
    author.label = "Mohammed bin Rashid Al Maktoum"
    book.hasAuthor.append(author)

    # Position instances
    rulerOfDubai = Position("RulerOfDubai")
    rulerOfDubai.label = "Ruler of Dubai"
    author.holdsPosition.append(rulerOfDubai)

    vpUAE = Position("VicePresidentUAE")
    vpUAE.label = "Vice-President of the United Arab Emirates"
    author.holdsPosition.append(vpUAE)

    pmUAE = Position("PrimeMinisterUAE")
    pmUAE.label = "Prime Minister of the United Arab Emirates"
    author.holdsPosition.append(pmUAE)

    # Geographical place instances
    dubai = GeopoliticalPlace("Dubai")
    dubai.label = "Dubai"
    book.isLocatedIn.append(dubai)

    uae = GeopoliticalPlace("UnitedArabEmirates")
    uae.label = "United Arab Emirates"
    book.isLocatedIn.append(uae)

    # Concept instances
    excellence = Concept("Excellence")
    excellence.label = "Excellence"

    development = Concept("Development")
    development.label = "Development"

    book.isAbout.append(excellence)
    book.isAbout.append(development)
    book.isBasedOn = excellence

    # BookPart instances (5 parts as mentioned in text)
    for i in range(1, 6):
        part = BookPart(f"BookPart_{i}")
        part.label = f"Part {i}"
        book.hasPart.append(part)

    # Photograph instances
    publicPhotographs = Photograph("PublicPhotographs")
    publicPhotographs.label = "Public photographs"
    publicPhotographs.appearsIn.append(book)

    personalPhotographs = Photograph("PersonalPhotographs")
    personalPhotographs.label = "Personal photographs"
    personalPhotographs.isPersonal = True
    personalPhotographs.isUnpublished = True
    personalPhotographs.appearsIn.append(book)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
