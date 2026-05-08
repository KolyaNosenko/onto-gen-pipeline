"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

1. What is the birth date of Marissa Nadler?
2. What is the nationality of Marissa Nadler?
3. In which city and state is Marissa Nadler based?
4. Since when has Marissa Nadler been active as a musician?
5. Which record labels is Marissa Nadler currently signed to?
6. What is the title of Marissa Nadler’s seventh full-length studio album?
7. In which month and year was the album *Strangers* released?
8. What is Marissa Nadler’s primary profession or role in music?
9. How is Marissa Nadler’s music classified or described stylistically?
10. Which musical traditions or genres are rooted in Marissa Nadler’s work?
11. Which additional musical elements are present in Marissa Nadler’s music?
12. Has the term “dream folk” been used to describe Marissa Nadler’s work?
13. What is Marissa Nadler’s vocal range?
14. What critical acclaim has Marissa Nadler received for her vocals?
15. How did Pitchfork describe Marissa Nadler’s voice?
16. How did The Boston Globe describe Marissa Nadler’s voice?
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
    Abstract,
    AgentiveSocialObject,
    NonAgentiveSocialObject,
    PhysicalQuality,
    SocialAgent,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import directQualityOf


with core:
    class Musician(SocialAgent):
        pass

    class FineArtist(SocialAgent):
        pass

    class SingerSongwriter(Musician):
        pass

    class RecordLabel(AgentiveSocialObject):
        pass

    class Publication(NonAgentiveSocialObject):
        pass

    class MusicalWork(NonAgentiveSocialObject):
        pass

    class StudioAlbum(MusicalWork):
        pass

    class FullLengthStudioAlbum(StudioAlbum):
        pass

    class City(SpaceRegion):
        pass

    class State(SpaceRegion):
        pass

    class MusicalStyle(Abstract):
        pass

    class Voice(PhysicalQuality):
        pass

    class VocalRange(PhysicalQuality):
        pass

    class MythologicalPlace(Abstract):
        pass

    class birthDate(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range = [TimeInterval]

    class activeSince(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range = [TimeInterval]

    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Musician]
        range = [City]

    class locatedIn(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [State]

    class signedTo(ObjectProperty):
        domain = [Musician]
        range = [RecordLabel]

    class hasWork(ObjectProperty):
        domain = [Musician]
        range = [MusicalWork]

    class released(ObjectProperty):
        domain = [Musician]
        range = [StudioAlbum]

    class releaseDate(ObjectProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [TimeInterval]

    class albumSequence(DataProperty, FunctionalProperty):
        domain = [StudioAlbum]
        range = [int]

    class rootedInStyle(ObjectProperty):
        domain = [MusicalWork]
        range = [MusicalStyle]

    class includesStyleElement(ObjectProperty):
        domain = [MusicalWork]
        range = [MusicalStyle]

    class describedAsStyle(ObjectProperty):
        domain = [MusicalWork]
        range = [MusicalStyle]

    class describedByPublication(ObjectProperty):
        domain = [Voice]
        range = [Publication]

    class nationality(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [str]

    class pitchforkDescription(DataProperty, FunctionalProperty):
        domain = [Voice]
        range = [str]

    class bostonGlobeDescription(DataProperty, FunctionalProperty):
        domain = [Voice]
        range = [str]

    class criticalAcclaimNote(DataProperty, FunctionalProperty):
        domain = [Voice]
        range = [str]

    class classificationNote(DataProperty, FunctionalProperty):
        domain = [MusicalWork]
        range = [str]

    April51981 = TimeInterval("April51981")
    April51981.label = "April 5 , 1981"

    Year2000 = TimeInterval("Year2000")
    Year2000.label = "2000"

    May2016 = TimeInterval("May2016")
    May2016.label = "May 2016"

    MarissaNadler = SingerSongwriter("MarissaNadler")
    MarissaNadler.label = "Marissa Nadler"
    MarissaNadler.is_a.append(Musician)
    MarissaNadler.is_a.append(FineArtist)
    MarissaNadler.nationality = "American"
    MarissaNadler.birthDate = April51981
    MarissaNadler.activeSince = Year2000

    Boston = City("Boston")
    Boston.label = "Boston"

    Massachusetts = State("Massachusetts")
    Massachusetts.label = "Massachusetts"
    Boston.locatedIn = Massachusetts
    MarissaNadler.basedIn = Boston

    SacredBonesRecords = RecordLabel("SacredBonesRecords")
    SacredBonesRecords.label = "Sacred Bones Records"

    BellaUnion = RecordLabel("BellaUnion")
    BellaUnion.label = "Bella Union"

    MarissaNadler.signedTo.append(SacredBonesRecords)
    MarissaNadler.signedTo.append(BellaUnion)

    MarissaNadlerWork = MusicalWork("MarissaNadlerWork")
    MarissaNadlerWork.label = "her work"
    MarissaNadlerWork.classificationNote = "defies simple classification"

    OldSchoolCountry = MusicalStyle("OldSchoolCountry")
    OldSchoolCountry.label = "old - school country"

    Folk = MusicalStyle("Folk")
    Folk.label = "folk"

    Experimental = MusicalStyle("Experimental")
    Experimental.label = "experimental"

    BlackMetal = MusicalStyle("BlackMetal")
    BlackMetal.label = "black metal"

    DreamFolk = MusicalStyle("DreamFolk")
    DreamFolk.label = "dream folk"

    MarissaNadlerWork.rootedInStyle.append(OldSchoolCountry)
    MarissaNadlerWork.rootedInStyle.append(Folk)
    MarissaNadlerWork.includesStyleElement.append(Experimental)
    MarissaNadlerWork.includesStyleElement.append(BlackMetal)
    MarissaNadlerWork.describedAsStyle.append(DreamFolk)
    MarissaNadler.hasWork.append(MarissaNadlerWork)

    Pitchfork = Publication("Pitchfork")
    Pitchfork.label = "Pitchfork"

    TheBostonGlobe = Publication("TheBostonGlobe")
    TheBostonGlobe.label = "The Boston Globe"

    MarissaNadlerVoice = Voice("MarissaNadlerVoice")
    MarissaNadlerVoice.label = "her voice"
    MarissaNadlerVoice.directQualityOf = MarissaNadler
    MarissaNadlerVoice.describedByPublication.append(Pitchfork)
    MarissaNadlerVoice.describedByPublication.append(TheBostonGlobe)
    MarissaNadlerVoice.pitchforkDescription = (
        'one " you would follow straight into Hades " , and also '
        '" textured and angelic , with just a hint of pain captured within her iridescent falsetto "'
    )
    MarissaNadlerVoice.bostonGlobeDescription = (
        '" She has a voice that , in mythological times , could have lured men to their deaths at sea , '
        'an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke "'
    )
    MarissaNadlerVoice.criticalAcclaimNote = "received acclaim for her vocals"

    MarissaNadlerVocalRange = VocalRange("MarissaNadlerVocalRange")
    MarissaNadlerVocalRange.label = "mezzo - soprano"
    MarissaNadlerVocalRange.directQualityOf = MarissaNadler

    Hades = MythologicalPlace("Hades")
    Hades.label = "Hades"

    Strangers = FullLengthStudioAlbum("Strangers")
    Strangers.label = "Strangers"
    Strangers.albumSequence = 7
    Strangers.releaseDate = May2016
    MarissaNadler.released.append(Strangers)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
