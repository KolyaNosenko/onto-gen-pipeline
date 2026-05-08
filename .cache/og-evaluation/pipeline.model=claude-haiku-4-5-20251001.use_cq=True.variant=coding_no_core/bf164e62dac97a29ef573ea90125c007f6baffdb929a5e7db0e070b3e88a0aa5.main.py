"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. Where is Southwood national park located?
2. How far is Southwood national park from Brisbane?
3. What vegetation types are conserved in Southwood national park?
4. What plant species grow in Southwood national park?
5. How many bird species have been recorded in Southwood national park?
6. What is the wonga pigeon's significance in Southwood national park?
7. What are gilgais and how are they formed?
8. Which indigenous people traditionally inhabited Southwood?
9. Which explorers visited the area of Southwood national park?
10. What was Southwood national park formerly known as?
11. When did Southwood become a national park?
12. What type of soil is found in Southwood national park?
13. What wildlife takes refuge in Southwood's scrubby forests?
14. Where are the Darling Downs located in relation to Southwood?
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
    # --- Classes ---
    class Place(Thing):
        """Base class for locations"""
        pass

    class NationalPark(Place):
        """National parks"""
        pass

    class City(Place):
        """Cities"""
        pass

    class Region(Place):
        """Geographic regions, states, countries"""
        pass

    class VegetationType(Thing):
        """Types of vegetation/forests"""
        pass

    class PlantSpecies(Thing):
        """Plant species"""
        pass

    class BirdSpecies(Thing):
        """Bird species"""
        pass

    class GeologicalFeature(Thing):
        """Geological formations and features"""
        pass

    class SoilType(Thing):
        """Types of soil"""
        pass

    class IndigenousPeople(Thing):
        """Indigenous peoples and cultures"""
        pass

    class Person(Thing):
        """People"""
        pass

    class Explorer(Person):
        """Explorers and travelers"""
        pass

    # --- Properties ---
    class locatedIn(ObjectProperty, TransitiveProperty):
        """A place is located in another place"""
        domain = [Place]
        range = [Place]

    class distanceFromBrisbane(DataProperty, FunctionalProperty):
        """Distance from Brisbane in kilometers"""
        domain = [NationalPark]
        range = [int]

    class conservesVegetationType(ObjectProperty):
        """A national park conserves a vegetation type"""
        domain = [NationalPark]
        range = [VegetationType]

    class growsIn(ObjectProperty):
        """A plant species grows in a location"""
        domain = [PlantSpecies]
        range = [Place]

    class recordedBirdSpeciesCount(DataProperty, FunctionalProperty):
        """Number of bird species recorded in a location"""
        domain = [NationalPark]
        range = [int]

    class hasRangeLimitAt(ObjectProperty):
        """A bird species has its range limit at a location"""
        domain = [BirdSpecies]
        range = [Place]

    class foundIn(ObjectProperty):
        """A geological feature is found in a location"""
        domain = [GeologicalFeature]
        range = [Place]

    class formedBy(DataProperty):
        """How a geological feature is formed"""
        domain = [GeologicalFeature]
        range = [str]

    class hasSoilType(ObjectProperty):
        """A place has a certain soil type"""
        domain = [Place]
        range = [SoilType]

    class inhabitedBy(ObjectProperty):
        """A place is inhabited by a people"""
        domain = [Place]
        range = [IndigenousPeople]

    class visited(ObjectProperty):
        """A person visited a place"""
        domain = [Person]
        range = [Place]

    class previousName(DataProperty, FunctionalProperty):
        """Previous name of a place"""
        domain = [NationalPark]
        range = [str]

    class becameNationalParkYear(DataProperty, FunctionalProperty):
        """Year when a park became a national park"""
        domain = [NationalPark]
        range = [int]

    # --- Instances ---
    # Locations
    southwood = NationalPark("Southwood")
    southwood.label = "Southwood"
    
    brisbane = City("Brisbane")
    brisbane.label = "Brisbane"
    
    queensland = Region("Queensland")
    queensland.label = "Queensland"
    
    australia = Region("Australia")
    australia.label = "Australia"
    
    darlingDowns = Region("DarlingDowns")
    darlingDowns.label = "Darling Downs"

    # Vegetation and Plants
    brigalowBelahForest = VegetationType("BrigalowBelahForest")
    brigalowBelahForest.label = "Brigalow - belah forest remnants"

    cypressPine = PlantSpecies("CypressPine")
    cypressPine.label = "Cypress pine"

    poplarBox = PlantSpecies("PoplarBox")
    poplarBox.label = "poplar box"

    wilgaBush = PlantSpecies("WilgaBush")
    wilgaBush.label = "wilga bush"

    falseSandalwood = PlantSpecies("FalseSandalwood")
    falseSandalwood.label = "false sandalwood"

    westernTeatree = PlantSpecies("WesternTeatree")
    westernTeatree.label = "western teatree"

    # Birds
    wongaPigeon = BirdSpecies("WongaPigeon")
    wongaPigeon.label = "wonga pigeon"

    # Geological and Soil
    gilgai = GeologicalFeature("Gilgai")
    gilgai.label = "gilgais"

    heavyClayLoils = SoilType("HeavyClayLoils")
    heavyClayLoils.label = "heavy clay soils"

    # Indigenous peoples
    bigambulPeople = IndigenousPeople("BigambulPeople")
    bigambulPeople.label = "Bigambul people"

    # Explorers
    allanCunningham = Explorer("AllanCunningham")
    allanCunningham.label = "Allan Cunningham"

    thomasMitchell = Explorer("ThomasMitchell")
    thomasMitchell.label = "Thomas Mitchell"

    # --- Relations ---
    # Location hierarchy
    southwood.locatedIn = [darlingDowns]
    darlingDowns.locatedIn = [queensland]
    queensland.locatedIn = [australia]

    # Southwood characteristics
    southwood.distanceFromBrisbane = 288
    southwood.conservesVegetationType = [brigalowBelahForest]
    southwood.recordedBirdSpeciesCount = 92
    southwood.hasSoilType = [heavyClayLoils]
    southwood.inhabitedBy = [bigambulPeople]
    southwood.previousName = "Wild Horse Paradise"
    southwood.becameNationalParkYear = 1970

    # Plant species
    cypressPine.growsIn = [southwood]
    poplarBox.growsIn = [southwood]
    wilgaBush.growsIn = [southwood]
    falseSandalwood.growsIn = [southwood]
    westernTeatree.growsIn = [southwood]

    # Bird species
    wongaPigeon.hasRangeLimitAt = [southwood]

    # Geological features
    gilgai.foundIn = [southwood]
    gilgai.formedBy = ["constant wetting and drying"]

    # Explorers
    allanCunningham.visited = [southwood]
    thomasMitchell.visited = [southwood]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
