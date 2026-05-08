"""
=== TASK INPUT ===
Source text:
A grid cell is a type of neuron in the brains of many species that allows them to understand their position in space . Grid cells were discovered in 2005 by Edvard Moser , May - Britt Moser and their students Torkel Hafting , Marianne Fyhn and Sturla Molden at the Centre for the Biology of Memory ( CBM ) in Norway . They were awarded the 2014 Nobel Prize in Physiology or Medicine together with John O'Keefe for their discoveries of cells that constitute a positioning system in the brain . The arrangement of spatial firing fields all at equal distances from their neighbors led to a hypothesis that these cells encode a cognitive representation of Euclidean space . The discovery also suggested a mechanism for dynamic computation of self - position based on continuously updated information about position and direction . In a typical experimental study , an electrode capable of recording the activity of an individual neuron is implanted in the cerebral cortex of a rat , in a section called the dorsomedial entorhinal cortex , and recordings are made as the rat moves around freely in an open arena . For a grid cell , if a dot is placed at the location of the rat 's head every time the neuron emits an action potential , then as illustrated in the adjoining figure , these dots build up over time to form a set of small clusters , and the clusters form the vertices of a grid of equilateral triangles . This regular triangle - pattern is what distinguishes grid cells from other types of cells that show spatial firing . By contrast , if a place cell from the rat hippocampus is examined in the same way ( i.e. , by placing a dot at the location of the rat 's head whenever the cell emits an action potential ) , then the dots build up to form small clusters , but frequently there is only one cluster ( one " place field " ) in a given environment , and even when multiple clusters are seen , there is no perceptible regularity in their arrangement .

1. What is a grid cell and what is its function in the brain?

2. Who discovered grid cells and in what year?

3. Which scientists were awarded the Nobel Prize in Physiology or Medicine for discoveries related to grid cells?

4. What is the spatial firing pattern of grid cells?

5. In which brain region are grid cells typically located?

6. How are grid cells experimentally studied and recorded?

7. What is the geometric arrangement of grid cell firing fields?

8. How do grid cells differ from place cells in terms of spatial firing patterns?

9. What cognitive representation do grid cells encode?

10. What mechanism do grid cells provide for computing self-position?

11. In which species have grid cells been discovered?

12. What is the role of electrodes in grid cell research?

13. How can the activity of a grid cell be visualized during experimental studies?

14. What is the relationship between grid cells and a positioning system in the brain?

15. What distinguishes the firing pattern of grid cells from other spatially-firing neurons?
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
    # === Classes ===
    
    class Neuron(Thing):
        pass
    
    class Scientist(Thing):
        pass
    
    class BrainRegion(Thing):
        pass
    
    class CerebralCortex(BrainRegion):
        pass
    
    class DorsomedialEntorhinalCortex(CerebralCortex):
        pass
    
    class Hippocampus(BrainRegion):
        pass
    
    class ResearchCentre(Thing):
        pass
    
    class Country(Thing):
        pass
    
    class Prize(Thing):
        pass
    
    class NobelPrize(Prize):
        pass
    
    class Species(Thing):
        pass
    
    class Rat(Species):
        pass
    
    class SpatialFiringPattern(Thing):
        pass
    
    class Grid(Thing):
        pass
    
    class EquilateralTriangleGrid(Grid):
        pass
    
    class PlaceField(Thing):
        pass
    
    class CognitiveRepresentation(Thing):
        pass
    
    class EuclideanSpace(CognitiveRepresentation):
        pass
    
    class PositioningSystem(Thing):
        pass
    
    class Electrode(Thing):
        pass
    
    # === Object Properties ===
    
    class discoveredBy(ObjectProperty):
        domain = [Neuron]
        range = [Scientist]
    
    class discoveryLocation(ObjectProperty):
        domain = [Neuron]
        range = [ResearchCentre]
    
    class receivedPrize(ObjectProperty):
        domain = [Scientist]
        range = [Prize]
    
    class centreLocatedIn(ObjectProperty):
        domain = [ResearchCentre]
        range = [Country]
    
    class locatedIn(ObjectProperty):
        domain = [Neuron]
        range = [BrainRegion]
    
    class hasSpatialPattern(ObjectProperty):
        domain = [Neuron]
        range = [SpatialFiringPattern]
    
    class patternGeometry(ObjectProperty):
        domain = [SpatialFiringPattern]
        range = [Grid]
    
    class encodes(ObjectProperty):
        domain = [Neuron]
        range = [CognitiveRepresentation]
    
    class foundInSpecies(ObjectProperty):
        domain = [Neuron]
        range = [Species]
    
    class implantedIn(ObjectProperty):
        domain = [Electrode]
        range = [BrainRegion]
    
    class recordsFrom(ObjectProperty):
        domain = [Electrode]
        range = [Neuron]
    
    class constitutesPositioningSystem(ObjectProperty):
        domain = [Neuron]
        range = [PositioningSystem]
    
    class hasFiringFields(ObjectProperty):
        domain = [Neuron]
        range = [PlaceField]
    
    # === Data Properties ===
    
    class discoveredInYear(DataProperty):
        domain = [Neuron]
        range = [int]
    
    class awardedInYear(DataProperty):
        domain = [Prize]
        range = [int]
    
    # === Specialized neuron types with constraints ===
    
    class GridCell(Neuron):
        is_a = [
            locatedIn.some(DorsomedialEntorhinalCortex),
            encodes.some(EuclideanSpace),
            foundInSpecies.some(Rat),
            constitutesPositioningSystem.some(PositioningSystem),
        ]
    
    class PlaceCell(Neuron):
        is_a = [locatedIn.some(Hippocampus), hasFiringFields.some(PlaceField)]
    
    class ExperimentalElectrode(Electrode):
        is_a = [
            implantedIn.some(DorsomedialEntorhinalCortex),
            recordsFrom.some(GridCell),
        ]
    
    # === Scientist instances ===
    
    edvardMoser = Scientist("EdvardMoser")
    edvardMoser.label = "Edvard Moser"
    
    mayBrittMoser = Scientist("MayBrittMoser")
    mayBrittMoser.label = "May - Britt Moser"
    
    torkelHafting = Scientist("TorkelHafting")
    torkelHafting.label = "Torkel Hafting"
    
    marianneFyhn = Scientist("MarianneFyhn")
    marianneFyhn.label = "Marianne Fyhn"
    
    sturlaMolden = Scientist("SturlaMolden")
    sturlaMolden.label = "Sturla Molden"
    
    johnOKeefe = Scientist("JohnOKeefe")
    johnOKeefe.label = "John O'Keefe"
    
    # === Institution and location instances ===
    
    cbm = ResearchCentre("CentreForBiologyOfMemory")
    cbm.label = "Centre for the Biology of Memory"
    
    norway = Country("Norway")
    
    # === Prize instance ===
    
    nobelPrize = NobelPrize("NobelPrizePhysiologyMedicine")
    nobelPrize.label = "Nobel Prize in Physiology or Medicine"
    
    # === Set up instance relationships ===
    
    cbm.centreLocatedIn = [norway]
    nobelPrize.awardedInYear = [2014]
    
    for scientist in [edvardMoser, mayBrittMoser, torkelHafting, marianneFyhn, sturlaMolden, johnOKeefe]:
        scientist.receivedPrize = [nobelPrize]
    
    # === Grid cell instance to hold discovery facts ===
    
    gridCellConcept = GridCell("GridCellConcept")
    gridCellConcept.label = "grid cells"
    gridCellConcept.discoveredBy = [edvardMoser, mayBrittMoser, torkelHafting, marianneFyhn, sturlaMolden]
    gridCellConcept.discoveredInYear = [2005]
    gridCellConcept.discoveryLocation = [cbm]
    
    # === Spatial firing pattern for grid cells ===
    
    triangularPattern = SpatialFiringPattern("TriangularPattern")
    triangularPattern.label = "equilateral triangle firing pattern"
    triangularPattern.patternGeometry = [EquilateralTriangleGrid("EquilateralTriangleGridInstance")]
    
    gridCellConcept.hasSpatialPattern = [triangularPattern]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
