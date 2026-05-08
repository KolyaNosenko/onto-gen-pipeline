"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

What is Bovet Fleurier SA?
When was Bovet Fleurier SA chartered?
On what date was Bovet Fleurier SA chartered?
Where was Bovet Fleurier SA chartered?
Who chartered Bovet Fleurier SA?
What type of brand is Bovet Fleurier SA?
In which country is Bovet Fleurier SA based?
For what is Bovet Fleurier SA most noted?
What kind of watches did Bovet Fleurier SA manufacture for the Chinese market in the 19th century?
Which market was especially important for Bovet Fleurier SA in the 19th century?
What products does Bovet Fleurier SA produce today?
What is the price range of Bovet Fleurier SA’s watches today?
How does the style of Bovet Fleurier SA’s current watches relate to its history?
What are the distinctive quality features associated with Bovet Fleurier SA watches?
Which Bovet Fleurier SA models are examples of high-quality dials?
What decorative techniques are associated with Bovet Fleurier SA watches?
What is notable about Bovet Fleurier SA’s tourbillon?
What visual design features distinguished the original Bovet watches?
How did the original Bovet watches emphasize the beauty of their movements?
Were Bovet watches among the first to include a second hand?
What innovations are associated with the original Bovet watches?
What is unusual about Bovet Fleurier SA’s employment tradition in the context of European watchmaking?
Did Bovet Fleurier SA traditionally employ women artisans?
Why is Bovet Fleurier SA’s tradition of employing women artisans considered rare?
Who is the current owner of Bovet Fleurier SA?
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
    Abstract,
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    NonPhysicalObject,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class Person(AgentivePhysicalObject):
        pass


    class WatchmakingCompany(Society):
        pass


    class LuxuryWatchmakingBrand(WatchmakingCompany):
        pass


    class SwissWatchmakingBrand(LuxuryWatchmakingBrand):
        pass


    class GeographicPlace(SpaceRegion):
        pass


    class City(GeographicPlace):
        pass


    class Country(GeographicPlace):
        pass


    class Continent(GeographicPlace):
        pass


    class Market(NonAgentiveSocialObject):
        pass


    class Watch(NonAgentivePhysicalObject):
        pass


    class PocketWatch(Watch):
        pass


    class ArtisticWatch(Watch):
        pass


    class HighEndArtisticWatch(ArtisticWatch):
        pass


    class WatchStyle(NonPhysicalObject):
        pass


    class HistoricallyReferentialStyle(WatchStyle):
        pass


    class WatchFeature(NonPhysicalObject):
        pass


    class HighQualityDial(WatchFeature):
        pass


    class Engraving(WatchFeature):
        pass


    class Tourbillon(WatchFeature):
        pass


    class SevenDayTourbillon(Tourbillon):
        pass


    class SkeletonizedView(WatchFeature):
        pass


    class HighlyDecorativeMovement(WatchFeature):
        pass


    class SecondHandFeature(WatchFeature):
        pass


    class WatchModel(NonPhysicalObject):
        pass


    class HighQualityDialModel(WatchModel):
        pass


    class EmploymentTradition(NonPhysicalObject):
        pass


    class WomenArtisanEmploymentTradition(EmploymentTradition):
        pass


    class WomanArtisan(Person):
        pass


    class TraditionalWatchMakingCompany(WatchmakingCompany):
        pass


    class TraditionalEuropeanWatchMakingCompany(TraditionalWatchMakingCompany):
        pass


    class HistoricalPeriod(TimeInterval):
        pass


    class CalendarDate(TimeInterval):
        pass


    class MonetaryAmount(Abstract):
        pass


    class ChineseMarketPocketWatch(PocketWatch):
        pass


    class CurrentBovetArtisticWatch(HighEndArtisticWatch):
        pass


    class OriginalBovetWatch(PocketWatch):
        pass


    class BovetFleurierSAWatchmakingBrand(SwissWatchmakingBrand):
        pass


    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Country]


    class charteredOn(ObjectProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [TimeInterval]


    class charteredIn(ObjectProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [City]


    class charteredInCountry(ObjectProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [Country]


    class charteredBy(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Person]


    class basedInCountryDescriptor(DataProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [str]


    class hasCurrentOwner(ObjectProperty, FunctionalProperty):
        domain = [WatchmakingCompany]
        range = [Person]


    class mostNotedFor(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Watch]


    class historicallyProduced(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Watch]


    class manufacturedForMarket(ObjectProperty):
        domain = [Watch]
        range = [Market]


    class manufacturedDuring(ObjectProperty):
        domain = [Watch]
        range = [TimeInterval]


    class currentlyProduces(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [Watch]


    class pricedFrom(ObjectProperty, FunctionalProperty):
        domain = [Watch]
        range = [MonetaryAmount]


    class pricedTo(ObjectProperty, FunctionalProperty):
        domain = [Watch]
        range = [MonetaryAmount]


    class hasWatchStyle(ObjectProperty):
        domain = [Watch]
        range = [WatchStyle]


    class referencesHistoryOf(ObjectProperty):
        domain = [WatchStyle]
        range = [WatchmakingCompany]


    class knownForFeature(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [WatchFeature]


    class hasModelExample(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [WatchModel]


    class illustratesFeature(ObjectProperty):
        domain = [WatchModel]
        range = [WatchFeature]


    class emphasizesMovementBeautyWith(ObjectProperty):
        domain = [Watch]
        range = [WatchFeature]


    class pioneeredFeature(ObjectProperty):
        domain = [Watch]
        range = [WatchFeature]


    class hasEmploymentTradition(ObjectProperty):
        domain = [WatchmakingCompany]
        range = [EmploymentTradition]


    class employsArtisan(ObjectProperty):
        domain = [EmploymentTradition]
        range = [Person]


    class rareAmong(ObjectProperty):
        domain = [EmploymentTradition]
        range = [WatchmakingCompany]


    class rareInRegion(ObjectProperty, FunctionalProperty):
        domain = [EmploymentTradition]
        range = [Continent]


    class durationDays(DataProperty, FunctionalProperty):
        domain = [Tourbillon]
        range = [int]


    BovetFleurierSA = BovetFleurierSAWatchmakingBrand("BovetFleurierSAInstance")
    BovetFleurierSA.label = "Bovet Fleurier SA"

    EdouardBovet = Person("EdouardBovetInstance")
    EdouardBovet.label = "Édouard Bovet"

    London = City("LondonInstance")
    London.label = "London"

    UK = Country("UKInstance")
    UK.label = "U.K."

    May11822 = CalendarDate("May11822Instance")
    May11822.label = "May 1 , 1822"

    ChineseMarket = Market("ChineseMarketInstance")
    ChineseMarket.label = "Chinese market"

    NineteenthCentury = HistoricalPeriod("NineteenthCenturyInstance")
    NineteenthCentury.label = "19th century"

    MinimumWatchPrice = MonetaryAmount("MinimumWatchPriceInstance")
    MinimumWatchPrice.label = "US$ 18,000"

    MaximumWatchPrice = MonetaryAmount("MaximumWatchPriceInstance")
    MaximumWatchPrice.label = "$ 2.5 million"

    FleurierMiniaturePaintingModels = HighQualityDialModel(
        "FleurierMiniaturePaintingModelsInstance"
    )
    FleurierMiniaturePaintingModels.label = "Fleurier Miniature Painting models"

    Europe = Continent("EuropeInstance")
    Europe.label = "Europe"

    PascalRaffy = Person("PascalRaffyInstance")
    PascalRaffy.label = "Pascal Raffy"

    London.locatedInCountry = UK

    BovetFleurierSA.charteredOn = May11822
    BovetFleurierSA.charteredIn = London
    BovetFleurierSA.charteredInCountry = UK
    BovetFleurierSA.charteredBy.append(EdouardBovet)
    BovetFleurierSA.basedInCountryDescriptor = "Swiss"
    BovetFleurierSA.hasCurrentOwner = PascalRaffy
    BovetFleurierSA.hasModelExample.append(FleurierMiniaturePaintingModels)

    HighQualityDialModel.is_a.append(illustratesFeature.some(HighQualityDial))
    SevenDayTourbillon.is_a.append(durationDays.value(7))
    HistoricallyReferentialStyle.is_a.append(referencesHistoryOf.value(BovetFleurierSA))
    ChineseMarketPocketWatch.is_a.extend([
        manufacturedForMarket.value(ChineseMarket),
        manufacturedDuring.value(NineteenthCentury),
    ])
    CurrentBovetArtisticWatch.is_a.extend([
        pricedFrom.value(MinimumWatchPrice),
        pricedTo.value(MaximumWatchPrice),
        hasWatchStyle.some(HistoricallyReferentialStyle),
    ])
    OriginalBovetWatch.is_a.extend([
        emphasizesMovementBeautyWith.some(SkeletonizedView),
        emphasizesMovementBeautyWith.some(HighlyDecorativeMovement),
        pioneeredFeature.some(SkeletonizedView),
        pioneeredFeature.some(HighlyDecorativeMovement),
        pioneeredFeature.some(SecondHandFeature),
    ])
    WomenArtisanEmploymentTradition.is_a.extend([
        employsArtisan.some(WomanArtisan),
        rareAmong.some(TraditionalEuropeanWatchMakingCompany),
        rareInRegion.value(Europe),
    ])
    BovetFleurierSAWatchmakingBrand.is_a.extend([
        mostNotedFor.some(ChineseMarketPocketWatch),
        currentlyProduces.some(CurrentBovetArtisticWatch),
        knownForFeature.some(HighQualityDial),
        knownForFeature.some(Engraving),
        knownForFeature.some(SevenDayTourbillon),
        historicallyProduced.some(OriginalBovetWatch),
        hasEmploymentTradition.some(WomenArtisanEmploymentTradition),
    ])


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
