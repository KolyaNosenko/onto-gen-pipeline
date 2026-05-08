"""
=== TASK INPUT ===
Source text:
Boom Blox Bash Party , Boom Blox Smash Party in non - English territories , is a physics - based puzzle video game developed by EA Los Angeles and Amblin Entertainment and published by Electronic Arts for the Wii video game console . It is a sequel to Boom Blox , and was released on 19 May 2009 in North America and in Europe on 29 May 2009 . The game features more than 400 levels , and players are able to download new levels and upload their own custom - created levels to share online . Its development began after the completion of its predecessor , and it was formally announced on 28 January 2009 . As with the original game , this sequel was also designed by film director Steven Spielberg . The gameplay of Boom Blox Bash Party resembles the original 's , but features new mechanics . It also has less emphasis on the shooting mode , which the developers commented was their least favorite mode of play in Boom Blox . It was created as part of a deal between Electronic Arts and Steven Spielberg to make three original properties , though it does not count as one of the three original properties . As of April 2012 , EA has shut down the online servers , meaning players can no longer upload and download user created games .

1. What is the title of the game and what are its alternate names in different territories?
2. Who developed Boom Blox Bash Party?
3. Who published Boom Blox Bash Party?
4. For which video game console was Boom Blox Bash Party released?
5. What is the predecessor game of Boom Blox Bash Party?
6. When was Boom Blox Bash Party released in North America?
7. When was Boom Blox Bash Party released in Europe?
8. How many levels does Boom Blox Bash Party feature?
9. What features does Boom Blox Bash Party offer regarding user-generated content?
10. When was the development of Boom Blox Bash Party announced?
11. Who designed Boom Blox Bash Party?
12. How does the gameplay of Boom Blox Bash Party compare to the original game?
13. What new mechanics were introduced in Boom Blox Bash Party?
14. What gameplay mode received less emphasis in Boom Blox Bash Party compared to the original?
15. What was the reason for reducing emphasis on the shooting mode?
16. What deal was Boom Blox Bash Party created as part of?
17. Does Boom Blox Bash Party count as one of the three original properties in the EA-Spielberg deal?
18. When did EA shut down the online servers for Boom Blox Bash Party?
19. What functionality was lost when EA shut down the online servers?
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
    NonAgentiveSocialObject, NonAgentivePhysicalObject, AgentivePhysicalObject,
    Society, SpaceRegion, TimeInterval
)


with core:
    # Domain entity classes
    class VideoGame(NonAgentiveSocialObject):
        """A video game is a non-physical, cultural artefact."""
        pass
    
    class GameConsole(NonAgentivePhysicalObject):
        """A physical gaming hardware platform."""
        pass
    
    # Domain ObjectProperties
    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Society]
    
    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Society]
    
    class releasedFor(ObjectProperty):
        domain = [VideoGame]
        range = [NonAgentivePhysicalObject]
    
    class sequelOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]
    
    class designedBy(ObjectProperty):
        domain = [VideoGame]
        range = [AgentivePhysicalObject]
    
    class releasedInNorthAmerica(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]
    
    class releasedInEurope(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]
    
    class announcementDate(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]
    
    class developmentStartedAfter(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]
    
    class serverShutdownDate(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]
    
    # Domain DataProperties
    class numberOfLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class alternateTitle(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class lessEmphasizedMode(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class reasonForReducedEmphasis(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class creationDeal(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class countsAsOriginalProperty(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]
    
    class allowsDownloadingLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]
    
    class allowsUploadingLevels(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]
    
    class introducesNewMechanics(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]
    
    # Named instances from the source text
    
    # TimeInterval instances (dates mentioned in text)
    dateAnnouncement = TimeInterval('Jan28_2009')
    dateAnnouncement.label = '28 January 2009'
    
    dateReleaseNA = TimeInterval('May19_2009')
    dateReleaseNA.label = '19 May 2009'
    
    dateReleaseEU = TimeInterval('May29_2009')
    dateReleaseEU.label = '29 May 2009'
    
    dateServerShutdown = TimeInterval('April2012')
    dateServerShutdown.label = 'April 2012'
    
    # SpaceRegion instances
    northAmerica = SpaceRegion('NorthAmerica')
    northAmerica.label = 'North America'
    
    europe = SpaceRegion('Europe')
    europe.label = 'Europe'
    
    # Society instances (organizations)
    eaLosAngeles = Society('EALosAngeles')
    eaLosAngeles.label = 'EA Los Angeles'
    
    amblinEntertainment = Society('AmblinEntertainment')
    amblinEntertainment.label = 'Amblin Entertainment'
    
    electronicArts = Society('ElectronicArts')
    electronicArts.label = 'Electronic Arts'
    
    # AgentivePhysicalObject instance (person)
    spielberg = AgentivePhysicalObject('StevenSpielberg')
    spielberg.label = 'Steven Spielberg'
    
    # GameConsole instance
    wii = GameConsole('Wii')
    wii.label = 'Wii'
    
    # VideoGame instances
    boomBlox = VideoGame('BoomBlox')
    boomBlox.label = 'Boom Blox'
    
    boomBloxBashParty = VideoGame('BoomBloxBashParty')
    boomBloxBashParty.label = 'Boom Blox Bash Party'
    boomBloxBashParty.alternateTitle = 'Boom Blox Smash Party'
    boomBloxBashParty.developedBy = [eaLosAngeles, amblinEntertainment]
    boomBloxBashParty.publishedBy = [electronicArts]
    boomBloxBashParty.releasedFor = [wii]
    boomBloxBashParty.sequelOf = boomBlox
    boomBloxBashParty.numberOfLevels = 'more than 400'
    boomBloxBashParty.designedBy = [spielberg]
    boomBloxBashParty.announcementDate = dateAnnouncement
    boomBloxBashParty.releasedInNorthAmerica = dateReleaseNA
    boomBloxBashParty.releasedInEurope = dateReleaseEU
    boomBloxBashParty.developmentStartedAfter = boomBlox
    boomBloxBashParty.lessEmphasizedMode = 'shooting mode'
    boomBloxBashParty.reasonForReducedEmphasis = 'it was the developers\' least favorite mode of play in Boom Blox'
    boomBloxBashParty.creationDeal = 'a deal between Electronic Arts and Steven Spielberg to make three original properties'
    boomBloxBashParty.countsAsOriginalProperty = False
    boomBloxBashParty.serverShutdownDate = dateServerShutdown
    boomBloxBashParty.allowsDownloadingLevels = True
    boomBloxBashParty.allowsUploadingLevels = True
    boomBloxBashParty.introducesNewMechanics = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
