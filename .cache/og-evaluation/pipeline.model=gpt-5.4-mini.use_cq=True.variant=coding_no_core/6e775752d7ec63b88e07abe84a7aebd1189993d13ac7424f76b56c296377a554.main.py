"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. In which Australian state is Southwood National Park located?
2. How far and in which direction is Southwood National Park from Brisbane?
3. What type of vegetation remnants are conserved in Southwood National Park?
4. On which region of the Darling Downs are the brigalow-belah forest remnants found?
5. Which plant species grow in Southwood National Park?
6. Which wildlife species have been observed in Southwood National Park?
7. How many bird species have been seen in Southwood National Park?
8. Which bird species is close to the inland limit of its range in Southwood National Park?
9. What geological or soil features are scattered through Southwood National Park?
10. How are gilgais formed in Southwood National Park?
11. Which Indigenous people are the traditional owners of the land where Southwood National Park is located?
12. Which explorers passed through the area of Southwood National Park?
13. What was Southwood National Park formerly known as?
14. In what year did Southwood become a national park?
15. Why is Southwood National Park important for wildlife conservation?
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
    class Place(Thing):
        pass

    class Country(Place):
        pass

    class AustralianState(Place):
        pass

    class City(Place):
        pass

    class Region(Place):
        pass

    class Park(Place):
        pass

    class NationalPark(Park):
        pass

    class PeopleGroup(Thing):
        pass

    class IndigenousPeople(PeopleGroup):
        pass

    class Person(Thing):
        pass

    class Explorer(Person):
        pass

    class Wildlife(Thing):
        pass

    class Species(Thing):
        pass

    class PlantSpecies(Species):
        pass

    class AnimalSpecies(Species):
        pass

    class BirdSpecies(AnimalSpecies):
        pass

    class VegetationType(Thing):
        pass

    class VegetationRemnant(VegetationType):
        pass

    class ForestRemnant(VegetationRemnant):
        pass

    class ScrubbyForest(VegetationType):
        pass

    class GeologicalFeature(Thing):
        pass

    class Depression(GeologicalFeature):
        pass

    class Gilgai(Depression):
        pass

    class Soil(Thing):
        pass

    class ClaySoil(Soil):
        pass

    class FormerName(Thing):
        pass

    class Year(Thing):
        pass

    class hasPart(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [Country]

    class locatedInState(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [AustralianState]

    class westOf(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [Place]

    class traditionalLandOf(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [IndigenousPeople]

    class formerlyKnownAs(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [FormerName]

    class becameNationalParkIn(ObjectProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [Year]

    class distanceKmFromBrisbane(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class birdSpeciesSeenMinimum(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class birdSpeciesSeenMoreThan(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [bool]

    class conservedIn(ObjectProperty):
        domain = [ForestRemnant]
        range = [NationalPark]

    class locatedOn(ObjectProperty):
        domain = [Thing]
        range = [Region]

    class growsIn(ObjectProperty):
        domain = [PlantSpecies]
        range = [NationalPark]

    class commonThroughout(ObjectProperty):
        domain = [Species]
        range = [Region]

    class seenIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class nearInlandLimitOfRangeIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class scatteredThrough(ObjectProperty):
        domain = [GeologicalFeature]
        range = [NationalPark]

    class formedByDescription(DataProperty, FunctionalProperty):
        domain = [Gilgai]
        range = [str]

    class passedThrough(ObjectProperty):
        domain = [Explorer]
        range = [Place]

    class refugeForDescription(DataProperty, FunctionalProperty):
        domain = [ScrubbyForest]
        range = [str]

    Southwood = NationalPark("Southwood")
    Southwood.label = "Southwood"

    Queensland = AustralianState("Queensland")
    Queensland.label = "Queensland"

    Australia = Country("Australia")
    Australia.label = "Australia"

    Brisbane = City("Brisbane")
    Brisbane.label = "Brisbane"

    WesternDarlingDowns = Region("WesternDarlingDowns")
    WesternDarlingDowns.label = "western Darling Downs"

    SemiAridLands = Region("SemiAridLands")
    SemiAridLands.label = "semi-arid lands"

    BigambulPeople = IndigenousPeople("BigambulPeople")
    BigambulPeople.label = "Bigambul people"

    AllanCunningham = Explorer("AllanCunningham")
    AllanCunningham.label = "Allan Cunningham"

    ThomasMitchell = Explorer("ThomasMitchell")
    ThomasMitchell.label = "Thomas Mitchell"

    WildHorseParadise = FormerName("WildHorseParadise")
    WildHorseParadise.label = '"Wild Horse Paradise"'

    Year1970 = Year("Year1970")
    Year1970.label = "1970"

    BrigalowBelahForestRemnants = ForestRemnant("BrigalowBelahForestRemnants")
    BrigalowBelahForestRemnants.label = "Brigalow-belah forest remnants"

    SouthwoodScrubbyForests = ScrubbyForest("SouthwoodScrubbyForests")
    SouthwoodScrubbyForests.label = "Southwood’s scrubby forests"
    SouthwoodScrubbyForests.refugeForDescription = "wildlife"

    CypressPine = PlantSpecies("CypressPine")
    CypressPine.label = "cypress pine"

    PoplarBox = PlantSpecies("PoplarBox")
    PoplarBox.label = "poplar box"

    WilgaBush = PlantSpecies("WilgaBush")
    WilgaBush.label = "wilga bush"

    FalseSandalwood = PlantSpecies("FalseSandalwood")
    FalseSandalwood.label = "false sandalwood"

    WesternTeatree = PlantSpecies("WesternTeatree")
    WesternTeatree.label = "western teatree"

    WongaPigeon = BirdSpecies("WongaPigeon")
    WongaPigeon.label = "wonga pigeon"

    Gilgais = Gilgai("Gilgais")
    Gilgais.label = "gilgais"

    Southwood.locatedInState = Queensland
    Southwood.locatedInCountry = Australia
    Southwood.westOf = Brisbane
    Southwood.distanceKmFromBrisbane = 288
    Southwood.becameNationalParkIn = Year1970
    Southwood.formerlyKnownAs = WildHorseParadise
    Southwood.traditionalLandOf = BigambulPeople
    Southwood.birdSpeciesSeenMinimum = 92
    Southwood.birdSpeciesSeenMoreThan = True
    Southwood.hasPart = [SouthwoodScrubbyForests, BrigalowBelahForestRemnants, Gilgais]

    BrigalowBelahForestRemnants.conservedIn = [Southwood]
    BrigalowBelahForestRemnants.locatedOn = [WesternDarlingDowns]

    CypressPine.growsIn = [Southwood]
    CypressPine.commonThroughout = [SemiAridLands]
    PoplarBox.growsIn = [Southwood]
    PoplarBox.commonThroughout = [SemiAridLands]
    WilgaBush.growsIn = [Southwood]
    WilgaBush.commonThroughout = [SemiAridLands]
    FalseSandalwood.growsIn = [Southwood]
    FalseSandalwood.commonThroughout = [SemiAridLands]
    WesternTeatree.growsIn = [Southwood]
    WesternTeatree.commonThroughout = [SemiAridLands]

    WongaPigeon.seenIn = [Southwood]
    WongaPigeon.nearInlandLimitOfRangeIn = [Southwood]

    Gilgais.scatteredThrough = [Southwood]
    Gilgais.formedByDescription = "constant wetting and drying of the heavy clay soils"

    AllanCunningham.passedThrough = [Southwood]
    ThomasMitchell.passedThrough = [Southwood]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
