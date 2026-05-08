"""
=== TASK INPUT ===
Source text:
" Ike 's Wee Wee " is the fourth episode of the second season of the American animated television series South Park . The 18th episode of the series overall , it first aired on Comedy Central in the United States on May 27 , 1998 . In the episode , school counselor Mr. Mackey is fired , and turns to drugs . Meanwhile , the boys misconstrue what circumcision entails , and try to save Kyle 's younger brother Ike from his upcoming bris . The episode was written and directed by series co - creator Trey Parker . " Ike 's Wee Wee " satirizes certain attitudes towards drug users , and explores whether family can only mean those who are related by blood . This episode introduced Ike 's backstory as an adopted Canadian child . " Ike 's Wee Wee " received positive responses from critics , who especially praised the episode for its touching moments .

# Competency Questions

1. What is the title of the fourth episode of the second season of South Park?
2. Which episode number is "Ike's Wee Wee" in the overall series?
3. When did "Ike's Wee Wee" first air?
4. On which television network did "Ike's Wee Wee" air?
5. Who wrote and directed "Ike's Wee Wee"?
6. What is the main plot point regarding Mr. Mackey in this episode?
7. What misconception do the boys have in "Ike's Wee Wee"?
8. Who is Ike and what is his relationship to Kyle?
9. What is Ike's backstory revealed in this episode?
10. What social themes does "Ike's Wee Wee" satirize?
11. What topics does the episode explore regarding family?
12. How did critics respond to "Ike's Wee Wee"?
13. What aspects of the episode did critics particularly praise?
14. In what season of South Park does "Ike's Wee Wee" appear?
15. What is Ike's country of origin?
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
import datetime

model = get_ontology("https://og.example.org/ontology")


with model:
    # Domain entity classes
    class TelevisionSeries(Thing): pass
    class Episode(Thing): pass
    class Person(Thing): pass
    class Network(Thing): pass
    class Country(Thing): pass
    class Theme(Thing): pass

    # Object Properties
    class belongsToSeries(ObjectProperty):
        domain = [Episode]
        range = [TelevisionSeries]
    
    class airedOn(ObjectProperty):
        domain = [Episode]
        range = [Network]
    
    class airedIn(ObjectProperty):
        domain = [Episode]
        range = [Country]
    
    class writtenBy(ObjectProperty, FunctionalProperty):
        domain = [Episode]
        range = [Person]
    
    class directedBy(ObjectProperty, FunctionalProperty):
        domain = [Episode]
        range = [Person]
    
    class createdBy(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Person]
    
    class youngerBrotherOf(ObjectProperty):
        domain = [Person]
        range = [Person]
    
    class originatesFrom(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Country]
    
    class satirizes(ObjectProperty):
        domain = [Episode]
        range = [Theme]
    
    class explores(ObjectProperty):
        domain = [Episode]
        range = [Theme]

    # Data Properties
    class title(DataProperty, FunctionalProperty):
        domain = [Episode, TelevisionSeries, Theme]
        range = [str]
    
    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [int]
    
    class episodeNumber(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [int]
    
    class overallEpisodeNumber(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [int]
    
    class airDate(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [datetime.date]
    
    class role(DataProperty):
        domain = [Person]
        range = [str]
    
    class isAdopted(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [bool]
    
    class criticalReception(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [str]
    
    class praisedFor(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [str]

    # Concrete instances
    # Episode: "Ike's Wee Wee"
    ikesweewee = Episode("IkesWeeWee")
    ikesweewee.label = "Ike 's Wee Wee"
    ikesweewee.title = "Ike 's Wee Wee"
    ikesweewee.seasonNumber = 2
    ikesweewee.episodeNumber = 4
    ikesweewee.overallEpisodeNumber = 18
    ikesweewee.airDate = datetime.date(1998, 5, 27)
    ikesweewee.criticalReception = "positive"
    ikesweewee.praisedFor = "touching moments"
    
    # TelevisionSeries: South Park
    southpark = TelevisionSeries("SouthPark")
    southpark.label = "South Park"
    southpark.title = "South Park"
    
    # Network: Comedy Central
    comedycentral = Network("ComedyCentral")
    comedycentral.label = "Comedy Central"
    
    # Countries
    unitedstates = Country("UnitedStates")
    unitedstates.label = "United States"
    
    canada = Country("Canada")
    canada.label = "Canada"
    
    # Persons
    treyparker = Person("TreyParker")
    treyparker.label = "Trey Parker"
    
    mr_mackey = Person("MrMackey")
    mr_mackey.label = "Mr. Mackey"
    mr_mackey.role = ["school counselor"]
    
    kyle = Person("Kyle")
    kyle.label = "Kyle"
    
    ike = Person("Ike")
    ike.label = "Ike"
    ike.isAdopted = True
    ike.originatesFrom = canada
    
    # Themes
    druguserstheme = Theme("DrugUsersAttitudes")
    druguserstheme.label = "attitudes towards drug users"
    druguserstheme.title = "attitudes towards drug users"
    
    familytheme = Theme("FamilyBlood")
    familytheme.label = "whether family can only mean those who are related by blood"
    familytheme.title = "whether family can only mean those who are related by blood"
    
    # Establish relationships
    ikesweewee.belongsToSeries = [southpark]
    ikesweewee.airedOn = [comedycentral]
    ikesweewee.airedIn = [unitedstates]
    ikesweewee.writtenBy = treyparker
    ikesweewee.directedBy = treyparker
    ikesweewee.satirizes = [druguserstheme]
    ikesweewee.explores = [familytheme]
    
    southpark.createdBy = [treyparker]
    
    ike.youngerBrotherOf = [kyle]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
