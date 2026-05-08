"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What is a grid cell?
2. In which species’ brains are grid cells found?
3. What function do grid cells serve in understanding position in space?
4. When were grid cells discovered?
5. Who discovered grid cells?
6. Where were grid cells discovered?
7. In which country were grid cells discovered?
8. Which individuals were awarded the 2014 Nobel Prize in Physiology or Medicine for discoveries related to grid cells?
9. What did the Nobel Prize-winning discoveries constitute in the brain?
10. What hypothesis was suggested by the arrangement of spatial firing fields in grid cells?
11. What kind of spatial representation do grid cells encode according to the hypothesis?
12. What mechanism for self-position computation was suggested by the discovery of grid cells?
13. What information is continuously updated to support self-position computation?
14. In typical experimental studies of grid cells, where is the recording electrode implanted?
15. In typical experimental studies, in what brain region are grid cells recorded?
16. In typical experimental studies, what animal is commonly used to record grid cell activity?
17. What does placing a dot at the rat’s head location each time a grid cell fires reveal over time?
18. What geometric pattern do the firing clusters of a grid cell form?
19. What shape are the triangles in the grid-like pattern formed by grid cell firing?
20. What feature distinguishes grid cells from other cells that show spatial firing?
21. How do place cells differ from grid cells in their firing cluster arrangement?
22. How many place fields does a place cell typically have in a given environment?
23. Do place cells show regularity in the arrangement of their firing fields?
24. From which brain structure are place cells examined in the comparison with grid cells?
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
    AbstractRegion,
    Accomplishment,
    Achievement,
    Event,
    NonAgentivePhysicalObject,
    Process,
    SocialAgent,
    SocialObject,
    Society,
    SpaceRegion,
    SpatialLocation,
    TimeInterval,
)


with core:
    class Scientist(SocialAgent):
        pass

    class ResearchCentre(SocialObject):
        pass

    class Country(Society):
        pass

    class Species(Abstract):
        pass

    class BrainStructure(NonAgentivePhysicalObject):
        pass

    class CerebralCortex(BrainStructure):
        pass

    class DorsomedialEntorhinalCortex(CerebralCortex):
        pass

    class Hippocampus(BrainStructure):
        pass

    class Neuron(NonAgentivePhysicalObject):
        pass

    class GridCell(Neuron):
        pass

    class PlaceCell(Neuron):
        pass

    class RecordingElectrode(NonAgentivePhysicalObject):
        pass

    class Rat(NonAgentivePhysicalObject):
        pass

    class Arena(NonAgentivePhysicalObject):
        pass

    class OpenArena(Arena):
        pass

    class ActionPotential(Achievement):
        pass

    class Dot(NonAgentivePhysicalObject):
        pass

    class Cluster(Abstract):
        pass

    class GridPattern(Abstract):
        pass

    class RegularTrianglePattern(GridPattern):
        pass

    class EquilateralTriangle(Abstract):
        pass

    class SpatialFiringField(SpaceRegion):
        pass

    class PlaceField(SpaceRegion):
        pass

    class PositionInSpace(SpatialLocation):
        pass

    class EuclideanSpace(AbstractRegion):
        pass

    class CognitiveRepresentationOfEuclideanSpace(Abstract):
        pass

    class PositioningSystem(Abstract):
        pass

    class Hypothesis(Abstract):
        pass

    class EuclideanSpaceEncodingHypothesis(Hypothesis):
        pass

    class SpatialFiringFieldArrangement(Abstract):
        pass

    class Information(Abstract):
        pass

    class representsSpace(ObjectProperty):
        domain = [CognitiveRepresentationOfEuclideanSpace]
        range = [EuclideanSpace]

    class SpatialInformation(Information):
        pass

    class PositionAndDirectionInformation(SpatialInformation):
        pass

    class DynamicSelfPositionComputation(Process):
        pass

    class Discovery(Accomplishment):
        pass

    class GridCellDiscoveryEvent(Discovery):
        pass

    class PrizeAward(Achievement):
        pass

    class ExperimentalStudy(Event):
        pass

    class GridCellRecordingStudy(ExperimentalStudy):
        pass

    class foundInSpecies(ObjectProperty):
        domain = [GridCell]
        range = [Species]

    class understandsPositionInSpace(ObjectProperty):
        domain = [GridCell]
        range = [PositionInSpace]

    class encodesRepresentationOf(ObjectProperty):
        domain = [GridCell]
        range = [CognitiveRepresentationOfEuclideanSpace]

    class hasSpatialFiringField(ObjectProperty):
        domain = [GridCell]
        range = [SpatialFiringField]

    class distinguishedBy(ObjectProperty):
        domain = [Neuron]
        range = [GridPattern]

    class emitsActionPotential(ObjectProperty):
        domain = [Neuron]
        range = [ActionPotential]

    class hasPlaceField(ObjectProperty):
        domain = [PlaceCell]
        range = [PlaceField]

    class originatesFrom(ObjectProperty):
        domain = [PlaceCell]
        range = [Hippocampus]

    class recordsActivityOf(ObjectProperty):
        domain = [RecordingElectrode]
        range = [Neuron]

    class implantedIn(ObjectProperty):
        domain = [RecordingElectrode]
        range = [DorsomedialEntorhinalCortex]

    class usesAnimal(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Rat]

    class hasRecordingElectrode(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [RecordingElectrode]

    class recordsNeuron(ObjectProperty):
        domain = [GridCellRecordingStudy]
        range = [GridCell]

    class recordedInRegion(ObjectProperty):
        domain = [GridCellRecordingStudy]
        range = [DorsomedialEntorhinalCortex]

    class takesPlaceIn(ObjectProperty):
        domain = [GridCellRecordingStudy]
        range = [OpenArena]

    class movesAroundIn(ObjectProperty):
        domain = [Rat]
        range = [OpenArena]

    class discoveredBy(ObjectProperty):
        domain = [GridCellDiscoveryEvent]
        range = [Scientist]

    class discoveredAt(ObjectProperty):
        domain = [GridCellDiscoveryEvent]
        range = [ResearchCentre]

    class discoveredInCountry(ObjectProperty):
        domain = [GridCellDiscoveryEvent]
        range = [Country]

    class locatedInCountry(ObjectProperty):
        domain = [ResearchCentre]
        range = [Country]

    class awardedTo(ObjectProperty):
        domain = [PrizeAward]
        range = [Scientist]

    class awardedFor(ObjectProperty):
        domain = [PrizeAward]
        range = [Discovery]

    class suggestsHypothesis(ObjectProperty):
        domain = [SpatialFiringFieldArrangement]
        range = [Hypothesis]

    class constitutes(ObjectProperty):
        domain = [Discovery]
        range = [PositioningSystem]

    class suggestsMechanismFor(ObjectProperty):
        domain = [Discovery]
        range = [DynamicSelfPositionComputation]

    class basedOnInformationAbout(ObjectProperty):
        domain = [DynamicSelfPositionComputation]
        range = [PositionAndDirectionInformation]

    class buildsUpToForm(ObjectProperty):
        domain = [Dot]
        range = [Cluster]

    class formsVerticesOf(ObjectProperty):
        domain = [Cluster]
        range = [GridPattern]

    class consistsOfTriangle(ObjectProperty):
        domain = [GridPattern]
        range = [EquilateralTriangle]

    Neuron.is_a.append(emitsActionPotential.some(ActionPotential))
    GridCell.is_a.append(foundInSpecies.some(Species))
    GridCell.is_a.append(understandsPositionInSpace.some(PositionInSpace))
    GridCell.is_a.append(encodesRepresentationOf.some(CognitiveRepresentationOfEuclideanSpace))
    GridCell.is_a.append(hasSpatialFiringField.some(SpatialFiringField))
    GridCell.is_a.append(distinguishedBy.some(RegularTrianglePattern))
    PlaceCell.is_a.append(hasPlaceField.some(PlaceField))
    PlaceCell.is_a.append(originatesFrom.some(Hippocampus))
    PlaceCell.is_a.append(Not(distinguishedBy.some(RegularTrianglePattern)))
    RecordingElectrode.is_a.append(recordsActivityOf.some(Neuron))
    RecordingElectrode.is_a.append(implantedIn.some(DorsomedialEntorhinalCortex))
    Rat.is_a.append(movesAroundIn.some(OpenArena))
    SpatialFiringFieldArrangement.is_a.append(suggestsHypothesis.some(EuclideanSpaceEncodingHypothesis))
    CognitiveRepresentationOfEuclideanSpace.is_a.append(representsSpace.some(EuclideanSpace))
    DynamicSelfPositionComputation.is_a.append(
        basedOnInformationAbout.some(PositionAndDirectionInformation)
    )
    GridCellDiscoveryEvent.is_a.append(constitutes.some(PositioningSystem))
    GridCellDiscoveryEvent.is_a.append(
        suggestsMechanismFor.some(DynamicSelfPositionComputation)
    )
    GridCellRecordingStudy.is_a.append(usesAnimal.some(Rat))
    GridCellRecordingStudy.is_a.append(hasRecordingElectrode.some(RecordingElectrode))
    GridCellRecordingStudy.is_a.append(recordsNeuron.some(GridCell))
    GridCellRecordingStudy.is_a.append(recordedInRegion.some(DorsomedialEntorhinalCortex))
    GridCellRecordingStudy.is_a.append(takesPlaceIn.some(OpenArena))
    Dot.is_a.append(buildsUpToForm.some(Cluster))
    Cluster.is_a.append(formsVerticesOf.some(GridPattern))
    GridPattern.is_a.append(consistsOfTriangle.some(EquilateralTriangle))

    edvard_moser = Scientist("EdvardMoser")
    edvard_moser.label = "Edvard Moser"

    may_britt_moser = Scientist("MayBrittMoser")
    may_britt_moser.label = "May - Britt Moser"

    torkel_hafting = Scientist("TorkelHafting")
    torkel_hafting.label = "Torkel Hafting"

    marianne_fyhn = Scientist("MarianneFyhn")
    marianne_fyhn.label = "Marianne Fyhn"

    sturla_molden = Scientist("SturlaMolden")
    sturla_molden.label = "Sturla Molden"

    john_okeefe = Scientist("JohnOKeefe")
    john_okeefe.label = "John O'Keefe"

    cbm = ResearchCentre("CentreForTheBiologyOfMemoryCBM")
    cbm.label = "Centre for the Biology of Memory ( CBM )"

    norway = Country("Norway")
    norway.label = "Norway"

    year_2005 = TimeInterval("Year2005")
    year_2005.label = "2005"

    year_2014 = TimeInterval("Year2014")
    year_2014.label = "2014"

    grid_cell_discovery = GridCellDiscoveryEvent("GridCellDiscovery")
    grid_cell_discovery.label = "discovery of grid cells"
    grid_cell_discovery.discoveredBy.append(edvard_moser)
    grid_cell_discovery.discoveredBy.append(may_britt_moser)
    grid_cell_discovery.discoveredBy.append(torkel_hafting)
    grid_cell_discovery.discoveredBy.append(marianne_fyhn)
    grid_cell_discovery.discoveredBy.append(sturla_molden)
    grid_cell_discovery.discoveredAt.append(cbm)
    grid_cell_discovery.discoveredInCountry.append(norway)
    grid_cell_discovery.temporallyLocatedAt = year_2005

    cbm.locatedInCountry.append(norway)

    nobel_prize_2014 = PrizeAward("NobelPrizeInPhysiologyOrMedicine2014")
    nobel_prize_2014.label = "2014 Nobel Prize in Physiology or Medicine"
    nobel_prize_2014.awardedTo.append(edvard_moser)
    nobel_prize_2014.awardedTo.append(may_britt_moser)
    nobel_prize_2014.awardedTo.append(torkel_hafting)
    nobel_prize_2014.awardedTo.append(marianne_fyhn)
    nobel_prize_2014.awardedTo.append(sturla_molden)
    nobel_prize_2014.awardedTo.append(john_okeefe)
    nobel_prize_2014.awardedFor.append(grid_cell_discovery)
    nobel_prize_2014.temporallyLocatedAt = year_2014


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
