"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

Competency questions — natural-language queries the ontology should
support; your output must contain enough classes, properties, and
individuals to answer every one of them:
1. What is El Niño and which phase of the El Niño Southern Oscillation (ENSO) does it represent?  
2. What oceanic region is associated with El Niño’s warm band of water?  
3. Between which longitudinal boundaries does the El Niño warm water band typically develop?  
4. Does El Niño include waters off the Pacific coast of South America?  
5. What does El Niño Southern Oscillation (ENSO) refer to?  
6. What variables are used to measure the warm and cold phases of ENSO?  
7. What air pressure conditions accompany El Niño in the western and eastern Pacific?  
8. What is the cool phase of ENSO called?  
9. What sea surface temperature conditions characterize La Niña in the eastern Pacific?  
10. What air pressure conditions accompany La Niña in the eastern and western Pacific?  
11. What global changes are caused by the ENSO cycle?  
12. Which populations are usually most affected by ENSO-related changes?  
13. Which sectors are especially affected by ENSO in developing countries?  
14. Which countries or regions bordering the Pacific Ocean are particularly affected by ENSO?  
15. What does the term “El Niño” mean in American Spanish?  
16. Why was the phenomenon named “El Niño de Navidad”?  
17. Who originally named the weather phenomenon El Niño, and in what context?  
18. What does “La Niña” literally translate to, and why was it chosen as the opposite of El Niño?
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
    class ClimatePhenomenon(Thing):
        pass

    class WeatherPhenomenon(ClimatePhenomenon):
        pass

    class Oscillation(ClimatePhenomenon):
        pass

    class ENSOCycle(Oscillation):
        pass

    class ENSOPhase(ClimatePhenomenon):
        pass

    class WarmPhase(ENSOPhase):
        pass

    class CoolPhase(ENSOPhase):
        pass

    class OceanWaterBand(Thing):
        pass

    class OceanRegion(Thing):
        pass

    class PacificRegion(OceanRegion):
        pass

    class Ocean(Thing):
        pass

    class SeaSurfaceTemperatureVariable(Thing):
        pass

    class SeaSurfaceTemperatureCondition(Thing):
        pass

    class AirPressureCondition(Thing):
        pass

    class GlobalChange(Thing):
        pass

    class TemperatureChange(GlobalChange):
        pass

    class RainfallChange(GlobalChange):
        pass

    class CountryGroup(Thing):
        pass

    class DevelopingCountry(CountryGroup):
        pass

    class Sector(Thing):
        pass

    class AgricultureSector(Sector):
        pass

    class FishingSector(Sector):
        pass

    class Language(Thing):
        pass

    class Acronym(Thing):
        pass

    class ReligiousFigure(Thing):
        pass

    class FishermenGroup(Thing):
        pass

    class Holiday(Thing):
        pass

    class GeographicalBoundary(Thing):
        pass

    class LongitudeBoundary(GeographicalBoundary):
        pass

    class Continent(Thing):
        pass

    class phaseOf(ObjectProperty, FunctionalProperty):
        domain = [ENSOPhase]
        range = [ENSOCycle]

    class associatedWith(ObjectProperty):
        domain = [Thing]
        range = [Thing]

    class developsIn(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [OceanRegion]

    class westernBoundary(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [LongitudeBoundary]

    class easternBoundary(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [LongitudeBoundary]

    class includesRegion(ObjectProperty):
        domain = [OceanWaterBand]
        range = [OceanRegion]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    class measuredBy(ObjectProperty):
        domain = [ENSOCycle]
        range = [SeaSurfaceTemperatureVariable]

    class occursIn(ObjectProperty, FunctionalProperty):
        domain = [ENSOCycle]
        range = [OceanRegion]

    class abbreviates(ObjectProperty, FunctionalProperty):
        domain = [Acronym]
        range = [Thing]

    class inRegion(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [OceanRegion]

    class accompaniedBy(ObjectProperty):
        domain = [ClimatePhenomenon]
        range = [AirPressureCondition]

    class hasSeaSurfaceTemperatureCondition(ObjectProperty, FunctionalProperty):
        domain = [ENSOPhase]
        range = [SeaSurfaceTemperatureCondition]

    class causes(ObjectProperty):
        domain = [ENSOCycle]
        range = [GlobalChange]

    class dependentUpon(ObjectProperty):
        domain = [CountryGroup]
        range = [Sector]

    class bordering(ObjectProperty):
        domain = [CountryGroup]
        range = [Ocean]

    class mostAffectedBy(ObjectProperty, FunctionalProperty):
        domain = [CountryGroup]
        range = [ENSOCycle]

    class usedInLanguage(ObjectProperty, FunctionalProperty):
        domain = [Thing]
        range = [Language]

    class meansText(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class literallyTranslatesTo(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class definitionText(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]

    class namedInReferenceTo(ObjectProperty, FunctionalProperty):
        domain = [WeatherPhenomenon]
        range = [Thing]

    class namedBy(ObjectProperty, FunctionalProperty):
        domain = [WeatherPhenomenon]
        range = [FishermenGroup]

    class originalNameFor(ObjectProperty, FunctionalProperty):
        domain = [WeatherPhenomenon]
        range = [Thing]

    class occursAround(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBand]
        range = [Holiday]

    class oppositeOf(ObjectProperty, SymmetricProperty):
        domain = [Thing]
        range = [Thing]

    WarmPhase.is_a.append(phaseOf.some(ENSOCycle))
    CoolPhase.is_a.append(phaseOf.some(ENSOCycle))
    ENSOCycle.is_a.append(measuredBy.some(SeaSurfaceTemperatureVariable))
    ENSOCycle.is_a.append(causes.some(TemperatureChange))
    ENSOCycle.is_a.append(causes.some(RainfallChange))
    DevelopingCountry.is_a.append(dependentUpon.some(AgricultureSector))
    DevelopingCountry.is_a.append(dependentUpon.some(FishingSector))

    PacificOcean = Ocean("PacificOcean")
    PacificOcean.label = "Pacific Ocean"

    SouthAmerica = Continent("SouthAmerica")
    SouthAmerica.label = "South America"

    InternationalDateLine = LongitudeBoundary("InternationalDateLine")
    InternationalDateLine.label = "International Date Line"

    West120W = LongitudeBoundary("West120W")
    West120W.label = "120 ° W"

    CentralAndEastCentralEquatorialPacific = OceanRegion("CentralAndEastCentralEquatorialPacific")
    CentralAndEastCentralEquatorialPacific.label = "the central and east - central equatorial Pacific"
    CentralAndEastCentralEquatorialPacific.partOf = [PacificOcean]

    TropicalCentralAndEasternPacificOcean = OceanRegion("TropicalCentralAndEasternPacificOcean")
    TropicalCentralAndEasternPacificOcean.label = "the tropical central and eastern Pacific Ocean"
    TropicalCentralAndEasternPacificOcean.partOf = [PacificOcean]

    PacificCoastOfSouthAmerica = OceanRegion("PacificCoastOfSouthAmerica")
    PacificCoastOfSouthAmerica.label = "the Pacific coast of South America"
    PacificCoastOfSouthAmerica.partOf = [SouthAmerica]

    WesternPacific = PacificRegion("WesternPacific")
    WesternPacific.label = "the western Pacific"
    WesternPacific.partOf = [PacificOcean]

    EasternPacific = PacificRegion("EasternPacific")
    EasternPacific.label = "the eastern Pacific"
    EasternPacific.partOf = [PacificOcean]

    SeaSurfaceTemperature = SeaSurfaceTemperatureVariable("SeaSurfaceTemperature")
    SeaSurfaceTemperature.label = "sea surface temperature"

    SST = SeaSurfaceTemperatureVariable("SST", is_a=[Acronym])
    SST.label = "SST"
    SST.abbreviates = SeaSurfaceTemperature

    ENSO = Acronym("ENSO")
    ENSO.label = "ENSO"

    ElNinoSouthernOscillation = ENSOCycle("ElNinoSouthernOscillation")
    ElNinoSouthernOscillation.label = "El Niño Southern Oscillation"
    ElNinoSouthernOscillation.definitionText = "the cycle of warm and cold temperatures as measured by sea surface temperature, SST, of the tropical central and eastern Pacific Ocean"
    ElNinoSouthernOscillation.measuredBy = [SeaSurfaceTemperature, SST]
    ElNinoSouthernOscillation.occursIn = TropicalCentralAndEasternPacificOcean
    ENSO.abbreviates = ElNinoSouthernOscillation

    ElNinoWarmBand = OceanWaterBand("ElNinoWarmBand")
    ElNinoWarmBand.label = "a band of warm ocean water"
    ElNinoWarmBand.definitionText = "a band of warm ocean water that develops in the central and east-central equatorial Pacific"
    ElNinoWarmBand.developsIn = CentralAndEastCentralEquatorialPacific
    ElNinoWarmBand.westernBoundary = InternationalDateLine
    ElNinoWarmBand.easternBoundary = West120W
    ElNinoWarmBand.includesRegion = [PacificCoastOfSouthAmerica]


    HighAirPressureWesternPacific = AirPressureCondition("HighAirPressureWesternPacific")
    HighAirPressureWesternPacific.label = "high air pressure in the western Pacific"
    HighAirPressureWesternPacific.inRegion = WesternPacific

    LowAirPressureEasternPacific = AirPressureCondition("LowAirPressureEasternPacific")
    LowAirPressureEasternPacific.label = "low air pressure in the eastern Pacific"
    LowAirPressureEasternPacific.inRegion = EasternPacific

    HighAirPressureEasternPacific = AirPressureCondition("HighAirPressureEasternPacific")
    HighAirPressureEasternPacific.label = "air pressures high in the eastern Pacific"
    HighAirPressureEasternPacific.inRegion = EasternPacific

    LowAirPressureWesternPacific = AirPressureCondition("LowAirPressureWesternPacific")
    LowAirPressureWesternPacific.label = "low air pressure in the western Pacific"
    LowAirPressureWesternPacific.inRegion = WesternPacific

    BelowAverageSSTEasternPacific = SeaSurfaceTemperatureCondition("BelowAverageSSTEasternPacific")
    BelowAverageSSTEasternPacific.label = "SST in the eastern Pacific below average"
    BelowAverageSSTEasternPacific.inRegion = EasternPacific

    AmericanSpanish = Language("AmericanSpanish")
    AmericanSpanish.label = "American Spanish"

    Christ = ReligiousFigure("Christ")
    Christ.label = "Christ"

    Christmas = Holiday("Christmas")
    Christmas.label = "Christmas"
    ElNinoWarmBand.occursAround = Christmas

    PeruvianFishermen = FishermenGroup("PeruvianFishermen")
    PeruvianFishermen.label = "Peruvian fishermen"

    ElNinoDeNavidad = WeatherPhenomenon("ElNinoDeNavidad")
    ElNinoDeNavidad.label = "El Niño de Navidad"
    ElNinoDeNavidad.definitionText = "the original name of the weather phenomenon"
    ElNinoDeNavidad.namedBy = PeruvianFishermen
    ElNinoDeNavidad.namedInReferenceTo = Christ


    Agriculture = AgricultureSector("agriculture")
    Agriculture.label = "agriculture"

    Fishing = FishingSector("fishing")
    Fishing.label = "fishing"

    DevelopingCountries = DevelopingCountry("DevelopingCountries")
    DevelopingCountries.label = "developing countries"
    DevelopingCountries.dependentUpon = [Agriculture, Fishing]
    DevelopingCountries.bordering = [PacificOcean]
    DevelopingCountries.mostAffectedBy = ElNinoSouthernOscillation

    ElNino = WarmPhase("ElNino")
    ElNino.label = "El Niño"
    ElNino.definitionText = "the warm phase of the El Niño Southern Oscillation (commonly called ENSO)"
    ElNino.phaseOf = ElNinoSouthernOscillation
    ElNino.associatedWith = [ElNinoWarmBand]
    ElNino.accompaniedBy = [HighAirPressureWesternPacific, LowAirPressureEasternPacific]
    ElNino.usedInLanguage = AmericanSpanish
    ElNino.meansText = "the boy"
    ElNinoDeNavidad.originalNameFor = ElNino

    LaNina = CoolPhase("LaNina")
    LaNina.label = "La Niña"
    LaNina.definitionText = "the cool phase of ENSO"
    LaNina.phaseOf = ElNinoSouthernOscillation
    LaNina.associatedWith = [ElNinoWarmBand]
    LaNina.accompaniedBy = [HighAirPressureEasternPacific, LowAirPressureWesternPacific]
    LaNina.hasSeaSurfaceTemperatureCondition = BelowAverageSSTEasternPacific
    LaNina.oppositeOf = [ElNino]
    LaNina.literallyTranslatesTo = "the girl"

    ElNinoWarmBand.associatedWith = [ElNino]



graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
