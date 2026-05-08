"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

What is the full name of AANR?
What does the acronym AANR stand for?
What type of organization is the American Association for Nude Recreation?
Where is AANR based?
Is AANR a naturist organization?
Is AANR the largest organization of its kind in North America?
Is AANR the longest-established organization of its kind in North America?
When was AANR founded?
What was the previous name of AANR?
Under what name was AANR originally founded?
How many nudist resorts, clubs, and businesses are affiliated with AANR?
How many members does AANR serve?
In which countries and territories does AANR serve members?
Does AANR serve members in the United States?
Does AANR serve members in Canada?
Does AANR serve members in Mexico?
Does AANR serve members in the French West Indies?
Does AANR serve members in the Virgin Islands?
Does AANR serve members in St. Martin?
What does AANR promote?
Does AANR promote wholesome nude family recreation?
What rights does AANR work to protect?
In what settings does AANR protect the rights of nudists?
Does AANR support nudism on sanctioned nude beaches?
Does AANR support nudism on public lands set aside for that use?
Does AANR support nudism in homes?
Does AANR support nudism in private backyards?
Does AANR support nudism in AANR-affiliated clubs?
Does AANR support nudism in campgrounds?
Does AANR support nudism in resorts?
How does AANR use a portion of its collected membership fees?
Is AANR politically active?
Does AANR campaign and lobby governments?
Which governments does AANR lobby?
Does AANR fight to allow nudism in the United States?
Does AANR fight to allow nudism in Canada?
What is the relationship between AANR and affiliated resorts, clubs, and businesses?
What kinds of organizations choose to affiliate with AANR?
What geographic regions are included in AANR's membership area?
What activities does AANR undertake to protect nudist rights?
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
    SpaceRegion,
    TimeInterval,
    Process,
    NonAgentivePhysicalObject,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Organization(Society):
        pass


    class NaturistOrganization(Organization):
        pass


    class AdvocacyNaturistOrganization(NaturistOrganization):
        pass


    class AffiliateOrganization(Organization):
        pass


    class NudistResort(AffiliateOrganization):
        pass


    class NudistClub(AffiliateOrganization):
        pass


    class NudistBusiness(AffiliateOrganization):
        pass


    class GeographicRegion(SpaceRegion):
        pass


    class ContinentalRegion(GeographicRegion):
        pass


    class CountryOrTerritory(GeographicRegion):
        pass


    class RecreationActivity(Process):
        pass


    class WholesomeNudeFamilyRecreation(RecreationActivity):
        pass


    class NudismSetting(NonAgentivePhysicalObject):
        pass


    class SanctionedNudeBeach(NudismSetting):
        pass


    class PublicLandSetAsideForNudism(NudismSetting):
        pass


    class Home(NudismSetting):
        pass


    class PrivateBackyard(NudismSetting):
        pass


    class Campground(NudismSetting):
        pass


    class PoliticalActivity(Process):
        pass


    class Campaigning(PoliticalActivity):
        pass


    class Lobbying(PoliticalActivity):
        pass


    class affiliatedWith(ObjectProperty):
        domain = [AffiliateOrganization]
        range = [NaturistOrganization]


    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [GeographicRegion]


    class foundedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [TimeInterval]


    class largestOfItsKindIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [GeographicRegion]


    class longestEstablishedOfItsKindIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [GeographicRegion]


    class servesMembersIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [GeographicRegion]


    class promotesBenefitsOf(ObjectProperty):
        domain = [NaturistOrganization]
        range = [RecreationActivity]


    class supportsNudismIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [NudismSetting, AffiliateOrganization]


    class usesMembershipFeesFor(ObjectProperty):
        domain = [NaturistOrganization]
        range = [PoliticalActivity]


    class campaignsIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [CountryOrTerritory]


    class lobbiesGovernmentsIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [CountryOrTerritory]


    class acronym(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]


    class previousName(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [str]


    class approximateAffiliateCount(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [int]


    class minimumMemberCount(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [int]


    class protectsRightsOf(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]


    class politicallyActive(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]


    class promotesDescription(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]


    class membershipFeeUseDescription(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]


    AffiliateOrganization.is_a.append(affiliatedWith.some(NaturistOrganization))
    AdvocacyNaturistOrganization.is_a.extend([
        promotesBenefitsOf.some(WholesomeNudeFamilyRecreation),
        supportsNudismIn.some(SanctionedNudeBeach),
        supportsNudismIn.some(PublicLandSetAsideForNudism),
        supportsNudismIn.some(Home),
        supportsNudismIn.some(PrivateBackyard),
        supportsNudismIn.some(NudistClub),
        supportsNudismIn.some(Campground),
        supportsNudismIn.some(NudistResort),
        usesMembershipFeesFor.some(Campaigning),
        usesMembershipFeesFor.some(Lobbying),
        campaignsIn.some(CountryOrTerritory),
        lobbiesGovernmentsIn.some(CountryOrTerritory),
    ])

    NorthAmerica = ContinentalRegion("NorthAmericaRegion")
    NorthAmerica.label = "North America"

    UnitedStates = CountryOrTerritory("UnitedStatesRegion")
    UnitedStates.label = ["United States", "US"]
    UnitedStates.partOf.append(NorthAmerica)

    Canada = CountryOrTerritory("CanadaRegion")
    Canada.label = "Canada"
    Canada.partOf.append(NorthAmerica)

    Mexico = CountryOrTerritory("MexicoRegion")
    Mexico.label = "Mexico"
    Mexico.partOf.append(NorthAmerica)

    FrenchWestIndies = CountryOrTerritory("FrenchWestIndiesRegion")
    FrenchWestIndies.label = "French West Indies"
    FrenchWestIndies.partOf.append(NorthAmerica)

    VirginIslands = CountryOrTerritory("VirginIslandsRegion")
    VirginIslands.label = "Virgin Islands"
    VirginIslands.partOf.append(NorthAmerica)

    StMartin = CountryOrTerritory("StMartinRegion")
    StMartin.label = "St. Martin"
    StMartin.partOf.append(NorthAmerica)

    Year1931 = TimeInterval("Year1931Interval")
    Year1931.label = "1931"

    AmericanAssociationForNudeRecreation = AdvocacyNaturistOrganization("AmericanAssociationForNudeRecreationOrg")
    AmericanAssociationForNudeRecreation.label = [
        "American Association for Nude Recreation",
        "AANR",
        "American Sunbathing Association",
    ]
    AmericanAssociationForNudeRecreation.acronym = "AANR"
    AmericanAssociationForNudeRecreation.previousName = "American Sunbathing Association"
    AmericanAssociationForNudeRecreation.basedIn = UnitedStates
    AmericanAssociationForNudeRecreation.foundedIn = Year1931
    AmericanAssociationForNudeRecreation.largestOfItsKindIn.append(NorthAmerica)
    AmericanAssociationForNudeRecreation.longestEstablishedOfItsKindIn.append(NorthAmerica)
    AmericanAssociationForNudeRecreation.approximateAffiliateCount = 200
    AmericanAssociationForNudeRecreation.minimumMemberCount = 30000
    AmericanAssociationForNudeRecreation.servesMembersIn.append(UnitedStates)
    AmericanAssociationForNudeRecreation.servesMembersIn.append(Canada)
    AmericanAssociationForNudeRecreation.servesMembersIn.append(Mexico)
    AmericanAssociationForNudeRecreation.servesMembersIn.append(FrenchWestIndies)
    AmericanAssociationForNudeRecreation.servesMembersIn.append(VirginIslands)
    AmericanAssociationForNudeRecreation.servesMembersIn.append(StMartin)
    AmericanAssociationForNudeRecreation.protectsRightsOf = "nudists"
    AmericanAssociationForNudeRecreation.politicallyActive = True
    AmericanAssociationForNudeRecreation.promotesDescription = "the benefits of wholesome nude family recreation"
    AmericanAssociationForNudeRecreation.membershipFeeUseDescription = (
        "to be politically active by campaigning and lobbying governments fighting "
        "to allow nudism in the US and Canada"
    )
    AmericanAssociationForNudeRecreation.campaignsIn.append(UnitedStates)
    AmericanAssociationForNudeRecreation.campaignsIn.append(Canada)
    AmericanAssociationForNudeRecreation.lobbiesGovernmentsIn.append(UnitedStates)
    AmericanAssociationForNudeRecreation.lobbiesGovernmentsIn.append(Canada)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
