"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

1. What is the original title of a game in non-English territories?
2. What genre does a specific video game belong to?
3. Who developed a specific video game?
4. Who published a specific video game?
5. For which platform was a specific video game released?
6. Is a specific video game a sequel to another game?
7. What is the release date of a specific video game in a particular region?
8. How many levels does a specific video game feature?
9. Can players download and upload custom levels in a specific video game?
10. When did the development of a specific video game begin?
11. When was a specific video game formally announced?
12. Who designed a specific video game?
13. What is the occupation of the person who designed a specific video game?
14. What new mechanics does a sequel introduce compared to its predecessor?
15. What mode of play was least favored by the developers of a specific video game?
16. As part of what deal was a specific video game created?
17. Does a specific video game count as one of the original properties in a deal?
18. When were the online servers for a specific video game shut down?
19. What features became unavailable after the online servers were shut down?
20. Who was the predecessor of a specific sequel game?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    AsymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

from og_sandbox_with_core.core.entities import (
    NonAgentiveSocialObject,
    NonAgentivePhysicalObject,
    AgentivePhysicalObject,
    Society,
    Accomplishment,
    Achievement,
    Process,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── Entity classes ────────────────────────────────────────────────────────

    class VideoGame(NonAgentiveSocialObject):
        """A software title released for a video game platform."""

    class PuzzleVideoGame(VideoGame):
        """A video game belonging to the puzzle genre."""

    class VideoGameConsole(NonAgentivePhysicalObject):
        """A physical hardware platform designed to play video games."""

    class Organization(Society):
        """A company or studio involved in game development or publishing."""

    class Person(AgentivePhysicalObject):
        """A human individual."""

    class FilmDirector(Person):
        """A person who directs films."""

    class GameGenre(NonAgentiveSocialObject):
        """A category classifying video games by style of gameplay."""

    class GameMode(NonAgentiveSocialObject):
        """A specific mode of play available within a video game."""

    class Deal(NonAgentiveSocialObject):
        """A commercial agreement between two or more parties."""

    class GeographicRegion(NonAgentiveSocialObject):
        """A geopolitical or geographic territory."""

    class ReleaseEvent(Accomplishment):
        """The event of a video game being made commercially available in a region."""

    class GameDevelopment(Process):
        """The process of creating a video game."""

    class GameAnnouncement(Achievement):
        """The instantaneous event of a video game being formally announced."""

    class ServerShutdownEvent(Achievement):
        """The instantaneous event of online servers being shut down."""

    # ── Object properties ─────────────────────────────────────────────────────

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Organization]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Organization]

    class releasedFor(ObjectProperty):
        domain = [VideoGame]
        range  = [VideoGameConsole]

    class sequelOf(ObjectProperty, AsymmetricProperty):
        domain = [VideoGame]
        range  = [VideoGame]

    class hasGenre(ObjectProperty):
        domain = [VideoGame]
        range  = [GameGenre]

    class releaseOf(ObjectProperty):
        domain = [ReleaseEvent]
        range  = [VideoGame]

    class releasedIn(ObjectProperty):
        domain = [ReleaseEvent]
        range  = [GeographicRegion]

    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Person]

    class hasMode(ObjectProperty):
        domain = [VideoGame]
        range  = [GameMode]

    class leastFavoriteMode(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [GameMode]

    class createdUnderDeal(ObjectProperty):
        domain = [VideoGame]
        range  = [Deal]

    class dealParty(ObjectProperty):
        domain = [Deal]
        range  = [Or([Organization, Person])]

    class announcementOf(ObjectProperty):
        domain = [GameAnnouncement]
        range  = [VideoGame]

    class developmentOf(ObjectProperty):
        domain = [GameDevelopment]
        range  = [VideoGame]

    class serverShutdownOf(ObjectProperty):
        domain = [ServerShutdownEvent]
        range  = [VideoGame]

    # ── Data properties ───────────────────────────────────────────────────────

    class levelCount(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [int]

    class alternativeTitle(DataProperty):
        domain = [VideoGame]
        range  = [str]

    class supportsLevelDownload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [bool]

    class supportsLevelUpload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [bool]

    class countsAsOriginalProperty(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [bool]

    class hasNewMechanic(DataProperty):
        domain = [VideoGame]
        range  = [str]

    # ── Named individuals ─────────────────────────────────────────────────────

    # Time intervals for named dates
    na_release_date = TimeInterval("NorthAmericaReleaseDate")
    na_release_date.label = "19 May 2009"

    eu_release_date = TimeInterval("EuropeReleaseDate")
    eu_release_date.label = "29 May 2009"

    announcement_date = TimeInterval("AnnouncementDate")
    announcement_date.label = "28 January 2009"

    server_shutdown_date = TimeInterval("ServerShutdownDate")
    server_shutdown_date.label = "April 2012"

    # Organizations
    ea_los_angeles = Organization("EALosAngeles")
    ea_los_angeles.label = "EA Los Angeles"

    amblin_entertainment = Organization("AmblinEntertainment")
    amblin_entertainment.label = "Amblin Entertainment"

    electronic_arts = Organization("ElectronicArts")
    electronic_arts.label = "Electronic Arts"

    # Person
    steven_spielberg = FilmDirector("StevenSpielberg")
    steven_spielberg.label = "Steven Spielberg"

    # VideoGameConsole
    wii = VideoGameConsole("WiiConsole")
    wii.label = "Wii"

    # Geographic regions
    north_america = GeographicRegion("NorthAmerica")
    north_america.label = "North America"

    europe = GeographicRegion("Europe")
    europe.label = "Europe"

    # Game genre
    physics_puzzle_genre = GameGenre("PhysicsBasedPuzzleGenre")
    physics_puzzle_genre.label = "physics-based puzzle"

    # Game mode
    shooting_mode = GameMode("ShootingMode")
    shooting_mode.label = "shooting mode"

    # Deal
    ea_spielberg_deal = Deal("EAStevenSpielbergDeal")
    ea_spielberg_deal.label = "deal between Electronic Arts and Steven Spielberg"
    ea_spielberg_deal.dealParty.append(electronic_arts)
    ea_spielberg_deal.dealParty.append(steven_spielberg)

    # Video games
    boom_blox = VideoGame("BoomBlox")
    boom_blox.label = "Boom Blox"

    boom_blox_bash_party = PuzzleVideoGame("BoomBloxBashParty")
    boom_blox_bash_party.label = "Boom Blox Bash Party"
    boom_blox_bash_party.alternativeTitle.append("Boom Blox Smash Party")
    boom_blox_bash_party.developedBy.append(ea_los_angeles)
    boom_blox_bash_party.developedBy.append(amblin_entertainment)
    boom_blox_bash_party.publishedBy.append(electronic_arts)
    boom_blox_bash_party.releasedFor.append(wii)
    boom_blox_bash_party.sequelOf.append(boom_blox)
    boom_blox_bash_party.hasGenre.append(physics_puzzle_genre)
    boom_blox_bash_party.designedBy.append(steven_spielberg)
    boom_blox_bash_party.levelCount = 400
    boom_blox_bash_party.hasMode.append(shooting_mode)
    boom_blox_bash_party.leastFavoriteMode = shooting_mode
    boom_blox_bash_party.createdUnderDeal.append(ea_spielberg_deal)
    boom_blox_bash_party.countsAsOriginalProperty = False
    boom_blox_bash_party.supportsLevelDownload = True
    boom_blox_bash_party.supportsLevelUpload = True
    boom_blox_bash_party.hasNewMechanic.append("new mechanics")

    # Release events
    na_release = ReleaseEvent("BoomBloxBashPartyNorthAmericaRelease")
    na_release.label = "Boom Blox Bash Party North America Release"
    na_release.releaseOf.append(boom_blox_bash_party)
    na_release.releasedIn.append(north_america)
    na_release.temporallyLocatedAt = na_release_date

    eu_release = ReleaseEvent("BoomBloxBashPartyEuropeRelease")
    eu_release.label = "Boom Blox Bash Party Europe Release"
    eu_release.releaseOf.append(boom_blox_bash_party)
    eu_release.releasedIn.append(europe)
    eu_release.temporallyLocatedAt = eu_release_date

    # Announcement
    announcement = GameAnnouncement("BoomBloxBashPartyAnnouncement")
    announcement.label = "Boom Blox Bash Party Announcement"
    announcement.announcementOf.append(boom_blox_bash_party)
    announcement.temporallyLocatedAt = announcement_date

    # Development process
    development = GameDevelopment("BoomBloxBashPartyDevelopment")
    development.label = "Boom Blox Bash Party Development"
    development.developmentOf.append(boom_blox_bash_party)

    # Server shutdown event
    server_shutdown = ServerShutdownEvent("BoomBloxBashPartyServerShutdown")
    server_shutdown.label = "Boom Blox Bash Party Server Shutdown"
    server_shutdown.serverShutdownOf.append(boom_blox_bash_party)
    server_shutdown.temporallyLocatedAt = server_shutdown_date


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
