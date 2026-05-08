"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. Who founded Bovet Fleurier SA and on what date was it chartered?
2. In which city and country was Bovet Fleurier SA chartered?
3. What type of company is Bovet Fleurier SA?
4. What is Bovet Fleurier SA best known for historically?
5. What market were Bovet’s pocket watches originally manufactured for?
6. What kinds of watches does Bovet Fleurier SA produce today?
7. What is the price range of Bovet Fleurier SA’s current watches?
8. What style characterizes Bovet Fleurier SA’s contemporary watches?
9. For what features is Bovet Fleurier SA known in its watchmaking?
10. What are examples of Bovet Fleurier SA’s high-quality dial models?
11. What special movement features are associated with Bovet watches?
12. What notable innovation regarding watch hands were Bovet watches among the first to include?
13. What traditions distinguish Bovet Fleurier SA’s workforce composition?
14. Who is the current owner of Bovet Fleurier SA?
15. What historical features of Bovet watches are referenced in the company’s current designs?
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
    AgentiveSocialObject,
    Feature,
    PhysicalObject,
    PhysicalQuality,
    SocialObject,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import constantPartOf, directQualityOf, temporallyLocatedAt


with core:
    class Company(AgentiveSocialObject):
        pass

    class LuxuryWatchmakerCompany(Company):
        pass

    class Person(AgentivePhysicalObject):
        pass

    class WomanArtisan(Person):
        pass

    class City(SocialObject):
        pass

    class Country(SocialObject):
        pass

    class Market(SocialObject):
        pass

    class Watch(PhysicalObject):
        pass

    class PocketWatch(Watch):
        pass

    class ArtisticWatch(Watch):
        pass

    class WatchFeature(Feature):
        pass

    class Dial(WatchFeature):
        pass

    class HighQualityDial(Dial):
        pass

    class Engraving(WatchFeature):
        pass

    class Tourbillon(WatchFeature):
        pass

    class SkeletonizedView(WatchFeature):
        pass

    class DecorativeMovement(WatchFeature):
        pass

    class SecondHand(WatchFeature):
        pass

    class Style(PhysicalQuality):
        pass

    class foundedBy(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Person]

    class charteredOn(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [TimeInterval]

    class charteredInCity(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [City]

    class charteredInCountry(ObjectProperty, FunctionalProperty):
        domain = [Company]
        range = [Country]

    class produces(ObjectProperty):
        domain = [Company]
        range = [Watch]

    class knownFor(ObjectProperty):
        domain = [Company]
        range = [Or([Watch, WatchFeature])]

    class employs(ObjectProperty):
        domain = [Company]
        range = [Person]

    class manufacturedForMarket(ObjectProperty, FunctionalProperty):
        domain = [PocketWatch]
        range = [Market]

    class hasPriceMinUSD(DataProperty, FunctionalProperty):
        domain = [ArtisticWatch]
        range = [float]

    class hasPriceMaxUSD(DataProperty, FunctionalProperty):
        domain = [ArtisticWatch]
        range = [float]

    BovetFleurierSA = LuxuryWatchmakerCompany("BovetFleurierSA")
    BovetFleurierSA.label = "Bovet Fleurier SA"

    EdouardBovet = Person("EdouardBovet")
    EdouardBovet.label = "Édouard Bovet"

    PascalRaffy = Person("PascalRaffy")
    PascalRaffy.label = "Pascal Raffy"

    London = City("London")
    London.label = "London"

    UK = Country("UK")
    UK.label = "U.K."

    May1_1822 = TimeInterval("May1_1822")
    May1_1822.label = "May 1 , 1822"

    ChineseMarket = Market("ChineseMarket")
    ChineseMarket.label = "Chinese market"

    NineteenthCentury = TimeInterval("NineteenthCentury")
    NineteenthCentury.label = "19th century"

    HighEndArtisticWatches = ArtisticWatch("HighEndArtisticWatches")
    HighEndArtisticWatches.label = "high - end artistic watches"
    HighEndArtisticWatches.hasPriceMinUSD = 18000.0
    HighEndArtisticWatches.hasPriceMaxUSD = 2500000.0

    OriginalBovetWatches = PocketWatch("OriginalBovetWatches")
    OriginalBovetWatches.label = "original Bovet watches"
    OriginalBovetWatches.manufacturedForMarket = ChineseMarket
    OriginalBovetWatches.temporallyLocatedAt = NineteenthCentury

    FleurierMiniaturePaintingModels = HighQualityDial("FleurierMiniaturePaintingModels")
    FleurierMiniaturePaintingModels.label = "Fleurier Miniature Painting models"
    FleurierMiniaturePaintingModels.constantPartOf.append(HighEndArtisticWatches)

    EngravingFeature = Engraving("EngravingFeature")
    EngravingFeature.label = "engraving"
    EngravingFeature.constantPartOf.append(HighEndArtisticWatches)

    SevenDayTourbillonFeature = Tourbillon("SevenDayTourbillonFeature")
    SevenDayTourbillonFeature.label = "seven - day tourbillon"
    SevenDayTourbillonFeature.constantPartOf.append(HighEndArtisticWatches)

    SkeletonizedViews = SkeletonizedView("SkeletonizedViews")
    SkeletonizedViews.label = "skeletonized views"
    SkeletonizedViews.constantPartOf.append(OriginalBovetWatches)

    HighlyDecorativeMovements = DecorativeMovement("HighlyDecorativeMovements")
    HighlyDecorativeMovements.label = "highly decorative movements"
    HighlyDecorativeMovements.constantPartOf.append(OriginalBovetWatches)

    SecondHandInnovation = SecondHand("SecondHandInnovation")
    SecondHandInnovation.label = "second hand"
    SecondHandInnovation.constantPartOf.append(OriginalBovetWatches)

    HistoryReferencingStyle = Style("HistoryReferencingStyle")
    HistoryReferencingStyle.label = "style that references its history"
    HistoryReferencingStyle.directQualityOf = HighEndArtisticWatches

    BovetFleurierSA.foundedBy = EdouardBovet
    BovetFleurierSA.charteredOn = May1_1822
    BovetFleurierSA.charteredInCity = London
    BovetFleurierSA.charteredInCountry = UK
    BovetFleurierSA.produces.append(HighEndArtisticWatches)
    BovetFleurierSA.knownFor.append(OriginalBovetWatches)
    BovetFleurierSA.knownFor.append(FleurierMiniaturePaintingModels)
    BovetFleurierSA.knownFor.append(EngravingFeature)
    BovetFleurierSA.knownFor.append(SevenDayTourbillonFeature)
    BovetFleurierSA.currentOwner = PascalRaffy
    BovetFleurierSA.is_a.append(employs.some(WomanArtisan))


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
