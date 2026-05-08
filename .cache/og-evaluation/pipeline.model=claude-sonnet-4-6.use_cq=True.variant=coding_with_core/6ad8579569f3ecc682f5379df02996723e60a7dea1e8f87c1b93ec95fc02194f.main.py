"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

1. Who portrays Dr. Nicholas Rush in Stargate Universe?
2. What nationality is the actor who plays Dr. Nicholas Rush?
3. What television network(s) produced Stargate Universe?
4. What type of television series is Stargate Universe?
5. What is the name of the Ancient spaceship featured in Stargate Universe?
6. What is the primary goal of Dr. Nicholas Rush's life work?
7. What is the name of the base from which personnel traveled through the Stargate?
8. In which episode did Dr. Nicholas Rush make his first appearance?
9. When was the pilot episode of Stargate Universe first broadcast?
10. In which countries was the pilot episode first broadcast?
11. What personality type is Dr. Nicholas Rush described as?
12. Why were the crew members unable to return to Earth?
13. What is the significance of the ninth chevron of the Stargate?
14. Where is Destiny traveling in the universe?
15. What was Robert Carlyle's initial attitude toward the show before taking the role?
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
    SocialObject,
    Society,
    TimeInterval,
)


with core:
    # ── Entity classes ────────────────────────────────────────────────────

    class FictionalCharacter(SocialObject):
        """A fictional character in a TV series."""

    class TvSeries(NonAgentiveSocialObject):
        """A television series (social artefact, no intentions)."""

    class TvEpisode(NonAgentiveSocialObject):
        """A single episode belonging to a TV series."""

    class Actor(AgentivePhysicalObject):
        """A person who portrays characters in TV / film."""

    class ProductionCompany(Society):
        """A company that produces TV or film content."""

    class TvNetwork(Society):
        """A television broadcast network."""

    class Spaceship(NonAgentivePhysicalObject):
        """An artificial spacecraft."""

    class MilitaryBase(NonAgentivePhysicalObject):
        """A military installation / facility."""

    class StargateDevice(NonAgentivePhysicalObject):
        """The Stargate — a fictional portal device."""

    class Country(Society):
        """A sovereign nation / state."""

    class Planet(NonAgentivePhysicalObject):
        """A planet in the universe."""

    # ── Properties ───────────────────────────────────────────────────────

    class portrayedBy(ObjectProperty):
        domain = [FictionalCharacter]
        range  = [Actor]

    class appearsInSeries(ObjectProperty):
        domain = [FictionalCharacter]
        range  = [TvSeries]

    class madeFirstAppearanceIn(ObjectProperty):
        domain = [FictionalCharacter]
        range  = [TvEpisode]

    class hasPersonalityTrait(DataProperty):
        domain = [FictionalCharacter]
        range  = [str]

    class lifeWorkGoal(DataProperty):
        domain = [FictionalCharacter]
        range  = [str]

    class producedBy(ObjectProperty):
        domain = [TvSeries]
        range  = [Society]

    class hasGenre(DataProperty):
        domain = [TvSeries]
        range  = [str]

    class featuresSpaceship(ObjectProperty):
        domain = [TvSeries]
        range  = [Spaceship]

    class personnelTraveledFrom(ObjectProperty):
        domain = [TvSeries]
        range  = [MilitaryBase]

    class unableToReturnTo(ObjectProperty):
        domain = [TvSeries]
        range  = [Planet]

    class hasNationality(DataProperty):
        domain = [Actor]
        range  = [str]

    class initialAttitudeTowardShow(DataProperty):
        domain = [Actor]
        range  = [str]

    class firstBroadcastIn(ObjectProperty):
        domain = [TvEpisode]
        range  = [Country]

    class firstBroadcastYear(DataProperty, FunctionalProperty):
        domain = [TvEpisode]
        range  = [int]

    class firstBroadcastedAt(ObjectProperty, FunctionalProperty):
        domain = [TvEpisode]
        range  = [TimeInterval]

    class spaceshipTravelingIn(DataProperty):
        domain = [Spaceship]
        range  = [str]

    class ninthChevronLeadsTo(DataProperty):
        domain = [StargateDevice]
        range  = [str]

    # ── Named instances ───────────────────────────────────────────────────

    # Fictional character
    rush = FictionalCharacter("Dr_Nicholas_Rush")
    rush.label = "Dr. Nicholas Rush"
    rush.hasPersonalityTrait.append("machiavellian")
    rush.lifeWorkGoal.append(
        "uncovering the mysteries behind the ninth chevron of the Stargate"
    )

    # Actor
    carlyle = Actor("Robert_Carlyle")
    carlyle.label = "Robert Carlyle"
    carlyle.hasNationality.append("Scottish")
    carlyle.initialAttitudeTowardShow.append("skeptical")

    # TV series
    sg_universe = TvSeries("Stargate_Universe")
    sg_universe.label = "Stargate Universe"
    sg_universe.hasGenre.append("military science fiction serial drama")

    # Production company and network
    mgm = ProductionCompany("Metro_Goldwyn_Mayer")
    mgm.label = "Metro-Goldwyn-Mayer"

    syfy = TvNetwork("Syfy")
    syfy.label = "Syfy"

    # Ancient spaceship
    destiny = Spaceship("Destiny")
    destiny.label = "Destiny"
    destiny.spaceshipTravelingIn.append("distant corner of the universe")

    # Military base
    icarus_base = MilitaryBase("Icarus_Base")
    icarus_base.label = "Icarus Base"

    # The Stargate device
    stargate = StargateDevice("Stargate")
    stargate.label = "Stargate"
    stargate.ninthChevronLeadsTo.append("far-away galaxy")

    # Pilot episode
    air = TvEpisode("Air")
    air.label = "Air"
    air.firstBroadcastYear = 2009

    # Countries of first broadcast
    us = Country("United_States")
    us.label = "United States"

    canada = Country("Canada")
    canada.label = "Canada"

    # Planet
    earth = Planet("Earth")
    earth.label = "Earth"

    # Time interval for 2009
    year_2009 = TimeInterval("Year2009")
    year_2009.label = "2009"

    # ── Assertions ────────────────────────────────────────────────────────

    rush.portrayedBy.append(carlyle)
    rush.appearsInSeries.append(sg_universe)
    rush.madeFirstAppearanceIn.append(air)

    sg_universe.producedBy.append(mgm)
    sg_universe.producedBy.append(syfy)
    sg_universe.featuresSpaceship.append(destiny)
    sg_universe.personnelTraveledFrom.append(icarus_base)
    sg_universe.unableToReturnTo.append(earth)

    air.firstBroadcastIn.append(us)
    air.firstBroadcastIn.append(canada)
    air.firstBroadcastedAt = year_2009


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
