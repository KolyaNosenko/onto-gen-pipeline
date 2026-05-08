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
7. Were the two lighthouses built with the same specifications?
8. Which town do the twin lighthouses mark the way to?
9. On which municipality's coat-of-arms were the two lighthouses placed?
10. Which of the two twin lighthouses is still standing?
11. Is Lille Torungen Lighthouse still in use?
12. How can the site of Store Torungen Lighthouse be accessed?
13. Is the island of Store Torungen open to the public?
14. During which season is the lighthouse tower open daily?
15. What accommodation is available at the Store Torungen Lighthouse site?
16. What body of water do the lighthouses mark the entrance from?
17. Were both lighthouses replaced over time?
18. What navigational purpose do the two lighthouses serve together?
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
    # ── ENTITY CLASSES ──────────────────────────────────────────────────────

    # Geographic features
    class GeographicFeature(Thing): pass
    class Island(GeographicFeature): pass
    class BodyOfWater(GeographicFeature): pass

    # Administrative divisions
    class AdministrativeDivision(Thing): pass
    class Municipality(AdministrativeDivision): pass
    class County(AdministrativeDivision): pass
    class Country(AdministrativeDivision): pass

    # Settlements
    class Settlement(Thing): pass
    class Town(Settlement): pass

    # Built structures
    class Structure(Thing): pass
    class Lighthouse(Structure): pass
    class CoastalLighthouse(Lighthouse): pass
    class Tower(Structure): pass

    # Heraldry
    class HeraldrySymbol(Thing): pass
    class CoatOfArms(HeraldrySymbol): pass

    # Site and accommodation
    class Site(Thing): pass
    class LighthouseSite(Site): pass
    class Accommodation(Thing): pass
    class LighthouseKeepersHouse(Accommodation): pass

    # Time / season
    class Season(Thing): pass

    # ── OBJECT PROPERTIES ───────────────────────────────────────────────────

    class locatedOnIsland(ObjectProperty):
        domain = [Lighthouse]
        range  = [Island]

    class locatedInMunicipality(ObjectProperty):
        domain = [Thing]
        range  = [Municipality]

    class locatedInCounty(ObjectProperty):
        domain = [AdministrativeDivision]
        range  = [County]

    class locatedInCountry(ObjectProperty):
        domain = [AdministrativeDivision]
        range  = [Country]

    class marksEntranceTo(ObjectProperty):
        domain = [Lighthouse]
        range  = [Town]

    class marksEntranceFrom(ObjectProperty):
        domain = [Lighthouse]
        range  = [BodyOfWater]

    # Two lighthouses are twins of each other — symmetric
    class twinsWith(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range  = [Lighthouse]

    # One lighthouse is near another — symmetric
    class nearbyLighthouse(ObjectProperty, SymmetricProperty):
        domain = [Lighthouse]
        range  = [Lighthouse]

    class appearsOnCoatOfArms(ObjectProperty):
        domain = [Lighthouse]
        range  = [CoatOfArms]

    # Each coat of arms belongs to exactly one municipality
    class coatOfArmsOf(ObjectProperty, FunctionalProperty):
        domain = [CoatOfArms]
        range  = [Municipality]

    class hasSite(ObjectProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [LighthouseSite]

    class hasTower(ObjectProperty):
        domain = [LighthouseSite]
        range  = [Tower]

    class hasAccommodation(ObjectProperty):
        domain = [LighthouseSite]
        range  = [Accommodation]

    class openDuringSeason(ObjectProperty):
        domain = [Thing]
        range  = [Season]

    # ── DATA PROPERTIES ─────────────────────────────────────────────────────

    class builtInYear(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [int]

    class builtWithSameSpecifications(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class isStillStanding(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class isInUse(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class wasReplaced(DataProperty, FunctionalProperty):
        domain = [Lighthouse]
        range  = [bool]

    class accessibleBy(DataProperty, FunctionalProperty):
        domain = [LighthouseSite]
        range  = [str]

    class openToPublic(DataProperty, FunctionalProperty):
        domain = [Thing]
        range  = [bool]

    class availableToRent(DataProperty, FunctionalProperty):
        domain = [Accommodation]
        range  = [bool]

    # ── INDIVIDUALS ─────────────────────────────────────────────────────────

    # Lighthouses
    StoreTorungen_LH = CoastalLighthouse("StoreTorungen_LH")
    StoreTorungen_LH.label = "Store Torungen Lighthouse"

    LilleTorungen_LH = CoastalLighthouse("LilleTorungen_LH")
    LilleTorungen_LH.label = "Lille Torungen Lighthouse"

    # Island
    StoreTorungen_Island = Island("StoreTorungen_Island")
    StoreTorungen_Island.label = "Store Torungen"

    # Municipalities
    Arendal_Municipality = Municipality("Arendal_Municipality")
    Arendal_Municipality.label = "Arendal"

    Hisoey_Municipality = Municipality("Hisoey_Municipality")
    Hisoey_Municipality.label = "Hisøy"

    # County
    AustAgder_County = County("AustAgder_County")
    AustAgder_County.label = "Aust-Agder"

    # Country
    Norway_Country = Country("Norway_Country")
    Norway_Country.label = "Norway"

    # Town (Arendal as a mainland town — distinct role from the municipality)
    Arendal_Town = Town("Arendal_Town")
    Arendal_Town.label = "Arendal"

    # Body of water
    Skaggerak_Water = BodyOfWater("Skaggerak_Water")
    Skaggerak_Water.label = "Skaggerak"

    # Coat of arms
    Hisoey_CoatOfArms = CoatOfArms("Hisoey_CoatOfArms")
    Hisoey_CoatOfArms.label = "Hisøy coat of arms"

    # Lighthouse site
    StoreTorungen_Site = LighthouseSite("StoreTorungen_Site")
    StoreTorungen_Site.label = "Store Torungen Lighthouse site"

    # Tower at the site (open to public daily in summer)
    StoreTorungen_Tower = Tower("StoreTorungen_Tower")
    StoreTorungen_Tower.label = "Store Torungen Lighthouse tower"

    # Lighthouse keepers house (available for rent)
    LighthouseKeepers_House = LighthouseKeepersHouse("LighthouseKeepers_House")
    LighthouseKeepers_House.label = "lighthouse keepers house"

    # Season
    SummerSeason = Season("SummerSeason")
    SummerSeason.label = "summer"

    # ── ASSERTIONS ──────────────────────────────────────────────────────────

    # Store Torungen Lighthouse
    StoreTorungen_LH.locatedOnIsland           = [StoreTorungen_Island]
    StoreTorungen_LH.locatedInMunicipality     = [Arendal_Municipality, Hisoey_Municipality]
    StoreTorungen_LH.builtInYear               = 1844
    StoreTorungen_LH.builtWithSameSpecifications = True
    StoreTorungen_LH.isStillStanding           = False
    StoreTorungen_LH.isInUse                   = False
    StoreTorungen_LH.wasReplaced               = True
    StoreTorungen_LH.twinsWith                 = [LilleTorungen_LH]
    StoreTorungen_LH.nearbyLighthouse          = [LilleTorungen_LH]
    StoreTorungen_LH.marksEntranceTo           = [Arendal_Town]
    StoreTorungen_LH.marksEntranceFrom         = [Skaggerak_Water]
    StoreTorungen_LH.appearsOnCoatOfArms       = [Hisoey_CoatOfArms]
    StoreTorungen_LH.hasSite                   = StoreTorungen_Site

    # Lille Torungen Lighthouse
    LilleTorungen_LH.locatedInMunicipality     = [Hisoey_Municipality]
    LilleTorungen_LH.builtInYear               = 1844
    LilleTorungen_LH.builtWithSameSpecifications = True
    LilleTorungen_LH.isStillStanding           = True
    LilleTorungen_LH.isInUse                   = False
    LilleTorungen_LH.wasReplaced               = True
    LilleTorungen_LH.marksEntranceTo           = [Arendal_Town]
    LilleTorungen_LH.marksEntranceFrom         = [Skaggerak_Water]
    LilleTorungen_LH.appearsOnCoatOfArms       = [Hisoey_CoatOfArms]

    # Island
    StoreTorungen_Island.locatedInMunicipality = [Arendal_Municipality]
    StoreTorungen_Island.openToPublic          = True

    # Administrative hierarchy
    Arendal_Municipality.locatedInCounty       = [AustAgder_County]
    Hisoey_Municipality.locatedInCounty        = [AustAgder_County]
    AustAgder_County.locatedInCountry          = [Norway_Country]

    # Coat of arms
    Hisoey_CoatOfArms.coatOfArmsOf             = Hisoey_Municipality

    # Lighthouse site
    StoreTorungen_Site.accessibleBy            = "boat"
    StoreTorungen_Site.openToPublic            = True
    StoreTorungen_Site.hasTower                = [StoreTorungen_Tower]
    StoreTorungen_Site.hasAccommodation        = [LighthouseKeepers_House]

    # Tower
    StoreTorungen_Tower.openDuringSeason       = [SummerSeason]
    StoreTorungen_Tower.openToPublic           = True

    # Accommodation
    LighthouseKeepers_House.availableToRent    = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
