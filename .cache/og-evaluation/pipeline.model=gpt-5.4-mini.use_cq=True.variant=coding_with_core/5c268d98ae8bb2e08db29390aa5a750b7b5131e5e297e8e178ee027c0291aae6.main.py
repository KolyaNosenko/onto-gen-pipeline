"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

1. What is El Niño, and which phase of the El Niño Southern Oscillation (ENSO) does it represent?
2. What oceanic region is associated with El Niño’s warm water band?
3. Between which longitudinal boundaries does the El Niño warm water band typically develop?
4. Is El Niño associated with the Pacific coast of South America?
5. What does El Niño Southern Oscillation (ENSO) refer to?
6. Which temperatures are measured to characterize ENSO?
7. What are the air pressure conditions in the western and eastern Pacific during El Niño?
8. What is the cool phase of ENSO called?
9. What are the sea surface temperature conditions in the eastern Pacific during La Niña?
10. What are the air pressure conditions in the eastern and western Pacific during La Niña?
11. What global environmental changes are caused by the ENSO cycle?
12. Which regions are usually most affected by El Niño and La Niña?
13. Which types of countries are particularly affected by ENSO-related changes?
14. What does the term “El Niño” mean in American Spanish?
15. Why was El Niño named “the boy”?
16. What is the original name “El Niño de Navidad” associated with?
17. Who originally named the weather phenomenon now called El Niño?
18. What does “La Niña” literally translate to?
19. Why was La Niña chosen as the opposite of El Niño?
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
    AbstractRegion, AmountOfMatter, NonPhysicalObject, PhysicalQuality,
    PhysicalRegion, Process, SocialAgent, SocialObject, State, TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, specificallyDependsOn


with core:
    class ClimateCycle(Process):
        pass

    class ClimatePhase(State):
        pass

    class WarmPhase(ClimatePhase):
        pass

    class CoolPhase(ClimatePhase):
        pass

    class OceanWaterBand(AmountOfMatter):
        pass

    class EnvironmentalChange(Process):
        pass

    class TemperatureChange(EnvironmentalChange):
        pass

    class RainfallChange(EnvironmentalChange):
        pass

    class Country(SocialObject):
        pass

    class DevelopingCountry(Country):
        pass

    class Agriculture(Process):
        pass

    class Fishing(Process):
        pass

    class Language(NonPhysicalObject):
        pass

    class Term(NonPhysicalObject):
        pass

    class GeographicRegion(PhysicalRegion):
        pass

    class OceanRegion(GeographicRegion):
        pass

    class PacificOceanRegion(OceanRegion):
        pass

    class EquatorialPacificRegion(PacificOceanRegion):
        pass

    class CentralEastCentralEquatorialPacificRegion(EquatorialPacificRegion):
        pass

    class WesternPacificRegion(PacificOceanRegion):
        pass

    class EasternPacificRegion(PacificOceanRegion):
        pass

    class TropicalCentralEasternPacificOceanRegion(PacificOceanRegion):
        pass

    class PacificCoastOfSouthAmericaRegion(GeographicRegion):
        pass

    class SouthAmericaRegion(GeographicRegion):
        pass

    class LongitudeBoundary(AbstractRegion):
        pass

    class SeaSurfaceTemperatureCondition(PhysicalQuality):
        pass

    class AirPressureCondition(PhysicalQuality):
        pass

    class HighAirPressureCondition(AirPressureCondition):
        pass

    class LowAirPressureCondition(AirPressureCondition):
        pass

    class BelowAverageSeaSurfaceTemperatureCondition(SeaSurfaceTemperatureCondition):
        pass

    class phaseOf(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [ClimateCycle]

    class associatedWithBand(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [OceanWaterBand]

    class associatedWithRegion(ObjectProperty):
        domain = [ClimatePhase, OceanWaterBand]
        range = [GeographicRegion]

    class developsIn(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [GeographicRegion]

    class boundedBy(ObjectProperty):
        domain = [OceanWaterBand]
        range = [LongitudeBoundary]

    class measuredBy(ObjectProperty, FunctionalProperty):
        domain = [ClimateCycle]
        range = [SeaSurfaceTemperatureCondition]

    class hasAirPressureCondition(ObjectProperty):
        domain = [ClimatePhase]
        range = [AirPressureCondition]

    class hasSeaSurfaceTemperatureCondition(ObjectProperty):
        domain = [ClimatePhase]
        range = [SeaSurfaceTemperatureCondition]

    class causes(ObjectProperty):
        domain = [ClimateCycle]
        range = [EnvironmentalChange]

    class language(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [Language]

    class meaning(DataProperty, FunctionalProperty):
        domain = [Term]
        range = [str]

    class literalTranslation(DataProperty, FunctionalProperty):
        domain = [Term]
        range = [str]

    class originalNameOf(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [ClimatePhase]

    class namedBy(ObjectProperty):
        domain = [Term]
        range = [SocialObject]

    class inReferenceTo(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [SocialAgent]

    class warmestAround(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [TimeInterval]

    class borders(ObjectProperty):
        domain = [Country]
        range = [GeographicRegion]

    class refersTo(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [ClimatePhase]

    class AgricultureFishingDependentCountry(DevelopingCountry):
        is_a = [
            specificallyDependsOn.some(Agriculture),
            specificallyDependsOn.some(Fishing),
        ]

    class PacificBorderingCountry(Country):
        is_a = [borders.some(PacificOceanRegion)]

    class PacificBorderingAgricultureFishingDependentCountry(
        AgricultureFishingDependentCountry,
        PacificBorderingCountry,
    ):
        pass

    class ElNinoPhenomenon(WarmPhase):
        pass

    class ElNinoSpanishTerm(Term):
        pass

    class LaNinaPhenomenon(CoolPhase):
        pass

    class LaNinaSpanishTerm(Term):
        pass

    ClimateCycle.label = ["climate cycle"]
    ClimatePhase.label = ["climate phase"]
    WarmPhase.label = ["warm phase"]
    CoolPhase.label = ["cool phase"]
    OceanWaterBand.label = ["band of warm ocean water"]
    EnvironmentalChange.label = ["environmental change"]
    TemperatureChange.label = ["temperature change"]
    RainfallChange.label = ["rainfall change"]
    Country.label = ["country"]
    DevelopingCountry.label = ["developing country"]
    AgricultureFishingDependentCountry.label = [
        "developing countries dependent upon agriculture and fishing",
    ]
    PacificBorderingCountry.label = ["countries bordering the Pacific Ocean"]
    PacificBorderingAgricultureFishingDependentCountry.label = [
        "developing countries dependent upon agriculture and fishing, particularly those bordering the Pacific Ocean",
    ]
    Agriculture.label = ["agriculture"]
    Fishing.label = ["fishing"]
    Language.label = ["language"]
    Term.label = ["term"]
    GeographicRegion.label = ["geographic region"]
    OceanRegion.label = ["oceanic region"]
    PacificOceanRegion.label = ["Pacific Ocean region"]
    EquatorialPacificRegion.label = ["equatorial Pacific region"]
    CentralEastCentralEquatorialPacificRegion.label = [
        "central and east-central equatorial Pacific region",
    ]
    WesternPacificRegion.label = ["western Pacific region"]
    EasternPacificRegion.label = ["eastern Pacific region"]
    TropicalCentralEasternPacificOceanRegion.label = [
        "tropical central and eastern Pacific Ocean region",
    ]
    PacificCoastOfSouthAmericaRegion.label = [
        "Pacific coast of South America region",
    ]
    SouthAmericaRegion.label = ["South America region"]
    LongitudeBoundary.label = ["longitude boundary"]
    SeaSurfaceTemperatureCondition.label = ["sea surface temperature"]
    AirPressureCondition.label = ["air pressure"]

    HighAirPressureCondition.label = ["high air pressure"]
    LowAirPressureCondition.label = ["low air pressure"]
    BelowAverageSeaSurfaceTemperatureCondition.label = [
        "below average sea surface temperature",
    ]
    ElNinoPhenomenon.label = ["El Niño"]
    ElNinoSpanishTerm.label = ["El Niño"]
    LaNinaPhenomenon.label = ["La Niña"]
    LaNinaSpanishTerm.label = ["La Niña"]

    enso = ClimateCycle("ElNinoSouthernOscillation")
    enso.label = ["El Niño Southern Oscillation", "ENSO"]

    el_nino = ElNinoPhenomenon("ElNinoPhenomenonInstance")
    el_nino.label = ["El Niño"]
    el_nino.phaseOf = enso

    el_nino_term = ElNinoSpanishTerm("ElNinoSpanishTermInstance")
    el_nino_term.label = ["El Niño"]
    american_spanish = Language("AmericanSpanish")
    american_spanish.label = ["American Spanish"]
    el_nino_term.language = american_spanish
    el_nino_term.meaning = "the boy"
    el_nino_term.refersTo = el_nino

    warm_water_band = OceanWaterBand("WarmOceanWaterBand")
    warm_water_band.label = ["band of warm ocean water"]
    warm_water_band.developsIn = central_pacific = CentralEastCentralEquatorialPacificRegion(
        "CentralEastCentralEquatorialPacific"
    )
    central_pacific.label = ["central and east-central equatorial Pacific"]
    warm_water_band.associatedWithRegion.append(central_pacific)
    pacific_coast_south_america = PacificCoastOfSouthAmericaRegion(
        "PacificCoastOfSouthAmerica"
    )
    pacific_coast_south_america.label = ["Pacific coast of South America"]
    warm_water_band.associatedWithRegion.append(pacific_coast_south_america)
    south_america = SouthAmericaRegion("SouthAmerica")
    south_america.label = ["South America"]
    pacific_coast_south_america.partOf.append(south_america)

    el_nino.associatedWithBand = warm_water_band
    el_nino.associatedWithRegion.append(pacific_coast_south_america)

    international_date_line = LongitudeBoundary("InternationalDateLine")
    international_date_line.label = ["International Date Line"]
    longitude_120_w = LongitudeBoundary("Longitude120West")
    longitude_120_w.label = ["120 ° W"]
    warm_water_band.boundedBy.append(international_date_line)
    warm_water_band.boundedBy.append(longitude_120_w)

    warm_water_band.warmestAround = christmas = TimeInterval("Christmas")
    christmas.label = ["Christmas"]

    pacific_ocean = PacificOceanRegion("PacificOcean")
    pacific_ocean.label = ["Pacific Ocean"]
    central_pacific.partOf.append(pacific_ocean)
    western_pacific = WesternPacificRegion("WesternPacific")
    western_pacific.label = ["western Pacific"]
    western_pacific.partOf.append(pacific_ocean)
    eastern_pacific = EasternPacificRegion("EasternPacific")
    eastern_pacific.label = ["eastern Pacific"]
    eastern_pacific.partOf.append(pacific_ocean)
    tropical_central_eastern_pacific = TropicalCentralEasternPacificOceanRegion(
        "TropicalCentralEasternPacificOcean"
    )
    tropical_central_eastern_pacific.label = ["tropical central and eastern Pacific Ocean"]
    tropical_central_eastern_pacific.partOf.append(pacific_ocean)

    sea_surface_temperature = SeaSurfaceTemperatureCondition(
        "SeaSurfaceTemperatureOfTropicalCentralEasternPacificOcean"
    )
    sea_surface_temperature.label = [
        "sea surface temperature, SST, of the tropical central and eastern Pacific Ocean",
        "SST",
    ]
    enso.measuredBy = sea_surface_temperature

    high_air_pressure_west = HighAirPressureCondition("HighAirPressureWesternPacific")
    high_air_pressure_west.label = ["high air pressure in the western Pacific"]
    low_air_pressure_east = LowAirPressureCondition("LowAirPressureEasternPacific")
    low_air_pressure_east.label = ["low air pressure in the eastern Pacific"]
    el_nino.hasAirPressureCondition.append(high_air_pressure_west)
    el_nino.hasAirPressureCondition.append(low_air_pressure_east)

    high_air_pressure_east = HighAirPressureCondition("HighAirPressureEasternPacific")
    high_air_pressure_east.label = ["high air pressure in the eastern Pacific"]
    low_air_pressure_west = LowAirPressureCondition("LowAirPressureWesternPacific")
    low_air_pressure_west.label = ["low air pressure in western Pacific"]

    la_nina = LaNinaPhenomenon("LaNinaPhenomenonInstance")
    la_nina.label = ["La Niña"]
    la_nina.phaseOf = enso
    la_nina.oppositeOf = el_nino
    below_average_sst_east = BelowAverageSeaSurfaceTemperatureCondition(
        "BelowAverageSeaSurfaceTemperatureEasternPacific"
    )
    below_average_sst_east.label = ["SST in the eastern Pacific below average"]
    la_nina.hasSeaSurfaceTemperatureCondition.append(below_average_sst_east)
    la_nina.hasAirPressureCondition.append(high_air_pressure_east)
    la_nina.hasAirPressureCondition.append(low_air_pressure_west)

    global_temperature_change = TemperatureChange("GlobalTemperatureChange")
    global_temperature_change.label = ["global changes of temperatures"]
    global_rainfall_change = RainfallChange("GlobalRainfallChange")
    global_rainfall_change.label = ["global changes of rainfall"]
    enso.causes.append(global_temperature_change)
    enso.causes.append(global_rainfall_change)

    enso.associatedWithRegion.append(pacific_coast_south_america)

    la_nina_term = LaNinaSpanishTerm("LaNinaSpanishTermInstance")
    la_nina_term.label = ["La Niña"]
    la_nina_term.language = american_spanish
    la_nina_term.literalTranslation = "the girl"
    la_nina_term.refersTo = la_nina

    el_nino_de_navidad = Term("ElNinoDeNavidad")
    el_nino_de_navidad.label = ["El Niño de Navidad"]
    el_nino_de_navidad.language = american_spanish
    el_nino_de_navidad.originalNameOf = el_nino
    peruvian_fishermen = SocialObject("PeruvianFishermen")
    peruvian_fishermen.label = ["Peruvian fishermen"]
    el_nino_de_navidad.namedBy.append(peruvian_fishermen)
    newborn_christ = SocialAgent("NewbornChrist")
    newborn_christ.label = ["newborn Christ"]
    el_nino_de_navidad.inReferenceTo = newborn_christ



graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
