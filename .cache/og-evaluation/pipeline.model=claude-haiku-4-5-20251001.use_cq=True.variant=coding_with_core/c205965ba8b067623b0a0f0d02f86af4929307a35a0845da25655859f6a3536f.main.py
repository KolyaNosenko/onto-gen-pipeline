"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

1. Who was Joos van Cleve and what were his main artistic contributions?
2. What painting techniques did Joos van Cleve combine in his work?
3. During what time period was Joos van Cleve active as a painter?
4. In which city did Joos van Cleve primarily work?
5. What types of artworks was Joos van Cleve known for producing?
6. Was Joos van Cleve a member of any professional guild?
7. What was Joos van Cleve's role in the Guild of Saint Luke of Antwerp?
8. What innovative artistic technique did Joos van Cleve introduce to northern Renaissance painting?
9. Who was Joos van Cleve's son and what did he do?
10. What happened to Cornelis van Cleve during his residence in England?
11. What were the dates of Joos van Cleve's life?
12. How did Joos van Cleve influence sixteenth century painting styles?
13. What artistic influences shaped Joos van Cleve's work?
14. What characteristics distinguished Joos van Cleve as a skilled technician?
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
    AgentivePhysicalObject, Society, NonAgentivePhysicalObject,
    SpaceRegion,
)


with core:
    # Domain entity classes
    class Painter(AgentivePhysicalObject):
        """A person who creates paintings and other artworks."""
        pass

    class ArtistsGuild(Society):
        """An organized society of artists, such as a craft guild."""
        pass

    class Artwork(NonAgentivePhysicalObject):
        """A creative work such as a painting or other artistic creation."""
        pass

    class ReligiousWork(Artwork):
        """An artwork with religious subject matter or purpose."""
        pass

    class Portrait(Artwork):
        """A painting or artwork depicting a person."""
        pass

    class Location(SpaceRegion):
        """A geographic location such as a city or country."""
        pass

    # Domain ObjectProperty and DataProperty classes
    class fatherOf(ObjectProperty):
        """Relation between a father and his child."""
        domain = [Painter]
        range = [Painter]

    class memberOf(ObjectProperty):
        """Relation indicating membership in an organization."""
        domain = [AgentivePhysicalObject]
        range = [Society]

    class coDeaconOf(ObjectProperty):
        """Relation indicating a co-deacon role in an organization."""
        domain = [AgentivePhysicalObject]
        range = [Society]

    class activeIn(ObjectProperty):
        """Relation indicating where an artist was active or worked."""
        domain = [Painter]
        range = [Location]

    class residedIn(ObjectProperty):
        """Relation indicating where someone lived or had residence."""
        domain = [AgentivePhysicalObject]
        range = [Location]

    class birthYear(DataProperty, FunctionalProperty):
        """The year a person was born."""
        domain = [AgentivePhysicalObject]
        range = [int]

    class deathYear(DataProperty, FunctionalProperty):
        """The year a person died."""
        domain = [AgentivePhysicalObject]
        range = [int]

    class activeStartYear(DataProperty, FunctionalProperty):
        """The year a painter became active in their profession."""
        domain = [Painter]
        range = [int]

    class activeEndYear(DataProperty, FunctionalProperty):
        """The year a painter ceased to be active in their profession."""
        domain = [Painter]
        range = [int]

    class mentallyIll(DataProperty, FunctionalProperty):
        """Boolean indicating whether a person became mentally ill."""
        domain = [AgentivePhysicalObject]
        range = [bool]

    # Named instances from the source text
    joos = Painter("JoosVanCleve")
    joos.label = "Joos van Cleve"
    joos.birthYear = 1485
    joos.deathYear = 1540
    joos.activeStartYear = 1511
    joos.activeEndYear = 1540

    cornelis = Painter("CornelisVanCleve")
    cornelis.label = ["Cornelis van Cleve", "Sotte Cleef"]
    cornelis.birthYear = 1520
    cornelis.deathYear = 1567
    cornelis.mentallyIll = True

    joos.fatherOf.append(cornelis)

    guild = ArtistsGuild("GuildOfSaintLukeOfAntwerp")
    guild.label = "Guild of Saint Luke of Antwerp"

    joos.memberOf.append(guild)
    joos.coDeaconOf.append(guild)

    antwerp = Location("Antwerp")
    antwerp.label = "Antwerp"

    england = Location("England")
    england.label = "England"

    joos.activeIn.append(antwerp)
    cornelis.residedIn.append(england)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
