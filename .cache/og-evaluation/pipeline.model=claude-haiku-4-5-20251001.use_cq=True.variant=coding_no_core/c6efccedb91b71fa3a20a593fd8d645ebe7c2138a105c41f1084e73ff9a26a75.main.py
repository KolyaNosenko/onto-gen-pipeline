"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. Who is Marissa Nadler and what is her profession?
2. When was Marissa Nadler born?
3. Where is Marissa Nadler based?
4. Which record labels is Marissa Nadler signed to?
5. What is the title of Marissa Nadler's seventh studio album and when was it released?
6. How long has Marissa Nadler been active as a musician?
7. What musical genres and styles characterize Marissa Nadler's work?
8. What vocal range does Marissa Nadler have?
9. How have music critics described Marissa Nadler's voice?
10. What publications have reviewed or commented on Marissa Nadler's vocal abilities?
11. What term has been used to describe Marissa Nadler's musical style?
12. What are the influences in Marissa Nadler's music?
=== END TASK INPUT ===

Domain model entry point (no-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
a fresh `with model:` block and writes the resulting graph to
`output.txt` in this directory.
"""
from datetime import date
from og_sandbox_no_core.engine import (
    Thing, ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    Or, And, Not,
    get_ontology, default_world,
)

model = get_ontology("https://og.example.org/ontology")


with model:
    # === ENTITY CLASSES ===
    
    class Person(Thing):
        pass
    
    class Musician(Person):
        pass
    
    class SingerSongwriter(Musician):
        pass
    
    class FineArtist(Person):
        pass
    
    class RecordLabel(Thing):
        pass
    
    class Album(Thing):
        pass
    
    class Place(Thing):
        pass
    
    class Publication(Thing):
        pass
    
    class MusicGenre(Thing):
        pass
    
    class CountryMusic(MusicGenre):
        pass
    
    class FolkMusic(MusicGenre):
        pass
    
    class ExperimentalMusic(MusicGenre):
        pass
    
    class BlackMetal(MusicGenre):
        pass
    
    class DreamFolk(MusicGenre):
        pass
    
    class VoiceDescription(Thing):
        pass
    
    # === OBJECT PROPERTIES ===
    
    class basedIn(ObjectProperty):
        domain = [Person]
        range = [Place]
    
    class signedTo(ObjectProperty):
        domain = [Musician]
        range = [RecordLabel]
    
    class hasAlbum(ObjectProperty):
        domain = [Musician]
        range = [Album]
    
    class musicGenres(ObjectProperty):
        domain = [Musician]
        range = [MusicGenre]
    
    class voiceDescription(ObjectProperty):
        domain = [Musician]
        range = [VoiceDescription]
    
    class descriptionAuthor(ObjectProperty, FunctionalProperty):
        domain = [VoiceDescription]
        range = [Publication]
    
    # === DATA PROPERTIES ===
    
    class bornOn(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [date]
    
    class activeFrom(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [int]
    
    class releaseDate(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [date]
    
    class vocalRange(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [str]
    
    class descriptionContent(DataProperty, FunctionalProperty):
        domain = [VoiceDescription]
        range = [str]
    
    class albumNumber(DataProperty, FunctionalProperty):
        domain = [Album]
        range = [int]
    
    # === INDIVIDUALS ===
    
    # Places
    boston = Place("Boston")
    boston.label = "Boston"
    
    massachusetts = Place("Massachusetts")
    massachusetts.label = "Massachusetts"
    
    # Record Labels
    sacred_bones = RecordLabel("SacredBonesRecords")
    sacred_bones.label = "Sacred Bones Records"
    
    bella_union = RecordLabel("BellaUnion")
    bella_union.label = "Bella Union"
    
    # Album
    strangers = Album("Strangers")
    strangers.label = "Strangers"
    strangers.releaseDate = date(2016, 5, 15)
    strangers.albumNumber = 7
    
    # Music Genres
    country = CountryMusic("CountryGenre")
    country.label = "country"
    
    folk = FolkMusic("FolkGenre")
    folk.label = "folk"
    
    experimental = ExperimentalMusic("ExperimentalGenre")
    experimental.label = "experimental"
    
    black_metal = BlackMetal("BlackMetalGenre")
    black_metal.label = "black metal"
    
    dream_folk = DreamFolk("DreamFolkGenre")
    dream_folk.label = "dream folk"
    
    # Publications
    pitchfork = Publication("Pitchfork")
    pitchfork.label = "Pitchfork"
    
    boston_globe = Publication("BostonGlobe")
    boston_globe.label = "The Boston Globe"
    
    # Voice Descriptions
    desc1 = VoiceDescription()
    desc1.descriptionContent = 'one " you would follow straight into Hades "'
    desc1.descriptionAuthor = pitchfork
    
    desc2 = VoiceDescription()
    desc2.descriptionContent = '" textured and angelic , with just a hint of pain captured within her iridescent falsetto "'
    desc2.descriptionAuthor = pitchfork
    
    desc3 = VoiceDescription()
    desc3.descriptionContent = '" She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke "'
    desc3.descriptionAuthor = boston_globe
    
    # Person: Marissa Nadler
    marissa_nadler = SingerSongwriter("MarissaNadler")
    marissa_nadler.label = "Marissa Nadler"
    marissa_nadler.bornOn = date(1981, 4, 5)
    marissa_nadler.activeFrom = 2000
    marissa_nadler.vocalRange = "mezzo-soprano"
    marissa_nadler.basedIn = [boston]
    marissa_nadler.signedTo = [sacred_bones, bella_union]
    marissa_nadler.hasAlbum = [strangers]
    marissa_nadler.musicGenres = [country, folk, experimental, black_metal, dream_folk]
    marissa_nadler.voiceDescription = [desc1, desc2, desc3]
    
    # Also make her a FineArtist (IRI deduplication means this adds the class membership)
    FineArtist("MarissaNadler")


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
