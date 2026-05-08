"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

1. Who is Dr. Nicholas Rush portrayed by?
2. In which television series does Dr. Nicholas Rush appear?
3. What type of character is Dr. Nicholas Rush?
4. What is Dr. Nicholas Rush’s profession?
5. What is the name of the actor who portrays Dr. Nicholas Rush?
6. What is Dr. Nicholas Rush’s life’s work?
7. What mystery is Dr. Nicholas Rush trying to uncover?
8. Which Stargate feature is central to Dr. Nicholas Rush’s research?
9. What event leads Dr. Nicholas Rush and the Icarus Base personnel through the Stargate?
10. To what location do Dr. Nicholas Rush and the Icarus Base personnel travel through the Stargate?
11. In which pilot episode does Dr. Nicholas Rush first appear?
12. In what year was Dr. Nicholas Rush’s first appearance broadcast?
13. Is Dr. Nicholas Rush a fictional character?
14. What kind of television series is Stargate Universe?
15. What is the Ancient spaceship named in the series?
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
    AgentivePhysicalObject,
    Event,
    Feature,
    NonAgentiveSocialObject,
    PhysicalObject,
    SocialObject,
)


with core:
    class FictionalCharacter(NonAgentiveSocialObject):
        pass

    class Scientist(SocialObject):
        pass

    class MachiavellianScientist(Scientist):
        pass

    class Actor(AgentivePhysicalObject):
        pass

    class TelevisionSeries(NonAgentiveSocialObject):
        pass

    class ScienceFictionSerialDrama(TelevisionSeries):
        pass

    class MilitaryScienceFictionSerialDrama(ScienceFictionSerialDrama):
        pass

    class TelevisionEpisode(Event):
        pass

    class PilotEpisode(TelevisionEpisode):
        pass

    class Country(SocialObject):
        pass

    class Organization(SocialObject):
        pass

    class ExplorationTeam(SocialObject):
        pass

    class PresentDayMultinationalExplorationTeam(ExplorationTeam):
        pass

    class Mystery(Abstract):
        pass

    class NinthChevronMystery(Mystery):
        pass

    class Evacuation(Event):
        pass

    class EvacuationToDestiny(Evacuation):
        pass

    class Planet(PhysicalObject):
        pass

    class Galaxy(PhysicalObject):
        pass

    class FarAwayGalaxy(Galaxy):
        pass

    class Spaceship(PhysicalObject):
        pass

    class AncientSpaceship(Spaceship):
        pass

    class Base(PhysicalObject):
        pass

    class StargateDevice(PhysicalObject):
        pass

    class Chevron(Feature):
        pass

    class NinthChevron(Chevron):
        pass

    class portrayedBy(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [Actor]

    class appearsIn(ObjectProperty):
        domain = [FictionalCharacter]
        range = [TelevisionSeries]

    class firstAppearsIn(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [TelevisionEpisode]

    class episodeOf(ObjectProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [TelevisionSeries]

    class lifeWork(DataProperty, FunctionalProperty):
        domain = [Scientist]
        range = [str]

    class seeks(ObjectProperty):
        domain = [Scientist]
        range = [Mystery]

    class concerns(ObjectProperty, FunctionalProperty):
        domain = [Mystery]
        range = [Chevron]

    class featureOf(ObjectProperty, FunctionalProperty):
        domain = [Feature]
        range = [StargateDevice]

    class about(ObjectProperty):
        domain = [TelevisionSeries]
        range = [ExplorationTeam]

    class firstBroadcastIn(ObjectProperty):
        domain = [TelevisionEpisode]
        range = [Country]

    class firstBroadcastYear(DataProperty, FunctionalProperty):
        domain = [TelevisionEpisode]
        range = [int]

    class travelsThrough(ObjectProperty, FunctionalProperty):
        domain = [FictionalCharacter]
        range = [StargateDevice]

    class travelsTo(ObjectProperty):
        domain = [FictionalCharacter]
        range = [Galaxy]

    class involvedIn(ObjectProperty):
        domain = [FictionalCharacter]
        range = [Evacuation]

    class destination(ObjectProperty, FunctionalProperty):
        domain = [Evacuation]
        range = [Spaceship]

    class leadsThrough(ObjectProperty, FunctionalProperty):
        domain = [Evacuation]
        range = [StargateDevice]

    class evacuatedTo(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [Spaceship]

    class cannotReturnTo(ObjectProperty, FunctionalProperty):
        domain = [ExplorationTeam]
        range = [Planet]

    DrNicholasRush = MachiavellianScientist("DrNicholasRush")
    DrNicholasRush.label = ["Dr. Nicholas Rush", "Rush"]

    RobertCarlyle = Actor("RobertCarlyle")
    RobertCarlyle.label = ["Robert Carlyle", "Carlyle"]

    StargateUniverse = MilitaryScienceFictionSerialDrama("StargateUniverse")
    StargateUniverse.label = ["Stargate Universe"]

    Destiny = AncientSpaceship("Destiny")
    Destiny.label = ["Destiny"]

    Air = PilotEpisode("Air")
    Air.label = ["Air"]

    UnitedStates = Country("UnitedStates")
    UnitedStates.label = ["United States"]

    Canada = Country("Canada")
    Canada.label = ["Canada"]

    Earth = Planet("Earth")
    Earth.label = ["Earth"]

    IcarusBase = Base("IcarusBase")
    IcarusBase.label = ["Icarus Base"]

    Stargate = StargateDevice("Stargate")
    Stargate.label = ["Stargate"]

    MetroGoldwynMayerSyfy = Organization("MetroGoldwynMayerSyfy")
    MetroGoldwynMayerSyfy.label = ["Metro-Goldwyn-Mayer-Syfy"]

    DrNicholasRush.portrayedBy = RobertCarlyle
    DrNicholasRush.appearsIn.append(StargateUniverse)
    DrNicholasRush.firstAppearsIn = Air
    DrNicholasRush.lifeWork = "uncovering the mysteries behind the ninth chevron of the Stargate"
    DrNicholasRush.travelsThrough = Stargate
    DrNicholasRush.is_a.append(FictionalCharacter)
    DrNicholasRush.is_a.append(seeks.some(NinthChevronMystery))
    DrNicholasRush.is_a.append(involvedIn.some(EvacuationToDestiny))
    DrNicholasRush.is_a.append(travelsTo.some(FarAwayGalaxy))

    Air.episodeOf = StargateUniverse
    Air.firstBroadcastIn.append(UnitedStates)
    Air.firstBroadcastIn.append(Canada)
    Air.firstBroadcastYear = 2009

    StargateUniverse.is_a.append(about.some(PresentDayMultinationalExplorationTeam))

    NinthChevronMystery.is_a.append(concerns.some(NinthChevron))
    NinthChevron.is_a.append(featureOf.value(Stargate))
    PresentDayMultinationalExplorationTeam.is_a.append(evacuatedTo.value(Destiny))
    PresentDayMultinationalExplorationTeam.is_a.append(cannotReturnTo.value(Earth))
    EvacuationToDestiny.is_a.append(destination.value(Destiny))
    EvacuationToDestiny.is_a.append(leadsThrough.value(Stargate))


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
