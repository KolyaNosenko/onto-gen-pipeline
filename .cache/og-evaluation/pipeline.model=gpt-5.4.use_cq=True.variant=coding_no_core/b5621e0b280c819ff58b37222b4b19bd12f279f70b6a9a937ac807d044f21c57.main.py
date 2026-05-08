"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What is Odeon and Sky Filmworks?
2. Which organizations are involved in the joint venture Odeon and Sky Filmworks?
3. What type of business entity is Odeon and Sky Filmworks?
4. What is the purpose of the collaboration between Odeon Cinemas and British Sky Broadcasting?
5. Under what name does the collaboration operate?
6. What does the acronym FILMWORKS refer to?
7. In which country is Odeon and Sky Filmworks based?
8. What role does Odeon and Sky Filmworks play in the film industry?
9. From whom does Odeon and Sky Filmworks acquire film titles?
10. How many films does Filmworks plan to sign for release each year initially?
11. Which films are intended to be released by Odeon and Sky Filmworks?
12. Where do films distributed by Filmworks receive their theatrical release?
13. Are Filmworks titles released only at Odeon cinemas or also at other cinema chains?
14. What distribution stages follow the theatrical release of Filmworks titles?
15. Through which retail channels are Filmworks titles made available on DVD?
16. Does DVD retail for Filmworks titles include Odeon foyer sales?
17. Through which rental channels are Filmworks titles made available on DVD?
18. Does DVD rental for Filmworks titles include Odeon Direct?
19. Which organization retains the UK TV rights for Filmworks titles?
20. What rights does Sky retain in relation to Filmworks titles?
21. Through which Sky services are Filmworks films made available to viewers?
22. Are Filmworks titles available through Sky Movies By Broadband?
23. Are Filmworks titles available through Sky Box Office?
24. In what order are Filmworks titles released across cinema, DVD, download services, box office, and television premiere?
25. When do Filmworks titles receive their UK Television Premiere on Sky Movies?
26. Which organization makes Filmworks titles available to Sky viewers at home?
27. Are Filmworks films intended for both cinema audiences and home audiences in the UK?
28. What relationship exists between Odeon Cinemas and British Sky Broadcasting in Filmworks?
29. What kinds of release channels are associated with Filmworks titles?
30. Which home-viewing platforms are used for Filmworks film distribution before the UK television premiere?
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

    class BusinessEntity(Organization):
        pass

    class JointVenture(BusinessEntity):
        pass

    class FilmDistributor(BusinessEntity):
        pass

    class Country(Thing):
        pass

    class Filmmaker(Thing):
        pass

    class AudienceGroup(Thing):
        pass

    class CinemaAudience(AudienceGroup):
        pass

    class HomeAudience(AudienceGroup):
        pass

    class SkyViewer(HomeAudience):
        pass

    class DistributionChannel(Thing):
        pass

    class CinemaChain(BusinessEntity, DistributionChannel):
        pass

    class OtherCinemaChain(CinemaChain):
        pass

    class RetailChannel(DistributionChannel):
        pass

    class RentalChannel(DistributionChannel):
        pass

    class HomeViewingService(DistributionChannel):
        pass

    class DownloadService(HomeViewingService):
        pass

    class BoxOfficeService(HomeViewingService):
        pass

    class TelevisionChannel(HomeViewingService):
        pass

    class Film(Thing):
        pass

    class FilmTitle(Film):
        pass

    class EntityName(Thing):
        pass

    class CollaborationName(EntityName):
        pass

    class Acronym(EntityName):
        pass

    class OrganizationAlias(EntityName):
        pass

    class hasJointVenturePartner(ObjectProperty):
        domain = [JointVenture]
        range = [Organization]

    class jointVenturesWith(ObjectProperty, SymmetricProperty):
        domain = [Organization]
        range = [Organization]

    class basedInCountry(ObjectProperty):
        domain = [BusinessEntity]
        range = [Country]

    class aliasFor(ObjectProperty):
        domain = [EntityName]
        range = [Thing]

    class operatesUnderName(ObjectProperty):
        domain = [BusinessEntity]
        range = [CollaborationName]

    class hasAcronym(ObjectProperty):
        domain = [BusinessEntity]
        range = [Acronym]

    class acquiresFilmTitlesFrom(ObjectProperty):
        domain = [FilmDistributor]
        range = [Filmmaker]

    class servesAudienceType(ObjectProperty):
        domain = [BusinessEntity]
        range = [AudienceGroup]

    class bringsFilmTitlesToCinemaAudienceIn(ObjectProperty):
        domain = [FilmDistributor]
        range = [Country]

    class bringsFilmTitlesToHomeAudienceIn(ObjectProperty):
        domain = [FilmDistributor]
        range = [Country]

    class usesTheatricalReleaseVenue(ObjectProperty):
        domain = [FilmDistributor]
        range = [CinemaChain]

    class usesDvdRetailChannel(ObjectProperty):
        domain = [FilmDistributor]
        range = [RetailChannel]

    class usesDvdRentalChannel(ObjectProperty):
        domain = [FilmDistributor]
        range = [RentalChannel]

    class usesHomeViewingService(ObjectProperty):
        domain = [FilmDistributor]
        range = [HomeViewingService]

    class hasTelevisionPremiereOn(ObjectProperty):
        domain = [FilmDistributor]
        range = [TelevisionChannel]

    class precedesChannel(ObjectProperty, TransitiveProperty):
        domain = [DistributionChannel]
        range = [DistributionChannel]

    class retainsTvRightsFor(ObjectProperty):
        domain = [Organization]
        range = [BusinessEntity]

    class retainsTvRightsInCountry(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class makesTitlesAvailableThrough(ObjectProperty):
        domain = [Organization]
        range = [HomeViewingService]

    class plannedFilmsPerYear(DataProperty, FunctionalProperty):
        domain = [FilmDistributor]
        range = [int]

    class FilmDistributionJointVenture(JointVenture, FilmDistributor):
        is_a = [
            hasJointVenturePartner.some(Organization),
            operatesUnderName.some(CollaborationName),
            hasAcronym.some(Acronym),
            basedInCountry.some(Country),
            acquiresFilmTitlesFrom.some(Filmmaker),
            servesAudienceType.some(CinemaAudience),
            servesAudienceType.some(HomeAudience),
            bringsFilmTitlesToCinemaAudienceIn.some(Country),
            bringsFilmTitlesToHomeAudienceIn.some(Country),
            usesTheatricalReleaseVenue.some(CinemaChain),
            usesTheatricalReleaseVenue.some(OtherCinemaChain),
            usesDvdRetailChannel.some(RetailChannel),
            usesDvdRentalChannel.some(RentalChannel),
            usesHomeViewingService.some(HomeViewingService),
            hasTelevisionPremiereOn.some(TelevisionChannel),
        ]

    OdeonSkyFilmworks = FilmDistributionJointVenture("OdeonSkyFilmworksEntity")
    OdeonSkyFilmworks.label = "Odeon Sky Filmworks"

    OdeonCinemas = CinemaChain("OdeonCinemasEntity")
    OdeonCinemas.label = "Odeon Cinemas"

    BritishSkyBroadcasting = BusinessEntity("BritishSkyBroadcastingEntity")
    BritishSkyBroadcasting.label = "British Sky Broadcasting"

    OdeonAndSkyFilmworksName = CollaborationName("OdeonAndSkyFilmworksQuotedName")
    OdeonAndSkyFilmworksName.label = "‘ Odeon and Sky Filmworks’"

    FilmworksAcronym = Acronym("FilmworksAcronymEntity")
    FilmworksAcronym.label = "FILMWORKS"

    SkyAcronym = OrganizationAlias("SkyAcronymEntity")
    SkyAcronym.label = "SKY"

    OdeonAcronym = OrganizationAlias("OdeonAcronymEntity")
    OdeonAcronym.label = "ODEON"

    SkyName = OrganizationAlias("SkyNameEntity")
    SkyName.label = "Sky"

    UkCountry = Country("UKCountryEntity")
    UkCountry.label = "UK"

    OdeonFoyerSales = RetailChannel("OdeonFoyerSalesChannel")
    OdeonFoyerSales.label = "ODEON foyer sales"

    OdeonDirect = RentalChannel("OdeonDirectService")
    OdeonDirect.label = "ODEON Direct"

    SkyMoviesByBroadband = DownloadService("SkyMoviesByBroadbandService")
    SkyMoviesByBroadband.label = "Sky Movies By Broadband"

    SkyBoxOffice = BoxOfficeService("SkyBoxOfficeService")
    SkyBoxOffice.label = "Sky Box Office"

    SkyMovies = TelevisionChannel("SkyMoviesChannel")
    SkyMovies.label = "Sky Movies"

    OdeonSkyFilmworks.hasJointVenturePartner = [OdeonCinemas, BritishSkyBroadcasting]
    OdeonSkyFilmworks.operatesUnderName = [OdeonAndSkyFilmworksName]
    OdeonSkyFilmworks.hasAcronym = [FilmworksAcronym]
    OdeonSkyFilmworks.basedInCountry = [UkCountry]
    OdeonSkyFilmworks.bringsFilmTitlesToCinemaAudienceIn = [UkCountry]
    OdeonSkyFilmworks.bringsFilmTitlesToHomeAudienceIn = [UkCountry]
    OdeonSkyFilmworks.usesTheatricalReleaseVenue = [OdeonCinemas]
    OdeonSkyFilmworks.usesDvdRetailChannel = [OdeonFoyerSales]
    OdeonSkyFilmworks.usesDvdRentalChannel = [OdeonDirect]
    OdeonSkyFilmworks.usesHomeViewingService = [SkyMoviesByBroadband, SkyBoxOffice]
    OdeonSkyFilmworks.hasTelevisionPremiereOn = [SkyMovies]
    OdeonSkyFilmworks.plannedFilmsPerYear = 6

    OdeonCinemas.jointVenturesWith = [BritishSkyBroadcasting]
    OdeonCinemas.precedesChannel = [OdeonFoyerSales, OdeonDirect]

    BritishSkyBroadcasting.jointVenturesWith = [OdeonCinemas]
    BritishSkyBroadcasting.retainsTvRightsFor = [OdeonSkyFilmworks]
    BritishSkyBroadcasting.retainsTvRightsInCountry = [UkCountry]
    BritishSkyBroadcasting.makesTitlesAvailableThrough = [SkyMoviesByBroadband, SkyBoxOffice]

    OdeonAndSkyFilmworksName.aliasFor = [OdeonSkyFilmworks]
    FilmworksAcronym.aliasFor = [OdeonSkyFilmworks]
    SkyAcronym.aliasFor = [BritishSkyBroadcasting]
    OdeonAcronym.aliasFor = [OdeonCinemas]
    SkyName.aliasFor = [BritishSkyBroadcasting]

    SkyMoviesByBroadband.precedesChannel = [SkyMovies]
    SkyBoxOffice.precedesChannel = [SkyMovies]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
