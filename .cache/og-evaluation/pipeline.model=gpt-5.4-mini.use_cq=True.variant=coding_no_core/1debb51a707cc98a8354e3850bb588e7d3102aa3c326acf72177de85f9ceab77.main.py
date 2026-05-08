"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

What is the title of the game and its non-English title?
Who developed Boom Blox Bash Party?
Who published Boom Blox Bash Party?
For which video game console was Boom Blox Bash Party released?
Is Boom Blox Bash Party a sequel, and if so, to which game?
When was Boom Blox Bash Party released in North America?
When was Boom Blox Bash Party released in Europe?
How many levels does Boom Blox Bash Party feature?
Can players download new levels in Boom Blox Bash Party?
Can players upload custom-created levels to share online?
When did development of Boom Blox Bash Party begin?
On what date was Boom Blox Bash Party formally announced?
Who designed Boom Blox Bash Party?
How does the gameplay of Boom Blox Bash Party compare to the original Boom Blox?
Which gameplay mode received less emphasis in Boom Blox Bash Party?
Was Boom Blox Bash Party created as part of a deal between Electronic Arts and Steven Spielberg?
Does Boom Blox Bash Party count as one of the three original properties in the deal?
Have the online servers for Boom Blox Bash Party been shut down?
Can players still upload and download user-created games for Boom Blox Bash Party?
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
    class VideoGame(Thing):
        pass

    class PuzzleVideoGame(VideoGame):
        pass

    class PhysicsBasedPuzzleVideoGame(PuzzleVideoGame):
        pass

    class GameConsole(Thing):
        pass

    class Organization(Thing):
        pass

    class Person(Thing):
        pass

    class Region(Thing):
        pass

    class GameMode(Thing):
        pass

    class Title(Thing):
        pass

    class DatePoint(Thing):
        pass

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class releasedForConsole(ObjectProperty):
        domain = [VideoGame]
        range = [GameConsole]

    class sequelTo(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class releasedInRegion(ObjectProperty):
        domain = [VideoGame]
        range = [Region]

    class releasedInNorthAmericaOn(ObjectProperty):
        domain = [VideoGame]
        range = [DatePoint]

    class releasedInEuropeOn(ObjectProperty):
        domain = [VideoGame]
        range = [DatePoint]

    class developmentBeganAfterCompletionOf(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class formallyAnnouncedOn(ObjectProperty):
        domain = [VideoGame]
        range = [DatePoint]

    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Person]

    class resembles(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class lessEmphasisOn(ObjectProperty):
        domain = [VideoGame]
        range = [GameMode]

    class createdAsPartOfDealWith(ObjectProperty):
        domain = [VideoGame]
        range = [Organization, Person]

    class onlineServersShutDownOn(ObjectProperty):
        domain = [VideoGame]
        range = [DatePoint]

    class onlineServersShutDownBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class hasNonEnglishTitle(ObjectProperty):
        domain = [VideoGame]
        range = [Title]

    class levelCountDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]

    class allowsDownloadingNewLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class allowsUploadingCustomCreatedLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class canUploadAndDownloadUserCreatedGames(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class originalPropertyTargetCount(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [int]

    class countsAsOneOfOriginalProperties(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class onlineServersShutDown(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    BoomBloxBashParty = PhysicsBasedPuzzleVideoGame("BoomBloxBashParty")
    BoomBloxBashParty.label = "Boom Blox Bash Party"

    BoomBloxSmashPartyInNonEnglishTerritories = Title("BoomBloxSmashPartyInNonEnglishTerritories")
    BoomBloxSmashPartyInNonEnglishTerritories.label = "Boom Blox Smash Party in non - English territories"

    EALosAngeles = Organization("EALosAngeles")
    EALosAngeles.label = "EA Los Angeles"

    AmblinEntertainment = Organization("AmblinEntertainment")
    AmblinEntertainment.label = "Amblin Entertainment"

    ElectronicArts = Organization("ElectronicArts")
    ElectronicArts.label = ["Electronic Arts", "EA"]

    WiiVideoGameConsole = GameConsole("WiiVideoGameConsole")
    WiiVideoGameConsole.label = "Wii video game console"

    BoomBlox = VideoGame("BoomBlox")
    BoomBlox.label = "Boom Blox"

    NorthAmerica = Region("NorthAmerica")
    NorthAmerica.label = "North America"

    Europe = Region("Europe")
    Europe.label = "Europe"

    StevenSpielberg = Person("StevenSpielberg")
    StevenSpielberg.label = "Steven Spielberg"

    May19_2009 = DatePoint("May19_2009")
    May19_2009.label = "19 May 2009"

    May29_2009 = DatePoint("May29_2009")
    May29_2009.label = "29 May 2009"

    January28_2009 = DatePoint("January28_2009")
    January28_2009.label = "28 January 2009"

    April2012 = DatePoint("April2012")
    April2012.label = "April 2012"

    ShootingMode = GameMode("ShootingMode")
    ShootingMode.label = "shooting mode"

    BoomBloxBashParty.developedBy = [EALosAngeles, AmblinEntertainment]
    BoomBloxBashParty.publishedBy = [ElectronicArts]
    BoomBloxBashParty.releasedForConsole = [WiiVideoGameConsole]
    BoomBloxBashParty.sequelTo = [BoomBlox]
    BoomBloxBashParty.releasedInRegion = [NorthAmerica, Europe]
    BoomBloxBashParty.releasedInNorthAmericaOn = [May19_2009]
    BoomBloxBashParty.releasedInEuropeOn = [May29_2009]
    BoomBloxBashParty.developmentBeganAfterCompletionOf = [BoomBlox]
    BoomBloxBashParty.formallyAnnouncedOn = [January28_2009]
    BoomBloxBashParty.designedBy = [StevenSpielberg]
    BoomBloxBashParty.resembles = [BoomBlox]
    BoomBloxBashParty.lessEmphasisOn = [ShootingMode]
    BoomBloxBashParty.createdAsPartOfDealWith = [ElectronicArts, StevenSpielberg]
    BoomBloxBashParty.hasNonEnglishTitle = [BoomBloxSmashPartyInNonEnglishTerritories]
    BoomBloxBashParty.levelCountDescription = "more than 400"
    BoomBloxBashParty.allowsDownloadingNewLevels = True
    BoomBloxBashParty.allowsUploadingCustomCreatedLevels = True
    BoomBloxBashParty.canUploadAndDownloadUserCreatedGames = False
    BoomBloxBashParty.originalPropertyTargetCount = 3
    BoomBloxBashParty.countsAsOneOfOriginalProperties = False
    BoomBloxBashParty.onlineServersShutDown = True
    BoomBloxBashParty.onlineServersShutDownOn = [April2012]
    BoomBloxBashParty.onlineServersShutDownBy = [ElectronicArts]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
