"""
=== TASK INPUT ===
Source text:
Store Torungen Lighthouse ( ) is a coastal lighthouse on the island of Store Torungen in the municipality of Arendal in Aust - Agder county , Norway . This lighthouse , together with the nearby Lille Torungen Lighthouse , mark the entrance from the Skaggerak through the outlying islands to the mainland town of Arendal . Both lighthouses were built in 1844 with the same specifications , making " twin " lighthouses marking the way to Arendal . The two lighthouses were put on the coat - of - arms for the local municipality of Hisøy in which the lighthouses were located . Over time , both lighthouses were replaced , and the only one still standing is the Lille Torungen Lighthouse , although it is no longer in use . The site of the Store Torungen Lighthouse is accessible only by boat . The island and site is open to the public , the tower is open daily during the summers , and the lighthouse keepers house is available to rent for overnight accommodations .

What is Store Torungen Lighthouse?
Where is Store Torungen Lighthouse located?
On which island is Store Torungen Lighthouse situated?
In which municipality is Store Torungen Lighthouse located?
In which county is Store Torungen Lighthouse located?
Which country is Store Torungen Lighthouse in?
What type of lighthouse is Store Torungen Lighthouse?
Which lighthouse, together with Store Torungen Lighthouse, marks the entrance to Arendal?
What route or entrance is marked by Store Torungen Lighthouse and Lille Torungen Lighthouse?
What mainland town do Store Torungen Lighthouse and Lille Torungen Lighthouse help mark the way to?
When was Store Torungen Lighthouse built?
When was Lille Torungen Lighthouse built?
Were Store Torungen Lighthouse and Lille Torungen Lighthouse built with the same specifications?
Are Store Torungen Lighthouse and Lille Torungen Lighthouse considered twin lighthouses?
Which municipality had the two lighthouses on its coat of arms?
Where were Store Torungen Lighthouse and Lille Torungen Lighthouse located when they appeared on the coat of arms?
What happened over time to Store Torungen Lighthouse and Lille Torungen Lighthouse?
Which of the two original twin lighthouses is still standing?
Is Lille Torungen Lighthouse still in use?
Is Store Torungen Lighthouse still standing?
How can the site of Store Torungen Lighthouse be accessed?
Is the island of Store Torungen open to the public?
Is the site of Store Torungen Lighthouse open to the public?
When is the tower at Store Torungen Lighthouse open?
Is the lighthouse keeper's house at Store Torungen Lighthouse available for overnight accommodation?
What facilities are available to visitors at the Store Torungen Lighthouse site?
What is the relationship between Store Torungen Lighthouse and Lille Torungen Lighthouse?
What body of water or sea entrance do Store Torungen Lighthouse and Lille Torungen Lighthouse mark from?
Did Store Torungen Lighthouse and Lille Torungen Lighthouse serve as navigational markers for access to Arendal?
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

    class AdministrativeArea(Place):
        pass

    class Country(AdministrativeArea):
        pass

    class County(AdministrativeArea):
        pass

    class Municipality(AdministrativeArea):
        pass

    class Town(Place):
        pass

    class MunicipalTown(Municipality, Town):
        pass

    class Island(Place):
        pass

    class BodyOfWater(Place):
        pass

    class Sea(BodyOfWater):
        pass

    class BuiltStructure(Thing):
        pass

    class Lighthouse(BuiltStructure):
        pass

    class CoastalLighthouse(Lighthouse):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place, BuiltStructure]
        range = [Place]

    class locatedOnIsland(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [Island]

    class locatedInMunicipality(ObjectProperty, FunctionalProperty):
        domain = [Place, BuiltStructure]
        range = [Municipality]

    class historicallyLocatedInMunicipality(ObjectProperty, FunctionalProperty):
        domain = [BuiltStructure]
        range = [Municipality]

    class locatedInCounty(ObjectProperty, FunctionalProperty):
        domain = [Place, BuiltStructure]
        range = [County]

    class locatedInCountry(ObjectProperty, FunctionalProperty):
        domain = [Place, BuiltStructure]
        range = [Country]

    class marksEntranceTogetherWith(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class marksEntranceFrom(ObjectProperty):
        domain = [Lighthouse]
        range = [Sea]

    class marksWayTo(ObjectProperty):
        domain = [Lighthouse]
        range = [Town]

    class hasSameSpecificationsAs(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class twinWith(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range = [Lighthouse]

    class hasCoatOfArmsFeaturing(ObjectProperty):
        domain = [Municipality]
        range = [Lighthouse]

    class builtYear(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [int]

    class stillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class inUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class wasReplaced(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class accessibleOnlyByBoat(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class openToPublic(DataProperty, FunctionalProperty):
        domain = [Place]
        range = [bool]

    class siteOpenToPublic(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class towerOpenDailyDuringSummers(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    class keepersHouseAvailableForOvernightAccommodation(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range = [bool]

    Norway = Country("Norway")
    Norway.label = "Norway"

    AustAgderCounty = County("AustAgderCounty")
    AustAgderCounty.label = "Aust - Agder county"
    AustAgderCounty.locatedIn = [Norway]
    AustAgderCounty.locatedInCountry = Norway

    Arendal = MunicipalTown("Arendal")
    Arendal.label = "Arendal"
    Arendal.locatedIn = [AustAgderCounty, Norway]
    Arendal.locatedInCounty = AustAgderCounty
    Arendal.locatedInCountry = Norway

    Hisoy = Municipality("HisoyMunicipality")
    Hisoy.label = "Hisøy"
    Hisoy.locatedIn = [AustAgderCounty, Norway]
    Hisoy.locatedInCounty = AustAgderCounty
    Hisoy.locatedInCountry = Norway

    StoreTorungen = Island("StoreTorungenIsland")
    StoreTorungen.label = "Store Torungen"
    StoreTorungen.locatedIn = [Arendal, AustAgderCounty, Norway]
    StoreTorungen.locatedInMunicipality = Arendal
    StoreTorungen.locatedInCounty = AustAgderCounty
    StoreTorungen.locatedInCountry = Norway
    StoreTorungen.openToPublic = True

    Skaggerak = Sea("Skaggerak")
    Skaggerak.label = "Skaggerak"

    StoreTorungenLighthouse = CoastalLighthouse("StoreTorungenLighthouse")
    StoreTorungenLighthouse.label = "Store Torungen Lighthouse"
    StoreTorungenLighthouse.locatedIn = [StoreTorungen, Arendal, AustAgderCounty, Norway]
    StoreTorungenLighthouse.locatedOnIsland = StoreTorungen
    StoreTorungenLighthouse.locatedInMunicipality = Arendal
    StoreTorungenLighthouse.historicallyLocatedInMunicipality = Hisoy
    StoreTorungenLighthouse.locatedInCounty = AustAgderCounty
    StoreTorungenLighthouse.locatedInCountry = Norway
    StoreTorungenLighthouse.marksEntranceFrom = [Skaggerak]
    StoreTorungenLighthouse.marksWayTo = [Arendal]
    StoreTorungenLighthouse.builtYear = 1844
    StoreTorungenLighthouse.wasReplaced = True
    StoreTorungenLighthouse.stillStanding = False
    StoreTorungenLighthouse.inUse = False
    StoreTorungenLighthouse.accessibleOnlyByBoat = True
    StoreTorungenLighthouse.siteOpenToPublic = True
    StoreTorungenLighthouse.towerOpenDailyDuringSummers = True
    StoreTorungenLighthouse.keepersHouseAvailableForOvernightAccommodation = True

    LilleTorungenLighthouse = Lighthouse("LilleTorungenLighthouse")
    LilleTorungenLighthouse.label = "Lille Torungen Lighthouse"
    LilleTorungenLighthouse.historicallyLocatedInMunicipality = Hisoy
    LilleTorungenLighthouse.marksEntranceFrom = [Skaggerak]
    LilleTorungenLighthouse.marksWayTo = [Arendal]
    LilleTorungenLighthouse.builtYear = 1844
    LilleTorungenLighthouse.wasReplaced = True
    LilleTorungenLighthouse.stillStanding = True
    LilleTorungenLighthouse.inUse = False

    StoreTorungenLighthouse.marksEntranceTogetherWith = [LilleTorungenLighthouse]
    StoreTorungenLighthouse.hasSameSpecificationsAs = [LilleTorungenLighthouse]
    StoreTorungenLighthouse.twinWith = [LilleTorungenLighthouse]

    Hisoy.hasCoatOfArmsFeaturing = [StoreTorungenLighthouse, LilleTorungenLighthouse]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
