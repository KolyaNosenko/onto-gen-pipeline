"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. Who founded Bovet Fleurier SA and when and where was it chartered?
2. What type of company is Bovet Fleurier SA?
3. In which country is Bovet Fleurier SA based?
4. For which market were Bovet’s pocket watches mainly manufactured in the 19th century?
5. What products does Bovet Fleurier SA produce today?
6. What is the price range of Bovet Fleurier SA’s current watches?
7. What historical elements are referenced in Bovet Fleurier SA’s current watch styles?
8. What is Bovet Fleurier SA known for in terms of watch features and craftsmanship?
9. Which specific watch models are mentioned as examples of Bovet’s high-quality dials?
10. What special movement feature is Bovet known for?
11. What decorative or structural characteristics distinguished the original Bovet watches?
12. What innovation related to time display were Bovet watches among the first to include?
13. What tradition does Bovet Fleurier SA have regarding its artisans?
14. Who is the current owner of Bovet Fleurier SA?
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
    class Organization(Thing):
        pass

    class Company(Organization):
        pass

    class Brand(Organization):
        pass

    class WatchmakingCompany(Company):
        pass

    class TraditionalWatchmakingCompany(WatchmakingCompany):
        pass

    class LuxuryWatchmakingBrand(Brand):
        pass

    class SwissBrand(LuxuryWatchmakingBrand):
        pass

    class Person(Thing):
        pass

    class Artisan(Person):
        pass

    class WomanArtisan(Artisan):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class Country(Place):
        pass

    class Continent(Place):
        pass

    class Market(Thing):
        pass

    class ChineseMarket(Market):
        pass

    class TimePoint(Thing):
        pass

    class DatePoint(TimePoint):
        pass

    class Century(TimePoint):
        pass

    class NineteenthCentury(Century):
        pass

    class Quantity(Thing):
        pass

    class MonetaryQuantity(Quantity):
        pass

    class PriceRange(MonetaryQuantity):
        pass

    class Artifact(Thing):
        pass

    class Watch(Artifact):
        pass

    class PocketWatch(Watch):
        pass

    class ArtisticWatch(Watch):
        pass

    class Dial(Artifact):
        pass

    class DialModel(Dial):
        pass

    class Movement(Artifact):
        pass

    class Tourbillon(Movement):
        pass

    class SevenDayTourbillon(Tourbillon):
        pass

    class Hand(Artifact):
        pass

    class SecondHand(Hand):
        pass

    class Feature(Thing):
        pass

    class Engraving(Feature):
        pass

    class SkeletonizedView(Feature):
        pass

    class DecorativeMovement(Feature):
        pass

    class Style(Thing):
        pass

    class History(Thing):
        pass

    class foundedBy(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Person]

    class charteredOn(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [DatePoint]

    class charteredIn(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [City]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Country]

    class basedInCountryName(DataProperty, FunctionalProperty):
        domain = [Company]
        range = [str]

    class priceRange(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [PriceRange]

    class produces(ObjectProperty):
        domain = [Company]
        range = [Watch]

    class mostNotedFor(ObjectProperty):
        domain = [Company]
        range = [PocketWatch]

    class manufacturedForMarket(ObjectProperty):
        domain = [PocketWatch]
        range = [Market]

    class manufacturedDuring(ObjectProperty):
        domain = [PocketWatch]
        range = [Century]

    class styleReferencesHistory(ObjectProperty):
        domain = [ArtisticWatch]
        range = [History]

    class knownFor(ObjectProperty):
        domain = [Company]
        range = [Thing]

    class hasDialExample(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [DialModel]

    class employs(ObjectProperty):
        domain = [Company]
        range = [WomanArtisan]

    class currentOwner(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Person]

    PocketWatch.is_a.append(manufacturedForMarket.some(ChineseMarket))
    PocketWatch.is_a.append(manufacturedDuring.some(NineteenthCentury))
    ArtisticWatch.is_a.append(styleReferencesHistory.some(History))

    BovetFleurierSA = SwissBrand("BovetFleurierSA", is_a=[Company, WatchmakingCompany])
    BovetFleurierSA.label = "Bovet Fleurier SA"
    BovetFleurierSA.basedInCountryName = "Switzerland"
    BovetFleurierSA.is_a.extend([
        produces.some(ArtisticWatch),
        mostNotedFor.some(PocketWatch),
        knownFor.some(Dial),
        knownFor.some(Engraving),
        knownFor.some(SevenDayTourbillon),
        knownFor.some(SkeletonizedView),
        knownFor.some(DecorativeMovement),
        knownFor.some(SecondHand),
        employs.some(WomanArtisan),
    ])

    EdouardBovet = Person("EdouardBovet")
    EdouardBovet.label = "Édouard Bovet"

    PascalRaffy = Person("PascalRaffy")
    PascalRaffy.label = "Pascal Raffy"

    London = City("London")
    London.label = "London"

    UK = Country("UK")
    UK.label = "U.K."

    Europe = Continent("Europe")
    Europe.label = "Europe"

    May11822 = DatePoint("May11822")
    May11822.label = "May 1 , 1822"

    NineteenthCenturyPeriod = NineteenthCentury("NineteenthCenturyPeriod")
    NineteenthCenturyPeriod.label = "19th century"

    PriceRangeUsd18000To25Million = PriceRange("PriceRangeUsd18000To25Million")
    PriceRangeUsd18000To25Million.label = "priced between US$ 18,000 and $ 2.5 million"

    FleurierMiniaturePaintingModels = DialModel("FleurierMiniaturePaintingModels")
    FleurierMiniaturePaintingModels.label = "Fleurier Miniature Painting models"

    BovetFleurierSA.foundedBy = EdouardBovet
    BovetFleurierSA.charteredOn = May11822
    BovetFleurierSA.charteredIn = London
    BovetFleurierSA.priceRange = PriceRangeUsd18000To25Million
    BovetFleurierSA.hasDialExample = FleurierMiniaturePaintingModels
    BovetFleurierSA.currentOwner = PascalRaffy
    London.locatedInCountry = UK


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
