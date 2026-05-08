"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the fifth studio album of Becoming the Archetype?
2. Which band recorded and released the album I Am?
3. Between which dates was I Am recorded?
4. On what date was I Am released?
5. Which record label released I Am?
6. How did Seth Hecox describe the musical departure of I Am from the previous album?
7. Which instruments or musical elements were present on Celestial Completion but absent from I Am?
8. Which songs or characteristics were used to describe the style of I Am?
9. Which album was the previous effort before I Am?
10. Which release of Becoming the Archetype first featured Chris McCane on vocals?
11. Which release of Becoming the Archetype first featured Codey Watkins on bass?
12. Which release of Becoming the Archetype first featured Chris Heaton on drums?
13. Which original member from the debut album is featured on I Am?
14. What was the first single released to promote I Am?
15. On what date was “The Time Bender” released?
16. What promotional media were released alongside “The Time Bender”?
17. Who is the vocalist and guitarist credited on I Am?
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
    NonPhysicalObject,
    Society,
    TimeInterval,
)


with core:
    class Album(NonPhysicalObject):
        pass

    class StudioAlbum(Album):
        pass

    class Song(NonPhysicalObject):
        pass

    class Single(Song):
        pass

    class PromotionalMedia(NonPhysicalObject):
        pass

    class MusicVideo(PromotionalMedia):
        pass

    class MusicalElement(NonPhysicalObject):
        pass

    class Musician(AgentivePhysicalObject):
        pass

    class Vocalist(Musician):
        pass

    class Bassist(Musician):
        pass

    class Drummer(Musician):
        pass

    class GuitaristVocalist(Musician):
        pass

    class Band(Society):
        pass

    class RecordLabel(Society):
        pass

    class byBand(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Band]

    class recordedBetween(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [TimeInterval]

    class releasedOn(ObjectProperty, FunctionalProperty):
        domain = [Album, Single]
        range = [TimeInterval]

    class releasedThrough(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [RecordLabel]

    class previousEffort(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Album]

    class firstSingle(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Single]

    class promotesAlbum(ObjectProperty, FunctionalProperty):
        domain = [Single]
        range = [Album]

    class promotionalMedia(ObjectProperty):
        domain = [Single]
        range = [PromotionalMedia]

    class containsMusicalElement(ObjectProperty):
        domain = [Album]
        range = [MusicalElement]

    class firstReleaseToFeatureVocals(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Vocalist]

    class firstReleaseToFeatureBass(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Bassist]

    class firstReleaseToFeatureDrums(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Drummer]

    class featuredGuitaristVocalist(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [GuitaristVocalist]

    class featuredOriginalMemberFromDebutAlbum(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Musician]

    class describedDepartureAs(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [str]

    class describedStyleAs(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [str]

    class studioAlbumNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class departureDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class styleDescription(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]


    BecomingTheArchetype = Band("BecomingTheArchetype")
    BecomingTheArchetype.label = "Becoming the Archetype"



    SolidStateRecords = RecordLabel("SolidStateRecords")
    SolidStateRecords.label = "Solid State Records"

    IAm = StudioAlbum("IAm")
    IAm.label = "I Am"
    IAm.studioAlbumNumber = 5
    IAm.byBand = BecomingTheArchetype
    IAm.releasedThrough = SolidStateRecords

    IAm.departureDescription = (
        "gone are the sitars and horns of Celestial Completion. Instead, we've crafted "
        "an album full of the heaviest and most technical songs we've ever written."
    )
    IAm.styleDescription = "the heaviest and most technical songs we've ever written"


    CelestialCompletion = StudioAlbum("CelestialCompletion")
    CelestialCompletion.label = "Celestial Completion"
    CelestialCompletion.byBand = BecomingTheArchetype

    SethHecox = GuitaristVocalist("SethHecox")
    SethHecox.label = "Seth Hecox"
    SethHecox.describedDepartureAs = (
        "gone are the sitars and horns of Celestial Completion. Instead, we've crafted "
        "an album full of the heaviest and most technical songs we've ever written."
    )
    SethHecox.describedStyleAs = "the heaviest and most technical songs we've ever written"

    ChrisMcCane = Vocalist("ChrisMcCane")
    ChrisMcCane.label = "Chris McCane"

    CodeyWatkins = Bassist("CodeyWatkins")
    CodeyWatkins.label = "Codey Watkins"

    ChrisHeaton = Drummer("ChrisHeaton")
    ChrisHeaton.label = "Chris Heaton"

    May21June17RecordingInterval = TimeInterval("May21June17RecordingInterval")
    May21June17RecordingInterval.label = "May 21 and June 17"
    IAm.recordedBetween = May21June17RecordingInterval

    September182012ReleaseDate = TimeInterval("September182012ReleaseDate")
    September182012ReleaseDate.label = "September 18, 2012"
    IAm.releasedOn = September182012ReleaseDate

    August282012ReleaseDate = TimeInterval("August282012ReleaseDate")
    August282012ReleaseDate.label = "August 28, 2012"

    Sitars = MusicalElement("Sitars")
    Sitars.label = "sitars"
    CelestialCompletion.containsMusicalElement.append(Sitars)

    Horns = MusicalElement("Horns")
    Horns.label = "horns"
    CelestialCompletion.containsMusicalElement.append(Horns)

    TheTimeBender = Single("TheTimeBender")
    TheTimeBender.label = "The Time Bender"
    TheTimeBender.promotesAlbum = IAm
    TheTimeBender.releasedOn = August282012ReleaseDate

    LyricVideoPromotionalMedia = MusicVideo("LyricVideoPromotionalMedia")
    LyricVideoPromotionalMedia.label = "lyric video"
    TheTimeBender.promotionalMedia.append(LyricVideoPromotionalMedia)

    OfficialVideoPromotionalMedia = MusicVideo("OfficialVideoPromotionalMedia")
    OfficialVideoPromotionalMedia.label = "official video"
    TheTimeBender.promotionalMedia.append(OfficialVideoPromotionalMedia)

    IAm.firstSingle = TheTimeBender
    IAm.previousEffort = CelestialCompletion
    IAm.firstReleaseToFeatureVocals = ChrisMcCane
    IAm.firstReleaseToFeatureBass = CodeyWatkins
    IAm.firstReleaseToFeatureDrums = ChrisHeaton
    IAm.featuredGuitaristVocalist = SethHecox
    IAm.featuredOriginalMemberFromDebutAlbum = SethHecox


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
