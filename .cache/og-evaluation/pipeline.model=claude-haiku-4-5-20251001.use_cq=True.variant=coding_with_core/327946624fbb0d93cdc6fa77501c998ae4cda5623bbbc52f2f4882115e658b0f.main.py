"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

1. Who initiated the military reforms of the Florentine Republic?
2. During which time period did the Republic of Florence exist?
3. What was the primary inspiration for Machiavelli's military reforms?
4. What were the main objectives of Machiavelli's military reforms?
5. In what year were the military reforms instituted?
6. How many men comprised the citizen army established by Machiavelli?
7. What was the purpose of the citizen-infantry established by Machiavelli?
8. Who was the political leader under whom the Florentine Republic existed during this period?
9. What threats did the citizen army need to address?
10. What system did Machiavelli establish to maintain the citizen army's readiness?
11. What military model did Machiavelli seek to replicate?
12. Why did Machiavelli focus on establishing an army with the discipline of Roman legions?
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
    AgentivePhysicalObject, Society, Accomplishment, TimeInterval
)


with core:
    # Domain entity classes
    class Politician(AgentivePhysicalObject):
        """A person engaged in politics."""
        pass
    
    class MilitaryReform(Accomplishment):
        """A military reform, a series of changes to military organization and structure."""
        pass
    
    class CitizenArmy(Society):
        """A military force composed of citizens rather than professional soldiers."""
        pass
    
    # Domain properties
    class initiatedBy(ObjectProperty):
        """Relates an event to the agent that initiated it."""
        domain = [Accomplishment]
        range = [AgentivePhysicalObject]
    
    class leaderOf(ObjectProperty):
        """Relates a person to an organization they lead."""
        domain = [AgentivePhysicalObject]
        range = [Society]
    
    class modelledOn(ObjectProperty):
        """Relates a reform to the model or inspiration it is based on."""
        domain = [Accomplishment]
        range = [Society]
    
    class citizenArmySize(DataProperty, FunctionalProperty):
        """The size of a citizen army measured in number of soldiers."""
        domain = [CitizenArmy]
        range = [int]
    
    # Domain instances - named entities from the source text
    niccoloMachiavelli = Politician("NiccoloMachiavelli")
    niccoloMachiavelli.label = "Niccolò Machiavelli"
    
    girolamoSavonarola = Politician("GirolamoSavonarola")
    girolamoSavonarola.label = "Girolamo Savonarola"
    
    florentineRepublic = Society("FlorentineRepublic")
    florentineRepublic.label = "Florentine Republic"
    
    ancientRome = Society("AncientRome")
    ancientRome.label = "ancient Rome"
    
    # Time intervals
    timeInterval1498_1512 = TimeInterval("TimeInterval1498-1512")
    timeInterval1498_1512.label = "1498-1512"
    
    timeInterval1506 = TimeInterval("TimeInterval1506")
    timeInterval1506.label = "1506"
    
    # Military reforms instance
    militaryReforms = MilitaryReform("FlorentineMilitaryReforms1506")
    militaryReforms.label = "military reforms"
    militaryReforms.initiatedBy = [niccoloMachiavelli]
    militaryReforms.modelledOn = [ancientRome]
    militaryReforms.temporallyLocatedAt = timeInterval1506
    
    # Florentine Republic temporal extent
    florentineRepublic.temporallyLocatedAt = timeInterval1498_1512
    
    # Leadership relation
    girolamoSavonarola.leaderOf = [florentineRepublic]
    
    # Citizen army instance
    citizenArmy = CitizenArmy("FlorentineCitizenArmy")
    citizenArmy.label = "citizen army"
    citizenArmy.citizenArmySize = 20000


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
