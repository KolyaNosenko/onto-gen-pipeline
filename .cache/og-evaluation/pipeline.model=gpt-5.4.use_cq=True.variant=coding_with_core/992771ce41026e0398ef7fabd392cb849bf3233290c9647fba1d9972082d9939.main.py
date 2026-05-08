"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What is a grid cell?
2. In which part of the brain are grid cells found?
3. Which species are described as having grid cells in their brains?
4. What function do grid cells enable with respect to spatial position?
5. Who discovered grid cells?
6. In what year were grid cells discovered?
7. At which research center were grid cells discovered?
8. Which researchers were awarded the 2014 Nobel Prize in Physiology or Medicine for discoveries related to the brain’s positioning system?
9. For what discovery were Edvard Moser, May-Britt Moser, and John O'Keefe awarded the Nobel Prize?
10. What hypothesis was proposed based on the equal spacing of spatial firing fields in grid cells?
11. Do grid cells encode a cognitive representation of Euclidean space?
12. What mechanism for self-position computation was suggested by the discovery of grid cells?
13. What kind of information is continuously updated for dynamic computation of self-position?
14. In a typical experimental study, how is the activity of an individual neuron recorded?
15. In which animal is grid cell activity typically studied in the described experiment?
16. In which cortical region is the recording electrode implanted in the described grid cell experiment?
17. What happens when a dot is placed at the rat’s head location each time a grid cell emits an action potential?
18. What geometric pattern is formed by the firing locations of a grid cell over time?
19. Do the firing clusters of a grid cell form the vertices of a grid of equilateral triangles?
20. What feature distinguishes grid cells from other spatially firing cells?
21. How does the firing pattern of a grid cell differ from that of a place cell?
22. In which brain region are the place cells mentioned in the document located?
23. How many place fields does a place cell frequently show in a given environment?
24. When place cells show multiple clusters, is there regularity in their arrangement?
25. What is the relationship between action potentials and recorded spatial firing locations in grid cell experiments?
26. Can grid cells be identified by the regular triangular arrangement of their firing fields?
27. Can place cells be identified by the absence of a regular triangular firing pattern?
28. What type of spatial firing field arrangement is characteristic of grid cells?
29. What type of spatial firing field arrangement is characteristic of place cells?
30. Which individuals besides Edvard Moser and May-Britt Moser participated in the discovery of grid cells?
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
    AbstractRegion,
    Achievement,
    Accomplishment,
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    SocialObject,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class Person(AgentivePhysicalObject):
        pass


    class Researcher(Person):
        pass


    class StudentResearcher(Researcher):
        pass


    class Country(Society):
        pass


    class ResearchCenter(Society):
        pass


    class Species(SocialObject):
        pass


    class Organism(NonAgentivePhysicalObject):
        pass


    class Rat(Organism):
        pass


    class Brain(NonAgentivePhysicalObject):
        pass


    class BrainRegion(NonAgentivePhysicalObject):
        is_a = [partOf.some(Brain)]


    class CerebralCortex(BrainRegion):
        pass


    class DorsomedialEntorhinalCortex(CerebralCortex):
        pass


    class Hippocampus(BrainRegion):
        pass


    class Neuron(NonAgentivePhysicalObject):
        pass


    class GridCell(Neuron):
        pass


    class PlaceCell(Neuron):
        pass


    class Electrode(NonAgentivePhysicalObject):
        pass


    class ExperimentalEnvironment(NonAgentivePhysicalObject):
        pass


    class OpenArena(ExperimentalEnvironment):
        pass


    class ActionPotential(Achievement):
        pass


    class ExperimentalStudy(Accomplishment):
        pass


    class TypicalGridCellExperiment(ExperimentalStudy):
        pass


    class SpatialPositionUnderstanding(SocialObject):
        pass


    class PositioningSystem(SocialObject):
        pass


    class CognitiveRepresentation(SocialObject):
        pass


    class ScientificHypothesis(SocialObject):
        pass


    class ComputationMechanism(SocialObject):
        pass


    class InformationType(SocialObject):
        pass


    class PositionInformation(InformationType):
        pass


    class DirectionInformation(InformationType):
        pass


    class SpatialFiringPattern(SocialObject):
        pass


    class GridOfEquilateralTriangles(SpatialFiringPattern):
        pass


    class IrregularPlaceFieldArrangement(SpatialFiringPattern):
        pass


    class ScientificPrizeAward(Achievement):
        pass


    class GeometricSpace(AbstractRegion):
        pass


    class EuclideanSpaceEncodingHypothesis(ScientificHypothesis):
        pass


    class EuclideanSpaceRepresentation(CognitiveRepresentation):
        pass


    class DynamicSelfPositionComputationMechanism(ComputationMechanism):
        pass


    class studiedUnder(ObjectProperty):
        domain = [StudentResearcher]
        range = [Researcher]


    class locatedInCountry(partOf):
        domain = [ResearchCenter]
        range = [Country]


    class foundInSpecies(ObjectProperty):
        domain = [Neuron]
        range = [Species]


    class locatedInBrainRegion(partOf):
        domain = [Neuron]
        range = [BrainRegion]


    class enablesUnderstandingOf(ObjectProperty):
        domain = [GridCell]
        range = [SpatialPositionUnderstanding]


    class discoveredBy(ObjectProperty):
        domain = [GridCell]
        range = [Researcher]


    class discoveredInYear(ObjectProperty):
        domain = [GridCell]
        range = [TimeInterval]


    class discoveredAtResearchCenter(ObjectProperty):
        domain = [GridCell]
        range = [ResearchCenter]


    class recognizedByPrize(ObjectProperty):
        domain = [GridCell]
        range = [ScientificPrizeAward]


    class constitutesPositioningSystem(ObjectProperty):
        domain = [GridCell]
        range = [PositioningSystem]


    class hasCharacteristicPattern(ObjectProperty):
        domain = [Neuron]
        range = [SpatialFiringPattern]


    class supportsHypothesis(ObjectProperty):
        domain = [GridCell]
        range = [ScientificHypothesis]


    class encodesRepresentation(ObjectProperty):
        domain = [GridCell]
        range = [CognitiveRepresentation]


    class representsSpace(ObjectProperty):
        domain = [CognitiveRepresentation, ScientificHypothesis]
        range = [GeometricSpace]


    class suggestsMechanism(ObjectProperty):
        domain = [GridCell]
        range = [ComputationMechanism]


    class usesUpdatedInformation(ObjectProperty):
        domain = [ComputationMechanism]
        range = [InformationType]


    class awardedTo(ObjectProperty):
        domain = [ScientificPrizeAward]
        range = [Researcher]


    class usesInstrument(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Electrode]


    class studiesCellType(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Neuron]


    class performedOnAnimalType(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Organism]


    class hasImplantationSite(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [BrainRegion]


    class conductedInEnvironmentType(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [ExperimentalEnvironment]


    class recordsSignalType(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [ActionPotential]


    class producesPattern(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [SpatialFiringPattern]


    class awardCitation(DataProperty, FunctionalProperty):
        domain = [ScientificPrizeAward]
        range = [str]


    class patternDescription(DataProperty, FunctionalProperty):
        domain = [SpatialFiringPattern]
        range = [str]


    class clusterCountDescription(DataProperty, FunctionalProperty):
        domain = [SpatialFiringPattern]
        range = [str]


    class arrangementRegularityDescription(DataProperty, FunctionalProperty):
        domain = [SpatialFiringPattern]
        range = [str]


    class experimentProcedureDescription(DataProperty, FunctionalProperty):
        domain = [ExperimentalStudy]
        range = [str]


    class computationDescription(DataProperty, FunctionalProperty):
        domain = [ComputationMechanism]
        range = [str]


    EdvardMoser = Researcher("EdvardMoser")
    EdvardMoser.label = "Edvard Moser"

    MayBrittMoser = Researcher("MayBrittMoser")
    MayBrittMoser.label = "May - Britt Moser"

    TorkelHafting = StudentResearcher("TorkelHafting")
    TorkelHafting.label = "Torkel Hafting"

    MarianneFyhn = StudentResearcher("MarianneFyhn")
    MarianneFyhn.label = "Marianne Fyhn"

    SturlaMolden = StudentResearcher("SturlaMolden")
    SturlaMolden.label = "Sturla Molden"

    JohnOKeefe = Researcher("JohnOKeefe")
    JohnOKeefe.label = "John O'Keefe"

    CentreForTheBiologyOfMemoryCBM = ResearchCenter("CentreForTheBiologyOfMemoryCBM")
    CentreForTheBiologyOfMemoryCBM.label = "Centre for the Biology of Memory ( CBM )"

    Norway = Country("Norway")
    Norway.label = "Norway"

    NobelPrizeInPhysiologyOrMedicine2014 = ScientificPrizeAward("NobelPrizeInPhysiologyOrMedicine2014")
    NobelPrizeInPhysiologyOrMedicine2014.label = "2014 Nobel Prize in Physiology or Medicine"

    Year2005 = TimeInterval("Year2005")
    Year2005.label = "2005"

    Year2014 = TimeInterval("Year2014")
    Year2014.label = "2014"

    EuclideanSpaceEntity = GeometricSpace("EuclideanSpaceEntity")
    EuclideanSpaceEntity.label = "Euclidean space"

    TorkelHafting.studiedUnder = [EdvardMoser, MayBrittMoser]
    MarianneFyhn.studiedUnder = [EdvardMoser, MayBrittMoser]
    SturlaMolden.studiedUnder = [EdvardMoser, MayBrittMoser]

    CentreForTheBiologyOfMemoryCBM.locatedInCountry = [Norway]

    NobelPrizeInPhysiologyOrMedicine2014.temporallyLocatedAt = Year2014
    NobelPrizeInPhysiologyOrMedicine2014.awardedTo = [EdvardMoser, MayBrittMoser, JohnOKeefe]
    NobelPrizeInPhysiologyOrMedicine2014.awardCitation = (
        "their discoveries of cells that constitute a positioning system in the brain"
    )

    GridCell.foundInSpecies = [Species]
    GridCell.locatedInBrainRegion = [DorsomedialEntorhinalCortex]
    GridCell.enablesUnderstandingOf = [SpatialPositionUnderstanding]
    GridCell.discoveredBy = [
        EdvardMoser,
        MayBrittMoser,
        TorkelHafting,
        MarianneFyhn,
        SturlaMolden,
    ]
    GridCell.discoveredInYear = [Year2005]
    GridCell.discoveredAtResearchCenter = [CentreForTheBiologyOfMemoryCBM]
    GridCell.recognizedByPrize = [NobelPrizeInPhysiologyOrMedicine2014]
    GridCell.constitutesPositioningSystem = [PositioningSystem]
    GridCell.hasCharacteristicPattern = [GridOfEquilateralTriangles]
    GridCell.supportsHypothesis = [EuclideanSpaceEncodingHypothesis]
    GridCell.encodesRepresentation = [EuclideanSpaceRepresentation]
    GridCell.suggestsMechanism = [DynamicSelfPositionComputationMechanism]

    PlaceCell.locatedInBrainRegion = [Hippocampus]
    PlaceCell.hasCharacteristicPattern = [IrregularPlaceFieldArrangement]

    EuclideanSpaceEncodingHypothesis.representsSpace = [EuclideanSpaceEntity]
    EuclideanSpaceRepresentation.representsSpace = [EuclideanSpaceEntity]

    DynamicSelfPositionComputationMechanism.usesUpdatedInformation = [
        PositionInformation,
        DirectionInformation,
    ]
    DynamicSelfPositionComputationMechanism.computationDescription = (
        "dynamic computation of self - position based on continuously updated information about position and direction"
    )

    GridOfEquilateralTriangles.patternDescription = (
        "these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles"
    )
    GridOfEquilateralTriangles.arrangementRegularityDescription = (
        "This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing ."
    )

    IrregularPlaceFieldArrangement.patternDescription = (
        "the dots build up to form small clusters"
    )
    IrregularPlaceFieldArrangement.clusterCountDescription = (
        'frequently there is only one cluster ( one " place field " ) in a given environment'
    )
    IrregularPlaceFieldArrangement.arrangementRegularityDescription = (
        "even when multiple clusters are seen , there is no perceptible regularity in their arrangement"
    )

    TypicalGridCellExperiment.usesInstrument = [Electrode]
    TypicalGridCellExperiment.studiesCellType = [GridCell]
    TypicalGridCellExperiment.performedOnAnimalType = [Rat]
    TypicalGridCellExperiment.hasImplantationSite = [DorsomedialEntorhinalCortex]
    TypicalGridCellExperiment.conductedInEnvironmentType = [OpenArena]
    TypicalGridCellExperiment.recordsSignalType = [ActionPotential]
    TypicalGridCellExperiment.producesPattern = [GridOfEquilateralTriangles]
    TypicalGridCellExperiment.experimentProcedureDescription = (
        "an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and a dot is placed at the location of the rat 's head every time the neuron emits an action potential as the rat moves around freely in an open arena"
    )


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
