"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What is a grid cell and what is its function in the brain?

2. Who discovered grid cells and in what year were they discovered?

3. Which researchers were awarded the Nobel Prize in Physiology or Medicine in 2014 for their discoveries related to grid cells?

4. What is the spatial firing pattern of grid cells?

5. In which part of the brain are grid cells typically located?

6. How are grid cells experimentally studied and recorded?

7. What is the geometric arrangement of grid cell firing fields?

8. How do grid cells differ from place cells in terms of their firing patterns?

9. What cognitive representation do grid cells encode?

10. What mechanism do grid cells provide for computing self-position in space?

11. In which species have grid cells been discovered?

12. What is the role of the dorsomedial entorhinal cortex in grid cell activity?

13. How can the regular triangle-pattern of grid cells be distinguished from other spatial firing cells?

14. What is the relationship between grid cells and a positioning system in the brain?

15. How do continuously updated information about position and direction relate to grid cell function?
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
    AgentivePhysicalObject, NonAgentivePhysicalObject, Feature,
    Achievement, Accomplishment, PhysicalQuality, AbstractRegion, Abstract,
    MentalObject, NonPhysicalObject, TimeInterval, AgentiveSocialObject,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # Define all entity classes first (before properties that reference them)
    
    # Brain and anatomical regions
    class Brain(NonAgentivePhysicalObject):
        """An organ of the central nervous system."""
        pass
    
    class BrainRegion(Feature):
        """A distinct anatomical region of the brain."""
        pass
    
    class CerebralCortex(BrainRegion):
        """The outer layer of the brain."""
        pass
    
    class EntorhinalCortex(BrainRegion):
        """A brain region involved in spatial navigation."""
        pass
    
    class DorsomedialEntorhinalCortex(EntorhinalCortex):
        """A specific region of the medial entorhinal cortex."""
        pass
    
    class Hippocampus(BrainRegion):
        """A brain region involved in memory and spatial navigation."""
        pass
    
    # Qualities and spatial/abstract regions (needed before neuron classes)
    class FiringPattern(PhysicalQuality):
        """A pattern of neural activity in space and time."""
        pass
    
    class SpatialFiringField(AbstractRegion):
        """A spatial region where a neuron fires."""
        pass
    
    class Cluster(SpatialFiringField):
        """A spatial grouping of firing locations."""
        pass
    
    class GridPattern(SpatialFiringField):
        """A regular geometric pattern of firing fields in a grid arrangement."""
        pass
    
    class Triangle(Abstract):
        """A geometric shape with three sides."""
        pass
    
    class PositioningSystem(NonPhysicalObject):
        """A neural system that encodes spatial position."""
        pass
    
    class CognitiveRepresentation(MentalObject):
        """A mental model or representation in the brain."""
        pass
    
    class EuclideanSpace(Abstract):
        """The mathematical space of Euclidean geometry."""
        pass
    
    # Research and agents
    class Researcher(AgentivePhysicalObject):
        """A scientist who conducts research."""
        pass
    
    class ResearchCentre(AgentiveSocialObject):
        """An institution where scientific research is conducted."""
        pass
    
    # Events
    class Discovery(Accomplishment):
        """An event of discovering something new."""
        pass
    
    class NobelPrizeAward(Accomplishment):
        """An event of awarding the Nobel Prize."""
        pass
    
    class ActionPotential(Achievement):
        """An instantaneous firing event of a neuron."""
        pass
    
    # Experimental apparatus and subjects
    class Electrode(NonAgentivePhysicalObject):
        """A device for recording neural activity."""
        pass
    
    class Arena(NonAgentivePhysicalObject):
        """An experimental space for behavioral testing."""
        pass
    
    class Rat(AgentivePhysicalObject):
        """A rodent used as an experimental subject."""
        pass
    
    # Neurons and related cell types (defined after related classes)
    class Neuron(NonAgentivePhysicalObject):
        """A cell in the nervous system."""
        pass
    
    class GridCell(Neuron):
        """A type of neuron that fires in a regular grid pattern."""
        pass
    
    class PlaceCell(Neuron):
        """A type of neuron in the hippocampus that fires at specific locations."""
        pass
    
    # Properties (relationships)
    
    class discoveredBy(ObjectProperty):
        """Relates a discovery event to the researchers who made it."""
        domain = [Discovery]
        range = [Researcher]
    
    class worksAt(ObjectProperty):
        """Relates a researcher to their workplace or institution."""
        domain = [Researcher]
        range = [ResearchCentre]
    
    class hasStudent(ObjectProperty):
        """Relates a researcher to their student."""
        domain = [Researcher]
        range = [Researcher]
    
    class awardedTo(ObjectProperty):
        """Relates an award event to the recipient researchers."""
        domain = [NobelPrizeAward]
        range = [Researcher]
    
    class exhibits(ObjectProperty):
        """Relates a neuron to the pattern of activity it exhibits."""
        domain = [Neuron]
        range = [FiringPattern]
    
    class implantedIn(ObjectProperty, FunctionalProperty):
        """Relates an electrode to the brain region where it is implanted."""
        domain = [Electrode]
        range = [BrainRegion]
    
    class locatedIn(ObjectProperty):
        """Relates a neuron to the brain region where it is located."""
        domain = [Neuron]
        range = [BrainRegion]
    
    class encodes(ObjectProperty):
        """Relates a neuron to the cognitive representation it encodes."""
        domain = [Neuron]
        range = [CognitiveRepresentation]
    
    class constitutes(ObjectProperty):
        """Relates neurons to the positioning system they form together."""
        domain = [Neuron]
        range = [PositioningSystem]
    
    # Instances (named entities from the text)
    
    # Research institution
    cbm = ResearchCentre("CBM")
    cbm.label = "Centre for the Biology of Memory"
    
    # Brain regions
    cerebral_cortex = CerebralCortex("CerebralCortex_region")
    cerebral_cortex.label = "cerebral cortex"
    
    dorsomedial_ec = DorsomedialEntorhinalCortex("DorsomedialEC_region")
    dorsomedial_ec.label = "dorsomedial entorhinal cortex"
    
    hippocampus_instance = Hippocampus("Hippocampus_region")
    hippocampus_instance.label = "hippocampus"
    
    # Time intervals for discovery and award
    year_2005 = TimeInterval("TimeInterval_2005")
    year_2005.label = "2005"
    
    year_2014 = TimeInterval("TimeInterval_2014")
    year_2014.label = "2014"
    
    # Researchers who discovered grid cells
    edvard_moser = Researcher("EdvardMoser")
    edvard_moser.label = "Edvard Moser"
    edvard_moser.worksAt = [cbm]
    
    may_britt_moser = Researcher("MayBrittMoser")
    may_britt_moser.label = "May-Britt Moser"
    may_britt_moser.worksAt = [cbm]
    
    torkel_hafting = Researcher("TorkelHafting")
    torkel_hafting.label = "Torkel Hafting"
    torkel_hafting.worksAt = [cbm]
    
    marianne_fyhn = Researcher("MarianneFyhn")
    marianne_fyhn.label = "Marianne Fyhn"
    marianne_fyhn.worksAt = [cbm]
    
    sturla_molden = Researcher("SturlaMolden")
    sturla_molden.label = "Sturla Molden"
    sturla_molden.worksAt = [cbm]
    
    john_okeefe = Researcher("JohnOKeefe")
    john_okeefe.label = "John O'Keefe"
    
    # Student relationships
    edvard_moser.hasStudent = [torkel_hafting, marianne_fyhn, sturla_molden]
    may_britt_moser.hasStudent = [torkel_hafting, marianne_fyhn, sturla_molden]
    
    # Discovery event
    grid_cell_discovery = Discovery("GridCellDiscovery")
    grid_cell_discovery.label = "discovery of grid cells"
    grid_cell_discovery.discoveredBy = [edvard_moser, may_britt_moser, torkel_hafting, marianne_fyhn, sturla_molden]
    grid_cell_discovery.temporallyLocatedAt = year_2005
    
    # Nobel Prize award event
    nobel_prize_2014 = NobelPrizeAward("NobelPrize2014")
    nobel_prize_2014.label = "2014 Nobel Prize in Physiology or Medicine"
    nobel_prize_2014.awardedTo = [edvard_moser, may_britt_moser, john_okeefe]
    nobel_prize_2014.temporallyLocatedAt = year_2014


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
