"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

1. What type of television series is The Celebrity Apprentice?
2. Who hosted The Celebrity Apprentice and during which periods?
3. What is the opening theme song of The Celebrity Apprentice?
4. Who performed the opening theme song of The Celebrity Apprentice?
5. How does The Celebrity Apprentice differ from The Apprentice in terms of contestants?
6. What do the celebrities compete to win on The Celebrity Apprentice?
7. What fields or backgrounds do the competing celebrities come from?
8. Which seasons of The Apprentice series correspond to The Celebrity Apprentice?
9. Which seasons belong to The Celebrity Apprentice?
10. Which network aired The Celebrity Apprentice?
11. Who announced the cancellation of The Celebrity Apprentice and when?
12. What is the relationship between The Celebrity Apprentice and The Apprentice?
13. What role did Donald Trump hold before becoming U.S. President?
14. What role did Arnold Schwarzenegger hold before hosting The Celebrity Apprentice?
15. When did Arnold Schwarzenegger begin hosting The Celebrity Apprentice?
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
    NonAgentiveSocialObject, Society, TimeInterval,
    AgentivePhysicalObject, State, Achievement,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── Entity classes ──────────────────────────────────────────────────────

    class TelevisionSeries(NonAgentiveSocialObject):
        """A TV show broadcast to audiences."""

    class RealityCompetitionSeries(TelevisionSeries):
        """A television series in the reality-competition genre."""

    class Person(AgentivePhysicalObject):
        """A human being."""

    class RealEstateDeveloper(Person):
        """A person whose profession is real-estate development."""

    class Actor(Person):
        """A person who acts in film or television."""

    class USPresident(Person):
        """A person serving as President of the United States."""

    class StateGovernor(Person):
        """A person serving as the governor of a U.S. state."""

    class BroadcastingExecutive(Person):
        """A senior executive at a broadcasting organisation."""

    class Celebrity(Person):
        """A widely-known public figure."""

    class BroadcastNetwork(Society):
        """A television broadcasting network."""

    class Song(NonAgentiveSocialObject):
        """A musical composition."""

    class ThemeSong(Song):
        """An opening or identifying song for a TV series."""

    class MusicGroup(Society):
        """A musical group or band."""

    class CharitableOrganization(Society):
        """A non-profit organisation that benefits from charitable donations."""

    class MediaField(NonAgentiveSocialObject):
        """A sector of the media industry (e.g. sitcoms, sports)."""

    class HostingEngagement(State):
        """The state of a person hosting a television series over a period."""

    class CancellationAnnouncement(Achievement):
        """An instantaneous announcement that a TV series has been cancelled."""

    class SeasonRange(NonAgentiveSocialObject):
        """A contiguous block of seasons belonging to a TV series."""

    # ── Properties ──────────────────────────────────────────────────────────

    class hostedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [Person]

    class engagedHost(ObjectProperty):
        domain = [HostingEngagement]
        range  = [Person]

    class engagedShow(ObjectProperty):
        domain = [HostingEngagement]
        range  = [TelevisionSeries]

    class isVariationOf(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [TelevisionSeries]

    class hasThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [ThemeSong]

    class performedBy(ObjectProperty):
        domain = [Song]
        range  = [MusicGroup]

    class airedOn(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [BroadcastNetwork]

    class announcedBy(ObjectProperty):
        domain = [CancellationAnnouncement]
        range  = [BroadcastingExecutive]

    class concernsShow(ObjectProperty):
        domain = [CancellationAnnouncement]
        range  = [TelevisionSeries]

    class hasMediaField(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [MediaField]

    class hasSeasonRange(ObjectProperty):
        domain = [TelevisionSeries]
        range  = [SeasonRange]

    class startSeason(DataProperty, FunctionalProperty):
        domain = [SeasonRange]
        range  = [int]

    class endSeason(DataProperty, FunctionalProperty):
        domain = [SeasonRange]
        range  = [int]

    # ── Named individuals ───────────────────────────────────────────────────

    # Television shows
    TheCelebrityApprenticeInst = RealityCompetitionSeries("TheCelebrityApprentice")
    TheCelebrityApprenticeInst.label = "The Celebrity Apprentice"

    TheApprenticeInst = TelevisionSeries("TheApprentice")
    TheApprenticeInst.label = "The Apprentice"

    # People
    DonaldTrump = RealEstateDeveloper("DonaldTrump")
    DonaldTrump.label = "Donald Trump"
    DonaldTrump.is_a.append(USPresident)

    ArnoldSchwarzenegger = Actor("ArnoldSchwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"
    ArnoldSchwarzenegger.is_a.append(StateGovernor)

    BobGreenblatt = BroadcastingExecutive("BobGreenblatt")
    BobGreenblatt.label = "Bob Greenblatt"

    # Broadcast network
    NBCNetwork = BroadcastNetwork("NBC")
    NBCNetwork.label = "NBC"

    # Theme song and performer
    ForTheLoveOfMoney = ThemeSong("ForTheLoveOfMoney")
    ForTheLoveOfMoney.label = "For the Love of Money"

    TheOJays = MusicGroup("TheOJays")
    TheOJays.label = "The O'Jays"

    ForTheLoveOfMoney.performedBy.append(TheOJays)

    # Time intervals
    Period2008to2015 = TimeInterval("Period2008to2015")
    Period2008to2015.label = "2008 to 2015"

    PeriodFromJanuary2017 = TimeInterval("PeriodFromJanuary2017")
    PeriodFromJanuary2017.label = "January 2017"

    August3_2017 = TimeInterval("August3_2017")
    August3_2017.label = "August 3, 2017"

    # Hosting engagements
    TrumpHostingEngagement = HostingEngagement("TrumpHostingEngagement")
    TrumpHostingEngagement.label = "Donald Trump hosting The Celebrity Apprentice"
    TrumpHostingEngagement.engagedHost.append(DonaldTrump)
    TrumpHostingEngagement.engagedShow.append(TheCelebrityApprenticeInst)
    TrumpHostingEngagement.temporallyLocatedAt = Period2008to2015

    SchwarzeneggerHostingEngagement = HostingEngagement("SchwarzeneggerHostingEngagement")
    SchwarzeneggerHostingEngagement.label = "Arnold Schwarzenegger hosting The Celebrity Apprentice"
    SchwarzeneggerHostingEngagement.engagedHost.append(ArnoldSchwarzenegger)
    SchwarzeneggerHostingEngagement.engagedShow.append(TheCelebrityApprenticeInst)
    SchwarzeneggerHostingEngagement.temporallyLocatedAt = PeriodFromJanuary2017

    # Cancellation announcement
    CancellationAnnouncementInst = CancellationAnnouncement("CancellationAnnouncementInst")
    CancellationAnnouncementInst.label = "NBC cancellation announcement"
    CancellationAnnouncementInst.announcedBy.append(BobGreenblatt)
    CancellationAnnouncementInst.concernsShow.append(TheCelebrityApprenticeInst)
    CancellationAnnouncementInst.temporallyLocatedAt = August3_2017

    # Show-level properties
    TheCelebrityApprenticeInst.hostedBy.append(DonaldTrump)
    TheCelebrityApprenticeInst.hostedBy.append(ArnoldSchwarzenegger)
    TheCelebrityApprenticeInst.isVariationOf.append(TheApprenticeInst)
    TheCelebrityApprenticeInst.hasThemeSong = ForTheLoveOfMoney
    TheCelebrityApprenticeInst.airedOn.append(NBCNetwork)

    TheApprenticeInst.hasThemeSong = ForTheLoveOfMoney
    TheApprenticeInst.airedOn.append(NBCNetwork)

    # Media fields the competing celebrities come from
    SitcomsField = MediaField("Sitcoms")
    SitcomsField.label = "sitcoms"

    ProfessionalSportsField = MediaField("ProfessionalSports")
    ProfessionalSportsField.label = "professional sports"

    MusicIndustryField = MediaField("MusicIndustry")
    MusicIndustryField.label = "music industry"

    RealityTelevisionField = MediaField("RealityTelevision")
    RealityTelevisionField.label = "reality television"

    RadioField = MediaField("Radio")
    RadioField.label = "radio"

    TheCelebrityApprenticeInst.hasMediaField.append(SitcomsField)
    TheCelebrityApprenticeInst.hasMediaField.append(ProfessionalSportsField)
    TheCelebrityApprenticeInst.hasMediaField.append(MusicIndustryField)
    TheCelebrityApprenticeInst.hasMediaField.append(RealityTelevisionField)
    TheCelebrityApprenticeInst.hasMediaField.append(RadioField)

    # Season ranges — The Apprentice: seasons 1–6 and season 10
    ApprenticeSeasons1to6 = SeasonRange("ApprenticeSeasons1to6")
    ApprenticeSeasons1to6.label = "seasons one to six"
    ApprenticeSeasons1to6.startSeason = 1
    ApprenticeSeasons1to6.endSeason = 6

    ApprenticeSeasonTen = SeasonRange("ApprenticeSeasonTen")
    ApprenticeSeasonTen.label = "season ten"
    ApprenticeSeasonTen.startSeason = 10
    ApprenticeSeasonTen.endSeason = 10

    # Season ranges — The Celebrity Apprentice: seasons 7–9 and 11–15
    CelebAppSeasons7to9 = SeasonRange("CelebAppSeasons7to9")
    CelebAppSeasons7to9.label = "seasons seven to nine"
    CelebAppSeasons7to9.startSeason = 7
    CelebAppSeasons7to9.endSeason = 9

    CelebAppSeasons11to15 = SeasonRange("CelebAppSeasons11to15")
    CelebAppSeasons11to15.label = "seasons eleven to fifteen"
    CelebAppSeasons11to15.startSeason = 11
    CelebAppSeasons11to15.endSeason = 15

    TheApprenticeInst.hasSeasonRange.append(ApprenticeSeasons1to6)
    TheApprenticeInst.hasSeasonRange.append(ApprenticeSeasonTen)
    TheCelebrityApprenticeInst.hasSeasonRange.append(CelebAppSeasons7to9)
    TheCelebrityApprenticeInst.hasSeasonRange.append(CelebAppSeasons11to15)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
