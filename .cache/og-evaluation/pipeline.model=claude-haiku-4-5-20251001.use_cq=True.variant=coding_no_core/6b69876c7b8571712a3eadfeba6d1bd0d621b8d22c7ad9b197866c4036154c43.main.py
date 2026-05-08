"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

1. Who portrays the character Dr. Nicholas Rush in Stargate Universe?
2. What is the nationality of the actor who plays Dr. Nicholas Rush?
3. In which television series does Dr. Nicholas Rush appear?
4. What are the production companies behind Stargate Universe?
5. What is the genre classification of Stargate Universe?
6. What is Dr. Nicholas Rush's primary scientific focus or life's work?
7. In which episode does Dr. Nicholas Rush make his first appearance?
8. When was the pilot episode of Stargate Universe first broadcast?
9. In which countries was the pilot episode broadcast?
10. What event forces the exploration team to evacuate to the Ancient spaceship Destiny?
11. What is the purpose of the Stargate that Dr. Nicholas Rush investigates?
12. From which military base did the exploration team evacuate?
13. What type of spaceship is the Destiny?
14. How many chevrons of the Stargate does Dr. Nicholas Rush study?
15. Where is the Ancient spaceship Destiny traveling?
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
    # ============================================
    # Entity Classes
    # ============================================
    
    class Person(Thing): pass
    class Actor(Person): pass
    class FictionalCharacter(Thing): pass
    
    class TelevisionSeries(Thing): pass
    class TelevisionEpisode(Thing): pass
    class PilotEpisode(TelevisionEpisode): pass
    
    class Country(Thing): pass
    class Location(Thing): pass
    class Galaxy(Location): pass
    
    class Spaceship(Thing): pass
    class AncientSpaceship(Spaceship): pass
    
    class MilitaryBase(Thing): pass
    class ProductionCompany(Thing): pass
    class ExplorationTeam(Thing): pass
    
    class GenreClassification(Thing): pass
    class StargateMechanism(Thing): pass
    class Chevron(Thing): pass
    
    # ============================================
    # Object Properties
    # ============================================
    
    class portrays(ObjectProperty):
        domain = [Actor]
        range = [FictionalCharacter]
    
    class appearsIn(ObjectProperty):
        domain = [FictionalCharacter]
        range = [TelevisionSeries]
    
    class hasNationality(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Country]
    
    class producedBy(ObjectProperty):
        domain = [TelevisionSeries]
        range = [ProductionCompany]
    
    class hasGenre(ObjectProperty):
        domain = [TelevisionSeries]
        range = [GenreClassification]
    
    class investigates(ObjectProperty):
        domain = [FictionalCharacter]
        range = [Thing]
    
    class madeFirstAppearanceIn(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [TelevisionEpisode]
    
    class isPartOfSeries(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]
    
    class broadcastIn(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Country]
    
    class usesSpaceship(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [Spaceship]
    
    class travels(ObjectProperty, FunctionalProperty):
        domain = [Spaceship]
        range = [Location]
    
    class evacuatedFrom(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [MilitaryBase]
    
    class hasChevron(ObjectProperty):
        domain = [StargateMechanism]
        range = [Chevron]
    
    # ============================================
    # Data Properties
    # ============================================
    
    class broadcastYear(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]
    
    # ============================================
    # Instances - Countries
    # ============================================
    
    scotland = Country("Scotland")
    scotland.label = "Scotland"
    
    usa = Country("UnitedStates")
    usa.label = "United States"
    
    canada = Country("Canada")
    canada.label = "Canada"
    
    earth_location = Location("Earth")
    earth_location.label = "Earth"
    
    # ============================================
    # Instances - People
    # ============================================
    
    robert_carlyle = Actor("RobertCarlyle")
    robert_carlyle.label = "Robert Carlyle"
    robert_carlyle.hasNationality = scotland
    
    # ============================================
    # Instances - Fictional Characters
    # ============================================
    
    nicholas_rush = FictionalCharacter("NicholasRush")
    nicholas_rush.label = "Dr. Nicholas Rush"
    
    # ============================================
    # Instances - Production Companies
    # ============================================
    
    mgm = ProductionCompany("MetroGoldwynMayer")
    mgm.label = "Metro - Goldwyn - Mayer"
    
    syfy = ProductionCompany("Syfy")
    syfy.label = "Syfy"
    
    # ============================================
    # Instances - Genre
    # ============================================
    
    military_scifi = GenreClassification("MilitarySciFiSerialDrama")
    military_scifi.label = "military science fiction serial drama"
    
    # ============================================
    # Instances - Television Series
    # ============================================
    
    stargate_universe = TelevisionSeries("StargateUniverse")
    stargate_universe.label = "Stargate Universe"
    stargate_universe.producedBy = [mgm, syfy]
    stargate_universe.hasGenre = [military_scifi]
    
    # ============================================
    # Instances - Stargate Mechanism
    # ============================================
    
    stargate = StargateMechanism("Stargate")
    stargate.label = "Stargate"
    
    ninth_chevron = Chevron("NinthChevron")
    ninth_chevron.label = "ninth chevron"
    
    stargate.hasChevron = [ninth_chevron]
    
    # ============================================
    # Instances - Episodes
    # ============================================
    
    air_episode = PilotEpisode("Air")
    air_episode.label = "Air"
    air_episode.broadcastYear = 2009
    air_episode.broadcastIn = [usa, canada]
    air_episode.isPartOfSeries = stargate_universe
    
    # ============================================
    # Instances - Locations
    # ============================================
    
    distant_universe = Location("DistantCornerOfUniverse")
    distant_universe.label = "distant corner of the universe"
    
    far_away_galaxy = Galaxy("FarAwayGalaxy")
    far_away_galaxy.label = "far-away galaxy"
    
    # ============================================
    # Instances - Spaceship
    # ============================================
    
    destiny = AncientSpaceship("Destiny")
    destiny.label = "Destiny"
    destiny.travels = distant_universe
    
    # ============================================
    # Instances - Military Base
    # ============================================
    
    icarus_base = MilitaryBase("IcarusBase")
    icarus_base.label = "Icarus Base"
    
    # ============================================
    # Instances - Exploration Team
    # ============================================
    
    exploration_team = ExplorationTeam("DestinyMission")
    exploration_team.label = "exploration team"
    exploration_team.usesSpaceship = destiny
    exploration_team.evacuatedFrom = icarus_base
    
    # ============================================
    # Link Character to Actor and Series
    # ============================================
    
    robert_carlyle.portrays = [nicholas_rush]
    nicholas_rush.appearsIn = [stargate_universe]
    nicholas_rush.investigates = [ninth_chevron]
    nicholas_rush.madeFirstAppearanceIn = air_episode


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
