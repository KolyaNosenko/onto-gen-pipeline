"""
=== TASK INPUT ===
Source text:
I Am is the fifth studio album by the heavy metal band Becoming the Archetype . The album was recorded between May 21 and June 17 and was released on September 18 , 2012 through Solid State Records . This album is a departure from the previous effort , as Seth Hecox says , " gone are the sitars and horns of Celestial Completion . Instead , we 've crafted an album full of the heaviest and most technical songs we 've ever written . ” It is the first release by the band to feature Chris McCane on vocals , Codey Watkins on bass , and Chris Heaton on drums . Guitarist / vocalist Seth Hecox is the only original member from the debut album featured on I Am . The first single to promote the album was the song " The Time Bender " , released on August 28 , 2012 , as well a lyric video and an official video .

1. What is the title of Becoming the Archetype's fifth studio album?
2. When was the album "I Am" released?
3. Which record label released the album "I Am"?
4. During which dates was the album "I Am" recorded?
5. Who are the band members featured on the album "I Am"?
6. What is the role of Seth Hecox in Becoming the Archetype?
7. Who is the vocalist on the album "I Am"?
8. Who is the bassist on the album "I Am"?
9. Who is the drummer on the album "I Am"?
10. Which member of Becoming the Archetype is an original member from the debut album?
11. What was the first single released to promote "I Am"?
12. When was the first single "The Time Bender" released?
13. How does the musical style of "I Am" differ from the previous album "Celestial Completion"?
14. What instruments were featured on the previous album "Celestial Completion"?
15. What promotional materials were released for "The Time Bender"?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
import datetime
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    NonPhysicalObject, SocialAgent, AgentivePhysicalObject
)

# TODO (optional): import the core properties you actually subclass.


with core:
    # Entity Classes
    class Band(SocialAgent):
        """A musical band, a collective with agency and intentions."""
        pass
    
    class Musician(AgentivePhysicalObject):
        """A person who plays musical instruments."""
        pass
    
    class Album(NonPhysicalObject):
        """A studio album, a creative work that is a collection of songs."""
        pass
    
    class Song(NonPhysicalObject):
        """A song or track on an album."""
        pass
    
    class RecordLabel(SocialAgent):
        """A record label or music company."""
        pass
    
    class PromoVideo(NonPhysicalObject):
        """A promotional video for a song or album."""
        pass

    # Object Properties
    class hasMember(ObjectProperty):
        """A band has member musicians."""
        domain = [Band]
        range = [Musician]
    
    class releasedBy(ObjectProperty, FunctionalProperty):
        """An album is released by a record label."""
        domain = [Album]
        range = [RecordLabel]
    
    class hasTrack(ObjectProperty):
        """An album has songs/tracks."""
        domain = [Album]
        range = [Song]
    
    class previousAlbum(ObjectProperty, FunctionalProperty):
        """An album's previous album (the immediately preceding one)."""
        domain = [Album]
        range = [Album]
    
    class performsVocalsOn(ObjectProperty):
        """A musician performs vocals on an album."""
        domain = [Musician]
        range = [Album]
    
    class performsBassOn(ObjectProperty):
        """A musician plays bass on an album."""
        domain = [Musician]
        range = [Album]
    
    class performsDrumsOn(ObjectProperty):
        """A musician plays drums on an album."""
        domain = [Musician]
        range = [Album]
    
    class performsGuitarOn(ObjectProperty):
        """A musician plays guitar on an album."""
        domain = [Musician]
        range = [Album]
    
    class hasPromoVideo(ObjectProperty):
        """A song has promotional videos."""
        domain = [Song]
        range = [PromoVideo]
    
    class isFirstSingleOf(ObjectProperty, FunctionalProperty):
        """A song is the first single released from an album."""
        domain = [Song]
        range = [Album]

    # Data Properties
    class albumNumber(DataProperty, FunctionalProperty):
        """The sequential number of an album (e.g., fifth album = 5)."""
        domain = [Album]
        range = [int]
    
    class releasedOn(DataProperty, FunctionalProperty):
        """The release date of an album or song."""
        domain = [Album, Song]
        range = [datetime.date]
    
    class recordedFrom(DataProperty, FunctionalProperty):
        """The start date of album recording."""
        domain = [Album]
        range = [datetime.date]
    
    class recordedTo(DataProperty, FunctionalProperty):
        """The end date of album recording."""
        domain = [Album]
        range = [datetime.date]
    
    class isOriginalMember(DataProperty, FunctionalProperty):
        """Whether a musician is an original member of a band."""
        domain = [Musician]
        range = [bool]
    
    class videoType(DataProperty, FunctionalProperty):
        """The type of promotional video (e.g., lyric, official)."""
        domain = [PromoVideo]
        range = [str]
    
    class featuresInstrument(DataProperty):
        """An instrument featured on an album."""
        domain = [Album]
        range = [str]
    
    class albumStyle(DataProperty, FunctionalProperty):
        """A description of the musical style of an album."""
        domain = [Album]
        range = [str]

    # Named Individuals
    becoming_the_archetype = Band("BecomingTheArchetype")
    becoming_the_archetype.label = "Becoming the Archetype"
    
    i_am = Album("IAm")
    i_am.label = "I Am"
    
    celestial_completion = Album("CelestialCompletion")
    celestial_completion.label = "Celestial Completion"
    
    solid_state_records = RecordLabel("SolidStateRecords")
    solid_state_records.label = "Solid State Records"
    
    seth_hecox = Musician("SethHecox")
    seth_hecox.label = "Seth Hecox"
    
    chris_mccane = Musician("ChrisMcCane")
    chris_mccane.label = "Chris McCane"
    
    codey_watkins = Musician("CodeyWatkins")
    codey_watkins.label = "Codey Watkins"
    
    chris_heaton = Musician("ChrisHeaton")
    chris_heaton.label = "Chris Heaton"
    
    the_time_bender = Song("TheTimeBender")
    the_time_bender.label = "The Time Bender"
    
    # Band membership
    becoming_the_archetype.hasMember.append(seth_hecox)
    becoming_the_archetype.hasMember.append(chris_mccane)
    becoming_the_archetype.hasMember.append(codey_watkins)
    becoming_the_archetype.hasMember.append(chris_heaton)
    
    # Album properties
    i_am.releasedBy = solid_state_records
    i_am.hasTrack.append(the_time_bender)
    i_am.previousAlbum = celestial_completion
    i_am.albumNumber = 5
    i_am.releasedOn = datetime.date(2012, 9, 18)
    i_am.recordedFrom = datetime.date(2012, 5, 21)
    i_am.recordedTo = datetime.date(2012, 6, 17)
    i_am.albumStyle = "full of the heaviest and most technical songs we've ever written"
    
    # Previous album properties
    celestial_completion.featuresInstrument.append("sitar")
    celestial_completion.featuresInstrument.append("horn")
    celestial_completion.albumStyle = "features sitars and horns"
    
    # Musician roles on I Am
    seth_hecox.performsGuitarOn.append(i_am)
    seth_hecox.performsVocalsOn.append(i_am)
    seth_hecox.isOriginalMember = True
    
    chris_mccane.performsVocalsOn.append(i_am)
    
    codey_watkins.performsBassOn.append(i_am)
    
    chris_heaton.performsDrumsOn.append(i_am)
    
    # Song properties
    the_time_bender.releasedOn = datetime.date(2012, 8, 28)
    the_time_bender.isFirstSingleOf = i_am
    
    # Promotional videos
    lyric_video = PromoVideo()
    lyric_video.videoType = "lyric"
    the_time_bender.hasPromoVideo.append(lyric_video)
    
    official_video = PromoVideo()
    official_video.videoType = "official"
    the_time_bender.hasPromoVideo.append(official_video)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
