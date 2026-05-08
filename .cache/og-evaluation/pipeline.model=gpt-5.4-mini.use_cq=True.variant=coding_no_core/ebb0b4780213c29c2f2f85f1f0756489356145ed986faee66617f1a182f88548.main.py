"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the title of the fifth studio album by Becoming the Archetype?
2. What type of release is I Am in the band’s discography?
3. When was I Am recorded?
4. When was I Am released?
5. Which record label released I Am?
6. Which band recorded I Am?
7. How does I Am differ from the band’s previous album, according to Seth Hecox?
8. Which instruments or elements were present on Celestial Completion but absent from I Am?
9. Which songs are described as the heaviest and most technical the band had written up to that point?
10. Which release was the first to feature Chris McCane on vocals?
11. Which release was the first to feature Codey Watkins on bass?
12. Which release was the first to feature Chris Heaton on drums?
13. Which original member from the debut album is featured on I Am?
14. Who is the guitarist and vocalist on I Am?
15. What was the first single released to promote I Am?
16. When was “The Time Bender” released?
17. What promotional media accompanied the release of “The Time Bender”?
18. How many studio albums had Becoming the Archetype released up to I Am?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
from datetime import date
from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    class Organization(Thing):
        pass

    class Band(Organization):
        pass

    class RecordLabel(Organization):
        pass

    class Person(Thing):
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

    class Video(Thing):
        pass

    class PromotionalVideo(Video):
        pass

    class Role(Thing):
        pass

    class MusicalElement(Thing):
        pass

    class DatePoint(Thing):
        pass

    class recordedByBand(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Band]

    class releasedThroughLabel(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [RecordLabel]

    class recordedStartDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [DatePoint]

    class recordedEndDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [DatePoint]

    class releasedOnDate(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [DatePoint]

    class studioAlbumOrdinal(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class hasDescription(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class featuresPerson(ObjectProperty):
        domain = [Album]
        range = [Person]

    class hasRole(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Role]

    class previousEffort(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Album]

    class hasMusicalElement(ObjectProperty):
        domain = [Album]
        range = [MusicalElement]

    class lacksMusicalElement(ObjectProperty):
        domain = [Album]
        range = [MusicalElement]

    class promotesAlbum(ObjectProperty, FunctionalProperty):
        domain = [Single]
        range = [Album]

    class accompaniedBy(ObjectProperty):
        domain = [Single]
        range = [PromotionalVideo]

    class isOriginalMemberOfBand(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Band]

    class dateValue(DataProperty, FunctionalProperty):
        domain = [DatePoint]
        range = [date]

    BecomingTheArchetype = Band("BecomingTheArchetypeBand")
    BecomingTheArchetype.label = "Becoming the Archetype"

    SolidStateRecords = RecordLabel("SolidStateRecordsLabel")
    SolidStateRecords.label = "Solid State Records"

    IAm = StudioAlbum("IAmAlbum")
    IAm.label = "I Am"

    CelestialCompletion = StudioAlbum("CelestialCompletionAlbum")
    CelestialCompletion.label = "Celestial Completion"

    SethHecox = Person("SethHecoxPerson")
    SethHecox.label = "Seth Hecox"

    ChrisMcCane = Person("ChrisMcCanePerson")
    ChrisMcCane.label = "Chris McCane"

    CodeyWatkins = Person("CodeyWatkinsPerson")
    CodeyWatkins.label = "Codey Watkins"

    ChrisHeaton = Person("ChrisHeatonPerson")
    ChrisHeaton.label = "Chris Heaton"

    TheTimeBender = Single("TheTimeBenderSong")
    TheTimeBender.label = "The Time Bender"

    May21 = DatePoint("May21Date")
    May21.label = "May 21"
    May21.dateValue = date(2012, 5, 21)

    June17 = DatePoint("June17Date")
    June17.label = "June 17"
    June17.dateValue = date(2012, 6, 17)

    September18_2012 = DatePoint("September18_2012Date")
    September18_2012.label = "September 18 , 2012"
    September18_2012.dateValue = date(2012, 9, 18)

    August28_2012 = DatePoint("August28_2012Date")
    August28_2012.label = "August 28 , 2012"
    August28_2012.dateValue = date(2012, 8, 28)

    Sitars = MusicalElement("SitarsElement")
    Sitars.label = "sitars"

    Horns = MusicalElement("HornsElement")
    Horns.label = "horns"

    Vocals = Role("VocalsRole")
    Vocals.label = "vocals"

    Bass = Role("BassRole")
    Bass.label = "bass"

    Drums = Role("DrumsRole")
    Drums.label = "drums"

    GuitaristVocalist = Role("GuitaristVocalistRole")
    GuitaristVocalist.label = "Guitarist / vocalist"

    LyricVideo = PromotionalVideo("LyricVideoMedia")
    LyricVideo.label = "lyric video"

    OfficialVideo = PromotionalVideo("OfficialVideoMedia")
    OfficialVideo.label = "official video"

    IAm.recordedByBand = BecomingTheArchetype
    IAm.releasedThroughLabel = SolidStateRecords
    IAm.recordedStartDate = May21
    IAm.recordedEndDate = June17
    IAm.releasedOnDate = September18_2012
    IAm.studioAlbumOrdinal = 5
    IAm.hasDescription = "gone are the sitars and horns of Celestial Completion. Instead, we've crafted an album full of the heaviest and most technical songs we've ever written."
    IAm.previousEffort = CelestialCompletion
    IAm.featuresPerson = [ChrisMcCane, CodeyWatkins, ChrisHeaton, SethHecox]
    IAm.lacksMusicalElement = [Sitars, Horns]
    CelestialCompletion.hasMusicalElement = [Sitars, Horns]

    SethHecox.hasRole = GuitaristVocalist
    SethHecox.isOriginalMemberOfBand = BecomingTheArchetype
    ChrisMcCane.hasRole = Vocals
    CodeyWatkins.hasRole = Bass
    ChrisHeaton.hasRole = Drums

    TheTimeBender.promotesAlbum = IAm
    TheTimeBender.releasedOnDate = August28_2012
    TheTimeBender.accompaniedBy = [LyricVideo, OfficialVideo]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
