"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

Who is Dr. Nicholas Rush?
Is Dr. Nicholas Rush a fictional character?
In which television series does Dr. Nicholas Rush appear?
What is the nationality of the television series Stargate Universe?
Which companies are associated with the television series Stargate Universe?
What genre is Stargate Universe?
What is Stargate Universe about?
Why is the exploration team in Stargate Universe unable to return to Earth?
To which spaceship does the team evacuate?
What is the name of the Ancient spaceship in Stargate Universe?
Where is the spaceship Destiny traveling?
Who portrays Dr. Nicholas Rush?
What is Robert Carlyle’s nationality?
Why did Robert Carlyle become interested in playing Dr. Nicholas Rush?
How is Dr. Nicholas Rush characterized?
What is Dr. Nicholas Rush’s profession?
What is Dr. Nicholas Rush’s life’s work?
What mystery is Dr. Nicholas Rush trying to uncover?
What does uncovering the ninth chevron of the Stargate lead to?
From where do Dr. Nicholas Rush and the Icarus Base personnel travel through the Stargate?
To where are Dr. Nicholas Rush and the Icarus Base personnel transported?
What challenge do Dr. Nicholas Rush and the Icarus Base personnel face in the far-away galaxy?
In which episode did Dr. Nicholas Rush first appear?
What is the title of Dr. Nicholas Rush’s first appearance episode?
When was the pilot episode “Air” first broadcast?
In which countries was the pilot episode “Air” first broadcast?
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
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    SocialAgent,
    Society,
    TimeInterval,
)


with core:
    class TelevisionSeries(NonAgentiveSocialObject):
        pass


    class FictionalCharacter(SocialAgent):
        pass


    class TelevisionSeriesCharacter(FictionalCharacter):
        pass


    class ScientistCharacter(TelevisionSeriesCharacter):
        pass


    class MachiavellianScientistCharacter(ScientistCharacter):
        pass


    class Actor(AgentivePhysicalObject):
        pass


    class Company(Society):
        pass


    class TelevisionEpisode(NonAgentiveSocialObject):
        pass


    class PilotEpisode(TelevisionEpisode):
        pass


    class ExplorationTeam(Society):
        pass


    class MultinationalExplorationTeam(ExplorationTeam):
        pass


    class SpaceShip(NonAgentivePhysicalObject):
        pass


    class AncientSpaceShip(SpaceShip):
        pass


    class Planet(NonAgentivePhysicalObject):
        pass


    class Galaxy(NonAgentivePhysicalObject):
        pass


    class Base(NonAgentivePhysicalObject):
        pass


    class PortalDevice(NonAgentivePhysicalObject):
        pass


    class Country(Society):
        pass


    class CalendarYear(TimeInterval):
        pass


    class appearsInSeries(ObjectProperty):
        domain = [TelevisionSeriesCharacter]
        range = [TelevisionSeries]


    class portrayedBy(ObjectProperty):
        domain = [TelevisionSeriesCharacter]
        range = [Actor]


    class associatedWithCompany(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Company]


    class teamUnableToReturnTo(ObjectProperty):
        domain = [TelevisionSeries]
        range = [Planet]


    class teamEvacuatedTo(ObjectProperty):
        domain = [TelevisionSeries]
        range = [SpaceShip]


    class episodeOf(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]


    class firstAppearsInEpisode(ObjectProperty, FunctionalProperty):
        domain = [TelevisionSeriesCharacter]
        range = [TelevisionEpisode]


    class firstBroadcastInCountry(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Country]


    class firstBroadcastAt(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [CalendarYear]


    class seeksMysteryOf(ObjectProperty):
        domain = [ScientistCharacter]
        range = [PortalDevice]


    class becameInterestedInPortraying(ObjectProperty):
        domain = [Actor]
        range = [TelevisionSeriesCharacter]


    class fromBase(ObjectProperty):
        domain = [TelevisionSeriesCharacter]
        range = [Base]


    class travelsThrough(ObjectProperty):
        domain = [TelevisionSeriesCharacter]
        range = [PortalDevice]


    class nationalityDescription(DataProperty, FunctionalProperty):
        domain = [Or([Actor, TelevisionSeries])]
        range = [str]


    class genreDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]


    class seriesAboutDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]


    class teamUnableToReturnReasonDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeries]
        range = [str]


    class travelLocationDescription(DataProperty, FunctionalProperty):
        domain = [SpaceShip]
        range = [str]


    class characterizationDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeriesCharacter]
        range = [str]


    class lifeWorkDescription(DataProperty, FunctionalProperty):
        domain = [ScientistCharacter]
        range = [str]


    class soughtMysteryDescription(DataProperty, FunctionalProperty):
        domain = [ScientistCharacter]
        range = [str]


    class interestReasonDescription(DataProperty, FunctionalProperty):
        domain = [Actor]
        range = [str]


    class discoveryOutcomeDescription(DataProperty, FunctionalProperty):
        domain = [ScientistCharacter]
        range = [str]


    class transportDestinationDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeriesCharacter]
        range = [str]


    class survivalChallengeDescription(DataProperty, FunctionalProperty):
        domain = [TelevisionSeriesCharacter]
        range = [str]


    TelevisionSeriesCharacter.is_a.append(appearsInSeries.some(TelevisionSeries))
    TelevisionEpisode.is_a.append(episodeOf.some(TelevisionSeries))
    PilotEpisode.is_a.append(firstBroadcastAt.some(CalendarYear))

    DrNicholasRush = MachiavellianScientistCharacter("DrNicholasRush")
    DrNicholasRush.label = ["Dr. Nicholas Rush", "Rush"]

    StargateUniverse = TelevisionSeries("StargateUniverse")
    StargateUniverse.label = "Stargate Universe"

    MetroGoldwynMayer = Company("MetroGoldwynMayer")
    MetroGoldwynMayer.label = "Metro - Goldwyn - Mayer"

    Syfy = Company("Syfy")
    Syfy.label = "Syfy"

    Earth = Planet("Earth")
    Earth.label = "Earth"

    Destiny = AncientSpaceShip("Destiny")
    Destiny.label = "Destiny"

    RobertCarlyle = Actor("RobertCarlyle")
    RobertCarlyle.label = ["Robert Carlyle", "Carlyle"]

    Stargate = PortalDevice("Stargate")
    Stargate.label = "Stargate"

    IcarusBase = Base("IcarusBase")
    IcarusBase.label = "Icarus Base"

    Air = PilotEpisode("Air")
    Air.label = "Air"

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = "United States"

    Canada = Country("Canada")
    Canada.label = "Canada"

    Year2009 = CalendarYear("Year2009")
    Year2009.label = "2009"

    DrNicholasRush.appearsInSeries.append(StargateUniverse)
    DrNicholasRush.portrayedBy.append(RobertCarlyle)
    DrNicholasRush.characterizationDescription = "machiavellian"
    DrNicholasRush.lifeWorkDescription = (
        "uncovering the mysteries behind the ninth chevron of the Stargate"
    )
    DrNicholasRush.soughtMysteryDescription = (
        "the mysteries behind the ninth chevron of the Stargate"
    )
    DrNicholasRush.seeksMysteryOf.append(Stargate)
    DrNicholasRush.discoveryOutcomeDescription = (
        "it ultimately leads him and personnel from the Icarus Base through the "
        "Stargate to a far-away galaxy"
    )
    DrNicholasRush.fromBase.append(IcarusBase)
    DrNicholasRush.travelsThrough.append(Stargate)
    DrNicholasRush.transportDestinationDescription = "a far-away galaxy"
    DrNicholasRush.survivalChallengeDescription = "fight for their own survival"
    DrNicholasRush.firstAppearsInEpisode = Air

    StargateUniverse.nationalityDescription = "Canadian-American"
    StargateUniverse.associatedWithCompany.append(MetroGoldwynMayer)
    StargateUniverse.associatedWithCompany.append(Syfy)
    StargateUniverse.genreDescription = "military science fiction serial drama"
    StargateUniverse.seriesAboutDescription = (
        "the adventures of a present-day, multinational exploration team unable "
        "to return to Earth after an evacuation to the Ancient spaceship Destiny"
    )
    StargateUniverse.teamUnableToReturnTo.append(Earth)
    StargateUniverse.teamEvacuatedTo.append(Destiny)
    StargateUniverse.teamUnableToReturnReasonDescription = (
        "after an evacuation to the Ancient spaceship Destiny"
    )

    Destiny.travelLocationDescription = "a distant corner of the universe"

    RobertCarlyle.nationalityDescription = "Scottish"
    RobertCarlyle.becameInterestedInPortraying.append(DrNicholasRush)
    RobertCarlyle.interestReasonDescription = (
        'he felt Rush was a "very interesting" character to portray'
    )

    Air.episodeOf.append(StargateUniverse)
    Air.firstBroadcastAt = Year2009
    Air.firstBroadcastInCountry.append(UnitedStates)
    Air.firstBroadcastInCountry.append(Canada)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
