"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

1. What is the full name of AANR?
2. What type of organization is AANR?
3. In which country is AANR based?
4. When was AANR founded?
5. What was AANR’s previous name?
6. Is AANR the largest and longest-established organization of its kind in North America?
7. How many resorts, clubs, and businesses affiliate with AANR?
8. How many members does AANR serve?
9. In which countries and territories does AANR serve members?
10. What benefits does AANR promote?
11. What rights does AANR work to protect?
12. In what settings does AANR support nudism?
13. Does AANR support nudism in sanctioned nude beaches?
14. Does AANR support nudism on public lands set aside for nudism?
15. Does AANR support nudism in homes and private backyards?
16. Does AANR support nudism in AANR-affiliated clubs, campgrounds, and resorts?
17. Does AANR use membership fees for political activity?
18. What does AANR do politically with a portion of its membership fees?
19. In which governments does AANR campaign and lobby regarding nudism?
20. Does AANR campaign and lobby governments in the United States and Canada to allow nudism?
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

    class Place(Thing):
        pass

    class Country(Place):
        pass

    class Territory(Place):
        pass

    class Continent(Place):
        pass

    class Setting(Place):
        pass

    class Beach(Setting):
        pass

    class Land(Setting):
        pass

    class Home(Setting):
        pass

    class Backyard(Setting):
        pass

    class Club(Setting):
        pass

    class Campground(Setting):
        pass

    class Resort(Setting):
        pass

    class Business(Organization):
        pass

    class Benefit(Thing):
        pass

    class Right(Thing):
        pass

    class PoliticalActivity(Thing):
        pass

    class Nudist(Thing):
        pass

    class Government(Thing):
        pass

    class basedIn(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class operatesIn(ObjectProperty):
        domain = [Organization]
        range = [Continent]

    class hasPreviousName(ObjectProperty, FunctionalProperty):
        domain = [Organization]
        range = [Organization]

    class servesMembersIn(ObjectProperty):
        domain = [Organization]
        range = [Place]

    class promotesBenefit(ObjectProperty):
        domain = [Organization]
        range = [Benefit]

    class protectsRightsOf(ObjectProperty):
        domain = [Organization]
        range = [Right]

    class supportsNudismIn(ObjectProperty):
        domain = [Organization]
        range = [Setting]

    class usesMembershipFeesFor(ObjectProperty):
        domain = [Organization]
        range = [PoliticalActivity]

    class campaignsIn(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class lobbiesIn(ObjectProperty):
        domain = [Organization]
        range = [Country]

    class affiliatesWith(ObjectProperty):
        domain = [Thing]
        range = [Organization]

    class foundedInYear(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class affiliateCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class memberCount(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [int]

    class isLargestOfItsKindInNorthAmerica(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    class isLongestEstablishedOfItsKindInNorthAmerica(DataProperty, FunctionalProperty):
        domain = [Organization]
        range = [bool]

    AANR = NaturistOrganization("AANR")
    AANR.label = ["American Association for Nude Recreation ( AANR )", "American Association for Nude Recreation", "AANR", "The AANR"]

    AmericanSunbathingAssociation = Organization("AmericanSunbathingAssociation")
    AmericanSunbathingAssociation.label = "American Sunbathing Association"

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

    NorthAmerica = Continent("NorthAmerica")
    NorthAmerica.label = "North America"

    WholesomeNudeFamilyRecreation = Benefit("WholesomeNudeFamilyRecreation")
    WholesomeNudeFamilyRecreation.label = "wholesome nude family recreation"

    RightsOfNudistsInAppropriateSettings = Right("RightsOfNudistsInAppropriateSettings")
    RightsOfNudistsInAppropriateSettings.label = "the rights of nudists in appropriate settings"

    Nudists = Nudist("Nudists")
    Nudists.label = "nudists"

    SanctionedNudeBeaches = Beach("SanctionedNudeBeaches")
    SanctionedNudeBeaches.label = "sanctioned nude beaches"

    PublicLandsSetAsideForThatUse = Land("PublicLandsSetAsideForThatUse")
    PublicLandsSetAsideForThatUse.label = "public lands set aside for that use"

    Homes = Home("Homes")
    Homes.label = "homes"

    PrivateBackyards = Backyard("PrivateBackyards")
    PrivateBackyards.label = "private backyards"

    AANRAffiliatedClubs = Club("AANRAffiliatedClubs")
    AANRAffiliatedClubs.label = "AANR - affiliated clubs"

    Campgrounds = Campground("Campgrounds")
    Campgrounds.label = "campgrounds"

    Resorts = Resort("Resorts")
    Resorts.label = "resorts"

    CampaigningActivity = PoliticalActivity("CampaigningActivity")
    CampaigningActivity.label = "campaigning"

    LobbyingActivity = PoliticalActivity("LobbyingActivity")
    LobbyingActivity.label = "lobbying"

    AANR.basedIn = [UnitedStates]
    AANR.operatesIn = [NorthAmerica]
    AANR.hasPreviousName = AmericanSunbathingAssociation
    AANR.servesMembersIn = [UnitedStates, Canada, Mexico, FrenchWestIndies, VirginIslands, StMartin]
    AANR.promotesBenefit = [WholesomeNudeFamilyRecreation]
    AANR.protectsRightsOf = [RightsOfNudistsInAppropriateSettings]
    AANR.supportsNudismIn = [SanctionedNudeBeaches, PublicLandsSetAsideForThatUse, Homes, PrivateBackyards, AANRAffiliatedClubs, Campgrounds, Resorts]
    AANR.usesMembershipFeesFor = [CampaigningActivity, LobbyingActivity]
    AANR.campaignsIn = [UnitedStates, Canada]
    AANR.lobbiesIn = [UnitedStates, Canada]
    AANR.foundedInYear = 1931
    AANR.affiliateCount = 200
    AANR.memberCount = 30000
    AANR.isLargestOfItsKindInNorthAmerica = True
    AANR.isLongestEstablishedOfItsKindInNorthAmerica = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
