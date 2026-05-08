"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

What is the title of the fifth studio album by Becoming the Archetype?
Which band released the album I Am?
What type of album is I Am?
What number studio album is I Am in Becoming the Archetype’s discography?
When was I Am recorded?
On what date was I Am released?
Through which record label was I Am released?
How does I Am differ stylistically from the band’s previous album Celestial Completion?
Which musical elements present in Celestial Completion were said to be absent from I Am?
How was I Am described by Seth Hecox in terms of heaviness and technicality?
Who provided a statement about the musical direction of I Am?
Which band members made their first appearance on I Am?
Did I Am mark the first release featuring Chris McCane on vocals?
Did I Am mark the first release featuring Codey Watkins on bass?
Did I Am mark the first release featuring Chris Heaton on drums?
Who was the only original member from the debut album featured on I Am?
What roles did Seth Hecox perform on I Am?
What was the first single released to promote I Am?
When was the first single from I Am released?
What promotional materials were released for the song The Time Bender?
Was an official video released for The Time Bender?
Was a lyric video released for The Time Bender?
What is the relationship between The Time Bender and the album I Am?
Which album preceded I Am in Becoming the Archetype’s discography?
What band members and their instruments or roles are associated with I Am?
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
    NonAgentiveSocialObject,
    Society,
    TimeInterval,
)


with core:
    class Musician(AgentivePhysicalObject):
        pass


    class MusicGroup(Society):
        pass


    class HeavyMetalBand(MusicGroup):
        pass


    class RecordLabel(Society):
        pass


    class MusicalWork(NonAgentiveSocialObject):
        pass


    class Album(MusicalWork):
        pass


    class StudioAlbum(Album):
        pass


    class Song(MusicalWork):
        pass


    class SingleSong(Song):
        pass


    class PromotionalMaterial(NonAgentiveSocialObject):
        pass


    class Video(PromotionalMaterial):
        pass


    class LyricVideo(Video):
        pass


    class OfficialVideo(Video):
        pass


    class CalendarDate(TimeInterval):
        pass


    class releasedByBand(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [HeavyMetalBand]


    class releasedThrough(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [RecordLabel]


    class previousAlbum(ObjectProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [StudioAlbum]


    class releasedOn(ObjectProperty, FunctionalProperty):
        domain = [MusicalWork]
        range = [CalendarDate]


    class recordingStartDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [CalendarDate]


    class recordingEndDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [CalendarDate]


    class promotesAlbum(ObjectProperty, FunctionalProperty):
        domain = [SingleSong]
        range = [StudioAlbum]


    class firstSingle(ObjectProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [SingleSong]


    class hasVocalist(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class hasGuitarist(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class hasBassist(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class hasDrummer(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class firstReleaseFeaturingVocalist(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class firstReleaseFeaturingBassist(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class firstReleaseFeaturingDrummer(ObjectProperty):
        domain = [Album]
        range = [Musician]


    class onlyOriginalMemberFromDebutAlbumFeatured(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Musician]


    class musicalDirectionStatementBy(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Musician]


    class studioAlbumNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]


    class stylisticDifferenceDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]


    class absentMusicalElementsDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]


    class heavinessTechnicalityDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]


    class musicalDirectionQuotation(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]


    class promotionalMaterialsDescription(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [str]


    class hasLyricVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]


    class hasOfficialVideo(DataProperty, FunctionalProperty):
        domain = [Song]
        range = [bool]


    becomingTheArchetype = HeavyMetalBand("BecomingTheArchetypeBand")
    becomingTheArchetype.label = "Becoming the Archetype"

    iAm = StudioAlbum("IAmAlbum")
    iAm.label = "I Am"
    iAm.releasedByBand = becomingTheArchetype
    iAm.studioAlbumNumber = 5
    iAm.stylisticDifferenceDescription = "a departure from the previous effort"
    iAm.absentMusicalElementsDescription = "gone are the sitars and horns of Celestial Completion"
    iAm.heavinessTechnicalityDescription = "an album full of the heaviest and most technical songs we've ever written"
    iAm.musicalDirectionQuotation = "gone are the sitars and horns of Celestial Completion. Instead, we've crafted an album full of the heaviest and most technical songs we've ever written."
    solidStateRecords = RecordLabel("SolidStateRecordsLabel")
    solidStateRecords.label = "Solid State Records"
    iAm.releasedThrough = solidStateRecords

    celestialCompletion = StudioAlbum("CelestialCompletionAlbum")
    celestialCompletion.label = "Celestial Completion"
    iAm.previousAlbum = celestialCompletion

    sethHecox = Musician("SethHecoxMusician")
    sethHecox.label = "Seth Hecox"
    iAm.hasVocalist.append(sethHecox)
    iAm.hasGuitarist.append(sethHecox)
    iAm.onlyOriginalMemberFromDebutAlbumFeatured = sethHecox
    iAm.musicalDirectionStatementBy = sethHecox

    chrisMcCane = Musician("ChrisMcCaneMusician")
    chrisMcCane.label = "Chris McCane"
    iAm.hasVocalist.append(chrisMcCane)
    iAm.firstReleaseFeaturingVocalist.append(chrisMcCane)

    codeyWatkins = Musician("CodeyWatkinsMusician")
    codeyWatkins.label = "Codey Watkins"
    iAm.hasBassist.append(codeyWatkins)
    iAm.firstReleaseFeaturingBassist.append(codeyWatkins)

    chrisHeaton = Musician("ChrisHeatonMusician")
    chrisHeaton.label = "Chris Heaton"
    iAm.hasDrummer.append(chrisHeaton)
    iAm.firstReleaseFeaturingDrummer.append(chrisHeaton)

    may21 = CalendarDate("May21Date")
    may21.label = "May 21"
    iAm.recordingStartDate = may21

    june17 = CalendarDate("June17Date")
    june17.label = "June 17"
    iAm.recordingEndDate = june17

    september182012 = CalendarDate("September182012Date")
    september182012.label = "September 18 , 2012"
    iAm.releasedOn = september182012

    theTimeBender = SingleSong("TheTimeBenderSingle")
    theTimeBender.label = "The Time Bender"
    theTimeBender.promotesAlbum = iAm
    theTimeBender.promotionalMaterialsDescription = "a lyric video and an official video"
    theTimeBender.hasLyricVideo = True
    theTimeBender.hasOfficialVideo = True
    iAm.firstSingle = theTimeBender

    august282012 = CalendarDate("August282012Date")
    august282012.label = "August 28 , 2012"
    theTimeBender.releasedOn = august282012


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
