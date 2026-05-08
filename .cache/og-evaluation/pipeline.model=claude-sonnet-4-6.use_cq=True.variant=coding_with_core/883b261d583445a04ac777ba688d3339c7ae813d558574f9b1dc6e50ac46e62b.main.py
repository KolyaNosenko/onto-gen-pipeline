"""
=== TASK INPUT ===
Source text:
Bovet Fleurier SA is a Swiss brand of luxury watchmakers chartered May 1 , 1822 in London , U.K. by Édouard Bovet . It is most noted for its pocket watches manufactured for the Chinese market in the 19th century . Today it produces high - end artistic watches ( priced between US$ 18,000 and $ 2.5 million ) with a style that references its history . The company is known for its high - quality dials ( such as the Fleurier Miniature Painting models ) , engraving , and its seven - day tourbillon . The original Bovet watches were also among the first to emphasize the beauty of their movements with skeletonized views and highly decorative movements . Bovet watches were also among the first to include a second hand while the company has a tradition of employing women artisans , which is rare for traditional watch making companies in Europe . Pascal Raffy is the current owner .

1. What is the nationality or origin of the Bovet Fleurier SA brand?
2. When was Bovet Fleurier SA chartered?
3. Where was Bovet Fleurier SA chartered?
4. Who founded Bovet Fleurier SA?
5. For which market were the original Bovet pocket watches primarily manufactured?
6. During which century were Bovet watches manufactured for the Chinese market?
7. What is the price range of Bovet Fleurier SA watches?
8. What types of products does Bovet Fleurier SA currently produce?
9. What notable features or complications are associated with Bovet watches?
10. What dial models is Bovet Fleurier SA known for?
11. What decorative techniques is Bovet Fleurier SA known for?
12. What was innovative about the original Bovet watch movements?
13. What was Bovet among the first watch companies to include on their watches?
14. What is the employment tradition that distinguishes Bovet Fleurier SA from other European watchmaking companies?
15. Who is the current owner of Bovet Fleurier SA?
16. What style references does Bovet Fleurier SA incorporate into its modern watches?
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

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    Feature,
    NonAgentiveSocialObject,
    Society,
    Achievement,
    TimeInterval,
)

# TODO (optional): import the core properties you actually subclass.
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ------------------------------------------------------------------ #
    # Entity classes                                                       #
    # ------------------------------------------------------------------ #

    class LuxuryWatchCompany(Society):
        """A company (collective social agent) that designs and manufactures
        luxury watches."""

    class Person(AgentivePhysicalObject):
        """A human individual; used for the founder and the current owner."""

    class Watch(NonAgentivePhysicalObject):
        """A physical timekeeping artefact produced by a watch company."""

    class PocketWatch(Watch):
        """A watch carried in a pocket, not worn on the wrist."""

    class LuxuryArtisticWatch(Watch):
        """A high-end artistic watch, as currently produced by Bovet."""

    class WatchComplication(Feature):
        """A functional or decorative complication that is a feature of a
        watch (e.g. tourbillon, second hand)."""

    class WatchDial(Feature):
        """The dial face component of a watch."""

    class WatchMovement(Feature):
        """The mechanical movement component of a watch."""

    class DecorativeTechnique(NonAgentiveSocialObject):
        """A craft technique applied for decorative effect on watches
        (e.g. engraving, miniature painting)."""

    class WatchDialModel(NonAgentiveSocialObject):
        """A named dial design or product-line model (e.g. Fleurier
        Miniature Painting)."""

    class City(NonAgentiveSocialObject):
        """An administrative urban settlement (e.g. London)."""

    class Country(Society):
        """A nation-state or sovereign country (e.g. Switzerland, U.K.)."""

    class Market(NonAgentiveSocialObject):
        """A commercial or geographical market targeted by a product
        (e.g. Chinese market)."""

    class CharteringEvent(Achievement):
        """The instantaneous act by which a company is formally chartered
        (incorporated)."""

    # ------------------------------------------------------------------ #
    # Properties                                                           #
    # ------------------------------------------------------------------ #

    class charteredBy(ObjectProperty):
        """Links a CharteringEvent to the Person who carried it out."""
        domain = [CharteringEvent]
        range  = [Person]

    class charteredIn(ObjectProperty):
        """Links a CharteringEvent to the City where it took place."""
        domain = [CharteringEvent]
        range  = [City]

    class charteringOf(ObjectProperty):
        """Links a CharteringEvent to the LuxuryWatchCompany that was
        chartered."""
        domain = [CharteringEvent]
        range  = [LuxuryWatchCompany]

    class hasOriginCountry(ObjectProperty):
        """The country of origin (nationality) of a watch company."""
        domain = [LuxuryWatchCompany]
        range  = [Country]

    class hasOwner(ObjectProperty):
        """The current owner of a watch company."""
        domain = [LuxuryWatchCompany]
        range  = [Person]

    class manufactures(ObjectProperty):
        """Relates a watch company to the type of watch it produces."""
        domain = [LuxuryWatchCompany]
        range  = [Watch]

    class hasComplication(ObjectProperty):
        """Associates a watch company (or watch) with a complication it
        features."""
        domain = [LuxuryWatchCompany]
        range  = [WatchComplication]

    class usesDecorativeTechnique(ObjectProperty):
        """Relates a watch company to a decorative technique it is known
        for."""
        domain = [LuxuryWatchCompany]
        range  = [DecorativeTechnique]

    class hasDialModel(ObjectProperty):
        """Relates a watch company to a specific dial model or product line
        it is known for."""
        domain = [LuxuryWatchCompany]
        range  = [WatchDialModel]

    class locatedIn(ObjectProperty):
        """Relates a City to the Country it is located in."""
        domain = [City]
        range  = [Country]

    class historicalProductMarket(ObjectProperty):
        """The market for which a company historically manufactured its
        products."""
        domain = [LuxuryWatchCompany]
        range  = [Market]

    class historicalProductionPeriod(ObjectProperty):
        """The time interval during which a company's historical production
        took place."""
        domain = [LuxuryWatchCompany]
        range  = [TimeInterval]

    class minimumWatchPriceUSD(DataProperty, FunctionalProperty):
        """Minimum retail price (in USD) of watches produced by a
        company."""
        domain = [LuxuryWatchCompany]
        range  = [float]

    class maximumWatchPriceUSD(DataProperty, FunctionalProperty):
        """Maximum retail price (in USD) of watches produced by a
        company."""
        domain = [LuxuryWatchCompany]
        range  = [float]

    class styleReference(DataProperty):
        """A textual note on the stylistic inspiration or reference of a
        company's products."""
        domain = [LuxuryWatchCompany]
        range  = [str]

    class employmentTradition(DataProperty):
        """A textual description of a notable employment tradition at a
        company."""
        domain = [LuxuryWatchCompany]
        range  = [str]

    # ------------------------------------------------------------------ #
    # Named individuals                                                    #
    # ------------------------------------------------------------------ #

    # Countries
    switzerland = Country("Switzerland")
    switzerland.label = "Swiss"

    uk = Country("UK")
    uk.label = "U.K."

    # City
    london = City("London")
    london.label = "London"
    london.locatedIn.append(uk)

    # Persons
    edouardBovet = Person("EdouardBovet")
    edouardBovet.label = "Édouard Bovet"

    pascalRaffy = Person("PascalRaffy")
    pascalRaffy.label = "Pascal Raffy"

    # Time intervals
    may1_1822 = TimeInterval("May1_1822")
    may1_1822.label = "May 1 , 1822"

    the19thCentury = TimeInterval("The19thCentury")
    the19thCentury.label = "19th century"

    # Market
    chineseMarket = Market("ChineseMarket")
    chineseMarket.label = "Chinese market"

    # Chartering event (Achievement — instantaneous act)
    charteringEvent = CharteringEvent("BovetChartering1822")
    charteringEvent.label = "Bovet Fleurier SA chartering, May 1 , 1822"
    charteringEvent.temporallyLocatedAt = may1_1822
    charteringEvent.charteredBy.append(edouardBovet)
    charteringEvent.charteredIn.append(london)

    # Company
    bovetFleurierSA = LuxuryWatchCompany("BovetFleurierSA")
    bovetFleurierSA.label = "Bovet Fleurier SA"
    charteringEvent.charteringOf.append(bovetFleurierSA)
    bovetFleurierSA.hasOriginCountry.append(switzerland)
    bovetFleurierSA.hasOwner.append(pascalRaffy)
    bovetFleurierSA.historicalProductMarket.append(chineseMarket)
    bovetFleurierSA.historicalProductionPeriod.append(the19thCentury)
    bovetFleurierSA.minimumWatchPriceUSD = 18000.0
    bovetFleurierSA.maximumWatchPriceUSD = 2500000.0
    bovetFleurierSA.styleReference.append("history")
    bovetFleurierSA.employmentTradition.append("employing women artisans")

    # What the company currently manufactures (LuxuryArtisticWatch)
    bovetFleurierSA.is_a.append(manufactures.some(LuxuryArtisticWatch))
    # Historical production of pocket watches for the Chinese market
    bovetFleurierSA.is_a.append(manufactures.some(PocketWatch))

    # Dial model
    fleurierMiniaturePainting = WatchDialModel("FleurierMiniaturePainting")
    fleurierMiniaturePainting.label = "Fleurier Miniature Painting"
    bovetFleurierSA.hasDialModel.append(fleurierMiniaturePainting)

    # Decorative technique
    engraving = DecorativeTechnique("Engraving")
    engraving.label = "engraving"
    bovetFleurierSA.usesDecorativeTechnique.append(engraving)

    # Watch complications
    sevenDayTourbillon = WatchComplication("SevenDayTourbillon")
    sevenDayTourbillon.label = "seven-day tourbillon"
    bovetFleurierSA.hasComplication.append(sevenDayTourbillon)

    secondHand = WatchComplication("SecondHand")
    secondHand.label = "second hand"
    bovetFleurierSA.hasComplication.append(secondHand)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
