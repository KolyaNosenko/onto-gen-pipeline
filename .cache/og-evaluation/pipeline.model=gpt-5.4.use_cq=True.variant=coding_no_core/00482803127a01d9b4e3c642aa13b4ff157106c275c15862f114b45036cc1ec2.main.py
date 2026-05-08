"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. What is Marissa Nadler’s date of birth?
2. What nationality is Marissa Nadler?
3. What professions or artistic roles does Marissa Nadler have?
4. Where is Marissa Nadler based?
5. Since what year has Marissa Nadler been active?
6. Which record labels is Marissa Nadler currently signed to?
7. What is the title of Marissa Nadler’s seventh full-length studio album?
8. When was the album *Strangers* released?
9. How is Marissa Nadler’s music characterized in terms of genre?
10. What musical elements are said to influence Marissa Nadler’s work?
11. Is Marissa Nadler’s music described as rooted in country and folk?
12. Does Marissa Nadler’s music incorporate experimental and black metal elements?
13. What descriptive term has sometimes been used for Marissa Nadler’s musical style?
14. What vocal range or voice type does Marissa Nadler sing in?
15. Has Marissa Nadler received acclaim for her vocals?
16. Which source described Marissa Nadler’s voice as one “you would follow straight into Hades”?
17. Which source described Marissa Nadler’s voice as “textured and angelic” with “a hint of pain”?
18. Which publication compared Marissa Nadler’s voice to one that could lure men to their deaths at sea?
19. How has Pitchfork characterized Marissa Nadler’s voice?
20. How has The Boston Globe characterized Marissa Nadler’s voice?
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

    class CreativeWork(Thing):
        pass

    class Album(CreativeWork):
        pass

    class StudioAlbum(Album):
        pass

    class FullLengthStudioAlbum(StudioAlbum):
        pass

    class Genre(Thing):
        pass

    class VoiceType(Thing):
        pass

    class Nationality(Thing):
        pass

    class TimePoint(Thing):
        pass

    class CalendarDate(TimePoint):
        pass

    class Year(TimePoint):
        pass

    class MonthYear(TimePoint):
        pass

    class OrdinalPosition(Thing):
        pass

    class basedIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class locatedIn(ObjectProperty):
        domain = [Place]
        range = [Place]

    class hasNationality(ObjectProperty):
        domain = [Person]
        range = [Nationality]

    class bornOn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [CalendarDate]

    class activeSince(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Year]

    class currentlySignedTo(ObjectProperty):
        domain = [Person]
        range = [RecordLabel]

    class releasedAlbum(ObjectProperty):
        domain = [Person]
        range = [Album]

    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [TimePoint]

    class hasOrdinalPosition(ObjectProperty, FunctionalProperty):
        domain = [Album]
        range = [OrdinalPosition]

    class musicRootedInGenre(ObjectProperty):
        domain = [Person]
        range = [Genre]

    class musicIncorporatesElementOfGenre(ObjectProperty):
        domain = [Person]
        range = [Genre]

    class describedAsGenre(ObjectProperty):
        domain = [Person]
        range = [Genre]

    class singsInVoiceType(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [VoiceType]

    class describesVoiceOf(ObjectProperty):
        domain = [Publication]
        range = [Person]

    class referencesPlace(ObjectProperty):
        domain = [Publication]
        range = [Place]

    class musicClassificationDescription(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class hasReceivedAcclaimForVocals(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [bool]

    class voiceCharacterization(DataProperty):
        domain = [Publication]
        range = [str]

    marissaNadler = SingerSongwriter("MarissaNadler")
    marissaNadler.label = "Marissa Nadler"
    marissaNadler.is_a.append(FineArtist)

    american = Nationality("AmericanNationality")
    american.label = "American"
    marissaNadler.hasNationality = [american]

    boston = City("Boston")
    boston.label = "Boston"
    marissaNadler.basedIn = [boston]

    april51981 = CalendarDate("April51981")
    april51981.label = "April 5 , 1981"
    marissaNadler.bornOn = april51981

    year2000 = Year("Year2000")
    year2000.label = "2000"
    marissaNadler.activeSince = year2000

    sacredBonesRecords = RecordLabel("SacredBonesRecords")
    sacredBonesRecords.label = "Sacred Bones Records"
    bellaUnion = RecordLabel("BellaUnion")
    bellaUnion.label = "Bella Union"
    marissaNadler.currentlySignedTo = [sacredBonesRecords, bellaUnion]

    marissaNadler.musicClassificationDescription = "defies simple classification"

    oldSchoolCountry = Genre("OldSchoolCountry")
    oldSchoolCountry.label = "old - school country"
    folk = Genre("Folk")
    folk.label = "folk"
    marissaNadler.musicRootedInGenre = [oldSchoolCountry, folk]

    experimental = Genre("Experimental")
    experimental.label = "experimental"
    blackMetal = Genre("BlackMetal")
    blackMetal.label = "black metal"
    marissaNadler.musicIncorporatesElementOfGenre = [experimental, blackMetal]

    dreamFolk = Genre("DreamFolk")
    dreamFolk.label = "dream folk"
    marissaNadler.describedAsGenre = [dreamFolk]

    mezzoSoprano = VoiceType("MezzoSoprano")
    mezzoSoprano.label = "mezzo - soprano"
    marissaNadler.singsInVoiceType = mezzoSoprano
    marissaNadler.hasReceivedAcclaimForVocals = True

    massachusetts = State("Massachusetts")
    massachusetts.label = "Massachusetts"
    boston.locatedIn = [massachusetts]

    strangers = FullLengthStudioAlbum("Strangers")
    strangers.label = "Strangers"
    seventh = OrdinalPosition("Seventh")
    seventh.label = "seventh"
    strangers.hasOrdinalPosition = seventh
    may2016 = MonthYear("May2016")
    may2016.label = "May 2016"
    strangers.releasedIn = may2016
    marissaNadler.releasedAlbum = [strangers]

    pitchfork = Publication("Pitchfork")
    pitchfork.label = "Pitchfork"
    pitchfork.describesVoiceOf = [marissaNadler]
    hades = MythologicalPlace("Hades")
    hades.label = "Hades"
    pitchfork.referencesPlace = [hades]
    pitchfork.voiceCharacterization = [
        "you would follow straight into Hades",
        "textured and angelic , with just a hint of pain captured within her iridescent falsetto",
    ]

    theBostonGlobe = Publication("TheBostonGlobe")
    theBostonGlobe.label = "The Boston Globe"
    theBostonGlobe.describesVoiceOf = [marissaNadler]
    theBostonGlobe.voiceCharacterization = [
        "She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke"
    ]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
