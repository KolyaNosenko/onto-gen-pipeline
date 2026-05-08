"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

What is the American Association for Nude Recreation?
What type of organization is the American Association for Nude Recreation?
Where is the American Association for Nude Recreation based?
What does the acronym AANR stand for?
What is the previous name of the American Association for Nude Recreation?
When was the American Association for Nude Recreation founded?
Is the American Association for Nude Recreation the largest naturist organization in North America?
Is the American Association for Nude Recreation the longest-established organization of its kind in North America?
How many nudist resorts, clubs, and businesses are affiliated with AANR?
How many members does AANR serve?
In which countries and territories does AANR serve members?
Does AANR serve members in the United States?
Does AANR serve members in Canada?
Does AANR serve members in Mexico?
Does AANR serve members in the French West Indies?
Does AANR serve members in the Virgin Islands?
Does AANR serve members in St. Martin?
What are the main goals of AANR?
Does AANR promote wholesome nude family recreation?
What rights does AANR work to protect?
In which settings does AANR seek to protect the rights of nudists?
Does AANR support nudism on sanctioned nude beaches?
Does AANR support nudism on public lands set aside for that use?
Does AANR support nudism in homes and private backyards?
Does AANR support nudism in AANR-affiliated clubs, campgrounds, and resorts?
How does AANR use a portion of its collected membership fees?
Is AANR politically active?
Does AANR campaign and lobby governments?
Which governments does AANR lobby regarding nudism rights?
Does AANR campaign to allow nudism in the United States?
Does AANR campaign to allow nudism in Canada?
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

    class NaturistOrganization(Organization):
        pass

    class Name(Thing):
        pass

    class Acronym(Name):
        pass

    class OrganizationName(Name):
        pass

    class Member(Thing):
        pass

    class SocialGroup(Thing):
        pass

    class NudistCommunity(SocialGroup):
        pass

    class Right(Thing):
        pass

    class RecreationActivity(Thing):
        pass

    class PoliticalAction(Thing):
        pass

    class Place(Thing):
        pass

    class Region(Place):
        pass

    class Country(Region):
        pass

    class Territory(Region):
        pass

    class TimePoint(Thing):
        pass

    class Year(TimePoint):
        pass

    class Facility(Place):
        pass

    class NudeBeach(Facility):
        pass

    class PublicLand(Facility):
        pass

    class Home(Facility):
        pass

    class PrivateBackyard(Facility):
        pass

    class Club(Facility):
        pass

    class Campground(Facility):
        pass

    class Resort(Facility):
        pass

    class Business(Organization):
        pass

    class NudistResort(Resort):
        pass

    class NudistClub(Club):
        pass

    class NudistBusiness(Business):
        pass

    class hasAcronym(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Acronym]

    class hasPreviousName(ObjectProperty):
        domain = [Organization]
        range = [OrganizationName]

    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Country]

    class foundedIn(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Year]

    class largestOfItsKindIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [Region]

    class longestEstablishedOfItsKindIn(ObjectProperty):
        domain = [NaturistOrganization]
        range = [Region]

    class hasApproximateAffiliateCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class servesMoreThanMembersCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class servesMembersIn(ObjectProperty):
        domain = [Organization]
        range = [Region]

    class promotes(ObjectProperty):
        domain = [Organization]
        range = [RecreationActivity]

    class protects(ObjectProperty):
        domain = [Organization]
        range = [Right]

    class concernsGroup(ObjectProperty, FunctionalProperty):
        domain = [Right]
        range = [SocialGroup]

    class protectsRightsIn(ObjectProperty):
        domain = [Organization]
        range = [Facility]

    class supportsNudismIn(ObjectProperty):
        domain = [Organization]
        range = [Facility]

    class affiliatedWith(ObjectProperty):
        domain = [Facility, Business]
        range = [Organization]

    class usesCollectedMembershipFeesFor(ObjectProperty):
        domain = [Organization]
        range = [PoliticalAction]

    class campaignsToAllowNudismIn(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class lobbiesGovernmentsIn(ObjectProperty):
        domain = [Organization]
        range = [Country]

    AmericanAssociationForNudeRecreation = NaturistOrganization(
        "AmericanAssociationForNudeRecreation"
    )
    AmericanAssociationForNudeRecreation.label = [
        "American Association for Nude Recreation ( AANR )",
        "American Association for Nude Recreation",
    ]

    AANR = Acronym("AANRAcronym")
    AANR.label = "AANR"

    AmericanSunbathingAssociation = OrganizationName(
        "AmericanSunbathingAssociationName"
    )
    AmericanSunbathingAssociation.label = "American Sunbathing Association"

    Year1931 = Year("Year1931")
    Year1931.label = "1931"

    NorthAmerica = Region("NorthAmerica")
    NorthAmerica.label = "North America"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = ["United States", "US"]

    Canada = Country("Canada")
    Canada.label = "Canada"

    Mexico = Country("Mexico")
    Mexico.label = "Mexico"

    FrenchWestIndies = Territory("FrenchWestIndies")
    FrenchWestIndies.label = "French West Indies"

    VirginIslands = Territory("VirginIslands")
    VirginIslands.label = "Virgin Islands"

    StMartin = Territory("StMartin")
    StMartin.label = "St. Martin"

    WholesomeNudeFamilyRecreation = RecreationActivity(
        "WholesomeNudeFamilyRecreation"
    )
    WholesomeNudeFamilyRecreation.label = "wholesome nude family recreation"

    RightsOfNudists = Right("RightsOfNudists")
    RightsOfNudists.label = "rights of nudists"

    Nudists = NudistCommunity("Nudists")
    Nudists.label = "nudists"

    SanctionedNudeBeaches = NudeBeach("SanctionedNudeBeaches")
    SanctionedNudeBeaches.label = "sanctioned nude beaches"

    PublicLandsSetAsideForThatUse = PublicLand(
        "PublicLandsSetAsideForThatUse"
    )
    PublicLandsSetAsideForThatUse.label = "public lands set aside for that use"

    Homes = Home("Homes")
    Homes.label = "homes"

    PrivateBackyards = PrivateBackyard("PrivateBackyards")
    PrivateBackyards.label = "private backyards"

    AANRAffiliatedClubs = Club("AANRAffiliatedClubs")
    AANRAffiliatedClubs.label = "AANR - affiliated clubs"

    Campgrounds = Campground("Campgrounds")
    Campgrounds.label = "campgrounds"

    Resorts = Resort("Resorts")
    Resorts.label = "resorts"

    Campaigning = PoliticalAction("Campaigning")
    Campaigning.label = "campaigning"

    LobbyingGovernments = PoliticalAction("LobbyingGovernments")
    LobbyingGovernments.label = "lobbying governments"

    AmericanAssociationForNudeRecreation.hasAcronym = AANR
    AmericanAssociationForNudeRecreation.hasPreviousName = [
        AmericanSunbathingAssociation
    ]
    AmericanAssociationForNudeRecreation.basedIn = UnitedStates
    AmericanAssociationForNudeRecreation.foundedIn = Year1931
    AmericanAssociationForNudeRecreation.largestOfItsKindIn = [NorthAmerica]
    AmericanAssociationForNudeRecreation.longestEstablishedOfItsKindIn = [
        NorthAmerica
    ]
    AmericanAssociationForNudeRecreation.hasApproximateAffiliateCount = 200
    AmericanAssociationForNudeRecreation.servesMoreThanMembersCount = 30000
    AmericanAssociationForNudeRecreation.servesMembersIn = [
        UnitedStates,
        Canada,
        Mexico,
        FrenchWestIndies,
        VirginIslands,
        StMartin,
    ]
    AmericanAssociationForNudeRecreation.promotes = [
        WholesomeNudeFamilyRecreation
    ]
    AmericanAssociationForNudeRecreation.protects = [RightsOfNudists]
    AmericanAssociationForNudeRecreation.protectsRightsIn = [
        SanctionedNudeBeaches,
        PublicLandsSetAsideForThatUse,
        Homes,
        PrivateBackyards,
        AANRAffiliatedClubs,
        Campgrounds,
        Resorts,
    ]
    AmericanAssociationForNudeRecreation.supportsNudismIn = [
        SanctionedNudeBeaches,
        PublicLandsSetAsideForThatUse,
        Homes,
        PrivateBackyards,
        AANRAffiliatedClubs,
        Campgrounds,
        Resorts,
    ]
    AmericanAssociationForNudeRecreation.usesCollectedMembershipFeesFor = [
        Campaigning,
        LobbyingGovernments,
    ]
    AmericanAssociationForNudeRecreation.campaignsToAllowNudismIn = [
        UnitedStates,
        Canada,
    ]
    AmericanAssociationForNudeRecreation.lobbiesGovernmentsIn = [
        UnitedStates,
        Canada,
    ]

    RightsOfNudists.concernsGroup = Nudists

    AANRAffiliatedClubs.affiliatedWith = [AmericanAssociationForNudeRecreation]
    Campgrounds.affiliatedWith = [AmericanAssociationForNudeRecreation]
    Resorts.affiliatedWith = [AmericanAssociationForNudeRecreation]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
