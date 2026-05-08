"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

1. What is the title of the episode?
2. Which television series does the episode belong to?
3. Which season is the episode part of?
4. Which episode number in the season is it?
5. Which episode number overall in the series is it?
6. When did the episode first air?
7. On which television network or channel did the episode first air?
8. In which country did the episode first air?
9. Who wrote the episode?
10. Who directed the episode?
11. Which character is fired in the episode?
12. What does the fired school counselor turn to after being fired?
13. What do the boys misconstrue about circumcision?
14. Whom do the boys try to save from a bris?
15. What relationship does Ike have to Kyle?
16. What is Ike’s background or origin as described in the episode?
17. What themes or attitudes does the episode satirize?
18. What question about family does the episode explore?
19. What kind of critical response did the episode receive?
20. What aspects of the episode did critics especially praise?
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

    class TelevisionSeason(Thing):
        pass

    class Person(Thing):
        pass

    class Character(Person):
        pass

    class SchoolCounselor(Character):
        pass

    class Child(Character):
        pass

    class AdoptedChild(Child):
        pass

    class CanadianChild(Child):
        pass

    class AdoptedCanadianChild(AdoptedChild, CanadianChild):
        equivalent_to = [AdoptedChild & CanadianChild]

    class Writer(Person):
        pass

    class Director(Person):
        pass

    class SeriesCoCreator(Person):
        pass

    class BoyGroup(Thing):
        pass

    class TelevisionNetwork(Thing):
        pass

    class Country(Thing):
        pass

    class TimePoint(Thing):
        pass

    class Drug(Thing):
        pass

    class Bris(Thing):
        pass

    class Theme(Thing):
        pass

    class CriticalResponse(Thing):
        pass

    class title(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [str]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [TelevisionSeason]
        range = [int]

    class episodeNumberInSeason(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class episodeNumberOverall(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class originCountry(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Country]

    class partOfSeries(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]

    class partOfSeason(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeason]

    class firstAiredOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TimePoint]

    class firstAiredOnNetwork(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionNetwork]

    class firstAiredInCountry(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [Country]

    class writtenBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]

    class directedBy(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Person]

    class coCreatedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Person]

    class firedCharacter(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Character]

    class turnsTo(ObjectProperty):
        domain = [Character]
        range = [Drug]

    class isYoungerBrotherOf(ObjectProperty):
        domain = [Character]
        range = [Character]

    class triesToSave(ObjectProperty):
        domain = [BoyGroup]
        range = [Character]

    class misconstrues(ObjectProperty):
        domain = [BoyGroup]
        range = [Thing]

    class fromBris(ObjectProperty):
        domain = [Character]
        range = [Bris]

    class satirizes(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Theme]

    class explores(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Theme]

    class receivedCriticalResponse(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [CriticalResponse]

    class praisedFor(ObjectProperty):
        domain = [CriticalResponse]
        range = [Theme]

    SouthParkSeries = AnimatedTelevisionSeries("SouthParkSeries")
    SouthParkSeries.label = "South Park"

    SecondSeason = TelevisionSeason("SecondSeason")
    SecondSeason.label = "second season"
    SecondSeason.seasonNumber = 2

    ComedyCentralNetwork = TelevisionNetwork("ComedyCentral")
    ComedyCentralNetwork.label = "Comedy Central"

    UnitedStatesCountry = Country("UnitedStates")
    UnitedStatesCountry.label = "United States"

    SouthParkSeries.originCountry = UnitedStatesCountry

    May271998 = TimePoint("May271998")
    May271998.label = "May 27 , 1998"

    IkeWeeWeeEpisode = TelevisionEpisode("IkeWeeWeeEpisode")
    IkeWeeWeeEpisode.label = "Ike 's Wee Wee"
    IkeWeeWeeEpisode.title = "Ike 's Wee Wee"
    IkeWeeWeeEpisode.partOfSeries = SouthParkSeries
    IkeWeeWeeEpisode.partOfSeason = SecondSeason
    IkeWeeWeeEpisode.episodeNumberInSeason = 4
    IkeWeeWeeEpisode.episodeNumberOverall = 18
    IkeWeeWeeEpisode.firstAiredOn = May271998
    IkeWeeWeeEpisode.firstAiredOnNetwork = ComedyCentralNetwork
    IkeWeeWeeEpisode.firstAiredInCountry = UnitedStatesCountry

    TreyParker = SeriesCoCreator("TreyParker")
    TreyParker.label = "Trey Parker"
    TreyParker.is_a.append(Writer)
    TreyParker.is_a.append(Director)
    SouthParkSeries.coCreatedBy = [TreyParker]
    IkeWeeWeeEpisode.writtenBy = [TreyParker]
    IkeWeeWeeEpisode.directedBy = [TreyParker]

    MrMackey = SchoolCounselor("MrMackey")
    MrMackey.label = "Mr. Mackey"
    IkeWeeWeeEpisode.firedCharacter = [MrMackey]

    Drugs = Drug("Drugs")
    Drugs.label = "drugs"
    MrMackey.turnsTo = [Drugs]

    Kyle = Character("Kyle")
    Kyle.label = "Kyle"

    Ike = AdoptedCanadianChild("Ike")
    Ike.label = "Ike"
    Ike.isYoungerBrotherOf = [Kyle]

    UpcomingBris = Bris("UpcomingBris")
    UpcomingBris.label = "his upcoming bris"
    Ike.fromBris = [UpcomingBris]

    TheBoys = BoyGroup("TheBoys")
    TheBoys.label = "the boys"

    WhatCircumcisionEntails = Theme("WhatCircumcisionEntails")
    WhatCircumcisionEntails.label = "what circumcision entails"
    TheBoys.misconstrues = [WhatCircumcisionEntails]
    TheBoys.triesToSave = [Ike]

    CertainAttitudesTowardsDrugUsers = Theme("CertainAttitudesTowardsDrugUsers")
    CertainAttitudesTowardsDrugUsers.label = "certain attitudes towards drug users"
    IkeWeeWeeEpisode.satirizes = [CertainAttitudesTowardsDrugUsers]

    FamilyRelatedByBlood = Theme("FamilyRelatedByBlood")
    FamilyRelatedByBlood.label = "whether family can only mean those who are related by blood"
    IkeWeeWeeEpisode.explores = [FamilyRelatedByBlood]

    PositiveResponsesFromCritics = CriticalResponse("PositiveResponsesFromCritics")
    PositiveResponsesFromCritics.label = "positive responses from critics"
    IkeWeeWeeEpisode.receivedCriticalResponse = PositiveResponsesFromCritics

    ItsTouchingMoments = Theme("ItsTouchingMoments")
    ItsTouchingMoments.label = "its touching moments"
    PositiveResponsesFromCritics.praisedFor = [ItsTouchingMoments]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
