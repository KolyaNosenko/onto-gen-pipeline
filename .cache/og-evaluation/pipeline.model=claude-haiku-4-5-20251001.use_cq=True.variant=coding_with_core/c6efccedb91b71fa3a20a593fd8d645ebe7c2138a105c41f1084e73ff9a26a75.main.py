"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. Who is Marissa Nadler and what is her nationality?
2. When was Marissa Nadler born?
3. Where is Marissa Nadler based?
4. What record labels is Marissa Nadler signed to?
5. What is the title and release date of Marissa Nadler's seventh studio album?
6. How many studio albums has Marissa Nadler released?
7. What music genres does Marissa Nadler's work incorporate?
8. What is Marissa Nadler's vocal range classification?
9. When did Marissa Nadler become active as a musician?
10. What are the critical descriptions of Marissa Nadler's voice?
11. Which publications have reviewed or described Marissa Nadler's vocal abilities?
12. What art forms does Marissa Nadler practice besides music?
13. What alternative genre descriptors have been used to classify Marissa Nadler's music?
14. How have critics compared Marissa Nadler's voice to mythological or metaphorical concepts?
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
    Society,
    SpaceRegion,
    AbstractQuality,
)


with core:
    # Entity classes
    
    class Person(AgentivePhysicalObject):
        """A human being with agency and intentions."""
        pass
    
    class Musician(Person):
        """A person who performs music."""
        pass
    
    class FineArtist(Person):
        """A person who creates fine art."""
        pass
    
    class Album(NonPhysicalObject):
        """A collection of recorded music."""
        pass
    
    class RecordLabel(Society):
        """An organization that produces and distributes recordings."""
        pass
    
    class Publication(Society):
        """A media organization that publishes content."""
        pass
    
    class Place(SpaceRegion):
        """A geographic location."""
        pass
    
    class MusicGenre(NonPhysicalObject):
        """A style or category of music."""
        pass
    
    class VocalRange(AbstractQuality):
        """A classification of singing voice range."""
        pass
    
    class Nationality(NonPhysicalObject):
        """A classification of national origin."""
        pass
    
    # Properties
    
    class birthDate(DataProperty, FunctionalProperty):
        """The date of birth of a person."""
        domain = [Person]
        range = [str]
    
    class hasNationality(ObjectProperty, FunctionalProperty):
        """The nationality of a person."""
        domain = [Person]
        range = [Nationality]
    
    class basedIn(ObjectProperty):
        """The place where a person is based or lives."""
        domain = [Person]
        range = [Place]
    
    class activeFrom(DataProperty, FunctionalProperty):
        """The year or date when a musician became active."""
        domain = [Musician]
        range = [int]
    
    class signedTo(ObjectProperty):
        """A record label that a musician is signed to."""
        domain = [Musician]
        range = [RecordLabel]
    
    class releasedAlbum(ObjectProperty):
        """An album released by a musician."""
        domain = [Musician]
        range = [Album]
    
    class hasGenre(ObjectProperty):
        """A music genre associated with a musician or album."""
        domain = [Musician, Album]
        range = [MusicGenre]
    
    class hasVocalRange(ObjectProperty):
        """A vocal range classification of a musician."""
        domain = [Musician]
        range = [VocalRange]
    
    class releaseDate(DataProperty, FunctionalProperty):
        """The release date of an album."""
        domain = [Album]
        range = [str]
    
    class albumNumber(DataProperty, FunctionalProperty):
        """The album number in an artist's discography."""
        domain = [Album]
        range = [int]
    
    class describedVoiceAbout(ObjectProperty, FunctionalProperty):
        """A musician whose voice is described by a publication."""
        domain = [Publication]
        range = [Musician]
    
    class hasVoiceDescription(DataProperty):
        """A critical description of a musician's voice."""
        domain = [Publication]
        range = [str]
    
    # Named instances
    
    marissa_nadler = Musician("MarissaNadler")
    marissa_nadler.label = "Marissa Nadler"
    
    # Also mark her as a fine artist (same IRI, different type)
    FineArtist("MarissaNadler")
    
    strangers = Album("Strangers")
    strangers.label = "Strangers"
    
    sacred_bones_records = RecordLabel("SacredBonesRecords")
    sacred_bones_records.label = "Sacred Bones Records"
    
    bella_union = RecordLabel("BellaUnion")
    bella_union.label = "Bella Union"
    
    pitchfork = Publication("Pitchfork")
    pitchfork.label = "Pitchfork"
    
    boston_globe = Publication("TheBostonGlobe")
    boston_globe.label = "The Boston Globe"
    
    boston = Place("Boston")
    boston.label = "Boston"
    
    massachusetts = Place("Massachusetts")
    massachusetts.label = "Massachusetts"
    
    american = Nationality("American")
    american.label = "American"
    
    country = MusicGenre("Country")
    country.label = "country"
    
    folk = MusicGenre("Folk")
    folk.label = "folk"
    
    experimental = MusicGenre("Experimental")
    experimental.label = "experimental"
    
    black_metal = MusicGenre("BlackMetal")
    black_metal.label = "black metal"
    
    dream_folk = MusicGenre("DreamFolk")
    dream_folk.label = "dream folk"
    
    mezzo_soprano = VocalRange("MezzoSoprano")
    mezzo_soprano.label = "mezzo-soprano"
    
    falsetto = VocalRange("Falsetto")
    falsetto.label = "falsetto"
    
    soprano = VocalRange("Soprano")
    soprano.label = "soprano"
    
    # Relationships
    
    marissa_nadler.birthDate = "April 5, 1981"
    marissa_nadler.hasNationality = american
    marissa_nadler.basedIn = [boston, massachusetts]
    marissa_nadler.activeFrom = 2000
    marissa_nadler.signedTo = [sacred_bones_records, bella_union]
    marissa_nadler.releasedAlbum = [strangers]
    marissa_nadler.hasGenre = [country, folk, experimental, black_metal, dream_folk]
    marissa_nadler.hasVocalRange = [mezzo_soprano, falsetto, soprano]
    
    strangers.releaseDate = "May 2016"
    strangers.albumNumber = 7
    strangers.hasGenre = [country, folk, experimental, black_metal, dream_folk]
    
    pitchfork.describedVoiceAbout = marissa_nadler
    pitchfork.hasVoiceDescription = [
        "you would follow straight into Hades",
        "textured and angelic, with just a hint of pain captured within her iridescent falsetto"
    ]
    
    boston_globe.describedVoiceAbout = marissa_nadler
    boston_globe.hasVoiceDescription = [
        "She has a voice that, in mythological times, could have lured men to their deaths at sea, "
        "an intoxicating soprano drenched in gauzy reverb that hits bell-clear heights, lingers, and tapers off like rings of smoke"
    ]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
