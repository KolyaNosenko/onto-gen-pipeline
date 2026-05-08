"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

1. What is the title of the video game Boom Blox Bash Party in non-English territories?
2. What type of video game is Boom Blox Bash Party?
3. Who developed Boom Blox Bash Party?
4. Who published Boom Blox Bash Party?
5. For which video game console was Boom Blox Bash Party released?
6. Of which game is Boom Blox Bash Party a sequel?
7. When was Boom Blox Bash Party released in North America?
8. When was Boom Blox Bash Party released in Europe?
9. How many levels does Boom Blox Bash Party feature?
10. Can players download new levels in Boom Blox Bash Party?
11. Can players upload their own custom-created levels to share online in Boom Blox Bash Party?
12. When did the development of Boom Blox Bash Party begin relative to its predecessor?
13. On what date was Boom Blox Bash Party formally announced?
14. Who designed Boom Blox Bash Party?
15. How does the gameplay of Boom Blox Bash Party compare to that of the original Boom Blox?
16. What new gameplay mechanics are featured in Boom Blox Bash Party?
17. Which gameplay mode received less emphasis in Boom Blox Bash Party?
18. Why did the developers place less emphasis on the shooting mode in Boom Blox Bash Party?
19. Under what deal or agreement was Boom Blox Bash Party created?
20. Does Boom Blox Bash Party count as one of the three original properties in the deal between Electronic Arts and Steven Spielberg?
21. What happened to the online servers for Boom Blox Bash Party as of April 2012?
22. What effect did the shutdown of the online servers have on players’ ability to upload and download user-created games?
23. Which companies were involved in the development of Boom Blox Bash Party?
24. What alternative title is used for Boom Blox Bash Party outside English-speaking territories?
25. What online sharing features were available in Boom Blox Bash Party before the server shutdown?
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
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class Person(AgentivePhysicalObject):
        pass


    class FilmDirector(Person):
        pass


    class Organization(Society):
        pass


    class GameCompany(Organization):
        pass


    class VideoGame(NonAgentiveSocialObject):
        pass


    class PhysicsBasedPuzzleVideoGame(VideoGame):
        pass


    class VideoGameTitle(NonAgentiveSocialObject):
        pass


    class VideoGameConsole(NonAgentivePhysicalObject):
        pass


    class GameLevel(NonAgentiveSocialObject):
        pass


    class CustomCreatedLevel(GameLevel):
        pass


    class GameplayMechanic(NonAgentiveSocialObject):
        pass


    class GameplayMode(NonAgentiveSocialObject):
        pass


    class DevelopmentDeal(NonAgentiveSocialObject):
        pass


    class OriginalProperty(NonAgentiveSocialObject):
        pass


    class OnlineServer(NonAgentivePhysicalObject):
        pass


    class GeographicRegion(SpaceRegion):
        pass


    class CalendarTimeInterval(TimeInterval):
        pass


    class hasAlternativeTitleInNonEnglishTerritories(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGameTitle]


    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [GameCompany]


    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [GameCompany]


    class releasedFor(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGameConsole]


    class releasedIn(ObjectProperty):
        domain = [VideoGame]
        range = [GeographicRegion]


    class sequelTo(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]


    class releaseDateInNorthAmerica(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [CalendarTimeInterval]


    class releaseDateInEurope(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [CalendarTimeInterval]


    class developmentBeganAfterCompletionOf(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]


    class formallyAnnouncedOn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [CalendarTimeInterval]


    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Person]


    class gameplayResembles(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]


    class serverShutdownAsOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [CalendarTimeInterval]


    class serverShutdownBy(ObjectProperty):
        domain = [VideoGame]
        range = [GameCompany]


    class featuredLevelCountDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class allowsDownloadingNewLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]


    class allowsUploadingCustomCreatedLevelsOnline(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]


    class gameplayComparisonDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class newGameplayMechanicsDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class lessEmphasizedModeDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class lessEmphasisReasonDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class creationDealDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class dealOriginalPropertyTargetCount(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [int]


    class countsAsOneOfDealOriginalProperties(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]


    class onlineSharingFeaturesDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class serverShutdownEffectDescription(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]


    class canUploadUserCreatedGamesAfterShutdown(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]


    class canDownloadUserCreatedGamesAfterShutdown(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]


    BoomBloxBashParty = PhysicsBasedPuzzleVideoGame("BoomBloxBashParty")
    BoomBloxBashParty.label = "Boom Blox Bash Party"

    BoomBloxSmashParty = VideoGameTitle("BoomBloxSmashPartyTitle")
    BoomBloxSmashParty.label = "Boom Blox Smash Party"

    BoomBlox = VideoGame("BoomBlox")
    BoomBlox.label = "Boom Blox"

    EALosAngeles = GameCompany("EALosAngeles")
    EALosAngeles.label = "EA Los Angeles"

    AmblinEntertainment = GameCompany("AmblinEntertainment")
    AmblinEntertainment.label = "Amblin Entertainment"

    ElectronicArts = GameCompany("ElectronicArts")
    ElectronicArts.label = ["Electronic Arts", "EA"]

    StevenSpielberg = FilmDirector("StevenSpielberg")
    StevenSpielberg.label = "Steven Spielberg"

    Wii = VideoGameConsole("Wii")
    Wii.label = "Wii"

    NorthAmerica = GeographicRegion("NorthAmerica")
    NorthAmerica.label = "North America"

    Europe = GeographicRegion("Europe")
    Europe.label = "Europe"

    NineteenMay2009 = CalendarTimeInterval("NineteenMay2009")
    NineteenMay2009.label = "19 May 2009"

    TwentyNineMay2009 = CalendarTimeInterval("TwentyNineMay2009")
    TwentyNineMay2009.label = "29 May 2009"

    TwentyEightJanuary2009 = CalendarTimeInterval("TwentyEightJanuary2009")
    TwentyEightJanuary2009.label = "28 January 2009"

    April2012 = CalendarTimeInterval("April2012")
    April2012.label = "April 2012"

    BoomBloxBashParty.hasAlternativeTitleInNonEnglishTerritories = [BoomBloxSmashParty]
    BoomBloxBashParty.developedBy = [EALosAngeles, AmblinEntertainment]
    BoomBloxBashParty.publishedBy = [ElectronicArts]
    BoomBloxBashParty.releasedFor = [Wii]
    BoomBloxBashParty.releasedIn = [NorthAmerica, Europe]
    BoomBloxBashParty.sequelTo = [BoomBlox]
    BoomBloxBashParty.releaseDateInNorthAmerica = NineteenMay2009
    BoomBloxBashParty.releaseDateInEurope = TwentyNineMay2009
    BoomBloxBashParty.developmentBeganAfterCompletionOf = [BoomBlox]
    BoomBloxBashParty.formallyAnnouncedOn = TwentyEightJanuary2009
    BoomBloxBashParty.designedBy = [StevenSpielberg]
    BoomBloxBashParty.gameplayResembles = [BoomBlox]
    BoomBloxBashParty.serverShutdownAsOf = April2012
    BoomBloxBashParty.serverShutdownBy = [ElectronicArts]
    BoomBloxBashParty.featuredLevelCountDescription = "more than 400 levels"
    BoomBloxBashParty.allowsDownloadingNewLevels = True
    BoomBloxBashParty.allowsUploadingCustomCreatedLevelsOnline = True
    BoomBloxBashParty.gameplayComparisonDescription = "resembles the original's gameplay, but features new mechanics"
    BoomBloxBashParty.newGameplayMechanicsDescription = "new mechanics"
    BoomBloxBashParty.lessEmphasizedModeDescription = "shooting mode"
    BoomBloxBashParty.lessEmphasisReasonDescription = (
        "the developers commented that it was their least favorite mode of play in Boom Blox"
    )
    BoomBloxBashParty.creationDealDescription = (
        "a deal between Electronic Arts and Steven Spielberg to make three original properties"
    )
    BoomBloxBashParty.dealOriginalPropertyTargetCount = 3
    BoomBloxBashParty.countsAsOneOfDealOriginalProperties = False
    BoomBloxBashParty.onlineSharingFeaturesDescription = (
        "players could download new levels and upload their own custom-created levels to share online"
    )
    BoomBloxBashParty.serverShutdownEffectDescription = (
        "players can no longer upload and download user created games"
    )
    BoomBloxBashParty.canUploadUserCreatedGamesAfterShutdown = False
    BoomBloxBashParty.canDownloadUserCreatedGamesAfterShutdown = False


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
