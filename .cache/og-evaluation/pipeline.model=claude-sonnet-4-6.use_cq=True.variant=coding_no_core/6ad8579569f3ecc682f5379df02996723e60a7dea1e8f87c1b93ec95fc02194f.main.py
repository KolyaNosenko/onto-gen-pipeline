"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

1. Who portrays Dr. Nicholas Rush in Stargate Universe?
2. What nationality is the actor who portrays Dr. Nicholas Rush?
3. What television series does Dr. Nicholas Rush appear in?
4. Which networks produced the television series Stargate Universe?
5. What genre is the television series Stargate Universe?
6. What is the name of the Ancient spaceship featured in Stargate Universe?
7. What is the life's work of Dr. Nicholas Rush?
8. What is the name of the base from which personnel travel through the Stargate?
9. In which episode did Dr. Nicholas Rush make his first appearance?
10. When was the pilot episode of Stargate Universe first broadcast?
11. In which countries was the pilot episode first broadcast?
12. What type of scientist is Dr. Nicholas Rush described as?
13. What is the ninth chevron associated with in the story?
14. What is the premise of the television series Stargate Universe?
15. What was Robert Carlyle's initial attitude towards Stargate Universe before joining the show?
16. What country of origin is associated with the production of Stargate Universe?
17. What challenges do the characters face after traveling through the Stargate in Stargate Universe?
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
    # ── CLASSES ────────────────────────────────────────────────────────────────

    # Real people
    class Person(Thing): pass

    class Actor(Person): pass

    # Fictional characters (people in the show)
    class FictionalCharacter(Thing): pass

    class FictionalScientist(FictionalCharacter): pass

    class MachiavellianScientist(FictionalScientist): pass

    # Media
    class TelevisionSeries(Thing): pass

    class Genre(Thing): pass

    class Episode(Thing): pass

    # Organisations involved in production / broadcast
    class MediaOrganisation(Thing): pass

    class ProductionCompany(MediaOrganisation): pass

    class BroadcastNetwork(MediaOrganisation): pass

    # Locations
    class Location(Thing): pass

    class Country(Location): pass

    class MilitaryBase(Location): pass

    # Other artefacts
    class Spaceship(Thing): pass

    class StargateDevice(Thing): pass

    class Nationality(Thing): pass

    # ── OBJECT PROPERTIES ──────────────────────────────────────────────────────

    class portrayedBy(ObjectProperty, FunctionalProperty):
        """Links a fictional character to the real actor who portrays them."""
        domain = [FictionalCharacter]
        range  = [Actor]

    class appearsIn(ObjectProperty):
        """Links a fictional character to the television series they appear in."""
        domain = [FictionalCharacter]
        range  = [TelevisionSeries]

    class producedBy(ObjectProperty):
        """Links a television series to the media organisations that produced it."""
        domain = [TelevisionSeries]
        range  = [MediaOrganisation]

    class hasGenre(ObjectProperty):
        """Links a television series to its genre."""
        domain = [TelevisionSeries]
        range  = [Genre]

    class featuresSpaceship(ObjectProperty):
        """Links a television series to a spaceship featured in it."""
        domain = [TelevisionSeries]
        range  = [Spaceship]

    class hasCountryOfOrigin(ObjectProperty):
        """Links a television series to the country associated with its production."""
        domain = [TelevisionSeries]
        range  = [Country]

    class hasNationality(ObjectProperty):
        """Links a person to their nationality."""
        domain = [Person]
        range  = [Nationality]

    class hasFirstAppearance(ObjectProperty, FunctionalProperty):
        """Links a fictional character to the episode of their first appearance."""
        domain = [FictionalCharacter]
        range  = [Episode]

    class firstBroadcastIn(ObjectProperty):
        """Links an episode to the countries where it was first broadcast."""
        domain = [Episode]
        range  = [Country]

    class departedFrom(ObjectProperty):
        """Links a fictional character to the military base they departed from."""
        domain = [FictionalCharacter]
        range  = [MilitaryBase]

    class traveledThroughStargate(ObjectProperty):
        """Links a fictional character to the Stargate device they traveled through."""
        domain = [FictionalCharacter]
        range  = [StargateDevice]

    class associatesLifeWorkWith(ObjectProperty, FunctionalProperty):
        """Links a fictional scientist to the device their life's work concerns."""
        domain = [FictionalScientist]
        range  = [StargateDevice]

    # ── DATA PROPERTIES ────────────────────────────────────────────────────────

    class lifeWork(DataProperty, FunctionalProperty):
        """Textual description of the life's work of a fictional scientist."""
        domain = [FictionalScientist]
        range  = [str]

    class broadcastYear(DataProperty, FunctionalProperty):
        """Year an episode was first broadcast."""
        domain = [Episode]
        range  = [int]

    class hasPremise(DataProperty, FunctionalProperty):
        """Textual description of a television series' premise."""
        domain = [TelevisionSeries]
        range  = [str]

    class initialAttitude(DataProperty, FunctionalProperty):
        """Describes an actor's initial attitude towards a show before joining."""
        domain = [Actor]
        range  = [str]

    class characterDescription(DataProperty, FunctionalProperty):
        """A brief description of a fictional character as given in the source."""
        domain = [FictionalCharacter]
        range  = [str]

    # ── INDIVIDUALS ────────────────────────────────────────────────────────────

    # Fictional character: Dr. Nicholas Rush
    DrNicholasRush = MachiavellianScientist("DrNicholasRush")
    DrNicholasRush.label = "Dr. Nicholas Rush"

    # Real person: Robert Carlyle
    RobertCarlyle = Actor("RobertCarlyle")
    RobertCarlyle.label = "Robert Carlyle"

    # Nationalities
    ScottishNat = Nationality("ScottishNat")
    ScottishNat.label = "Scottish"

    # Countries
    CanadaInst = Country("CanadaInst")
    CanadaInst.label = "Canada"

    UnitedStatesInst = Country("UnitedStatesInst")
    UnitedStatesInst.label = "United States"

    # Media organisations
    MetroGoldwynMayerInst = ProductionCompany("MetroGoldwynMayerInst")
    MetroGoldwynMayerInst.label = "Metro-Goldwyn-Mayer"

    SyfyInst = BroadcastNetwork("SyfyInst")
    SyfyInst.label = "Syfy"

    # Television series
    StargateUniverseInst = TelevisionSeries("StargateUniverseInst")
    StargateUniverseInst.label = "Stargate Universe"

    # Genres
    MilitaryScienceFictionGenre = Genre("MilitaryScienceFictionGenre")
    MilitaryScienceFictionGenre.label = "military science fiction"

    SerialDramaGenre = Genre("SerialDramaGenre")
    SerialDramaGenre.label = "serial drama"

    # Spaceship
    DestinyInst = Spaceship("DestinyInst")
    DestinyInst.label = "Destiny"

    # Military base
    IcarusBaseInst = MilitaryBase("IcarusBaseInst")
    IcarusBaseInst.label = "Icarus Base"

    # Stargate device (the portal device, not the series)
    StargateDeviceInst = StargateDevice("StargateDeviceInst")
    StargateDeviceInst.label = "Stargate"

    # Pilot episode
    AirEpisodeInst = Episode("AirEpisodeInst")
    AirEpisodeInst.label = "Air"

    # ── PROPERTY ASSERTIONS ────────────────────────────────────────────────────

    # Dr. Nicholas Rush
    DrNicholasRush.portrayedBy = RobertCarlyle
    DrNicholasRush.appearsIn = [StargateUniverseInst]
    DrNicholasRush.lifeWork = "uncovering the mysteries behind the ninth chevron of the Stargate"
    DrNicholasRush.associatesLifeWorkWith = StargateDeviceInst
    DrNicholasRush.departedFrom = [IcarusBaseInst]
    DrNicholasRush.traveledThroughStargate = [StargateDeviceInst]
    DrNicholasRush.hasFirstAppearance = AirEpisodeInst
    DrNicholasRush.characterDescription = "machiavellian scientist"

    # Robert Carlyle
    RobertCarlyle.hasNationality = [ScottishNat]
    RobertCarlyle.initialAttitude = "skeptical"

    # Stargate Universe series
    StargateUniverseInst.producedBy = [MetroGoldwynMayerInst, SyfyInst]
    StargateUniverseInst.hasGenre = [MilitaryScienceFictionGenre, SerialDramaGenre]
    StargateUniverseInst.featuresSpaceship = [DestinyInst]
    StargateUniverseInst.hasCountryOfOrigin = [CanadaInst, UnitedStatesInst]
    StargateUniverseInst.hasPremise = (
        "adventures of a present-day, multinational exploration team unable to "
        "return to Earth after an evacuation to the Ancient spaceship Destiny, "
        "which is traveling in a distant corner of the universe"
    )

    # Air episode
    AirEpisodeInst.broadcastYear = 2009
    AirEpisodeInst.firstBroadcastIn = [UnitedStatesInst, CanadaInst]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
