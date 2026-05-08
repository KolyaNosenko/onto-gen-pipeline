"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the title of the fifth studio album by Becoming the Archetype?
2. When was the album "I Am" released?
3. Which record label released the album "I Am"?
4. During what time period was the album "I Am" recorded?
5. What musical elements were absent from "I Am" compared to the previous album?
6. What was the name of the previous album by Becoming the Archetype before "I Am"?
7. Who provided vocals on the album "I Am"?
8. Who played bass on the album "I Am"?
9. Who played drums on the album "I Am"?
10. Which member of Becoming the Archetype is the only original member featured on "I Am"?
11. What instrument does Seth Hecox play?
12. What was the first single released to promote the album "I Am"?
13. When was the first single from "I Am" released?
14. What types of promotional media were released alongside the first single?
15. How does "I Am" differ stylistically from the band's previous album?
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
    # ── Entity classes ───────────────────────────────────────────────────────
    class MusicGroup(Thing): pass
    class HeavyMetalBand(MusicGroup): pass
    class Album(Thing): pass
    class StudioAlbum(Album): pass
    class Song(Thing): pass
    class Single(Song): pass
    class RecordLabel(Thing): pass
    class Person(Thing): pass
    class Musician(Person): pass
    class PromotionalMedia(Thing): pass
    class LyricVideo(PromotionalMedia): pass
    class OfficialVideo(PromotionalMedia): pass
    class MusicalInstrument(Thing): pass

    # ── Object properties ────────────────────────────────────────────────────
    class performedBy(ObjectProperty):
        domain = [Album]
        range = [MusicGroup]

    class releasedThrough(ObjectProperty):
        domain = [Album]
        range = [RecordLabel]

    class hasPreviousAlbum(ObjectProperty):
        domain = [Album]
        range = [Album]

    class featuresMusician(ObjectProperty):
        domain = [Album]
        range = [Musician]

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

    class hasFirstSingle(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [Single]

    class promotesAlbum(ObjectProperty):
        domain = [Single]
        range = [Album]

    class hasPromotionalMedia(ObjectProperty):
        domain = [Single]
        range = [PromotionalMedia]

    class playsInstrument(ObjectProperty):
        domain = [Musician]
        range = [MusicalInstrument]

    class memberOf(ObjectProperty):
        domain = [Musician]
        range = [MusicGroup]

    class isOriginalMemberOf(ObjectProperty):
        domain = [Musician]
        range = [MusicGroup]

    class featuresInstrument(ObjectProperty):
        domain = [Album]
        range = [MusicalInstrument]

    # ── Data properties ──────────────────────────────────────────────────────
    class albumNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class recordingStartDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class recordingEndDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [str]

    class singleReleaseDate(DataProperty, FunctionalProperty):
        domain = [Single]
        range = [str]

    # ── Named individuals ────────────────────────────────────────────────────

    # Band
    becoming_the_archetype = HeavyMetalBand("Becoming_the_Archetype")
    becoming_the_archetype.label = "Becoming the Archetype"

    # Albums
    i_am = StudioAlbum("I_Am")
    i_am.label = "I Am"

    celestial_completion = Album("Celestial_Completion")
    celestial_completion.label = "Celestial Completion"

    # Record label
    solid_state_records = RecordLabel("Solid_State_Records")
    solid_state_records.label = "Solid State Records"

    # Musicians
    chris_mccane = Musician("Chris_McCane")
    chris_mccane.label = "Chris McCane"

    codey_watkins = Musician("Codey_Watkins")
    codey_watkins.label = "Codey Watkins"

    chris_heaton = Musician("Chris_Heaton")
    chris_heaton.label = "Chris Heaton"

    seth_hecox = Musician("Seth_Hecox")
    seth_hecox.label = "Seth Hecox"

    # Single
    the_time_bender = Single("The_Time_Bender")
    the_time_bender.label = "The Time Bender"

    # Instruments mentioned in the text
    vocals_inst = MusicalInstrument("vocals")
    vocals_inst.label = "vocals"

    bass_inst = MusicalInstrument("bass")
    bass_inst.label = "bass"

    drums_inst = MusicalInstrument("drums")
    drums_inst.label = "drums"

    guitar_inst = MusicalInstrument("guitar")
    guitar_inst.label = "guitar"

    sitars_inst = MusicalInstrument("sitars")
    sitars_inst.label = "sitars"

    horns_inst = MusicalInstrument("horns")
    horns_inst.label = "horns"

    # Promotional media released with the first single (mentioned but unnamed)
    lyric_video = LyricVideo("LyricVideoForTheTimeBender")
    lyric_video.label = "lyric video"

    official_video = OfficialVideo("OfficialVideoForTheTimeBender")
    official_video.label = "official video"

    # ── Facts ────────────────────────────────────────────────────────────────

    # I Am
    i_am.albumNumber = 5
    i_am.performedBy = [becoming_the_archetype]
    i_am.releasedThrough = [solid_state_records]
    i_am.releaseDate = "September 18, 2012"
    i_am.recordingStartDate = "May 21"
    i_am.recordingEndDate = "June 17"
    i_am.hasPreviousAlbum = [celestial_completion]
    i_am.hasVocalist = [chris_mccane, seth_hecox]
    i_am.hasBassist = [codey_watkins]
    i_am.hasDrummer = [chris_heaton]
    i_am.hasGuitarist = [seth_hecox]
    i_am.featuresMusician = [chris_mccane, codey_watkins, chris_heaton, seth_hecox]
    i_am.hasFirstSingle = the_time_bender

    # Celestial Completion
    celestial_completion.performedBy = [becoming_the_archetype]
    celestial_completion.featuresInstrument = [sitars_inst, horns_inst]

    # The Time Bender single
    the_time_bender.singleReleaseDate = "August 28, 2012"
    the_time_bender.promotesAlbum = [i_am]
    the_time_bender.hasPromotionalMedia = [lyric_video, official_video]

    # Musicians
    chris_mccane.playsInstrument = [vocals_inst]
    chris_mccane.memberOf = [becoming_the_archetype]

    codey_watkins.playsInstrument = [bass_inst]
    codey_watkins.memberOf = [becoming_the_archetype]

    chris_heaton.playsInstrument = [drums_inst]
    chris_heaton.memberOf = [becoming_the_archetype]

    seth_hecox.playsInstrument = [guitar_inst, vocals_inst]
    seth_hecox.memberOf = [becoming_the_archetype]
    seth_hecox.isOriginalMemberOf = [becoming_the_archetype]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
