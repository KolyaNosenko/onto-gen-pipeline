"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

What is Kristian Matsson’s date of birth?
What is Kristian Matsson’s place of origin?
What stage name does Kristian Matsson perform under?
In which region or country is Kristian Matsson from?
Where did Kristian Matsson grow up?
When did Kristian Matsson begin his solo career?
What band was Kristian Matsson a member of before starting his solo career?
What role did Kristian Matsson have in the band Montezumas?
Which artist’s music is Kristian Matsson’s music often compared to?
How many full-length albums has Kristian Matsson released since 2006?
How many EPs has Kristian Matsson released since 2006?
Where does Kristian Matsson record and produce his music?
How does Kristian Matsson usually record his voice and guitar?
What is Kristian Matsson known for among critics and fans?
Who was Kristian Matsson previously married to?
What is Amanda Bergman’s stage name?
What work did Kristian Matsson and Amanda Bergman create together?
For which film did Kristian Matsson and Amanda Bergman write the music?
What genre or profession is Kristian Matsson associated with?
Is Kristian Matsson also known as The Tallest Man on Earth?
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

    class MusicalArtist(Person):
        pass

    class Singer(MusicalArtist):
        pass

    class SingerSongwriter(Singer):
        pass

    class Band(Thing):
        pass

    class IndieBand(Band):
        pass

    class Place(Thing):
        pass

    class Region(Place):
        pass

    class Country(Place):
        pass

    class Town(Place):
        pass

    class StageName(Thing):
        pass

    class TimePoint(Thing):
        pass

    class DatePoint(TimePoint):
        pass

    class Year(TimePoint):
        pass

    class CreativeWork(Thing):
        pass

    class MusicRelease(CreativeWork):
        pass

    class FullLengthAlbum(MusicRelease):
        pass

    class ExtendedPlay(MusicRelease):
        pass

    class Film(CreativeWork):
        pass

    class DramaFilm(Film):
        pass

    class bornOn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [DatePoint]

    class placeOfOrigin(ObjectProperty):
        domain = [Person]
        range = [Place]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class hasStageName(ObjectProperty):
        domain = [MusicalArtist]
        range = [StageName]

    class grewUpIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class beganSoloCareerIn(ObjectProperty, FunctionalProperty):
        domain = [MusicalArtist]
        range = [Year]

    class leadSingerOf(ObjectProperty):
        domain = [Singer]
        range = [Band]

    class musicComparedToArtist(ObjectProperty):
        domain = [MusicalArtist]
        range = [MusicalArtist]

    class fullLengthAlbumCountSince2006(DataProperty, FunctionalProperty):
        domain = [MusicalArtist]
        range = [int]

    class epCountSince2006(DataProperty, FunctionalProperty):
        domain = [MusicalArtist]
        range = [int]

    class recordingAndProductionLocationDescription(DataProperty, FunctionalProperty):
        domain = [MusicalArtist]
        range = [str]

    class usualRecordingMethodDescription(DataProperty, FunctionalProperty):
        domain = [MusicalArtist]
        range = [str]

    class knownForDescription(DataProperty):
        domain = [Person]
        range = [str]

    class previouslyMarriedTo(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]

    class wroteMusicFor(ObjectProperty):
        domain = [Person]
        range = [Film]

    KristianMatsson = SingerSongwriter("KristianMatsson")
    KristianMatsson.label = ["Kristian Matsson", "Matsson"]

    Date30April1983 = DatePoint("Date30April1983")
    Date30April1983.label = "30 April 1983"

    Dalarna = Region("Dalarna")
    Dalarna.label = "Dalarna"

    Sweden = Country("Sweden")
    Sweden.label = "Sweden"

    TheTallestManOnEarth = StageName("TheTallestManOnEarth")
    TheTallestManOnEarth.label = "The Tallest Man on Earth"

    Leksand = Town("Leksand")
    Leksand.label = "Leksand"

    Year2006 = Year("Year2006")
    Year2006.label = "2006"

    Montezumas = IndieBand("Montezumas")
    Montezumas.label = "Montezumas"

    BobDylan = MusicalArtist("BobDylan")
    BobDylan.label = "Bob Dylan"

    AmandaBergman = MusicalArtist("AmandaBergman")
    AmandaBergman.label = "Amanda Bergman"

    IdiotWind = StageName("IdiotWind")
    IdiotWind.label = "Idiot Wind"

    OnceAYear = DramaFilm("OnceAYear")
    OnceAYear.label = "Once a Year"

    Dalarna.locatedIn = [Sweden]

    KristianMatsson.bornOn = Date30April1983
    KristianMatsson.placeOfOrigin = [Dalarna, Sweden]
    KristianMatsson.hasStageName = [TheTallestManOnEarth]
    KristianMatsson.grewUpIn = [Leksand]
    KristianMatsson.beganSoloCareerIn = Year2006
    KristianMatsson.leadSingerOf = [Montezumas]
    KristianMatsson.musicComparedToArtist = [BobDylan]
    KristianMatsson.fullLengthAlbumCountSince2006 = 4
    KristianMatsson.epCountSince2006 = 2
    KristianMatsson.recordingAndProductionLocationDescription = "his home"
    KristianMatsson.usualRecordingMethodDescription = "records his voice and guitar together on one track"
    KristianMatsson.knownForDescription = ["charismatic stage presence"]
    KristianMatsson.previouslyMarriedTo = [AmandaBergman]
    KristianMatsson.wroteMusicFor = [OnceAYear]

    AmandaBergman.hasStageName = [IdiotWind]
    AmandaBergman.previouslyMarriedTo = [KristianMatsson]
    AmandaBergman.wroteMusicFor = [OnceAYear]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
