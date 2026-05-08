"""
=== TASK INPUT ===
Source text:
The Celebrity Apprentice is an American television reality competition series . It is a variation of The Apprentice series , and was hosted by real estate developer ( and now U.S. President ) Donald Trump from 2008 to 2015 , and actor and former California Governor Arnold Schwarzenegger from January 2017 . On August 3 , 2017 , NBC Entertainment Chairman Bob Greenblatt said that the show has effectively been canceled . Like its precursor , the show 's opening theme song is " For the Love of Money " by The O'Jays . Unlike its precursor , however , Celebrity Apprentice consists of celebrities as competing apprentices rather than unknowns . Some of the celebrities are relatively current while others tend to be those who have been out of the public eye for some time . All of them are competing to win money for a charitable organization of their choice . The celebrities come from a wide variety of different fields in the media : sitcoms , professional sports , music industry , reality television , radio , and other backgrounds . The Celebrity Apprentice is linked in seasons to its precursor TV show , The Apprentice , which consists of seasons one to six and season ten . The Celebrity Apprentice consists of seasons seven to nine and eleven to fifteen .

1. What type of television series is The Celebrity Apprentice?
2. Which television series is The Celebrity Apprentice a variation of?
3. Who hosted The Celebrity Apprentice from 2008 to 2015?
4. Who hosted The Celebrity Apprentice starting in January 2017?
5. On what date was the show effectively canceled?
6. Who announced that the show had effectively been canceled?
7. What is the opening theme song of The Celebrity Apprentice?
8. Which band performs the opening theme song of The Celebrity Apprentice?
9. How does The Celebrity Apprentice differ from its precursor regarding the competitors?
10. What are the participants in The Celebrity Apprentice competing to win?
11. For what kind of organization do the celebrities compete to win money?
12. From which fields do the celebrities on The Celebrity Apprentice come?
13. Which seasons of The Apprentice are linked to The Celebrity Apprentice?
14. Which season range does The Celebrity Apprentice consist of?
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
    NonPhysicalObject,
    SocialObject,
    State,
    TimeInterval,
)


with core:
    class TelevisionSeries(NonPhysicalObject):
        pass

    class RealityCompetitionSeries(TelevisionSeries):
        pass

    class AmericanRealityCompetitionSeries(RealityCompetitionSeries):
        pass

    class Organization(SocialObject):
        pass

    class Broadcaster(Organization):
        pass

    class CharitableOrganization(Organization):
        pass

    class Band(Organization):
        pass

    class Country(SocialObject):
        pass

    class Occupation(NonPhysicalObject):
        pass

    class RealEstateDeveloper(Occupation):
        pass

    class Actor(Occupation):
        pass

    class President(Occupation):
        pass

    class Governor(Occupation):
        pass

    class Chairman(Occupation):
        pass

    class Person(AgentivePhysicalObject):
        pass

    class Apprentice(Person):
        pass

    class Celebrity(Apprentice):
        pass

    class UnknownPerson(Apprentice):
        pass

    class Song(NonPhysicalObject):
        pass

    class ThemeSong(Song):
        pass

    class Season(NonPhysicalObject):
        pass

    class Field(NonPhysicalObject):
        pass

    class MediaField(Field):
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

    class OtherBackground(MediaField):
        pass

    class Money(NonPhysicalObject):
        pass

    class variationOf(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class linkedInSeasonsTo(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TelevisionSeries]

    class openingThemeSong(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Song]

    class performedBy(ObjectProperty, FunctionalProperty):
        domain = [Song]
        range = [Band]

    class hasHost(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Person]

    class hasSeason(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Season]

    class hasCompetitor(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Apprentice]

    class comesFromField(ObjectProperty):
        domain = [Celebrity]
        range = [MediaField]


    class competesToWin(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Money]

    class competesForBenefitOf(ObjectProperty):
        domain = [TelevisionSeries]
        range = [CharitableOrganization]

    class chairmanOf(ObjectProperty, FunctionalProperty):
        domain = [Chairman]
        range = [Organization]

    class presidentOf(ObjectProperty, FunctionalProperty):
        domain = [President]
        range = [Country]

    class governorOf(ObjectProperty, FunctionalProperty):
        domain = [Governor]
        range = [State]

    class canceledOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [TimeInterval]

    class announcedCancellationOf(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TelevisionSeries]

    class announcedCancellationOn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]

    class hostedFromDate(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]

    class hostedUntilDate(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]

    class seasonNumber(DataProperty, FunctionalProperty):
        domain = [Season]
        range = [int]

    def make_labeled(cls, local_name, label):
        entity = cls(local_name)
        entity.label = label
        return entity

    Celebrity.is_a.append(comesFromField.some(Or([
        Sitcom,
        ProfessionalSports,
        MusicIndustry,
        RealityTelevision,
        Radio,
        OtherBackground,
    ])))

    TheCelebrityApprentice = AmericanRealityCompetitionSeries("TheCelebrityApprentice")
    TheCelebrityApprentice.label = "The Celebrity Apprentice"

    TheApprentice = TelevisionSeries("TheApprentice")
    TheApprentice.label = "The Apprentice"

    DonaldTrump = Person("DonaldTrump")
    DonaldTrump.label = "Donald Trump"
    DonaldTrump.is_a.append(RealEstateDeveloper)
    DonaldTrump.is_a.append(President)

    ArnoldSchwarzenegger = Person("ArnoldSchwarzenegger")
    ArnoldSchwarzenegger.label = "Arnold Schwarzenegger"
    ArnoldSchwarzenegger.is_a.append(Actor)
    ArnoldSchwarzenegger.is_a.append(Governor)

    BobGreenblatt = Person("BobGreenblatt")
    BobGreenblatt.label = "Bob Greenblatt"
    BobGreenblatt.is_a.append(Chairman)

    NBCEntertainment = Broadcaster("NBCEntertainment")
    NBCEntertainment.label = "NBC Entertainment"

    TheOJays = Band("TheOJays")
    TheOJays.label = "The O'Jays"

    ForTheLoveOfMoney = ThemeSong("ForTheLoveOfMoney")
    ForTheLoveOfMoney.label = "For the Love of Money"

    MoneyPrize = Money("MoneyPrize")
    MoneyPrize.label = "money"

    January2017 = make_labeled(TimeInterval, "January2017", "January 2017")
    August32017 = make_labeled(TimeInterval, "August32017", "August 3, 2017")
    Year2008 = make_labeled(TimeInterval, "Year2008", "2008")
    Year2015 = make_labeled(TimeInterval, "Year2015", "2015")

    California = State("California")
    California.label = "California"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "U.S."

    season_names = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
    }
    seasons = {}
    for number, word in season_names.items():
        season = make_labeled(Season, f"Season{word}", f"season {word.lower()}")
        season.seasonNumber = number
        seasons[number] = season

    TheCelebrityApprentice.variationOf = TheApprentice
    TheCelebrityApprentice.linkedInSeasonsTo = TheApprentice
    TheCelebrityApprentice.openingThemeSong = ForTheLoveOfMoney
    TheCelebrityApprentice.hasHost = [DonaldTrump, ArnoldSchwarzenegger]
    TheCelebrityApprentice.competesToWin = MoneyPrize
    TheCelebrityApprentice.is_a.append(hasCompetitor.some(Celebrity))
    TheCelebrityApprentice.is_a.append(competesForBenefitOf.some(CharitableOrganization))
    TheCelebrityApprentice.canceledOn = August32017

    TheApprentice.is_a.append(hasCompetitor.some(UnknownPerson))

    ForTheLoveOfMoney.performedBy = TheOJays
    BobGreenblatt.chairmanOf = NBCEntertainment
    BobGreenblatt.announcedCancellationOf = TheCelebrityApprentice
    BobGreenblatt.announcedCancellationOn = August32017

    DonaldTrump.hostedFromDate = Year2008
    DonaldTrump.hostedUntilDate = Year2015
    DonaldTrump.presidentOf = UnitedStates

    ArnoldSchwarzenegger.hostedFromDate = January2017
    ArnoldSchwarzenegger.governorOf = California

    TheApprentice.hasSeason = [seasons[n] for n in [1, 2, 3, 4, 5, 6, 10]]
    TheCelebrityApprentice.hasSeason = [seasons[n] for n in [7, 8, 9, 11, 12, 13, 14, 15]]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
