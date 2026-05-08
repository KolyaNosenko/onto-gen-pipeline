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
10. What type of vocal range does Marissa Nadler sing in?
11. What professions does Marissa Nadler practice?
12. Which music publications have reviewed or described Marissa Nadler's vocals?
13. What elements does Marissa Nadler's music incorporate beyond country and folk?
14. How many full-length studio albums has Marissa Nadler released?
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

import datetime

# TODO: import the core entity classes you actually subclass.
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    PhysicalObject,
    NonAgentiveSocialObject,
    Society,
    AbstractQuality,
)

# TODO (optional): import the core properties you actually subclass.
# (no core properties subclassed — all domain properties are fresh)


with core:
    # ------------------------------------------------------------------ #
    # Entity Classes                                                       #
    # ------------------------------------------------------------------ #

    class Person(AgentivePhysicalObject):
        pass

    class Musician(Person):
        pass

    class SingerSongwriter(Musician):
        pass

    class FineArtist(Person):
        pass

    class City(PhysicalObject):
        pass

    class USState(NonAgentiveSocialObject):
        pass

    class RecordLabel(Society):
        pass

    class StudioAlbum(NonAgentiveSocialObject):
        pass

    class MusicalGenre(NonAgentiveSocialObject):
        pass

    class MusicPublication(Society):
        pass

    class VocalRange(AbstractQuality):
        pass

    # ------------------------------------------------------------------ #
    # Properties                                                           #
    # ------------------------------------------------------------------ #

    class birthDate(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [datetime.date]

    class nationality(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class basedIn(ObjectProperty):
        domain = [Person]
        range = [City]

    class locatedIn(ObjectProperty):
        domain = [City]
        range = [USState]

    class signedTo(ObjectProperty):
        domain = [Musician]
        range = [RecordLabel]

    class activeFrom(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [int]

    class releasedAlbum(ObjectProperty):
        domain = [Musician]
        range = [StudioAlbum]

    class albumReleaseDate(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [str]

    class albumSequenceNumber(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class hasGenre(ObjectProperty):
        domain = [Musician]
        range = [MusicalGenre]

    class hasVocalRange(ObjectProperty):
        domain = [Person]
        range = [VocalRange]

    class reviewedBy(ObjectProperty):
        domain = [Musician]
        range = [MusicPublication]

    # ------------------------------------------------------------------ #
    # Named Individuals                                                    #
    # ------------------------------------------------------------------ #

    # --- Person ---
    marissaNadler = SingerSongwriter("Marissa_Nadler")
    marissaNadler.label = "Marissa Nadler"
    marissaNadler.is_a.append(FineArtist)
    marissaNadler.birthDate = datetime.date(1981, 4, 5)
    marissaNadler.nationality = "American"
    marissaNadler.activeFrom = 2000

    # --- Places ---
    boston = City("Boston")
    boston.label = "Boston"

    massachusetts = USState("Massachusetts")
    massachusetts.label = "Massachusetts"

    boston.locatedIn.append(massachusetts)
    marissaNadler.basedIn.append(boston)

    # --- Record Labels ---
    sacredBonesRecords = RecordLabel("Sacred_Bones_Records")
    sacredBonesRecords.label = "Sacred Bones Records"

    bellaUnion = RecordLabel("Bella_Union")
    bellaUnion.label = "Bella Union"

    marissaNadler.signedTo.append(sacredBonesRecords)
    marissaNadler.signedTo.append(bellaUnion)

    # --- Studio Album ---
    strangers = StudioAlbum("Strangers")
    strangers.label = "Strangers"
    strangers.albumSequenceNumber = 7
    strangers.albumReleaseDate = "May 2016"

    marissaNadler.releasedAlbum.append(strangers)

    # --- Musical Genres ---
    country = MusicalGenre("country")
    country.label = "country"

    folk = MusicalGenre("folk")
    folk.label = "folk"

    experimental = MusicalGenre("experimental")
    experimental.label = "experimental"

    blackMetal = MusicalGenre("black_metal")
    blackMetal.label = "black metal"

    dreamFolk = MusicalGenre("dream_folk")
    dreamFolk.label = "dream folk"

    marissaNadler.hasGenre.append(country)
    marissaNadler.hasGenre.append(folk)
    marissaNadler.hasGenre.append(experimental)
    marissaNadler.hasGenre.append(blackMetal)
    marissaNadler.hasGenre.append(dreamFolk)

    # --- Vocal Ranges ---
    mezzoSoprano = VocalRange("mezzo_soprano")
    mezzoSoprano.label = "mezzo-soprano"

    soprano = VocalRange("soprano")
    soprano.label = "soprano"

    marissaNadler.hasVocalRange.append(mezzoSoprano)
    marissaNadler.hasVocalRange.append(soprano)

    # --- Music Publications ---
    pitchfork = MusicPublication("Pitchfork")
    pitchfork.label = "Pitchfork"

    bostonGlobe = MusicPublication("The_Boston_Globe")
    bostonGlobe.label = "The Boston Globe"

    marissaNadler.reviewedBy.append(pitchfork)
    marissaNadler.reviewedBy.append(bostonGlobe)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
