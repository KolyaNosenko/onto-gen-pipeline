"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

1. What is the real name of the artist who performs under the stage name The Tallest Man on Earth?
2. When was Kristian Matsson born?
3. Where is Kristian Matsson from?
4. Where did Kristian Matsson grow up?
5. What is Kristian Matsson’s profession?
6. Under what stage name does Kristian Matsson perform?
7. In what year did Kristian Matsson begin his solo career?
8. What band was Kristian Matsson previously the lead singer of?
9. What artists is Kristian Matsson’s music often compared to?
10. How many full-length albums has Kristian Matsson released since 2006?
11. How many EPs has Kristian Matsson released since 2006?
12. Where does Kristian Matsson record and produce his music?
13. How does Kristian Matsson usually record his voice and guitar?
14. What is Kristian Matsson known for among critics and fans?
15. Who was Kristian Matsson previously married to?
16. What is Amanda Bergman’s stage name?
17. What music did Kristian Matsson and Amanda Bergman write together?
18. What Swedish drama film did Kristian Matsson and Amanda Bergman write music for?
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
    class Person(Thing):
        pass

    class Artist(Person):
        pass

    class Singer(Artist):
        pass

    class Songwriter(Artist):
        pass

    class SingerSongwriter(Artist):
        equivalent_to = [Singer & Songwriter]

    class Place(Thing):
        pass

    class Country(Place):
        pass

    class Region(Place):
        pass

    class Locality(Place):
        pass

    class Band(Thing):
        pass

    class IndieBand(Band):
        pass

    class MusicalRelease(Thing):
        pass

    class Album(MusicalRelease):
        pass

    class EP(MusicalRelease):
        pass

    class StageName(Thing):
        pass

    class Film(Thing):
        pass

    class DramaFilm(Film):
        pass

    class hasBirthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [date]

    class fromPlace(ObjectProperty):
        domain = [Person]
        range = [Place]

    class grewUpIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class stageName(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [StageName]

    class beganSoloCareerYear(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]

    class leadSingerOf(ObjectProperty):
        domain = [Person]
        range = [Band]

    class musicComparedToArtist(ObjectProperty):
        domain = [Person]
        range = [Artist]

    class releasedFullLengthAlbumsCount(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]

    class releasedEPsCount(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]

    class recordsAndProducesIn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class recordsVoiceAndGuitarTogetherOn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class knownFor(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class previousSpouse(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]

    class wroteMusicFor(ObjectProperty):
        domain = [Person]
        range = [Film]

    kristianMatsson = SingerSongwriter("KristianMatsson")
    kristianMatsson.label = "Kristian Matsson"
    kristianMatsson.hasBirthDate = date(1983, 4, 30)
    kristianMatsson.beganSoloCareerYear = 2006
    kristianMatsson.releasedFullLengthAlbumsCount = 4
    kristianMatsson.releasedEPsCount = 2
    kristianMatsson.recordsAndProducesIn = "his home"
    kristianMatsson.recordsVoiceAndGuitarTogetherOn = "one track"
    kristianMatsson.knownFor = "charismatic stage presence"

    dalarna = Region("Dalarna")
    dalarna.label = "Dalarna"

    sweden = Country("Sweden")
    sweden.label = "Sweden"

    leksand = Locality("Leksand")
    leksand.label = "Leksand"

    theTallestManOnEarth = StageName("TheTallestManOnEarth")
    theTallestManOnEarth.label = "The Tallest Man on Earth"

    montezumas = IndieBand("Montezumas")
    montezumas.label = "Montezumas"

    bobDylan = Artist("BobDylan")
    bobDylan.label = "Bob Dylan"

    amandaBergman = Person("AmandaBergman")
    amandaBergman.label = "Amanda Bergman"

    idiotWind = StageName("IdiotWind")
    idiotWind.label = "Idiot Wind"

    onceAYear = DramaFilm("OnceAYear")
    onceAYear.label = "Once a Year"

    kristianMatsson.fromPlace = [dalarna, sweden]
    kristianMatsson.grewUpIn = [leksand]
    kristianMatsson.stageName = theTallestManOnEarth
    kristianMatsson.leadSingerOf = [montezumas]
    kristianMatsson.musicComparedToArtist = [bobDylan]
    kristianMatsson.previousSpouse = [amandaBergman]
    kristianMatsson.wroteMusicFor = [onceAYear]

    amandaBergman.previousSpouse = [kristianMatsson]
    amandaBergman.stageName = idiotWind
    amandaBergman.wroteMusicFor = [onceAYear]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
