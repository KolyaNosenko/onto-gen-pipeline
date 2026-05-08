"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

What is The Celebrity Apprentice?
What type of television program is The Celebrity Apprentice?
How is The Celebrity Apprentice related to The Apprentice series?
Who hosted The Celebrity Apprentice between 2008 and 2015?
Who hosted The Celebrity Apprentice in January 2017?
What occupations or public roles did Donald Trump have as described in the document?
What occupations or public roles did Arnold Schwarzenegger have as described in the document?
When did Arnold Schwarzenegger begin hosting The Celebrity Apprentice?
Who stated that The Celebrity Apprentice had effectively been canceled?
When was it stated that The Celebrity Apprentice had effectively been canceled?
What network executive announced the effective cancellation of The Celebrity Apprentice?
What is the opening theme song of The Celebrity Apprentice?
Who performed the opening theme song of The Celebrity Apprentice?
Does The Celebrity Apprentice use the same opening theme song as its precursor?
How does The Celebrity Apprentice differ from its precursor in terms of contestant type?
Who competes on The Celebrity Apprentice?
Are the contestants on The Celebrity Apprentice celebrities or unknown individuals?
What are the contestants competing to win on The Celebrity Apprentice?
For whom is the prize money intended on The Celebrity Apprentice?
Can contestants choose the charitable organization for which they compete?
From which fields or backgrounds do the celebrities on The Celebrity Apprentice come?
Do contestants on The Celebrity Apprentice come from sitcoms?
Do contestants on The Celebrity Apprentice come from professional sports?
Do contestants on The Celebrity Apprentice come from the music industry?
Do contestants on The Celebrity Apprentice come from reality television?
Do contestants on The Celebrity Apprentice come from radio?
Is The Celebrity Apprentice linked in seasons to The Apprentice?
Which seasons of The Apprentice belong to the precursor show?
Which seasons are part of The Celebrity Apprentice?
Does The Celebrity Apprentice include season ten?
Which season numbers correspond to The Celebrity Apprentice?
Which season numbers correspond to The Apprentice precursor series?
Was The Celebrity Apprentice still active after August 3, 2017?
What is the precursor show of The Celebrity Apprentice?
Is The Celebrity Apprentice an American television series?
Is The Celebrity Apprentice a reality competition series?
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
    class TelevisionProgram(Thing):
        pass

    class TelevisionSeries(TelevisionProgram):
        pass

    class RealityCompetitionSeries(TelevisionSeries):
        pass

    class AmericanTelevisionSeries(TelevisionSeries):
        pass

    class AmericanTelevisionRealityCompetitionSeries(
        AmericanTelevisionSeries,
        RealityCompetitionSeries,
    ):
        pass

    class Person(Thing):
        pass

    class Organization(Thing):
        pass

    class CharitableOrganization(Organization):
        pass

    class MusicGroup(Organization):
        pass

    class Song(Thing):
        pass

    class Role(Thing):
        pass

    class Occupation(Role):
        pass

    class PublicRole(Role):
        pass

    class NetworkExecutiveRole(PublicRole):
        pass

    class Field(Thing):
        pass

    class TimePoint(Thing):
        pass

    class ContestantType(Thing):
        pass

    class isVariationOf(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class hasPrecursor(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class linkedInSeasonsTo(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class hasHost(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Person]

    class hosts(ObjectProperty):
        domain = [Person]
        range = [TelevisionSeries]

    class hasRole(ObjectProperty):
        domain = [Person]
        range = [Role]

    class affiliatedWith(ObjectProperty):
        domain = [Person]
        range = [Organization]

    class hasOpeningThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Song]

    class performedBy(ObjectProperty, FunctionalProperty):
        domain = [Song]
        range = [MusicGroup]

    class effectiveCancellationAnnouncedBy(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Person]

    class effectiveCancellationAnnouncedOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TimePoint]

    class hostingStartTime(ObjectProperty):
        domain = [Person]
        range = [TimePoint]

    class hostingEndTime(ObjectProperty):
        domain = [Person]
        range = [TimePoint]

    class hasContestantType(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [ContestantType]

    class prizeMoneyIntendedFor(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [CharitableOrganization]

    class contestantsComeFromField(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Field]

    class includesSeasonNumber(DataProperty):
        domain = [TelevisionSeries]
        range = [int]

    class allowsContestantChoice(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [bool]

    class isEffectivelyCanceled(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [bool]

    TheCelebrityApprentice = AmericanTelevisionRealityCompetitionSeries("TheCelebrityApprentice")
    TheCelebrityApprentice.label = "The Celebrity Apprentice"

    TheApprenticeSeries = TelevisionSeries("TheApprenticeSeries")
    TheApprenticeSeries.label = ["The Apprentice series", "The Apprentice"]

    DonaldTrump = Person("DonaldTrump")
    DonaldTrump.label = "Donald Trump"

    ArnoldSchwarzenegger = Person("ArnoldSchwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"

    BobGreenblatt = Person("BobGreenblatt")
    BobGreenblatt.label = "Bob Greenblatt"

    NBCEntertainment = Organization("NBCEntertainment")
    NBCEntertainment.label = "NBC Entertainment"

    ForTheLoveOfMoney = Song("ForTheLoveOfMoney")
    ForTheLoveOfMoney.label = "For the Love of Money"

    TheOJays = MusicGroup("TheOJays")
    TheOJays.label = "The O'Jays"

    RealEstateDeveloper = Occupation("RealEstateDeveloper")
    RealEstateDeveloper.label = "real estate developer"

    USPresident = PublicRole("USPresident")
    USPresident.label = "U.S. President"

    Actor = Occupation("ActorOccupation")
    Actor.label = "actor"

    FormerCaliforniaGovernor = PublicRole("FormerCaliforniaGovernor")
    FormerCaliforniaGovernor.label = "former California Governor"

    NBCEntertainmentChairman = NetworkExecutiveRole("NBCEntertainmentChairman")
    NBCEntertainmentChairman.label = "NBC Entertainment Chairman"

    Celebrities = ContestantType("Celebrities")
    Celebrities.label = "celebrities"

    Unknowns = ContestantType("Unknowns")
    Unknowns.label = "unknowns"

    CharitableOrganizationOfTheirChoice = CharitableOrganization("CharitableOrganizationOfTheirChoice")
    CharitableOrganizationOfTheirChoice.label = "charitable organization of their choice"

    Sitcoms = Field("Sitcoms")
    Sitcoms.label = "sitcoms"

    ProfessionalSports = Field("ProfessionalSports")
    ProfessionalSports.label = "professional sports"

    MusicIndustry = Field("MusicIndustry")
    MusicIndustry.label = "music industry"

    RealityTelevision = Field("RealityTelevision")
    RealityTelevision.label = "reality television"

    Radio = Field("Radio")
    Radio.label = "radio"

    OtherBackgrounds = Field("OtherBackgrounds")
    OtherBackgrounds.label = "other backgrounds"

    Year2008 = TimePoint("Year2008")
    Year2008.label = "2008"

    Year2015 = TimePoint("Year2015")
    Year2015.label = "2015"

    January2017 = TimePoint("January2017")
    January2017.label = "January 2017"

    August32017 = TimePoint("August32017")
    August32017.label = "August 3 , 2017"

    TheCelebrityApprentice.isVariationOf = TheApprenticeSeries
    TheCelebrityApprentice.hasPrecursor = TheApprenticeSeries
    TheCelebrityApprentice.linkedInSeasonsTo = TheApprenticeSeries
    TheCelebrityApprentice.hasHost = [DonaldTrump, ArnoldSchwarzenegger]
    TheCelebrityApprentice.hasOpeningThemeSong = ForTheLoveOfMoney
    TheCelebrityApprentice.effectiveCancellationAnnouncedBy = BobGreenblatt
    TheCelebrityApprentice.effectiveCancellationAnnouncedOn = August32017
    TheCelebrityApprentice.hasContestantType = Celebrities
    TheCelebrityApprentice.prizeMoneyIntendedFor = CharitableOrganizationOfTheirChoice
    TheCelebrityApprentice.contestantsComeFromField = [
        Sitcoms,
        ProfessionalSports,
        MusicIndustry,
        RealityTelevision,
        Radio,
        OtherBackgrounds,
    ]
    TheCelebrityApprentice.includesSeasonNumber = [7, 8, 9, 11, 12, 13, 14, 15]
    TheCelebrityApprentice.allowsContestantChoice = True
    TheCelebrityApprentice.isEffectivelyCanceled = True

    TheApprenticeSeries.hasOpeningThemeSong = ForTheLoveOfMoney
    TheApprenticeSeries.hasContestantType = Unknowns
    TheApprenticeSeries.includesSeasonNumber = [1, 2, 3, 4, 5, 6, 10]

    DonaldTrump.hosts = [TheCelebrityApprentice]
    DonaldTrump.hasRole = [RealEstateDeveloper, USPresident]
    DonaldTrump.hostingStartTime = [Year2008]
    DonaldTrump.hostingEndTime = [Year2015]

    ArnoldSchwarzenegger.hosts = [TheCelebrityApprentice]
    ArnoldSchwarzenegger.hasRole = [Actor, FormerCaliforniaGovernor]
    ArnoldSchwarzenegger.hostingStartTime = [January2017]

    BobGreenblatt.hasRole = [NBCEntertainmentChairman]
    BobGreenblatt.affiliatedWith = [NBCEntertainment]

    ForTheLoveOfMoney.performedBy = TheOJays


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
