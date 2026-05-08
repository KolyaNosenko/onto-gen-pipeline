"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. Who co-authored the book *My Vision — Challenges in the Race for Excellence*?
2. What is the Arabic title of *My Vision — Challenges in the Race for Excellence*?
3. What is the full official title of the book attributed to Mohammed bin Rashid Al Maktoum?
4. Which political offices does Mohammed bin Rashid Al Maktoum hold?
5. Who is the ruler of Dubai and Vice President of the United Arab Emirates?
6. What is the book about?
7. What vision or experience does the book present?
8. What is the subject of the development experience described in the book?
9. How many pages does the book contain?
10. What is the physical size of the book?
11. How many parts does the book include?
12. How many sets of photographs are included in the book?
13. What kinds of photographs are included in the book?
14. Are any of the personal images in the book published for the first time?
15. What role do the photographs play in the book’s content?
16. Which city’s development story is told in the book?
17. What is the book’s relationship to excellence in Dubai?
18. How is Dubai described in relation to its regional role in the book?
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
    AbstractQuality,
    MentalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Process,
    SocialAgent,
    Society,
)
from og_sandbox_with_core.core.properties import constantConstituentOf


with core:
    class Book(NonAgentivePhysicalObject):
        pass

    class Person(SocialAgent):
        pass

    class City(NonAgentiveSocialObject):
        pass

    class Country(Society):
        pass

    class BookPart(NonAgentivePhysicalObject):
        pass

    class PhotographSet(NonAgentivePhysicalObject):
        pass

    class PublicPhotographSet(PhotographSet):
        pass

    class PersonalWriterPhotographSet(PhotographSet):
        pass

    class Photograph(NonAgentivePhysicalObject):
        pass

    class PublicImage(Photograph):
        pass

    class PersonalWriterImage(Photograph):
        pass

    class FirstPublishedPersonalWriterImage(PersonalWriterImage):
        pass

    class Vision(MentalObject):
        pass

    class DevelopmentExperience(Process):
        pass

    class Excellence(AbstractQuality):
        pass

    class coAuthoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]

    class rulerOf(ObjectProperty):
        domain = [Person]
        range = [City]

    class vicePresidentOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class primeMinisterOf(ObjectProperty):
        domain = [Person]
        range = [Country]

    class includesPart(constantConstituentOf):
        domain = [Book]
        range = [BookPart]

    class includesPhotographSet(constantConstituentOf):
        domain = [Book]
        range = [PhotographSet]

    class containsPhotograph(constantConstituentOf):
        domain = [PhotographSet]
        range = [Photograph]

    class presentsVision(ObjectProperty):
        domain = [Book]
        range = [Vision]

    class presentsExperience(ObjectProperty):
        domain = [Book]
        range = [DevelopmentExperience]

    class basedOn(ObjectProperty):
        domain = [DevelopmentExperience]
        range = [Excellence]

    class hasOfficialTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasArabicTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasPageCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasPhysicalSize(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasPartCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasPhotographSetCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    class hasContentSummary(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    Book.is_a = [
        coAuthoredBy.some(Person),
        includesPart.some(BookPart),
        includesPhotographSet.some(PublicPhotographSet),
        includesPhotographSet.some(PersonalWriterPhotographSet),
        presentsVision.some(Vision),
        presentsExperience.some(DevelopmentExperience),
    ]

    DevelopmentExperience.is_a = [basedOn.some(Excellence)]
    PublicPhotographSet.is_a = [containsPhotograph.some(PublicImage)]
    PersonalWriterPhotographSet.is_a = [
        containsPhotograph.some(PersonalWriterImage),
        containsPhotograph.some(FirstPublishedPersonalWriterImage),
    ]

    my_vision_book = Book("MyVisionChallengesInTheRaceForExcellenceBook")
    my_vision_book.label = [
        "My Vision — Challenges in the Race for Excellence",
        "رؤيتي .. التحديات في سباق التميز",
    ]
    my_vision_book.hasOfficialTitle = "My vision .. Challenges in the Race for Excellence"
    my_vision_book.hasArabicTitle = "رؤيتي .. التحديات في سباق التميز"
    my_vision_book.hasPageCount = 223
    my_vision_book.hasPhysicalSize = "medium size"
    my_vision_book.hasPartCount = 5
    my_vision_book.hasPhotographSetCount = 2
    my_vision_book.hasContentSummary = (
        "co-authored by Mohammed bin Rashid Al Maktoum; consists of 223 pages, "
        "five parts, and two sets of photographs; presents the vision of His "
        "Highness and the experience of development based on excellence and the "
        "UAE and Dubai's regional economic role; includes public images and "
        "personal writer-related images, some of them published for the first "
        "time, to tell the development story of excellence in Dubai"
    )

    mohammed_bin_rashid_al_maktoum = Person("MohammedBinRashidAlMaktoum")
    mohammed_bin_rashid_al_maktoum.label = [
        "Mohammed bin Rashid Al Maktoum",
        "His Highness Sheikh Mohammed bin Rashid",
    ]

    dubai = City("Dubai")
    dubai.label = ["Dubai"]

    united_arab_emirates = Country("UnitedArabEmirates")
    united_arab_emirates.label = ["the United Arab Emirates", "UAE"]

    my_vision_book.coAuthoredBy.append(mohammed_bin_rashid_al_maktoum)

    mohammed_bin_rashid_al_maktoum.rulerOf.append(dubai)
    mohammed_bin_rashid_al_maktoum.vicePresidentOf.append(united_arab_emirates)
    mohammed_bin_rashid_al_maktoum.primeMinisterOf.append(united_arab_emirates)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
