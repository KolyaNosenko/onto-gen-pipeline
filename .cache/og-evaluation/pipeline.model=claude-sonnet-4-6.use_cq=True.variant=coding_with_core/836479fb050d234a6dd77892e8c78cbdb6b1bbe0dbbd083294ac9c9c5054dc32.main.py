"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

1. What is the title of a specific episode of a television series?
2. Which season does an episode belong to?
3. What is the episode number within a season?
4. What is the overall episode number within a series?
5. When did an episode first air?
6. On which network or channel did an episode air?
7. In which country did an episode air?
8. Who wrote a specific episode?
9. Who directed a specific episode?
10. What themes or topics does an episode explore or satirize?
11. Which characters appear in a specific episode?
12. What is the backstory introduced for a character in an episode?
13. What is the nationality or origin of a character?
14. What is the relationship between characters in an episode?
15. What is the plot of a specific episode?
16. Who is the creator or co-creator of a television series?
17. What critical reception did an episode receive?
18. What aspects of an episode were praised by critics?
19. Which television series does an episode belong to?
20. What genre or style of animation is a television series?
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
    NonAgentiveSocialObject,
    SocialObject,
    AgentivePhysicalObject,
    Society,
    TimeInterval,
)

from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── Entity classes ────────────────────────────────────────────────────────

    class TelevisionSeries(NonAgentiveSocialObject):
        """A multi-season scripted television series."""

    class Season(NonAgentiveSocialObject):
        """An ordered collection of episodes broadcast as a single run."""

    class TelevisionEpisode(NonAgentiveSocialObject):
        """A single, individually broadcast instalment of a television series."""

    class Person(AgentivePhysicalObject):
        """A real human being credited in connection with the series."""

    class FictionalCharacter(SocialObject):
        """A character that appears in a television series."""

    class BroadcastNetwork(Society):
        """A television channel or cable network that airs content."""

    class Country(Society):
        """A sovereign nation state."""

    class Theme(NonAgentiveSocialObject):
        """A topic, idea, or attitude explored or satirised by an episode."""

    class AirDate(TimeInterval):
        """The specific calendar date on which an episode first aired."""

    # ── Properties ────────────────────────────────────────────────────────────

    class episodeOf(ObjectProperty):
        """Links a television episode to the series it belongs to."""
        domain = [TelevisionEpisode]
        range  = [TelevisionSeries]

    class episodeOfSeason(ObjectProperty):
        """Links a television episode to the season it belongs to."""
        domain = [TelevisionEpisode]
        range  = [Season]

    class seasonOf(ObjectProperty):
        """Links a season to the series it belongs to."""
        domain = [Season]
        range  = [TelevisionSeries]

    class writtenBy(ObjectProperty):
        """Credits the writer(s) of an episode."""
        domain = [TelevisionEpisode]
        range  = [Person]

    class directedBy(ObjectProperty):
        """Credits the director(s) of an episode."""
        domain = [TelevisionEpisode]
        range  = [Person]

    class createdBy(ObjectProperty):
        """Credits the creator(s) or co-creator(s) of a television series."""
        domain = [TelevisionSeries]
        range  = [Person]

    class airedOn(ObjectProperty):
        """Links an episode to the network on which it was broadcast."""
        domain = [TelevisionEpisode]
        range  = [BroadcastNetwork]

    class airedIn(ObjectProperty):
        """Links an episode to the country in which it was broadcast."""
        domain = [TelevisionEpisode]
        range  = [Country]

    class features(ObjectProperty):
        """Links an episode to the fictional characters that appear in it."""
        domain = [TelevisionEpisode]
        range  = [FictionalCharacter]

    class satirizes(ObjectProperty):
        """Links an episode to an attitude or theme it satirises."""
        domain = [TelevisionEpisode]
        range  = [Theme]

    class explores(ObjectProperty):
        """Links an episode to a theme or question it explores."""
        domain = [TelevisionEpisode]
        range  = [Theme]

    class youngerBrotherOf(ObjectProperty):
        """States that one character is the younger brother of another."""
        domain = [FictionalCharacter]
        range  = [FictionalCharacter]

    class firstAiredAt(temporallyLocatedAt):
        """The unique date/interval on which an episode first aired."""
        domain = [TelevisionEpisode]
        range  = [AirDate]

    class episodeTitle(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range  = [str]

    class seriesTitle(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [str]

    class episodeNumberInSeason(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range  = [int]

    class overallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range  = [int]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Season]
        range  = [int]

    class genre(DataProperty, FunctionalProperty):
        """The style or genre of the series (e.g. 'animated')."""
        domain = [TelevisionSeries]
        range  = [str]

    class countryOfOrigin(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range  = [str]

    class nationality(DataProperty, FunctionalProperty):
        """The national or ethnic identity of a fictional character."""
        domain = [FictionalCharacter]
        range  = [str]

    class isAdopted(DataProperty, FunctionalProperty):
        """Whether a fictional character is depicted as adopted."""
        domain = [FictionalCharacter]
        range  = [bool]

    class plot(DataProperty, FunctionalProperty):
        """A prose summary of the events in an episode."""
        domain = [TelevisionEpisode]
        range  = [str]

    class criticalReception(DataProperty, FunctionalProperty):
        """The overall critical verdict received by an episode."""
        domain = [TelevisionEpisode]
        range  = [str]

    class praisedFor(DataProperty, FunctionalProperty):
        """Aspects of an episode that critics specifically praised."""
        domain = [TelevisionEpisode]
        range  = [str]

    class backstory(DataProperty, FunctionalProperty):
        """Background information about a character introduced in the series."""
        domain = [FictionalCharacter]
        range  = [str]

    # ── Named individuals ─────────────────────────────────────────────────────

    # Television series
    southPark = TelevisionSeries("SouthPark")
    southPark.label = "South Park"
    southPark.seriesTitle = "South Park"
    southPark.genre = "animated"
    southPark.countryOfOrigin = "American"

    # Season
    season2 = Season("SouthParkSeason2")
    season2.label = "the second season"
    season2.seasonNumber = 2
    season2.seasonOf.append(southPark)

    # Air date
    may27_1998 = AirDate("May27_1998")
    may27_1998.label = "May 27, 1998"

    # Broadcast network
    comedyCentral = BroadcastNetwork("ComedyCentral")
    comedyCentral.label = "Comedy Central"

    # Country
    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    # Creator / writer / director
    treyParker = Person("TreyParker")
    treyParker.label = "Trey Parker"
    southPark.createdBy.append(treyParker)

    # Fictional characters
    mrMackey = FictionalCharacter("MrMackey")
    mrMackey.label = "Mr. Mackey"

    kyle = FictionalCharacter("Kyle")
    kyle.label = "Kyle"

    ike = FictionalCharacter("Ike")
    ike.label = "Ike"
    ike.nationality = "Canadian"
    ike.isAdopted = True
    ike.backstory = "adopted Canadian child"
    ike.youngerBrotherOf.append(kyle)

    # The episode
    ikesWeeWee = TelevisionEpisode("IkesWeeWeeEpisode")
    ikesWeeWee.label = "Ike's Wee Wee"
    ikesWeeWee.episodeTitle = "Ike's Wee Wee"
    ikesWeeWee.episodeNumberInSeason = 4
    ikesWeeWee.overallEpisodeNumber = 18
    ikesWeeWee.plot = (
        "School counselor Mr. Mackey is fired and turns to drugs. "
        "The boys misconstrue what circumcision entails and try to save "
        "Kyle's younger brother Ike from his upcoming bris."
    )
    ikesWeeWee.criticalReception = "positive"
    ikesWeeWee.praisedFor = "touching moments"
    ikesWeeWee.episodeOf.append(southPark)
    ikesWeeWee.episodeOfSeason.append(season2)
    ikesWeeWee.firstAiredAt = may27_1998
    ikesWeeWee.airedOn.append(comedyCentral)
    ikesWeeWee.airedIn.append(unitedStates)
    ikesWeeWee.writtenBy.append(treyParker)
    ikesWeeWee.directedBy.append(treyParker)
    ikesWeeWee.features.append(mrMackey)
    ikesWeeWee.features.append(kyle)
    ikesWeeWee.features.append(ike)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
