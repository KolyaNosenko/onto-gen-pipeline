"""
=== TASK INPUT ===
Source text:
Odeon Sky Filmworks is a joint venture between Odeon Cinemas and British Sky Broadcasting designed to bring film titles to UK audiences in cinemas and at home . Called ‘ Odeon and Sky Filmworks’ ( FILMWORKS ) , the collaboration between SKY and ODEON will act as a UK - based film distributor , signing up titles directly from filmmakers . Filmworks plans initially to sign up to six films for release per year . Films will have a theatrical release at ODEON , as well as at other cinema chains , prior to DVD retail ( including ODEON foyer sales ) and DVD rental ( including ODEON Direct ) . Sky will retain all UK TV rights – and will make the films available to Sky viewers across its download service – Sky Movies By Broadband , as well as Sky Box Office , before their UK Television Premiere on Sky Movies .

1. What is Odeon Sky Filmworks a joint venture between?
2. What is the purpose of the joint venture between Odeon Cinemas and British Sky Broadcasting?
3. What is the official name of the collaboration between SKY and ODEON?
4. What role does Filmworks act as in the UK?
5. How many films does Filmworks plan to sign up for release per year initially?
6. Where will films have their theatrical release?
7. What distribution channels are available for films after theatrical release?
8. What TV rights does Sky retain for the films?
9. Through which services will Sky make films available to its viewers?
10. Which Sky service allows viewers to download films?
11. Where will the UK Television Premiere of the films take place?
12. What sales channels are available for DVD retail?
13. What is Sky Box Office's role in the distribution of Filmworks titles?
14. Which cinema chains will screen the Filmworks titles?
15. What is the sequence of release windows for Filmworks titles?
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
    Society, NonAgentiveSocialObject, AgentivePhysicalObject,
)


with core:
    # --- Entity classes ---

    # Agentive social collectives (organisations)
    class JointVenture(Society): pass
    class CinemaChain(Society): pass
    class Broadcaster(Society): pass
    class FilmDistributor(Society): pass

    # Persons who create films (agentive physical objects)
    class Filmmaker(AgentivePhysicalObject): pass

    # Non-agentive social objects
    class Film(NonAgentiveSocialObject): pass
    class DistributionChannel(NonAgentiveSocialObject): pass
    class CinemaReleaseChannel(DistributionChannel): pass
    class DVDRetailChannel(DistributionChannel): pass
    class DVDRentalChannel(DistributionChannel): pass
    class BroadbandDownloadService(DistributionChannel): pass
    class PayPerViewService(DistributionChannel): pass
    class TVChannel(DistributionChannel): pass
    class TVRights(NonAgentiveSocialObject): pass
    class Territory(NonAgentiveSocialObject): pass

    # --- Object and data properties ---

    class hasPartner(ObjectProperty):
        """Joint venture has a partner organisation."""
        domain = [JointVenture]
        range  = [Society]

    class distributes(ObjectProperty):
        """A film distributor distributes a film."""
        domain = [FilmDistributor]
        range  = [Film]

    class signsFilmFrom(ObjectProperty):
        """A film distributor signs a title directly from a filmmaker."""
        domain = [FilmDistributor]
        range  = [Filmmaker]

    class releasedVia(ObjectProperty):
        """A film is released via a distribution channel."""
        domain = [Film]
        range  = [DistributionChannel]

    class theatricallyReleasedAt(ObjectProperty):
        """A film has its theatrical release at a cinema chain."""
        domain = [Film]
        range  = [CinemaChain]

    class theatricalVenue(ObjectProperty):
        """Primary cinema chain used by a film distributor for theatrical release."""
        domain = [FilmDistributor]
        range  = [CinemaChain]

    class offersService(ObjectProperty):
        """A broadcaster offers a distribution channel service to its viewers."""
        domain = [Broadcaster]
        range  = [DistributionChannel]

    class retainsTVRights(ObjectProperty):
        """A broadcaster retains TV rights over a set of films."""
        domain = [Broadcaster]
        range  = [TVRights]

    class coversTerritory(ObjectProperty):
        """TV rights cover a geographic/political territory."""
        domain = [TVRights]
        range  = [Territory]

    class basedIn(ObjectProperty):
        """A film distributor is based in a territory."""
        domain = [FilmDistributor]
        range  = [Territory]

    class precedes(ObjectProperty, TransitiveProperty):
        """One distribution channel / release window precedes another."""
        domain = [DistributionChannel]
        range  = [DistributionChannel]

    class annualFilmCount(DataProperty, FunctionalProperty):
        """Number of films a distributor plans to release per year."""
        domain = [FilmDistributor]
        range  = [int]

    # Release-window ordering captured as class-level restrictions
    # (theatrical → DVD retail & rental; digital download & pay-per-view → TV premiere)
    CinemaReleaseChannel.is_a.append(precedes.some(DVDRetailChannel))
    CinemaReleaseChannel.is_a.append(precedes.some(DVDRentalChannel))
    BroadbandDownloadService.is_a.append(precedes.some(TVChannel))
    PayPerViewService.is_a.append(precedes.some(TVChannel))

    # --- Named individuals ---

    # Geographic / political territory
    UK_inst = Territory("UK_inst")
    UK_inst.label = "UK"

    # Organisations
    OdeonCinemas_inst = CinemaChain("OdeonCinemas_inst")
    OdeonCinemas_inst.label = "Odeon Cinemas"

    BritishSkyBroadcasting_inst = Broadcaster("BritishSkyBroadcasting_inst")
    BritishSkyBroadcasting_inst.label = "British Sky Broadcasting"

    OdeonSkyFilmworks_inst = JointVenture("OdeonSkyFilmworks_inst")
    OdeonSkyFilmworks_inst.label = "Odeon Sky Filmworks"
    OdeonSkyFilmworks_inst.is_a.append(FilmDistributor)
    OdeonSkyFilmworks_inst.hasPartner.append(OdeonCinemas_inst)
    OdeonSkyFilmworks_inst.hasPartner.append(BritishSkyBroadcasting_inst)
    OdeonSkyFilmworks_inst.basedIn.append(UK_inst)
    OdeonSkyFilmworks_inst.annualFilmCount = 6
    OdeonSkyFilmworks_inst.theatricalVenue.append(OdeonCinemas_inst)

    # Named distribution channels and services
    SkyMoviesByBroadband_inst = BroadbandDownloadService("SkyMoviesByBroadband_inst")
    SkyMoviesByBroadband_inst.label = "Sky Movies By Broadband"

    SkyBoxOffice_inst = PayPerViewService("SkyBoxOffice_inst")
    SkyBoxOffice_inst.label = "Sky Box Office"

    SkyMovies_inst = TVChannel("SkyMovies_inst")
    SkyMovies_inst.label = "Sky Movies"

    OdeonDirect_inst = DVDRentalChannel("OdeonDirect_inst")
    OdeonDirect_inst.label = "ODEON Direct"

    # TV rights
    UKTVRights_inst = TVRights("UKTVRights_inst")
    UKTVRights_inst.label = "UK TV rights"
    UKTVRights_inst.coversTerritory.append(UK_inst)

    BritishSkyBroadcasting_inst.retainsTVRights.append(UKTVRights_inst)
    BritishSkyBroadcasting_inst.offersService.append(SkyMoviesByBroadband_inst)
    BritishSkyBroadcasting_inst.offersService.append(SkyBoxOffice_inst)
    BritishSkyBroadcasting_inst.offersService.append(SkyMovies_inst)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
