"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

1. What is The Celebrity Apprentice and what type of television show is it?
2. Who hosted The Celebrity Apprentice and during what time periods?
3. When was The Celebrity Apprentice canceled?
4. What is the opening theme song of The Celebrity Apprentice?
5. How does The Celebrity Apprentice differ from The Apprentice in terms of participants?
6. What is the purpose or goal for which celebrities compete on The Celebrity Apprentice?
7. What types of media backgrounds do the celebrities on The Celebrity Apprentice come from?
8. How are the seasons of The Celebrity Apprentice linked to The Apprentice?
9. Which seasons of The Apprentice and The Celebrity Apprentice are considered part of the overall series?
10. Why might some celebrities on The Celebrity Apprentice be considered "out of the public eye"?
11. What charitable organizations have been benefited through The Celebrity Apprentice competition?
12. How does The Celebrity Apprentice relate to or vary from its precursor show The Apprentice?
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
    # Entity classes
    class Role(Thing):
        pass
    
    class RealEstateDeveloper(Role):
        pass
    
    class President(Role):
        pass
    
    class Actor(Role):
        pass
    
    class Governor(Role):
        pass
    
    class Chairman(Role):
        pass
    
    class Person(Thing):
        pass
    
    class Celebrity(Person):
        pass
    
    class Organization(Thing):
        pass
    
    class MusicGroup(Organization):
        pass
    
    class Song(Thing):
        pass
    
    class TelevisionSeries(Thing):
        pass
    
    class RealityCompetitionSeries(TelevisionSeries):
        pass
    
    class Hosting(Thing):
        pass
    
    class MediaField(Thing):
        pass
    
    class Sitcom(MediaField):
        pass
    
    class ProfessionalSports(MediaField):
        pass
    
    class MusicIndustry(MediaField):
        pass
    
    class RealityTelevision(MediaField):
        pass
    
    class Radio(MediaField):
        pass
    
    class CharitableOrganization(Organization):
        pass
    
    # Object Properties
    class hasRole(ObjectProperty):
        domain = [Person]
        range = [Role]
    
    class hasHosting(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Hosting]
    
    class host(ObjectProperty):
        domain = [Hosting]
        range = [Person]
    
    class hasOpeningThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Song]
    
    class composedBy(ObjectProperty):
        domain = [Song]
        range = [MusicGroup]
    
    class isVariationOf(ObjectProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]
    
    class hasMediaBackground(ObjectProperty):
        domain = [Celebrity]
        range = [MediaField]
    
    class competesFor(ObjectProperty):
        domain = [Celebrity]
        range = [CharitableOrganization]
    
    # Data Properties
    class hostingStartYear(DataProperty, FunctionalProperty):
        domain = [Hosting]
        range = [int]
    
    class hostingEndYear(DataProperty, FunctionalProperty):
        domain = [Hosting]
        range = [int]
    
    class seasonNumbers(DataProperty):
        domain = [TelevisionSeries]
        range = [int]
    
    class cancelledDate(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]
    
    # TV Shows
    the_celebrity_apprentice = RealityCompetitionSeries("TheCelebrityApprentice")
    the_celebrity_apprentice.label = "The Celebrity Apprentice"
    
    the_apprentice = TelevisionSeries("TheApprentice")
    the_apprentice.label = "The Apprentice"
    
    # People
    donald_trump = Person("DonaldTrump")
    donald_trump.label = "Donald Trump"
    
    arnold_schwarzenegger = Person("ArnoldSchwarzenegger")
    arnold_schwarzenegger.label = "Arnold Schwarzenegger"
    
    bob_greenblatt = Person("BobGreenblatt")
    bob_greenblatt.label = "Bob Greenblatt"
    
    # Roles
    real_estate_developer = RealEstateDeveloper("RealEstateDeveloper_inst")
    real_estate_developer.label = "real estate developer"
    
    president = President("President_inst")
    president.label = "U.S. President"
    
    actor_role = Actor("Actor_inst")
    actor_role.label = "actor"
    
    governor = Governor("Governor_inst")
    governor.label = "former California Governor"
    
    chairman = Chairman("Chairman_inst")
    chairman.label = "NBC Entertainment Chairman"
    
    # Link people to roles
    donald_trump.hasRole = [real_estate_developer, president]
    arnold_schwarzenegger.hasRole = [actor_role, governor]
    bob_greenblatt.hasRole = [chairman]
    
    # Organizations and songs
    the_ojays = MusicGroup("TheOJays")
    the_ojays.label = "The O'Jays"
    
    for_the_love_of_money = Song("ForTheLoveOfMoney")
    for_the_love_of_money.label = "For the Love of Money"
    for_the_love_of_money.composedBy = [the_ojays]
    
    # Hosting periods
    hosting_trump = Hosting("Hosting_Trump")
    hosting_trump.label = "Hosting by Donald Trump (2008-2015)"
    hosting_trump.host = [donald_trump]
    hosting_trump.hostingStartYear = 2008
    hosting_trump.hostingEndYear = 2015
    
    hosting_schwarzenegger = Hosting("Hosting_Schwarzenegger")
    hosting_schwarzenegger.label = "Hosting by Arnold Schwarzenegger (January 2017)"
    hosting_schwarzenegger.host = [arnold_schwarzenegger]
    hosting_schwarzenegger.hostingStartYear = 2017
    
    # Link shows to properties
    the_celebrity_apprentice.hasHosting = [hosting_trump, hosting_schwarzenegger]
    the_celebrity_apprentice.hasOpeningThemeSong = for_the_love_of_money
    the_apprentice.hasOpeningThemeSong = for_the_love_of_money
    
    the_celebrity_apprentice.isVariationOf = [the_apprentice]
    
    the_celebrity_apprentice.seasonNumbers = [7, 8, 9, 11, 12, 13, 14, 15]
    the_apprentice.seasonNumbers = [1, 2, 3, 4, 5, 6, 10]
    
    the_celebrity_apprentice.cancelledDate = "August 3, 2017"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
