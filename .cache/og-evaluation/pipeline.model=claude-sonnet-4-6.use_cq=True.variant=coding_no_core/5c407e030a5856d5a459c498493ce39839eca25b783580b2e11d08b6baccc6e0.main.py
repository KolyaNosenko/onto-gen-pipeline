"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. What is the birth date of Marissa Nadler?
2. What is the nationality of Marissa Nadler?
3. What city is Marissa Nadler based in?
4. What record labels is Marissa Nadler currently signed to?
5. When did Marissa Nadler become active as a musician?
6. What is the title of Marissa Nadler's seventh studio album?
7. When was Marissa Nadler's seventh studio album released?
8. What musical genres are associated with Marissa Nadler's work?
9. What term has been used to describe Marissa Nadler's musical style?
10. What type of voice does Marissa Nadler have?
11. What professions does Marissa Nadler hold?
12. Which music publications have reviewed or described Marissa Nadler's vocals?
13. What elements does Marissa Nadler's music incorporate beyond country and folk?
14. How has Marissa Nadler's voice been described by The Boston Globe?
15. How has Pitchfork described Marissa Nadler's voice?
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
    class Place(Thing): pass
    class City(Place): pass
    class AdministrativeDivision(Place): pass
    class Country(Place): pass

    class Organisation(Thing): pass
    class RecordLabel(Organisation): pass
    class Publication(Organisation): pass

    class Person(Thing): pass
    class Musician(Person): pass
    class SingerSongwriter(Musician): pass
    class FineArtist(Person): pass

    class CreativeWork(Thing): pass
    class Album(CreativeWork): pass
    class StudioAlbum(Album): pass

    class MusicGenre(Thing): pass
    class VoiceType(Thing): pass
    class VocalDescription(Thing): pass

    # ── Object properties ─────────────────────────────────────────────────
    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range  = [City]

    class locatedIn(ObjectProperty, FunctionalProperty):
        domain = [City]
        range  = [Place]

    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range  = [Country]

    class signedTo(ObjectProperty):
        domain = [Musician]
        range  = [RecordLabel]

    class releasedAlbum(ObjectProperty):
        domain = [Musician]
        range  = [Album]

    class associatedWithGenre(ObjectProperty):
        domain = [Musician]
        range  = [MusicGenre]

    class hasVoiceType(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range  = [VoiceType]

    class hasVocalDescription(ObjectProperty):
        domain = [Musician]
        range  = [VocalDescription]

    class publishedBy(ObjectProperty, FunctionalProperty):
        domain = [VocalDescription]
        range  = [Publication]

    class reviewedBy(ObjectProperty):
        domain = [Musician]
        range  = [Publication]

    # ── Data properties ───────────────────────────────────────────────────
    class birthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class activeFrom(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [int]

    class albumNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range  = [int]

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range  = [str]

    class descriptionText(DataProperty, FunctionalProperty):
        domain = [VocalDescription]
        range  = [str]

    class styleLabel(DataProperty, FunctionalProperty):
        domain = [Musician]
        range  = [str]

    # ── Individuals ───────────────────────────────────────────────────────
    # Places
    bostonInst = City("Boston")
    bostonInst.label = "Boston"

    massachusettsInst = AdministrativeDivision("Massachusetts")
    massachusettsInst.label = "Massachusetts"

    unitedStatesInst = Country("UnitedStates")
    unitedStatesInst.label = "United States"

    bostonInst.locatedIn = massachusettsInst

    # Organisations
    sacredBonesRecords = RecordLabel("SacredBonesRecords")
    sacredBonesRecords.label = "Sacred Bones Records"

    bellaUnion = RecordLabel("BellaUnion")
    bellaUnion.label = "Bella Union"

    pitchfork = Publication("Pitchfork")
    pitchfork.label = "Pitchfork"

    bostonGlobe = Publication("TheBostonGlobe")
    bostonGlobe.label = "The Boston Globe"

    # Music genres
    countryGenre = MusicGenre("CountryGenre")
    countryGenre.label = "country"

    folkGenre = MusicGenre("FolkGenre")
    folkGenre.label = "folk"

    experimentalGenre = MusicGenre("ExperimentalGenre")
    experimentalGenre.label = "experimental"

    blackMetalGenre = MusicGenre("BlackMetalGenre")
    blackMetalGenre.label = "black metal"

    dreamFolkGenre = MusicGenre("DreamFolkGenre")
    dreamFolkGenre.label = "dream folk"

    # Voice type
    mezzoSoprano = VoiceType("MezzoSoprano")
    mezzoSoprano.label = "mezzo-soprano"

    # Vocal descriptions
    pitchforkVocalDesc = VocalDescription("PitchforkVocalDescription")
    pitchforkVocalDesc.label = "Pitchfork vocal description"
    pitchforkVocalDesc.descriptionText = (
        "you would follow straight into Hades; "
        "textured and angelic, with just a hint of pain captured within her iridescent falsetto"
    )
    pitchforkVocalDesc.publishedBy = pitchfork

    bostonGlobeVocalDesc = VocalDescription("BostonGlobeVocalDescription")
    bostonGlobeVocalDesc.label = "The Boston Globe vocal description"
    bostonGlobeVocalDesc.descriptionText = (
        "She has a voice that, in mythological times, could have lured men to their deaths at sea, "
        "an intoxicating soprano drenched in gauzy reverb that hits bell-clear heights, "
        "lingers, and tapers off like rings of smoke"
    )
    bostonGlobeVocalDesc.publishedBy = bostonGlobe

    # Album
    strangersAlbum = StudioAlbum("StrangersAlbum")
    strangersAlbum.label = "Strangers"
    strangersAlbum.albumNumber = 7
    strangersAlbum.releaseDate = "May 2016"

    # Person
    marissaNadler = SingerSongwriter("MarissaNadler")
    marissaNadler.label = "Marissa Nadler"
    marissaNadler.is_a.append(FineArtist)
    marissaNadler.birthDate = "April 5, 1981"
    marissaNadler.activeFrom = 2000
    marissaNadler.basedIn = bostonInst
    marissaNadler.hasNationality = unitedStatesInst
    marissaNadler.signedTo = [sacredBonesRecords, bellaUnion]
    marissaNadler.releasedAlbum = [strangersAlbum]
    marissaNadler.associatedWithGenre = [
        countryGenre, folkGenre, experimentalGenre, blackMetalGenre, dreamFolkGenre
    ]
    marissaNadler.hasVoiceType = mezzoSoprano
    marissaNadler.hasVocalDescription = [pitchforkVocalDesc, bostonGlobeVocalDesc]
    marissaNadler.reviewedBy = [pitchfork, bostonGlobe]
    marissaNadler.styleLabel = "dream folk"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
