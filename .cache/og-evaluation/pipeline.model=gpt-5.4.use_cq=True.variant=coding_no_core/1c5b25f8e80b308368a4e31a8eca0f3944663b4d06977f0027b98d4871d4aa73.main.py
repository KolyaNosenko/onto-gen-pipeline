"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

What is the title of the fifth studio album by Becoming the Archetype?
Which band released the album I Am?
What number studio album is I Am in Becoming the Archetype’s discography?
Between what dates was the album I Am recorded?
On what date was the album I Am released?
Through which record label was I Am released?
How does I Am differ stylistically from the previous album Celestial Completion?
Which instruments or musical elements present in Celestial Completion were absent from I Am?
How was I Am described by Seth Hecox in terms of musical style?
Which members made their first appearance on a Becoming the Archetype release with I Am?
Did I Am feature Chris McCane on vocals?
Did I Am feature Codey Watkins on bass?
Did I Am feature Chris Heaton on drums?
Who was the only original member from the debut album featured on I Am?
What roles did Seth Hecox perform on I Am?
What was the first single released to promote I Am?
On what date was the song The Time Bender released as the first single?
Was The Time Bender accompanied by a lyric video?
Was there an official video released for The Time Bender?
What album preceded I Am by Becoming the Archetype?
Which quote by Seth Hecox describes the musical direction of I Am?
Which band members and their instruments are associated with I Am?
Was I Am released before or after August 28, 2012?
How long was the recording period for I Am?
Which people contributed vocals, bass, drums, and guitar/vocals on I Am?
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
    class Person(Thing):
        pass

    class Musician(Person):
        pass

    class Vocalist(Musician):
        pass

    class Bassist(Musician):
        pass

    class Drummer(Musician):
        pass

    class Guitarist(Musician):
        pass

    class GuitaristVocalist(Musician):
        pass

    class Organization(Thing):
        pass

    class Band(Organization):
        pass

    class RecordLabel(Organization):
        pass

    class MusicalWork(Thing):
        pass

    class Album(MusicalWork):
        pass

    class StudioAlbum(Album):
        pass

    class Song(MusicalWork):
        pass

    class Single(Song):
        pass

    class DatePoint(Thing):
        pass

    class releasedByBand(ObjectProperty, FunctionalProperty):
        domain = [MusicalWork]
        range = [Band]

    class releasedThrough(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [RecordLabel]

    class recordingStartDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [DatePoint]

    class recordingEndDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [DatePoint]

    class releasedOn(ObjectProperty, FunctionalProperty):
        domain = [MusicalWork]
        range = [DatePoint]

    class previousAlbum(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Album]

    class departsStylisticallyFrom(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Album]

    class firstSingle(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Single]

    class promotesAlbum(ObjectProperty, FunctionalProperty):
        domain = [Single]
        range = [Album]

    class hasMember(ObjectProperty):
        domain = [Band]
        range = [Musician]

    class memberOfBand(ObjectProperty):
        domain = [Musician]
        range = [Band]

    class hasVocalist(ObjectProperty):
        domain = [Album]
        range = [Musician]

    class hasBassist(ObjectProperty):
        domain = [Album]
        range = [Musician]

    class hasDrummer(ObjectProperty):
        domain = [Album]
        range = [Musician]

    class hasGuitarist(ObjectProperty):
        domain = [Album]
        range = [Musician]

    class firstReleaseByBandFeaturing(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range = [Album]

    class onlyOriginalMemberFromDebutAlbum(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Musician]

    class quoteSource(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Musician]

    class albumNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class musicalStyleDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class descriptiveQuote(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class lacksMusicalElement(DataProperty):
        domain = [Album]
        range = [str]

    class containsMusicalElement(DataProperty):
        domain = [Album]
        range = [str]

    class hasLyricVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]

    class hasOfficialVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]

    class isOriginalMemberFromDebutAlbum(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [bool]

    BecomingTheArchetype = Band("BecomingTheArchetype")
    BecomingTheArchetype.label = "Becoming the Archetype"

    IAm = StudioAlbum("IAmAlbum")
    IAm.label = "I Am"

    CelestialCompletion = StudioAlbum("CelestialCompletion")
    CelestialCompletion.label = "Celestial Completion"

    TheTimeBender = Single("TheTimeBender")
    TheTimeBender.label = "The Time Bender"

    SolidStateRecords = RecordLabel("SolidStateRecords")
    SolidStateRecords.label = "Solid State Records"

    SethHecox = GuitaristVocalist("SethHecox")
    SethHecox.label = "Seth Hecox"

    ChrisMcCane = Vocalist("ChrisMcCane")
    ChrisMcCane.label = "Chris McCane"

    CodeyWatkins = Bassist("CodeyWatkins")
    CodeyWatkins.label = "Codey Watkins"

    ChrisHeaton = Drummer("ChrisHeaton")
    ChrisHeaton.label = "Chris Heaton"

    May21 = DatePoint("May21")
    May21.label = "May 21"

    June17 = DatePoint("June17")
    June17.label = "June 17"

    September182012 = DatePoint("September18_2012")
    September182012.label = "September 18 , 2012"

    August282012 = DatePoint("August28_2012")
    August282012.label = "August 28 , 2012"

    BecomingTheArchetype.hasMember = [SethHecox, ChrisMcCane, CodeyWatkins, ChrisHeaton]

    SethHecox.memberOfBand = [BecomingTheArchetype]
    SethHecox.isOriginalMemberFromDebutAlbum = True
    ChrisMcCane.memberOfBand = [BecomingTheArchetype]
    CodeyWatkins.memberOfBand = [BecomingTheArchetype]
    ChrisHeaton.memberOfBand = [BecomingTheArchetype]

    IAm.releasedByBand = BecomingTheArchetype
    IAm.albumNumber = 5
    IAm.recordingStartDate = May21
    IAm.recordingEndDate = June17
    IAm.releasedOn = September182012
    IAm.releasedThrough = SolidStateRecords
    IAm.previousAlbum = CelestialCompletion
    IAm.departsStylisticallyFrom = CelestialCompletion
    IAm.musicalStyleDescription = "full of the heaviest and most technical songs we've ever written"
    IAm.descriptiveQuote = "gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written ."
    IAm.quoteSource = SethHecox
    IAm.lacksMusicalElement = ["sitars", "horns"]
    IAm.hasVocalist = [ChrisMcCane, SethHecox]
    IAm.hasBassist = [CodeyWatkins]
    IAm.hasDrummer = [ChrisHeaton]
    IAm.hasGuitarist = [SethHecox]
    IAm.firstSingle = TheTimeBender
    IAm.onlyOriginalMemberFromDebutAlbum = SethHecox

    CelestialCompletion.releasedByBand = BecomingTheArchetype
    CelestialCompletion.containsMusicalElement = ["sitars", "horns"]

    ChrisMcCane.firstReleaseByBandFeaturing = IAm
    CodeyWatkins.firstReleaseByBandFeaturing = IAm
    ChrisHeaton.firstReleaseByBandFeaturing = IAm

    TheTimeBender.promotesAlbum = IAm
    TheTimeBender.releasedByBand = BecomingTheArchetype
    TheTimeBender.releasedOn = August282012
    TheTimeBender.hasLyricVideo = True
    TheTimeBender.hasOfficialVideo = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
