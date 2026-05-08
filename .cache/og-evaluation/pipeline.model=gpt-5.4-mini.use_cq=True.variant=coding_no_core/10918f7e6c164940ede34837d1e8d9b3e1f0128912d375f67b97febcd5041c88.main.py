"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What is the name of the joint venture between Odeon Cinemas and British Sky Broadcasting?
2. Which organizations form the collaboration known as Filmworks?
3. What is the role of Filmworks in the UK film market?
4. Does Filmworks act as a UK-based film distributor?
5. From whom does Filmworks sign up film titles directly?
6. How many films does Filmworks plan to sign up initially per year?
7. Which films are scheduled for theatrical release at ODEON?
8. Are the films released theatrically at other cinema chains before home distribution?
9. What distribution channels are used after theatrical release?
10. Are films available for DVD retail after cinema release?
11. Are films available for DVD rental after cinema release?
12. Does ODEON participate in DVD retail sales through foyer sales?
13. Does ODEON participate in DVD rental through ODEON Direct?
14. Which organization retains all UK TV rights for the films?
15. Through which Sky services are the films made available to viewers?
16. Are the films available on Sky Movies By Broadband?
17. Are the films available on Sky Box Office?
18. Before which event do the films become available on Sky services?
19. What is the UK television premiere platform for the films?
20. Are the films available to UK audiences both in cinemas and at home?
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
    class Organization(Thing):
        pass

    class Collaboration(Organization):
        pass

    class JointVenture(Collaboration):
        pass

    class FilmDistributor(Organization):
        pass

    class UKBasedFilmDistributor(FilmDistributor):
        pass

    class BroadcastingCompany(Organization):
        pass

    class CinemaChain(Organization):
        pass

    class Territory(Thing):
        pass

    class Country(Territory):
        pass

    class HomeDistribution(Thing):
        pass

    class Service(HomeDistribution):
        pass

    class RetailService(Service):
        pass

    class RentalService(Service):
        pass

    class DownloadService(Service):
        pass

    class TelevisionChannel(Service):
        pass

    class TelevisionPremiere(HomeDistribution):
        pass

    class TelevisionRights(Thing):
        pass

    class Filmmaker(Thing):
        pass

    class Film(Thing):
        pass

    class hasPartner(ObjectProperty, SymmetricProperty):
        domain = [Collaboration]
        range = [Organization]

    class targetsAudienceIn(ObjectProperty):
        domain = [Collaboration]
        range = [Territory]

    class basedIn(ObjectProperty):
        domain = [Organization]
        range = [Territory]

    class signsUpTitleFrom(ObjectProperty):
        domain = [FilmDistributor]
        range = [Filmmaker]

    class plannedInitialFilmCount(DataProperty, FunctionalProperty):
        domain = [Collaboration]
        range = [int]

    class providesService(ObjectProperty):
        domain = [Organization]
        range = [Service]

    class retainsRights(ObjectProperty):
        domain = [Organization]
        range = [TelevisionRights]

    class hasTheatricalReleaseAt(ObjectProperty):
        domain = [Film]
        range = [CinemaChain]

    class hasRetailReleaseAt(ObjectProperty):
        domain = [Film]
        range = [RetailService]

    class hasRentalReleaseAt(ObjectProperty):
        domain = [Film]
        range = [RentalService]

    class availableVia(ObjectProperty):
        domain = [Film]
        range = [Service]

    class precedes(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class hasPremierePlatform(ObjectProperty, FunctionalProperty):
        domain = [TelevisionPremiere]
        range = [TelevisionChannel]

    OdeonCinemas = CinemaChain("OdeonCinemas")
    OdeonCinemas.label = ["Odeon Cinemas", "ODEON", "Odeon"]

    BritishSkyBroadcasting = BroadcastingCompany("BritishSkyBroadcasting")
    BritishSkyBroadcasting.label = ["British Sky Broadcasting", "SKY", "Sky"]

    UkTerritory = Country("UkTerritory")
    UkTerritory.label = ["UK"]

    AllUKTvRights = TelevisionRights("AllUKTvRights")
    AllUKTvRights.label = ["all UK TV rights"]

    SkyMoviesByBroadband = DownloadService("SkyMoviesByBroadband")
    SkyMoviesByBroadband.label = ["Sky Movies By Broadband"]

    SkyBoxOffice = Service("SkyBoxOffice")
    SkyBoxOffice.label = ["Sky Box Office"]

    SkyMovies = TelevisionChannel("SkyMovies")
    SkyMovies.label = ["Sky Movies"]

    OdeonFoyerSales = RetailService("OdeonFoyerSales")
    OdeonFoyerSales.label = ["ODEON foyer sales"]

    OdeonDirect = RentalService("OdeonDirect")
    OdeonDirect.label = ["ODEON Direct"]

    UkTelevisionPremiere = TelevisionPremiere("UkTelevisionPremiere")
    UkTelevisionPremiere.label = ["UK Television Premiere"]
    UkTelevisionPremiere.hasPremierePlatform = SkyMovies

    BritishSkyBroadcasting.providesService = [SkyMoviesByBroadband, SkyBoxOffice, SkyMovies]
    BritishSkyBroadcasting.retainsRights = [AllUKTvRights]

    OdeonCinemas.providesService = [OdeonFoyerSales, OdeonDirect]

    SkyMoviesByBroadband.precedes = [UkTelevisionPremiere]
    SkyBoxOffice.precedes = [UkTelevisionPremiere]
    OdeonFoyerSales.precedes = [UkTelevisionPremiere]
    OdeonDirect.precedes = [UkTelevisionPremiere]

    FilmworksVenture = JointVenture("FilmworksVenture")
    FilmworksVenture.label = ["Odeon Sky Filmworks", "Odeon and Sky Filmworks", "FILMWORKS"]
    FilmworksVenture.is_a.append(UKBasedFilmDistributor)
    FilmworksVenture.is_a.append(signsUpTitleFrom.some(Filmmaker))
    FilmworksVenture.hasPartner = [OdeonCinemas, BritishSkyBroadcasting]
    FilmworksVenture.targetsAudienceIn = [UkTerritory]
    FilmworksVenture.plannedInitialFilmCount = 6

    class FilmworksPlannedFilm(Film):
        is_a = [
            hasTheatricalReleaseAt.some(CinemaChain),
            hasTheatricalReleaseAt.value(OdeonCinemas),
            hasRetailReleaseAt.some(RetailService),
            hasRetailReleaseAt.value(OdeonFoyerSales),
            hasRentalReleaseAt.some(RentalService),
            hasRentalReleaseAt.value(OdeonDirect),
            availableVia.value(SkyMoviesByBroadband),
            availableVia.value(SkyBoxOffice),
            precedes.some(HomeDistribution),
        ]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
