"""
=== TASK INPUT ===
Source text:
My Vision — Challenges in the Race for Excellence ( Arabic : رؤيتي .. التحديات في سباق التميز ) is a book co - authored by Mohammed bin Rashid Al Maktoum , ruler of Dubai and Vice - President of the United Arab Emirates . The book of His Highness Sheikh Mohammed bin Rashid , Vice President and Prime Minister of the United Arab Emirates and Ruler of Dubai , " My vision .. Challenges in the Race for Excellence " , present the vision of His Highness the experience of development , which is based on excellence and move in the UAE and Dubai from their role as a regional economic , The book consists of 223 pages of medium size , which includes two sets of photographs , which joins the content of the book , to tell the whole story development of excellence in Dubai . Include two groups relate to the book public images , and other related personal writer , readers will see some of them published for the first time . The book includes five parts that are going to be explained in the following paragraphs , so read more ..

1. What is the title of the book co-authored by Mohammed bin Rashid Al Maktoum?
2. What is the Arabic title of the book "My Vision — Challenges in the Race for Excellence"?
3. Who are the authors or co-authors of the book "My Vision — Challenges in the Race for Excellence"?
4. What official positions are held by Mohammed bin Rashid Al Maktoum?
5. Which country is Mohammed bin Rashid Al Maktoum associated with as Vice-President and Prime Minister?
6. Of which city is Mohammed bin Rashid Al Maktoum the ruler?
7. What is the main vision presented in the book "My Vision — Challenges in the Race for Excellence"?
8. What development experience is described in the book?
9. On what principles is the development vision in the book based?
10. How does the book describe the transformation of the UAE and Dubai?
11. What role did the UAE and Dubai have before the transformation described in the book?
12. How many pages does the book contain?
13. What is the physical size or format of the book?
14. How many sets of photographs are included in the book?
15. What purpose do the photographs serve in the book?
16. What types of photographs are included in the two sets of images?
17. Are there public images included in the book?
18. Are there personal images related to the author included in the book?
19. Were some of the photographs published for the first time in this book?
20. How many parts does the book include?
21. Does the book include sections that explain the story of development and excellence in Dubai?
22. What subject matter is covered in the five parts of the book?
23. Which entities are central to the book’s narrative of development and excellence?
24. What relationship does the book establish between excellence and development in Dubai?
25. Is the book associated with the theme of regional economic transformation?
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
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Process,
    Society,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Person(AgentivePhysicalObject):
        pass


    class Book(NonAgentivePhysicalObject):
        pass


    class BookTitle(NonAgentiveSocialObject):
        pass


    class OfficialPosition(NonAgentiveSocialObject):
        pass


    class City(Society):
        pass


    class Country(Society):
        pass


    class DevelopmentVision(NonAgentiveSocialObject):
        pass


    class DevelopmentExperience(Process):
        pass


    class DevelopmentPrinciple(NonAgentiveSocialObject):
        pass


    class PhotographSet(NonAgentivePhysicalObject):
        pass


    class Photograph(NonAgentivePhysicalObject):
        pass


    class PublicPhotograph(Photograph):
        pass


    class PersonalAuthorPhotograph(Photograph):
        pass


    class BookPart(NonAgentiveSocialObject):
        pass


    class coAuthoredBy(ObjectProperty):
        domain = [Book]
        range = [Person]


    class hasArabicTitle(ObjectProperty, FunctionalProperty):
        domain = [Book]
        range = [BookTitle]


    class holdsOfficialPosition(ObjectProperty):
        domain = [Person]
        range = [OfficialPosition]


    class positionJurisdiction(ObjectProperty, FunctionalProperty):
        domain = [OfficialPosition]
        range = [Society]


    class centersOnEntity(ObjectProperty):
        domain = [Book]
        range = [Society]


    class describesTransformationOf(ObjectProperty):
        domain = [Book]
        range = [Society]


    class bookPartOf(partOf):
        domain = [BookPart]
        range = [Book]


    class photographSetPartOf(partOf):
        domain = [PhotographSet]
        range = [Book]


    class photographPartOf(partOf):
        domain = [Photograph]
        range = [PhotographSet]


    class pageCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]


    class physicalFormat(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class mainVisionDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class developmentExperienceDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class basedOnPrinciplesDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class transformationDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class priorRoleDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class photographSetCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]


    class photographPurposeDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class photographTypesDescription(DataProperty):
        domain = [Book]
        range = [str]


    class includesPublicImages(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]


    class includesPersonalAuthorImages(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]


    class includesPreviouslyUnpublishedPhotographs(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]


    class partCount(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]


    class partsSubjectMatterDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class explainsDevelopmentExcellenceStoryInDubai(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]


    class excellenceDevelopmentRelationshipDescription(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]


    class associatedWithRegionalEconomicTransformation(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [bool]


    Book.is_a.append(coAuthoredBy.some(Person))
    Book.is_a.append(hasArabicTitle.some(BookTitle))
    OfficialPosition.is_a.append(positionJurisdiction.some(Society))
    BookPart.is_a.append(bookPartOf.some(Book))
    PhotographSet.is_a.append(photographSetPartOf.some(Book))
    Photograph.is_a.append(photographPartOf.some(PhotographSet))

    my_vision = Book("MyVisionChallengesInTheRaceForExcellence")
    my_vision.label = [
        "My Vision — Challenges in the Race for Excellence",
        "My vision .. Challenges in the Race for Excellence",
    ]

    arabic_title = BookTitle("ArabicTitleMyVisionChallengesInTheRaceForExcellence")
    arabic_title.label = "رؤيتي .. التحديات في سباق التميز"

    mohammed_bin_rashid_al_maktoum = Person("MohammedBinRashidAlMaktoum")
    mohammed_bin_rashid_al_maktoum.label = [
        "Mohammed bin Rashid Al Maktoum",
        "His Highness Sheikh Mohammed bin Rashid",
    ]

    dubai = City("Dubai")
    dubai.label = "Dubai"

    united_arab_emirates = Country("UnitedArabEmirates")
    united_arab_emirates.label = ["United Arab Emirates", "UAE"]

    vice_president_uae = OfficialPosition("VicePresidentOfUnitedArabEmirates")
    vice_president_uae.label = [
        "Vice - President of the United Arab Emirates",
        "Vice President of the United Arab Emirates",
    ]

    prime_minister_uae = OfficialPosition("PrimeMinisterOfUnitedArabEmirates")
    prime_minister_uae.label = "Prime Minister of the United Arab Emirates"

    ruler_of_dubai = OfficialPosition("RulerOfDubai")
    ruler_of_dubai.label = "Ruler of Dubai"

    my_vision.coAuthoredBy.append(mohammed_bin_rashid_al_maktoum)
    my_vision.hasArabicTitle = arabic_title
    my_vision.centersOnEntity.append(united_arab_emirates)
    my_vision.centersOnEntity.append(dubai)
    my_vision.describesTransformationOf.append(united_arab_emirates)
    my_vision.describesTransformationOf.append(dubai)
    my_vision.pageCount = 223
    my_vision.physicalFormat = "medium size"
    my_vision.mainVisionDescription = "the vision of the experience of development"
    my_vision.developmentExperienceDescription = "the experience of development"
    my_vision.basedOnPrinciplesDescription = "excellence"
    my_vision.transformationDescription = (
        "move in the UAE and Dubai from their role as a regional economic"
    )
    my_vision.priorRoleDescription = "their role as a regional economic"
    my_vision.photographSetCount = 2
    my_vision.photographPurposeDescription = (
        "to tell the whole story development of excellence in Dubai"
    )
    my_vision.photographTypesDescription = [
        "public images",
        "personal writer images",
    ]
    my_vision.includesPublicImages = True
    my_vision.includesPersonalAuthorImages = True
    my_vision.includesPreviouslyUnpublishedPhotographs = True
    my_vision.partCount = 5
    my_vision.partsSubjectMatterDescription = (
        "the experience of development based on excellence and the story development of excellence in Dubai"
    )
    my_vision.explainsDevelopmentExcellenceStoryInDubai = True
    my_vision.excellenceDevelopmentRelationshipDescription = (
        "development in Dubai is presented as based on excellence"
    )
    my_vision.associatedWithRegionalEconomicTransformation = True

    mohammed_bin_rashid_al_maktoum.holdsOfficialPosition.append(vice_president_uae)
    mohammed_bin_rashid_al_maktoum.holdsOfficialPosition.append(prime_minister_uae)
    mohammed_bin_rashid_al_maktoum.holdsOfficialPosition.append(ruler_of_dubai)

    vice_president_uae.positionJurisdiction = united_arab_emirates
    prime_minister_uae.positionJurisdiction = united_arab_emirates
    ruler_of_dubai.positionJurisdiction = dubai


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
