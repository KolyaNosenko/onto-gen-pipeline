"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

1. What type of television series is The Celebrity Apprentice?
2. Who hosted The Celebrity Apprentice and during what period?
3. What is the opening theme song of The Celebrity Apprentice?
4. Who performed the opening theme song of The Celebrity Apprentice?
5. How does The Celebrity Apprentice differ from its precursor, The Apprentice?
6. What do the competing celebrities aim to win on The Celebrity Apprentice?
7. What fields or backgrounds do the competing celebrities come from?
8. Which seasons are associated with The Celebrity Apprentice?
9. Which seasons are associated with The Apprentice (precursor)?
10. When was The Celebrity Apprentice effectively canceled?
11. Who announced the cancellation of The Celebrity Apprentice?
12. What role did Bob Greenblatt hold at the time of the cancellation announcement?
13. What is the relationship between The Celebrity Apprentice and The Apprentice in terms of seasons?
14. Who hosted The Celebrity Apprentice starting from January 2017?
15. What was Donald Trump's profession before becoming U.S. President?
16. What was Arnold Schwarzenegger's role before hosting The Celebrity Apprentice?
17. On which network did The Celebrity Apprentice air?
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
    # ── ENTITY CLASSES ────────────────────────────────────────────────────────

    # Television
    class TelevisionSeries(Thing): pass
    class RealityCompetitionSeries(TelevisionSeries): pass

    # People and roles
    class Person(Thing): pass
    class Host(Person): pass
    class Celebrity(Person): pass
    class Contestant(Person): pass
    class CelebrityContestant(Contestant, Celebrity): pass
    class UnknownContestant(Contestant): pass
    class RealEstateDeveloper(Person): pass
    class Actor(Person): pass
    class PoliticalFigure(Person): pass
    class Governor(PoliticalFigure): pass
    class President(PoliticalFigure): pass
    class NetworkExecutive(Person): pass

    # Media and entertainment
    class Song(Thing): pass
    class MusicGroup(Thing): pass
    class BroadcastNetwork(Thing): pass
    class MediaField(Thing): pass

    # Other
    class CharitableOrganization(Thing): pass
    class State(Thing): pass
    class Season(Thing): pass

    # ── OBJECT PROPERTIES ─────────────────────────────────────────────────────

    class isVariationOf(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [TelevisionSeries]

    class isPrecursorOf(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [TelevisionSeries]

    class linkedToSeries(ObjectProperty, SymmetricProperty):
        domain = [TelevisionSeries]
        range  = [TelevisionSeries]

    class hostedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [Host]

    class hasOpeningThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [Song]

    class performedBy(ObjectProperty):
        domain = [Song]
        range  = [MusicGroup]

    class airedOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [BroadcastNetwork]

    class hasSeason(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [Season]

    class cancellationAnnouncedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [Person]

    class hasContestant(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [Contestant]

    class celebrityFieldsInclude(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [MediaField]

    class governorOf(ObjectProperty, FunctionalProperty):
        domain = [Governor]
        range  = [State]

    class hasCharityBeneficiary(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [CharitableOrganization]

    # ── DATA PROPERTIES ───────────────────────────────────────────────────────

    class hostingStartYear(DataProperty, FunctionalProperty):
        domain = [Host]
        range  = [int]

    class hostingEndYear(DataProperty, FunctionalProperty):
        domain = [Host]
        range  = [int]

    class hostingStartMonth(DataProperty, FunctionalProperty):
        domain = [Host]
        range  = [str]

    class cancellationAnnouncementDate(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [str]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Season]
        range  = [int]

    class hasJobTitle(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class contestantType(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [str]

    class country(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [str]

    # ── INDIVIDUALS ───────────────────────────────────────────────────────────

    # Television series
    TheCelebrityApprentice = RealityCompetitionSeries("TheCelebrityApprentice")
    TheCelebrityApprentice.label = "The Celebrity Apprentice"

    TheApprentice = TelevisionSeries("TheApprentice")
    TheApprentice.label = "The Apprentice"

    # People
    DonaldTrump = RealEstateDeveloper("DonaldTrump")
    DonaldTrump.label = "Donald Trump"
    DonaldTrump.is_a.append(Host)
    DonaldTrump.is_a.append(President)

    ArnoldSchwarzenegger = Actor("ArnoldSchwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"
    ArnoldSchwarzenegger.is_a.append(Host)
    ArnoldSchwarzenegger.is_a.append(Governor)

    BobGreenblatt = NetworkExecutive("BobGreenblatt")
    BobGreenblatt.label = "Bob Greenblatt"

    # Song and performer
    ForTheLoveOfMoney = Song("ForTheLoveOfMoney")
    ForTheLoveOfMoney.label = "For the Love of Money"

    TheOJays = MusicGroup("TheOJays")
    TheOJays.label = "The O'Jays"

    # Broadcast network
    NBCNetwork = BroadcastNetwork("NBCNetwork")
    NBCNetwork.label = "NBC"

    # State
    California = State("California")
    California.label = "California"

    # Seasons for The Apprentice (1–6 and 10)
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

    # Seasons for The Celebrity Apprentice (7–9 and 11–15)
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

    # Media fields
    Sitcoms = MediaField("Sitcoms")
    Sitcoms.label = "sitcoms"

    ProfessionalSports = MediaField("ProfessionalSports")
    ProfessionalSports.label = "professional sports"

    MusicIndustry = MediaField("MusicIndustry")
    MusicIndustry.label = "music industry"

    RealityTelevision = MediaField("RealityTelevision")
    RealityTelevision.label = "reality television"

    Radio = MediaField("Radio")
    Radio.label = "radio"

    # ── PROPERTY ASSERTIONS ───────────────────────────────────────────────────

    # Series relationships
    TheCelebrityApprentice.isVariationOf = [TheApprentice]
    TheApprentice.isPrecursorOf = [TheCelebrityApprentice]
    TheCelebrityApprentice.linkedToSeries = [TheApprentice]
    TheApprentice.linkedToSeries = [TheCelebrityApprentice]

    # Hosting
    TheCelebrityApprentice.hostedBy = [DonaldTrump, ArnoldSchwarzenegger]
    DonaldTrump.hostingStartYear = 2008
    DonaldTrump.hostingEndYear = 2015
    ArnoldSchwarzenegger.hostingStartYear = 2017
    ArnoldSchwarzenegger.hostingStartMonth = "January"

    # Theme song (both shows share it)
    TheCelebrityApprentice.hasOpeningThemeSong = ForTheLoveOfMoney
    TheApprentice.hasOpeningThemeSong = ForTheLoveOfMoney
    ForTheLoveOfMoney.performedBy = [TheOJays]

    # Network
    TheCelebrityApprentice.airedOn = NBCNetwork

    # Cancellation
    TheCelebrityApprentice.cancellationAnnouncementDate = "August 3, 2017"
    TheCelebrityApprentice.cancellationAnnouncedBy = [BobGreenblatt]
    BobGreenblatt.hasJobTitle = "NBC Entertainment Chairman"

    # Seasons
    TheApprentice.hasSeason = [Season1, Season2, Season3, Season4, Season5, Season6, Season10]
    TheCelebrityApprentice.hasSeason = [Season7, Season8, Season9, Season11, Season12, Season13, Season14, Season15]

    # Contestant types
    TheCelebrityApprentice.contestantType = "celebrities"
    TheApprentice.contestantType = "unknowns"

    # Celebrity fields
    TheCelebrityApprentice.celebrityFieldsInclude = [Sitcoms, ProfessionalSports, MusicIndustry, RealityTelevision, Radio]

    # Geography
    ArnoldSchwarzenegger.governorOf = California

    # Country
    TheCelebrityApprentice.country = "American"
    TheApprentice.country = "American"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
