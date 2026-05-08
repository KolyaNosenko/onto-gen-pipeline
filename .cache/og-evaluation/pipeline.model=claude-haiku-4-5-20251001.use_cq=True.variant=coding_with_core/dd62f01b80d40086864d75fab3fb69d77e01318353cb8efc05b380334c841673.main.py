"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

1. What is the title of the fourth episode of the second season of South Park?
2. Which episode number is "Ike's Wee Wee" in the overall series?
3. When did "Ike's Wee Wee" first air?
4. On which television network did "Ike's Wee Wee" premiere?
5. Who wrote and directed "Ike's Wee Wee"?
6. What is the main plot involving Mr. Mackey in this episode?
7. What misconception do the boys have about circumcision in the episode?
8. Who is Ike and what is his relationship to Kyle?
9. What is revealed about Ike's backstory in this episode?
10. What themes does "Ike's Wee Wee" satirize?
11. What family-related concept does this episode explore?
12. What was the critical reception of "Ike's Wee Wee"?
13. Which aspects of the episode did critics particularly praise?
14. Who is the series co-creator that directed this episode?
15. What nationality is Ike according to the episode?
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
    NonAgentiveSocialObject, AgentivePhysicalObject, Society,
    SpaceRegion, Abstract, TimeInterval,
)


with core:
    # Domain entity classes
    class TelevisionEpisode(NonAgentiveSocialObject):
        """A television episode; a created cultural work."""
        pass

    class TelevisionSeries(NonAgentiveSocialObject):
        """A television series; a collection of episodes."""
        pass

    class Character(AgentivePhysicalObject):
        """A fictional character with agency and intentions."""
        pass

    class Creator(AgentivePhysicalObject):
        """A person who creates or produces media."""
        pass

    class TelevisionNetwork(Society):
        """A television broadcasting organization."""
        pass

    class Country(SpaceRegion):
        """A geographical region; a country."""
        pass

    class Theme(Abstract):
        """An abstract theme or concept explored in media."""
        pass

    class CriticalReception(Abstract):
        """An abstract assessment of critical reception."""
        pass

    # Domain properties
    class isEpisodeOf(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class episodeNumberInSeason(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class overallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class firstAiredOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TimeInterval]

    class airedOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionNetwork]

    class airedIn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Country]

    class writtenBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Creator]

    class directedBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Creator]

    class createdBy(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Creator]

    class isYoungerBrotherOf(ObjectProperty):
        domain = [Character]
        range = [Character]

    class isAdopted(DataProperty, FunctionalProperty):
        domain = [Character]
        range = [bool]

    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Character]
        range = [Country]

    class satirizes(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Theme]

    class explores(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Theme]

    class hasCriticalReception(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [CriticalReception]

    class praisedFor(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Theme]

    class characterAppears(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class hasProfession(DataProperty):
        domain = [Character]
        range = [str]

    # Concrete instances for named entities from the text
    # Countries
    Canada = Country("Canada")
    Canada.label = "Canada"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    # Time interval for air date
    AirDate = TimeInterval("MayTwentySeven1998")
    AirDate.label = "May 27, 1998"

    # Television network
    ComedyCentral = TelevisionNetwork("ComedyCentral")
    ComedyCentral.label = "Comedy Central"

    # Television series
    SouthPark = TelevisionSeries("SouthPark")
    SouthPark.label = "South Park"

    # Creator
    TreyParker = Creator("TreyParker")
    TreyParker.label = "Trey Parker"

    # Characters
    MrMackey = Character("MrMackey")
    MrMackey.label = "Mr. Mackey"
    MrMackey.hasProfession = ["school counselor"]

    Kyle = Character("Kyle")
    Kyle.label = "Kyle"

    Ike = Character("Ike")
    Ike.label = "Ike"
    Ike.isAdopted = True
    Ike.hasNationality = Canada
    Ike.isYoungerBrotherOf = [Kyle]

    # Themes
    DrugUserAttitudes = Theme("DrugUserAttitudes")
    DrugUserAttitudes.label = "attitudes towards drug users"

    FamilyConcept = Theme("FamilyConcept")
    FamilyConcept.label = "whether family can only mean those who are related by blood"

    TouchingMoments = Theme("TouchingMoments")
    TouchingMoments.label = "its touching moments"

    # Critical reception
    PositiveReception = CriticalReception("PositiveReception")
    PositiveReception.label = "positive responses from critics"

    # Television episode
    IkesWeeWee = TelevisionEpisode("IkesWeeWee")
    IkesWeeWee.label = "Ike's Wee Wee"
    IkesWeeWee.isEpisodeOf = [SouthPark]
    IkesWeeWee.seasonNumber = 2
    IkesWeeWee.episodeNumberInSeason = 4
    IkesWeeWee.overallEpisodeNumber = 18
    IkesWeeWee.firstAiredOn = AirDate
    IkesWeeWee.airedOn = ComedyCentral
    IkesWeeWee.airedIn = UnitedStates
    IkesWeeWee.writtenBy = [TreyParker]
    IkesWeeWee.directedBy = [TreyParker]
    IkesWeeWee.characterAppears = [MrMackey, Kyle, Ike]
    IkesWeeWee.satirizes = [DrugUserAttitudes]
    IkesWeeWee.explores = [FamilyConcept]
    IkesWeeWee.hasCriticalReception = PositiveReception
    IkesWeeWee.praisedFor = [TouchingMoments]

    # Set South Park series creator
    SouthPark.createdBy = [TreyParker]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
