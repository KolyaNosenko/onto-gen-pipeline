"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. What is the nationality or country of origin of Bovet Fleurier SA?
2. When was Bovet Fleurier SA chartered?
3. Where was Bovet Fleurier SA founded?
4. Who founded Bovet Fleurier SA?
5. What type of products does Bovet Fleurier SA produce?
6. What market were the original Bovet pocket watches manufactured for?
7. What is the price range of Bovet Fleurier SA watches?
8. What are the notable features or specialties of Bovet Fleurier SA watches?
9. What is the name of the dial models produced by Bovet Fleurier SA?
10. What type of tourbillon is Bovet Fleurier SA known for?
11. What innovative features did the original Bovet watches introduce?
12. What is the tradition of Bovet Fleurier SA regarding its workforce?
13. Who is the current owner of Bovet Fleurier SA?
14. In which century did Bovet Fleurier SA manufacture pocket watches for the Chinese market?
15. What artistic techniques is Bovet Fleurier SA known for in its watchmaking?
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
    # --- Entity Classes ---

    class Organisation(Thing): pass
    class WatchCompany(Organisation): pass

    class Person(Thing): pass

    class Place(Thing): pass
    class Country(Place): pass
    class City(Place): pass

    class Market(Thing): pass
    class Century(Thing): pass

    class Watch(Thing): pass
    class PocketWatch(Watch): pass
    class ArtisticWatch(Watch): pass

    class WatchComponent(Thing): pass
    class Dial(WatchComponent): pass
    class Tourbillon(WatchComponent): pass
    class WatchMovement(WatchComponent): pass

    class WatchFeature(Thing): pass
    class WatchmakingTechnique(Thing): pass

    # --- Object Properties ---

    class foundedBy(ObjectProperty):
        domain = [WatchCompany]
        range  = [Person]

    class foundedInCity(ObjectProperty, FunctionalProperty):
        domain = [WatchCompany]
        range  = [City]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    class hasCountryOfOrigin(ObjectProperty, FunctionalProperty):
        domain = [WatchCompany]
        range  = [Country]

    class hasCurrentOwner(ObjectProperty, FunctionalProperty):
        domain = [WatchCompany]
        range  = [Person]

    class producesWatch(ObjectProperty):
        domain = [WatchCompany]
        range  = [Watch]

    class manufacturedFor(ObjectProperty):
        domain = [Watch]
        range  = [Market]

    class manufacturedInCentury(ObjectProperty, FunctionalProperty):
        domain = [Watch]
        range  = [Century]

    class hasDial(ObjectProperty):
        domain = [Watch]
        range  = [Dial]

    class hasTourbillon(ObjectProperty):
        domain = [Watch]
        range  = [Tourbillon]

    class hasMovement(ObjectProperty):
        domain = [Watch]
        range  = [WatchMovement]

    class hasFeature(ObjectProperty):
        domain = [Watch]
        range  = [WatchFeature]

    class usesWatchmakingTechnique(ObjectProperty):
        domain = [WatchCompany]
        range  = [WatchmakingTechnique]

    class isKnownFor(ObjectProperty):
        domain = [WatchCompany]
        range  = [Thing]

    # --- Data Properties ---

    class charteredDate(DataProperty, FunctionalProperty):
        domain = [WatchCompany]
        range  = [str]

    class minimumPrice(DataProperty, FunctionalProperty):
        domain = [Watch]
        range  = [float]

    class maximumPrice(DataProperty, FunctionalProperty):
        domain = [Watch]
        range  = [float]

    class employsWomenArtisans(DataProperty, FunctionalProperty):
        domain = [WatchCompany]
        range  = [bool]

    # --- Individuals ---

    # Places
    switzerland = Country("Switzerland")
    switzerland.label = "Switzerland"

    uk = Country("UK")
    uk.label = "U.K."

    london = City("London")
    london.label = "London"
    london.locatedIn = [uk]

    # Persons
    edouardBovet = Person("EdouardBovet")
    edouardBovet.label = "Édouard Bovet"

    pascalRaffy = Person("PascalRaffy")
    pascalRaffy.label = "Pascal Raffy"

    # Market and time
    chineseMarket = Market("ChineseMarket")
    chineseMarket.label = "Chinese market"

    nineteenthCentury = Century("NineteenthCentury")
    nineteenthCentury.label = "19th century"

    # Watch components / features / techniques
    fleurierMiniaturePainting = Dial("FleurierMiniaturePainting")
    fleurierMiniaturePainting.label = "Fleurier Miniature Painting"

    sevenDayTourbillon = Tourbillon("SevenDayTourbillon")
    sevenDayTourbillon.label = "seven-day tourbillon"

    engraving = WatchmakingTechnique("Engraving")
    engraving.label = "engraving"

    miniaturePainting = WatchmakingTechnique("MiniaturePainting")
    miniaturePainting.label = "miniature painting"

    skeletonizedView = WatchFeature("SkeletonizedView")
    skeletonizedView.label = "skeletonized views"

    secondHand = WatchFeature("SecondHand")
    secondHand.label = "second hand"

    # Watch product instances
    bovetPocketWatch = PocketWatch("BovetPocketWatch")
    bovetPocketWatch.label = "pocket watches"
    bovetPocketWatch.manufacturedFor = [chineseMarket]
    bovetPocketWatch.manufacturedInCentury = nineteenthCentury
    bovetPocketWatch.hasFeature = [skeletonizedView, secondHand]

    bovetArtisticWatch = ArtisticWatch("BovetArtisticWatch")
    bovetArtisticWatch.label = "artistic watches"
    bovetArtisticWatch.minimumPrice = 18000.0
    bovetArtisticWatch.maximumPrice = 2500000.0
    bovetArtisticWatch.hasDial = [fleurierMiniaturePainting]
    bovetArtisticWatch.hasTourbillon = [sevenDayTourbillon]

    # Main company
    bovetFleurierSA = WatchCompany("BovetFleurierSA")
    bovetFleurierSA.label = "Bovet Fleurier SA"
    bovetFleurierSA.hasCountryOfOrigin = switzerland
    bovetFleurierSA.foundedBy = [edouardBovet]
    bovetFleurierSA.foundedInCity = london
    bovetFleurierSA.charteredDate = "May 1, 1822"
    bovetFleurierSA.hasCurrentOwner = pascalRaffy
    bovetFleurierSA.producesWatch = [bovetPocketWatch, bovetArtisticWatch]
    bovetFleurierSA.usesWatchmakingTechnique = [engraving, miniaturePainting]
    bovetFleurierSA.isKnownFor = [fleurierMiniaturePainting, sevenDayTourbillon,
                                   engraving, miniaturePainting]
    bovetFleurierSA.employsWomenArtisans = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
