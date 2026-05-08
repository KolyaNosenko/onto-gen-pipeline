"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

What is the name of the luxury watchmaking brand described in the document?
Who founded Bovet Fleurier SA?
On what date was Bovet Fleurier SA chartered?
In which city and country was Bovet Fleurier SA chartered?
What type of company is Bovet Fleurier SA?
For which market were Bovet’s pocket watches manufactured in the 19th century?
What kinds of products does Bovet Fleurier SA produce today?
What is the price range of Bovet’s modern high-end artistic watches?
How does the style of Bovet’s current watches relate to its history?
For what qualities is Bovet Fleurier SA known?
Which Bovet models are associated with high-quality dials?
What horological feature is associated with Bovet’s seven-day watches?
Were original Bovet watches among the first to emphasize the beauty of their movements?
How were the movements of original Bovet watches visually presented?
Did original Bovet watches have highly decorative movements?
Were Bovet watches among the first to include a second hand?
Does Bovet Fleurier SA have a tradition of employing women artisans?
Is employing women artisans rare among traditional watchmaking companies in Europe?
Who is the current owner of Bovet Fleurier SA?
Is Bovet Fleurier SA a Swiss brand?
What century is particularly associated with Bovet’s pocket watches for the Chinese market?
What artistic craftsmanship techniques are associated with Bovet watches?
What decorative characteristics distinguish original Bovet watch movements?
What historical innovations are attributed to Bovet watches?
Which aspects of Bovet’s products reflect its heritage?
What is the relationship between Bovet Fleurier SA and Fleurier Miniature Painting models?
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
    class Agent(Thing):
        pass

    class Person(Agent):
        pass

    class Organization(Agent):
        pass

    class Company(Organization):
        pass

    class Brand(Organization):
        pass

    class WatchmakingCompany(Company):
        pass

    class LuxuryWatchmakingCompany(WatchmakingCompany):
        pass

    class LuxuryWatchmakingBrand(Brand):
        pass

    class SwissLuxuryWatchmakingBrand(LuxuryWatchmakingCompany, LuxuryWatchmakingBrand):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class Country(Place):
        pass

    class Region(Place):
        pass

    class Market(Place):
        pass

    class TimeEntity(Thing):
        pass

    class CalendarDate(TimeEntity):
        pass

    class HistoricalPeriod(TimeEntity):
        pass

    class MonetaryAmount(Thing):
        pass

    class Product(Thing):
        pass

    class Watch(Product):
        pass

    class PocketWatch(Watch):
        pass

    class ArtisticWatch(Watch):
        pass

    class WatchModel(Watch):
        pass

    class MiniaturePaintingModel(WatchModel):
        pass

    class WatchComponent(Thing):
        pass

    class Dial(WatchComponent):
        pass

    class Movement(WatchComponent):
        pass

    class Feature(Thing):
        pass

    class CraftTechnique(Feature):
        pass

    class HorologicalFeature(Feature):
        pass

    class VisualPresentationFeature(Feature):
        pass

    class MovementCharacteristic(Feature):
        pass

    class Artisan(Agent):
        pass

    class WomenArtisan(Artisan):
        pass

    class foundedBy(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Person]

    class charteredBy(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Person]

    class charteredOn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [CalendarDate]

    class charteredInCity(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [City]

    class charteredInCountry(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Country]

    class hasCurrentOwner(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Person]

    class manufacturedForMarket(ObjectProperty):
        domain = [Organization, Product]
        range = [Market]

    class associatedWithPeriod(ObjectProperty):
        domain = [Thing]
        range = [HistoricalPeriod]

    class producesToday(ObjectProperty):
        domain = [Organization]
        range = [Watch]

    class knownForModel(ObjectProperty):
        domain = [Organization]
        range = [WatchModel]

    class hasMinimumPrice(ObjectProperty, FunctionalProperty):
        domain = [Organization, ArtisticWatch]
        range = [MonetaryAmount]

    class hasMaximumPrice(ObjectProperty, FunctionalProperty):
        domain = [Organization, ArtisticWatch]
        range = [MonetaryAmount]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class hasCompanyType(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class notedForProductType(DataProperty):
        domain = [Organization]
        range = [str]

    class producesTodayDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class hasStyleDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class knownForDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class craftTechniqueDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class horologicalFeatureDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class movementPresentationDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class movementDecorationDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class historicalInnovationDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class reflectsHeritageAspectDescription(DataProperty):
        domain = [Organization]
        range = [str]

    class associatedDialQuality(DataProperty, FunctionalProperty):
        domain = [WatchModel]
        range = [str]

    class employsWomenArtisansTraditionally(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class employingWomenArtisansRareInEurope(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class rareContextDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class emphasizesMovementBeauty(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class hasSkeletonizedViews(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class hasHighlyDecorativeMovements(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class includesSecondHand(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class isSwissBrand(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    WatchmakingCompany.is_a.append(producesToday.some(Watch))
    PocketWatch.is_a.append(manufacturedForMarket.some(Market))
    ArtisticWatch.is_a.append(hasMinimumPrice.some(MonetaryAmount))
    ArtisticWatch.is_a.append(hasMaximumPrice.some(MonetaryAmount))
    SwissLuxuryWatchmakingBrand.is_a.append(foundedBy.some(Person))
    SwissLuxuryWatchmakingBrand.is_a.append(charteredOn.some(CalendarDate))
    SwissLuxuryWatchmakingBrand.is_a.append(charteredInCity.some(City))
    SwissLuxuryWatchmakingBrand.is_a.append(charteredInCountry.some(Country))
    SwissLuxuryWatchmakingBrand.is_a.append(hasCurrentOwner.some(Person))

    BovetFleurierSA = SwissLuxuryWatchmakingBrand("BovetFleurierSACompany")
    BovetFleurierSA.label = "Bovet Fleurier SA"

    London = City("LondonCity")
    London.label = "London"

    UK = Country("UKCountry")
    UK.label = "U.K."

    EdouardBovet = Person("EdouardBovetPerson")
    EdouardBovet.label = "Édouard Bovet"

    ChineseMarket = Market("ChineseMarket")
    ChineseMarket.label = "Chinese market"

    NineteenthCentury = HistoricalPeriod("NineteenthCentury")
    NineteenthCentury.label = "19th century"

    May11822 = CalendarDate("May1_1822")
    May11822.label = "May 1 , 1822"

    FleurierMiniaturePaintingModels = MiniaturePaintingModel("FleurierMiniaturePaintingModels")
    FleurierMiniaturePaintingModels.label = "Fleurier Miniature Painting models"

    Europe = Region("EuropeRegion")
    Europe.label = "Europe"

    PascalRaffy = Person("PascalRaffyPerson")
    PascalRaffy.label = "Pascal Raffy"

    MinimumModernPrice = MonetaryAmount("MinimumModernPrice")
    MinimumModernPrice.label = "US$ 18,000"

    MaximumModernPrice = MonetaryAmount("MaximumModernPrice")
    MaximumModernPrice.label = "$ 2.5 million"

    BovetFleurierSA.foundedBy = EdouardBovet
    BovetFleurierSA.charteredBy = EdouardBovet
    BovetFleurierSA.charteredOn = May11822
    BovetFleurierSA.charteredInCity = London
    BovetFleurierSA.charteredInCountry = UK
    BovetFleurierSA.hasCurrentOwner = PascalRaffy
    BovetFleurierSA.manufacturedForMarket = [ChineseMarket]
    BovetFleurierSA.associatedWithPeriod = [NineteenthCentury]
    BovetFleurierSA.knownForModel = [FleurierMiniaturePaintingModels]
    BovetFleurierSA.hasMinimumPrice = MinimumModernPrice
    BovetFleurierSA.hasMaximumPrice = MaximumModernPrice
    BovetFleurierSA.hasCompanyType = "Swiss brand of luxury watchmakers"
    BovetFleurierSA.notedForProductType = ["pocket watches"]
    BovetFleurierSA.producesTodayDescription = ["high-end artistic watches"]
    BovetFleurierSA.hasStyleDescription = "style that references its history"
    BovetFleurierSA.knownForDescription = ["high-quality dials", "engraving", "seven-day tourbillon"]
    BovetFleurierSA.craftTechniqueDescription = ["engraving", "miniature painting"]
    BovetFleurierSA.horologicalFeatureDescription = ["seven-day tourbillon"]
    BovetFleurierSA.movementPresentationDescription = ["skeletonized views"]
    BovetFleurierSA.movementDecorationDescription = ["highly decorative movements"]
    BovetFleurierSA.historicalInnovationDescription = [
        "emphasizing the beauty of movements",
        "including a second hand",
    ]
    BovetFleurierSA.reflectsHeritageAspectDescription = [
        "high-end artistic watches",
        "style that references its history",
    ]
    BovetFleurierSA.employsWomenArtisansTraditionally = True
    BovetFleurierSA.employingWomenArtisansRareInEurope = True
    BovetFleurierSA.rareContextDescription = "traditional watch making companies in Europe"
    BovetFleurierSA.emphasizesMovementBeauty = True
    BovetFleurierSA.hasSkeletonizedViews = True
    BovetFleurierSA.hasHighlyDecorativeMovements = True
    BovetFleurierSA.includesSecondHand = True
    BovetFleurierSA.isSwissBrand = True

    FleurierMiniaturePaintingModels.associatedDialQuality = "high-quality dials"
    London.partOf = [UK]
    UK.partOf = [Europe]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
