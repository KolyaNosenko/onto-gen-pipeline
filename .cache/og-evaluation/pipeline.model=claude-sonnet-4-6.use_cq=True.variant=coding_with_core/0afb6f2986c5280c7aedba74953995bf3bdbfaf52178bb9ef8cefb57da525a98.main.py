"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the title of the fifth studio album by Becoming the Archetype?
2. When was the album "I Am" released?
3. Which record label released the album "I Am"?
4. Between which dates was the album "I Am" recorded?
5. What distinguishes "I Am" from the previous album "Celestial Completion"?
6. Who provided vocals on the album "I Am"?
7. Who played bass on the album "I Am"?
8. Who played drums on the album "I Am"?
9. Which member of Becoming the Archetype is the only original member featured on "I Am"?
10. What instrument does Seth Hecox play?
11. What was the first single released to promote the album "I Am"?
12. When was the first single from "I Am" released?
13. What type of video was released alongside the first single?
14. What genre of music does Becoming the Archetype play?
15. How does Seth Hecox describe the musical style of "I Am" compared to previous albums?
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
)


with core:
    # ── Entity classes ──────────────────────────────────────────────────────

    # Individual musicians (persons)
    class Musician(AgentivePhysicalObject):
        pass

    class Vocalist(Musician):
        pass

    class Guitarist(Musician):
        pass

    class Bassist(Musician):
        pass

    class Drummer(Musician):
        pass

    class GuitaristVocalist(Guitarist, Vocalist):
        pass

    # Music organisations
    class MusicBand(Society):
        pass

    class RecordLabel(Society):
        pass

    # Musical works
    class MusicalWork(NonAgentiveSocialObject):
        pass

    class StudioAlbum(MusicalWork):
        pass

    class Song(MusicalWork):
        pass

    class Single(Song):
        pass

    # Music genre
    class MusicGenre(NonAgentiveSocialObject):
        pass

    # Music videos
    class MusicVideo(NonAgentiveSocialObject):
        pass

    class LyricVideo(MusicVideo):
        pass

    class OfficialVideo(MusicVideo):
        pass

    # ── Properties ──────────────────────────────────────────────────────────

    class recordedBy(ObjectProperty):
        domain = [StudioAlbum]
        range  = [MusicBand]

    class releasedBy(ObjectProperty):
        domain = [StudioAlbum]
        range  = [RecordLabel]

    class albumSequenceNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range  = [int]

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [MusicalWork]
        range  = [str]

    class recordingStartDate(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range  = [str]

    class recordingEndDate(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range  = [str]

    class hasMember(ObjectProperty):
        domain = [MusicBand]
        range  = [Musician]

    class hasVocalist(ObjectProperty):
        domain = [StudioAlbum]
        range  = [Vocalist]

    class hasBassist(ObjectProperty):
        domain = [StudioAlbum]
        range  = [Bassist]

    class hasDrummer(ObjectProperty):
        domain = [StudioAlbum]
        range  = [Drummer]

    class hasGuitaristVocalist(ObjectProperty):
        domain = [StudioAlbum]
        range  = [GuitaristVocalist]

    class hasOriginalMember(ObjectProperty):
        domain = [StudioAlbum]
        range  = [Musician]

    class playsInstrument(DataProperty):
        domain = [Musician]
        range  = [str]

    class hasGenre(ObjectProperty):
        domain = [MusicBand]
        range  = [MusicGenre]

    class promotedBy(ObjectProperty):
        domain = [StudioAlbum]
        range  = [Single]

    class hasAssociatedVideo(ObjectProperty):
        domain = [Single]
        range  = [MusicVideo]

    class departsFrom(ObjectProperty):
        domain = [StudioAlbum]
        range  = [StudioAlbum]

    # ── Named individuals ────────────────────────────────────────────────────

    # Albums
    i_am = StudioAlbum("IAm")
    i_am.label = "I Am"
    i_am.albumSequenceNumber = 5
    i_am.releaseDate = "September 18, 2012"
    i_am.recordingStartDate = "May 21"
    i_am.recordingEndDate = "June 17"

    celestial = StudioAlbum("CelestialCompletion")
    celestial.label = "Celestial Completion"

    # Band and label
    becoming = MusicBand("BecomingTheArchetype")
    becoming.label = "Becoming the Archetype"

    solid_state = RecordLabel("SolidStateRecords")
    solid_state.label = "Solid State Records"

    # Musicians
    seth = GuitaristVocalist("SethHecox")
    seth.label = "Seth Hecox"
    seth.playsInstrument.append("guitar")
    seth.playsInstrument.append("vocals")

    chris_mc = Vocalist("ChrisMcCane")
    chris_mc.label = "Chris McCane"
    chris_mc.playsInstrument.append("vocals")

    codey = Bassist("CodeyWatkins")
    codey.label = "Codey Watkins"
    codey.playsInstrument.append("bass")

    chris_h = Drummer("ChrisHeaton")
    chris_h.label = "Chris Heaton"
    chris_h.playsInstrument.append("drums")

    # Genre
    heavy_metal = MusicGenre("HeavyMetal")
    heavy_metal.label = "heavy metal"

    # Single
    time_bender = Single("TheTimeBender")
    time_bender.label = "The Time Bender"
    time_bender.releaseDate = "August 28, 2012"

    # Videos (unnamed; type captures the textual fact)
    lyric_video = LyricVideo()
    official_video = OfficialVideo()

    # ── Relations ────────────────────────────────────────────────────────────

    i_am.recordedBy.append(becoming)
    i_am.releasedBy.append(solid_state)
    i_am.departsFrom.append(celestial)
    i_am.hasVocalist.append(chris_mc)
    i_am.hasBassist.append(codey)
    i_am.hasDrummer.append(chris_h)
    i_am.hasGuitaristVocalist.append(seth)
    i_am.hasOriginalMember.append(seth)
    i_am.promotedBy.append(time_bender)

    becoming.hasMember.append(seth)
    becoming.hasMember.append(chris_mc)
    becoming.hasMember.append(codey)
    becoming.hasMember.append(chris_h)
    becoming.hasGenre.append(heavy_metal)

    time_bender.hasAssociatedVideo.append(lyric_video)
    time_bender.hasAssociatedVideo.append(official_video)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
