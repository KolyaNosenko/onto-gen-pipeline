"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What type of neuron is a grid cell?
2. In which year were grid cells discovered?
3. Who discovered grid cells?
4. At which institution were grid cells discovered?
5. In which country was the discovering institution located?
6. Which Nobel Prize were the discoverers of grid cells awarded?
7. In which year was the Nobel Prize awarded to the discoverers of grid cells?
8. Who shared the Nobel Prize with the discoverers of grid cells?
9. What type of spatial firing pattern do grid cells form?
10. What geometric shape is formed by the firing fields of grid cells?
11. What cognitive representation do grid cells encode?
12. What brain region is used to record grid cell activity in experimental studies?
13. In which animal species are grid cells typically studied experimentally?
14. How is a grid cell identified in an experimental study?
15. How does the firing pattern of a grid cell differ from that of a place cell?
16. Where in the brain are place cells located?
17. What is a place field?
18. What mechanism do grid cells provide for computing self-position?
19. What information is continuously updated to compute self-position using grid cells?
20. How many place fields does a place cell typically have in a given environment?
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
    NonAgentivePhysicalObject,
    AgentivePhysicalObject,
    Feature,
    Accomplishment,
    Achievement,
    NonAgentiveSocialObject,
    Society,
    MentalObject,
    AbstractRegion,
    SpaceRegion,
    TimeInterval,
    Process,
)

from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── ENTITY CLASSES ──────────────────────────────────────────────────────

    class Neuron(NonAgentivePhysicalObject):
        """A biological neuron cell found in animal brains."""

    class GridCell(Neuron):
        """A type of neuron whose firing fields tile space in a periodic
        grid of equilateral triangles, enabling spatial navigation."""

    class PlaceCell(Neuron):
        """A type of neuron found in the hippocampus whose firing defines
        one or more place fields in a given environment."""

    class BrainRegion(Feature):
        """A spatially distinct, anatomically named region of the brain,
        existentially dependent on the brain that hosts it."""

    class Researcher(AgentivePhysicalObject):
        """A person who conducts scientific research."""

    class ResearchInstitution(Society):
        """A collective organisation whose purpose is scientific research."""

    class Country(Society):
        """A sovereign nation-state."""

    class ScientificDiscovery(Accomplishment):
        """The event of first establishing and reporting a scientific
        finding."""

    class NobelPrize(NonAgentiveSocialObject):
        """An internationally recognised award for outstanding scientific
        or cultural contributions."""

    class ActionPotential(Achievement):
        """An individual, mereologically atomic neuronal firing event."""

    class SpatialFiringField(SpaceRegion):
        """A spatial region in which a neuron's action potentials cluster,
        as observed in experimental recordings."""

    class EquilateralTriangleGrid(SpatialFiringField):
        """The periodic hexagonal lattice of firing clusters characteristic
        of grid cells, whose vertices form equilateral triangles."""

    class PlaceField(SpatialFiringField):
        """The spatially localised cluster of firing associated with a
        place cell in a given environment; typically one per environment."""

    class CognitiveRepresentation(MentalObject):
        """A mental encoding of an aspect of the external world, dependent
        on the agentive physical object (animal) that holds it."""

    class PositionInformation(MentalObject):
        """Continuously updated information about the animal's current
        spatial position, used in self-position computation."""

    class DirectionInformation(MentalObject):
        """Continuously updated information about the animal's movement
        direction, used in self-position computation."""

    class Animal(AgentivePhysicalObject):
        """A non-human animal organism used as a subject in experimental
        studies of neural activity."""

    class Electrode(NonAgentivePhysicalObject):
        """A device implanted in neural tissue to record the electrical
        activity of individual neurons."""

    class Year(TimeInterval):
        """A time interval of exactly one calendar year."""

    class SelfPositionComputation(Process):
        """The continuous process by which an animal dynamically computes
        its own position using updated position and direction information."""

    # ── OBJECT PROPERTIES ───────────────────────────────────────────────────

    class discoveredBy(ObjectProperty):
        """Relates a discovery event to each researcher who made it."""
        domain = [ScientificDiscovery]
        range  = [Researcher]

    class discoveredAt(ObjectProperty):
        """Relates a discovery event to the institution where it occurred."""
        domain = [ScientificDiscovery]
        range  = [ResearchInstitution]

    class locatedIn(ObjectProperty):
        """Relates a research institution to the country it resides in."""
        domain = [ResearchInstitution]
        range  = [Country]

    class awardedTo(ObjectProperty):
        """Relates a prize to each researcher who received it."""
        domain = [NobelPrize]
        range  = [Researcher]

    class locatedInBrainRegion(ObjectProperty):
        """Relates a neuron type to the brain region in which it is found."""
        domain = [Neuron]
        range  = [BrainRegion]

    class encodes(ObjectProperty):
        """Relates a grid cell to the cognitive representation it encodes."""
        domain = [GridCell]
        range  = [CognitiveRepresentation]

    class representsRegion(ObjectProperty):
        """Relates a cognitive representation to the abstract region it
        represents (e.g. Euclidean space)."""
        domain = [CognitiveRepresentation]
        range  = [AbstractRegion]

    class formsFiringField(ObjectProperty):
        """Relates a neuron to the spatial firing field pattern it produces."""
        domain = [Neuron]
        range  = [SpatialFiringField]

    class implantedIn(ObjectProperty):
        """Relates a recording electrode to the brain region in which it
        is implanted."""
        domain = [Electrode]
        range  = [BrainRegion]

    class recordsActivityOf(ObjectProperty):
        """Relates an electrode to the individual neuron whose activity
        it records."""
        domain = [Electrode]
        range  = [Neuron]

    class enablesComputation(ObjectProperty):
        """Relates a grid cell to the self-position computation it
        supports."""
        domain = [GridCell]
        range  = [SelfPositionComputation]

    class updatesPositionInfo(ObjectProperty):
        """Relates a self-position computation process to the position
        information it continuously updates."""
        domain = [SelfPositionComputation]
        range  = [PositionInformation]

    class updatesDirectionInfo(ObjectProperty):
        """Relates a self-position computation process to the direction
        information it continuously updates."""
        domain = [SelfPositionComputation]
        range  = [DirectionInformation]

    # ── CLASS RESTRICTIONS ──────────────────────────────────────────────────

    GridCell.is_a.append(formsFiringField.some(EquilateralTriangleGrid))
    GridCell.is_a.append(encodes.some(CognitiveRepresentation))
    GridCell.is_a.append(enablesComputation.some(SelfPositionComputation))

    PlaceCell.is_a.append(formsFiringField.some(PlaceField))
    PlaceCell.is_a.append(locatedInBrainRegion.some(BrainRegion))

    CognitiveRepresentation.is_a.append(representsRegion.some(AbstractRegion))

    SelfPositionComputation.is_a.append(updatesPositionInfo.some(PositionInformation))
    SelfPositionComputation.is_a.append(updatesDirectionInfo.some(DirectionInformation))

    # ── INDIVIDUALS ─────────────────────────────────────────────────────────

    # Researchers who discovered grid cells
    EdvardMoser = Researcher("EdvardMoser")
    EdvardMoser.label = "Edvard Moser"

    MayBrittMoser = Researcher("MayBrittMoser")
    MayBrittMoser.label = "May-Britt Moser"

    TorkelHafting = Researcher("TorkelHafting")
    TorkelHafting.label = "Torkel Hafting"

    MarianneFyhn = Researcher("MarianneFyhn")
    MarianneFyhn.label = "Marianne Fyhn"

    SturlaMolden = Researcher("SturlaMolden")
    SturlaMolden.label = "Sturla Molden"

    # Nobel Prize co-recipient
    JohnOKeefe = Researcher("JohnOKeefe")
    JohnOKeefe.label = "John O'Keefe"

    # Research institution and host country
    CBM = ResearchInstitution("CentreForBiologyOfMemory")
    CBM.label = "Centre for the Biology of Memory (CBM)"

    NorwayInst = Country("Norway")
    NorwayInst.label = "Norway"

    CBM.locatedIn.append(NorwayInst)

    # Nobel Prize
    Nobel2014 = NobelPrize("Nobel2014PhysiologyOrMedicine")
    Nobel2014.label = "2014 Nobel Prize in Physiology or Medicine"
    Nobel2014.awardedTo.append(EdvardMoser)
    Nobel2014.awardedTo.append(MayBrittMoser)
    Nobel2014.awardedTo.append(TorkelHafting)
    Nobel2014.awardedTo.append(MarianneFyhn)
    Nobel2014.awardedTo.append(SturlaMolden)
    Nobel2014.awardedTo.append(JohnOKeefe)

    # Years
    Yr2005 = Year("Year2005")
    Yr2005.label = "2005"

    Yr2014 = Year("Year2014")
    Yr2014.label = "2014"

    Nobel2014.temporallyLocatedAt = Yr2014

    # Grid-cell discovery event
    GridDiscovery = ScientificDiscovery("GridCellDiscovery2005")
    GridDiscovery.label = "discovery of grid cells"
    GridDiscovery.discoveredBy.append(EdvardMoser)
    GridDiscovery.discoveredBy.append(MayBrittMoser)
    GridDiscovery.discoveredBy.append(TorkelHafting)
    GridDiscovery.discoveredBy.append(MarianneFyhn)
    GridDiscovery.discoveredBy.append(SturlaMolden)
    GridDiscovery.discoveredAt.append(CBM)
    GridDiscovery.temporallyLocatedAt = Yr2005

    # Named brain regions
    DMEntorhinalCortex = BrainRegion("DorsomedialEntorhinalCortex")
    DMEntorhinalCortex.label = "dorsomedial entorhinal cortex"

    RatHippocampus = BrainRegion("RatHippocampus")
    RatHippocampus.label = "rat hippocampus"

    # Abstract Euclidean space (what grid cells encode a representation of)
    EuclideanSpaceInst = AbstractRegion("EuclideanSpace")
    EuclideanSpaceInst.label = "Euclidean space"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
