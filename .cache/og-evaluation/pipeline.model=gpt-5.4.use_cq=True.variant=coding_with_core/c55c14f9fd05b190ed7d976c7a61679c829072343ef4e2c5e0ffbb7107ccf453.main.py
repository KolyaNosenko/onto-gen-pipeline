"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

What is the title of the episode?
Which television series does "Ike's Wee Wee" belong to?
What season of South Park is "Ike's Wee Wee" in?
What episode number is "Ike's Wee Wee" within season 2?
What is the overall series episode number of "Ike's Wee Wee"?
When did "Ike's Wee Wee" first air?
On which television network did "Ike's Wee Wee" first air?
In which country did "Ike's Wee Wee" first air?
What type of television series is South Park?
What are the main plotlines of "Ike's Wee Wee"?
What happens to Mr. Mackey in the episode?
Why do the boys try to save Ike in the episode?
What event involving Ike motivates the boys' actions?
Who is Kyle's younger brother?
Who wrote "Ike's Wee Wee"?
Who directed "Ike's Wee Wee"?
Which co-creator of South Park wrote and directed "Ike's Wee Wee"?
What themes are explored in "Ike's Wee Wee"?
How does "Ike's Wee Wee" satirize attitudes toward drug users?
What question about family relationships is explored in the episode?
What backstory about Ike is introduced in "Ike's Wee Wee"?
Is Ike an adopted child?
What is Ike's nationality or origin?
How was "Ike's Wee Wee" received by critics?
What aspects of the episode were especially praised by critics?
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
    SocialAgent,
    SocialObject,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class TelevisionSeries(SocialObject):
        pass


    class AnimatedTelevisionSeries(TelevisionSeries):
        pass


    class TelevisionNetwork(Society):
        pass


    class Country(Society):
        pass


    class Person(AgentivePhysicalObject):
        pass


    class Character(SocialAgent):
        pass


    class SchoolCounselor(Character):
        pass


    class TelevisionEpisode(SocialObject):
        pass


    class partOfSeries(partOf):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]


    class writtenBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]


    class directedBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]


    class firstAiredDuring(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TimeInterval]


    class firstAiredOnNetwork(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionNetwork]


    class firstAiredInCountry(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Country]


    class countryOfOrigin(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Country]


    class seriesCoCreatorOf(ObjectProperty):
        domain = [Person]
        range = [TelevisionSeries]


    class hasYoungerBrother(ObjectProperty):
        domain = [Character]
        range = [Character]


    class isFiredIn(ObjectProperty):
        domain = [Character]
        range = [TelevisionEpisode]


    class turnsToDrugsIn(ObjectProperty):
        domain = [Character]
        range = [TelevisionEpisode]


    class featuresSaveAttemptFor(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]


    class motivatedByUpcomingBrisOf(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]


    class introducedBackstoryIn(ObjectProperty):
        domain = [Character]
        range = [TelevisionEpisode]


    class titleText(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class seriesTypeDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]


    class hasSeasonNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]


    class hasEpisodeNumberInSeason(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]


    class hasOverallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]


    class plotlineSummary(DataProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class misconstruedProcedureDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class satirizesAttitudesToward(DataProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class exploresQuestion(DataProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class criticalReceptionDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class especiallyPraisedFor(DataProperty):
        domain = [TelevisionEpisode]
        range = [str]


    class isAdoptedChild(DataProperty, FunctionalProperty):
        domain = [Character]
        range = [bool]


    class nationalityDescription(DataProperty, FunctionalProperty):
        domain = [Character]
        range = [str]


    TelevisionEpisode.is_a.extend([
        partOfSeries.some(TelevisionSeries),
        writtenBy.some(Person),
        directedBy.some(Person),
        firstAiredDuring.some(TimeInterval),
        firstAiredOnNetwork.some(TelevisionNetwork),
        firstAiredInCountry.some(Country),
    ])

    SouthPark = AnimatedTelevisionSeries("SouthPark")
    SouthPark.label = "South Park"
    SouthPark.seriesTypeDescription = "American animated television series"

    ComedyCentral = TelevisionNetwork("ComedyCentral")
    ComedyCentral.label = "Comedy Central"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    May271998 = TimeInterval("May271998")
    May271998.label = "May 27, 1998"

    MrMackey = SchoolCounselor("MrMackey")
    MrMackey.label = "Mr. Mackey"

    Kyle = Character("Kyle")
    Kyle.label = "Kyle"

    Ike = Character("Ike")
    Ike.label = "Ike"
    Ike.isAdoptedChild = True
    Ike.nationalityDescription = "Canadian"

    TreyParker = Person("TreyParker")
    TreyParker.label = "Trey Parker"

    IkesWeeWeeEpisode = TelevisionEpisode("IkesWeeWeeEpisode")
    IkesWeeWeeEpisode.label = "Ike's Wee Wee"
    IkesWeeWeeEpisode.titleText = "Ike's Wee Wee"
    IkesWeeWeeEpisode.firstAiredDuring = May271998
    IkesWeeWeeEpisode.firstAiredOnNetwork = ComedyCentral
    IkesWeeWeeEpisode.firstAiredInCountry = UnitedStates
    IkesWeeWeeEpisode.hasSeasonNumber = 2
    IkesWeeWeeEpisode.hasEpisodeNumberInSeason = 4
    IkesWeeWeeEpisode.hasOverallEpisodeNumber = 18
    IkesWeeWeeEpisode.misconstruedProcedureDescription = "circumcision"
    IkesWeeWeeEpisode.criticalReceptionDescription = "received positive responses from critics"
    IkesWeeWeeEpisode.plotlineSummary = [
        "Mr. Mackey is fired and turns to drugs.",
        "The boys misconstrue circumcision and try to save Ike from his upcoming bris.",
    ]
    IkesWeeWeeEpisode.satirizesAttitudesToward = ["certain attitudes towards drug users"]
    IkesWeeWeeEpisode.exploresQuestion = [
        "whether family can only mean those who are related by blood"
    ]
    IkesWeeWeeEpisode.especiallyPraisedFor = ["its touching moments"]
    IkesWeeWeeEpisode.partOfSeries.append(SouthPark)
    IkesWeeWeeEpisode.writtenBy.append(TreyParker)
    IkesWeeWeeEpisode.directedBy.append(TreyParker)
    IkesWeeWeeEpisode.featuresSaveAttemptFor.append(Ike)
    IkesWeeWeeEpisode.motivatedByUpcomingBrisOf.append(Ike)

    SouthPark.countryOfOrigin.append(UnitedStates)
    TreyParker.seriesCoCreatorOf.append(SouthPark)
    MrMackey.isFiredIn.append(IkesWeeWeeEpisode)
    MrMackey.turnsToDrugsIn.append(IkesWeeWeeEpisode)
    Kyle.hasYoungerBrother.append(Ike)
    Ike.introducedBackstoryIn.append(IkesWeeWeeEpisode)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
