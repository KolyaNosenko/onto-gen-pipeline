"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What organizations form the Odeon Sky Filmworks joint venture?  
2. What is the name of the collaboration between Sky and Odeon?  
3. What is the purpose of Filmworks?  
4. Is Filmworks a UK-based film distributor?  
5. From whom does Filmworks sign titles directly?  
6. How many films does Filmworks plan to sign up initially per year?  
7. What types of release do the films have before UK television premiere?  
8. Which cinema chains will show the films theatrically?  
9. Will the films have a theatrical release at Odeon cinemas?  
10. Will the films also have theatrical release at other cinema chains?  
11. What distribution channels are used for DVD retail of the films?  
12. Does DVD retail include Odeon foyer sales?  
13. What distribution channels are used for DVD rental of the films?  
14. Does DVD rental include Odeon Direct?  
15. Who retains all UK TV rights for the films?  
16. Through which Sky services will the films be made available to viewers?  
17. Are the films available on Sky Movies By Broadband?  
18. Are the films available on Sky Box Office?  
19. At what point do the films have their UK television premiere?  
20. Are the films released on Sky television after availability on Sky Movies By Broadband and Sky Box Office?
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
    AgentiveSocialObject,
    NonPhysicalObject,
    Perdurant,
    SocialAgent,
    SpaceRegion,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class BroadcastingCompany(AgentiveSocialObject):
        pass

    class CinemaChain(AgentiveSocialObject):
        pass

    class OtherCinemaChain(CinemaChain):
        pass

    class JointVenture(AgentiveSocialObject):
        pass

    class FilmDistributor(AgentiveSocialObject):
        pass

    class UKBasedFilmDistributor(FilmDistributor):
        pass

    class FilmTitle(NonPhysicalObject):
        pass

    class DistributionChannel(Perdurant):
        pass

    class Release(DistributionChannel):
        pass

    class TheatricalRelease(Release):
        pass

    class DVDRetail(Release):
        pass

    class DVDRental(Release):
        pass

    class TelevisionPremiere(Release):
        pass

    class SkyService(DistributionChannel):
        pass

    class DownloadService(SkyService):
        pass

    class TVChannel(SkyService):
        pass

    class Filmmaker(SocialAgent):
        pass

    class Film(NonPhysicalObject):
        pass

    class UnitedKingdom(SpaceRegion):
        pass

    class formedBy(ObjectProperty):
        domain = [JointVenture]
        range = [AgentiveSocialObject]

    class basedIn(ObjectProperty):
        domain = [AgentiveSocialObject]
        range = [SpaceRegion]

    class hasPurposeText(DataProperty, FunctionalProperty):
        domain = [JointVenture]
        range = [str]

    class signsTitlesDirectlyFrom(ObjectProperty):
        domain = [FilmDistributor]
        range = [Filmmaker]

    class plansInitialFilmSignUpLimit(DataProperty, FunctionalProperty):
        domain = [FilmDistributor]
        range = [int]

    class hasRelease(ObjectProperty):
        domain = [Film]
        range = [Release]

    class hasTheatricalReleaseAt(ObjectProperty):
        domain = [Film]
        range = [CinemaChain]

    class availableVia(ObjectProperty):
        domain = [Film]
        range = [SkyService]

    class premieresOn(ObjectProperty):
        domain = [Film]
        range = [TVChannel]

    class retainsAllUKTVRightsFor(ObjectProperty):
        domain = [AgentiveSocialObject]
        range = [Film]

    class includedIn(partOf):
        domain = [DistributionChannel]
        range = [DistributionChannel]

    UK = UnitedKingdom("UK")
    UK.label = "UK"

    OdeonCinemas = CinemaChain("OdeonCinemas")
    OdeonCinemas.label = ["Odeon Cinemas", "ODEON"]

    BritishSkyBroadcasting = BroadcastingCompany("BritishSkyBroadcasting")
    BritishSkyBroadcasting.label = ["British Sky Broadcasting", "SKY"]

    OdeonSkyFilmworks = UKBasedFilmDistributor("OdeonSkyFilmworks")
    OdeonSkyFilmworks.label = [
        "Odeon Sky Filmworks",
        "Odeon and Sky Filmworks",
        "FILMWORKS",
        "Filmworks",
    ]

    SkyMoviesByBroadband = DownloadService("SkyMoviesByBroadband")
    SkyMoviesByBroadband.label = "Sky Movies By Broadband"

    SkyBoxOffice = SkyService("SkyBoxOffice")
    SkyBoxOffice.label = "Sky Box Office"

    SkyMovies = TVChannel("SkyMovies")
    SkyMovies.label = "Sky Movies"

    OdeonFoyerSales = DistributionChannel("OdeonFoyerSales")
    OdeonFoyerSales.label = "ODEON foyer sales"

    OdeonDirect = DistributionChannel("OdeonDirect")
    OdeonDirect.label = "ODEON Direct"

    Film.is_a.extend([
        hasRelease.some(TheatricalRelease),
        hasRelease.some(DVDRetail),
        hasRelease.some(DVDRental),
        hasRelease.some(TelevisionPremiere),
        hasTheatricalReleaseAt.value(OdeonCinemas),
        hasTheatricalReleaseAt.some(OtherCinemaChain),
        availableVia.value(SkyMoviesByBroadband),
        availableVia.value(SkyBoxOffice),
        premieresOn.value(SkyMovies),
    ])

    OdeonSkyFilmworks.is_a.extend([
        JointVenture,
        signsTitlesDirectlyFrom.some(Filmmaker),
    ])
    OdeonSkyFilmworks.formedBy.extend([OdeonCinemas, BritishSkyBroadcasting])
    OdeonSkyFilmworks.basedIn.append(UK)
    OdeonSkyFilmworks.hasPurposeText = "bring film titles to UK audiences in cinemas and at home"
    OdeonSkyFilmworks.plansInitialFilmSignUpLimit = 6

    BritishSkyBroadcasting.is_a.append(retainsAllUKTVRightsFor.some(Film))

    OdeonFoyerSales.is_a.append(includedIn.some(DVDRetail))
    OdeonDirect.is_a.append(includedIn.some(DVDRental))


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
