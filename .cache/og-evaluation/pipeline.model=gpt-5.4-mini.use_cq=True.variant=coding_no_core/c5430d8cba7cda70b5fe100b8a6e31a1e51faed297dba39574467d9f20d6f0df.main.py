"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. Who is Marissa Nadler?
2. What is Marissa Nadler’s date of birth?
3. What is Marissa Nadler’s nationality?
4. What is Marissa Nadler’s place of residence or base?
5. Since when has Marissa Nadler been active?
6. Which record labels is Marissa Nadler currently signed to?
7. What is the title of Marissa Nadler’s seventh full-length studio album?
8. When was Marissa Nadler’s seventh full-length studio album released?
9. What is Marissa Nadler’s profession or occupations?
10. What genres or stylistic influences characterize Marissa Nadler’s music?
11. How has Marissa Nadler’s music been described or classified?
12. What term is sometimes used to describe Marissa Nadler’s work?
13. What vocal range does Marissa Nadler sing in?
14. What critical acclaim has Marissa Nadler received for her vocals?
15. How have Pitchfork and The Boston Globe described Marissa Nadler’s voice?
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
    class Person(Thing):
        pass

    class Artist(Person):
        pass

    class Musician(Artist):
        pass

    class FineArtist(Artist):
        pass

    class SingerSongwriter(Musician):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class State(Place):
        pass

    class MythologicalPlace(Place):
        pass

    class Organization(Thing):
        pass

    class RecordLabel(Organization):
        pass

    class Publication(Organization):
        pass

    class Album(Thing):
        pass

    class StudioAlbum(Album):
        pass

    class Nationality(Thing):
        pass

    class Genre(Thing):
        pass

    class Style(Thing):
        pass

    class VocalRange(Thing):
        pass

    class ArtisticQuality(Thing):
        pass

    class TimeMention(Thing):
        pass

    class FullDate(TimeMention):
        pass

    class Year(TimeMention):
        pass

    class MonthYear(TimeMention):
        pass

    class bornOn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [FullDate]

    class nationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Nationality]

    class basedIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class activeSince(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Year]

    class signedTo(ObjectProperty):
        domain = [Person]
        range = [RecordLabel]

    class releasedAlbum(ObjectProperty):
        domain = [Person]
        range = [Album]

    class releaseDate(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [MonthYear]

    class rootedIn(ObjectProperty):
        domain = [Person]
        range = [Genre]

    class bringsInElementsOf(ObjectProperty):
        domain = [Person]
        range = [Genre]

    class describedAsTerm(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Style]

    class singsIn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [VocalRange]

    class receivedAcclaimFor(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [ArtisticQuality]

    class describedBy(ObjectProperty):
        domain = [Person]
        range = [Publication]

    class musicClassification(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class pitchforkDescription(DataProperty):
        domain = [Person]
        range = [str]

    class bostonGlobeDescription(DataProperty):
        domain = [Person]
        range = [str]

    MarissaNadler = SingerSongwriter("MarissaNadler")
    MarissaNadler.label = "Marissa Nadler"
    MarissaNadler.is_a.append(FineArtist)

    American = Nationality("American")
    American.label = "American"

    Boston = City("Boston")
    Boston.label = "Boston"

    Massachusetts = State("Massachusetts")
    Massachusetts.label = "Massachusetts"

    Hades = MythologicalPlace("Hades")
    Hades.label = "Hades"

    SacredBonesRecords = RecordLabel("SacredBonesRecords")
    SacredBonesRecords.label = "Sacred Bones Records"

    BellaUnion = RecordLabel("BellaUnion")
    BellaUnion.label = "Bella Union"

    Strangers = StudioAlbum("Strangers")
    Strangers.label = "Strangers"

    Pitchfork = Publication("Pitchfork")
    Pitchfork.label = "Pitchfork"

    TheBostonGlobe = Publication("TheBostonGlobe")
    TheBostonGlobe.label = "The Boston Globe"

    April51981 = FullDate("April51981")
    April51981.label = "April 5 , 1981"

    Year2000 = Year("Year2000")
    Year2000.label = "2000"

    May2016 = MonthYear("May2016")
    May2016.label = "May 2016"

    OldSchoolCountry = Genre("OldSchoolCountry")
    OldSchoolCountry.label = "old - school country"

    Folk = Genre("Folk")
    Folk.label = "folk"

    Experimental = Genre("Experimental")
    Experimental.label = "experimental"

    BlackMetal = Genre("BlackMetal")
    BlackMetal.label = "black metal"

    DreamFolk = Style("DreamFolk")
    DreamFolk.label = "dream folk"

    MezzoSoprano = VocalRange("MezzoSoprano")
    MezzoSoprano.label = "mezzo - soprano"

    Vocals = ArtisticQuality("Vocals")
    Vocals.label = "vocals"

    MarissaNadler.bornOn = April51981
    MarissaNadler.nationality = American
    MarissaNadler.basedIn = [Boston, Massachusetts]
    MarissaNadler.activeSince = Year2000
    MarissaNadler.signedTo = [SacredBonesRecords, BellaUnion]
    MarissaNadler.releasedAlbum = [Strangers]
    MarissaNadler.rootedIn = [OldSchoolCountry, Folk]
    MarissaNadler.bringsInElementsOf = [Experimental, BlackMetal]
    MarissaNadler.describedAsTerm = DreamFolk
    MarissaNadler.singsIn = MezzoSoprano
    MarissaNadler.receivedAcclaimFor = Vocals
    MarissaNadler.describedBy = [Pitchfork, TheBostonGlobe]
    MarissaNadler.musicClassification = "defies simple classification"
    MarissaNadler.pitchforkDescription = [
        "you would follow straight into Hades",
        "textured and angelic, with just a hint of pain captured within her iridescent falsetto",
    ]
    MarissaNadler.bostonGlobeDescription = [
        "She has a voice that, in mythological times, could have lured men to their deaths at sea, an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights, lingers, and tapers off like rings of smoke"
    ]

    Strangers.releaseDate = May2016


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
