"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

What is Odeon and Sky Filmworks?
Which organizations formed Odeon and Sky Filmworks?
Is Odeon Sky Filmworks a joint venture?
What is the purpose of Odeon and Sky Filmworks?
What role does Odeon and Sky Filmworks play in the UK film industry?
Is Odeon and Sky Filmworks a UK-based film distributor?
Which film titles are signed directly from filmmakers by Odeon and Sky Filmworks?
How many films does Filmworks plan to sign up for release per year?
Which audiences are targeted by Odeon and Sky Filmworks?
Through which channels are Filmworks titles released?
Do Filmworks films receive a theatrical release at Odeon cinemas?
Are Filmworks films also released at other cinema chains?
Do Filmworks films have a DVD retail release?
Is Odeon foyer sales included in the DVD retail channel?
Do Filmworks films have a DVD rental release?
Is Odeon Direct included in the DVD rental channel?
What is the release sequence for films distributed by Filmworks?
Which organization retains the UK TV rights for Filmworks films?
What rights does Sky retain for Filmworks films?
Through which Sky services are Filmworks films made available to viewers?
Are Filmworks films available through Sky Movies By Broadband?
Are Filmworks films available through Sky Box Office?
Do Filmworks films become available on Sky services before their UK television premiere?
On which channel do Filmworks films have their UK television premiere?
What relationship exists between Odeon Cinemas and British Sky Broadcasting in Filmworks?
Which company is responsible for cinema exhibition in the Filmworks distribution model?
Which company is responsible for UK television rights in the Filmworks distribution model?
Can a Filmworks film be released in cinemas and at home?
Are Filmworks titles distributed directly from filmmakers to UK audiences through this collaboration?
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
    Event,
    NonAgentiveSocialObject,
    SocialAgent,
    Society,
    SpaceRegion,
)
from og_sandbox_with_core.core.properties import constantPartOf


with core:
    class Organization(Society):
        pass


    class CinemaChain(Organization):
        pass


    class OtherCinemaChain(CinemaChain):
        pass


    class BroadcastingCompany(Organization):
        pass


    class FilmDistributor(Organization):
        pass


    class JointVenture(Organization):
        pass


    class FilmDistributionJointVenture(JointVenture, FilmDistributor):
        pass


    class AudienceGroup(Society):
        pass


    class UnitedKingdomAudience(AudienceGroup):
        pass


    class SkyViewerGroup(AudienceGroup):
        pass


    class Filmmaker(SocialAgent):
        pass


    class FilmTitle(NonAgentiveSocialObject):
        pass


    class DistributionChannel(NonAgentiveSocialObject):
        pass


    class CinemaReleaseChannel(DistributionChannel):
        pass


    class HomeReleaseChannel(DistributionChannel):
        pass


    class TheatricalReleaseChannel(CinemaReleaseChannel):
        pass


    class DvdRetailChannel(HomeReleaseChannel):
        pass


    class DvdRentalChannel(HomeReleaseChannel):
        pass


    class DownloadService(HomeReleaseChannel):
        pass


    class PayPerViewService(HomeReleaseChannel):
        pass


    class TelevisionChannel(HomeReleaseChannel):
        pass


    class TelevisionPremiere(Event):
        pass


    class TelevisionRight(NonAgentiveSocialObject):
        pass


    class Country(SpaceRegion):
        pass


    class hasVenturePartner(ObjectProperty):
        domain = [JointVenture]
        range = [Organization]


    class collaboratesWith(ObjectProperty, SymmetricProperty):
        domain = [Organization]
        range = [Organization]


    class targetsAudience(ObjectProperty):
        domain = [Organization]
        range = [AudienceGroup]


    class targetsCountry(ObjectProperty):
        domain = [Organization]
        range = [Country]


    class signsTitlesDirectlyFrom(ObjectProperty):
        domain = [FilmDistributor]
        range = [Filmmaker]


    class distributesThrough(ObjectProperty):
        domain = [FilmDistributor]
        range = [DistributionChannel]


    class exhibitedAt(ObjectProperty):
        domain = [FilmDistributor]
        range = [CinemaChain]


    class retainsRight(ObjectProperty):
        domain = [Organization]
        range = [TelevisionRight]


    class makesAvailableThrough(ObjectProperty):
        domain = [Organization]
        range = [HomeReleaseChannel]


    class premieresOn(ObjectProperty):
        domain = [FilmDistributor]
        range = [TelevisionChannel]


    class cinemaExhibitionBy(ObjectProperty):
        domain = [FilmDistributionJointVenture]
        range = [CinemaChain]


    class televisionRightsBy(ObjectProperty):
        domain = [FilmDistributionJointVenture]
        range = [BroadcastingCompany]


    class includedInReleaseChannel(constantPartOf):
        domain = [DistributionChannel]
        range = [DistributionChannel]


    class precedesReleaseChannel(ObjectProperty):
        domain = [DistributionChannel]
        range = [DistributionChannel]


    class hasTelevisionPremiere(ObjectProperty):
        domain = [FilmDistributor]
        range = [TelevisionPremiere]


    class occursOnChannel(ObjectProperty):
        domain = [TelevisionPremiere]
        range = [TelevisionChannel]


    class precedesPremiere(ObjectProperty):
        domain = [DistributionChannel]
        range = [TelevisionPremiere]


    class plannedFilmsPerYear(DataProperty, FunctionalProperty):
        domain = [FilmDistributor]
        range = [int]


    JointVenture.is_a.append(hasVenturePartner.some(Organization))
    FilmDistributionJointVenture.is_a.extend([
        hasVenturePartner.some(Organization),
        targetsAudience.some(UnitedKingdomAudience),
        targetsCountry.some(Country),
        signsTitlesDirectlyFrom.some(Filmmaker),
        distributesThrough.some(TheatricalReleaseChannel),
        distributesThrough.some(DvdRetailChannel),
        distributesThrough.some(DvdRentalChannel),
        distributesThrough.some(HomeReleaseChannel),
        exhibitedAt.some(CinemaChain),
        exhibitedAt.some(OtherCinemaChain),
        hasTelevisionPremiere.some(TelevisionPremiere),
    ])
    TheatricalReleaseChannel.is_a.extend([
        precedesReleaseChannel.some(DvdRetailChannel),
        precedesReleaseChannel.some(DvdRentalChannel),
    ])
    DownloadService.is_a.append(precedesPremiere.some(TelevisionPremiere))
    PayPerViewService.is_a.append(precedesPremiere.some(TelevisionPremiere))
    TelevisionPremiere.is_a.append(occursOnChannel.some(TelevisionChannel))

    filmworks = FilmDistributionJointVenture("OdeonSkyFilmworks")
    filmworks.label = [
        "Odeon Sky Filmworks",
        "Odeon and Sky Filmworks",
        "FILMWORKS",
    ]

    odeonCinemas = CinemaChain("OdeonCinemas")
    odeonCinemas.label = ["Odeon Cinemas", "ODEON"]

    britishSkyBroadcasting = BroadcastingCompany("BritishSkyBroadcasting")
    britishSkyBroadcasting.label = ["British Sky Broadcasting", "SKY", "Sky"]

    unitedKingdom = Country("UK")
    unitedKingdom.label = "UK"

    ukAudiences = UnitedKingdomAudience("UKAudiences")
    ukAudiences.label = "UK audiences"

    skyViewers = SkyViewerGroup("SkyViewers")
    skyViewers.label = "Sky viewers"

    theatricalRelease = TheatricalReleaseChannel("TheatricalRelease")
    theatricalRelease.label = "theatrical release"

    dvdRetail = DvdRetailChannel("DVDRetail")
    dvdRetail.label = "DVD retail"

    dvdRental = DvdRentalChannel("DVDRental")
    dvdRental.label = "DVD rental"

    odeonFoyerSales = DvdRetailChannel("OdeonFoyerSales")
    odeonFoyerSales.label = "ODEON foyer sales"

    odeonDirect = DvdRentalChannel("OdeonDirect")
    odeonDirect.label = "ODEON Direct"

    skyMoviesByBroadband = DownloadService("SkyMoviesByBroadband")
    skyMoviesByBroadband.label = "Sky Movies By Broadband"

    skyBoxOffice = PayPerViewService("SkyBoxOffice")
    skyBoxOffice.label = "Sky Box Office"

    skyMovies = TelevisionChannel("SkyMovies")
    skyMovies.label = "Sky Movies"

    ukTvRights = TelevisionRight("UKTVRights")
    ukTvRights.label = "UK TV rights"

    ukTelevisionPremiere = TelevisionPremiere("UKTelevisionPremiere")
    ukTelevisionPremiere.label = "UK Television Premiere"

    filmworks.hasVenturePartner = [odeonCinemas, britishSkyBroadcasting]
    filmworks.targetsAudience = [ukAudiences]
    filmworks.targetsCountry = [unitedKingdom]
    filmworks.distributesThrough = [
        theatricalRelease,
        dvdRetail,
        dvdRental,
        skyMoviesByBroadband,
        skyBoxOffice,
    ]
    filmworks.exhibitedAt = [odeonCinemas]
    filmworks.cinemaExhibitionBy = [odeonCinemas]
    filmworks.televisionRightsBy = [britishSkyBroadcasting]
    filmworks.hasTelevisionPremiere = [ukTelevisionPremiere]
    filmworks.premieresOn = [skyMovies]
    filmworks.plannedFilmsPerYear = 6

    odeonCinemas.collaboratesWith = [britishSkyBroadcasting]

    britishSkyBroadcasting.targetsAudience = [skyViewers]
    britishSkyBroadcasting.targetsCountry = [unitedKingdom]
    britishSkyBroadcasting.retainsRight = [ukTvRights]
    britishSkyBroadcasting.makesAvailableThrough = [
        skyMoviesByBroadband,
        skyBoxOffice,
    ]

    odeonFoyerSales.includedInReleaseChannel = [dvdRetail]
    odeonDirect.includedInReleaseChannel = [dvdRental]

    theatricalRelease.precedesReleaseChannel = [dvdRetail, dvdRental]
    skyMoviesByBroadband.precedesPremiere = [ukTelevisionPremiere]
    skyBoxOffice.precedesPremiere = [ukTelevisionPremiere]
    ukTelevisionPremiere.occursOnChannel = [skyMovies]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
