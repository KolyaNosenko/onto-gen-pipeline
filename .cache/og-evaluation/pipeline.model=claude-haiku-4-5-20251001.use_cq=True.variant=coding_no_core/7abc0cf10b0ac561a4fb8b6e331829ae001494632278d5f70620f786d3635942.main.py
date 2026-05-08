"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. When was Bovet Fleurier SA founded and by whom?
2. In which country was Bovet Fleurier SA chartered?
3. What types of watches did Bovet Fleurier SA manufacture in the 19th century?
4. What is the price range of Bovet Fleurier SA watches today?
5. What are the distinctive features and characteristics of Bovet watches?
6. What is the current ownership of Bovet Fleurier SA?
7. Which markets did Bovet Fleurier SA historically serve?
8. What design innovations did Bovet introduce to watchmaking?
9. What is notable about Bovet's employment practices in the watchmaking industry?
10. What are the specific dial models Bovet Fleurier SA is known for?
11. What movement complications are Bovet watches famous for?
12. How does the current Bovet watch style relate to its historical heritage?
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
    # ===== ENTITY CLASSES =====
    class WatchmakingCompany(Thing):
        pass
    
    class Person(Thing):
        pass
    
    class Country(Thing):
        pass
    
    class City(Thing):
        pass
    
    class Watch(Thing):
        pass
    
    class PocketWatch(Watch):
        pass
    
    class ArtisticWatch(Watch):
        pass
    
    class DialModel(Thing):
        pass
    
    class MovementType(Thing):
        pass
    
    class Artisan(Person):
        pass
    
    class Era(Thing):
        pass
    
    # ===== OBJECT PROPERTIES =====
    class foundedBy(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Person]
    
    class foundedIn(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [City]
    
    class charterCountry(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Country]
    
    class servedMarket(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Country]
    
    class knownForDialModel(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [DialModel]
    
    class knownForMovement(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [MovementType]
    
    class currentOwner(ObjectProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [Person]
    
    class employs(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Person]
    
    # ===== DATA PROPERTIES =====
    class foundedDate(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class nationality(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class historicalProducts(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class currentProducts(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class priceRange(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class knownFeatures(DataProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class designInnovations(DataProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class styleDescription(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    class employmentPractices(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]
    
    # ===== INSTANCES =====
    # Main company
    bovet_sa = WatchmakingCompany("BovetFleurierSA")
    bovet_sa.label = "Bovet Fleurier SA"
    bovet_sa.nationality = "Swiss"
    bovet_sa.foundedDate = "May 1, 1822"
    bovet_sa.historicalProducts = "Pocket Watches"
    bovet_sa.currentProducts = "Artistic Watches"
    bovet_sa.priceRange = "US$ 18,000 to US$ 2.5 million"
    bovet_sa.knownFeatures = ["high-quality dials", "engraving", "skeletonized views", "decorative movements", "second hand"]
    bovet_sa.designInnovations = ["skeletonized views", "decorative movements", "second hand"]
    bovet_sa.styleDescription = "references its history"
    bovet_sa.employmentPractices = "tradition of employing women artisans"
    
    # Founder
    edouard_bovet = Person("EdouardBovet")
    edouard_bovet.label = "Édouard Bovet"
    bovet_sa.foundedBy = [edouard_bovet]
    
    # Current owner
    pascal_raffy = Person("PascalRaffy")
    pascal_raffy.label = "Pascal Raffy"
    bovet_sa.currentOwner = pascal_raffy
    
    # Founding location
    london = City("London")
    london.label = "London"
    bovet_sa.foundedIn = [london]
    
    # Charter country
    united_kingdom = Country("UnitedKingdom")
    united_kingdom.label = "U.K."
    bovet_sa.charterCountry = [united_kingdom]
    
    # Historical market
    china = Country("China")
    china.label = "China"
    bovet_sa.servedMarket = [china]
    
    # Known dial model
    fleurier_models = DialModel("FleurierMiniaturePaintingModels")
    fleurier_models.label = "Fleurier Miniature Painting models"
    bovet_sa.knownForDialModel = [fleurier_models]
    
    # Known movement type
    tourbillon = MovementType("SevenDayTourbillon")
    tourbillon.label = "seven-day tourbillon"
    bovet_sa.knownForMovement = [tourbillon]
    
    # Time period
    nineteenth_century = Era("NineteenthCentury")
    nineteenth_century.label = "19th century"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
