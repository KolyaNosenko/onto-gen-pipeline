"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

Here are the competency questions derived from the document:

1. What is Odeon Sky Filmworks and who are its founding partners?
2. What type of business entity is Odeon Sky Filmworks?
3. What is the primary purpose of the joint venture between Odeon Cinemas and British Sky Broadcasting?
4. How many films does Filmworks plan to sign up for release per year initially?
5. Where will films signed by Filmworks receive their theatrical release?
6. What distribution channels are planned for films released by Filmworks?
7. Which company retains all UK TV rights for films distributed by Filmworks?
8. Through which platforms will Sky make Filmworks films available to viewers?
9. What is the sequence of release windows for Filmworks films?
10. Where can DVD retail sales of Filmworks films take place?
11. What download service does Sky use to distribute Filmworks films?
12. What TV channel will broadcast the UK Television Premiere of Filmworks films?
13. Is Filmworks limited to releasing films only through Odeon Cinemas?
14. What rental services are available for Filmworks films?
15. What is the role of Filmworks as a UK-based organization in the film industry?
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
    # ── Entity Classes ────────────────────────────────────────────────────
    class Organisation(Thing): pass
    class CinemaChain(Organisation): pass
    class BroadcastingCompany(Organisation): pass
    class JointVenture(Organisation): pass
    class FilmDistributor(Organisation): pass

    class Film(Thing): pass
    class Filmmaker(Thing): pass
    class Audience(Thing): pass
    class Country(Thing): pass

    class DistributionChannel(Thing): pass
    class TheatricalRelease(DistributionChannel): pass
    class HomeViewingChannel(DistributionChannel): pass
    class DVDRetail(HomeViewingChannel): pass
    class DVDRentalService(HomeViewingChannel): pass
    class DownloadService(HomeViewingChannel): pass
    class PayPerViewService(HomeViewingChannel): pass
    class TVChannel(HomeViewingChannel): pass

    # ── Object Properties ─────────────────────────────────────────────────
    class hasFoundingPartner(ObjectProperty):
        domain = [JointVenture]
        range  = [Organisation]

    class operatesIn(ObjectProperty):
        domain = [Organisation]
        range  = [Country]

    class signsFilmFrom(ObjectProperty):
        domain = [FilmDistributor]
        range  = [Filmmaker]

    class hasDistributionChannel(ObjectProperty):
        domain = [Organisation]
        range  = [DistributionChannel]

    class hasTheatricalVenue(ObjectProperty):
        domain = [Organisation]
        range  = [CinemaChain]

    class retainsUKTVRightsFrom(ObjectProperty):
        domain = [BroadcastingCompany]
        range  = [JointVenture]

    class makesAvailableVia(ObjectProperty):
        domain = [BroadcastingCompany]
        range  = [DistributionChannel]

    class precedes(ObjectProperty, TransitiveProperty):
        """Release window ordering (transitive): earlier window precedes later ones."""
        domain = [DistributionChannel]
        range  = [DistributionChannel]

    # ── Data Properties ───────────────────────────────────────────────────
    class plansFilmsPerYear(DataProperty, FunctionalProperty):
        domain = [FilmDistributor]
        range  = [int]

    # ── Named Individuals ─────────────────────────────────────────────────

    # Organisations
    odeonSkyFilmworks = JointVenture("OdeonSkyFilmworks")
    odeonSkyFilmworks.label = ["Odeon Sky Filmworks", "Odeon and Sky Filmworks"]
    odeonSkyFilmworks.is_a.append(FilmDistributor)

    odeonCinemas = CinemaChain("OdeonCinemas")
    odeonCinemas.label = "Odeon Cinemas"

    britishSkyBroadcasting = BroadcastingCompany("BritishSkyBroadcasting")
    britishSkyBroadcasting.label = "British Sky Broadcasting"

    uk = Country("UK")
    uk.label = "UK"

    # Distribution Channels / Release Services
    odeonTheatricalRelease = TheatricalRelease("OdeonTheatricalRelease")
    odeonTheatricalRelease.label = "Odeon theatrical release"

    odeonFoyerSales = DVDRetail("OdeonFoyerSales")
    odeonFoyerSales.label = "ODEON foyer sales"

    odeonDirect = DVDRentalService("OdeonDirect")
    odeonDirect.label = "ODEON Direct"

    skyMoviesByBroadband = DownloadService("SkyMoviesByBroadband")
    skyMoviesByBroadband.label = "Sky Movies By Broadband"

    skyBoxOffice = PayPerViewService("SkyBoxOffice")
    skyBoxOffice.label = "Sky Box Office"

    skyMovies = TVChannel("SkyMovies")
    skyMovies.label = "Sky Movies"

    # Property assertions – Odeon Sky Filmworks
    odeonSkyFilmworks.hasFoundingPartner = [odeonCinemas, britishSkyBroadcasting]
    odeonSkyFilmworks.operatesIn = [uk]
    odeonSkyFilmworks.plansFilmsPerYear = 6
    odeonSkyFilmworks.hasTheatricalVenue = [odeonCinemas]
    odeonSkyFilmworks.hasDistributionChannel = [
        odeonTheatricalRelease, odeonFoyerSales, odeonDirect,
        skyMoviesByBroadband, skyBoxOffice, skyMovies,
    ]

    # Property assertions – British Sky Broadcasting
    britishSkyBroadcasting.operatesIn = [uk]
    britishSkyBroadcasting.retainsUKTVRightsFrom = [odeonSkyFilmworks]
    britishSkyBroadcasting.makesAvailableVia = [skyMoviesByBroadband, skyBoxOffice, skyMovies]

    # Release window sequence: theatrical → DVD retail/rental → download/box-office → TV premiere
    odeonTheatricalRelease.precedes = [
        odeonFoyerSales, odeonDirect,
        skyMoviesByBroadband, skyBoxOffice, skyMovies,
    ]
    odeonFoyerSales.precedes = [skyMoviesByBroadband, skyBoxOffice, skyMovies]
    odeonDirect.precedes   = [skyMoviesByBroadband, skyBoxOffice, skyMovies]
    skyMoviesByBroadband.precedes = [skyMovies]
    skyBoxOffice.precedes         = [skyMovies]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
