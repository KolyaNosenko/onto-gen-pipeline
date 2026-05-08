"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

1. What is The Celebrity Apprentice and what type of television show is it?
2. Who hosted The Celebrity Apprentice and during which time periods?
3. When was The Celebrity Apprentice canceled?
4. What is the opening theme song of The Celebrity Apprentice and who performs it?
5. How does The Celebrity Apprentice differ from The Apprentice in terms of participants?
6. What are the objectives or goals for celebrities competing on The Celebrity Apprentice?
7. What types of media backgrounds do the celebrities on The Celebrity Apprentice come from?
8. How are the seasons of The Celebrity Apprentice related to the seasons of The Apprentice?
9. Which seasons constitute The Celebrity Apprentice series?
10. Which seasons constitute The Apprentice series?
11. Is The Celebrity Apprentice a variation of The Apprentice?
12. What is the relationship between Donald Trump and The Celebrity Apprentice?
13. What is the relationship between Arnold Schwarzenegger and The Celebrity Apprentice?
14. When did Arnold Schwarzenegger begin hosting The Celebrity Apprentice?
15. Why did celebrities participate in The Celebrity Apprentice competitions?
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
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject
from og_sandbox_with_core.core.entities import (
    Accomplishment, Event, SocialObject, Society, AgentivePhysicalObject
)

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # TODO: declare your domain entity classes here.
    # Each MUST be a subclass of a class from `og_sandbox_with_core.core.entities`
    # (or of another domain class that ultimately roots in one). Direct
    # subclassing of `Thing` is forbidden — pick the most specific core
    # ancestor that fits.

    class TelevisionSeries(Accomplishment):
        """A television series: a complex event composed of multiple episodes/seasons."""
        pass

    class RealityCompetitionSeries(TelevisionSeries):
        """A reality competition television series."""
        pass

    class Season(Event):
        """A season of a television series."""
        pass

    class Song(SocialObject):
        """A musical composition that is a social/creative work."""
        pass

    class MusicalBand(Society):
        """A collective of musicians performing together."""
        pass

    class Person(AgentivePhysicalObject):
        """An individual human being with agency."""
        pass

    class Organization(Society):
        """A formal organization or corporation."""
        pass

    class HostingPeriod(Event):
        """An event representing a period during which someone hosted a show."""
        pass

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. If a core property matches the text's semantics, subclass it;
    # otherwise declare a fresh ObjectProperty / DataProperty with explicit
    # domain / range.

    class isVariationOf(ObjectProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class performedBy(ObjectProperty):
        domain = [Song]
        range = [MusicalBand, Person]

    class isOpeningThemeOf(ObjectProperty):
        domain = [Song]
        range = [TelevisionSeries]

    class containsSeason(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Season]

    class hasHost(ObjectProperty):
        domain = [HostingPeriod]
        range = [Person]

    class hostedShow(ObjectProperty):
        domain = [HostingPeriod]
        range = [TelevisionSeries]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Season]
        range = [int]

    class canceledOn(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]

    class hostingStartYear(DataProperty, FunctionalProperty):
        domain = [HostingPeriod]
        range = [int]

    class hostingEndYear(DataProperty, FunctionalProperty):
        domain = [HostingPeriod]
        range = [int]

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    # Television series instances
    TheCelebrityApprentice = RealityCompetitionSeries("TheCelebrityApprentice")
    TheCelebrityApprentice.label = "The Celebrity Apprentice"

    TheApprentice = TelevisionSeries("TheApprentice")
    TheApprentice.label = "The Apprentice"

    # People instances
    DonaldTrump = Person("DonaldTrump")
    DonaldTrump.label = "Donald Trump"

    ArnoldSchwarzenegger = Person("ArnoldSchwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"

    BobGreenblatt = Person("BobGreenblatt")
    BobGreenblatt.label = "Bob Greenblatt"

    # Organization instance
    NBCEntertainment = Organization("NBCEntertainment")
    NBCEntertainment.label = "NBC Entertainment"

    # Song instance
    ForTheLoveOfMoney = Song("ForTheLoveOfMoney")
    ForTheLoveOfMoney.label = "For the Love of Money"

    # Band instance
    TheOJays = MusicalBand("TheOJays")
    TheOJays.label = "The O'Jays"

    # Hosting periods
    TrumpHosting = HostingPeriod("TrumpHosting")
    TrumpHosting.hasHost = [DonaldTrump]
    TrumpHosting.hostedShow = [TheCelebrityApprentice]
    TrumpHosting.hostingStartYear = 2008
    TrumpHosting.hostingEndYear = 2015

    SchwarzeneggerHosting = HostingPeriod("SchwarzeneggerHosting")
    SchwarzeneggerHosting.hasHost = [ArnoldSchwarzenegger]
    SchwarzeneggerHosting.hostedShow = [TheCelebrityApprentice]
    SchwarzeneggerHosting.hostingStartYear = 2017

    # Season instances for The Apprentice (seasons 1-6 and 10)
    Season1 = Season("Season1")
    Season1.label = "Season 1"
    Season1.seasonNumber = 1

    Season2 = Season("Season2")
    Season2.label = "Season 2"
    Season2.seasonNumber = 2

    Season3 = Season("Season3")
    Season3.label = "Season 3"
    Season3.seasonNumber = 3

    Season4 = Season("Season4")
    Season4.label = "Season 4"
    Season4.seasonNumber = 4

    Season5 = Season("Season5")
    Season5.label = "Season 5"
    Season5.seasonNumber = 5

    Season6 = Season("Season6")
    Season6.label = "Season 6"
    Season6.seasonNumber = 6

    Season10 = Season("Season10")
    Season10.label = "Season 10"
    Season10.seasonNumber = 10

    # Season instances for The Celebrity Apprentice (seasons 7-9 and 11-15)
    Season7 = Season("Season7")
    Season7.label = "Season 7"
    Season7.seasonNumber = 7

    Season8 = Season("Season8")
    Season8.label = "Season 8"
    Season8.seasonNumber = 8

    Season9 = Season("Season9")
    Season9.label = "Season 9"
    Season9.seasonNumber = 9

    Season11 = Season("Season11")
    Season11.label = "Season 11"
    Season11.seasonNumber = 11

    Season12 = Season("Season12")
    Season12.label = "Season 12"
    Season12.seasonNumber = 12

    Season13 = Season("Season13")
    Season13.label = "Season 13"
    Season13.seasonNumber = 13

    Season14 = Season("Season14")
    Season14.label = "Season 14"
    Season14.seasonNumber = 14

    Season15 = Season("Season15")
    Season15.label = "Season 15"
    Season15.seasonNumber = 15

    # Relationships between shows
    TheCelebrityApprentice.isVariationOf = [TheApprentice]

    # Opening theme information
    ForTheLoveOfMoney.performedBy = [TheOJays]
    ForTheLoveOfMoney.isOpeningThemeOf = [TheCelebrityApprentice]

    # Cancellation information
    TheCelebrityApprentice.canceledOn = "August 3, 2017"

    # Associate seasons with shows
    TheApprentice.containsSeason = [Season1, Season2, Season3, Season4, Season5, Season6, Season10]
    TheCelebrityApprentice.containsSeason = [Season7, Season8, Season9, Season11, Season12, Season13, Season14, Season15]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
