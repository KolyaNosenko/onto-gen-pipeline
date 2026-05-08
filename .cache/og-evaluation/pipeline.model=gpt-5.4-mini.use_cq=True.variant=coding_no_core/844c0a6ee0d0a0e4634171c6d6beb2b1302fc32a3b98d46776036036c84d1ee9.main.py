"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

1. Who is Dr. Nicholas Rush?
2. In which television series does Dr. Nicholas Rush appear?
3. What type of television series is Stargate Universe?
4. What nationality is the production company description of Stargate Universe?
5. Who portrays Dr. Nicholas Rush?
6. What is Dr. Nicholas Rush’s occupation or characterization?
7. What is Dr. Nicholas Rush’s life work?
8. What does Dr. Nicholas Rush’s work involve uncovering?
9. Which Stargate feature is associated with Dr. Nicholas Rush’s research?
10. What event ultimately leads Dr. Nicholas Rush and Icarus Base personnel through the Stargate?
11. Where do Dr. Nicholas Rush and the Icarus Base personnel travel through the Stargate?
12. What must Dr. Nicholas Rush and the others do to survive in the far-away galaxy?
13. In which episode did Dr. Nicholas Rush first appear?
14. When was Dr. Nicholas Rush’s first appearance broadcast?
15. What is the name of the spaceship Destiny?
16. What organization or base are personnel from when they travel with Dr. Nicholas Rush?
17. What interest did Robert Carlyle initially have in the character of Rush?
18. Why did Robert Carlyle find the character of Rush interesting to portray?
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

    class Actor(Person):
        pass

    class Scientist(Person):
        pass

    class FictionalCharacter(Thing):
        pass

    class MachiavellianScientist(FictionalCharacter, Scientist):
        pass

    class TelevisionSeries(Thing):
        pass

    class SerialDrama(TelevisionSeries):
        pass

    class MilitaryScienceFictionSerialDrama(SerialDrama):
        pass

    class Organization(Thing):
        pass

    class Company(Organization):
        pass

    class Network(Organization):
        pass

    class Base(Thing):
        pass

    class Spacecraft(Thing):
        pass

    class StargateArtifact(Thing):
        pass

    class Chevron(Thing):
        pass

    class Episode(Thing):
        pass

    class Country(Thing):
        pass

    class Planet(Thing):
        pass

    class Galaxy(Thing):
        pass

    class ExplorationTeam(Thing):
        pass

    class Personnel(Person):
        pass

    class Investigation(Thing):
        pass

    class Journey(Thing):
        pass

    class SurvivalFight(Thing):
        pass

    class appearsIn(ObjectProperty):
        domain = [FictionalCharacter]
        range = [TelevisionSeries]

    class portrayedBy(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [Actor]

    class interestedIn(ObjectProperty, FunctionalProperty):
        domain = [Actor]
        range = [FictionalCharacter]

    class skepticalTowards(ObjectProperty, FunctionalProperty):
        domain = [Actor]
        range = [TelevisionSeries]

    class interestReason(DataProperty, FunctionalProperty):
        domain = [Actor]
        range = [str]

    class hasLifeWork(ObjectProperty, FunctionalProperty):
        domain = [Scientist]
        range = [Investigation]

    class investigates(ObjectProperty, FunctionalProperty):
        domain = [Investigation]
        range = [Chevron]

    class ultimatelyLeadsTo(ObjectProperty, FunctionalProperty):
        domain = [Investigation]
        range = [Journey]

    class partOfStargate(ObjectProperty, FunctionalProperty):
        domain = [Chevron]
        range = [StargateArtifact]

    class firstAppearsIn(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [Episode]

    class firstBroadcastInCountry(ObjectProperty):
        domain = [Episode]
        range = [Country]

    class firstBroadcastYear(DataProperty, FunctionalProperty):
        domain = [Episode]
        range = [int]

    class producedBy(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Company]

    class airedOn(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Network]

    class hasNationalityDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]

    class about(ObjectProperty):
        domain = [TelevisionSeries]
        range = [ExplorationTeam]

    class evacuatedTo(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [Spacecraft]

    class unableToReturnTo(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [Planet]

    class travelsThrough(ObjectProperty, FunctionalProperty):
        domain = [Journey]
        range = [StargateArtifact]

    class destination(ObjectProperty, FunctionalProperty):
        domain = [Journey]
        range = [Galaxy]

    class involvesPerson(ObjectProperty):
        domain = [Journey]
        range = [Person]

    class requires(ObjectProperty, FunctionalProperty):
        domain = [Journey]
        range = [SurvivalFight]

    class fromBase(ObjectProperty, FunctionalProperty):
        domain = [Personnel]
        range = [Base]

    DrNicholasRush = MachiavellianScientist("DrNicholasRush")
    DrNicholasRush.label = ["Dr. Nicholas Rush", "Rush"]

    StargateUniverse = MilitaryScienceFictionSerialDrama("StargateUniverse")
    StargateUniverse.label = "Stargate Universe"

    RobertCarlyle = Actor("RobertCarlyle")
    RobertCarlyle.label = ["Robert Carlyle", "Carlyle"]

    MetroGoldwynMayer = Company("MetroGoldwynMayer")
    MetroGoldwynMayer.label = "Metro-Goldwyn-Mayer"

    Syfy = Network("Syfy")
    Syfy.label = "Syfy"

    Destiny = Spacecraft("Destiny")
    Destiny.label = "Destiny"

    Stargate = StargateArtifact("Stargate")
    Stargate.label = "Stargate"

    IcarusBase = Base("IcarusBase")
    IcarusBase.label = "Icarus Base"

    Air = Episode("Air")
    Air.label = "Air"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    Canada = Country("Canada")
    Canada.label = "Canada"

    Earth = Planet("Earth")
    Earth.label = "Earth"

    Ancient = Thing("Ancient")
    Ancient.label = "Ancient"

    NinthChevron = Chevron("NinthChevron")
    NinthChevron.label = "ninth chevron of the Stargate"

    FarAwayGalaxy = Galaxy("FarAwayGalaxy")
    FarAwayGalaxy.label = "far-away galaxy"

    explorationTeam = ExplorationTeam()
    explorationTeam.label = "present-day, multinational exploration team"

    rushInvestigation = Investigation()
    rushInvestigation.label = "uncovering the mysteries behind the ninth chevron of the Stargate"

    personnelFromIcarusBase = Personnel()
    personnelFromIcarusBase.label = "personnel from the Icarus Base"

    survivalFight = SurvivalFight()
    survivalFight.label = "fight for their own survival"

    survivalJourney = Journey()

    StargateUniverse.hasNationalityDescription = "Canadian-American"
    StargateUniverse.producedBy = MetroGoldwynMayer
    StargateUniverse.airedOn = Syfy
    StargateUniverse.about = [explorationTeam]

    explorationTeam.evacuatedTo = Destiny
    explorationTeam.unableToReturnTo = Earth

    DrNicholasRush.appearsIn = [StargateUniverse]
    DrNicholasRush.portrayedBy = RobertCarlyle
    DrNicholasRush.hasLifeWork = rushInvestigation
    DrNicholasRush.firstAppearsIn = Air

    RobertCarlyle.interestedIn = DrNicholasRush
    RobertCarlyle.interestReason = 'he felt Rush was a "very interesting" character to portray'
    RobertCarlyle.skepticalTowards = StargateUniverse

    rushInvestigation.investigates = NinthChevron
    rushInvestigation.ultimatelyLeadsTo = survivalJourney
    NinthChevron.partOfStargate = Stargate

    Air.firstBroadcastInCountry = [UnitedStates, Canada]
    Air.firstBroadcastYear = 2009

    personnelFromIcarusBase.fromBase = IcarusBase

    survivalJourney.involvesPerson = [DrNicholasRush, personnelFromIcarusBase]
    survivalJourney.travelsThrough = Stargate
    survivalJourney.destination = FarAwayGalaxy
    survivalJourney.requires = survivalFight


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
