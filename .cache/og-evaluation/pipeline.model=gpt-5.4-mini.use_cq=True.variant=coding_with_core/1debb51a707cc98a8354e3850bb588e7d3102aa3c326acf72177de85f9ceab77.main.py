"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

What is the title of the video game described in the document?

What type of video game is Boom Blox Bash Party?

Which company developed Boom Blox Bash Party?

Which company published Boom Blox Bash Party?

For which video game console was Boom Blox Bash Party released?

Is Boom Blox Bash Party a sequel, and if so, to which game?

On what date was Boom Blox Bash Party released in North America?

On what date was Boom Blox Bash Party released in Europe?

How many levels does Boom Blox Bash Party feature?

Can players download new levels in Boom Blox Bash Party?

Can players upload custom-created levels to share online in Boom Blox Bash Party?

When did development of Boom Blox Bash Party begin?

On what date was Boom Blox Bash Party formally announced?

Who designed Boom Blox Bash Party?

Does the gameplay of Boom Blox Bash Party resemble that of the original Boom Blox?

What new mechanics does Boom Blox Bash Party introduce compared with the original game?

Does Boom Blox Bash Party place less emphasis on the shooting mode than Boom Blox?

Was Boom Blox Bash Party created as part of a deal between Electronic Arts and Steven Spielberg?

Does Boom Blox Bash Party count as one of the three original properties in the Electronic Arts and Steven Spielberg deal?

Are the online servers for Boom Blox Bash Party still available?

Can players still upload and download user-created games for Boom Blox Bash Party?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty, FunctionalProperty, default_world,
)
from og_sandbox_with_core.core import core
from og_sandbox_with_core.core.entities import (
    Abstract,
    NonAgentivePhysicalObject,
    NonPhysicalObject,
    SocialAgent,
    SocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class VideoGame(NonPhysicalObject):
        pass

    class PuzzleVideoGame(VideoGame):
        pass

    class PhysicsBasedPuzzleVideoGame(PuzzleVideoGame):
        pass

    class VideoGameConsole(NonAgentivePhysicalObject):
        pass

    class GameTitle(Abstract):
        pass

    class Deal(SocialObject):
        pass

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [SocialObject]

    class publishedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [SocialObject]

    class designedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [SocialAgent]

    class sequelTo(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class forConsole(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGameConsole]

    class releasedInRegion(ObjectProperty):
        domain = [VideoGame]
        range = [SpaceRegion]

    class releasedInNorthAmericaOn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]

    class releasedInEuropeOn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]

    class formallyAnnouncedOn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]

    class developmentBeganAfter(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class gameplayResembles(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class hasAlternateTitle(ObjectProperty):
        domain = [VideoGame]
        range = [GameTitle]

    class createdAsPartOfDeal(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Deal]

    class dealParticipant(ObjectProperty):
        domain = [Deal]
        range = [SocialObject]

    class onlineServersShutDownBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [SocialObject]

    class onlineServersShutDownAsOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]

    class titleOf(ObjectProperty, FunctionalProperty):
        domain = [GameTitle]
        range = [VideoGame]

    class levelCountDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]

    class supportsNewLevelDownload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class supportsCustomLevelUpload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class supportsOnlineSharing(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class supportsUserCreatedGameUpload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class supportsUserCreatedGameDownload(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class hasNewMechanics(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class hasLessEmphasisOnShootingMode(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class countsAsOriginalProperty(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class originalPropertyCount(DataProperty, FunctionalProperty):
        domain = [Deal]
        range = [int]

    class dealPurposeDescription(DataProperty, FunctionalProperty):
        domain = [Deal]
        range = [str]

    class onlineServersAvailable(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    BoomBloxBashParty = PhysicsBasedPuzzleVideoGame("BoomBloxBashParty")
    BoomBloxBashParty.label = "Boom Blox Bash Party"
    BoomBlox = VideoGame("BoomBlox")
    BoomBlox.label = "Boom Blox"
    BoomBloxSmashPartyInNonEnglishTerritories = GameTitle("BoomBloxSmashPartyInNonEnglishTerritories")
    BoomBloxSmashPartyInNonEnglishTerritories.label = "Boom Blox Smash Party in non - English territories"

    EALosAngeles = Society("EALosAngeles")
    EALosAngeles.label = "EA Los Angeles"
    AmblinEntertainment = Society("AmblinEntertainment")
    AmblinEntertainment.label = "Amblin Entertainment"
    ElectronicArts = Society("ElectronicArts")
    ElectronicArts.label = "Electronic Arts"
    EA = Society("EA")
    EA.label = "EA"
    StevenSpielberg = SocialAgent("StevenSpielberg")
    StevenSpielberg.label = "Steven Spielberg"
    Wii = VideoGameConsole("Wii")
    Wii.label = "Wii"
    NorthAmerica = SpaceRegion("NorthAmerica")
    NorthAmerica.label = "North America"
    Europe = SpaceRegion("Europe")
    Europe.label = "Europe"
    May19_2009 = TimeInterval("May19_2009")
    May19_2009.label = "19 May 2009"
    May29_2009 = TimeInterval("May29_2009")
    May29_2009.label = "29 May 2009"
    Jan28_2009 = TimeInterval("Jan28_2009")
    Jan28_2009.label = "28 January 2009"
    April2012 = TimeInterval("April2012")
    April2012.label = "April 2012"
    ElectronicArtsStevenSpielbergDeal = Deal("ElectronicArtsStevenSpielbergDeal")
    ElectronicArtsStevenSpielbergDeal.label = "deal between Electronic Arts and Steven Spielberg"

    BoomBloxBashParty.developedBy.extend([EALosAngeles, AmblinEntertainment])
    BoomBloxBashParty.publishedBy = ElectronicArts
    BoomBloxBashParty.designedBy = StevenSpielberg
    BoomBloxBashParty.sequelTo = BoomBlox
    BoomBloxBashParty.forConsole = Wii
    BoomBloxBashParty.releasedInRegion.extend([NorthAmerica, Europe])
    BoomBloxBashParty.releasedInNorthAmericaOn = May19_2009
    BoomBloxBashParty.releasedInEuropeOn = May29_2009
    BoomBloxBashParty.formallyAnnouncedOn = Jan28_2009
    BoomBloxBashParty.developmentBeganAfter = BoomBlox
    BoomBloxBashParty.gameplayResembles = BoomBlox
    BoomBloxBashParty.hasAlternateTitle.append(BoomBloxSmashPartyInNonEnglishTerritories)
    BoomBloxBashParty.createdAsPartOfDeal = ElectronicArtsStevenSpielbergDeal
    BoomBloxBashParty.levelCountDescription = "more than 400"
    BoomBloxBashParty.supportsNewLevelDownload = True
    BoomBloxBashParty.supportsCustomLevelUpload = True
    BoomBloxBashParty.supportsOnlineSharing = True
    BoomBloxBashParty.supportsUserCreatedGameUpload = False
    BoomBloxBashParty.supportsUserCreatedGameDownload = False
    BoomBloxBashParty.hasNewMechanics = True
    BoomBloxBashParty.hasLessEmphasisOnShootingMode = True
    BoomBloxBashParty.countsAsOriginalProperty = False
    BoomBloxBashParty.onlineServersAvailable = False
    BoomBloxBashParty.onlineServersShutDownAsOf = April2012
    BoomBloxBashParty.onlineServersShutDownBy = EA

    ElectronicArtsStevenSpielbergDeal.dealParticipant.extend([ElectronicArts, StevenSpielberg])
    ElectronicArtsStevenSpielbergDeal.originalPropertyCount = 3
    ElectronicArtsStevenSpielbergDeal.dealPurposeDescription = "to make three original properties"

    BoomBloxSmashPartyInNonEnglishTerritories.titleOf = BoomBloxBashParty


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
