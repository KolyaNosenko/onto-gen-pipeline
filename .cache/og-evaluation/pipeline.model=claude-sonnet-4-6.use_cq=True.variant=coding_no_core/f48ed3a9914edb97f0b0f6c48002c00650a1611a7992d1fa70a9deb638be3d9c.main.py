"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

1. What is the original title of a game in non-English territories?
2. What genre does a specific video game belong to?
3. Who developed a specific video game?
4. Who published a specific video game?
5. For which platform was a specific video game released?
6. Is a specific game a sequel to another game?
7. What is the release date of a specific video game in a particular region?
8. How many levels does a specific video game feature?
9. Can players download or upload custom levels in a specific video game?
10. When did the development of a specific game begin?
11. When was a specific game formally announced?
12. Who designed a specific video game?
13. What new mechanics does a sequel introduce compared to its predecessor?
14. What deal or agreement led to the creation of a specific game?
15. When were the online servers for a specific game shut down?
16. What features became unavailable after the online servers were shut down?
17. Which gameplay modes are featured in a specific video game?
18. Which gameplay mode was considered the least favorite by the developers?
19. Does a specific game count as one of the original properties in a deal?
20. Who is the film director associated with the design of a specific video game?
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
    # ------------------------------------------------------------------ #
    # Classes                                                              #
    # ------------------------------------------------------------------ #
    class VideoGame(Thing): pass
    class PhysicsBasedPuzzleGame(VideoGame): pass

    class Company(Thing): pass
    class Person(Thing): pass
    class FilmDirector(Person): pass

    class Platform(Thing): pass
    class Region(Thing): pass

    class GameMode(Thing): pass
    class GameMechanic(Thing): pass
    class OnlineFeature(Thing): pass

    class Deal(Thing): pass
    class ReleaseEvent(Thing): pass

    # ------------------------------------------------------------------ #
    # Object Properties                                                    #
    # ------------------------------------------------------------------ #
    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Company]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Company]

    class releasedForPlatform(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [Platform]

    class isSequelTo(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [VideoGame]

    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [Person]

    class hasReleaseEvent(ObjectProperty):
        domain = [VideoGame]
        range  = [ReleaseEvent]

    class inRegion(ObjectProperty, FunctionalProperty):
        domain = [ReleaseEvent]
        range  = [Region]

    class hasGameMode(ObjectProperty):
        domain = [VideoGame]
        range  = [GameMode]

    class hasNewMechanic(ObjectProperty):
        domain = [VideoGame]
        range  = [GameMechanic]

    class leastFavoriteMode(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [GameMode]

    class hasOnlineFeature(ObjectProperty):
        domain = [VideoGame]
        range  = [OnlineFeature]

    class createdUnderDeal(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [Deal]

    class hasDealParticipant(ObjectProperty):
        domain = [Deal]
        range  = [Company, Person]

    class developmentBeganAfterCompletionOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [VideoGame]

    # ------------------------------------------------------------------ #
    # Data Properties                                                      #
    # ------------------------------------------------------------------ #
    class alternativeTitle(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [ReleaseEvent]
        range  = [str]

    class levelCount(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class announcedOn(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class onlineServersShutDownDate(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class countsAsOriginalProperty(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [bool]

    class targetOriginalPropertyCount(DataProperty, FunctionalProperty):
        domain = [Deal]
        range  = [int]

    # ------------------------------------------------------------------ #
    # Individuals                                                          #
    # ------------------------------------------------------------------ #

    # Games
    boomBloxBashParty = PhysicsBasedPuzzleGame("BoomBloxBashParty")
    boomBloxBashParty.label = "Boom Blox Bash Party"

    boomBlox = VideoGame("BoomBlox")
    boomBlox.label = "Boom Blox"

    # Companies
    eaLosAngeles = Company("EALosAngeles")
    eaLosAngeles.label = "EA Los Angeles"

    amblinEntertainment = Company("AmblinEntertainment")
    amblinEntertainment.label = "Amblin Entertainment"

    electronicArts = Company("ElectronicArts")
    electronicArts.label = "Electronic Arts"

    # Platform
    wii = Platform("Wii")
    wii.label = "Wii"

    # Regions
    northAmerica = Region("NorthAmerica")
    northAmerica.label = "North America"

    europe = Region("Europe")
    europe.label = "Europe"

    # People
    stevenSpielberg = FilmDirector("StevenSpielberg")
    stevenSpielberg.label = "Steven Spielberg"

    # Game modes
    shootingMode = GameMode("ShootingMode")
    shootingMode.label = "shooting mode"

    # Online features
    levelDownload = OnlineFeature("LevelDownload")
    levelDownload.label = "level download"

    levelUpload = OnlineFeature("LevelUpload")
    levelUpload.label = "level upload"

    # Release events
    naRelease = ReleaseEvent("NorthAmericaRelease")
    naRelease.label = "North America release"

    euRelease = ReleaseEvent("EuropeRelease")
    euRelease.label = "Europe release"

    # Deal
    eaSpielbergDeal = Deal("EASpielbergDeal")
    eaSpielbergDeal.label = "EA-Spielberg deal"

    # ------------------------------------------------------------------ #
    # Property assignments                                                 #
    # ------------------------------------------------------------------ #

    # Boom Blox Bash Party
    boomBloxBashParty.alternativeTitle = "Boom Blox Smash Party"
    boomBloxBashParty.developedBy     = [eaLosAngeles, amblinEntertainment]
    boomBloxBashParty.publishedBy     = [electronicArts]
    boomBloxBashParty.releasedForPlatform = wii
    boomBloxBashParty.isSequelTo      = boomBlox
    boomBloxBashParty.designedBy      = [stevenSpielberg]
    boomBloxBashParty.hasReleaseEvent = [naRelease, euRelease]
    boomBloxBashParty.levelCount      = "more than 400"
    boomBloxBashParty.announcedOn     = "28 January 2009"
    boomBloxBashParty.onlineServersShutDownDate = "April 2012"
    boomBloxBashParty.countsAsOriginalProperty  = False
    boomBloxBashParty.hasGameMode     = [shootingMode]
    boomBloxBashParty.leastFavoriteMode = shootingMode
    boomBloxBashParty.hasOnlineFeature  = [levelDownload, levelUpload]
    boomBloxBashParty.createdUnderDeal  = eaSpielbergDeal
    boomBloxBashParty.developmentBeganAfterCompletionOf = boomBlox

    # Boom Blox (original) — also designed by Spielberg per the source text
    boomBlox.designedBy = [stevenSpielberg]

    # Release events
    naRelease.inRegion   = northAmerica
    naRelease.releaseDate = "19 May 2009"

    euRelease.inRegion   = europe
    euRelease.releaseDate = "29 May 2009"

    # Deal
    eaSpielbergDeal.hasDealParticipant       = [electronicArts, stevenSpielberg]
    eaSpielbergDeal.targetOriginalPropertyCount = 3


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
