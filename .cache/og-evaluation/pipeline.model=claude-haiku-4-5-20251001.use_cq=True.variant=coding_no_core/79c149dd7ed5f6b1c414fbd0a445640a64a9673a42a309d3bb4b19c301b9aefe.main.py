"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

1. What is El Niño and which ocean regions does it affect?
2. What are the geographical boundaries of the warm water band associated with El Niño?
3. What is the El Niño Southern Oscillation (ENSO) and what does it measure?
4. What is the difference between El Niño and La Niña in terms of sea surface temperature and air pressure?
5. How do El Niño and La Niña affect global temperatures and rainfall?
6. Which countries and regions are most affected by the ENSO cycle?
7. Why is the phenomenon called "El Niño" and what is the historical origin of this name?
8. What are the characteristics of air pressure patterns during El Niño?
9. What are the characteristics of air pressure patterns during La Niña?
10. How does ENSO impact agriculture and fishing-dependent economies?
11. During which time of year is the warm water pool in the Pacific typically warmest?
12. What is the relationship between sea surface temperature (SST) and the ENSO cycle?
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
    # Entity Classes
    class OceanRegion(Thing):
        pass

    class Ocean(OceanRegion):
        pass

    class Continent(Thing):
        pass

    class Country(Thing):
        pass

    class TimeOfYear(Thing):
        pass

    class Phenomenon(Thing):
        pass

    class Oscillation(Phenomenon):
        pass

    class Phase(Phenomenon):
        pass

    class WarmPhase(Phase):
        pass

    class CoolPhase(Phase):
        pass

    class WaterBand(Thing):
        pass

    class Measurement(Thing):
        pass

    class Temperature(Measurement):
        pass

    class SeaSurfaceTemperature(Temperature):
        pass

    class Rainfall(Thing):
        pass

    class TemperatureAnomaly(Thing):
        pass

    class AboveAverage(TemperatureAnomaly):
        pass

    class BelowAverage(TemperatureAnomaly):
        pass

    class Sector(Thing):
        pass

    class Agriculture(Sector):
        pass

    class Fishing(Sector):
        pass

    class DevelopingCountry(Country):
        pass

    # Object Properties
    class hasWarmPhase(ObjectProperty):
        domain = [Oscillation]
        range = [WarmPhase]

    class hasCoolPhase(ObjectProperty):
        domain = [Oscillation]
        range = [CoolPhase]

    class isPhaseOf(ObjectProperty):
        domain = [Phase]
        range = [Oscillation]

    class associatedWithWaterBand(ObjectProperty):
        domain = [WarmPhase]
        range = [WaterBand]

    class developedIn(ObjectProperty):
        domain = [WaterBand]
        range = [OceanRegion]

    class locatedIn(ObjectProperty):
        domain = [Phenomenon, OceanRegion]
        range = [OceanRegion]

    class offCoastOf(ObjectProperty):
        domain = [OceanRegion]
        range = [Continent]

    class affectsGlobally(ObjectProperty):
        domain = [Oscillation]
        range = [Temperature, Rainfall]

    class affects(ObjectProperty):
        domain = [Oscillation]
        range = [Country]

    class dependsOn(ObjectProperty):
        domain = [Country]
        range = [Sector]

    class measuredBy(ObjectProperty, FunctionalProperty):
        domain = [Oscillation, Phase]
        range = [SeaSurfaceTemperature]

    class hasHighAirPressure(ObjectProperty):
        domain = [Phase]
        range = [OceanRegion]

    class hasLowAirPressure(ObjectProperty):
        domain = [Phase]
        range = [OceanRegion]

    class hasTemperatureAnomaly(ObjectProperty):
        domain = [Phase, OceanRegion]
        range = [TemperatureAnomaly]

    class wormestDuring(ObjectProperty, FunctionalProperty):
        domain = [OceanRegion]
        range = [TimeOfYear]

    class namedBecauseOf(ObjectProperty, FunctionalProperty):
        domain = [Phenomenon]
        range = [TimeOfYear]

    # Data Properties
    class hasMeaning(DataProperty, FunctionalProperty):
        domain = [Phenomenon]
        range = [str]

    class hasHistoricalOrigin(DataProperty, FunctionalProperty):
        domain = [Phenomenon]
        range = [str]

    class hasCoordinates(DataProperty, FunctionalProperty):
        domain = [OceanRegion]
        range = [str]

    # Named Instances
    christmas = TimeOfYear("Christmas")
    christmas.label = "Christmas"

    enso = Oscillation("ENSO")
    enso.label = "El Niño Southern Oscillation"

    elNino = WarmPhase("ElNino")
    elNino.label = "El Niño"
    elNino.hasMeaning = "the boy"
    elNino.hasHistoricalOrigin = "Peruvian fishermen"

    laNina = CoolPhase("LaNina")
    laNina.label = "La Niña"
    laNina.hasMeaning = "the girl"

    pacificOcean = Ocean("PacificOcean")
    pacificOcean.label = "Pacific Ocean"

    southAmerica = Continent("SouthAmerica")
    southAmerica.label = "South America"

    equatorialPacific = OceanRegion("EquatorialPacific")
    equatorialPacific.label = "Central and east-central equatorial Pacific"
    equatorialPacific.hasCoordinates = "between approximately the International Date Line and 120°W"

    tropicalPacific = OceanRegion("TropicalPacific")
    tropicalPacific.label = "Tropical central and eastern Pacific Ocean"

    westernPacific = OceanRegion("WesternPacific")
    westernPacific.label = "Western Pacific"

    easternPacific = OceanRegion("EasternPacific")
    easternPacific.label = "Eastern Pacific"

    warmWaterBand = WaterBand("WarmWaterBand")
    warmWaterBand.label = "Band of warm ocean water"

    agriculture = Agriculture("AgricultureActivity")
    agriculture.label = "Agriculture"

    fishing = Fishing("FishingActivity")
    fishing.label = "Fishing"

    sst = SeaSurfaceTemperature("SST")
    sst.label = "Sea Surface Temperature"

    belowAverage = BelowAverage("BelowAverageSST")
    belowAverage.label = "Below average"

    # Relationships
    enso.hasWarmPhase = [elNino]
    enso.hasCoolPhase = [laNina]
    elNino.isPhaseOf = [enso]
    laNina.isPhaseOf = [enso]

    elNino.associatedWithWaterBand = [warmWaterBand]
    warmWaterBand.developedIn = [equatorialPacific]

    elNino.locatedIn = [equatorialPacific, tropicalPacific]
    equatorialPacific.offCoastOf = [southAmerica]
    tropicalPacific.offCoastOf = [southAmerica]

    enso.measuredBy = sst

    elNino.hasHighAirPressure = [westernPacific]
    elNino.hasLowAirPressure = [easternPacific]

    laNina.hasLowAirPressure = [westernPacific]
    laNina.hasHighAirPressure = [easternPacific]

    laNina.hasTemperatureAnomaly = [belowAverage]
    easternPacific.hasTemperatureAnomaly = [belowAverage]

    elNino.namedBecauseOf = christmas
    pacificOcean.wormestDuring = christmas


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
