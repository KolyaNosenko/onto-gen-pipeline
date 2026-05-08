"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the title of the fifth studio album by Becoming the Archetype?
2. When was the album "I Am" released?
3. Which record label released the album "I Am"?
4. During which dates was the album "I Am" recorded?
5. Who is the vocalist on the album "I Am"?
6. Who plays bass on the album "I Am"?
7. Who is the drummer on the album "I Am"?
8. Which band members are new to the album "I Am"?
9. Who is the only original member from the debut album featured on "I Am"?
10. What is the first single from the album "I Am"?
11. When was the first single "The Time Bender" released?
12. How does the musical style of "I Am" differ from the previous album "Celestial Completion"?
13. What instruments were featured in the previous album that are absent in "I Am"?
14. Who is the guitarist and vocalist on the album "I Am"?
15. Did "I Am" feature a lyric video for its first single?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
import datetime

from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    # Domain entity classes
    class Band(Thing): pass
    class Album(Thing): pass
    class Person(Thing): pass
    class RecordLabel(Thing): pass
    class Song(Thing): pass
    class Instrument(Thing): pass

    # Object Properties
    class releasedBy(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [RecordLabel]

    class hasVocalist(ObjectProperty):
        domain = [Album]
        range = [Person]

    class hasBasist(ObjectProperty):
        domain = [Album]
        range = [Person]

    class hasDrummer(ObjectProperty):
        domain = [Album]
        range = [Person]

    class hasGuitarist(ObjectProperty):
        domain = [Album]
        range = [Person]

    class firstSingle(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Song]

    class previousAlbum(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Album]

    class features(ObjectProperty):
        domain = [Album]
        range = [Instrument]

    class promotesAlbum(ObjectProperty, FunctionalProperty):
        domain = [Song]
        range = [Album]

    class belongsTo(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Band]

    # Data Properties
    class studioNumber(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [int]

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [datetime.date]

    class recordingStartDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [datetime.date]

    class recordingEndDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [datetime.date]

    class isOriginalMember(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [bool]

    class singleReleaseDate(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [datetime.date]

    class hasLyricVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]

    class hasOfficialVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]

    # Concrete instances for named entities
    becomingTheArchetype = Band("BecomingTheArchetype")
    becomingTheArchetype.label = "Becoming the Archetype"

    iamAlbum = Album("IAm")
    iamAlbum.label = "I Am"
    iamAlbum.studioNumber = 5
    iamAlbum.releaseDate = datetime.date(2012, 9, 18)
    iamAlbum.recordingStartDate = datetime.date(2012, 5, 21)
    iamAlbum.recordingEndDate = datetime.date(2012, 6, 17)

    celestialCompletion = Album("CelestialCompletion")
    celestialCompletion.label = "Celestial Completion"

    solidStateRecords = RecordLabel("SolidStateRecords")
    solidStateRecords.label = "Solid State Records"

    iamAlbum.releasedBy = solidStateRecords
    iamAlbum.previousAlbum = celestialCompletion

    chrisMcCane = Person("ChrisMcCane")
    chrisMcCane.label = "Chris McCane"
    chrisMcCane.isOriginalMember = False
    chrisMcCane.belongsTo = becomingTheArchetype

    codeyWatkins = Person("CodeyWatkins")
    codeyWatkins.label = "Codey Watkins"
    codeyWatkins.isOriginalMember = False
    codeyWatkins.belongsTo = becomingTheArchetype

    chrisHeaton = Person("ChrisHeaton")
    chrisHeaton.label = "Chris Heaton"
    chrisHeaton.isOriginalMember = False
    chrisHeaton.belongsTo = becomingTheArchetype

    sethHecox = Person("SethHecox")
    sethHecox.label = "Seth Hecox"
    sethHecox.isOriginalMember = True
    sethHecox.belongsTo = becomingTheArchetype

    iamAlbum.hasVocalist = [chrisMcCane, sethHecox]
    iamAlbum.hasBasist = [codeyWatkins]
    iamAlbum.hasDrummer = [chrisHeaton]
    iamAlbum.hasGuitarist = [sethHecox]

    theTimeBender = Song("TheTimeBender")
    theTimeBender.label = "The Time Bender"
    theTimeBender.singleReleaseDate = datetime.date(2012, 8, 28)
    theTimeBender.hasLyricVideo = True
    theTimeBender.hasOfficialVideo = True
    theTimeBender.promotesAlbum = iamAlbum

    iamAlbum.firstSingle = theTimeBender

    sitar = Instrument("Sitar")
    sitar.label = "sitars"

    horn = Instrument("Horn")
    horn.label = "horns"

    celestialCompletion.features = [sitar, horn]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
