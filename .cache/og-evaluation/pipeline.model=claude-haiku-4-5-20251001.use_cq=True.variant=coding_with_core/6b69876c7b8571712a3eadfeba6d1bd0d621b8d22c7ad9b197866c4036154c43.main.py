"""
=== TASK INPUT ===
Source text:
Dr. Nicholas Rush is a fictional character in the Canadian - American Metro - Goldwyn - Mayer - Syfy television series Stargate Universe , a military science fiction serial drama about the adventures of a present - day , multinational exploration team unable to return to Earth after an evacuation to the Ancient spaceship Destiny , which is traveling in a distant corner of the universe . He is portrayed by Scottish actor Robert Carlyle . Carlyle , while at first skeptical towards the show , got an interest in the character of Rush because he felt Rush was a " very interesting " character to portray . Rush is a machiavellian scientist whose life 's work is uncovering the mysteries behind the ninth chevron of the Stargate , which ultimately leads him and personnel from the Icarus Base through the Stargate to a far - away galaxy where they must fight for their own survival . Rush made his first appearance in the pilot episode , " Air " , first broadcast in the United States and Canada in 2009 .

CQ1: Who portrays the character Dr. Nicholas Rush?

CQ2: In which television series does Dr. Nicholas Rush appear?

CQ3: What is the nationality of the actor who portrays Dr. Nicholas Rush?

CQ4: What is Dr. Nicholas Rush's primary area of scientific interest?

CQ5: In which episode does Dr. Nicholas Rush first appear?

CQ6: When was Dr. Nicholas Rush's first appearance broadcast?

CQ7: What spaceship do the characters evacuate to in Stargate Universe?

CQ8: From which location do the characters evacuate in the series?

CQ9: What is the production origin of the Stargate Universe series?

CQ10: What are the key characteristics of Dr. Nicholas Rush's personality?

CQ11: What motivates Dr. Nicholas Rush's scientific pursuits?

CQ12: Which base is mentioned in connection with Dr. Nicholas Rush's journey through the Stargate?
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
    AgentivePhysicalObject, NonAgentiveSocialObject, AgentiveSocialObject,
    Accomplishment, NonAgentivePhysicalObject, SpatialLocation
)


with core:
    # Entity classes
    class Actor(AgentivePhysicalObject):
        """A person who acts in television or film"""
        pass
    
    class TelevisionSeries(NonAgentiveSocialObject):
        """A television series"""
        pass
    
    class Character(AgentiveSocialObject):
        """A fictional character with agency and intentions"""
        pass
    
    class Episode(Accomplishment):
        """A television episode"""
        pass
    
    class Spaceship(NonAgentivePhysicalObject):
        """A spacecraft"""
        pass
    
    class Location(SpatialLocation):
        """A geographic or spatial location"""
        pass
    
    class Organization(NonAgentiveSocialObject):
        """An organization such as a production company or network"""
        pass
    
    # Object Properties
    class portrays(ObjectProperty):
        """An actor portrays a fictional character"""
        domain = [Actor]
        range = [Character]
    
    class appearsIn(ObjectProperty):
        """A character appears in a television series"""
        domain = [Character]
        range = [TelevisionSeries]
    
    class appearsInEpisode(ObjectProperty):
        """A character appears in a specific episode"""
        domain = [Character]
        range = [Episode]
    
    class evacuatesTo(ObjectProperty):
        """Characters evacuate to a location or vessel"""
        domain = [Character]
        range = [Spaceship]
    
    class evacuatesFrom(ObjectProperty):
        """Characters evacuate from a location"""
        domain = [Character]
        range = [Location]
    
    class producedBy(ObjectProperty):
        """A television series is produced by an organization"""
        domain = [TelevisionSeries]
        range = [Organization]
    
    class broadcastOn(ObjectProperty):
        """An episode is broadcast on a television series"""
        domain = [Episode]
        range = [TelevisionSeries]
    
    # Data Properties
    class nationality(DataProperty, FunctionalProperty):
        """The nationality of a person"""
        domain = [AgentivePhysicalObject]
        range = [str]
    
    class broadcastYear(DataProperty, FunctionalProperty):
        """The year in which an episode was broadcast"""
        domain = [Episode]
        range = [int]
    
    class personality(DataProperty):
        """A personality characteristic of a character"""
        domain = [Character]
        range = [str]
    
    class scientificInterestDescription(DataProperty, FunctionalProperty):
        """Description of a character's area of scientific interest"""
        domain = [Character]
        range = [str]
    
    class productionOrigin(DataProperty, FunctionalProperty):
        """The geographic origin of a television series' production"""
        domain = [TelevisionSeries]
        range = [str]
    
    # Named individuals
    robertCarlyle = Actor("RobertCarlyle")
    robertCarlyle.label = "Robert Carlyle"
    robertCarlyle.nationality = "Scottish"
    
    nicholasRush = Character("NicholasRush")
    nicholasRush.label = "Dr. Nicholas Rush"
    nicholasRush.personality = ["machiavellian"]
    nicholasRush.scientificInterestDescription = "the ninth chevron of the Stargate"
    
    stargateUniverse = TelevisionSeries("StargateUniverse")
    stargateUniverse.label = "Stargate Universe"
    stargateUniverse.productionOrigin = "Canadian-American"
    
    airEpisode = Episode("Air")
    airEpisode.label = "Air"
    airEpisode.broadcastYear = 2009
    
    destiny = Spaceship("Destiny")
    destiny.label = "Destiny"
    
    icarusBase = Location("IcarusBase")
    icarusBase.label = "Icarus Base"
    
    mgm = Organization("MGM")
    mgm.label = "Metro - Goldwyn - Mayer"
    
    syfy = Organization("Syfy")
    syfy.label = "Syfy"
    
    # Assign relationships
    robertCarlyle.portrays = [nicholasRush]
    nicholasRush.appearsIn = [stargateUniverse]
    nicholasRush.appearsInEpisode = [airEpisode]
    nicholasRush.evacuatesTo = [destiny]
    nicholasRush.evacuatesFrom = [icarusBase]
    airEpisode.broadcastOn = [stargateUniverse]
    stargateUniverse.producedBy = [mgm, syfy]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
