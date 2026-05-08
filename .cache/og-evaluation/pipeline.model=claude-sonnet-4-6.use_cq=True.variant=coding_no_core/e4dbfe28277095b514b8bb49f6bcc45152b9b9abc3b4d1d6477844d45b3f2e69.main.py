"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

1. What is El Niño and which phase of the El Niño Southern Oscillation does it represent?
2. Where does the band of warm ocean water associated with El Niño develop?
3. What does the acronym ENSO stand for?
4. How is the El Niño Southern Oscillation measured?
5. What are the air pressure conditions associated with El Niño in the western and eastern Pacific?
6. What is the cool phase of ENSO called and what are its characteristics?
7. What global changes are caused by the ENSO cycle?
8. Which countries are most affected by the ENSO cycle?
9. Why are developing countries bordering the Pacific Ocean particularly affected by ENSO?
10. What is the literal English translation of "El Niño" in American Spanish?
11. Why was the weather phenomenon named "El Niño"?
12. What is the original full name of El Niño and what is its origin?
13. Who originally named the El Niño weather phenomenon?
14. What is the literal translation of "La Niña" and why was it chosen as a name?
15. What is the relationship between sea surface temperature and the phases of ENSO?
16. During La Niña, what are the air pressure conditions in the eastern and western Pacific?
17. In which ocean region are the sea surface temperatures monitored to measure ENSO?
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
    # ── Entity classes ────────────────────────────────────────────────────────
    class ClimatePhenomenon(Thing): pass
    class ClimateOscillation(ClimatePhenomenon): pass
    class ENSOPhase(ClimatePhenomenon): pass
    class WarmPhase(ENSOPhase): pass
    class CoolPhase(ENSOPhase): pass

    class OceanRegion(Thing): pass
    class CoastalRegion(OceanRegion): pass
    class OceanWaterBand(Thing): pass

    class MeasurementMethod(Thing): pass
    class GeographicBoundary(Thing): pass

    class Country(Thing): pass
    class DevelopingCountry(Country): pass
    class Industry(Thing): pass
    class OccupationalGroup(Thing): pass

    class ReligiousFigure(Thing): pass
    class ReligiousHoliday(Thing): pass
    class Language(Thing): pass

    class GlobalChange(Thing): pass
    class TemperatureChange(GlobalChange): pass
    class RainfallChange(GlobalChange): pass

    # ── Properties ────────────────────────────────────────────────────────────
    class isPhaseOf(ObjectProperty):
        domain = [ENSOPhase]
        range  = [ClimateOscillation]

    class hasPhase(ObjectProperty):
        domain = [ClimateOscillation]
        range  = [ENSOPhase]

    class measuredBy(ObjectProperty):
        domain = [ClimateOscillation]
        range  = [MeasurementMethod]

    class monitorsRegion(ObjectProperty):
        domain = [MeasurementMethod]
        range  = [OceanRegion]

    class associatedWith(ObjectProperty):
        domain = [ENSOPhase]
        range  = [OceanWaterBand]

    class developsIn(ObjectProperty):
        domain = [OceanWaterBand]
        range  = [OceanRegion]

    class hasHighAirPressureIn(ObjectProperty):
        domain = [ENSOPhase]
        range  = [OceanRegion]

    class hasLowAirPressureIn(ObjectProperty):
        domain = [ENSOPhase]
        range  = [OceanRegion]

    class hasBelowAverageSST(ObjectProperty):
        domain = [ENSOPhase]
        range  = [OceanRegion]

    class causes(ObjectProperty):
        domain = [ClimateOscillation]
        range  = [GlobalChange]

    class mostAffects(ObjectProperty):
        domain = [ClimateOscillation]
        range  = [Country]

    class dependsOn(ObjectProperty):
        domain = [Country]
        range  = [Industry]

    class bordersOcean(ObjectProperty):
        domain = [Country]
        range  = [OceanRegion]

    class namedBy(ObjectProperty):
        domain = [ClimatePhenomenon]
        range  = [OccupationalGroup]

    class namedInReferenceTo(ObjectProperty):
        domain = [ClimatePhenomenon]
        range  = [ReligiousFigure]

    class isOppositeOf(ObjectProperty, SymmetricProperty):
        domain = [ENSOPhase]
        range  = [ENSOPhase]

    class warmestAround(ObjectProperty):
        domain = [OceanWaterBand]
        range  = [ReligiousHoliday]

    class inLanguage(ObjectProperty):
        domain = [ClimatePhenomenon]
        range  = [Language]

    class hasLiteralMeaning(DataProperty, FunctionalProperty):
        domain = [ENSOPhase]
        range  = [str]

    class hasOriginalName(DataProperty, FunctionalProperty):
        domain = [ClimatePhenomenon]
        range  = [str]

    class hasAcronym(DataProperty, FunctionalProperty):
        domain = [ClimateOscillation]
        range  = [str]

    class hasFullName(DataProperty, FunctionalProperty):
        domain = [ClimateOscillation]
        range  = [str]

    class isChosenAsOppositeOf(DataProperty, FunctionalProperty):
        domain = [ENSOPhase]
        range  = [str]

    # ── Individuals ───────────────────────────────────────────────────────────

    # Ocean regions
    western_pacific = OceanRegion("WesternPacific")
    western_pacific.label = "western Pacific"

    eastern_pacific = OceanRegion("EasternPacific")
    eastern_pacific.label = "eastern Pacific"

    equatorial_pacific = OceanRegion("EquatorialPacific")
    equatorial_pacific.label = "equatorial Pacific"

    central_east_central_equatorial_pacific = OceanRegion("CentralEastCentralEquatorialPacific")
    central_east_central_equatorial_pacific.label = "central and east-central equatorial Pacific"

    tropical_central_eastern_pacific = OceanRegion("TropicalCentralEasternPacific")
    tropical_central_eastern_pacific.label = "tropical central and eastern Pacific Ocean"

    pacific_ocean = OceanRegion("PacificOcean")
    pacific_ocean.label = "Pacific Ocean"

    pacific_coast_south_america = CoastalRegion("PacificCoastOfSouthAmerica")
    pacific_coast_south_america.label = "Pacific coast of South America"

    # Geographic boundaries
    int_date_line = GeographicBoundary("InternationalDateLine")
    int_date_line.label = "International Date Line"

    lon_120w = GeographicBoundary("120W")
    lon_120w.label = "120°W"

    # Measurement method
    sst = MeasurementMethod("SST")
    sst.label = "sea surface temperature"
    sst.monitorsRegion = [tropical_central_eastern_pacific]

    # Warm water band
    warm_water_band = OceanWaterBand("WarmOceanWaterBand")
    warm_water_band.label = "band of warm ocean water"
    warm_water_band.developsIn = [central_east_central_equatorial_pacific,
                                  pacific_coast_south_america]

    # Religious holiday
    christmas = ReligiousHoliday("Christmas")
    christmas.label = "Christmas"

    warm_water_band.warmestAround = [christmas]

    # Occupational group
    peruvian_fishermen = OccupationalGroup("PeruvianFishermen")
    peruvian_fishermen.label = "Peruvian fishermen"

    # Religious figure
    newborn_christ = ReligiousFigure("NewbornChrist")
    newborn_christ.label = "newborn Christ"

    # Language
    american_spanish = Language("AmericanSpanish")
    american_spanish.label = "American Spanish"

    # Industries
    agriculture = Industry("Agriculture")
    agriculture.label = "agriculture"

    fishing = Industry("Fishing")
    fishing.label = "fishing"

    # Global changes
    temperature_change = TemperatureChange("GlobalTemperatureChange")
    temperature_change.label = "global temperature change"

    rainfall_change = RainfallChange("GlobalRainfallChange")
    rainfall_change.label = "global rainfall change"

    # Developing countries
    developing_countries = DevelopingCountry("DevelopingCountries")
    developing_countries.label = "developing countries"
    developing_countries.dependsOn = [agriculture, fishing]
    developing_countries.bordersOcean = [pacific_ocean]

    # ENSO
    enso = ClimateOscillation("ENSO")
    enso.label = "El Niño Southern Oscillation"
    enso.hasAcronym = "ENSO"
    enso.hasFullName = "El Niño Southern Oscillation"
    enso.measuredBy = [sst]
    enso.causes = [temperature_change, rainfall_change]
    enso.mostAffects = [developing_countries]

    # El Niño — warm phase
    el_nino = WarmPhase("ElNino")
    el_nino.label = "El Niño"
    el_nino.hasLiteralMeaning = "the boy"
    el_nino.hasOriginalName = "El Niño de Navidad"
    el_nino.isPhaseOf = [enso]
    el_nino.associatedWith = [warm_water_band]
    el_nino.hasHighAirPressureIn = [western_pacific]
    el_nino.hasLowAirPressureIn = [eastern_pacific]
    el_nino.namedBy = [peruvian_fishermen]
    el_nino.namedInReferenceTo = [newborn_christ]
    el_nino.inLanguage = [american_spanish]

    # La Niña — cool phase
    la_nina = CoolPhase("LaNina")
    la_nina.label = "La Niña"
    la_nina.hasLiteralMeaning = "the girl"
    la_nina.isPhaseOf = [enso]
    la_nina.hasHighAirPressureIn = [eastern_pacific]
    la_nina.hasLowAirPressureIn = [western_pacific]
    la_nina.hasBelowAverageSST = [eastern_pacific]
    la_nina.isChosenAsOppositeOf = "El Niño"

    # Symmetric opposite relationship
    el_nino.isOppositeOf = [la_nina]
    la_nina.isOppositeOf = [el_nino]

    # Phases of ENSO
    enso.hasPhase = [el_nino, la_nina]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
