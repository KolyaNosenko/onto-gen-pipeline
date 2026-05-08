"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

Here are the competency questions derived from the document:

1. Who are the authors of the book "My Vision — Challenges in the Race for Excellence"?
2. What is the Arabic title of the book "My Vision — Challenges in the Race for Excellence"?
3. What political positions does Mohammed bin Rashid Al Maktoum hold?
4. Who is the ruler of Dubai?
5. Who is the Vice-President of the United Arab Emirates?
6. How many pages does the book "My Vision — Challenges in the Race for Excellence" contain?
7. How many parts does the book "My Vision — Challenges in the Race for Excellence" consist of?
8. How many sets of photographs are included in the book?
9. What is the main theme or vision presented in the book?
10. What role does the book describe for the UAE and Dubai in terms of economic development?
11. What types of photographs are included in the book?
12. Which photographs in the book are published for the first time?
13. What is the size classification of the book "My Vision — Challenges in the Race for Excellence"?
14. What concept of development does the book focus on?
15. Who holds the position of Prime Minister of the United Arab Emirates as mentioned in the book?
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
    Society,
)


with core:
    # ── Entity classes ──────────────────────────────────────────────────────

    class Person(AgentivePhysicalObject):
        """A human individual with agency."""

    class PoliticalLeader(Person):
        """A person who holds political office (ruler, president, prime minister)."""

    class Book(NonAgentiveSocialObject):
        """A written work that is a non-agentive social object."""

    class Emirate(Society):
        """A city-state or emirate governed by a ruler."""

    class Country(Society):
        """A sovereign nation-state."""

    class PhotographCollection(NonAgentiveSocialObject):
        """A set of photographs included in a publication."""

    # ── Properties ──────────────────────────────────────────────────────────

    class coAuthoredBy(ObjectProperty):
        """Links a book to one of its authors."""
        domain = [Book]
        range = [AgentivePhysicalObject]

    class rulerOf(ObjectProperty):
        """Links a political leader to the emirate they rule."""
        domain = [PoliticalLeader]
        range = [Emirate]

    class vicePresidentOf(ObjectProperty):
        """Links a political leader to the country whose vice-presidency they hold."""
        domain = [PoliticalLeader]
        range = [Country]

    class primeMinisterOf(ObjectProperty):
        """Links a political leader to the country whose prime-ministership they hold."""
        domain = [PoliticalLeader]
        range = [Country]

    class includesPhotographCollection(ObjectProperty):
        """Links a book to a photograph collection it contains."""
        domain = [Book]
        range = [PhotographCollection]

    class hasArabicTitle(DataProperty, FunctionalProperty):
        """The Arabic-script title of a book."""
        domain = [Book]
        range = [str]

    class pageCount(DataProperty, FunctionalProperty):
        """Total number of pages in the book."""
        domain = [Book]
        range = [int]

    class partCount(DataProperty, FunctionalProperty):
        """Number of structural parts (major sections) in the book."""
        domain = [Book]
        range = [int]

    class photographSetCount(DataProperty, FunctionalProperty):
        """Number of distinct photograph sets included in the book."""
        domain = [Book]
        range = [int]

    class sizeClassification(DataProperty, FunctionalProperty):
        """Physical size category of the book (e.g. 'medium')."""
        domain = [Book]
        range = [str]

    class hasTheme(DataProperty, FunctionalProperty):
        """The central theme or vision of the book."""
        domain = [Book]
        range = [str]

    class hasEconomicRole(DataProperty, FunctionalProperty):
        """Describes the economic role of a society as presented in the book."""
        domain = [Society]
        range = [str]

    class photographType(DataProperty, FunctionalProperty):
        """Classifies a photograph collection as 'public' or 'personal'."""
        domain = [PhotographCollection]
        range = [str]

    class hasPhotosPublishedForFirstTime(DataProperty, FunctionalProperty):
        """True when the collection includes photos appearing in print for the first time."""
        domain = [PhotographCollection]
        range = [bool]

    # ── Named individuals ────────────────────────────────────────────────────

    MohammedBinRashidAlMaktoum = PoliticalLeader("MohammedBinRashidAlMaktoum")
    MohammedBinRashidAlMaktoum.label = "Mohammed bin Rashid Al Maktoum"

    Dubai = Emirate("Dubai")
    Dubai.label = "Dubai"

    UnitedArabEmirates = Country("UnitedArabEmirates")
    UnitedArabEmirates.label = "United Arab Emirates"

    MyVisionBook = Book("MyVisionChallengesInTheRaceForExcellence")
    MyVisionBook.label = "My Vision — Challenges in the Race for Excellence"
    MyVisionBook.hasArabicTitle = "رؤيتي .. التحديات في سباق التميز"
    MyVisionBook.pageCount = 223
    MyVisionBook.partCount = 5
    MyVisionBook.photographSetCount = 2
    MyVisionBook.sizeClassification = "medium"
    MyVisionBook.hasTheme = "excellence and development"
    MyVisionBook.coAuthoredBy.append(MohammedBinRashidAlMaktoum)

    PublicImagesCollection = PhotographCollection("PublicImagesCollection")
    PublicImagesCollection.label = "public images"
    PublicImagesCollection.photographType = "public"
    PublicImagesCollection.hasPhotosPublishedForFirstTime = False

    PersonalWriterPhotographsCollection = PhotographCollection("PersonalWriterPhotographsCollection")
    PersonalWriterPhotographsCollection.label = "personal photographs of the writer"
    PersonalWriterPhotographsCollection.photographType = "personal"
    PersonalWriterPhotographsCollection.hasPhotosPublishedForFirstTime = True

    MyVisionBook.includesPhotographCollection.append(PublicImagesCollection)
    MyVisionBook.includesPhotographCollection.append(PersonalWriterPhotographsCollection)

    MohammedBinRashidAlMaktoum.rulerOf.append(Dubai)
    MohammedBinRashidAlMaktoum.vicePresidentOf.append(UnitedArabEmirates)
    MohammedBinRashidAlMaktoum.primeMinisterOf.append(UnitedArabEmirates)

    Dubai.hasEconomicRole = "regional economic hub"
    UnitedArabEmirates.hasEconomicRole = "regional economic hub"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
