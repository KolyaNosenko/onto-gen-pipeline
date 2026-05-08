"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

1. What is the real name of the artist who performs under the stage name "The Tallest Man on Earth"?
2. When was Kristian Matsson born?
3. Where is Kristian Matsson from?
4. In which city did Kristian Matsson grow up?
5. When did Kristian Matsson begin his solo career?
6. What band was Kristian Matsson previously a member of?
7. What role did Kristian Matsson have in his previous band?
8. Which famous musician's music is often compared to Kristian Matsson's music?
9. How many full-length albums has Kristian Matsson released since 2006?
10. How many EPs has Kristian Matsson released since 2006?
11. Where does Kristian Matsson record and produce his music?
12. How does Kristian Matsson typically record his voice and guitar?
13. What is Kristian Matsson known for among critics and fans?
14. Who was Kristian Matsson previously married to?
15. What is Amanda Bergman's stage name?
16. What did Kristian Matsson and Amanda Bergman collaborate on together?
17. What genre is the film "Once a Year" for which Kristian Matsson contributed music?
18. What is the nationality of Kristian Matsson?
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
    # ── Entity classes ──────────────────────────────────────────────
    class Person(Thing): pass
    class Musician(Person): pass
    class SingerSongwriter(Musician): pass
    class Band(Thing): pass
    class Film(Thing): pass
    class Place(Thing): pass
    class Country(Place): pass
    class Region(Place): pass
    class City(Place): pass

    # ── Object properties ───────────────────────────────────────────
    class fromPlace(ObjectProperty):
        domain = [Person]
        range  = [Place]

    class grewUpIn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range  = [City]

    class previousMemberOf(ObjectProperty):
        domain = [Musician]
        range  = [Band]

    class musicComparedTo(ObjectProperty):
        domain = [Musician]
        range  = [Musician]

    class formerSpouse(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range  = [Person]

    class composedMusicFor(ObjectProperty):
        domain = [Person]
        range  = [Film]

    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range  = [Country]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    class hasCountryOfOrigin(ObjectProperty, FunctionalProperty):
        domain = [Film]
        range  = [Country]

    # ── Data properties ─────────────────────────────────────────────
    class hasStageName(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [str]

    class birthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class soloCareerStartYear(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [int]

    class hadBandRole(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [str]

    class fullLengthAlbumCount(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [int]

    class epCount(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [int]

    class recordsAt(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [str]

    class recordingMethod(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [str]

    class knownFor(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class hasGenre(DataProperty, FunctionalProperty):
        domain = [Film]
        range  = [str]

    # ── Individuals ──────────────────────────────────────────────────
    # Places
    sweden = Country("Sweden")
    sweden.label = "Sweden"

    dalarna = Region("Dalarna")
    dalarna.label = "Dalarna"
    dalarna.locatedIn = [sweden]

    leksand = City("Leksand")
    leksand.label = "Leksand"
    leksand.locatedIn = [dalarna]

    # Band
    montezumas = Band("Montezumas")
    montezumas.label = "Montezumas"

    # Musicians
    bobDylan = Musician("BobDylan")
    bobDylan.label = "Bob Dylan"

    amandaBergman = Musician("AmandaBergman")
    amandaBergman.label = "Amanda Bergman"
    amandaBergman.hasStageName = "Idiot Wind"

    # Film
    onceAYear = Film("OnceAYear")
    onceAYear.label = "Once a Year"
    onceAYear.hasGenre = "drama"
    onceAYear.hasCountryOfOrigin = sweden

    # Main individual
    kristianMatsson = SingerSongwriter("KristianMatsson")
    kristianMatsson.label = "Kristian Matsson"
    kristianMatsson.hasStageName = "The Tallest Man on Earth"
    kristianMatsson.birthDate = "30 April 1983"
    kristianMatsson.fromPlace = [dalarna]
    kristianMatsson.hasNationality = sweden
    kristianMatsson.grewUpIn = leksand
    kristianMatsson.soloCareerStartYear = 2006
    kristianMatsson.previousMemberOf = [montezumas]
    kristianMatsson.hadBandRole = "lead singer"
    kristianMatsson.musicComparedTo = [bobDylan]
    kristianMatsson.fullLengthAlbumCount = 4
    kristianMatsson.epCount = 2
    kristianMatsson.recordsAt = "home"
    kristianMatsson.recordingMethod = "voice and guitar together on one track"
    kristianMatsson.knownFor = "charismatic stage presence"
    kristianMatsson.formerSpouse = [amandaBergman]
    kristianMatsson.composedMusicFor = [onceAYear]
    amandaBergman.composedMusicFor = [onceAYear]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
