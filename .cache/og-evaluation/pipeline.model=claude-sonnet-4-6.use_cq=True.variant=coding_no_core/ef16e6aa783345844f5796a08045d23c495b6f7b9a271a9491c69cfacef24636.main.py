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
12. How does the AANR use its membership fees?
13. In which countries does the AANR lobby governments?
14. What is the AANR's rank among organizations of its kind in North America?
15. What types of facilities are affiliated with the AANR?
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
    # ── Entity classes ────────────────────────────────────────────────────
    class Organization(Thing): pass
    class NaturistOrganization(Organization): pass

    class GeographicArea(Thing): pass
    class Country(GeographicArea): pass
    class GeographicRegion(GeographicArea): pass
    class IslandTerritory(GeographicArea): pass

    class NudistFacility(Thing): pass
    class Resort(NudistFacility): pass
    class Club(NudistFacility): pass
    class NudistBusiness(NudistFacility): pass
    class Campground(NudistFacility): pass

    class NudistSetting(Thing): pass
    class NudeBeach(NudistSetting): pass
    class PublicLand(NudistSetting): pass
    class PrivateProperty(NudistSetting): pass

    # ── Properties ───────────────────────────────────────────────────────
    class fullName(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class acronym(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range  = [Country]

    class foundedInYear(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [int]

    class previousName(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class affiliatedFacilityCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [int]

    class memberCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [int]

    class servesMembers(ObjectProperty):
        domain = [Organization]
        range  = [GeographicArea]

    class affiliatedWith(ObjectProperty):
        domain = [NudistFacility]
        range  = [Organization]

    class lobbiesGovernmentIn(ObjectProperty):
        domain = [Organization]
        range  = [Country]

    class rankAmongKind(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class largestInRegion(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range  = [GeographicArea]

    class promotes(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class protectsRights(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class approvedSettings(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    class usesMembershipFeesFor(DataProperty, FunctionalProperty):
        domain = [Organization]
        range  = [str]

    # ── Named individuals ─────────────────────────────────────────────────

    # Geographic areas
    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    canada = Country("Canada")
    canada.label = "Canada"

    mexico = Country("Mexico")
    mexico.label = "Mexico"

    frenchWestIndies = IslandTerritory("FrenchWestIndies")
    frenchWestIndies.label = "French West Indies"

    virginIslands = IslandTerritory("VirginIslands")
    virginIslands.label = "Virgin Islands"

    stMartin = IslandTerritory("StMartin")
    stMartin.label = "St. Martin"

    northAmerica = GeographicRegion("NorthAmerica")
    northAmerica.label = "North America"

    # Organization
    aanr = NaturistOrganization("AANR")
    aanr.label = "American Association for Nude Recreation"
    aanr.fullName = "American Association for Nude Recreation"
    aanr.acronym = "AANR"
    aanr.basedIn = unitedStates
    aanr.foundedInYear = 1931
    aanr.previousName = "American Sunbathing Association"
    aanr.affiliatedFacilityCount = 200
    aanr.memberCount = 30000
    aanr.servesMembers = [unitedStates, canada, mexico, frenchWestIndies, virginIslands, stMartin]
    aanr.lobbiesGovernmentIn = [unitedStates, canada]
    aanr.rankAmongKind = "largest, longest-established"
    aanr.largestInRegion = northAmerica
    aanr.promotes = "benefits of wholesome nude family recreation"
    aanr.protectsRights = "rights of nudists in appropriate settings"
    aanr.approvedSettings = "sanctioned nude beaches, public lands, homes, private backyards, AANR-affiliated clubs, campgrounds and resorts"
    aanr.usesMembershipFeesFor = "political activity by campaigning and lobbying governments"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
