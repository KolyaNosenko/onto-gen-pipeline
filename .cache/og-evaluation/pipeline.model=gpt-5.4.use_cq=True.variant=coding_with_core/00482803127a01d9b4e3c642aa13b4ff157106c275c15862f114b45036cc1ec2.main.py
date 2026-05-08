"""
=== TASK INPUT ===
Source text:
Marissa Nadler ( born April 5 , 1981 ) is an American musician and fine artist based in Boston , Massachusetts . Active since 2000 , she is currently signed to Sacred Bones Records and Bella Union , and released her seventh full - length studio album , Strangers , in May 2016 . As a singer - songwriter , her music defies simple classification . Her work " is rooted in old - school country and folk but brings in elements of experimental and black metal " . Sometimes the term " dream folk " has been invoked to describe her work . Singing in a mezzo - soprano , Nadler has received acclaim for her vocals . Her voice was described by Pitchfork as one " you would follow straight into Hades " , and also " textured and angelic , with just a hint of pain captured within her iridescent falsetto " . The Boston Globe said , " She has a voice that , in mythological times , could have lured men to their deaths at sea , an intoxicating soprano drenched in gauzy reverb that hits bell - clear heights , lingers , and tapers off like rings of smoke " .

What is Marissa Nadler’s date of birth?
What nationality is Marissa Nadler?
What professions or artistic roles does Marissa Nadler have?
Where is Marissa Nadler based?
Since what year has Marissa Nadler been active?
Which record labels is Marissa Nadler currently signed to?
What is the title of Marissa Nadler’s seventh full-length studio album?
When was the album Strangers released?
How many full-length studio albums had Marissa Nadler released by May 2016?
How is Marissa Nadler described as a musician in terms of genre classification?
What musical genres influence Marissa Nadler’s work?
Is Marissa Nadler’s music associated with the term “dream folk”?
What vocal range or voice type does Marissa Nadler sing in?
How has Marissa Nadler’s voice been described by Pitchfork?
How has Marissa Nadler’s voice been described by The Boston Globe?
What elements of country, folk, experimental, and black metal are said to appear in Marissa Nadler’s music?
Has Marissa Nadler received acclaim for her vocals?
Which publications have provided descriptions or reviews of Marissa Nadler’s voice?
What artistic disciplines besides music is Marissa Nadler associated with?
What album had Marissa Nadler released by May 2016 while signed to Sacred Bones Records and Bella Union?
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
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Artist(AgentivePhysicalObject):
        pass


    class Musician(Artist):
        pass


    class SingerSongwriter(Musician):
        pass


    class FineArtist(Artist):
        pass


    class Place(SpaceRegion):
        pass


    class City(Place):
        pass


    class State(Place):
        pass


    class MythologicalPlace(Place):
        pass


    class Organization(Society):
        pass


    class RecordLabel(Organization):
        pass


    class Publication(Organization):
        pass


    class CreativeWork(NonAgentiveSocialObject):
        pass


    class MusicAlbum(CreativeWork):
        pass


    class FullLengthStudioAlbum(MusicAlbum):
        pass


    class Genre(NonAgentiveSocialObject):
        pass


    class Nationality(NonAgentiveSocialObject):
        pass


    class VocalRange(NonAgentiveSocialObject):
        pass


    class VoiceDescription(NonAgentiveSocialObject):
        pass


    class dateOfBirth(ObjectProperty, FunctionalProperty):
        domain = [Artist]
        range = [TimeInterval]


    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Artist]
        range = [Nationality]


    class basedIn(ObjectProperty, FunctionalProperty):
        domain = [Artist]
        range = [Place]


    class activeSince(ObjectProperty, FunctionalProperty):
        domain = [Artist]
        range = [TimeInterval]


    class currentlySignedTo(ObjectProperty):
        domain = [Artist]
        range = [RecordLabel]


    class releasedAlbum(ObjectProperty):
        domain = [Artist]
        range = [MusicAlbum]


    class releasedBy(ObjectProperty, FunctionalProperty):
        domain = [MusicAlbum]
        range = [Artist]


    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [MusicAlbum]
        range = [TimeInterval]


    class rootedInGenre(ObjectProperty):
        domain = [Musician]
        range = [Genre]


    class incorporatesElementsOfGenre(ObjectProperty):
        domain = [Musician]
        range = [Genre]


    class associatedWithGenreTerm(ObjectProperty):
        domain = [Musician]
        range = [Genre]


    class singsIn(ObjectProperty, FunctionalProperty):
        domain = [Artist]
        range = [VocalRange]


    class voiceDescribedByPublication(ObjectProperty):
        domain = [Artist]
        range = [Publication]


    class sourcePublication(ObjectProperty, FunctionalProperty):
        domain = [VoiceDescription]
        range = [Publication]


    class describesVoiceOf(ObjectProperty, FunctionalProperty):
        domain = [VoiceDescription]
        range = [Artist]


    class mentionsPlace(ObjectProperty):
        domain = [VoiceDescription]
        range = [Place]


    class genreClassificationDescription(DataProperty, FunctionalProperty):
        domain = [Musician]
        range = [str]


    class albumSequenceNumber(DataProperty, FunctionalProperty):
        domain = [MusicAlbum]
        range = [int]


    class receivedAcclaimForVocals(DataProperty, FunctionalProperty):
        domain = [Artist]
        range = [bool]


    class quoteText(DataProperty, FunctionalProperty):
        domain = [VoiceDescription]
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

    April51981 = TimeInterval("April51981")
    April51981.label = "April 5, 1981"

    Year2000 = TimeInterval("Year2000")
    Year2000.label = "2000"

    May2016 = TimeInterval("May2016")
    May2016.label = "May 2016"

    SacredBonesRecords = RecordLabel("SacredBonesRecords")
    SacredBonesRecords.label = "Sacred Bones Records"

    BellaUnion = RecordLabel("BellaUnion")
    BellaUnion.label = "Bella Union"

    Pitchfork = Publication("Pitchfork")
    Pitchfork.label = "Pitchfork"

    TheBostonGlobe = Publication("TheBostonGlobe")
    TheBostonGlobe.label = "The Boston Globe"

    Strangers = FullLengthStudioAlbum("Strangers")
    Strangers.label = "Strangers"

    OldSchoolCountry = Genre("OldSchoolCountry")
    OldSchoolCountry.label = "old-school country"

    Folk = Genre("Folk")
    Folk.label = "folk"

    Experimental = Genre("Experimental")
    Experimental.label = "experimental"

    BlackMetal = Genre("BlackMetal")
    BlackMetal.label = "black metal"

    DreamFolk = Genre("DreamFolk")
    DreamFolk.label = "dream folk"

    MezzoSoprano = VocalRange("MezzoSoprano")
    MezzoSoprano.label = "mezzo-soprano"

    PitchforkStraightIntoHades = VoiceDescription("PitchforkStraightIntoHades")
    PitchforkStraightIntoHades.label = "you would follow straight into Hades"
    PitchforkStraightIntoHades.quoteText = "you would follow straight into Hades"
    PitchforkStraightIntoHades.sourcePublication = Pitchfork
    PitchforkStraightIntoHades.describesVoiceOf = MarissaNadler
    PitchforkStraightIntoHades.mentionsPlace.append(Hades)

    PitchforkTexturedAngelic = VoiceDescription("PitchforkTexturedAngelic")
    PitchforkTexturedAngelic.label = "textured and angelic, with just a hint of pain captured within her iridescent falsetto"
    PitchforkTexturedAngelic.quoteText = "textured and angelic, with just a hint of pain captured within her iridescent falsetto"
    PitchforkTexturedAngelic.sourcePublication = Pitchfork
    PitchforkTexturedAngelic.describesVoiceOf = MarissaNadler

    BostonGlobeVoiceDescription = VoiceDescription("BostonGlobeVoiceDescription")
    BostonGlobeVoiceDescription.label = "She has a voice that, in mythological times, could have lured men to their deaths at sea, an intoxicating soprano drenched in gauzy reverb that hits bell-clear heights, lingers, and tapers off like rings of smoke"
    BostonGlobeVoiceDescription.quoteText = "She has a voice that, in mythological times, could have lured men to their deaths at sea, an intoxicating soprano drenched in gauzy reverb that hits bell-clear heights, lingers, and tapers off like rings of smoke"
    BostonGlobeVoiceDescription.sourcePublication = TheBostonGlobe
    BostonGlobeVoiceDescription.describesVoiceOf = MarissaNadler

    Boston.partOf.append(Massachusetts)

    MarissaNadler.dateOfBirth = April51981
    MarissaNadler.hasNationality = American
    MarissaNadler.basedIn = Boston
    MarissaNadler.activeSince = Year2000
    MarissaNadler.currentlySignedTo.append(SacredBonesRecords)
    MarissaNadler.currentlySignedTo.append(BellaUnion)
    MarissaNadler.releasedAlbum.append(Strangers)
    MarissaNadler.rootedInGenre.append(OldSchoolCountry)
    MarissaNadler.rootedInGenre.append(Folk)
    MarissaNadler.incorporatesElementsOfGenre.append(Experimental)
    MarissaNadler.incorporatesElementsOfGenre.append(BlackMetal)
    MarissaNadler.associatedWithGenreTerm.append(DreamFolk)
    MarissaNadler.singsIn = MezzoSoprano
    MarissaNadler.voiceDescribedByPublication.append(Pitchfork)
    MarissaNadler.voiceDescribedByPublication.append(TheBostonGlobe)
    MarissaNadler.genreClassificationDescription = "defies simple classification"
    MarissaNadler.receivedAcclaimForVocals = True

    Strangers.releasedBy = MarissaNadler
    Strangers.releasedIn = May2016
    Strangers.albumSequenceNumber = 7


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
