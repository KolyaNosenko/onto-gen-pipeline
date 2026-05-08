"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

What is the title of the episode?
What season of South Park does "Ike's Wee Wee" belong to?
What episode number is "Ike's Wee Wee" within the second season?
What is the overall series episode number of "Ike's Wee Wee"?
What television series is "Ike's Wee Wee" part of?
What genre of television series is South Park?
In what country did "Ike's Wee Wee" first air?
On what network did "Ike's Wee Wee" first air?
On what date did "Ike's Wee Wee" first air?
What happens to Mr. Mackey in the episode?
Why does Mr. Mackey turn to drugs in the episode?
What do the boys misunderstand in the episode?
Whom do the boys try to save from an upcoming bris?
What is Ike's relationship to Kyle?
What event is Ike facing in the episode?
Who wrote "Ike's Wee Wee"?
Who directed "Ike's Wee Wee"?
Who is the co-creator associated with writing and directing this episode?
What attitudes does "Ike's Wee Wee" satirize?
What theme about family is explored in "Ike's Wee Wee"?
What backstory about Ike is introduced in this episode?
Is Ike an adopted child?
Is Ike Canadian?
How did critics respond to "Ike's Wee Wee"?
What aspects of the episode were especially praised by critics?
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
    class CreativeWork(Thing):
        pass

    class TelevisionSeries(CreativeWork):
        pass

    class AnimatedTelevisionSeries(TelevisionSeries):
        pass

    class TelevisionEpisode(CreativeWork):
        pass

    class Organization(Thing):
        pass

    class TelevisionNetwork(Organization):
        pass

    class Place(Thing):
        pass

    class Country(Place):
        pass

    class TemporalEntity(Thing):
        pass

    class Date(TemporalEntity):
        pass

    class Person(Thing):
        pass

    class Character(Person):
        pass

    class Child(Character):
        pass

    class Boy(Child):
        pass

    class AdoptedChild(Child):
        pass

    class CanadianChild(Child):
        pass

    class AdoptedCanadianChild(AdoptedChild, CanadianChild):
        pass

    class SchoolCounselor(Character):
        pass

    class SeriesCoCreator(Person):
        pass

    class title(DataProperty, FunctionalProperty):
        domain = [CreativeWork]
        range = [str]

    class genre(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class episodeNumberInSeason(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class overallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class misunderstoodProcedure(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class exploredTheme(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class satirizedAttitude(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class backstoryDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class criticalResponse(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class praisedFor(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class employmentStatus(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class turnsToSubstance(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class turnsToSubstanceBecause(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class upcomingEventDescription(DataProperty, FunctionalProperty):
        domain = [Child]
        range = [str]

    class isAdopted(DataProperty, FunctionalProperty):
        domain = [Child]
        range = [bool]

    class isCanadian(DataProperty, FunctionalProperty):
        domain = [Child]
        range = [bool]

    class partOfSeries(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]

    class firstAiredOnNetwork(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionNetwork]

    class firstAiredInCountry(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Country]

    class firstAirDate(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Date]

    class originCountry(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Country]

    class writtenBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]

    class directedBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]

    class coCreatorOf(ObjectProperty):
        domain = [SeriesCoCreator]
        range = [TelevisionSeries]

    class youngerBrotherOf(ObjectProperty):
        domain = [Child]
        range = [Person]

    class rescueTarget(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Child]

    class introducedBackstoryFor(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Child]

    IkesWeeWeeEpisode = TelevisionEpisode("IkesWeeWee")
    IkesWeeWeeEpisode.label = "Ike's Wee Wee"
    IkesWeeWeeEpisode.title = "Ike's Wee Wee"
    IkesWeeWeeEpisode.seasonNumber = 2
    IkesWeeWeeEpisode.episodeNumberInSeason = 4
    IkesWeeWeeEpisode.overallEpisodeNumber = 18
    IkesWeeWeeEpisode.misunderstoodProcedure = "circumcision"
    IkesWeeWeeEpisode.satirizedAttitude = "certain attitudes towards drug users"
    IkesWeeWeeEpisode.exploredTheme = "whether family can only mean those who are related by blood"
    IkesWeeWeeEpisode.backstoryDescription = "Ike is an adopted Canadian child"
    IkesWeeWeeEpisode.criticalResponse = "positive responses from critics"
    IkesWeeWeeEpisode.praisedFor = "its touching moments"

    SouthParkSeries = AnimatedTelevisionSeries("SouthPark")
    SouthParkSeries.label = "South Park"
    SouthParkSeries.title = "South Park"
    SouthParkSeries.genre = "animated television series"

    ComedyCentralNetwork = TelevisionNetwork("ComedyCentral")
    ComedyCentralNetwork.label = "Comedy Central"

    UnitedStatesCountry = Country("UnitedStates")
    UnitedStatesCountry.label = "United States"

    May271998Date = Date("May271998")
    May271998Date.label = "May 27, 1998"

    MrMackeyCharacter = SchoolCounselor("MrMackey")
    MrMackeyCharacter.label = "Mr. Mackey"
    MrMackeyCharacter.employmentStatus = "fired"
    MrMackeyCharacter.turnsToSubstance = "drugs"
    MrMackeyCharacter.turnsToSubstanceBecause = "being fired"

    KyleCharacter = Boy("Kyle")
    KyleCharacter.label = "Kyle"

    IkeCharacter = AdoptedCanadianChild("Ike")
    IkeCharacter.label = "Ike"
    IkeCharacter.upcomingEventDescription = "bris"
    IkeCharacter.isAdopted = True
    IkeCharacter.isCanadian = True
    IkeCharacter.youngerBrotherOf = [KyleCharacter]

    TreyParkerPerson = SeriesCoCreator("TreyParker")
    TreyParkerPerson.label = "Trey Parker"
    TreyParkerPerson.coCreatorOf = [SouthParkSeries]

    IkesWeeWeeEpisode.partOfSeries = SouthParkSeries
    IkesWeeWeeEpisode.firstAiredOnNetwork = [ComedyCentralNetwork]
    IkesWeeWeeEpisode.firstAiredInCountry = [UnitedStatesCountry]
    IkesWeeWeeEpisode.firstAirDate = May271998Date
    IkesWeeWeeEpisode.writtenBy = [TreyParkerPerson]
    IkesWeeWeeEpisode.directedBy = [TreyParkerPerson]
    IkesWeeWeeEpisode.rescueTarget = [IkeCharacter]
    IkesWeeWeeEpisode.introducedBackstoryFor = [IkeCharacter]

    SouthParkSeries.originCountry = [UnitedStatesCountry]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
