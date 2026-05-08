"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

1. What is the American Association for Nude Recreation (AANR)?

2. When was the AANR founded and under what name?

3. How many nudist resorts, clubs, and businesses are affiliated with AANR?

4. How many members does AANR serve?

5. In which geographic regions does AANR operate?

6. What are the primary objectives and activities of AANR?

7. What types of settings does AANR recognize as appropriate for nude recreation?

8. How does AANR use its membership fees?

9. What political activities does AANR engage in?

10. Is AANR the largest naturist organization in North America?

11. What was the previous name of AANR before 1931?

12. What rights does AANR work to protect?

13. Which countries and territories are served by AANR members?

14. What venues and locations are promoted by AANR for nude recreation?
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
        """Base class for organizations"""
        pass

    class NaturistOrganization(Organization):
        """Organization focused on naturism/nudism"""
        pass

    class Country(Thing):
        """A sovereign nation"""
        pass

    class Territory(Thing):
        """A geographic territory or region"""
        pass

    class GeographicRegion(Thing):
        """A larger geographic region (e.g., continent)"""
        pass

    class VenueType(Thing):
        """Type of venue for nude recreation"""
        pass

    class PoliticalActivity(Thing):
        """Political activity or campaign"""
        pass

    class Recreation(Thing):
        """Type of recreation activity"""
        pass

    class NudistRights(Thing):
        """Rights related to nudism"""
        pass

    # Properties
    class foundingYear(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class formerName(DataProperty):
        domain = [Organization]
        range = [str]

    class affiliatedEntitiesCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class memberCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class operatesIn(ObjectProperty):
        domain = [Organization]
        range = [Country, Territory, GeographicRegion]

    class recognizesVenueType(ObjectProperty):
        domain = [Organization]
        range = [VenueType]

    class protectsRights(ObjectProperty):
        domain = [Organization]
        range = [NudistRights]

    class engagesInPoliticalActivity(ObjectProperty):
        domain = [Organization]
        range = [PoliticalActivity]

    class promotes(ObjectProperty):
        domain = [Organization]
        range = [Recreation]

    class isLargestOfItsKindIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [GeographicRegion]

    class isLongestEstablishedOfItsKindIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [GeographicRegion]

    # Named instances from the source text
    
    # Main organization instance
    aanr = NaturistOrganization("AANR")
    aanr.label = "American Association for Nude Recreation (AANR)"
    aanr.foundingYear = 1931
    aanr.formerName = ["American Sunbathing Association"]
    aanr.affiliatedEntitiesCount = 200
    aanr.memberCount = 30000

    # Geographic locations where AANR operates
    united_states = Country("UnitedStates")
    united_states.label = "United States"

    canada = Country("Canada")
    canada.label = "Canada"

    mexico = Country("Mexico")
    mexico.label = "Mexico"

    french_west_indies = Territory("FrenchWestIndies")
    french_west_indies.label = "French West Indies"

    virgin_islands = Territory("VirginIslands")
    virgin_islands.label = "Virgin Islands"

    st_martin = Territory("StMartin")
    st_martin.label = "St. Martin"

    north_america = GeographicRegion("NorthAmerica")
    north_america.label = "North America"

    # Link AANR to geographic regions where it operates
    aanr.operatesIn = [united_states, canada, mexico, french_west_indies, virgin_islands, st_martin]
    aanr.isLargestOfItsKindIn = north_america
    aanr.isLongestEstablishedOfItsKindIn = north_america

    # Venue types recognized by AANR for nude recreation
    nude_beaches = VenueType("NudistBeaches")
    nude_beaches.label = "Sanctioned nude beaches"

    public_lands = VenueType("PublicLands")
    public_lands.label = "Public lands set aside for nude recreation"

    homes = VenueType("Homes")
    homes.label = "Homes"

    private_backyards = VenueType("PrivateBackyards")
    private_backyards.label = "Private backyards"

    affiliated_clubs = VenueType("AffiliatedClubs")
    affiliated_clubs.label = "AANR-affiliated clubs"

    campgrounds = VenueType("Campgrounds")
    campgrounds.label = "Campgrounds"

    resorts = VenueType("Resorts")
    resorts.label = "Resorts"

    aanr.recognizesVenueType = [nude_beaches, public_lands, homes, private_backyards, affiliated_clubs, campgrounds, resorts]

    # Rights protected by AANR
    nudist_rights = NudistRights("RightsOfNudists")
    nudist_rights.label = "Rights of nudists"

    aanr.protectsRights = [nudist_rights]

    # Recreation activity promoted by AANR
    wholesome_recreation = Recreation("WholesomeNudeRecreation")
    wholesome_recreation.label = "Wholesome nude family recreation"

    aanr.promotes = [wholesome_recreation]

    # Political activities engaged in by AANR
    campaigning = PoliticalActivity("Campaigning")
    campaigning.label = "Campaigning to allow nudism in the US and Canada"

    lobbying = PoliticalActivity("Lobbying")
    lobbying.label = "Lobbying governments"

    aanr.engagesInPoliticalActivity = [campaigning, lobbying]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
