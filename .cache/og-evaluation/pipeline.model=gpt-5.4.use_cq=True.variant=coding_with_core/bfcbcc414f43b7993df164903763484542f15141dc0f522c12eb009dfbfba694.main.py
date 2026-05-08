"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

What is Southwood?
Where is Southwood located?
In which state and country is Southwood situated?
How far is Southwood from Brisbane?
What type of protected area is Southwood?
What kinds of forest remnants are conserved in Southwood?
On which region are the brigalow-belah forest remnants in Southwood located?
Which plant species grow in Southwood National Park?
What vegetation type is considered rare on the Downs and preserved in Southwood?
What wildlife refuge role do Southwood’s scrubby forests provide?
How many bird species have been observed in Southwood?
Which bird species is close to the inland limit of its range in Southwood?
What landform features known as gilgais occur in Southwood?
How are the gilgais in Southwood formed?
What type of soil is associated with the formation of gilgais in Southwood?
Who are the traditional custodians of the land on which Southwood is located?
Which explorers passed through the Southwood area?
What was the historical settlement pattern of the area surrounding Southwood?
What was Southwood formerly known as?
When did Southwood become a national park?
What semi-arid land plant species are common throughout Southwood?
Why is Southwood ecologically significant on the western Darling Downs?
What notable characteristics of Southwood’s vegetation and wildlife justify its conservation?
What historical names and status changes are associated with Southwood?
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
    AgentivePhysicalObject,
    AmountOfMatter,
    Event,
    Feature,
    NonAgentivePhysicalObject,
    NonPhysicalObject,
    Process,
    Society,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class GeographicArea(NonAgentivePhysicalObject):
        pass


    class Country(GeographicArea):
        pass


    class State(GeographicArea):
        pass


    class City(GeographicArea):
        pass


    class NaturalRegion(GeographicArea):
        pass


    class ProtectedArea(GeographicArea):
        pass


    class NationalPark(ProtectedArea):
        pass


    class Forest(NonAgentivePhysicalObject):
        pass


    class ForestRemnant(Forest):
        pass


    class BrigalowBelahForestRemnant(ForestRemnant):
        pass


    class ScrubbyForest(Forest):
        pass


    class PlantSpecies(NonPhysicalObject):
        pass


    class AnimalSpecies(NonPhysicalObject):
        pass


    class BirdSpecies(AnimalSpecies):
        pass


    class WildlifePopulation(NonAgentivePhysicalObject):
        pass


    class LandformFeature(Feature):
        pass


    class Gilgai(LandformFeature):
        pass


    class Soil(AmountOfMatter):
        pass


    class HeavyClaySoil(Soil):
        pass


    class IndigenousPeople(Society):
        pass


    class Explorer(AgentivePhysicalObject):
        pass


    class HistoricalName(NonPhysicalObject):
        pass


    class Quantity(NonPhysicalObject):
        pass


    class DistanceQuantity(Quantity):
        pass


    class SpeciesCount(Quantity):
        pass


    class WettingAndDryingProcess(Process):
        pass


    class NationalParkEstablishment(Event):
        pass


    class locatedIn(partOf):
        domain = [GeographicArea, Forest, LandformFeature, Soil]
        range = [GeographicArea]


    class westOf(ObjectProperty):
        domain = [GeographicArea]
        range = [City]


    class hasDistanceDescription(ObjectProperty):
        domain = [GeographicArea]
        range = [DistanceQuantity]


    class conservedIn(ObjectProperty):
        domain = [ForestRemnant]
        range = [NationalPark]


    class growsIn(ObjectProperty):
        domain = [PlantSpecies]
        range = [NationalPark]


    class commonThroughout(ObjectProperty):
        domain = [PlantSpecies]
        range = [NaturalRegion]


    class refugeFor(ObjectProperty):
        domain = [ScrubbyForest]
        range = [WildlifePopulation]


    class hasObservedBirdSpeciesCount(ObjectProperty):
        domain = [NationalPark]
        range = [SpeciesCount]


    class closeToInlandLimitOfRangeIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]


    class formedBy(ObjectProperty):
        domain = [Gilgai]
        range = [WettingAndDryingProcess]


    class affectsSoil(ObjectProperty):
        domain = [WettingAndDryingProcess]
        range = [Soil]


    class traditionalLandOf(ObjectProperty):
        domain = [GeographicArea]
        range = [IndigenousPeople]


    class passedThrough(ObjectProperty):
        domain = [Explorer]
        range = [GeographicArea]


    class surroundingAreaOf(ObjectProperty, FunctionalProperty):
        domain = [GeographicArea]
        range = [GeographicArea]


    class wasSlowToAttractSettlers(DataProperty, FunctionalProperty):
        domain = [GeographicArea]
        range = [bool]


    class formerlyKnownAs(ObjectProperty):
        domain = [GeographicArea]
        range = [HistoricalName]


    class establishesNationalParkStatusOf(ObjectProperty, FunctionalProperty):
        domain = [NationalParkEstablishment]
        range = [NationalPark]


    class fewIntactExamplesRemainOn(ObjectProperty):
        domain = [ForestRemnant]
        range = [NaturalRegion]


    class hasNumericValue(DataProperty, FunctionalProperty):
        domain = [Quantity]
        range = [int]


    class hasMeasurementUnit(DataProperty, FunctionalProperty):
        domain = [Quantity]
        range = [str]


    class hasDirectionDescription(DataProperty, FunctionalProperty):
        domain = [DistanceQuantity]
        range = [str]


    class hasExclusiveLowerBound(DataProperty, FunctionalProperty):
        domain = [SpeciesCount]
        range = [bool]


    NationalPark.is_a.append(locatedIn.some(GeographicArea))
    ForestRemnant.is_a.append(conservedIn.some(NationalPark))
    ScrubbyForest.is_a.append(refugeFor.some(WildlifePopulation))
    Gilgai.is_a.append(formedBy.some(WettingAndDryingProcess))
    NationalParkEstablishment.is_a.append(establishesNationalParkStatusOf.some(NationalPark))
    NationalParkEstablishment.is_a.append(temporallyLocatedAt.some(TimeInterval))

    Southwood = NationalPark("Southwood")
    Southwood.label = "Southwood"

    Queensland = State("Queensland")
    Queensland.label = "Queensland"

    Australia = Country("Australia")
    Australia.label = "Australia"

    Brisbane = City("Brisbane")
    Brisbane.label = "Brisbane"

    WesternDarlingDowns = NaturalRegion("WesternDarlingDowns")
    WesternDarlingDowns.label = "western Darling Downs"

    Downs = NaturalRegion("Downs")
    Downs.label = "the Downs"

    SemiAridLands = NaturalRegion("SemiAridLands")
    SemiAridLands.label = "the semi - arid lands"

    BrigalowBelahForestRemnants = BrigalowBelahForestRemnant("BrigalowBelahForestRemnants")
    BrigalowBelahForestRemnants.label = "Brigalow - belah forest remnants"

    SouthwoodScrubbyForests = ScrubbyForest("SouthwoodScrubbyForests")
    SouthwoodScrubbyForests.label = "Southwood ’s scrubby forests"

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

    Wildlife = WildlifePopulation("Wildlife")
    Wildlife.label = "wildlife"

    MoreThan92SpeciesOfBirds = SpeciesCount("MoreThan92SpeciesOfBirds")
    MoreThan92SpeciesOfBirds.label = "More than 92 species of birds"

    WongaPigeon = BirdSpecies("WongaPigeon")
    WongaPigeon.label = "wonga pigeon"

    Gilgais = Gilgai("Gilgais")
    Gilgais.label = "gilgais"

    ConstantWettingAndDrying = WettingAndDryingProcess("ConstantWettingAndDrying")
    ConstantWettingAndDrying.label = "constant wetting and drying"

    HeavyClaySoils = HeavyClaySoil("HeavyClaySoils")
    HeavyClaySoils.label = "heavy clay soils"

    BigambulPeople = IndigenousPeople("BigambulPeople")
    BigambulPeople.label = "Bigambul people"

    AllanCunningham = Explorer("AllanCunningham")
    AllanCunningham.label = "Allan Cunningham"

    ThomasMitchell = Explorer("ThomasMitchell")
    ThomasMitchell.label = "Thomas Mitchell"

    SurroundingArea = GeographicArea("SurroundingArea")
    SurroundingArea.label = "the surrounding area"

    WildHorseParadise = HistoricalName("WildHorseParadise")
    WildHorseParadise.label = '" Wild Horse Paradise "'

    Year1970 = TimeInterval("Year1970")
    Year1970.label = "1970"

    Distance288KmWestOfBrisbane = DistanceQuantity("Distance288KmWestOfBrisbane")
    Distance288KmWestOfBrisbane.label = "288   km west of Brisbane"

    SouthwoodNationalParkEstablishment = NationalParkEstablishment("SouthwoodNationalParkEstablishment")
    SouthwoodNationalParkEstablishment.label = "Southwood became a national park in 1970"

    Southwood.locatedIn.append(Queensland)
    Southwood.locatedIn.append(Australia)
    Southwood.locatedIn.append(WesternDarlingDowns)
    Southwood.westOf.append(Brisbane)
    Southwood.hasDistanceDescription.append(Distance288KmWestOfBrisbane)
    Southwood.formerlyKnownAs.append(WildHorseParadise)
    Southwood.traditionalLandOf.append(BigambulPeople)

    Queensland.locatedIn.append(Australia)

    Distance288KmWestOfBrisbane.hasNumericValue = 288
    Distance288KmWestOfBrisbane.hasMeasurementUnit = "km"
    Distance288KmWestOfBrisbane.hasDirectionDescription = "west of Brisbane"

    BrigalowBelahForestRemnants.conservedIn.append(Southwood)
    BrigalowBelahForestRemnants.locatedIn.append(Southwood)
    BrigalowBelahForestRemnants.locatedIn.append(WesternDarlingDowns)
    BrigalowBelahForestRemnants.fewIntactExamplesRemainOn.append(Downs)

    SouthwoodScrubbyForests.locatedIn.append(Southwood)
    SouthwoodScrubbyForests.refugeFor.append(Wildlife)

    CypressPine.growsIn.append(Southwood)
    CypressPine.commonThroughout.append(SemiAridLands)
    PoplarBox.growsIn.append(Southwood)
    PoplarBox.commonThroughout.append(SemiAridLands)
    WilgaBush.growsIn.append(Southwood)
    WilgaBush.commonThroughout.append(SemiAridLands)
    FalseSandalwood.growsIn.append(Southwood)
    FalseSandalwood.commonThroughout.append(SemiAridLands)
    WesternTeatree.growsIn.append(Southwood)
    WesternTeatree.commonThroughout.append(SemiAridLands)

    Southwood.hasObservedBirdSpeciesCount.append(MoreThan92SpeciesOfBirds)
    MoreThan92SpeciesOfBirds.hasNumericValue = 92
    MoreThan92SpeciesOfBirds.hasExclusiveLowerBound = True

    WongaPigeon.closeToInlandLimitOfRangeIn.append(Southwood)

    Gilgais.locatedIn.append(Southwood)
    Gilgais.formedBy.append(ConstantWettingAndDrying)

    ConstantWettingAndDrying.affectsSoil.append(HeavyClaySoils)
    HeavyClaySoils.locatedIn.append(Southwood)

    AllanCunningham.passedThrough.append(Southwood)
    ThomasMitchell.passedThrough.append(Southwood)

    SurroundingArea.surroundingAreaOf = Southwood
    SurroundingArea.wasSlowToAttractSettlers = True

    SouthwoodNationalParkEstablishment.establishesNationalParkStatusOf = Southwood
    SouthwoodNationalParkEstablishment.temporallyLocatedAt = Year1970


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
