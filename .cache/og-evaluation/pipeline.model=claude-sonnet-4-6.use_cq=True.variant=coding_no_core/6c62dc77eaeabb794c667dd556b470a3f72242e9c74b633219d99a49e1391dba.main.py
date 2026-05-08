"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. What is the location of Southwood National Park?
2. How far is Southwood National Park from Brisbane?
3. In which state of Australia is Southwood National Park located?
4. What type of forest is conserved in Southwood National Park?
5. What vegetation types are found in Southwood National Park?
6. How many species of birds have been recorded in Southwood National Park?
7. What plant species grow in Southwood National Park?
8. What is a gilgai and how is it formed?
9. Which indigenous people are the traditional owners of the land where Southwood National Park is located?
10. Which explorers passed through the area of Southwood National Park?
11. What was the former name of Southwood National Park?
12. When did Southwood become a national park?
13. Which wildlife species are found near the inland limit of their range in Southwood National Park?
14. What is the geographical region where Southwood National Park is situated?
15. What soil type is responsible for the formation of gilgais in Southwood National Park?
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
    # ── Entity classes ──────────────────────────────────────────────────────

    # Places
    class Place(Thing): pass
    class AdministrativeDivision(Place): pass
    class Country(AdministrativeDivision): pass
    class State(AdministrativeDivision): pass
    class City(Place): pass
    class Region(Place): pass
    class SemiAridRegion(Region): pass
    class NationalPark(Place): pass

    # Species
    class Species(Thing): pass
    class PlantSpecies(Species): pass
    class WildlifeSpecies(Species): pass
    class BirdSpecies(WildlifeSpecies): pass

    # Vegetation
    class VegetationType(Thing): pass
    class ForestType(VegetationType): pass

    # Geological
    class GeologicalFeature(Thing): pass
    class Gilgai(GeologicalFeature): pass
    class SoilType(Thing): pass
    class HeavyClaySoil(SoilType): pass

    # People
    class Person(Thing): pass
    class Explorer(Person): pass
    class IndigenousPeople(Thing): pass

    # ── Object properties ───────────────────────────────────────────────────

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class locatedInRegion(ObjectProperty):
        domain = [NationalPark]
        range = [Region]

    class nearCity(ObjectProperty):
        domain = [NationalPark]
        range = [City]

    class conservesForestType(ObjectProperty):
        domain = [NationalPark]
        range = [ForestType]

    class hasPlantSpecies(ObjectProperty):
        domain = [NationalPark]
        range = [PlantSpecies]

    class hasWildlife(ObjectProperty):
        domain = [NationalPark]
        range = [WildlifeSpecies]

    class containsGilgai(ObjectProperty):
        domain = [NationalPark]
        range = [Gilgai]

    class formedInSoilType(ObjectProperty):
        domain = [Gilgai]
        range = [SoilType]

    class traditionalLandOf(ObjectProperty):
        domain = [NationalPark]
        range = [IndigenousPeople]

    class exploredBy(ObjectProperty):
        domain = [Place]
        range = [Explorer]

    class nearInlandRangeLimit(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    # ── Data properties ─────────────────────────────────────────────────────

    class distanceFromBrisbaneKm(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class directionFromBrisbane(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [str]

    class birdSpeciesCount(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class formerName(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [str]

    class becameNationalParkYear(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class formationProcess(DataProperty, FunctionalProperty):
        domain = [Gilgai]
        range = [str]

    # ── Class restrictions ──────────────────────────────────────────────────

    # Every Gilgai is formed in some HeavyClaySoil (CQ 8, 15)
    Gilgai.is_a.append(formedInSoilType.some(HeavyClaySoil))

    # ── Named individuals ───────────────────────────────────────────────────

    # Countries / states / cities
    australia = Country("Australia")
    australia.label = "Australia"

    queensland = State("Queensland")
    queensland.label = "Queensland"
    queensland.locatedIn = [australia]

    brisbane = City("Brisbane")
    brisbane.label = "Brisbane"
    brisbane.locatedIn = [queensland]

    darling_downs = Region("DarlingDowns")
    darling_downs.label = "western Darling Downs"
    darling_downs.locatedIn = [queensland]

    # The national park (CQ 1-4, 6, 11, 12, 14)
    southwood = NationalPark("Southwood")
    southwood.label = "Southwood"
    southwood.locatedIn = [queensland]
    southwood.locatedInRegion = [darling_downs]
    southwood.nearCity = [brisbane]
    southwood.distanceFromBrisbaneKm = 288
    southwood.directionFromBrisbane = "west"
    southwood.birdSpeciesCount = 92
    southwood.formerName = "Wild Horse Paradise"
    southwood.becameNationalParkYear = 1970

    # Forest type conserved in the park (CQ 4)
    brigalow_belah_forest = ForestType("BrigalowBelahForest")
    brigalow_belah_forest.label = "Brigalow-belah forest"
    southwood.conservesForestType = [brigalow_belah_forest]

    # Plant species (CQ 5, 7)
    cypress_pine = PlantSpecies("CypressPine")
    cypress_pine.label = "Cypress pine"

    poplar_box = PlantSpecies("PoplarBox")
    poplar_box.label = "Poplar box"

    wilga_bush = PlantSpecies("WilgaBush")
    wilga_bush.label = "Wilga bush"

    false_sandalwood = PlantSpecies("FalseSandalwood")
    false_sandalwood.label = "False sandalwood"

    western_teatree = PlantSpecies("WesternTeatree")
    western_teatree.label = "Western teatree"

    southwood.hasPlantSpecies = [
        cypress_pine, poplar_box, wilga_bush, false_sandalwood, western_teatree,
    ]

    # Bird species near inland range limit (CQ 13)
    wonga_pigeon = BirdSpecies("WongaPigeon")
    wonga_pigeon.label = "Wonga pigeon"
    wonga_pigeon.nearInlandRangeLimit = [southwood]
    southwood.hasWildlife = [wonga_pigeon]

    # Soil type and gilgais (CQ 8, 15)
    heavy_clay_soil = HeavyClaySoil("HeavyClaySoilInd")
    heavy_clay_soil.label = "heavy clay soils"

    gilgais = Gilgai("SouthwoodGilgais")
    gilgais.label = "gilgais"
    gilgais.formedInSoilType = [heavy_clay_soil]
    gilgais.formationProcess = "constant wetting and drying of heavy clay soils"
    southwood.containsGilgai = [gilgais]

    # Indigenous people (CQ 9)
    bigambul = IndigenousPeople("BigambulPeople")
    bigambul.label = "Bigambul people"
    southwood.traditionalLandOf = [bigambul]

    # Explorers (CQ 10)
    allan_cunningham = Explorer("AllanCunningham")
    allan_cunningham.label = "Allan Cunningham"

    thomas_mitchell = Explorer("ThomasMitchell")
    thomas_mitchell.label = "Thomas Mitchell"

    southwood.exploredBy = [allan_cunningham, thomas_mitchell]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
