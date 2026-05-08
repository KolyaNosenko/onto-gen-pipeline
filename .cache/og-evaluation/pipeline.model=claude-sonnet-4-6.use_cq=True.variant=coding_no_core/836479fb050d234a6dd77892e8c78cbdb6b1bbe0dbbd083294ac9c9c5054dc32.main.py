"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

1. What is the title of the fourth episode of the second season of South Park?
2. Which episode number in the overall series is "Ike's Wee Wee"?
3. On which date did "Ike's Wee Wee" first air?
4. On which television network did "Ike's Wee Wee" first air?
5. Who wrote and directed "Ike's Wee Wee"?
6. What role does Mr. Mackey hold in South Park?
7. What happens to Mr. Mackey in the episode "Ike's Wee Wee"?
8. What social or cultural topics does "Ike's Wee Wee" satirize?
9. What backstory about Ike is introduced in this episode?
10. What is the relationship between Kyle and Ike?
11. What season and episode number does "Ike's Wee Wee" belong to?
12. What country does Ike originally come from?
13. How did critics respond to "Ike's Wee Wee"?
14. What theme related to family does "Ike's Wee Wee" explore?
15. Who is the co-creator of South Park who directed this episode?
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
    # ── Entity classes ────────────────────────────────────────────────────
    class TVSeries(Thing): pass
    class AnimatedTVSeries(TVSeries): pass
    class TVSeason(Thing): pass
    class TVEpisode(Thing): pass
    class TVNetwork(Thing): pass
    class Country(Thing): pass
    class Person(Thing): pass
    class FictionalCharacter(Thing): pass
    class SchoolCounselor(FictionalCharacter): pass

    # ── Object properties ─────────────────────────────────────────────────
    class hasSeason(ObjectProperty):
        domain = [TVSeries]
        range  = [TVSeason]

    class hasEpisode(ObjectProperty):
        domain = [TVSeason]
        range  = [TVEpisode]

    class partOfSeason(ObjectProperty):
        domain = [TVEpisode]
        range  = [TVSeason]

    class partOfSeries(ObjectProperty):
        domain = [TVEpisode]
        range  = [TVSeries]

    class airedOn(ObjectProperty):
        domain = [TVEpisode]
        range  = [TVNetwork]

    class airedIn(ObjectProperty):
        domain = [TVEpisode]
        range  = [Country]

    class writtenBy(ObjectProperty):
        domain = [TVEpisode]
        range  = [Person]

    class directedBy(ObjectProperty):
        domain = [TVEpisode]
        range  = [Person]

    class coCreatedBy(ObjectProperty):
        domain = [TVSeries]
        range  = [Person]

    class features(ObjectProperty):
        domain = [TVEpisode]
        range  = [FictionalCharacter]

    class isYoungerBrotherOf(ObjectProperty):
        domain = [FictionalCharacter]
        range  = [FictionalCharacter]

    class originatesFrom(ObjectProperty):
        domain = [FictionalCharacter]
        range  = [Country]

    # ── Data properties ───────────────────────────────────────────────────
    class hasTitle(DataProperty, FunctionalProperty):
        domain = [TVEpisode]
        range  = [str]

    class hasEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TVEpisode]
        range  = [int]

    class hasOverallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [TVEpisode]
        range  = [int]

    class hasSeasonNumber(DataProperty, FunctionalProperty):
        domain = [TVSeason]
        range  = [int]

    class firstAiredDate(DataProperty, FunctionalProperty):
        domain = [TVEpisode]
        range  = [str]

    class receivedCriticalResponse(DataProperty, FunctionalProperty):
        domain = [TVEpisode]
        range  = [str]

    class satirizes(DataProperty):
        domain = [TVEpisode]
        range  = [str]

    class explores(DataProperty):
        domain = [TVEpisode]
        range  = [str]

    class isAdopted(DataProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range  = [bool]

    class isFired(DataProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range  = [bool]

    class turnsToDrugs(DataProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range  = [bool]

    # ── Individuals ───────────────────────────────────────────────────────

    # TV series
    SouthParkSeries = AnimatedTVSeries("SouthParkSeries")
    SouthParkSeries.label = "South Park"

    # Season
    SouthParkSeason2 = TVSeason("SouthParkSeason2")
    SouthParkSeason2.label = "second season"
    SouthParkSeason2.hasSeasonNumber = 2

    # Episode
    IkesWeeWeeEpisode = TVEpisode("IkesWeeWeeEpisode")
    IkesWeeWeeEpisode.label = "Ike's Wee Wee"
    IkesWeeWeeEpisode.hasTitle = "Ike's Wee Wee"
    IkesWeeWeeEpisode.hasEpisodeNumber = 4
    IkesWeeWeeEpisode.hasOverallEpisodeNumber = 18
    IkesWeeWeeEpisode.firstAiredDate = "May 27, 1998"
    IkesWeeWeeEpisode.receivedCriticalResponse = "positive"
    IkesWeeWeeEpisode.satirizes = ["attitudes towards drug users"]
    IkesWeeWeeEpisode.explores = ["whether family can only mean those who are related by blood"]

    # TV network
    ComedyCentralNetwork = TVNetwork("ComedyCentralNetwork")
    ComedyCentralNetwork.label = "Comedy Central"

    # Countries
    UnitedStatesCountry = Country("UnitedStatesCountry")
    UnitedStatesCountry.label = "United States"

    CanadaCountry = Country("CanadaCountry")
    CanadaCountry.label = "Canada"

    # People
    TreyParkerPerson = Person("TreyParkerPerson")
    TreyParkerPerson.label = "Trey Parker"

    # Fictional characters
    MrMackeyCharacter = SchoolCounselor("MrMackeyCharacter")
    MrMackeyCharacter.label = "Mr. Mackey"
    MrMackeyCharacter.isFired = True
    MrMackeyCharacter.turnsToDrugs = True

    KyleCharacter = FictionalCharacter("KyleCharacter")
    KyleCharacter.label = "Kyle"

    IkeCharacter = FictionalCharacter("IkeCharacter")
    IkeCharacter.label = "Ike"
    IkeCharacter.isAdopted = True
    IkeCharacter.isYoungerBrotherOf = [KyleCharacter]
    IkeCharacter.originatesFrom = [CanadaCountry]

    # ── Relationships ─────────────────────────────────────────────────────
    SouthParkSeries.hasSeason = [SouthParkSeason2]
    SouthParkSeries.coCreatedBy = [TreyParkerPerson]
    SouthParkSeason2.hasEpisode = [IkesWeeWeeEpisode]
    IkesWeeWeeEpisode.partOfSeason = [SouthParkSeason2]
    IkesWeeWeeEpisode.partOfSeries = [SouthParkSeries]
    IkesWeeWeeEpisode.airedOn = [ComedyCentralNetwork]
    IkesWeeWeeEpisode.airedIn = [UnitedStatesCountry]
    IkesWeeWeeEpisode.writtenBy = [TreyParkerPerson]
    IkesWeeWeeEpisode.directedBy = [TreyParkerPerson]
    IkesWeeWeeEpisode.features = [MrMackeyCharacter, KyleCharacter, IkeCharacter]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
