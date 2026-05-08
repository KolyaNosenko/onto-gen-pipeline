"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

1. What is the location of Store Torungen Lighthouse?
2. Which lighthouse is located on the island of Store Torungen?
3. What is the municipality where Store Torungen Lighthouse is situated?
4. Which county contains the Store Torungen Lighthouse?
5. What is the country where Store Torungen Lighthouse is located?
6. What nearby lighthouse marks the entrance to Arendal together with Store Torungen Lighthouse?
7. When were Store Torungen Lighthouse and Lille Torungen Lighthouse built?
8. What do the twin lighthouses mark?
9. Which lighthouses are considered twin lighthouses?
10. Why are Store Torungen Lighthouse and Lille Torungen Lighthouse called twin lighthouses?
11. On which coat-of-arms were the two lighthouses featured?
12. What municipality's coat-of-arms displays the two lighthouses?
13. Which of the two lighthouses is still standing today?
14. Is Lille Torungen Lighthouse currently in use?
15. How can the Store Torungen Lighthouse site be accessed?
16. Is the Store Torungen Lighthouse site open to the public?
17. When is the tower of Store Torungen Lighthouse open to visitors?
18. What accommodations are available at the Store Torungen Lighthouse site?
19. Can the lighthouse keepers house be rented for overnight stays?
20. What mainland town do the two lighthouses mark the way to?
21. What body of water do the lighthouses mark the entrance from?
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
    # Entity classes
    class Lighthouse(Thing): pass
    class Island(Thing): pass
    class Municipality(Thing): pass
    class County(Thing): pass
    class Country(Thing): pass
    class Town(Thing): pass
    class BodyOfWater(Thing): pass
    class Building(Thing): pass
    class LighthouseKeepersHouse(Building): pass
    class CoatOfArms(Thing): pass

    # Object Properties
    class locatedOn(ObjectProperty):
        domain = [Lighthouse]
        range = [Island]

    class locatedInMunicipality(ObjectProperty):
        domain = [Lighthouse, Island, Building]
        range = [Municipality]

    class locatedInCounty(ObjectProperty):
        domain = [Municipality, Island, Lighthouse]
        range = [County]

    class locatedInCountry(ObjectProperty):
        domain = [Municipality, Island, Lighthouse, County]
        range = [Country]

    class marksEntrance(ObjectProperty):
        domain = [Lighthouse]
        range = [BodyOfWater]

    class marksWayTo(ObjectProperty):
        domain = [Lighthouse]
        range = [Town]

    class hasSameSpecifications(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class nearbyLighthouse(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class featuredOn(ObjectProperty):
        domain = [Lighthouse]
        range = [CoatOfArms]

    class ofMunicipality(ObjectProperty):
        domain = [CoatOfArms]
        range = [Municipality]

    # Data Properties
    class builtInYear(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [int]

    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class inUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class openToPublic(DataProperty, FunctionalProperty):
        domain = [Island]
        range = [bool]

    class towerOpenDuring(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [str]

    class accessibleBy(DataProperty, FunctionalProperty):
        domain = [Island]
        range = [str]

    class availableToRent(DataProperty, FunctionalProperty):
        domain = [Building]
        range = [bool]

    # Individuals - Lighthouses
    StoreTorungenLighthouse = Lighthouse("StoreTorungenLighthouse")
    StoreTorungenLighthouse.label = "Store Torungen Lighthouse"

    LilleTorungenLighthouse = Lighthouse("LilleTorungenLighthouse")
    LilleTorungenLighthouse.label = "Lille Torungen Lighthouse"

    # Individuals - Geographic entities
    StoreTorungenIsland = Island("StoreTorungenIsland")
    StoreTorungenIsland.label = "Store Torungen"

    ArendallTown = Town("ArendallTown")
    ArendallTown.label = "Arendal"

    ArendallMunicipality = Municipality("ArendallMunicipality")
    ArendallMunicipality.label = "Arendal"

    AustAgderCounty = County("AustAgderCounty")
    AustAgderCounty.label = "Aust-Agder"

    NorwayCountry = Country("NorwayCountry")
    NorwayCountry.label = "Norway"

    HisøyMunicipality = Municipality("HisøyMunicipality")
    HisøyMunicipality.label = "Hisøy"

    Skaggerak = BodyOfWater("Skaggerak")
    Skaggerak.label = "Skaggerak"

    # Individuals - Buildings and artifacts
    StoreTorungenLighthouseKeepersHouse = LighthouseKeepersHouse("StoreTorungenLighthouseKeepersHouse")
    StoreTorungenLighthouseKeepersHouse.label = "lighthouse keepers house"

    HisøyCoatOfArms = CoatOfArms("HisøyCoatOfArms")
    HisøyCoatOfArms.label = "coat-of-arms of Hisøy"

    # Set properties for Store Torungen Lighthouse
    StoreTorungenLighthouse.locatedOn = [StoreTorungenIsland]
    StoreTorungenLighthouse.locatedInMunicipality = [ArendallMunicipality]
    StoreTorungenLighthouse.locatedInCounty = [AustAgderCounty]
    StoreTorungenLighthouse.locatedInCountry = [NorwayCountry]
    StoreTorungenLighthouse.marksEntrance = [Skaggerak]
    StoreTorungenLighthouse.marksWayTo = [ArendallTown]
    StoreTorungenLighthouse.hasSameSpecifications = [LilleTorungenLighthouse]
    StoreTorungenLighthouse.nearbyLighthouse = [LilleTorungenLighthouse]
    StoreTorungenLighthouse.featuredOn = [HisøyCoatOfArms]
    StoreTorungenLighthouse.builtInYear = 1844
    StoreTorungenLighthouse.stillStanding = False
    StoreTorungenLighthouse.inUse = False
    StoreTorungenLighthouse.towerOpenDuring = "daily during the summers"

    # Set properties for Lille Torungen Lighthouse
    LilleTorungenLighthouse.locatedInMunicipality = [ArendallMunicipality]
    LilleTorungenLighthouse.locatedInCounty = [AustAgderCounty]
    LilleTorungenLighthouse.locatedInCountry = [NorwayCountry]
    LilleTorungenLighthouse.marksEntrance = [Skaggerak]
    LilleTorungenLighthouse.marksWayTo = [ArendallTown]
    LilleTorungenLighthouse.hasSameSpecifications = [StoreTorungenLighthouse]
    LilleTorungenLighthouse.nearbyLighthouse = [StoreTorungenLighthouse]
    LilleTorungenLighthouse.featuredOn = [HisøyCoatOfArms]
    LilleTorungenLighthouse.builtInYear = 1844
    LilleTorungenLighthouse.stillStanding = True
    LilleTorungenLighthouse.inUse = False

    # Set properties for Store Torungen Island
    StoreTorungenIsland.locatedInMunicipality = [ArendallMunicipality]
    StoreTorungenIsland.locatedInCounty = [AustAgderCounty]
    StoreTorungenIsland.locatedInCountry = [NorwayCountry]
    StoreTorungenIsland.openToPublic = True
    StoreTorungenIsland.accessibleBy = "by boat"

    # Set properties for geographic regions
    ArendallMunicipality.locatedInCounty = [AustAgderCounty]
    ArendallMunicipality.locatedInCountry = [NorwayCountry]

    AustAgderCounty.locatedInCountry = [NorwayCountry]

    # Set properties for coat of arms
    HisøyCoatOfArms.ofMunicipality = [HisøyMunicipality]

    # Set properties for lighthouse keepers house
    StoreTorungenLighthouseKeepersHouse.locatedInMunicipality = [ArendallMunicipality]
    StoreTorungenLighthouseKeepersHouse.availableToRent = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
