"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

Here are the competency questions derived from the document:

1. What is the real name of the artist who performs under the stage name "The Tallest Man on Earth"?
2. When was Kristian Matsson born?
3. Where is Kristian Matsson from?
4. In which city did Kristian Matsson grow up?
5. When did Kristian Matsson begin his solo career?
6. What band was Kristian Matsson a member of before his solo career?
7. What role did Kristian Matsson have in the band Montezumas?
8. Which famous musician's music is often compared to Kristian Matsson's music?
9. How many full-length albums has Kristian Matsson released since 2006?
10. How many EPs has Kristian Matsson released since 2006?
11. Where does Kristian Matsson record and produce his music?
12. How does Kristian Matsson typically record his voice and guitar?
13. What is Kristian Matsson known for among critics and fans?
14. Who was Kristian Matsson previously married to?
15. What is Amanda Bergman's stage name?
16. What film did Kristian Matsson and Amanda Bergman collaborate on?
17. What type of film is "Once a Year"?
18. What nationality is the film "Once a Year"?
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

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    Process,
    TimeInterval,
)

# TODO (optional): import the core properties you actually subclass.
from og_sandbox_with_core.core.properties import presentAt


with core:
    # ── Entity classes ────────────────────────────────────────────────────────

    class Musician(AgentivePhysicalObject):
        """A person who creates and performs music."""

    class SingerSongwriter(Musician):
        """A musician who both sings and writes their own songs."""

    class StageName(NonAgentiveSocialObject):
        """An alias or pseudonym used by a performer on stage."""

    class GeographicPlace(NonAgentivePhysicalObject):
        """A bounded area on the Earth's surface with a recognised identity."""

    class Country(Society):
        """A sovereign nation-state."""

    class GeographicRegion(GeographicPlace):
        """A named sub-national geographic area (province, county, etc.)."""

    class City(GeographicPlace):
        """A city, town, or municipality."""

    class MusicBand(Society):
        """A collective of musicians performing together under a shared name."""

    class IndieBand(MusicBand):
        """A music band operating independently of major labels."""

    class MusicalWork(NonAgentiveSocialObject):
        """A musical composition or recording release."""

    class MusicAlbum(MusicalWork):
        """A full-length album release."""

    class ExtendedPlay(MusicalWork):
        """An EP (Extended Play) release."""

    class Film(NonAgentiveSocialObject):
        """A motion picture."""

    class DramaFilm(Film):
        """A film belonging to the drama genre."""

    # ── Object properties ─────────────────────────────────────────────────────

    class hasStageName(ObjectProperty):
        """Links a musician to their stage name / alias."""
        domain = [Musician]
        range  = [StageName]

    class originatesFrom(ObjectProperty):
        """Links a person to the geographic place or country they are from."""
        domain = [AgentivePhysicalObject]
        range  = [GeographicPlace, Country]

    class grewUpIn(ObjectProperty):
        """Links a person to the city where they grew up."""
        domain = [AgentivePhysicalObject]
        range  = [City]

    class memberOf(ObjectProperty):
        """Links a musician to a band they belong(ed) to."""
        domain = [Musician]
        range  = [MusicBand]

    class musicInfluencedBy(ObjectProperty):
        """Links a musician to another musician whose work theirs is compared to."""
        domain = [Musician]
        range  = [Musician]

    class bornAt(presentAt):
        """Links a musician to the time interval of their birth."""
        domain = [Musician]
        range  = [TimeInterval]

    class soloCareerBeganAt(ObjectProperty, FunctionalProperty):
        """Links a musician to the time interval when their solo career began."""
        domain = [Musician]
        range  = [TimeInterval]

    class marriedTo(ObjectProperty, SymmetricProperty):
        """Links two persons who are (or were) married to each other."""
        domain = [AgentivePhysicalObject]
        range  = [AgentivePhysicalObject]

    class wroteMusicFor(ObjectProperty):
        """Links a person to a film for which they wrote the music."""
        domain = [AgentivePhysicalObject]
        range  = [Film]

    class filmNationality(ObjectProperty):
        """Links a film to the country of its national identity."""
        domain = [Film]
        range  = [Country]

    # ── Data properties ───────────────────────────────────────────────────────

    class hasBandRole(DataProperty, FunctionalProperty):
        """The role a musician held in a band (e.g. 'lead singer')."""
        domain = [Musician]
        range  = [str]

    class fullLengthAlbumCount(DataProperty, FunctionalProperty):
        """Number of full-length albums released by a musician."""
        domain = [Musician]
        range  = [int]

    class epCount(DataProperty, FunctionalProperty):
        """Number of EPs released by a musician."""
        domain = [Musician]
        range  = [int]

    class recordingLocation(DataProperty, FunctionalProperty):
        """Where a musician records and produces their music."""
        domain = [Musician]
        range  = [str]

    class knownFor(DataProperty):
        """Something a person is widely recognised for."""
        domain = [AgentivePhysicalObject]
        range  = [str]

    # ── Named individuals ─────────────────────────────────────────────────────

    kristianMatsson = SingerSongwriter("KristianMatsson")
    kristianMatsson.label = "Kristian Matsson"

    theTallestManOnEarth = StageName("TheTallestManOnEarth")
    theTallestManOnEarth.label = "The Tallest Man on Earth"

    sweden = Country("Sweden")
    sweden.label = "Sweden"

    dalarna = GeographicRegion("Dalarna")
    dalarna.label = "Dalarna"

    leksand = City("Leksand")
    leksand.label = "Leksand"

    montezumas = IndieBand("Montezumas")
    montezumas.label = "Montezumas"

    bobDylan = Musician("BobDylan")
    bobDylan.label = "Bob Dylan"

    amandaBergman = SingerSongwriter("AmandaBergman")
    amandaBergman.label = "Amanda Bergman"

    idiotWind = StageName("IdiotWind")
    idiotWind.label = "Idiot Wind"

    onceAYear = DramaFilm("OnceAYear")
    onceAYear.label = "Once a Year"

    birth30April1983 = TimeInterval("Birth_30April1983")
    birth30April1983.label = "30 April 1983"

    year2006 = TimeInterval("Year_2006")
    year2006.label = "2006"

    # ── Property assertions ───────────────────────────────────────────────────

    # Kristian Matsson facts
    kristianMatsson.hasStageName.append(theTallestManOnEarth)
    kristianMatsson.bornAt.append(birth30April1983)
    kristianMatsson.originatesFrom.append(dalarna)
    kristianMatsson.originatesFrom.append(sweden)
    kristianMatsson.grewUpIn.append(leksand)
    kristianMatsson.soloCareerBeganAt = year2006
    kristianMatsson.memberOf.append(montezumas)
    kristianMatsson.hasBandRole = "lead singer"
    kristianMatsson.musicInfluencedBy.append(bobDylan)
    kristianMatsson.fullLengthAlbumCount = 4
    kristianMatsson.epCount = 2
    kristianMatsson.recordingLocation = "his home"
    kristianMatsson.knownFor.append("charismatic stage presence")
    kristianMatsson.marriedTo.append(amandaBergman)
    kristianMatsson.wroteMusicFor.append(onceAYear)

    # Amanda Bergman facts
    amandaBergman.hasStageName.append(idiotWind)
    amandaBergman.marriedTo.append(kristianMatsson)
    amandaBergman.wroteMusicFor.append(onceAYear)

    # Once a Year facts
    onceAYear.filmNationality.append(sweden)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
