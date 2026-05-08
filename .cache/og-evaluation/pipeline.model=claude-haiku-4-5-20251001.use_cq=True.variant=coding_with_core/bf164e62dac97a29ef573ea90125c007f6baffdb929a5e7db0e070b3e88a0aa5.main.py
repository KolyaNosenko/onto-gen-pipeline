"""
=== TASK INPUT ===
Source text:
Southwood is a national park in Queensland , Australia , 288   km west of Brisbane . Brigalow - belah forest remnants are conserved in this park on the western Darling Downs . Few intact examples of this vegetation type remain on the Downs . Cypress pine , poplar box , wilga bush , false sandalwood , western teatree and other plant species common throughout the semi - arid lands also grow in the park . Southwood ’s scrubby forests are a refuge for wildlife . More than 92 species of birds have been seen in the park . The wonga pigeon is close to the inland limit of its range here . Large depressions known as gilgais are scattered through the park . These form by constant wetting and drying of the heavy clay soils . This is the traditional land of the Bigambul people . Explorers Allan Cunningham and Thomas Mitchell passed this way but the surrounding area was slow to attract settlers . Formerly known as " Wild Horse Paradise " , Southwood became a national park in 1970 .

1. What is the location of Southwood national park?
2. How far is Southwood national park from Brisbane?
3. Which vegetation types are conserved in Southwood national park?
4. What plant species can be found in Southwood national park?
5. How many bird species have been observed in Southwood national park?
6. Which bird species are found near the inland limit of their range in Southwood?
7. What are gilgais and where are they found in Southwood?
8. What causes the formation of gilgais in Southwood?
9. Which indigenous people traditionally inhabited Southwood?
10. Which explorers passed through Southwood?
11. What was Southwood formerly known as?
12. When did Southwood become a national park?
13. What type of soils are present in Southwood national park?
14. What wildlife takes refuge in Southwood's forests?
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
    AgentivePhysicalObject, NonAgentivePhysicalObject,
    PhysicalEndurant, SocialObject, Society, Feature, AmountOfMatter
)


with core:
    # Domain entity classes
    class NationalPark(SocialObject):
        """A park established and managed by a government as a protected area."""
        pass
    
    class GeographicalRegion(PhysicalEndurant):
        """A geographical area or region."""
        pass
    
    class City(SocialObject):
        """An urban settlement and administrative center."""
        pass
    
    class Country(SocialObject):
        """A sovereign nation state."""
        pass
    
    class State(SocialObject):
        """A political subdivision of a country."""
        pass
    
    class PlantSpecies(NonAgentivePhysicalObject):
        """A species of plant."""
        pass
    
    class BirdSpecies(NonAgentivePhysicalObject):
        """A species of bird."""
        pass
    
    class VegetationType(NonAgentivePhysicalObject):
        """A type or community of vegetation."""
        pass
    
    class Gilgai(Feature):
        """A large depression in the ground, formed by wetting and drying of soil."""
        pass
    
    class SoilType(AmountOfMatter):
        """A type or classification of soil."""
        pass
    
    class Explorer(AgentivePhysicalObject):
        """A person who explores new territories."""
        pass
    
    class IndigenousCommunity(Society):
        """An indigenous people or community."""
        pass
    
    # Domain ObjectProperty and DataProperty classes
    class locatedIn(ObjectProperty):
        """Indicates that one entity is located within another geographical area."""
        domain = [NationalPark, GeographicalRegion, City, State]
        range = [GeographicalRegion, Country, State, City]
    
    class conserves(ObjectProperty):
        """Indicates that a park conserves or protects a vegetation type or species."""
        domain = [NationalPark]
        range = [VegetationType, PlantSpecies]
    
    class contains(ObjectProperty):
        """Indicates that a location contains or has a species, feature, or substance."""
        domain = [NationalPark, GeographicalRegion]
        range = [PlantSpecies, BirdSpecies, VegetationType, Gilgai, SoilType]
    
    class traditionallyInhabitedBy(ObjectProperty):
        """Indicates that a region was traditionally inhabited by a people."""
        domain = [NationalPark, GeographicalRegion]
        range = [IndigenousCommunity]
    
    class passedThrough(ObjectProperty):
        """Indicates that a person passed through or visited a location."""
        domain = [Explorer]
        range = [NationalPark, GeographicalRegion]
    
    class formerlyKnownAs(DataProperty):
        """Indicates a former name of an entity."""
        domain = [NationalPark]
        range = [str]
    
    class yearEstablished(DataProperty, FunctionalProperty):
        """The year in which an entity was officially established."""
        domain = [NationalPark]
        range = [int]
    
    class observedSpeciesCount(DataProperty, FunctionalProperty):
        """The count of observed species of a particular type."""
        domain = [NationalPark]
        range = [int]
    
    class nearRangeLimit(ObjectProperty):
        """Indicates that a species is near the limit of its geographical range."""
        domain = [BirdSpecies]
        range = [NationalPark, GeographicalRegion]
    
    class nearestUrbanCenter(ObjectProperty):
        """Indicates the nearest urban center to a location."""
        domain = [NationalPark]
        range = [City]
    
    class distanceToNearestUrbanCenter(DataProperty):
        """The distance to the nearest urban center, expressed as a string."""
        domain = [NationalPark]
        range = [str]
    
    class formedBy(DataProperty):
        """Indicates the process or mechanism by which a feature is formed."""
        domain = [Gilgai]
        range = [str]
    
    # Named instances from the source text
    southwood = NationalPark("Southwood")
    southwood.label = "Southwood"
    southwood.yearEstablished = 1970
    southwood.formerlyKnownAs = ["Wild Horse Paradise"]
    southwood.observedSpeciesCount = 92
    
    queensland = State("Queensland")
    queensland.label = "Queensland"
    
    australia = Country("Australia")
    australia.label = "Australia"
    
    brisbane = City("Brisbane")
    brisbane.label = "Brisbane"
    
    darling_downs = GeographicalRegion("DarlingDowns")
    darling_downs.label = "Darling Downs"
    
    brigalow_belah = VegetationType("BrigalowBelah")
    brigalow_belah.label = "Brigalow - belah"
    
    cypress_pine = PlantSpecies("CypressPine")
    cypress_pine.label = "Cypress pine"
    
    poplar_box = PlantSpecies("PoplarBox")
    poplar_box.label = "poplar box"
    
    wilga_bush = PlantSpecies("WilgaBush")
    wilga_bush.label = "wilga bush"
    
    false_sandalwood = PlantSpecies("FalseSandalwood")
    false_sandalwood.label = "false sandalwood"
    
    western_teatree = PlantSpecies("WesternTeatree")
    western_teatree.label = "western teatree"
    
    wonga_pigeon = BirdSpecies("WongaPigeon")
    wonga_pigeon.label = "wonga pigeon"
    
    heavy_clay_soils = SoilType("HeavyClaysoils")
    heavy_clay_soils.label = "heavy clay soils"
    
    bigambul = IndigenousCommunity("Bigambul")
    bigambul.label = "Bigambul people"
    
    cunningham = Explorer("AllanCunningham")
    cunningham.label = "Allan Cunningham"
    
    mitchell = Explorer("ThomasMitchell")
    mitchell.label = "Thomas Mitchell"
    
    # Relationships
    southwood.locatedIn.append(queensland)
    southwood.locatedIn.append(darling_downs)
    queensland.locatedIn.append(australia)
    brisbane.locatedIn.append(queensland)
    darling_downs.locatedIn.append(queensland)
    
    southwood.nearestUrbanCenter.append(brisbane)
    southwood.distanceToNearestUrbanCenter = ["288 km west"]
    
    southwood.conserves.append(brigalow_belah)
    
    southwood.contains.append(cypress_pine)
    southwood.contains.append(poplar_box)
    southwood.contains.append(wilga_bush)
    southwood.contains.append(false_sandalwood)
    southwood.contains.append(western_teatree)
    southwood.contains.append(wonga_pigeon)
    southwood.contains.append(heavy_clay_soils)
    
    southwood.traditionallyInhabitedBy.append(bigambul)
    
    cunningham.passedThrough.append(southwood)
    mitchell.passedThrough.append(southwood)
    
    wonga_pigeon.nearRangeLimit.append(southwood)
    
    # Gilgai formation description
    gilgai_general = Gilgai("Gilgais")
    gilgai_general.label = "gilgais"
    gilgai_general.formedBy = ["constant wetting and drying of heavy clay soils"]
    
    southwood.contains.append(gilgai_general)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
