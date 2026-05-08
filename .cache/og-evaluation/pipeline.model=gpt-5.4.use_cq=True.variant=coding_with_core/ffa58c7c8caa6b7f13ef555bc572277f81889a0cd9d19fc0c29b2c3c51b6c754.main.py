"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

What is Kristian Matsson’s stage name?
When was Kristian Matsson born?
Where is Kristian Matsson from?
In which region of Sweden did Kristian Matsson originate?
Where did Kristian Matsson grow up?
What is Kristian Matsson’s profession?
When did Kristian Matsson begin his solo career?
Which band was Kristian Matsson a member of before starting his solo career?
What role did Kristian Matsson have in the band Montezumas?
How has Kristian Matsson’s music been compared to Bob Dylan’s music?
How many full-length albums has Kristian Matsson released since 2006?
How many EPs has Kristian Matsson released since 2006?
Where does Kristian Matsson record and produce his music?
How does Kristian Matsson usually record his voice and guitar?
What is Kristian Matsson known for among critics and fans?
Who was Kristian Matsson previously married to?
What is Amanda Bergman’s stage name?
What music did Kristian Matsson and Amanda Bergman write together?
For which film did Kristian Matsson and Amanda Bergman write music?
What is the title of the Swedish drama film for which Kristian Matsson and Amanda Bergman wrote the music?
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
    AbstractQuality,
    AgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Person(AgentivePhysicalObject):
        pass


    class MusicArtist(Person):
        pass


    class Singer(MusicArtist):
        pass


    class SingerSongwriter(Singer):
        pass


    class Band(Society):
        pass


    class IndieBand(Band):
        pass


    class Name(NonAgentiveSocialObject):
        pass


    class StageName(Name):
        pass


    class Place(SpaceRegion):
        pass


    class Country(Place):
        pass


    class GeographicRegion(Place):
        pass


    class Town(Place):
        pass


    class CreativeWork(NonAgentiveSocialObject):
        pass


    class MusicWork(CreativeWork):
        pass


    class MusicRelease(MusicWork):
        pass


    class FullLengthAlbum(MusicRelease):
        pass


    class ExtendedPlay(MusicRelease):
        pass


    class Film(CreativeWork):
        pass


    class DramaFilm(Film):
        pass


    class SwedishDramaFilm(DramaFilm):
        pass


    class StagePresence(AbstractQuality):
        pass


    class CalendarDate(TimeInterval):
        pass


    class CalendarYear(TimeInterval):
        pass


    class locatedIn(partOf):
        domain = [Place]
        range = [Place]


    class hasStageName(ObjectProperty):
        domain = [MusicArtist]
        range = [StageName]


    class bornOn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]


    class originatesFrom(ObjectProperty):
        domain = [Person]
        range = [Place]


    class grewUpIn(ObjectProperty):
        domain = [Person]
        range = [Place]


    class soloCareerStartedOn(ObjectProperty, FunctionalProperty):
        domain = [MusicArtist]
        range = [TimeInterval]


    class memberOfBand(ObjectProperty):
        domain = [MusicArtist]
        range = [Band]


    class leadSingerOf(ObjectProperty):
        domain = [Singer]
        range = [Band]


    class musicComparedToArtist(ObjectProperty):
        domain = [MusicArtist]
        range = [MusicArtist]


    class fullLengthAlbumsReleasedSince(DataProperty, FunctionalProperty):
        domain = [MusicArtist]
        range = [int]


    class epsReleasedSince(DataProperty, FunctionalProperty):
        domain = [MusicArtist]
        range = [int]


    class recordsAndProducesAtDescription(DataProperty, FunctionalProperty):
        domain = [MusicArtist]
        range = [str]


    class usualRecordingMethod(DataProperty, FunctionalProperty):
        domain = [MusicArtist]
        range = [str]


    class knownForDescription(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]


    class previouslyMarriedTo(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]


    class coWroteMusicWith(ObjectProperty, SymmetricProperty):
        domain = [MusicArtist]
        range = [MusicArtist]


    class wroteMusicFor(ObjectProperty):
        domain = [MusicArtist]
        range = [Film]


    KristianMatsson = SingerSongwriter("KristianMatsson")
    KristianMatsson.label = "Kristian Matsson"

    TheTallestManOnEarth = StageName("TheTallestManOnEarth")
    TheTallestManOnEarth.label = "The Tallest Man on Earth"

    April301983 = CalendarDate("Date30April1983")
    April301983.label = "30 April 1983"

    Dalarna = GeographicRegion("Dalarna")
    Dalarna.label = "Dalarna"

    Sweden = Country("Sweden")
    Sweden.label = "Sweden"

    Leksand = Town("Leksand")
    Leksand.label = "Leksand"

    Year2006 = CalendarYear("Year2006")
    Year2006.label = "2006"

    Montezumas = IndieBand("Montezumas")
    Montezumas.label = "Montezumas"

    BobDylan = MusicArtist("BobDylan")
    BobDylan.label = "Bob Dylan"

    AmandaBergman = MusicArtist("AmandaBergman")
    AmandaBergman.label = "Amanda Bergman"

    IdiotWind = StageName("IdiotWind")
    IdiotWind.label = "Idiot Wind"

    OnceAYear = SwedishDramaFilm("OnceAYear")
    OnceAYear.label = "Once a Year"

    Dalarna.locatedIn = [Sweden]
    Leksand.locatedIn = [Dalarna]

    KristianMatsson.hasStageName = [TheTallestManOnEarth]
    KristianMatsson.bornOn = April301983
    KristianMatsson.originatesFrom = [Dalarna, Sweden]
    KristianMatsson.grewUpIn = [Leksand]
    KristianMatsson.soloCareerStartedOn = Year2006
    KristianMatsson.memberOfBand = [Montezumas]
    KristianMatsson.leadSingerOf = [Montezumas]
    KristianMatsson.musicComparedToArtist = [BobDylan]
    KristianMatsson.fullLengthAlbumsReleasedSince = 4
    KristianMatsson.epsReleasedSince = 2
    KristianMatsson.recordsAndProducesAtDescription = "his home"
    KristianMatsson.usualRecordingMethod = "records his voice and guitar together on one track"
    KristianMatsson.knownForDescription = "charismatic stage presence"
    KristianMatsson.previouslyMarriedTo = [AmandaBergman]
    KristianMatsson.coWroteMusicWith = [AmandaBergman]
    KristianMatsson.wroteMusicFor = [OnceAYear]

    AmandaBergman.hasStageName = [IdiotWind]
    AmandaBergman.previouslyMarriedTo = [KristianMatsson]
    AmandaBergman.coWroteMusicWith = [KristianMatsson]
    AmandaBergman.wroteMusicFor = [OnceAYear]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
