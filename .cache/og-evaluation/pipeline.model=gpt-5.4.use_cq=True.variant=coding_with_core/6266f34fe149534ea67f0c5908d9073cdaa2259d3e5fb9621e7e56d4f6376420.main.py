"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

What is The Celebrity Apprentice?
What type of television program is The Celebrity Apprentice?
How is The Celebrity Apprentice related to The Apprentice series?
Who hosted The Celebrity Apprentice, and during what years did each host serve?
When did Donald Trump host The Celebrity Apprentice?
When did Arnold Schwarzenegger host The Celebrity Apprentice?
Who announced that The Celebrity Apprentice had effectively been canceled?
When was The Celebrity Apprentice said to have been effectively canceled?
What is the opening theme song of The Celebrity Apprentice?
Who performs the opening theme song of The Celebrity Apprentice?
How does The Celebrity Apprentice differ from its precursor, The Apprentice?
Who are the competitors in The Celebrity Apprentice?
Are the competing apprentices in The Celebrity Apprentice celebrities or unknowns?
What is the goal of the celebrities competing in The Celebrity Apprentice?
For what purpose do contestants compete to win money on The Celebrity Apprentice?
Can each celebrity choose a charitable organization of their choice?
From which media or professional fields do the celebrities on The Celebrity Apprentice come?
Do contestants on The Celebrity Apprentice come from sitcoms?
Do contestants on The Celebrity Apprentice come from professional sports?
Do contestants on The Celebrity Apprentice come from the music industry?
Do contestants on The Celebrity Apprentice come from reality television?
Do contestants on The Celebrity Apprentice come from radio?
How are the seasons of The Celebrity Apprentice linked to The Apprentice?
Which seasons of The Apprentice belong to the original precursor show?
Which season numbers correspond to The Celebrity Apprentice?
Does The Celebrity Apprentice include seasons seven to nine?
Does The Celebrity Apprentice include seasons eleven to fifteen?
Is season ten part of The Apprentice rather than The Celebrity Apprentice?
Was The Celebrity Apprentice broadcast in the United States?
Is The Celebrity Apprentice a reality competition series?
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
    AgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Person(AgentivePhysicalObject):
        pass


    class TelevisionHost(Person):
        pass


    class RealEstateDeveloper(Person):
        pass


    class UnitedStatesPresident(Person):
        pass


    class Actor(Person):
        pass


    class FormerCaliforniaGovernor(Person):
        pass


    class EntertainmentChairman(Person):
        pass


    class Organization(Society):
        pass


    class EntertainmentOrganization(Organization):
        pass


    class MusicGroup(Organization):
        pass


    class CharitableOrganization(Organization):
        pass


    class GeographicRegion(SpaceRegion):
        pass


    class Country(GeographicRegion):
        pass


    class StateRegion(GeographicRegion):
        pass


    class TelevisionProgram(NonAgentiveSocialObject):
        pass


    class TelevisionSeries(TelevisionProgram):
        pass


    class TelevisionRealityCompetitionSeries(TelevisionSeries):
        pass


    class ApprenticePrecursorSeries(TelevisionRealityCompetitionSeries):
        pass


    class CelebrityApprenticeSeries(TelevisionRealityCompetitionSeries):
        pass


    class Song(NonAgentiveSocialObject):
        pass


    class TelevisionThemeSong(Song):
        pass


    class MediaField(NonAgentiveSocialObject):
        pass


    class SitcomField(MediaField):
        pass


    class ProfessionalSportsField(MediaField):
        pass


    class MusicIndustryField(MediaField):
        pass


    class RealityTelevisionField(MediaField):
        pass


    class RadioField(MediaField):
        pass


    class OtherBackgroundField(MediaField):
        pass


    class Contestant(Person):
        pass


    class CelebrityContestant(Contestant):
        pass


    class CurrentCelebrityContestant(CelebrityContestant):
        pass


    class OutOfPublicEyeCelebrityContestant(CelebrityContestant):
        pass


    class UnknownContestant(Contestant):
        pass


    class TelevisionSeasonGroup(NonAgentiveSocialObject):
        pass


    class ReferencedTimeInterval(TimeInterval):
        pass


    class variationOfSeries(ObjectProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]


    class linkedInSeasonsTo(ObjectProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]


    class hasOpeningThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionThemeSong]


    class performedBy(ObjectProperty):
        domain = [Song]
        range = [MusicGroup]


    class hasContestant(ObjectProperty):
        domain = [TelevisionRealityCompetitionSeries]
        range = [Contestant]


    class competesFor(ObjectProperty):
        domain = [CelebrityContestant]
        range = [CharitableOrganization]


    class comesFromField(ObjectProperty):
        domain = [CelebrityContestant]
        range = [MediaField]


    class hostedSeries(ObjectProperty):
        domain = [TelevisionHost]
        range = [TelevisionSeries]


    class hostingInterval(ObjectProperty):
        domain = [TelevisionHost]
        range = [ReferencedTimeInterval]


    class announcedEffectiveCancellationOf(ObjectProperty):
        domain = [Person]
        range = [TelevisionSeries]


    class announcementDate(ObjectProperty):
        domain = [Person]
        range = [ReferencedTimeInterval]


    class chairsOrganization(ObjectProperty):
        domain = [EntertainmentChairman]
        range = [EntertainmentOrganization]


    class isPresidentOf(ObjectProperty):
        domain = [UnitedStatesPresident]
        range = [Country]


    class isGovernorOf(ObjectProperty):
        domain = [FormerCaliforniaGovernor]
        range = [StateRegion]


    class broadcastInCountry(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Country]


    class seasonGroupOf(partOf):
        domain = [TelevisionSeasonGroup]
        range = [TelevisionSeries]


    CelebrityContestant.is_a.append(competesFor.some(CharitableOrganization))
    CelebrityContestant.is_a.append(
        comesFromField.some(
            Or([
                SitcomField,
                ProfessionalSportsField,
                MusicIndustryField,
                RealityTelevisionField,
                RadioField,
                OtherBackgroundField,
            ])
        )
    )
    ApprenticePrecursorSeries.is_a.append(hasContestant.some(UnknownContestant))
    CelebrityApprenticeSeries.is_a.append(hasContestant.some(CelebrityContestant))

    TheCelebrityApprentice = CelebrityApprenticeSeries("The_Celebrity_Apprentice")
    TheCelebrityApprentice.label = ["The Celebrity Apprentice", "Celebrity Apprentice"]

    TheApprentice = ApprenticePrecursorSeries("The_Apprentice")
    TheApprentice.label = ["The Apprentice", "The Apprentice series"]

    DonaldTrump = TelevisionHost("Donald_Trump")
    DonaldTrump.label = "Donald Trump"
    DonaldTrump.is_a.append(RealEstateDeveloper)
    DonaldTrump.is_a.append(UnitedStatesPresident)

    ArnoldSchwarzenegger = TelevisionHost("Arnold_Schwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"
    ArnoldSchwarzenegger.is_a.append(Actor)
    ArnoldSchwarzenegger.is_a.append(FormerCaliforniaGovernor)

    BobGreenblatt = EntertainmentChairman("Bob_Greenblatt")
    BobGreenblatt.label = "Bob Greenblatt"

    NBCEntertainment = EntertainmentOrganization("NBC_Entertainment")
    NBCEntertainment.label = "NBC Entertainment"

    ForTheLoveOfMoney = TelevisionThemeSong("For_the_Love_of_Money")
    ForTheLoveOfMoney.label = ['" For the Love of Money "', "For the Love of Money"]

    TheOJays = MusicGroup("The_OJays")
    TheOJays.label = "The O'Jays"

    UnitedStates = Country("US")
    UnitedStates.label = "U.S."

    California = StateRegion("California")
    California.label = "California"

    From2008To2015 = ReferencedTimeInterval("From_2008_to_2015")
    From2008To2015.label = "2008 to 2015"

    January2017 = ReferencedTimeInterval("January_2017")
    January2017.label = "January 2017"

    August32017 = ReferencedTimeInterval("August_3_2017")
    August32017.label = "August 3 , 2017"

    SeasonsOneToSix = TelevisionSeasonGroup("Seasons_one_to_six")
    SeasonsOneToSix.label = "seasons one to six"

    SeasonTen = TelevisionSeasonGroup("Season_ten")
    SeasonTen.label = "season ten"

    SeasonsSevenToNine = TelevisionSeasonGroup("Seasons_seven_to_nine")
    SeasonsSevenToNine.label = "seasons seven to nine"

    SeasonsElevenToFifteen = TelevisionSeasonGroup("Seasons_eleven_to_fifteen")
    SeasonsElevenToFifteen.label = "seasons eleven to fifteen"

    TheCelebrityApprentice.variationOfSeries.append(TheApprentice)
    TheCelebrityApprentice.linkedInSeasonsTo.append(TheApprentice)
    TheCelebrityApprentice.hasOpeningThemeSong = ForTheLoveOfMoney
    TheCelebrityApprentice.broadcastInCountry.append(UnitedStates)

    ForTheLoveOfMoney.performedBy.append(TheOJays)

    DonaldTrump.hostedSeries.append(TheCelebrityApprentice)
    DonaldTrump.hostingInterval.append(From2008To2015)
    DonaldTrump.isPresidentOf.append(UnitedStates)

    ArnoldSchwarzenegger.hostedSeries.append(TheCelebrityApprentice)
    ArnoldSchwarzenegger.hostingInterval.append(January2017)
    ArnoldSchwarzenegger.isGovernorOf.append(California)

    BobGreenblatt.chairsOrganization.append(NBCEntertainment)
    BobGreenblatt.announcedEffectiveCancellationOf.append(TheCelebrityApprentice)
    BobGreenblatt.announcementDate.append(August32017)

    SeasonsOneToSix.seasonGroupOf.append(TheApprentice)
    SeasonTen.seasonGroupOf.append(TheApprentice)
    SeasonsSevenToNine.seasonGroupOf.append(TheCelebrityApprentice)
    SeasonsElevenToFifteen.seasonGroupOf.append(TheCelebrityApprentice)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
