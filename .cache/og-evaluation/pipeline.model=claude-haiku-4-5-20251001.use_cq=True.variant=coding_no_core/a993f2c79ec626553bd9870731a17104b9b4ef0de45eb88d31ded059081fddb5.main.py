"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What is Odeon Sky Filmworks and which organizations are involved in this joint venture?

2. What are the primary functions of Odeon Sky Filmworks as a film distributor?

3. How many films does Filmworks plan to release per year initially?

4. What is the distribution sequence for films released through Filmworks?

5. In which venues can films be released theatrically through Filmworks?

6. What are the different formats and sales channels through which Filmworks films are made available?

7. Which organization retains UK TV rights for films distributed through Filmworks?

8. What are the different ways Sky makes films available to its viewers?

9. What is the timeline of film release across different platforms (theatrical, DVD, TV)?

10. Which retail and rental channels are available for DVD distribution of Filmworks films?

11. How does Sky Movies By Broadband relate to the film distribution timeline?

12. What is the relationship between Sky Box Office and UK Television Premiere on Sky Movies in the distribution strategy?
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
    # Entity classes
    class Organization(Thing):
        pass

    class JointVenture(Organization):
        pass

    class Film(Thing):
        pass

    class Filmmaker(Thing):
        pass

    class Venue(Thing):
        pass

    class DistributionChannel(Thing):
        pass

    class TVService(DistributionChannel):
        pass

    class Territory(Thing):
        pass

    # Object Properties
    class partnerInJointVenture(ObjectProperty):
        domain = [Organization]
        range = [JointVenture]

    class signsFilmsFrom(ObjectProperty):
        domain = [JointVenture]
        range = [Filmmaker]

    class releasedAt(ObjectProperty):
        domain = [Film]
        range = [Venue]

    class availableThrough(ObjectProperty):
        domain = [Film]
        range = [DistributionChannel]

    class holdsUKTVRights(ObjectProperty):
        domain = [Organization]
        range = [JointVenture]

    class makesAvailable(ObjectProperty):
        domain = [TVService]
        range = [Film]

    class operatesIn(ObjectProperty):
        domain = [Organization, TVService]
        range = [Territory]

    class precedes(ObjectProperty, TransitiveProperty):
        domain = [DistributionChannel]
        range = [DistributionChannel]

    # Data Properties
    class filmsPerYear(DataProperty, FunctionalProperty):
        domain = [JointVenture]
        range = [int]

    # Named Individuals
    OdeonSkyFilmworks = JointVenture("OdeonSkyFilmworks")
    OdeonSkyFilmworks.label = ["Odeon Sky Filmworks", "Odeon and Sky Filmworks", "FILMWORKS"]

    OdeonCinemas = Organization("OdeonCinemas")
    OdeonCinemas.label = ["Odeon Cinemas", "ODEON"]

    BritishSkyBroadcasting = Organization("BritishSkyBroadcasting")
    BritishSkyBroadcasting.label = ["British Sky Broadcasting", "SKY"]

    OdeonDirect = DistributionChannel("OdeonDirect")
    OdeonDirect.label = "ODEON Direct"

    SkyMoviesByBroadband = TVService("SkyMoviesByBroadband")
    SkyMoviesByBroadband.label = "Sky Movies By Broadband"

    SkyBoxOffice = TVService("SkyBoxOffice")
    SkyBoxOffice.label = "Sky Box Office"

    SkyMovies = TVService("SkyMovies")
    SkyMovies.label = "Sky Movies"

    UnitedKingdom = Territory("UnitedKingdom")
    UnitedKingdom.label = "UK"

    # Relationships
    OdeonCinemas.partnerInJointVenture = [OdeonSkyFilmworks]
    BritishSkyBroadcasting.partnerInJointVenture = [OdeonSkyFilmworks]

    OdeonSkyFilmworks.operatesIn = [UnitedKingdom]
    BritishSkyBroadcasting.operatesIn = [UnitedKingdom]

    OdeonSkyFilmworks.filmsPerYear = 6

    BritishSkyBroadcasting.holdsUKTVRights = [OdeonSkyFilmworks]

    SkyMoviesByBroadband.precedes = [SkyBoxOffice]
    SkyBoxOffice.precedes = [SkyMovies]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
