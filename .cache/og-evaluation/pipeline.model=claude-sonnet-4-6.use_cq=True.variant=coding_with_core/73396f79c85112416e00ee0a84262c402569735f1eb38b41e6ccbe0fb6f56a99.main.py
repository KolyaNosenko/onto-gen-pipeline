"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

1. What type of structure is Store Torungen Lighthouse?
2. On which island is Store Torungen Lighthouse located?
3. In which municipality is Store Torungen Lighthouse situated?
4. In which county is Store Torungen Lighthouse located?
5. Which two lighthouses mark the entrance from the Skaggerak to Arendal?
6. In what year were Store Torungen Lighthouse and Lille Torungen Lighthouse built?
7. What specifications were shared between Store Torungen Lighthouse and Lille Torungen Lighthouse?
8. Which coat-of-arms featured both lighthouses?
9. In which municipality were the two lighthouses located when they were added to the coat-of-arms?
10. Which of the two twin lighthouses is still standing?
11. Is Lille Torungen Lighthouse currently in use?
12. How can the site of Store Torungen Lighthouse be accessed?
13. Is the island of Store Torungen open to the public?
14. During which season is the lighthouse tower open daily?
15. What accommodation is available at the Store Torungen Lighthouse site?
16. What nautical route do the two lighthouses mark?
17. What is the relationship between Store Torungen Lighthouse and Lille Torungen Lighthouse?
18. Have the original lighthouses been replaced over time?
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
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
)

# No core properties are subclassed; all domain properties are declared fresh.


with core:
    # ── Entity Classes ────────────────────────────────────────────────────

    class Lighthouse(NonAgentivePhysicalObject):
        """A navigational structure designed to emit light as an aid to mariners."""

    class CoastalLighthouse(Lighthouse):
        """A lighthouse situated on a coast or coastal island."""

    class Island(NonAgentivePhysicalObject):
        """A landmass entirely surrounded by water."""

    class Municipality(Society):
        """A local administrative unit governed by a local authority."""

    class County(Society):
        """A county-level administrative and geographic division."""

    class Country(Society):
        """A sovereign nation-state."""

    class Town(NonAgentivePhysicalObject):
        """A human settlement, typically smaller than a city."""

    class WaterPassage(NonAgentivePhysicalObject):
        """A named body of water or navigable sea passage."""

    class CoatOfArms(NonAgentiveSocialObject):
        """A heraldic device representing a person, family, or administrative unit."""

    class LighthouseKeeperHouse(NonAgentivePhysicalObject):
        """Residential accommodation historically assigned to a lighthouse keeper."""

    # ── Object and Data Properties ────────────────────────────────────────

    class locatedOnIsland(ObjectProperty):
        domain = [Lighthouse]
        range  = [Island]

    class locatedInMunicipality(ObjectProperty):
        domain = [NonAgentivePhysicalObject]
        range  = [Municipality]

    class locatedInCounty(ObjectProperty):
        domain = [Municipality]
        range  = [County]

    class locatedInCountry(ObjectProperty):
        domain = [County]
        range  = [Country]

    class marksEntranceTo(ObjectProperty):
        domain = [Lighthouse]
        range  = [Town]

    class marksEntranceFrom(ObjectProperty):
        domain = [Lighthouse]
        range  = [WaterPassage]

    class twinOf(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range  = [Lighthouse]

    class featuredOnCoatOfArms(ObjectProperty):
        domain = [Lighthouse]
        range  = [CoatOfArms]

    class coatOfArmsOf(ObjectProperty, FunctionalProperty):
        domain = [CoatOfArms]
        range  = [Municipality]

    class hasLighthouseKeeperHouse(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [LighthouseKeeperHouse]

    class yearBuilt(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [int]

    class isStillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class isCurrentlyInUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class wasReplaced(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class accessibleOnlyByBoat(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class towerOpenDuringSummer(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class isOpenToPublic(DataProperty, FunctionalProperty):
        domain = [Island]
        range  = [bool]

    class isAvailableToRent(DataProperty, FunctionalProperty):
        domain = [LighthouseKeeperHouse]
        range  = [bool]

    # ── Named Individuals ─────────────────────────────────────────────────

    store_torungen_lighthouse = CoastalLighthouse("StoreTorungen_Lighthouse")
    store_torungen_lighthouse.label = "Store Torungen Lighthouse"

    lille_torungen_lighthouse = Lighthouse("LilleTorungen_Lighthouse")
    lille_torungen_lighthouse.label = "Lille Torungen Lighthouse"

    store_torungen_island = Island("StoreTorungen_Island")
    store_torungen_island.label = "Store Torungen"

    arendal_municipality = Municipality("ArendalMunicipality")
    arendal_municipality.label = "Arendal"

    aust_agder = County("AustAgder")
    aust_agder.label = "Aust-Agder"

    norway = Country("Norway")
    norway.label = "Norway"

    hisoy = Municipality("Hisoy")
    hisoy.label = "Hisøy"

    arendal_town = Town("ArendalTown")
    arendal_town.label = "Arendal"

    skaggerak = WaterPassage("Skaggerak")
    skaggerak.label = "Skaggerak"

    hisoy_coat_of_arms = CoatOfArms("HisoyCoatOfArms")
    hisoy_coat_of_arms.label = "Hisøy coat-of-arms"

    lighthouse_keepers_house = LighthouseKeeperHouse("StoreTorungen_LighthouseKeepersHouse")
    lighthouse_keepers_house.label = "lighthouse keepers house"

    # ── Property Assertions ───────────────────────────────────────────────

    # Store Torungen Lighthouse
    store_torungen_lighthouse.locatedOnIsland.append(store_torungen_island)
    store_torungen_lighthouse.locatedInMunicipality.append(arendal_municipality)
    store_torungen_lighthouse.locatedInMunicipality.append(hisoy)
    store_torungen_lighthouse.marksEntranceTo.append(arendal_town)
    store_torungen_lighthouse.marksEntranceFrom.append(skaggerak)
    store_torungen_lighthouse.twinOf.append(lille_torungen_lighthouse)
    store_torungen_lighthouse.featuredOnCoatOfArms.append(hisoy_coat_of_arms)
    store_torungen_lighthouse.yearBuilt = 1844
    store_torungen_lighthouse.isStillStanding = False
    store_torungen_lighthouse.wasReplaced = True
    store_torungen_lighthouse.accessibleOnlyByBoat = True
    store_torungen_lighthouse.towerOpenDuringSummer = True
    store_torungen_lighthouse.hasLighthouseKeeperHouse = lighthouse_keepers_house

    # Lille Torungen Lighthouse
    lille_torungen_lighthouse.locatedInMunicipality.append(hisoy)
    lille_torungen_lighthouse.marksEntranceTo.append(arendal_town)
    lille_torungen_lighthouse.marksEntranceFrom.append(skaggerak)
    lille_torungen_lighthouse.twinOf.append(store_torungen_lighthouse)
    lille_torungen_lighthouse.featuredOnCoatOfArms.append(hisoy_coat_of_arms)
    lille_torungen_lighthouse.yearBuilt = 1844
    lille_torungen_lighthouse.isStillStanding = True
    lille_torungen_lighthouse.wasReplaced = True
    lille_torungen_lighthouse.isCurrentlyInUse = False

    # Administrative hierarchy
    arendal_municipality.locatedInCounty.append(aust_agder)
    hisoy.locatedInCounty.append(aust_agder)
    aust_agder.locatedInCountry.append(norway)

    # Coat of arms
    hisoy_coat_of_arms.coatOfArmsOf = hisoy

    # Island
    store_torungen_island.locatedInMunicipality.append(arendal_municipality)
    store_torungen_island.isOpenToPublic = True

    # Lighthouse keeper's house
    lighthouse_keepers_house.isAvailableToRent = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
