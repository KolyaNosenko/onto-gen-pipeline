"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

What is a grid cell?
In which species have grid cells been found?
What role do grid cells play in spatial understanding or navigation?
Who discovered grid cells?
In what year were grid cells discovered?
At which institution or research centre were grid cells discovered?
Which researchers were awarded the 2014 Nobel Prize in Physiology or Medicine for the discovery related to the brain’s positioning system?
What was John O'Keefe’s relationship to the Nobel-recognized discovery of the brain’s positioning system?
What type of positioning system in the brain are grid cells part of?
What hypothesis was proposed based on the equal distances between spatial firing fields of grid cells?
Do grid cells encode a cognitive representation of Euclidean space?
What mechanism for self-position computation was suggested by the discovery of grid cells?
What kinds of information are continuously updated for dynamic computation of self-position?
In what type of experimental study are grid cells typically recorded?
What device is used to record the activity of an individual neuron in grid cell experiments?
In which part of the brain are recordings of grid cells typically made in rats?
What is the relationship between the dorsomedial entorhinal cortex and grid cells?
Under what behavioral conditions is rat neural activity recorded in a typical grid cell experiment?
How is the firing pattern of a grid cell visualized during an experiment?
What is plotted each time a grid cell emits an action potential?
What pattern is formed by the firing locations of a grid cell over time?
Do the firing fields of a grid cell form small clusters?
Do the clusters formed by grid cell firing correspond to the vertices of a grid of equilateral triangles?
What spatial regularity distinguishes grid cells from other spatially firing cells?
How do grid cells differ from place cells in their spatial firing patterns?
What is a place field in the context of place cells?
How many place fields does a place cell frequently exhibit in a given environment?
Can place cells exhibit multiple clusters in a given environment?
Is there regularity in the arrangement of multiple clusters formed by place cells?
What distinguishing geometric pattern is associated with grid cells but not with place cells?
Which brain region is associated with place cells in the rat?
How can an ontology distinguish between grid cells and place cells based on firing field organization?
What is the relationship between neuronal action potentials and spatial firing maps in grid cell studies?
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
    class LivingThing(Thing):
        pass

    class Animal(LivingThing):
        pass

    class Person(LivingThing):
        pass

    class Researcher(Person):
        pass

    class Student(Person):
        pass

    class SpeciesGroup(Thing):
        pass

    class Rat(Animal):
        pass

    class Country(Thing):
        pass

    class Institution(Thing):
        pass

    class ResearchCentre(Institution):
        pass

    class Prize(Thing):
        pass

    class NobelPrizeInPhysiologyOrMedicine(Prize):
        pass

    class Year(Thing):
        pass

    class BrainRegion(Thing):
        pass

    class CerebralCortex(BrainRegion):
        pass

    class EntorhinalCortex(BrainRegion):
        pass

    class DorsomedialEntorhinalCortex(EntorhinalCortex):
        pass

    class Hippocampus(BrainRegion):
        pass

    class Neuron(Thing):
        pass

    class GridCell(Neuron):
        pass

    class PlaceCell(Neuron):
        pass

    class Discovery(Thing):
        pass

    class PositioningSystem(Thing):
        pass

    class BrainPositioningSystem(PositioningSystem):
        pass

    class Hypothesis(Thing):
        pass

    class Mechanism(Thing):
        pass

    class SpatialPosition(Thing):
        pass

    class Space(Thing):
        pass

    class EuclideanSpace(Space):
        pass

    class Representation(Thing):
        pass

    class CognitiveRepresentation(Representation):
        pass

    class InformationType(Thing):
        pass

    class PositionInformation(InformationType):
        pass

    class DirectionInformation(InformationType):
        pass

    class ExperimentalStudy(Thing):
        pass

    class BehavioralCondition(Thing):
        pass

    class VisualizationMethod(Thing):
        pass

    class Device(Thing):
        pass

    class Electrode(Device):
        pass

    class Arena(Thing):
        pass

    class Environment(Thing):
        pass

    class ActionPotential(Thing):
        pass

    class SpatialFiringField(Thing):
        pass

    class PlaceField(SpatialFiringField):
        pass

    class Cluster(Thing):
        pass

    class GeometricPattern(Thing):
        pass

    class GridOfEquilateralTriangles(GeometricPattern):
        pass

    class RegularTrianglePattern(GeometricPattern):
        pass

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class locatedIn(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class studentOf(ObjectProperty):
        domain = [Student]
        range = [Researcher]

    class discoveredBy(ObjectProperty):
        domain = [Discovery]
        range = [Person]

    class discoveredInYear(ObjectProperty, FunctionalProperty):
        domain = [Discovery]
        range = [Year]

    class discoveredAtInstitution(ObjectProperty, FunctionalProperty):
        domain = [Discovery]
        range = [Institution]

    class contributedToDiscovery(ObjectProperty):
        domain = [Person]
        range = [Discovery]

    class concernsCellType(ObjectProperty):
        domain = [Thing]
        range = [Neuron]

    class awardedTo(ObjectProperty):
        domain = [Prize]
        range = [Person]

    class awardedFor(ObjectProperty, FunctionalProperty):
        domain = [Prize]
        range = [Discovery]

    class awardedInYear(ObjectProperty, FunctionalProperty):
        domain = [Prize]
        range = [Year]

    class foundInSpeciesGroup(ObjectProperty):
        domain = [GridCell]
        range = [SpeciesGroup]

    class allowsUnderstandingOf(ObjectProperty):
        domain = [GridCell]
        range = [SpatialPosition]

    class constitutesPartOfPositioningSystem(ObjectProperty):
        domain = [GridCell]
        range = [BrainPositioningSystem]

    class encodesRepresentation(ObjectProperty):
        domain = [GridCell]
        range = [CognitiveRepresentation]

    class representsSpace(ObjectProperty):
        domain = [CognitiveRepresentation]
        range = [Space]

    class suggestsHypothesis(ObjectProperty):
        domain = [Discovery]
        range = [Hypothesis]

    class suggestsMechanism(ObjectProperty):
        domain = [Discovery]
        range = [Mechanism]

    class basedOnUpdatedInformationAbout(ObjectProperty):
        domain = [Mechanism]
        range = [InformationType]

    class usesDevice(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Device]

    class implantedIn(ObjectProperty):
        domain = [Device]
        range = [BrainRegion]

    class performedOn(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Animal]

    class recordsInBrainRegion(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [BrainRegion]

    class takesPlaceIn(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Arena]

    class hasBehavioralCondition(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [BehavioralCondition]

    class typicallyRecordedIn(ObjectProperty):
        domain = [Neuron]
        range = [BrainRegion]

    class visualizedByPlotting(ObjectProperty):
        domain = [Neuron]
        range = [VisualizationMethod]

    class emits(ObjectProperty):
        domain = [Neuron]
        range = [ActionPotential]

    class hasSpatialFiringField(ObjectProperty):
        domain = [Neuron]
        range = [SpatialFiringField]

    class formsClusters(ObjectProperty):
        domain = [Neuron]
        range = [Cluster]

    class formsVerticesOf(ObjectProperty):
        domain = [Cluster]
        range = [GeometricPattern]

    class hasFiringPattern(ObjectProperty):
        domain = [Neuron]
        range = [GeometricPattern]

    class observedInEnvironment(ObjectProperty):
        domain = [Neuron]
        range = [Environment]

    class frequentlyHasPlaceFieldCount(DataProperty, FunctionalProperty):
        domain = [PlaceCell]
        range = [int]

    class canExhibitMultipleClusters(DataProperty, FunctionalProperty):
        domain = [PlaceCell]
        range = [bool]

    class hasPerceptibleRegularity(DataProperty, FunctionalProperty):
        domain = [GeometricPattern]
        range = [bool]

    class hasEqualDistancesFromNeighbors(DataProperty, FunctionalProperty):
        domain = [GeometricPattern]
        range = [bool]

    GridCell.is_a.append(foundInSpeciesGroup.some(SpeciesGroup))
    GridCell.is_a.append(allowsUnderstandingOf.some(SpatialPosition))
    GridCell.is_a.append(constitutesPartOfPositioningSystem.some(BrainPositioningSystem))
    GridCell.is_a.append(encodesRepresentation.some(CognitiveRepresentation))
    GridCell.is_a.append(hasSpatialFiringField.some(SpatialFiringField))
    GridCell.is_a.append(hasFiringPattern.some(RegularTrianglePattern))

    PlaceCell.is_a.append(hasSpatialFiringField.some(PlaceField))

    ExperimentalStudy.is_a.append(usesDevice.some(Electrode))
    ExperimentalStudy.is_a.append(performedOn.some(Rat))
    ExperimentalStudy.is_a.append(recordsInBrainRegion.some(DorsomedialEntorhinalCortex))
    ExperimentalStudy.is_a.append(takesPlaceIn.some(Arena))
    ExperimentalStudy.is_a.append(hasBehavioralCondition.some(BehavioralCondition))

    Year2005 = Year("Year2005")
    Year2005.label = "2005"

    Year2014 = Year("Year2014")
    Year2014.label = "2014"

    EdvardMoser = Researcher("EdvardMoser")
    EdvardMoser.label = "Edvard Moser"

    MayBrittMoser = Researcher("MayBrittMoser")
    MayBrittMoser.label = "May - Britt Moser"

    TorkelHafting = Student("TorkelHafting")
    TorkelHafting.label = "Torkel Hafting"

    MarianneFyhn = Student("MarianneFyhn")
    MarianneFyhn.label = "Marianne Fyhn"

    SturlaMolden = Student("SturlaMolden")
    SturlaMolden.label = "Sturla Molden"

    JohnOKeefe = Researcher("JohnOKeefe")
    JohnOKeefe.label = "John O'Keefe"

    CentreForTheBiologyOfMemory = ResearchCentre("CentreForTheBiologyOfMemory")
    CentreForTheBiologyOfMemory.label = [
        "Centre for the Biology of Memory",
        "CBM",
        "Centre for the Biology of Memory ( CBM )",
    ]

    Norway = Country("Norway")
    Norway.label = "Norway"
    CentreForTheBiologyOfMemory.locatedIn = [Norway]

    GridCellMention = GridCell("GridCellMention")
    GridCellMention.label = "grid cell"

    PlaceCellMention = PlaceCell("PlaceCellMention")
    PlaceCellMention.label = "place cell"

    ManySpecies = SpeciesGroup("ManySpecies")
    ManySpecies.label = "many species"

    PositionInSpace = SpatialPosition("PositionInSpace")
    PositionInSpace.label = "position in space"

    BrainPositioningSystemInTheBrain = BrainPositioningSystem("BrainPositioningSystemInTheBrain")
    BrainPositioningSystemInTheBrain.label = "a positioning system in the brain"

    EuclideanSpaceMention = EuclideanSpace("EuclideanSpaceMention")
    EuclideanSpaceMention.label = "Euclidean space"

    CognitiveRepresentationOfEuclideanSpace = CognitiveRepresentation("CognitiveRepresentationOfEuclideanSpace")
    CognitiveRepresentationOfEuclideanSpace.label = "a cognitive representation of Euclidean space"
    CognitiveRepresentationOfEuclideanSpace.representsSpace = [EuclideanSpaceMention]

    GridCellEuclideanSpaceHypothesis = Hypothesis("GridCellEuclideanSpaceHypothesis")
    GridCellEuclideanSpaceHypothesis.label = "these cells encode a cognitive representation of Euclidean space"
    GridCellEuclideanSpaceHypothesis.concernsCellType = [GridCellMention]

    DynamicComputationMechanism = Mechanism("DynamicComputationMechanism")
    DynamicComputationMechanism.label = (
        "dynamic computation of self - position based on continuously updated information "
        "about position and direction"
    )

    PositionInformationMention = PositionInformation("PositionInformationMention")
    PositionInformationMention.label = "position"

    DirectionInformationMention = DirectionInformation("DirectionInformationMention")
    DirectionInformationMention.label = "direction"
    DynamicComputationMechanism.basedOnUpdatedInformationAbout = [
        PositionInformationMention,
        DirectionInformationMention,
    ]

    GridCellDiscovery = Discovery("GridCellDiscovery")
    GridCellDiscovery.label = (
        "Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their "
        "students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the "
        "Biology of Memory ( CBM ) in Norway ."
    )
    GridCellDiscovery.discoveredBy = [
        EdvardMoser,
        MayBrittMoser,
        TorkelHafting,
        MarianneFyhn,
        SturlaMolden,
    ]
    GridCellDiscovery.discoveredInYear = Year2005
    GridCellDiscovery.discoveredAtInstitution = CentreForTheBiologyOfMemory
    GridCellDiscovery.concernsCellType = [GridCellMention]
    GridCellDiscovery.suggestsHypothesis = [GridCellEuclideanSpaceHypothesis]
    GridCellDiscovery.suggestsMechanism = [DynamicComputationMechanism]

    PositioningSystemDiscovery = Discovery("PositioningSystemDiscovery")
    PositioningSystemDiscovery.label = "their discoveries of cells that constitute a positioning system in the brain"
    PositioningSystemDiscovery.concernsCellType = [GridCellMention, PlaceCellMention]

    NobelPrize2014 = NobelPrizeInPhysiologyOrMedicine("NobelPrize2014")
    NobelPrize2014.label = "2014 Nobel Prize in Physiology or Medicine"
    NobelPrize2014.awardedTo = [EdvardMoser, MayBrittMoser, JohnOKeefe]
    NobelPrize2014.awardedFor = PositioningSystemDiscovery
    NobelPrize2014.awardedInYear = Year2014

    EdvardMoser.contributedToDiscovery = [GridCellDiscovery, PositioningSystemDiscovery]
    MayBrittMoser.contributedToDiscovery = [GridCellDiscovery, PositioningSystemDiscovery]
    TorkelHafting.contributedToDiscovery = [GridCellDiscovery]
    MarianneFyhn.contributedToDiscovery = [GridCellDiscovery]
    SturlaMolden.contributedToDiscovery = [GridCellDiscovery]
    JohnOKeefe.contributedToDiscovery = [PositioningSystemDiscovery]

    TorkelHafting.studentOf = [EdvardMoser, MayBrittMoser]
    MarianneFyhn.studentOf = [EdvardMoser, MayBrittMoser]
    SturlaMolden.studentOf = [EdvardMoser, MayBrittMoser]

    GridCellMention.foundInSpeciesGroup = [ManySpecies]
    GridCellMention.allowsUnderstandingOf = [PositionInSpace]
    GridCellMention.constitutesPartOfPositioningSystem = [BrainPositioningSystemInTheBrain]
    GridCellMention.encodesRepresentation = [CognitiveRepresentationOfEuclideanSpace]

    TypicalExperimentalStudy = ExperimentalStudy("TypicalExperimentalStudy")
    TypicalExperimentalStudy.label = "a typical experimental study"

    RecordingElectrode = Electrode("RecordingElectrode")
    RecordingElectrode.label = "an electrode capable of recording the activity of an individual neuron"

    RatSubject = Rat("RatSubject")
    RatSubject.label = "rat"

    CerebralCortexMention = CerebralCortex("CerebralCortexMention")
    CerebralCortexMention.label = "cerebral cortex"

    DorsomedialEntorhinalCortexMention = DorsomedialEntorhinalCortex("DorsomedialEntorhinalCortexMention")
    DorsomedialEntorhinalCortexMention.label = "dorsomedial entorhinal cortex"
    DorsomedialEntorhinalCortexMention.partOf = [CerebralCortexMention]

    OpenArena = Arena("OpenArena")
    OpenArena.label = "open arena"

    MovesAroundFreely = BehavioralCondition("MovesAroundFreely")
    MovesAroundFreely.label = "moves around freely"

    TypicalExperimentalStudy.usesDevice = [RecordingElectrode]
    TypicalExperimentalStudy.performedOn = [RatSubject]
    TypicalExperimentalStudy.recordsInBrainRegion = [DorsomedialEntorhinalCortexMention]
    TypicalExperimentalStudy.takesPlaceIn = [OpenArena]
    TypicalExperimentalStudy.hasBehavioralCondition = [MovesAroundFreely]
    RecordingElectrode.implantedIn = [CerebralCortexMention]
    GridCellMention.typicallyRecordedIn = [DorsomedialEntorhinalCortexMention]

    RatHeadDotPlot = VisualizationMethod("RatHeadDotPlot")
    RatHeadDotPlot.label = "a dot is placed at the location of the rat 's head every time the neuron emits an action potential"

    ActionPotentialMention = ActionPotential("ActionPotentialMention")
    ActionPotentialMention.label = "an action potential"

    GridCellSpatialFiringFields = SpatialFiringField("GridCellSpatialFiringFields")
    GridCellSpatialFiringFields.label = "spatial firing fields"

    SmallClusters = Cluster("SmallClusters")
    SmallClusters.label = "small clusters"

    GridOfEquilateralTrianglesMention = GridOfEquilateralTriangles("GridOfEquilateralTrianglesMention")
    GridOfEquilateralTrianglesMention.label = "a grid of equilateral triangles"
    GridOfEquilateralTrianglesMention.hasPerceptibleRegularity = True

    RegularTrianglePatternMention = RegularTrianglePattern("RegularTrianglePatternMention")
    RegularTrianglePatternMention.label = "This regular triangle - pattern"
    RegularTrianglePatternMention.hasPerceptibleRegularity = True
    RegularTrianglePatternMention.hasEqualDistancesFromNeighbors = True

    GridCellMention.visualizedByPlotting = [RatHeadDotPlot]
    PlaceCellMention.visualizedByPlotting = [RatHeadDotPlot]
    GridCellMention.emits = [ActionPotentialMention]
    PlaceCellMention.emits = [ActionPotentialMention]
    GridCellMention.hasSpatialFiringField = [GridCellSpatialFiringFields]
    GridCellMention.formsClusters = [SmallClusters]
    GridCellMention.hasFiringPattern = [GridOfEquilateralTrianglesMention, RegularTrianglePatternMention]
    SmallClusters.formsVerticesOf = [GridOfEquilateralTrianglesMention]

    RatHippocampus = Hippocampus("RatHippocampus")
    RatHippocampus.label = "rat hippocampus"

    PlaceFieldMention = PlaceField("PlaceFieldMention")
    PlaceFieldMention.label = 'one " place field "'

    GivenEnvironment = Environment("GivenEnvironment")
    GivenEnvironment.label = "a given environment"

    MultipleClusters = Cluster("MultipleClusters")
    MultipleClusters.label = "multiple clusters"

    NoPerceptibleRegularity = GeometricPattern("NoPerceptibleRegularity")
    NoPerceptibleRegularity.label = "no perceptible regularity in their arrangement"
    NoPerceptibleRegularity.hasPerceptibleRegularity = False

    PlaceCellMention.partOf = [RatHippocampus]
    PlaceCellMention.hasSpatialFiringField = [PlaceFieldMention]
    PlaceCellMention.formsClusters = [SmallClusters, MultipleClusters]
    PlaceCellMention.hasFiringPattern = [NoPerceptibleRegularity]
    PlaceCellMention.observedInEnvironment = [GivenEnvironment]
    PlaceCellMention.frequentlyHasPlaceFieldCount = 1
    PlaceCellMention.canExhibitMultipleClusters = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
