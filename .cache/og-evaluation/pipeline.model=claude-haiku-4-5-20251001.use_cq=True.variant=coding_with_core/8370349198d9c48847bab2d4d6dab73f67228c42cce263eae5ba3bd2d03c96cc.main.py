"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

1. What is the real name of the artist known as The Tallest Man on Earth?

2. When was Kristian Matsson born?

3. Where is Kristian Matsson from?

4. What stage name does Kristian Matsson perform under?

5. Which indie band was Kristian Matsson the lead singer of before his solo career?

6. When did Kristian Matsson begin his solo career?

7. How many full-length albums has Kristian Matsson released since 2006?

8. How many EPs has Kristian Matsson released since 2006?

9. How does Kristian Matsson typically record his music?

10. Which artist's music has Kristian Matsson's work been compared to?

11. What is Kristian Matsson known for among critics and fans?

12. Who was Kristian Matsson previously married to?

13. What is the stage name of Kristian Matsson's ex-wife?

14. Which Swedish drama film did Kristian Matsson and Amanda Bergman write music for together?

15. Where did Kristian Matsson grow up?

16. Does Kristian Matsson record his voice and guitar on separate tracks or together?
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
    AgentivePhysicalObject, Society, NonPhysicalObject, SpaceRegion
)


with core:
    # Entity classes
    class Musician(AgentivePhysicalObject):
        """A person who performs and creates music."""
        pass

    class IndieBand(Society):
        """An independent music band."""
        pass

    class Film(NonPhysicalObject):
        """A motion picture or dramatic film."""
        pass

    class Place(SpaceRegion):
        """A geographic location."""
        pass

    # Object properties
    class fromPlace(ObjectProperty, FunctionalProperty):
        """Origin place of a musician."""
        domain = [Musician]
        range = [Place]

    class grewUpIn(ObjectProperty, FunctionalProperty):
        """Place where a musician grew up."""
        domain = [Musician]
        range = [Place]

    class comparedToMusician(ObjectProperty):
        """Reference to another musician for stylistic comparison."""
        domain = [Musician]
        range = [Musician]

    class previouslyMarriedTo(ObjectProperty, SymmetricProperty):
        """Previous marriage relationship between two people."""
        domain = [AgentivePhysicalObject]
        range = [AgentivePhysicalObject]

    class wroteMusicalScoreFor(ObjectProperty):
        """Musician who wrote music for a film."""
        domain = [AgentivePhysicalObject]
        range = [Film]

    class leadSingerOf(ObjectProperty, FunctionalProperty):
        """Lead singer relationship with a band."""
        domain = [Musician]
        range = [IndieBand]

    # Data properties
    class hasStageName(DataProperty, FunctionalProperty):
        """Stage name of a musician."""
        domain = [Musician]
        range = [str]

    class birthDate(DataProperty, FunctionalProperty):
        """Birth date of a person."""
        domain = [AgentivePhysicalObject]
        range = [str]

    class soloCareerStartYear(DataProperty, FunctionalProperty):
        """Year a musician began their solo career."""
        domain = [Musician]
        range = [int]

    class numberOfAlbums(DataProperty, FunctionalProperty):
        """Number of full-length albums released."""
        domain = [Musician]
        range = [int]

    class numberOfEPs(DataProperty, FunctionalProperty):
        """Number of EPs released."""
        domain = [Musician]
        range = [int]

    class recordingMethod(DataProperty):
        """Description of how a musician records their music."""
        domain = [Musician]
        range = [str]

    class knownFor(DataProperty):
        """What a musician is known for."""
        domain = [Musician]
        range = [str]

    # Named instances
    kristian = Musician("KristianMatsson_person")
    kristian.label = "Kristian Matsson"
    kristian.hasStageName = "The Tallest Man on Earth"
    kristian.birthDate = "30 April 1983"
    kristian.soloCareerStartYear = 2006
    kristian.numberOfAlbums = 4
    kristian.numberOfEPs = 2
    kristian.recordingMethod.append("voice and guitar together on one track")
    kristian.knownFor.append("charismatic stage presence")

    amanda = Musician("AmandaBergman_person")
    amanda.label = "Amanda Bergman"
    amanda.hasStageName = "Idiot Wind"

    bob = Musician("BobDylan_person")
    bob.label = "Bob Dylan"

    montezumas = IndieBand("Montezumas_band")
    montezumas.label = "Montezumas"

    once_a_year = Film("OnceAYear_film")
    once_a_year.label = "Once a Year"

    dalarna = Place("Dalarna_place")
    dalarna.label = "Dalarna"

    leksand = Place("Leksand_place")
    leksand.label = "Leksand"

    sweden = Place("Sweden_place")
    sweden.label = "Sweden"

    # Relationships
    kristian.fromPlace = dalarna
    kristian.grewUpIn = leksand
    kristian.comparedToMusician.append(bob)
    kristian.previouslyMarriedTo.append(amanda)
    kristian.wroteMusicalScoreFor.append(once_a_year)
    kristian.leadSingerOf = montezumas

    amanda.previouslyMarriedTo.append(kristian)
    amanda.wroteMusicalScoreFor.append(once_a_year)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
