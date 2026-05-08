"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

1. What is Kristian Matsson’s stage name?
2. When was Kristian Matsson born?
3. Where is Kristian Matsson from?
4. Where did Kristian Matsson grow up?
5. What is Kristian Matsson’s profession?
6. In which year did Kristian Matsson begin his solo career?
7. Which band was Kristian Matsson the lead singer of before his solo career?
8. How many full-length albums has Kristian Matsson released since 2006?
9. How many EPs has Kristian Matsson released since 2006?
10. Where does Kristian Matsson record and produce his music?
11. How does Kristian Matsson usually record his voice and guitar?
12. What is Kristian Matsson known for among critics and fans?
13. Who was Kristian Matsson previously married to?
14. What is Amanda Bergman’s stage name?
15. For which film did Kristian Matsson and Amanda Bergman write the music?
16. Which artists or musicians has Kristian Matsson’s music been compared to?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from datetime import date

from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, SymmetricProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    PhysicalObject,
    NonPhysicalObject,
    SocialObject,
    Quality,
    SpaceRegion,
)


with core:
    class Person(AgentivePhysicalObject):
        pass

    class SingerSongwriter(Person):
        pass

    class LeadSinger(Person):
        pass

    class Place(SpaceRegion):
        pass

    class Country(Place):
        pass

    class GeographicRegion(Place):
        pass

    class Locality(Place):
        pass

    class StageName(NonPhysicalObject):
        pass

    class Home(PhysicalObject):
        pass

    class Track(NonPhysicalObject):
        pass

    class StagePresence(Quality):
        pass

    class Band(SocialObject):
        pass

    class IndieBand(Band):
        pass

    class MusicRelease(NonPhysicalObject):
        pass

    class Album(MusicRelease):
        pass

    class FullLengthAlbum(Album):
        pass

    class EP(MusicRelease):
        pass

    class Film(NonPhysicalObject):
        pass

    class DramaFilm(Film):
        pass

    class bornOn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [date]

    class fromPlace(ObjectProperty):
        domain = [Person]
        range = [Place]

    class grewUpIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class performsUnderStageName(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [StageName]

    class soloCareerStartYear(DataProperty, FunctionalProperty):
        domain = [SingerSongwriter]
        range = [int]

    class leadSingerOf(ObjectProperty):
        domain = [LeadSinger]
        range = [Band]

    class musicComparedTo(ObjectProperty):
        domain = [Person]
        range = [Person]

    class fullLengthAlbumCountSince2006(DataProperty, FunctionalProperty):
        domain = [SingerSongwriter]
        range = [int]

    class epCountSince2006(DataProperty, FunctionalProperty):
        domain = [SingerSongwriter]
        range = [int]

    class recordsAndProducesIn(DataProperty, FunctionalProperty):
        domain = [SingerSongwriter]
        range = [str]

    class usuallyRecordsVoiceAndGuitarTogetherOn(DataProperty, FunctionalProperty):
        domain = [SingerSongwriter]
        range = [str]

    class knownFor(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class previouslyMarriedTo(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]

    class wroteMusicFor(ObjectProperty):
        domain = [Person]
        range = [Film]

    Dalarna = GeographicRegion("Dalarna")
    Dalarna.label = "Dalarna"

    Sweden = Country("Sweden")
    Sweden.label = "Sweden"

    Leksand = Locality("Leksand")
    Leksand.label = "Leksand"

    TheTallestManOnEarth = StageName("TheTallestManOnEarth")
    TheTallestManOnEarth.label = "The Tallest Man on Earth"

    Montezumas = IndieBand("Montezumas")
    Montezumas.label = "Montezumas"

    BobDylan = Person("BobDylan")
    BobDylan.label = "Bob Dylan"

    AmandaBergman = Person("AmandaBergman")
    AmandaBergman.label = "Amanda Bergman"

    IdiotWind = StageName("IdiotWind")
    IdiotWind.label = "Idiot Wind"

    OnceAYear = DramaFilm("OnceAYear")
    OnceAYear.label = "Once a Year"

    KristianMatsson = SingerSongwriter("KristianMatsson")
    KristianMatsson.label = "Kristian Matsson"
    KristianMatsson.is_a.append(LeadSinger)
    KristianMatsson.bornOn = date(1983, 4, 30)
    KristianMatsson.fromPlace = [Dalarna, Sweden]
    KristianMatsson.grewUpIn = [Leksand]
    KristianMatsson.performsUnderStageName = TheTallestManOnEarth
    KristianMatsson.soloCareerStartYear = 2006
    KristianMatsson.leadSingerOf = [Montezumas]
    KristianMatsson.musicComparedTo = [BobDylan]
    KristianMatsson.fullLengthAlbumCountSince2006 = 4
    KristianMatsson.epCountSince2006 = 2
    KristianMatsson.recordsAndProducesIn = "his home"
    KristianMatsson.usuallyRecordsVoiceAndGuitarTogetherOn = "voice and guitar together on one track"
    KristianMatsson.knownFor = "his charismatic stage presence"
    KristianMatsson.previouslyMarriedTo = [AmandaBergman]
    KristianMatsson.wroteMusicFor = [OnceAYear]

    AmandaBergman.performsUnderStageName = IdiotWind
    AmandaBergman.previouslyMarriedTo = [KristianMatsson]
    AmandaBergman.wroteMusicFor = [OnceAYear]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
