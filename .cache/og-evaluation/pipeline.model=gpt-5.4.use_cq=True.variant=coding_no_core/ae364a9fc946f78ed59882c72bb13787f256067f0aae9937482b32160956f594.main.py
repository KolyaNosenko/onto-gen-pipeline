"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

What is Dr. Nicholas Rush?
In which television series does Dr. Nicholas Rush appear?
Is Dr. Nicholas Rush a fictional character?
What genre is Stargate Universe?
What is the premise of Stargate Universe?
Why is the exploration team in Stargate Universe unable to return to Earth?
To which spaceship does the team evacuate?
What is the name of the Ancient spaceship in Stargate Universe?
Where is the spaceship Destiny traveling?
What is Dr. Nicholas Rush's role in the series?
Who portrays Dr. Nicholas Rush?
What is the nationality of the actor who portrays Dr. Nicholas Rush?
Why did Robert Carlyle become interested in portraying Dr. Nicholas Rush?
Was Robert Carlyle initially skeptical about the show?
How is Dr. Nicholas Rush's personality characterized?
What is Dr. Nicholas Rush's life's work?
What mystery is Dr. Nicholas Rush trying to uncover?
What does uncovering the mystery of the ninth chevron lead to?
From where do Dr. Nicholas Rush and the Icarus Base personnel travel through the Stargate?
To where do Dr. Nicholas Rush and the Icarus Base personnel travel through the Stargate?
What challenge do Dr. Nicholas Rush and the Icarus Base personnel face in the far-away galaxy?
In which episode did Dr. Nicholas Rush first appear?
What is the title of the pilot episode featuring Dr. Nicholas Rush?
When was Dr. Nicholas Rush's first appearance broadcast?
In which countries was the pilot episode "Air" first broadcast?
Is Stargate Universe a Canadian-American television series?
Which companies are associated with the production of Stargate Universe?
Is Stargate Universe part of the Stargate franchise?
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

    class FictionalCharacter(Person):
        pass

    class Actor(Person):
        pass

    class Scientist(Person):
        pass

    class FictionalScientist(FictionalCharacter, Scientist):
        pass

    class MachiavellianScientist(FictionalScientist):
        pass

    class Organization(Thing):
        pass

    class MediaOrganization(Organization):
        pass

    class ProductionCompany(MediaOrganization):
        pass

    class TelevisionNetwork(MediaOrganization):
        pass

    class TelevisionSeries(Thing):
        pass

    class CanadianAmericanTelevisionSeries(TelevisionSeries):
        pass

    class MilitaryScienceFictionSerialDrama(TelevisionSeries):
        pass

    class ExplorationTeam(Thing):
        pass

    class PresentDayMultinationalExplorationTeam(ExplorationTeam):
        pass

    class PersonnelGroup(Thing):
        pass

    class Episode(Thing):
        pass

    class PilotEpisode(Episode):
        pass

    class Country(Thing):
        pass

    class Year(Thing):
        pass

    class Planet(Thing):
        pass

    class Galaxy(Thing):
        pass

    class UniverseRegion(Thing):
        pass

    class Base(Thing):
        pass

    class Spaceship(Thing):
        pass

    class AncientSpaceship(Spaceship):
        pass

    class SpacePortal(Thing):
        pass

    class Chevron(Thing):
        pass

    class Mystery(Thing):
        pass

    class appearsIn(ObjectProperty):
        domain = [FictionalCharacter]
        range = [TelevisionSeries]

    class portrayedBy(ObjectProperty):
        domain = [FictionalCharacter]
        range = [Actor]

    class associatedWithOrganization(ObjectProperty):
        domain = [TelevisionSeries]
        range = [MediaOrganization]

    class evacuationDestination(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [AncientSpaceship]

    class unableToReturnTo(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [Planet]

    class firstAppearedIn(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [Episode]

    class firstBroadcastInCountry(ObjectProperty):
        domain = [Episode]
        range = [Country]

    class firstBroadcastInYear(ObjectProperty, FunctionalProperty):
        domain = [Episode]
        range = [Year]

    class investigatesChevron(ObjectProperty):
        domain = [Scientist]
        range = [Chevron]

    class chevronOf(ObjectProperty, FunctionalProperty):
        domain = [Chevron]
        range = [SpacePortal]

    class skepticalToward(ObjectProperty):
        domain = [Actor]
        range = [TelevisionSeries]

    class interestedInCharacter(ObjectProperty):
        domain = [Actor]
        range = [FictionalCharacter]

    class departsFromBase(ObjectProperty):
        domain = [Person]
        range = [Base]

    class travelsThroughPortal(ObjectProperty):
        domain = [Person]
        range = [SpacePortal]

    class premiseDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]

    class inabilityToReturnReason(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]

    class nationalityDescription(DataProperty, FunctionalProperty):
        domain = [Actor]
        range = [str]

    class skepticalAtFirst(DataProperty, FunctionalProperty):
        domain = [Actor]
        range = [bool]

    class interestReasonDescription(DataProperty, FunctionalProperty):
        domain = [Actor]
        range = [str]

    class characterizationDescription(DataProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [str]

    class lifeWorkDescription(DataProperty, FunctionalProperty):
        domain = [Scientist]
        range = [str]

    class discoveryOutcomeDescription(DataProperty, FunctionalProperty):
        domain = [Chevron]
        range = [str]

    class arrivalDestinationDescription(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class survivalChallengeDescription(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class travelRegionDescription(DataProperty, FunctionalProperty):
        domain = [Spaceship]
        range = [str]

    FictionalCharacter.is_a.append(appearsIn.some(TelevisionSeries))
    MachiavellianScientist.is_a.append(investigatesChevron.some(Chevron))
    CanadianAmericanTelevisionSeries.is_a.append(associatedWithOrganization.some(MediaOrganization))
    PilotEpisode.is_a.append(firstBroadcastInCountry.some(Country))

    DrNicholasRush = MachiavellianScientist("DrNicholasRush")
    DrNicholasRush.label = ["Dr. Nicholas Rush", "Rush"]

    StargateUniverse = CanadianAmericanTelevisionSeries("StargateUniverse")
    StargateUniverse.label = "Stargate Universe"
    StargateUniverse.is_a.append(MilitaryScienceFictionSerialDrama)

    MetroGoldwynMayer = ProductionCompany("MetroGoldwynMayer")
    MetroGoldwynMayer.label = "Metro - Goldwyn - Mayer"

    Syfy = TelevisionNetwork("Syfy")
    Syfy.label = "Syfy"

    Destiny = AncientSpaceship("Destiny")
    Destiny.label = "Destiny"

    Earth = Planet("Earth")
    Earth.label = "Earth"

    RobertCarlyle = Actor("RobertCarlyle")
    RobertCarlyle.label = ["Robert Carlyle", "Carlyle"]

    Stargate = SpacePortal("Stargate")
    Stargate.label = "Stargate"

    IcarusBase = Base("IcarusBase")
    IcarusBase.label = "Icarus Base"

    Air = PilotEpisode("Air")
    Air.label = ["Air", '" Air "']

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    Canada = Country("Canada")
    Canada.label = "Canada"

    Year2009 = Year("Year2009")
    Year2009.label = "2009"

    NinthChevron = Chevron("NinthChevron")
    NinthChevron.label = "ninth chevron"

    DrNicholasRush.appearsIn = [StargateUniverse]
    DrNicholasRush.portrayedBy = [RobertCarlyle]
    DrNicholasRush.firstAppearedIn = Air
    DrNicholasRush.investigatesChevron = [NinthChevron]
    DrNicholasRush.characterizationDescription = "machiavellian"
    DrNicholasRush.lifeWorkDescription = "uncovering the mysteries behind the ninth chevron of the Stargate"
    DrNicholasRush.departsFromBase = [IcarusBase]
    DrNicholasRush.travelsThroughPortal = [Stargate]
    DrNicholasRush.arrivalDestinationDescription = "a far-away galaxy"
    DrNicholasRush.survivalChallengeDescription = "fight for their own survival"

    StargateUniverse.associatedWithOrganization = [MetroGoldwynMayer, Syfy]
    StargateUniverse.evacuationDestination = Destiny
    StargateUniverse.unableToReturnTo = Earth
    StargateUniverse.premiseDescription = "the adventures of a present-day, multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny"
    StargateUniverse.inabilityToReturnReason = "the team is unable to return to Earth after evacuating to the Ancient spaceship Destiny"

    Destiny.travelRegionDescription = "a distant corner of the universe"

    RobertCarlyle.nationalityDescription = "Scottish"
    RobertCarlyle.skepticalToward = [StargateUniverse]
    RobertCarlyle.skepticalAtFirst = True
    RobertCarlyle.interestedInCharacter = [DrNicholasRush]
    RobertCarlyle.interestReasonDescription = 'he felt Rush was a "very interesting" character to portray'

    NinthChevron.chevronOf = Stargate
    NinthChevron.discoveryOutcomeDescription = "uncovering its mysteries leads Dr. Nicholas Rush and personnel from the Icarus Base through the Stargate to a far-away galaxy"

    Air.firstBroadcastInCountry = [UnitedStates, Canada]
    Air.firstBroadcastInYear = Year2009


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
