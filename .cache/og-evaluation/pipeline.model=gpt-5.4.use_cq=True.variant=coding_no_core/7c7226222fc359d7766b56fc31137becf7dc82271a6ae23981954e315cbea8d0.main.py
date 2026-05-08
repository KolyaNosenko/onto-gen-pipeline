"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

What is Boom Blox Bash Party?
What is the non-English title of Boom Blox Bash Party?
What type of video game is Boom Blox Bash Party?
Who developed Boom Blox Bash Party?
Who published Boom Blox Bash Party?
For which video game console was Boom Blox Bash Party released?
Is Boom Blox Bash Party a sequel to another game?
What game is Boom Blox Bash Party a sequel to?
When was Boom Blox Bash Party released in North America?
When was Boom Blox Bash Party released in Europe?
How many levels does Boom Blox Bash Party feature?
Can players download new levels in Boom Blox Bash Party?
Can players upload their own custom-created levels in Boom Blox Bash Party?
What online sharing features are available in Boom Blox Bash Party?
When did the development of Boom Blox Bash Party begin?
Did development of Boom Blox Bash Party begin after the completion of its predecessor?
When was Boom Blox Bash Party formally announced?
Who designed Boom Blox Bash Party?
Was Steven Spielberg involved in the design of Boom Blox Bash Party?
How does the gameplay of Boom Blox Bash Party compare to the original Boom Blox?
Does Boom Blox Bash Party introduce new gameplay mechanics?
How much emphasis does Boom Blox Bash Party place on the shooting mode?
What did the developers say about the shooting mode in Boom Blox?
Was Boom Blox Bash Party created as part of a deal between Electronic Arts and Steven Spielberg?
What was the deal between Electronic Arts and Steven Spielberg related to Boom Blox Bash Party?
Did Boom Blox Bash Party count as one of the three original properties in the deal between Electronic Arts and Steven Spielberg?
What happened to the online servers for Boom Blox Bash Party as of April 2012?
Can players still upload user-created games in Boom Blox Bash Party after April 2012?
Can players still download user-created games in Boom Blox Bash Party after April 2012?
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
    class CreativeWork(Thing):
        pass

    class VideoGame(CreativeWork):
        pass

    class PuzzleVideoGame(VideoGame):
        pass

    class PhysicsBasedPuzzleVideoGame(PuzzleVideoGame):
        pass

    class Organization(Thing):
        pass

    class Person(Thing):
        pass

    class FilmDirector(Person):
        pass

    class VideoGameConsole(Thing):
        pass

    class Region(Thing):
        pass

    class DatePoint(Thing):
        pass

    class GameTitle(Thing):
        pass

    class OrganizationName(Thing):
        pass

    class hasNonEnglishTitle(ObjectProperty):
        domain = [VideoGame]
        range = [GameTitle]

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class releasedFor(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGameConsole]

    class isSequelTo(ObjectProperty):
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

    class gameplayResembles(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class createdAsPartOfDealWith(ObjectProperty):
        domain = [VideoGame]
        range = [Organization, Person]

    class onlineServersShutDownAsOf(ObjectProperty):
        domain = [VideoGame]
        range = [DatePoint]

    class onlineServersShutDownBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class hasShortName(ObjectProperty):
        domain = [Organization]
        range = [OrganizationName]

    class levelCountDescription(DataProperty):
        domain = [VideoGame]
        range = [str]

    class playersCanDownloadNewLevels(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class playersCanUploadCustomCreatedLevels(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class playersCanShareCustomCreatedLevelsOnline(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class developmentBeganAfterPredecessorCompletion(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class hasNewGameplayMechanics(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class shootingModeEmphasisDescription(DataProperty):
        domain = [VideoGame]
        range = [str]

    class shootingModeDeveloperComment(DataProperty):
        domain = [VideoGame]
        range = [str]

    class createdAsPartOfDeal(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class dealPurposeDescription(DataProperty):
        domain = [VideoGame]
        range = [str]

    class dealOriginalPropertyCount(DataProperty):
        domain = [VideoGame]
        range = [int]

    class countsAsOneOfThreeOriginalProperties(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class onlineServersShutDown(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class playersCanUploadUserCreatedGamesAfterShutdown(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class playersCanDownloadUserCreatedGamesAfterShutdown(DataProperty):
        domain = [VideoGame]
        range = [bool]

    class SequelVideoGame(VideoGame):
        is_a = [isSequelTo.some(VideoGame)]

    BoomBloxBashParty = PhysicsBasedPuzzleVideoGame("BoomBloxBashParty")
    BoomBloxBashParty.label = "Boom Blox Bash Party"

    BoomBloxSmashParty = GameTitle("BoomBloxSmashParty")
    BoomBloxSmashParty.label = "Boom Blox Smash Party"

    EALosAngeles = Organization("EALosAngeles")
    EALosAngeles.label = "EA Los Angeles"

    AmblinEntertainment = Organization("AmblinEntertainment")
    AmblinEntertainment.label = "Amblin Entertainment"

    ElectronicArts = Organization("ElectronicArts")
    ElectronicArts.label = "Electronic Arts"

    EA = OrganizationName("EAAbbreviation")
    EA.label = "EA"

    Wii = VideoGameConsole("WiiConsole")
    Wii.label = "Wii"

    BoomBlox = VideoGame("BoomBlox")
    BoomBlox.label = "Boom Blox"

    Date19May2009 = DatePoint("Date19May2009")
    Date19May2009.label = "19 May 2009"

    NorthAmerica = Region("NorthAmerica")
    NorthAmerica.label = "North America"

    Europe = Region("EuropeRegion")
    Europe.label = "Europe"

    Date29May2009 = DatePoint("Date29May2009")
    Date29May2009.label = "29 May 2009"

    Date28January2009 = DatePoint("Date28January2009")
    Date28January2009.label = "28 January 2009"

    StevenSpielberg = FilmDirector("StevenSpielberg")
    StevenSpielberg.label = "Steven Spielberg"

    April2012 = DatePoint("April2012Date")
    April2012.label = "April 2012"

    BoomBloxBashParty.hasNonEnglishTitle = [BoomBloxSmashParty]
    BoomBloxBashParty.developedBy = [EALosAngeles, AmblinEntertainment]
    BoomBloxBashParty.publishedBy = [ElectronicArts]
    BoomBloxBashParty.releasedFor = [Wii]
    BoomBloxBashParty.isSequelTo = [BoomBlox]
    BoomBloxBashParty.releasedInRegion = [NorthAmerica, Europe]
    BoomBloxBashParty.releasedInNorthAmericaOn = [Date19May2009]
    BoomBloxBashParty.releasedInEuropeOn = [Date29May2009]
    BoomBloxBashParty.levelCountDescription = ["more than 400"]
    BoomBloxBashParty.playersCanDownloadNewLevels = [True]
    BoomBloxBashParty.playersCanUploadCustomCreatedLevels = [True]
    BoomBloxBashParty.playersCanShareCustomCreatedLevelsOnline = [True]
    BoomBloxBashParty.developmentBeganAfterCompletionOf = [BoomBlox]
    BoomBloxBashParty.developmentBeganAfterPredecessorCompletion = [True]
    BoomBloxBashParty.formallyAnnouncedOn = [Date28January2009]
    BoomBloxBashParty.designedBy = [StevenSpielberg]
    BoomBloxBashParty.gameplayResembles = [BoomBlox]
    BoomBloxBashParty.hasNewGameplayMechanics = [True]
    BoomBloxBashParty.shootingModeEmphasisDescription = ["less emphasis on the shooting mode"]
    BoomBloxBashParty.shootingModeDeveloperComment = ["the shooting mode was the developers' least favorite mode of play in Boom Blox"]
    BoomBloxBashParty.createdAsPartOfDeal = [True]
    BoomBloxBashParty.createdAsPartOfDealWith = [ElectronicArts, StevenSpielberg]
    BoomBloxBashParty.dealPurposeDescription = ["make three original properties"]
    BoomBloxBashParty.dealOriginalPropertyCount = [3]
    BoomBloxBashParty.countsAsOneOfThreeOriginalProperties = [False]
    BoomBloxBashParty.onlineServersShutDown = [True]
    BoomBloxBashParty.onlineServersShutDownAsOf = [April2012]
    BoomBloxBashParty.onlineServersShutDownBy = [ElectronicArts]
    BoomBloxBashParty.playersCanUploadUserCreatedGamesAfterShutdown = [False]
    BoomBloxBashParty.playersCanDownloadUserCreatedGamesAfterShutdown = [False]

    ElectronicArts.hasShortName = [EA]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
