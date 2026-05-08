"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. In which country and state is Southwood National Park located?
2. How far west of Brisbane is Southwood National Park?
3. What vegetation remnants are conserved in Southwood National Park?
4. On which region of the Darling Downs are the brigalow-belah forest remnants conserved?
5. Which plant species grow in Southwood National Park?
6. What type of forests in Southwood National Park serve as a refuge for wildlife?
7. How many bird species have been seen in Southwood National Park?
8. Which bird is close to the inland limit of its range in Southwood National Park?
9. What are the large depressions scattered through Southwood National Park called?
10. How are gilgais formed in Southwood National Park?
11. Which soils are associated with the formation of gilgais in Southwood National Park?
12. What is the traditional land of the Bigambul people?
13. Which explorers passed through the area of Southwood National Park?
14. What was Southwood National Park formerly known as?
15. In what year did Southwood become a national park?
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
    Abstract,
    AmountOfMatter,
    Feature,
    NonAgentivePhysicalObject,
    Process,
    Society,
    SocialAgent,
)


with core:
    class Place(NonAgentivePhysicalObject):
        """A named geographic place."""

    class Country(Place):
        """A country."""

    class GeographicState(Place):
        """A state or state-equivalent administrative region."""

    class City(Place):
        """A city."""

    class GeographicRegion(Place):
        """A geographic region."""

    class NationalPark(Place):
        """A national park."""

    class ForestRemnant(Feature):
        """A remnant of forest vegetation."""

    class Forest(Feature):
        """A forest."""

    class Depression(Feature):
        """A topographic depression."""

    class Soil(AmountOfMatter):
        """Soil."""

    class ClaySoil(Soil):
        """Clay soil."""

    class HeavyClaySoil(ClaySoil):
        """Heavy clay soil."""

    class Species(Abstract):
        """A biological species."""

    class PlantSpecies(Species):
        """A plant species."""

    class BirdSpecies(Species):
        """A bird species."""

    class Wildlife(NonAgentivePhysicalObject):
        """Wild animals and fauna."""

    class Explorer(SocialAgent):
        """An explorer."""

    class PeopleGroup(Society):
        """A people group."""

    class PlaceName(Abstract):
        """A name for a place."""

    class ConstantWettingAndDrying(Process):
        """A constant wetting-and-drying process."""

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class westOf(ObjectProperty):
        domain = [Place]
        range = [Place]

    class conservedIn(ObjectProperty):
        domain = [ForestRemnant]
        range = [NationalPark]

    class growsIn(ObjectProperty):
        domain = [PlantSpecies]
        range = [NationalPark]

    class seenIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class nearInlandLimitOfRangeIn(ObjectProperty):
        domain = [BirdSpecies]
        range = [NationalPark]

    class traditionalLandOf(ObjectProperty):
        domain = [NationalPark]
        range = [PeopleGroup]

    class passedThrough(ObjectProperty):
        domain = [Explorer]
        range = [Place]

    class formerlyKnownAs(ObjectProperty):
        domain = [NationalPark]
        range = [PlaceName]

    class refugeFor(ObjectProperty):
        domain = [Forest]
        range = [Wildlife]

    class formedBy(ObjectProperty):
        domain = [Depression]
        range = [Process]

    class associatedWithSoil(ObjectProperty):
        domain = [Depression]
        range = [Soil]

    class scatteredThrough(ObjectProperty):
        domain = [Feature]
        range = [NationalPark]

    class distanceWestOfBrisbaneKm(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class birdSpeciesSeenLowerBound(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class becameNationalParkInYear(DataProperty, FunctionalProperty):
        domain = [NationalPark]
        range = [int]

    class ScrubbyForest(Forest):
        is_a = [refugeFor.some(Wildlife)]

    class Gilgai(Depression):
        is_a = [
            formedBy.some(ConstantWettingAndDrying),
            associatedWithSoil.some(HeavyClaySoil),
            scatteredThrough.some(NationalPark),
        ]

    australia = Country("Australia")
    australia.label = "Australia"

    queensland = GeographicState("Queensland")
    queensland.label = "Queensland"
    queensland.locatedIn.append(australia)

    brisbane = City("Brisbane")
    brisbane.label = "Brisbane"
    brisbane.locatedIn.append(queensland)

    darling_downs = GeographicRegion("DarlingDowns")
    darling_downs.label = "Darling Downs"
    darling_downs.locatedIn.append(queensland)

    western_darling_downs = GeographicRegion("WesternDarlingDowns")
    western_darling_downs.label = "western Darling Downs"
    western_darling_downs.locatedIn.append(darling_downs)

    bigambul_people = PeopleGroup("BigambulPeople")
    bigambul_people.label = "Bigambul people"

    wild_horse_paradise = PlaceName("WildHorseParadise")
    wild_horse_paradise.label = "Wild Horse Paradise"

    southwood = NationalPark("Southwood")
    southwood.label = "Southwood"
    southwood.locatedIn.append(queensland)
    southwood.locatedIn.append(australia)
    southwood.locatedIn.append(western_darling_downs)
    southwood.westOf.append(brisbane)
    southwood.distanceWestOfBrisbaneKm = 288
    southwood.birdSpeciesSeenLowerBound = 92
    southwood.traditionalLandOf.append(bigambul_people)
    southwood.formerlyKnownAs.append(wild_horse_paradise)
    southwood.becameNationalParkInYear = 1970

    brigalow_belah_forest_remnants = ForestRemnant("BrigalowBelahForestRemnants")
    brigalow_belah_forest_remnants.label = "Brigalow-belah forest remnants"
    brigalow_belah_forest_remnants.conservedIn.append(southwood)

    allan_cunningham = Explorer("AllanCunningham")
    allan_cunningham.label = "Allan Cunningham"
    allan_cunningham.passedThrough.append(southwood)

    thomas_mitchell = Explorer("ThomasMitchell")
    thomas_mitchell.label = "Thomas Mitchell"
    thomas_mitchell.passedThrough.append(southwood)

    cypress_pine = PlantSpecies("CypressPine")
    cypress_pine.label = "cypress pine"
    cypress_pine.growsIn.append(southwood)

    poplar_box = PlantSpecies("PoplarBox")
    poplar_box.label = "poplar box"
    poplar_box.growsIn.append(southwood)

    wilga_bush = PlantSpecies("WilgaBush")
    wilga_bush.label = "wilga bush"
    wilga_bush.growsIn.append(southwood)

    false_sandalwood = PlantSpecies("FalseSandalwood")
    false_sandalwood.label = "false sandalwood"
    false_sandalwood.growsIn.append(southwood)

    western_teatree = PlantSpecies("WesternTeatree")
    western_teatree.label = "western teatree"
    western_teatree.growsIn.append(southwood)

    wonga_pigeon = BirdSpecies("WongaPigeon")
    wonga_pigeon.label = "wonga pigeon"
    wonga_pigeon.seenIn.append(southwood)
    wonga_pigeon.nearInlandLimitOfRangeIn.append(southwood)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
