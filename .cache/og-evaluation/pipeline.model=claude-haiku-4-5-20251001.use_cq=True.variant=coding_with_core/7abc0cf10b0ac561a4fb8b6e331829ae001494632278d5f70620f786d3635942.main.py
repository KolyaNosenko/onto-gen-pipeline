"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. What is the founding date and location of Bovet Fleurier SA?
2. Who founded Bovet Fleurier SA and when?
3. What is the price range of Bovet watches?
4. What are the distinctive features and characteristics of Bovet watches?
5. For which market were Bovet pocket watches primarily manufactured in the 19th century?
6. What are the notable design elements that Bovet is known for?
7. Who is the current owner of Bovet Fleurier SA?
8. What is Bovet's heritage and historical significance in watchmaking?
9. What types of watches does Bovet currently produce?
10. What is unique about Bovet's workforce in traditional watchmaking?
11. What innovations did Bovet introduce to pocket watch design?
12. What is a seven-day tourbillon and how is it associated with Bovet?
13. What are Fleurier Miniature Painting models?
14. How does Bovet's current style reference its historical legacy?
15. What are skeletonized views in watch movements and why are they significant to Bovet?
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

# Import core entity classes used in this domain model
from og_sandbox_with_core.core.entities import (
    Society, SocialAgent, NonAgentivePhysicalObject, TimeInterval
)

# Import core properties if needed
from og_sandbox_with_core.core.properties import partOf


with core:
    # Domain entity classes - capturing types of things mentioned in the source text
    
    class Location(NonAgentivePhysicalObject):
        """A geographic location (city, country, etc.)"""
        pass
    
    class Watch(NonAgentivePhysicalObject):
        """Base class for watches manufactured by Bovet"""
        pass
    
    class PocketWatch(Watch):
        """Pocket watches manufactured for the Chinese market in the 19th century"""
        pass
    
    class ArtisticWatch(Watch):
        """High-end artistic watches produced today"""
        pass
    
    class FleurierMiniaturePaintingModel(ArtisticWatch):
        """Specific model of artistic watch known for high-quality Miniature Painting dials"""
        pass
    
    class Tourbillon(NonAgentivePhysicalObject):
        """Tourbillon mechanism - a feature of Bovet watches"""
        pass
    
    class SevenDayTourbillon(Tourbillon):
        """Seven-day tourbillon - a signature feature of Bovet watches"""
        pass
    
    class Dial(NonAgentivePhysicalObject):
        """Watch dial - a component of watches"""
        pass
    
    class Movement(NonAgentivePhysicalObject):
        """Watch movement - the mechanism that drives the watch"""
        pass
    
    # Domain ObjectProperty and DataProperty declarations
    
    class foundedBy(ObjectProperty):
        """Relation linking an organization to its founder"""
        domain = [Society]
        range = [SocialAgent]
    
    class foundedAt(ObjectProperty):
        """Relation linking an organization to its founding location"""
        domain = [Society]
        range = [Location]
    
    class foundedOn(ObjectProperty, FunctionalProperty):
        """Relation linking an organization to the time interval of its founding"""
        domain = [Society]
        range = [TimeInterval]
    
    class currentOwner(ObjectProperty, FunctionalProperty):
        """Relation linking an organization to its current owner"""
        domain = [Society]
        range = [SocialAgent]
    
    class manufactures(ObjectProperty):
        """Relation linking an organization to the types of products it manufactures"""
        domain = [Society]
        range = [Watch]
    
    class targetMarket(ObjectProperty):
        """Relation linking a product to its target market/location"""
        domain = [Watch]
        range = [Location]
    
    class minPrice(DataProperty, FunctionalProperty):
        """Minimum price of a product in US dollars"""
        domain = [ArtisticWatch]
        range = [int]
    
    class maxPrice(DataProperty, FunctionalProperty):
        """Maximum price of a product in US dollars"""
        domain = [ArtisticWatch]
        range = [int]
    
    class employsWomenArtisans(DataProperty, FunctionalProperty):
        """Whether an organization employs women artisans"""
        domain = [Society]
        range = [bool]
    
    class includesSecondHand(DataProperty, FunctionalProperty):
        """Whether watches include a second hand"""
        domain = [Watch]
        range = [bool]
    
    class hasSkeletonizedMovement(DataProperty, FunctionalProperty):
        """Whether watches feature skeletonized movements"""
        domain = [Watch]
        range = [bool]
    
    class hasDecorativeMovement(DataProperty, FunctionalProperty):
        """Whether watches feature decorative movements"""
        domain = [Watch]
        range = [bool]
    
    # Named instances from the source text
    
    # The company
    bovet = Society("BovetFleurierSA")
    bovet.label = "Bovet Fleurier SA"
    
    # Founders and owners
    edouard = SocialAgent("EdouardBovet")
    edouard.label = "Édouard Bovet"
    
    pascal = SocialAgent("PascalRaffy")
    pascal.label = "Pascal Raffy"
    
    # Geographic locations
    london = Location("London")
    london.label = "London"
    
    china = Location("China")
    china.label = "China"
    
    # Founding date
    may1_1822 = TimeInterval("May1_1822")
    may1_1822.label = "May 1, 1822"
    
    # Property assignments for the company
    bovet.foundedBy = [edouard]
    bovet.foundedAt = [london]
    bovet.foundedOn = may1_1822
    bovet.currentOwner = pascal
    bovet.employsWomenArtisans = True
    
    # Property assignments for watch types
    pocket_watch_instance = PocketWatch("BovetPocketWatch_1")
    pocket_watch_instance.label = "Bovet Pocket Watch"
    pocket_watch_instance.targetMarket = [china]
    pocket_watch_instance.includesSecondHand = True
    pocket_watch_instance.hasSkeletonizedMovement = True
    pocket_watch_instance.hasDecorativeMovement = True
    
    # Artistic watches with price range
    artistic_watch_instance = ArtisticWatch("BovetArtisticWatch_1")
    artistic_watch_instance.label = "Bovet Artistic Watch"
    artistic_watch_instance.minPrice = 18000
    artistic_watch_instance.maxPrice = 2500000
    
    # Fleurier Miniature Painting model instance
    fleurier_model = FleurierMiniaturePaintingModel("FleurierMiniaturePainting_1")
    fleurier_model.label = "Fleurier Miniature Painting Model"
    
    # Seven-day tourbillon instance
    seven_day_tourbillon_inst = SevenDayTourbillon("SevenDayTourbillon_1")
    seven_day_tourbillon_inst.label = "Seven-day tourbillon"
    
    # Manufacturing relationships
    bovet.manufactures = [pocket_watch_instance, artistic_watch_instance, fleurier_model]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
