"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

1. What is the full name of the AANR?
2. What type of organization is the AANR?
3. In which country is the AANR based?
4. When was the AANR founded?
5. What was the previous name of the AANR?
6. How many nudist resorts, clubs, and businesses are affiliated with the AANR?
7. How many members does the AANR serve?
8. In which countries does the AANR have members?
9. What does the AANR promote?
10. What rights does the AANR work to protect?
11. What types of settings does the AANR consider appropriate for nudism?
12. How does the AANR use its collected membership fees?
13. In which countries does the AANR engage in lobbying activities?
14. What is the largest naturist organization in North America?
15. What types of venues are affiliated with the AANR?
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
    Society,
    NonAgentiveSocialObject,
    NonAgentivePhysicalObject,
)


with core:
    # --- Entity Classes ---

    class NaturistOrganization(Society):
        """A collective organization that promotes naturism / nude recreation."""
        pass

    class Country(Society):
        """A sovereign nation-state."""
        pass

    class OverseasTerritory(NonAgentiveSocialObject):
        """A non-sovereign territory administered by another state."""
        pass

    class GeographicRegion(NonAgentivePhysicalObject):
        """A large physical geographic area such as a continent or subcontinent."""
        pass

    class AffiliatedVenue(NonAgentivePhysicalObject):
        """A physical venue affiliated with a naturist organization."""
        pass

    class NudistResort(AffiliatedVenue):
        """A resort that accommodates nude recreation."""
        pass

    class NudistClub(AffiliatedVenue):
        """A club that facilitates nude recreation for its members."""
        pass

    class NudistBusiness(AffiliatedVenue):
        """A business that operates in the naturist sector."""
        pass

    class Campground(AffiliatedVenue):
        """A campground that accommodates nude recreation."""
        pass

    class SanctionedNudeBeach(NonAgentivePhysicalObject):
        """A beach officially sanctioned for nude recreation."""
        pass

    class PublicLand(NonAgentivePhysicalObject):
        """Public land designated for nude recreation."""
        pass

    # --- Properties ---

    class basedIn(ObjectProperty, FunctionalProperty):
        """The country in which the organization is headquartered."""
        domain = [NaturistOrganization]
        range = [Country]

    class operatesIn(ObjectProperty):
        """The geographic region in which the organization is active."""
        domain = [NaturistOrganization]
        range = [GeographicRegion]

    class foundingYear(DataProperty, FunctionalProperty):
        """The year in which the organization was founded."""
        domain = [NaturistOrganization]
        range = [int]

    class previousName(DataProperty, FunctionalProperty):
        """A former official name of the organization."""
        domain = [NaturistOrganization]
        range = [str]

    class affiliatedVenueCount(DataProperty, FunctionalProperty):
        """Approximate number of venues affiliated with the organization."""
        domain = [NaturistOrganization]
        range = [int]

    class memberCount(DataProperty, FunctionalProperty):
        """Approximate number of members served by the organization."""
        domain = [NaturistOrganization]
        range = [int]

    class hasMembersIn(ObjectProperty):
        """Links the organization to a country or territory where it has members."""
        domain = [NaturistOrganization]

    class lobbiesIn(ObjectProperty):
        """Links the organization to a country where it lobbies the government."""
        domain = [NaturistOrganization]
        range = [Country]

    class affiliatedWith(ObjectProperty):
        """Links a venue to the naturist organization it is affiliated with."""
        domain = [AffiliatedVenue]
        range = [NaturistOrganization]

    class promotes(DataProperty, FunctionalProperty):
        """A brief description of what the organization promotes."""
        domain = [NaturistOrganization]
        range = [str]

    # --- Named Individuals ---

    aanr = NaturistOrganization("AANR")
    aanr.label = "American Association for Nude Recreation"
    aanr.previousName = "American Sunbathing Association"
    aanr.foundingYear = 1931
    aanr.affiliatedVenueCount = 200
    aanr.memberCount = 30000
    aanr.promotes = "wholesome nude family recreation"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    northAmerica = GeographicRegion("NorthAmerica")
    northAmerica.label = "North America"

    canada = Country("Canada")
    canada.label = "Canada"

    mexico = Country("Mexico")
    mexico.label = "Mexico"

    frenchWestIndies = OverseasTerritory("FrenchWestIndies")
    frenchWestIndies.label = "French West Indies"

    virginIslands = OverseasTerritory("VirginIslands")
    virginIslands.label = "Virgin Islands"

    stMartin = OverseasTerritory("StMartin")
    stMartin.label = "St. Martin"

    # Relational property assignments
    aanr.basedIn = unitedStates
    aanr.operatesIn.append(northAmerica)
    aanr.hasMembersIn.append(unitedStates)
    aanr.hasMembersIn.append(canada)
    aanr.hasMembersIn.append(mexico)
    aanr.hasMembersIn.append(frenchWestIndies)
    aanr.hasMembersIn.append(virginIslands)
    aanr.hasMembersIn.append(stMartin)
    aanr.lobbiesIn.append(unitedStates)
    aanr.lobbiesIn.append(canada)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
