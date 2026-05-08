"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

What is Southwood?
Where is Southwood located?
In which state and country is Southwood national park situated?
How far is Southwood from Brisbane?
In which direction is Southwood from Brisbane?
What type of protected area is Southwood?
What vegetation remnants are conserved in Southwood?
On which region are the brigalow-belah forest remnants in Southwood located?
Which plant species grow in Southwood national park?
Does cypress pine grow in Southwood?
Does poplar box grow in Southwood?
Does wilga bush grow in Southwood?
Does false sandalwood grow in Southwood?
Does western teatree grow in Southwood?
What kind of forests characterize Southwood?
What ecological role do Southwood’s scrubby forests play for wildlife?
How many bird species have been observed in Southwood?
Which bird species are found in Southwood?
Is the wonga pigeon found in Southwood?
What is significant about the wonga pigeon’s range in Southwood?
What landform features are scattered through Southwood?
What are gilgais?
How are gilgais formed in Southwood?
What soil type is associated with the formation of gilgais in Southwood?
Whose traditional land is Southwood located on?
Which Indigenous people are traditionally associated with the land of Southwood?
Which explorers passed through the Southwood area?
Did Allan Cunningham pass through the Southwood area?
Did Thomas Mitchell pass through the Southwood area?
How quickly did the surrounding area of Southwood attract settlers?
What was Southwood formerly known as?
When did Southwood become a national park?
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
    class GeographicEntity(Thing):
        pass

    class ProtectedArea(GeographicEntity):
        pass

    class NationalPark(ProtectedArea):
        pass

    class State(GeographicEntity):
        pass

    class Country(GeographicEntity):
        pass

    class City(GeographicEntity):
        pass

    class Region(GeographicEntity):
        pass

    class BiologicalEntity(Thing):
        pass

    class PlantSpecies(BiologicalEntity):
        pass

    class AnimalSpecies(BiologicalEntity):
        pass

    class BirdSpecies(AnimalSpecies):
        pass

    class Wildlife(BiologicalEntity):
        pass

    class VegetationFeature(Thing):
        pass

    class ForestRemnant(VegetationFeature):
        pass

    class Forest(VegetationFeature):
        pass

    class ScrubbyForest(Forest):
        pass

    class LandformFeature(Thing):
        pass

    class LargeDepression(LandformFeature):
        pass

    class Gilgai(LargeDepression):
        pass

    class Soil(Thing):
        pass

    class HeavyClaySoil(Soil):
        pass

    class HumanGroup(Thing):
        pass

    class IndigenousPeople(HumanGroup):
        pass

    class Person(Thing):
        pass

    class Explorer(Person):
        pass

    class Process(Thing):
        pass

    class WettingDryingProcess(Process):
        pass

    class NameEntity(Thing):
        pass

    class PlaceName(NameEntity):
        pass

    class TimePoint(Thing):
        pass

    class Year(TimePoint):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [GeographicEntity]
        range = [GeographicEntity]

    class westOf(ObjectProperty):
        domain = [GeographicEntity]
        range = [GeographicEntity]

    class conserves(ObjectProperty):
        domain = [NationalPark]
        range = [ForestRemnant]

    class occursIn(ObjectProperty):
        domain = [VegetationFeature]
        range = [GeographicEntity]

    class growsIn(ObjectProperty):
        domain = [PlantSpecies]
        range = [NationalPark]

    class seenIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class closeToInlandRangeLimitIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class hasForest(ObjectProperty):
        domain = [NationalPark]
        range = [Forest]

    class providesRefugeFor(ObjectProperty):
        domain = [Forest]
        range = [Wildlife]

    class scatteredThrough(ObjectProperty):
        domain = [LandformFeature]
        range = [NationalPark]

    class formedBy(ObjectProperty):
        domain = [LandformFeature]
        range = [Process]

    class associatedWithSoil(ObjectProperty):
        domain = [LandformFeature]
        range = [Soil]

    class traditionalLandOf(ObjectProperty):
        domain = [NationalPark]
        range = [IndigenousPeople]

    class passedThrough(ObjectProperty):
        domain = [Explorer]
        range = [GeographicEntity]

    class formerlyKnownAs(ObjectProperty):
        domain = [NationalPark]
        range = [PlaceName]

    class becameNationalParkIn(ObjectProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [Year]

    class distanceFromBrisbaneInKilometres(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class directionFromBrisbane(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [str]

    class observedBirdSpeciesCountText(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [str]

    class settlerAttractionPace(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [str]

    Gilgai.is_a.append(formedBy.some(WettingDryingProcess))
    Gilgai.is_a.append(associatedWithSoil.some(HeavyClaySoil))

    Southwood = NationalPark("Southwood")
    Southwood.label = "Southwood"
    Queensland = State("Queensland")
    Queensland.label = "Queensland"
    Australia = Country("Australia")
    Australia.label = "Australia"
    Brisbane = City("Brisbane")
    Brisbane.label = "Brisbane"
    WesternDarlingDowns = Region("WesternDarlingDowns")
    WesternDarlingDowns.label = "western Darling Downs"
    BrigalowBelahForestRemnants = ForestRemnant("BrigalowBelahForestRemnants")
    BrigalowBelahForestRemnants.label = "Brigalow - belah forest remnants"
    CypressPine = PlantSpecies("CypressPine")
    CypressPine.label = "Cypress pine"
    PoplarBox = PlantSpecies("PoplarBox")
    PoplarBox.label = "poplar box"
    WilgaBush = PlantSpecies("WilgaBush")
    WilgaBush.label = "wilga bush"
    FalseSandalwood = PlantSpecies("FalseSandalwood")
    FalseSandalwood.label = "false sandalwood"
    WesternTeatree = PlantSpecies("WesternTeatree")
    WesternTeatree.label = "western teatree"
    SouthwoodScrubbyForests = ScrubbyForest("SouthwoodScrubbyForests")
    SouthwoodScrubbyForests.label = "Southwood’s scrubby forests"
    SouthwoodWildlife = Wildlife("SouthwoodWildlife")
    SouthwoodWildlife.label = "wildlife"
    WongaPigeon = BirdSpecies("WongaPigeon")
    WongaPigeon.label = "wonga pigeon"
    Gilgais = Gilgai("Gilgais")
    Gilgais.label = "gilgais"
    ConstantWettingAndDrying = WettingDryingProcess("ConstantWettingAndDrying")
    ConstantWettingAndDrying.label = "constant wetting and drying"
    HeavyClaySoils = HeavyClaySoil("HeavyClaySoils")
    HeavyClaySoils.label = "heavy clay soils"
    BigambulPeople = IndigenousPeople("BigambulPeople")
    BigambulPeople.label = "Bigambul people"
    AllanCunningham = Explorer("AllanCunningham")
    AllanCunningham.label = "Allan Cunningham"
    ThomasMitchell = Explorer("ThomasMitchell")
    ThomasMitchell.label = "Thomas Mitchell"
    WildHorseParadiseName = PlaceName("WildHorseParadiseName")
    WildHorseParadiseName.label = '"Wild Horse Paradise"'
    Year1970 = Year("Year1970")
    Year1970.label = "1970"

    Queensland.locatedIn = [Australia]
    Southwood.locatedIn = [Queensland, Australia]
    Southwood.westOf = [Brisbane]
    Southwood.distanceFromBrisbaneInKilometres = 288
    Southwood.directionFromBrisbane = "west"
    Southwood.conserves = [BrigalowBelahForestRemnants]
    Southwood.hasForest = [SouthwoodScrubbyForests]
    Southwood.observedBirdSpeciesCountText = "more than 92 species of birds"
    Southwood.traditionalLandOf = [BigambulPeople]
    Southwood.formerlyKnownAs = [WildHorseParadiseName]
    Southwood.becameNationalParkIn = Year1970
    Southwood.settlerAttractionPace = "slow"

    BrigalowBelahForestRemnants.occursIn = [Southwood, WesternDarlingDowns]
    CypressPine.growsIn = [Southwood]
    PoplarBox.growsIn = [Southwood]
    WilgaBush.growsIn = [Southwood]
    FalseSandalwood.growsIn = [Southwood]
    WesternTeatree.growsIn = [Southwood]
    SouthwoodScrubbyForests.occursIn = [Southwood]
    SouthwoodScrubbyForests.providesRefugeFor = [SouthwoodWildlife]
    WongaPigeon.seenIn = [Southwood]
    WongaPigeon.closeToInlandRangeLimitIn = [Southwood]
    Gilgais.scatteredThrough = [Southwood]
    Gilgais.formedBy = [ConstantWettingAndDrying]
    Gilgais.associatedWithSoil = [HeavyClaySoils]
    AllanCunningham.passedThrough = [Southwood]
    ThomasMitchell.passedThrough = [Southwood]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
