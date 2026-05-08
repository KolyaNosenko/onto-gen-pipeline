"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What is a grid cell?
2. In which species’ brains are grid cells found?
3. What function do grid cells serve in spatial understanding?
4. Who discovered grid cells?
5. In what year were grid cells discovered?
6. Where were grid cells discovered?
7. Which Nobel Prize was awarded for discoveries related to grid cells?
8. Who shared the 2014 Nobel Prize in Physiology or Medicine for discoveries related to positioning cells in the brain?
9. What hypothesis was proposed based on the regular arrangement of grid cell firing fields?
10. What mechanism for self-position computation was suggested by the discovery of grid cells?
11. In which brain region are grid cell recordings typically made in rats?
12. What type of experimental setup is used to study grid cell activity?
13. What happens when rat head positions are marked each time a grid cell fires?
14. What geometric pattern do grid cell firing clusters form?
15. How do grid cells differ from place cells in their spatial firing patterns?
16. Where are place cells typically located in the rat brain?
17. How many place fields are typically seen for a place cell in a given environment?
18. What distinguishes grid cells from other cells that show spatial firing?
19. What does the regular triangle-pattern of grid cell firing suggest about spatial coding?
20. How are grid cell firing fields arranged relative to their neighbors?
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
    class Person(Thing):
        pass

    class Organization(Thing):
        pass

    class Place(Thing):
        pass

    class Country(Place):
        pass

    class Year(Thing):
        pass

    class Prize(Thing):
        pass

    class NobelPrize(Prize):
        pass

    class Discovery(Thing):
        pass

    class Hypothesis(Thing):
        pass

    class Mechanism(Thing):
        pass

    class Information(Thing):
        pass

    class PositionAndDirectionInformation(Information):
        pass

    class ContinuouslyUpdatedPositionAndDirectionInformation(PositionAndDirectionInformation):
        pass

    class Space(Thing):
        pass

    class EuclideanSpace(Space):
        pass

    class Position(Thing):
        pass

    class PositionInSpace(Position):
        pass

    class Direction(Thing):
        pass

    class Representation(Thing):
        pass

    class CognitiveRepresentation(Representation):
        pass

    class PositioningSystem(Thing):
        pass

    class Brain(Thing):
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

    class Species(Thing):
        pass

    class Rat(Species):
        pass

    class Cell(Thing):
        pass

    class Neuron(Cell):
        pass

    class SpatialFiringCell(Neuron):
        pass

    class Pattern(Thing):
        pass

    class SpatialFiringPattern(Pattern):
        pass

    class RegularTrianglePattern(SpatialFiringPattern):
        pass

    class IrregularSpatialFiringPattern(SpatialFiringPattern):
        pass

    class GridPattern(Pattern):
        pass

    class EquilateralTriangleGrid(GridPattern):
        pass

    class FiringFieldArrangement(Thing):
        pass

    class EqualDistanceNeighbourArrangement(FiringFieldArrangement):
        pass

    class Cluster(Thing):
        pass

    class Dot(Thing):
        pass

    class PlaceField(Thing):
        pass

    class ActionPotential(Thing):
        pass

    class Arena(Thing):
        pass

    class OpenArena(Arena):
        pass

    class ExperimentalStudy(Thing):
        pass

    class Electrode(Thing):
        pass

    class GridCellDiscovery(Discovery):
        pass

    class TypicalGridCellStudy(ExperimentalStudy):
        pass

    class EuclideanSpaceHypothesis(Hypothesis):
        pass

    class DynamicSelfPositionComputationMechanism(Mechanism):
        pass

    class GridCell(SpatialFiringCell):
        pass

    class PlaceCell(SpatialFiringCell):
        pass

    class about(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class basedOn(ObjectProperty):
        domain = [Mechanism]
        range = [Information]

    class ledTo(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class discoveredBy(ObjectProperty):
        domain = [Discovery]
        range = [Person]

    class discoveredInYear(ObjectProperty):
        domain = [Discovery]
        range = [Year]

    class discoveredAt(ObjectProperty):
        domain = [Discovery]
        range = [Place, Organization]

    class forDiscovery(ObjectProperty):
        domain = [Prize]
        range = [Discovery]

    class awardedTo(ObjectProperty):
        domain = [Prize]
        range = [Person]

    class awardYear(ObjectProperty, FunctionalProperty):
        domain = [Prize]
        range = [Year]

    class studentOf(ObjectProperty):
        domain = [Person]
        range = [Person]

    class sharedWith(ObjectProperty, SymmetricProperty):
        domain = [Person]
        range = [Person]

    class foundInBrainOf(ObjectProperty):
        domain = [Cell]
        range = [Species]

    class allowsUnderstandingOf(ObjectProperty):
        domain = [GridCell]
        range = [PositionInSpace]

    class encodes(ObjectProperty):
        domain = [GridCell]
        range = [CognitiveRepresentation]

    class constitutes(ObjectProperty):
        domain = [Cell]
        range = [PositioningSystem]

    class suggests(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class capableOfRecordingActivityOf(ObjectProperty):
        domain = [Electrode]
        range = [Neuron]

    class implantedIn(ObjectProperty):
        domain = [Electrode]
        range = [BrainRegion]

    class hasSubject(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Species]

    class usesInstrument(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Electrode]

    class takesPlaceIn(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [Arena]

    class recordsIn(ObjectProperty):
        domain = [ExperimentalStudy]
        range = [BrainRegion]

    class movesFreelyIn(ObjectProperty):
        domain = [Rat]
        range = [Arena]

    class emits(ObjectProperty):
        domain = [Neuron]
        range = [ActionPotential]

    class buildsUpToForm(ObjectProperty):
        domain = [Dot]
        range = [Cluster]

    class formsVerticesOf(ObjectProperty):
        domain = [Cluster]
        range = [GridPattern]

    class distinguishedBy(ObjectProperty):
        domain = [Cell]
        range = [Pattern]

    class showsSpatialFiring(ObjectProperty):
        domain = [Cell]
        range = [SpatialFiringPattern]

    class locatedIn(ObjectProperty):
        domain = [PlaceCell]
        range = [BrainRegion]

    class hasFiringFieldArrangement(ObjectProperty):
        domain = [GridCell]
        range = [FiringFieldArrangement]

    class hasTypicalPlaceFieldCount(DataProperty, FunctionalProperty):
        domain = [PlaceCell]
        range = [int]

    class yearValue(DataProperty, FunctionalProperty):
        domain = [Year]
        range = [int]

    EdvardMoser = Person("EdvardMoser")
    EdvardMoser.label = "Edvard Moser"

    MayBrittMoser = Person("MayBrittMoser")
    MayBrittMoser.label = "May - Britt Moser"

    TorkelHafting = Person("TorkelHafting")
    TorkelHafting.label = "Torkel Hafting"

    MarianneFyhn = Person("MarianneFyhn")
    MarianneFyhn.label = "Marianne Fyhn"

    SturlaMolden = Person("SturlaMolden")
    SturlaMolden.label = "Sturla Molden"

    JohnOKeefe = Person("JohnOKeefe")
    JohnOKeefe.label = "John O'Keefe"

    CentreForTheBiologyOfMemory = Organization("CentreForTheBiologyOfMemory")
    CentreForTheBiologyOfMemory.label = [
        "Centre for the Biology of Memory ( CBM )",
        "CBM",
    ]

    Norway = Country("Norway")
    Norway.label = "Norway"

    Year2005 = Year("Year2005")
    Year2005.label = "2005"
    Year2005.yearValue = 2005

    Year2014 = Year("Year2014")
    Year2014.label = "2014"
    Year2014.yearValue = 2014

    NobelPrize2014 = NobelPrize("NobelPrize2014")
    NobelPrize2014.label = "2014 Nobel Prize in Physiology or Medicine"
    NobelPrize2014.awardYear = Year2014
    NobelPrize2014.awardedTo = [
        EdvardMoser,
        MayBrittMoser,
        TorkelHafting,
        MarianneFyhn,
        SturlaMolden,
        JohnOKeefe,
    ]

    TorkelHafting.studentOf = [EdvardMoser, MayBrittMoser]
    MarianneFyhn.studentOf = [EdvardMoser, MayBrittMoser]
    SturlaMolden.studentOf = [EdvardMoser, MayBrittMoser]

    Neuron.is_a.append(emits.some(ActionPotential))
    SpatialFiringCell.is_a.append(showsSpatialFiring.some(SpatialFiringPattern))
    CognitiveRepresentation.is_a.append(about.some(EuclideanSpace))
    PositionAndDirectionInformation.is_a.extend(
        [about.some(Position), about.some(Direction)]
    )
    RegularTrianglePattern.is_a.append(ledTo.some(EuclideanSpaceHypothesis))
    EuclideanSpaceHypothesis.is_a.append(about.some(EuclideanSpace))
    DynamicSelfPositionComputationMechanism.is_a.append(
        basedOn.some(ContinuouslyUpdatedPositionAndDirectionInformation)
    )
    GridCellDiscovery.is_a.extend(
        [
            discoveredBy.value(EdvardMoser),
            discoveredBy.value(MayBrittMoser),
            discoveredBy.value(TorkelHafting),
            discoveredBy.value(MarianneFyhn),
            discoveredBy.value(SturlaMolden),
            discoveredInYear.value(Year2005),
            discoveredAt.value(CentreForTheBiologyOfMemory),
            discoveredAt.value(Norway),
            suggests.some(DynamicSelfPositionComputationMechanism),
        ]
    )
    GridCell.is_a.extend(
        [
            foundInBrainOf.some(Species),
            allowsUnderstandingOf.some(PositionInSpace),
            constitutes.some(PositioningSystem),
            encodes.some(CognitiveRepresentation),
            distinguishedBy.some(RegularTrianglePattern),
            hasFiringFieldArrangement.some(EqualDistanceNeighbourArrangement),
        ]
    )
    PlaceCell.is_a.extend(
        [
            locatedIn.some(Hippocampus),
            hasTypicalPlaceFieldCount.value(1),
            distinguishedBy.some(IrregularSpatialFiringPattern),
        ]
    )
    Cluster.is_a.append(formsVerticesOf.some(EquilateralTriangleGrid))
    Dot.is_a.append(buildsUpToForm.some(Cluster))
    Electrode.is_a.extend(
        [
            capableOfRecordingActivityOf.some(Neuron),
            implantedIn.some(CerebralCortex),
        ]
    )
    Rat.is_a.append(movesFreelyIn.some(OpenArena))
    TypicalGridCellStudy.is_a.extend(
        [
            hasSubject.some(Rat),
            usesInstrument.some(Electrode),
            recordsIn.some(DorsomedialEntorhinalCortex),
            takesPlaceIn.some(OpenArena),
        ]
    )
    NobelPrize2014.is_a.append(forDiscovery.some(GridCellDiscovery))



graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
