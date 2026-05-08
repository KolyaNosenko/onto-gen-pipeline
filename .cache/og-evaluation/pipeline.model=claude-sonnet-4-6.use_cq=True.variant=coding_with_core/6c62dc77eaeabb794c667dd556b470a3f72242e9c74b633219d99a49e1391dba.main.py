"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. What is the location of Southwood National Park?
2. In which state of Australia is Southwood National Park situated?
3. What is the distance of Southwood National Park from Brisbane?
4. What type of forest is conserved in Southwood National Park?
5. What vegetation types are found in Southwood National Park?
6. Which plant species grow in Southwood National Park?
7. How many bird species have been recorded in Southwood National Park?
8. What is the traditional name for the land on which Southwood National Park is located?
9. Which indigenous people are the traditional owners of the land where Southwood National Park is located?
10. What are gilgais and how are they formed?
11. Where are gilgais located within Southwood National Park?
12. Which explorers passed through the area of Southwood National Park?
13. What was the former name of Southwood National Park?
14. When did Southwood become a national park?
15. Which geographic region does Southwood National Park lie within?
16. What wildlife can be found in Southwood National Park?
17. What is the significance of Southwood National Park for the wonga pigeon?
18. What type of soil is found in Southwood National Park?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    AsymmetricProperty, IrreflexiveProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

from og_sandbox_with_core.core.entities import (
    NonAgentivePhysicalObject, NonAgentiveSocialObject,
    Feature, AmountOfMatter, Society, AgentivePhysicalObject, Process,
)


with core:
    # ── ENTITY CLASSES ──────────────────────────────────────────────────

    class GeographicPlace(NonAgentivePhysicalObject):
        """A named geographic location with a defined spatial extent."""

    class Country(GeographicPlace):
        """A sovereign nation (e.g. Australia)."""

    class FederalState(GeographicPlace):
        """A state or territory within a federal nation (e.g. Queensland)."""

    class City(GeographicPlace):
        """A city or town (e.g. Brisbane)."""

    class GeographicRegionArea(GeographicPlace):
        """A named geographic region that is not a country, state, or city
        (e.g. the Darling Downs)."""

    class NationalPark(GeographicPlace):
        """A legally designated national park."""

    class VegetationCommunity(NonAgentivePhysicalObject):
        """A named community of plant species sharing a habitat."""

    class Forest(VegetationCommunity):
        """A vegetation community dominated by trees."""

    class PlantSpecies(NonAgentiveSocialObject):
        """A named plant taxon (common-name or scientific classification)."""

    class AnimalSpecies(NonAgentiveSocialObject):
        """A named animal taxon."""

    class BirdSpecies(AnimalSpecies):
        """A named bird taxon."""

    class GeologicalFeature(Feature):
        """A geological feature of the landscape, existentially dependent on
        the surrounding terrain."""

    class GeologicalDepression(GeologicalFeature):
        """A hollow or depression in the terrain."""

    class Gilgai(GeologicalDepression):
        """A large depression formed by cyclic wetting and drying of heavy
        clay soils (common in semi-arid Queensland)."""

    class Soil(AmountOfMatter):
        """Soil regarded as an amount of matter (no unity criterion)."""

    class IndigenousCommunity(Society):
        """An indigenous people recognised as traditional owners of land."""

    class Explorer(AgentivePhysicalObject):
        """A historical explorer who surveys and records new territories."""

    class WettingDryingProcess(Process):
        """The cyclic process of clay soil wetting and drying that creates
        gilgai depressions."""

    # ── PROPERTIES ──────────────────────────────────────────────────────

    class locatedIn(ObjectProperty, TransitiveProperty):
        """A geographic entity is spatially contained within another."""
        domain = [GeographicPlace]
        range  = [GeographicPlace]

    class locatedWestOf(ObjectProperty, AsymmetricProperty, IrreflexiveProperty):
        """A place lies to the west of a reference place."""
        domain = [GeographicPlace]
        range  = [GeographicPlace]

    class distanceKm(DataProperty, FunctionalProperty):
        """Straight-line distance in kilometres to the nearest named reference
        point (Brisbane for Southwood)."""
        domain = [GeographicPlace]
        range  = [int]

    class conservesVegetation(ObjectProperty):
        """A protected area conserves a particular vegetation community."""
        domain = [NationalPark]
        range  = [VegetationCommunity]

    class hostsPlantSpecies(ObjectProperty):
        """A geographic place is habitat for a plant species."""
        domain = [GeographicPlace]
        range  = [PlantSpecies]

    class hostsBirdSpecies(ObjectProperty):
        """A geographic place is habitat for a bird species."""
        domain = [GeographicPlace]
        range  = [BirdSpecies]

    class hasTraditionalOwners(ObjectProperty):
        """Land has an indigenous community as its traditional owners."""
        domain = [GeographicPlace]
        range  = [IndigenousCommunity]

    class exploredBy(ObjectProperty):
        """A geographic area was traversed and recorded by an explorer."""
        domain = [GeographicPlace]
        range  = [Explorer]

    class formerName(DataProperty):
        """A former or historical name of a place."""
        domain = [GeographicPlace]
        range  = [str]

    class establishedYear(DataProperty, FunctionalProperty):
        """The year in which a national park was officially established."""
        domain = [NationalPark]
        range  = [int]

    class birdSpeciesCount(DataProperty, FunctionalProperty):
        """The number of bird species recorded in a national park."""
        domain = [NationalPark]
        range  = [int]

    class containsGeologicalFeature(ObjectProperty):
        """A geographic place contains a geological feature."""
        domain = [GeographicPlace]
        range  = [GeologicalFeature]

    class formedByProcess(ObjectProperty):
        """A geological feature is formed by a physical process."""
        domain = [GeologicalFeature]
        range  = [Process]

    class involvesSoil(ObjectProperty):
        """A process acts upon a soil type."""
        domain = [WettingDryingProcess]
        range  = [Soil]

    class hasSoilType(ObjectProperty):
        """A geographic place has a particular soil type."""
        domain = [GeographicPlace]
        range  = [Soil]

    class atRangeLimitOf(ObjectProperty):
        """A location marks or approximates the range limit of a species."""
        domain = [GeographicPlace]
        range  = [BirdSpecies]

    # Class-level restriction: every Gilgai is formed by some WettingDryingProcess
    Gilgai.is_a.append(formedByProcess.some(WettingDryingProcess))

    # ── NAMED INSTANCES ─────────────────────────────────────────────────

    # --- Geographic places ---
    australia = Country("Australia")
    australia.label = "Australia"

    queensland = FederalState("Queensland")
    queensland.label = "Queensland"
    queensland.locatedIn.append(australia)

    brisbane = City("Brisbane")
    brisbane.label = "Brisbane"
    brisbane.locatedIn.append(queensland)

    darling_downs = GeographicRegionArea("DarlingDowns")
    darling_downs.label = "Darling Downs"
    darling_downs.locatedIn.append(queensland)

    southwood = NationalPark("Southwood")
    southwood.label = "Southwood"
    southwood.locatedIn.append(queensland)
    southwood.locatedIn.append(darling_downs)
    southwood.locatedWestOf.append(brisbane)
    southwood.distanceKm = 288
    southwood.formerName.append("Wild Horse Paradise")
    southwood.establishedYear = 1970
    southwood.birdSpeciesCount = 92

    # --- Vegetation ---
    brigalow_belah_forest = Forest("BrigalowBelahForest")
    brigalow_belah_forest.label = "Brigalow-belah forest"
    southwood.conservesVegetation.append(brigalow_belah_forest)

    # --- Plant species ---
    cypress_pine = PlantSpecies("CypressPine")
    cypress_pine.label = "Cypress pine"
    southwood.hostsPlantSpecies.append(cypress_pine)

    poplar_box = PlantSpecies("PoplarBox")
    poplar_box.label = "Poplar box"
    southwood.hostsPlantSpecies.append(poplar_box)

    wilga_bush = PlantSpecies("WilgaBush")
    wilga_bush.label = "Wilga bush"
    southwood.hostsPlantSpecies.append(wilga_bush)

    false_sandalwood = PlantSpecies("FalseSandalwood")
    false_sandalwood.label = "False sandalwood"
    southwood.hostsPlantSpecies.append(false_sandalwood)

    western_teatree = PlantSpecies("WesternTeatree")
    western_teatree.label = "Western teatree"
    southwood.hostsPlantSpecies.append(western_teatree)

    # --- Bird species ---
    wonga_pigeon = BirdSpecies("WongaPigeon")
    wonga_pigeon.label = "Wonga pigeon"
    southwood.hostsBirdSpecies.append(wonga_pigeon)
    southwood.atRangeLimitOf.append(wonga_pigeon)

    # --- Indigenous community ---
    bigambul_people = IndigenousCommunity("BigambulPeople")
    bigambul_people.label = "Bigambul people"
    southwood.hasTraditionalOwners.append(bigambul_people)

    # --- Explorers ---
    allan_cunningham = Explorer("AllanCunningham")
    allan_cunningham.label = "Allan Cunningham"
    southwood.exploredBy.append(allan_cunningham)

    thomas_mitchell = Explorer("ThomasMitchell")
    thomas_mitchell.label = "Thomas Mitchell"
    southwood.exploredBy.append(thomas_mitchell)

    # --- Soil ---
    heavy_clay_soil = Soil("HeavyClaysoil")
    heavy_clay_soil.label = "Heavy clay soil"
    southwood.hasSoilType.append(heavy_clay_soil)

    # --- Geological features (gilgais in the park) ---
    gilgais = Gilgai("GilgaisInSouthwood")
    gilgais.label = "Gilgais"
    southwood.containsGeologicalFeature.append(gilgais)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
