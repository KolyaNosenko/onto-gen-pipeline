"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What is Odeon Sky Filmworks and who are the partners involved in this joint venture?

2. What is the primary role of Odeon and Sky Filmworks as a film distributor?

3. How many films does Filmworks plan to release per year initially?

4. What are the different distribution channels through which films are released by Filmworks?

5. In what order are films released across different media formats (theatrical, DVD, TV)?

6. Which organization retains the UK TV rights for films distributed by Filmworks?

7. What are the different ways Sky makes films available to its viewers?

8. Where can consumers access films through Odeon and Sky Filmworks services?

9. What is the relationship between theatrical releases at ODEON and releases at other cinema chains?

10. How do DVD retail and rental services fit into the overall distribution strategy of Filmworks?

11. What services does Sky provide for film distribution through broadband and box office channels?

12. When are films made available on Sky Movies By Broadband relative to their UK Television Premiere?
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
    Society, NonAgentiveSocialObject
)

# No core properties are subclassed for this domain


with core:
    # Domain entity classes
    class Film(NonAgentiveSocialObject):
        """A motion picture work distributed by Filmworks."""
        pass

    class FilmDistributor(Society):
        """An organization that distributes films."""
        pass

    class CinemaChain(Society):
        """A chain of cinema theaters."""
        pass

    class DistributionService(NonAgentiveSocialObject):
        """A service through which films are made available to consumers."""
        pass

    class BroadbandStreamingService(DistributionService):
        """Service for streaming films via broadband."""
        pass

    class VideoOnDemandService(DistributionService):
        """Service for digital purchase/rental of films."""
        pass

    class TelevisionService(DistributionService):
        """Television service for broadcasting films."""
        pass

    class DVDRentalService(DistributionService):
        """Service for renting films on DVD."""
        pass

    class DVDRetailService(DistributionService):
        """Service for retail sale of films on DVD."""
        pass

    # Domain ObjectProperty / DataProperty subclasses
    class partnerIn(ObjectProperty):
        """Organizations that are partners in a joint venture."""
        domain = [Society]
        range = [Society]

    class operatesService(ObjectProperty):
        """An organization operates a distribution service."""
        domain = [Society]
        range = [DistributionService]

    class plansToReleasePerYear(DataProperty, FunctionalProperty):
        """Number of films a distributor plans to release per year."""
        domain = [FilmDistributor]
        range = [int]

    class retainsUKTVRights(ObjectProperty):
        """An organization retains UK TV rights for films."""
        domain = [Society]
        range = [Film]

    # Named instances
    odeon_cinemas = CinemaChain("OdeonCinemas")
    odeon_cinemas.label = "Odeon Cinemas"

    british_sky = Society("BritishSkyBroadcasting")
    british_sky.label = "British Sky Broadcasting"

    filmworks = FilmDistributor("OdeonAndSkyFilmworks")
    filmworks.label = "Odeon and Sky Filmworks"

    # Partnership relationships
    filmworks.partnerIn.append(odeon_cinemas)
    filmworks.partnerIn.append(british_sky)

    # Film distribution plan
    filmworks.plansToReleasePerYear = 6

    # Distribution services
    sky_broadband = BroadbandStreamingService("SkyMoviesByBroadband")
    sky_broadband.label = "Sky Movies By Broadband"

    sky_boxoffice = VideoOnDemandService("SkyBoxOffice")
    sky_boxoffice.label = "Sky Box Office"

    sky_tv = TelevisionService("SkyMovies")
    sky_tv.label = "Sky Movies"

    odeon_direct = DVDRentalService("ODEONDirect")
    odeon_direct.label = "ODEON Direct"

    # Service operators
    british_sky.operatesService.append(sky_broadband)
    british_sky.operatesService.append(sky_boxoffice)
    british_sky.operatesService.append(sky_tv)

    odeon_cinemas.operatesService.append(odeon_direct)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
