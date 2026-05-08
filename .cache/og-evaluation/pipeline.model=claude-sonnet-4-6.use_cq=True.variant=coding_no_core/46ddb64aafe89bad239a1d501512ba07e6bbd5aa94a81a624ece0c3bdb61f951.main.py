"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What type of neuron is a grid cell?
2. In which year were grid cells discovered?
3. Who discovered grid cells?
4. At which institution were grid cells discovered?
5. In which country was the discovery of grid cells made?
6. Which Nobel Prize were the discoverers of grid cells awarded?
7. In which year was the Nobel Prize awarded to the discoverers of grid cells?
8. Which category of Nobel Prize did the grid cell discoverers receive?
9. Who shared the Nobel Prize with the grid cell discoverers?
10. What type of spatial firing pattern do grid cells form?
11. What geometric shape do the clusters of grid cell firing fields form?
12. What brain region is targeted when recording grid cell activity in rats?
13. What method is used to record the activity of individual neurons in experimental studies?
14. What distinguishes grid cells from other spatially firing cells?
15. How does the firing pattern of a place cell differ from that of a grid cell?
16. In which brain region are place cells found?
17. What cognitive representation do grid cells encode?
18. What type of computation do grid cells support based on position and direction information?
19. What animal is commonly used in experimental studies of grid cells?
20. What is the relationship between grid cell firing fields and their neighboring fields?
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
    # --- Entity classes ---

    class Neuron(Thing): pass
    class GridCell(Neuron): pass
    class PlaceCell(Neuron): pass

    class Person(Thing): pass
    class Researcher(Person): pass
    class Student(Researcher): pass

    class Institution(Thing): pass
    class ResearchInstitution(Institution): pass

    class Country(Thing): pass

    class Award(Thing): pass
    class NobelPrize(Award): pass

    class BrainRegion(Thing): pass
    class CerebralCortex(BrainRegion): pass
    class EntorhinalCortex(CerebralCortex): pass
    class Hippocampus(BrainRegion): pass

    class Animal(Thing): pass

    class CognitiveRepresentation(Thing): pass
    class EuclideanSpace(CognitiveRepresentation): pass

    class SpatialFiringPattern(Thing): pass
    class EquilateralTrianglePattern(SpatialFiringPattern): pass

    class Computation(Thing): pass

    class RecordingInstrument(Thing): pass
    class Electrode(RecordingInstrument): pass

    # --- Properties ---

    class discoveredBy(ObjectProperty):
        domain = [GridCell]
        range  = [Person]

    class discoveredAt(ObjectProperty):
        domain = [GridCell]
        range  = [ResearchInstitution]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Institution]
        range  = [Country]

    class awardedPrize(ObjectProperty):
        domain = [Researcher]
        range  = [Award]

    class sharedPrizeWith(ObjectProperty, SymmetricProperty):
        domain = [Researcher]
        range  = [Researcher]

    class encodesRepresentation(ObjectProperty):
        domain = [GridCell]
        range  = [CognitiveRepresentation]

    class formsFiringPattern(ObjectProperty):
        domain = [Neuron]
        range  = [SpatialFiringPattern]

    class recordedInRegion(ObjectProperty):
        domain = [Neuron]
        range  = [BrainRegion]

    class foundInRegion(ObjectProperty):
        domain = [Neuron]
        range  = [BrainRegion]

    class usesRecordingInstrument(ObjectProperty):
        domain = [Neuron]
        range  = [RecordingInstrument]

    class supportsComputation(ObjectProperty):
        domain = [GridCell]
        range  = [Computation]

    class usedInExperiment(ObjectProperty):
        domain = [Animal]
        range  = [Thing]

    class discoveryYear(DataProperty, FunctionalProperty):
        domain = [GridCell]
        range  = [int]

    class prizeYear(DataProperty, FunctionalProperty):
        domain = [Award]
        range  = [int]

    class prizeCategory(DataProperty, FunctionalProperty):
        domain = [Award]
        range  = [str]

    class hasAbbreviation(DataProperty, FunctionalProperty):
        domain = [Institution]
        range  = [str]

    class firingFieldsAtEqualDistances(DataProperty, FunctionalProperty):
        domain = [GridCell]
        range  = [bool]

    # --- Class restrictions ---

    GridCell.is_a.append(discoveredBy.some(Researcher))
    GridCell.is_a.append(encodesRepresentation.some(CognitiveRepresentation))
    GridCell.is_a.append(formsFiringPattern.some(EquilateralTrianglePattern))
    GridCell.is_a.append(recordedInRegion.some(EntorhinalCortex))

    PlaceCell.is_a.append(foundInRegion.some(Hippocampus))

    # --- Individuals ---

    # Country
    NorwayInst = Country("NorwayInst")
    NorwayInst.label = "Norway"

    # Research institution
    CBMInst = ResearchInstitution("CBMInst")
    CBMInst.label = "Centre for the Biology of Memory"
    CBMInst.hasAbbreviation = "CBM"
    CBMInst.locatedIn = [NorwayInst]

    # Researchers
    EdvardMoser = Researcher("EdvardMoser")
    EdvardMoser.label = "Edvard Moser"

    MayBrittMoser = Researcher("MayBrittMoser")
    MayBrittMoser.label = "May-Britt Moser"

    TorkelHafting = Student("TorkelHafting")
    TorkelHafting.label = "Torkel Hafting"

    MarianneFyhn = Student("MarianneFyhn")
    MarianneFyhn.label = "Marianne Fyhn"

    SturlaMolden = Student("SturlaMolden")
    SturlaMolden.label = "Sturla Molden"

    JohnOKeefe = Researcher("JohnOKeefe")
    JohnOKeefe.label = "John O'Keefe"

    # Nobel Prize
    NobelPrize2014Physiology = NobelPrize("NobelPrize2014Physiology")
    NobelPrize2014Physiology.label = "2014 Nobel Prize in Physiology or Medicine"
    NobelPrize2014Physiology.prizeYear = 2014
    NobelPrize2014Physiology.prizeCategory = "Physiology or Medicine"

    # Brain regions
    CerebralCortexInst = CerebralCortex("CerebralCortexInst")
    CerebralCortexInst.label = "cerebral cortex"

    DorsomedialEntorhinalCortexInst = EntorhinalCortex("DorsomedialEntorhinalCortexInst")
    DorsomedialEntorhinalCortexInst.label = "dorsomedial entorhinal cortex"

    HippocampusInst = Hippocampus("HippocampusInst")
    HippocampusInst.label = "hippocampus"

    # Cognitive representation
    EuclideanSpaceInst = EuclideanSpace("EuclideanSpaceInst")
    EuclideanSpaceInst.label = "Euclidean space"

    # Spatial firing pattern
    EquilateralTrianglePatternInst = EquilateralTrianglePattern("EquilateralTrianglePatternInst")
    EquilateralTrianglePatternInst.label = "equilateral triangle grid pattern"

    # Computation
    SelfPositionComputationInst = Computation("SelfPositionComputationInst")
    SelfPositionComputationInst.label = "dynamic computation of self-position"

    # Recording instrument
    ElectrodeInst = Electrode("ElectrodeInst")
    ElectrodeInst.label = "electrode"

    # Animal
    RatInst = Animal("RatInst")
    RatInst.label = "rat"

    # Grid cell concept (the neuron type as a named individual distinct from the class)
    GridCellConceptInst = GridCell("GridCellConceptInst")
    GridCellConceptInst.label = "grid cell"
    GridCellConceptInst.discoveredBy = [EdvardMoser, MayBrittMoser, TorkelHafting, MarianneFyhn, SturlaMolden]
    GridCellConceptInst.discoveredAt = [CBMInst]
    GridCellConceptInst.discoveryYear = 2005
    GridCellConceptInst.encodesRepresentation = [EuclideanSpaceInst]
    GridCellConceptInst.formsFiringPattern = [EquilateralTrianglePatternInst]
    GridCellConceptInst.recordedInRegion = [DorsomedialEntorhinalCortexInst]
    GridCellConceptInst.supportsComputation = [SelfPositionComputationInst]
    GridCellConceptInst.usesRecordingInstrument = [ElectrodeInst]
    GridCellConceptInst.firingFieldsAtEqualDistances = True

    # Place cell concept
    PlaceCellConceptInst = PlaceCell("PlaceCellConceptInst")
    PlaceCellConceptInst.label = "place cell"
    PlaceCellConceptInst.foundInRegion = [HippocampusInst]

    # Nobel Prize recipients
    EdvardMoser.awardedPrize = [NobelPrize2014Physiology]
    MayBrittMoser.awardedPrize = [NobelPrize2014Physiology]
    JohnOKeefe.awardedPrize = [NobelPrize2014Physiology]

    # Shared-prize relationships (symmetric)
    EdvardMoser.sharedPrizeWith = [MayBrittMoser, JohnOKeefe]
    MayBrittMoser.sharedPrizeWith = [JohnOKeefe]

    # Rat used in experimental studies
    RatInst.usedInExperiment = [GridCellConceptInst]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
