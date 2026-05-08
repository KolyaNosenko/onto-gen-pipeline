"""
=== TASK INPUT ===
Source text:
Kristian Matsson ( born 30 April 1983 ) is a singer - songwriter from Dalarna , Sweden , who performs under the stage name of The Tallest Man on Earth . Matsson grew up in Leksand , and began his solo career in 2006 , having previously been the lead singer of the indie band Montezumas . His music has often drawn comparisons to the music of Bob Dylan . Since 2006 , Matsson has released four full - length albums and two EPs . He records and produces these in his home , and usually records his voice and guitar together on one track . He is known both by critics and his fans for his charismatic stage presence . He was previously married to Amanda Bergman , also known by the stage name Idiot Wind . Together , they wrote the music for the Swedish drama film Once a Year .

1. What is the real name of the artist known as The Tallest Man on Earth?

2. When was Kristian Matsson born?

3. Where is Kristian Matsson from?

4. In which city did Kristian Matsson grow up?

5. When did Kristian Matsson begin his solo career?

6. What was the name of the indie band that Kristian Matsson was the lead singer of before his solo career?

7. Which artist's music is Kristian Matsson's music often compared to?

8. How many full-length albums has Kristian Matsson released since 2006?

9. How many EPs has Kristian Matsson released since 2006?

10. Where does Kristian Matsson record and produce his music?

11. What is Kristian Matsson's typical recording approach?

12. What is Kristian Matsson known for among critics and fans?

13. Who was Kristian Matsson previously married to?

14. What is the stage name of Kristian Matsson's ex-wife?

15. What Swedish drama film did Kristian Matsson and his ex-wife collaborate on?

16. What did Kristian Matsson and Amanda Bergman write for the film Once a Year?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
import datetime

from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    # Entity classes
    class Person(Thing): pass
    class Artist(Person): pass
    class SingerSongwriter(Artist): pass
    class Band(Thing): pass
    class Film(Thing): pass
    class Location(Thing): pass
    class Country(Location): pass
    class Region(Location): pass
    class City(Location): pass
    
    # Object and Data Properties
    class performsAs(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [str]
    
    class bornOn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [datetime.date]
    
    class isFrom(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Location]
    
    class grewUpIn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [City]
    
    class beganSoloCareerInYear(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]
    
    class wasLeadSingerOf(ObjectProperty):
        domain = [Artist]
        range = [Band]
    
    class musicComparableTo(ObjectProperty):
        domain = [Artist]
        range = [Artist]
    
    class releasedAlbumsCount(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]
    
    class releasedEPsCount(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [int]
    
    class recordsAt(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [str]
    
    class recordingApproach(DataProperty):
        domain = [Artist]
        range = [str]
    
    class knownFor(DataProperty):
        domain = [Person]
        range = [str]
    
    class previouslyMarriedTo(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]
    
    class wroteMusic(ObjectProperty):
        domain = [Artist]
        range = [Film]
    
    class country(ObjectProperty, FunctionalProperty):
        domain = [Film]
        range = [Country]
    
    class genre(DataProperty, FunctionalProperty):
        domain = [Film]
        range = [str]
    
    # Named instances from the source text
    # Create locations
    sweden = Country("Sweden")
    sweden.label = "Sweden"
    
    dalarna = Region("Dalarna")
    dalarna.label = "Dalarna"
    
    leksand = City("Leksand")
    leksand.label = "Leksand"
    
    # Create other artists and entities
    bob_dylan = Artist("BobDylan")
    bob_dylan.label = "Bob Dylan"
    
    montezumas = Band("Montezumas")
    montezumas.label = "Montezumas"
    
    once_a_year = Film("OnceAYear")
    once_a_year.label = "Once a Year"
    once_a_year.country = sweden
    once_a_year.genre = "drama"
    
    # Create Amanda Bergman first (needed for previouslyMarriedTo reference)
    amanda = SingerSongwriter("AmandaBergman")
    amanda.label = "Amanda Bergman"
    amanda.performsAs = "Idiot Wind"
    amanda.wroteMusic = [once_a_year]
    
    # Create Kristian Matsson
    kristian = SingerSongwriter("KristianMatsson")
    kristian.label = "Kristian Matsson"
    kristian.bornOn = datetime.date(1983, 4, 30)
    kristian.performsAs = "The Tallest Man on Earth"
    kristian.isFrom = dalarna
    kristian.grewUpIn = leksand
    kristian.beganSoloCareerInYear = 2006
    kristian.wasLeadSingerOf = [montezumas]
    kristian.musicComparableTo = [bob_dylan]
    kristian.releasedAlbumsCount = 4
    kristian.releasedEPsCount = 2
    kristian.recordsAt = "his home"
    kristian.recordingApproach = ["usually records his voice and guitar together on one track"]
    kristian.knownFor = ["charismatic stage presence"]
    kristian.wroteMusic = [once_a_year]
    kristian.previouslyMarriedTo = [amanda]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
