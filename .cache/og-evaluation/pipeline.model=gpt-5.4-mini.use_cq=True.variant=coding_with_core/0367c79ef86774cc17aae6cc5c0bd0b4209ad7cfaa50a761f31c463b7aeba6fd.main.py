"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

1. Which South Park episode is “Ike’s Wee Wee”?
2. What season and episode number is “Ike’s Wee Wee” in South Park?
3. What is the overall episode number of “Ike’s Wee Wee” in the South Park series?
4. When did “Ike’s Wee Wee” first air?
5. On which television network did “Ike’s Wee Wee” first air?
6. Which country is associated with the first airing of “Ike’s Wee Wee”?
7. Who wrote “Ike’s Wee Wee”?
8. Who directed “Ike’s Wee Wee”?
9. Which South Park character is fired in “Ike’s Wee Wee”?
10. What does Mr. Mackey do after being fired in “Ike’s Wee Wee”?
11. What misconception do the boys have about circumcision in “Ike’s Wee Wee”?
12. Who do the boys try to save from a bris in “Ike’s Wee Wee”?
13. What does “Ike’s Wee Wee” explore about the meaning of family?
14. What attitude toward drug users is satirized in “Ike’s Wee Wee”?
15. What backstory about Ike is introduced in “Ike’s Wee Wee”?
16. How was Ike related to the family in the episode’s backstory?
17. What kind of critical reception did “Ike’s Wee Wee” receive?
18. What aspects of “Ike’s Wee Wee” did critics especially praise?
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
    Event,
    Perdurant,
    SocialAgent,
    SocialObject,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class TelevisionSeries(Perdurant):
        pass

    class AnimatedTelevisionSeries(TelevisionSeries):
        pass

    class TelevisionSeason(Perdurant):
        is_a = [partOf.some(TelevisionSeries)]

    class TelevisionEpisode(Event):
        is_a = [partOf.some(TelevisionSeason), partOf.some(TelevisionSeries)]

    class TelevisionNetwork(SocialObject):
        pass

    class Country(Society):
        pass

    class Character(SocialAgent):
        pass

    class SchoolCounselor(Character):
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

    class Writer(Character):
        pass

    class Director(Character):
        pass

    class SeriesCoCreator(Character):
        pass

    class DrugUser(Character):
        pass

    class Critic(Character):
        pass

    class Family(SocialObject):
        pass

    class firstAiredOn(temporallyLocatedAt):
        domain = [TelevisionEpisode]
        range = [TimeInterval]

    class firstAiredOnNetwork(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionNetwork]

    class firstAiredInCountry(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Country]

    class countryOfOrigin(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Country]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Perdurant]
        range = [int]

    class episodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class overallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class writtenBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class directedBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class coCreatedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Character]

    class firedCharacter(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class hasYoungerBrother(ObjectProperty):
        domain = [Character]
        range = [Character]

    class introducedBackstoryOf(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class criticalReception(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class praisedFor(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class satirizes(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class explores(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    secondSeason = TelevisionSeason("SecondSeason")
    secondSeason.label = "second season"

    southPark = AnimatedTelevisionSeries("SouthPark")
    southPark.label = "South Park"

    ikeWeeWee = TelevisionEpisode("IkesWeeWee")
    ikeWeeWee.label = "Ike's Wee Wee"

    comedyCentral = TelevisionNetwork("ComedyCentral")
    comedyCentral.label = "Comedy Central"

    unitedStates = Country("UnitedStates")
    unitedStates.label = "United States"

    may272_1998 = TimeInterval("May272_1998")
    may272_1998.label = "May 27, 1998"

    treyParker = SeriesCoCreator("TreyParker")
    treyParker.label = "Trey Parker"
    treyParker.is_a.append(Character)
    treyParker.is_a.append(Writer)
    treyParker.is_a.append(Director)

    mrMackey = SchoolCounselor("MrMackey")
    mrMackey.label = "Mr. Mackey"
    mrMackey.is_a.append(Character)
    mrMackey.is_a.append(DrugUser)

    kyle = Boy("Kyle")
    kyle.label = "Kyle"
    kyle.is_a.append(Character)
    kyle.is_a.append(Child)

    ike = AdoptedCanadianChild("Ike")
    ike.label = "Ike"
    ike.is_a.append(Character)
    ike.is_a.append(Child)
    ike.is_a.append(AdoptedChild)
    ike.is_a.append(CanadianChild)
    ike.is_a.append(Boy)

    secondSeason.partOf.append(southPark)
    secondSeason.seasonNumber = 2

    ikeWeeWee.partOf.append(secondSeason)
    ikeWeeWee.partOf.append(southPark)
    ikeWeeWee.episodeNumber = 4
    ikeWeeWee.seasonNumber = 2

    ikeWeeWee.overallEpisodeNumber = 18
    ikeWeeWee.firstAiredOn = may272_1998
    ikeWeeWee.firstAiredOnNetwork = comedyCentral
    ikeWeeWee.firstAiredInCountry = unitedStates
    ikeWeeWee.writtenBy.append(treyParker)
    ikeWeeWee.directedBy.append(treyParker)
    ikeWeeWee.firedCharacter = mrMackey
    ikeWeeWee.introducedBackstoryOf = ike
    ikeWeeWee.criticalReception = "positive responses from critics"
    ikeWeeWee.praisedFor = "touching moments"
    ikeWeeWee.satirizes = "certain attitudes towards drug users"
    ikeWeeWee.explores = "whether family can only mean those who are related by blood"

    southPark.countryOfOrigin = unitedStates
    southPark.coCreatedBy.append(treyParker)

    kyle.hasYoungerBrother.append(ike)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
