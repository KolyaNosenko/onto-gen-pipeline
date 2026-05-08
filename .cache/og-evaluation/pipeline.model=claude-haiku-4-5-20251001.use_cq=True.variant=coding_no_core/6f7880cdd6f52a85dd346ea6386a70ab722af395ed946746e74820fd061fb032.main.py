"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

1. What is the title of the game and what are its alternative names in different territories?
2. Who developed Boom Blox Bash Party?
3. Which entertainment companies were involved in the creation of Boom Blox Bash Party?
4. For which video game console was Boom Blox Bash Party released?
5. What is the relationship between Boom Blox Bash Party and Boom Blox?
6. When was Boom Blox Bash Party released in North America and Europe?
7. How many levels does Boom Blox Bash Party feature?
8. What are the key gameplay features of Boom Blox Bash Party?
9. Who designed Boom Blox Bash Party?
10. How does the gameplay of Boom Blox Bash Party compare to the original game?
11. What changes were made to the shooting mode in Boom Blox Bash Party?
12. What kind of deal was made between Electronic Arts and Steven Spielberg?
13. How many original properties were supposed to be created under the EA-Spielberg deal?
14. When was Boom Blox Bash Party formally announced?
15. When did EA shut down the online servers for Boom Blox Bash Party?
16. What functionality was lost after the online servers were shut down?
17. What type of game is Boom Blox Bash Party?
18. What user-generated content features were available in Boom Blox Bash Party?
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
import datetime

model = get_ontology("https://og.example.org/ontology")


with model:
    # Entity classes
    class VideoGame(Thing):
        pass

    class Company(Thing):
        pass

    class Person(Thing):
        pass

    class VideoGameConsole(Thing):
        pass

    class Region(Thing):
        pass

    # Object properties
    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Company]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Company]

    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Person]

    class releasedForConsole(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGameConsole]

    class sequelOf(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class releasedInRegion(ObjectProperty):
        domain = [VideoGame]
        range = [Region]

    # Data properties
    class numberOfLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [int]

    class releaseDate(DataProperty):
        domain = [VideoGame]
        range = [datetime.date]

    class announcementDate(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [datetime.date]

    class serverShutdownDate(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [datetime.date]

    class dealPropertyTargetCount(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [int]

    class countsAsDealProperty(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class hasLevelUploadFeature(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class hasLevelDownloadFeature(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class shootingModeEmphasisLevel(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]

    # Named instances
    # Games
    BoomBloxBashParty = VideoGame("BoomBloxBashParty")
    BoomBloxBashParty.label = ["Boom Blox Bash Party", "Boom Blox Smash Party"]

    BoomBlox = VideoGame("BoomBlox")
    BoomBlox.label = "Boom Blox"

    # Companies
    EALosAngeles = Company("EALosAngeles")
    EALosAngeles.label = "EA Los Angeles"

    AmblinEntertainment = Company("AmblinEntertainment")
    AmblinEntertainment.label = "Amblin Entertainment"

    ElectronicArts = Company("ElectronicArts")
    ElectronicArts.label = "Electronic Arts"

    # Console
    Wii = VideoGameConsole("Wii")
    Wii.label = "Wii"

    # Person
    StevenSpielberg = Person("StevenSpielberg")
    StevenSpielberg.label = "Steven Spielberg"

    # Regions
    NorthAmerica = Region("NorthAmerica")
    NorthAmerica.label = "North America"

    Europe = Region("Europe")
    Europe.label = "Europe"

    # Properties for Boom Blox Bash Party
    BoomBloxBashParty.developedBy = [EALosAngeles, AmblinEntertainment]
    BoomBloxBashParty.publishedBy = [ElectronicArts]
    BoomBloxBashParty.releasedForConsole = [Wii]
    BoomBloxBashParty.designedBy = [StevenSpielberg]
    BoomBloxBashParty.sequelOf = [BoomBlox]
    BoomBloxBashParty.releasedInRegion = [NorthAmerica, Europe]
    BoomBloxBashParty.releaseDate = [datetime.date(2009, 5, 19), datetime.date(2009, 5, 29)]
    BoomBloxBashParty.announcementDate = datetime.date(2009, 1, 28)
    BoomBloxBashParty.serverShutdownDate = datetime.date(2012, 4, 1)
    BoomBloxBashParty.numberOfLevels = 400
    BoomBloxBashParty.hasLevelUploadFeature = True
    BoomBloxBashParty.hasLevelDownloadFeature = True
    BoomBloxBashParty.shootingModeEmphasisLevel = "low"
    BoomBloxBashParty.dealPropertyTargetCount = 3
    BoomBloxBashParty.countsAsDealProperty = False


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
