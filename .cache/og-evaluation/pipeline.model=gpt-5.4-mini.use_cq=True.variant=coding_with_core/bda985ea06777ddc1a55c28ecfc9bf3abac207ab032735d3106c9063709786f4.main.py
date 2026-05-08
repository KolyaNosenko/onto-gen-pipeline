"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

1. What is the full name of AANR?
2. What type of organization is AANR?
3. In which country is AANR based?
4. When was AANR founded?
5. What was AANR’s previous name?
6. What is AANR’s position among naturist organizations in North America?
7. How many resorts, clubs, and businesses are affiliated with AANR?
8. How many members does AANR serve?
9. In which countries and territories does AANR have members?
10. What is the purpose of AANR?
11. What benefits does AANR promote?
12. What rights does AANR work to protect?
13. In what settings does AANR support nudism?
14. What kinds of places are considered appropriate settings for nudism according to AANR?
15. How does AANR use a portion of its membership fees?
16. In which countries does AANR campaign and lobby governments?
17. Does AANR affiliate with clubs, campgrounds, and resorts?
18. Is AANR active in political lobbying related to nudism?
19. Does AANR protect nudists’ rights on public lands set aside for that use?
20. Does AANR support wholesome nude family recreation?
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
    Abstract,
    AgentivePhysicalObject,
    AgentiveSocialObject,
    NonAgentivePhysicalObject,
    Process,
    Region,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Organization(AgentiveSocialObject):
        label = ["organization"]

    class NaturistOrganization(Organization):
        label = ["naturist organization"]

    class OrganizationName(Abstract):
        label = ["organization name"]

    class Continent(Region):
        label = ["continent"]

    class Country(Region):
        label = ["country"]

    class Territory(Region):
        label = ["territory"]

    class Setting(NonAgentivePhysicalObject):
        label = ["setting"]

    class Beach(Setting):
        label = ["beach"]

    class SanctionedNudeBeach(Beach):
        label = ["sanctioned nude beach"]

    class PublicLand(Setting):
        label = ["public land"]

    class PublicLandSetAsideForThatUse(PublicLand):
        label = ["public land set aside for that use"]

    class Home(Setting):
        label = ["home"]

    class PrivateBackyard(Setting):
        label = ["private backyard"]

    class Club(Setting):
        label = ["club"]

    class AANRAffiliatedClub(Club):
        label = ["AANR-affiliated club"]

    class Campground(Setting):
        label = ["campground"]

    class AANRAffiliatedCampground(Campground):
        label = ["AANR-affiliated campground"]

    class Resort(Setting):
        label = ["resort"]

    class AANRAffiliatedResort(Resort):
        label = ["AANR-affiliated resort"]

    class Business(Setting):
        label = ["business"]

    class AANRAffiliatedBusiness(Business):
        label = ["AANR-affiliated business"]

    class Government(Organization):
        label = ["government"]

    class Benefit(Abstract):
        label = ["benefit"]

    class RightsOfNudists(Abstract):
        label = ["rights of nudists"]

    class Nudism(Abstract):
        label = ["nudism"]

    class Nudist(AgentivePhysicalObject):
        label = ["nudist"]

    class WholesomeNudeFamilyRecreation(Process):
        label = ["wholesome nude family recreation"]

    class PoliticalActivity(Process):
        label = ["political activity"]

    class Campaigning(PoliticalActivity):
        label = ["campaigning"]

    class Lobbying(PoliticalActivity):
        label = ["lobbying"]

    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Country]

    class previousName(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [OrganizationName]

    class servesMembersIn(ObjectProperty):
        domain = [Organization]
        range = [Region]

    class campaignsInCountry(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class lobbiesInCountry(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class affiliatedWith(ObjectProperty):
        domain = [Setting]
        range = [NaturistOrganization]

    class supportsNudismIn(ObjectProperty):
        domain = [Organization]
        range = [Setting]

    class promotesBenefitOf(ObjectProperty):
        domain = [Organization]
        range = [Benefit]

    class worksToProtect(ObjectProperty):
        domain = [Organization]
        range = [RightsOfNudists]

    class usesMembershipFeesFor(ObjectProperty):
        domain = [Organization]
        range = [PoliticalActivity]

    class foundedInYear(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class memberCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class memberCountDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class affiliateCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class affiliateCountDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class isLargestInNorthAmerica(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class isLongestEstablishedInNorthAmerica(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class positionDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class purposeDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class benefitsPromotedDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class rightsProtectedDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class supportedSettingsDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    class membershipFeesUseDescription(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]

    AANR = NaturistOrganization("AANR")
    AANR.label = ["American Association for Nude Recreation ( AANR )", "AANR"]
    AANR.basedIn = UnitedStates = Country("UnitedStates")
    UnitedStates.label = ["United States", "US"]
    NorthAmerica = Continent("NorthAmerica")
    NorthAmerica.label = ["North America"]

    Canada = Country("Canada")
    Canada.label = ["Canada"]
    Mexico = Country("Mexico")
    Mexico.label = ["Mexico"]
    FrenchWestIndies = Territory("FrenchWestIndies")
    FrenchWestIndies.label = ["French West Indies"]
    VirginIslands = Territory("VirginIslands")
    VirginIslands.label = ["Virgin Islands"]
    StMartin = Territory("StMartin")
    StMartin.label = ["St. Martin"]

    UnitedStates.partOf.append(NorthAmerica)
    Canada.partOf.append(NorthAmerica)
    Mexico.partOf.append(NorthAmerica)
    FrenchWestIndies.partOf.append(NorthAmerica)
    VirginIslands.partOf.append(NorthAmerica)
    StMartin.partOf.append(NorthAmerica)

    AmericanSunbathingAssociation = OrganizationName("AmericanSunbathingAssociation")
    AmericanSunbathingAssociation.label = ["American Sunbathing Association"]
    AANR.previousName = AmericanSunbathingAssociation

    AANR.foundedInYear = 1931
    AANR.memberCount = 30000
    AANR.memberCountDescription = "over 30,000"
    AANR.affiliateCount = 200
    AANR.affiliateCountDescription = "approximately 200"
    AANR.isLargestInNorthAmerica = True
    AANR.isLongestEstablishedInNorthAmerica = True
    AANR.positionDescription = "largest, longest-established organization of its kind in North America"
    AANR.purposeDescription = "promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings"
    AANR.benefitsPromotedDescription = "the benefits of wholesome nude family recreation"
    AANR.rightsProtectedDescription = "the rights of nudists in appropriate settings"
    AANR.supportedSettingsDescription = "sanctioned nude beaches and public lands set aside for that use; as well as homes, private backyards, plus AANR-affiliated clubs, campgrounds and resorts"
    AANR.membershipFeesUseDescription = "a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada"
    AANR.servesMembersIn = [UnitedStates, Canada, Mexico, FrenchWestIndies, VirginIslands, StMartin]
    AANR.campaignsInCountry = [UnitedStates, Canada]
    AANR.lobbiesInCountry = [UnitedStates, Canada]




graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
