"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

What is El Niño?
What larger climate pattern is El Niño a phase of?
What is the warm phase of the El Niño Southern Oscillation?
What is the cool phase of the El Niño Southern Oscillation?
What is La Niña?
How is ENSO defined in terms of ocean temperature variation?
What sea surface temperature conditions characterize El Niño?
What sea surface temperature conditions characterize La Niña?
In which part of the Pacific Ocean does El Niño develop?
What is the geographic extent of the warm ocean water associated with El Niño?
Does El Niño occur between the International Date Line and 120°W?
Is El Niño associated with waters off the Pacific coast of South America?
What air pressure conditions in the western Pacific accompany El Niño?
What air pressure conditions in the eastern Pacific accompany El Niño?
What air pressure conditions in the eastern Pacific accompany La Niña?
What air pressure conditions in the western Pacific accompany La Niña?
How are sea surface temperatures related to air pressure patterns during El Niño?
How are sea surface temperatures related to air pressure patterns during La Niña?
What global effects do El Niño and La Niña have on temperature?
What global effects do El Niño and La Niña have on rainfall?
Which regions or countries are usually most affected by the ENSO cycle?
Why are developing countries particularly affected by ENSO events?
Which economic sectors are especially vulnerable to El Niño and La Niña?
Are countries bordering the Pacific Ocean usually most affected by ENSO?
What does the term “El Niño” mean in American Spanish?
Why is the phenomenon called “El Niño”?
What is the origin of the name “El Niño de Navidad”?
Who originally named El Niño de Navidad?
Why did Peruvian fishermen name the phenomenon El Niño de Navidad?
When is the warm pool near South America often at its warmest?
What does the term “La Niña” literally mean?
How was the name “La Niña” chosen in relation to El Niño?
What are the opposite phases of ENSO?
What oceanic and atmospheric conditions distinguish El Niño from La Niña?
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
    class Phenomenon(Thing):
        pass

    class ClimatePattern(Phenomenon):
        pass

    class ClimatePhase(Phenomenon):
        pass

    class WarmClimatePhase(ClimatePhase):
        pass

    class CoolClimatePhase(ClimatePhase):
        pass

    class Place(Thing):
        pass

    class Ocean(Place):
        pass

    class OceanRegion(Place):
        pass

    class CoastRegion(OceanRegion):
        pass

    class Continent(Place):
        pass

    class BoundaryMarker(Place):
        pass

    class OceanWaterBody(Thing):
        pass

    class MeasurementIndicator(Thing):
        pass

    class Term(Thing):
        pass

    class LanguageVariety(Thing):
        pass

    class Holiday(Thing):
        pass

    class PersonGroup(Thing):
        pass

    class ReligiousFigure(Thing):
        pass

    class ClimateVariable(Thing):
        pass

    class CountryGroup(Thing):
        pass

    class EconomicSector(Thing):
        pass

    class phaseOf(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [ClimatePattern]

    class hasPhase(ObjectProperty):
        domain = [ClimatePattern]
        range = [ClimatePhase]

    class oppositeOf(ObjectProperty, SymmetricProperty):
        domain = [ClimatePhase, Term]
        range = [ClimatePhase, Term]

    class associatedWithWaterBody(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [OceanWaterBody]

    class developsInRegion(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase, OceanWaterBody, MeasurementIndicator]
        range = [Place]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class includesRegion(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class westBoundary(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [BoundaryMarker]

    class eastBoundary(ObjectProperty, FunctionalProperty):
        domain = [Place]
        range = [BoundaryMarker]

    class offCoastOf(ObjectProperty, FunctionalProperty):
        domain = [Place, OceanWaterBody]
        range = [Continent]

    class accompaniedByHighAirPressureIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]

    class accompaniedByLowAirPressureIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]

    class hasBelowAverageSeaSurfaceTemperatureIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]

    class measuredBy(ObjectProperty, FunctionalProperty):
        domain = [ClimatePattern]
        range = [MeasurementIndicator]

    class causesGlobalChangeIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [ClimateVariable]

    class alternativeNameFor(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [Thing]

    class usedInLanguage(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [LanguageVariety]

    class hasOriginalName(ObjectProperty, FunctionalProperty):
        domain = [ClimatePhase, Term]
        range = [Term]

    class namedBy(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [PersonGroup]

    class namedFor(ObjectProperty, FunctionalProperty):
        domain = [Term]
        range = [ReligiousFigure]

    class warmestAround(ObjectProperty, FunctionalProperty):
        domain = [OceanWaterBody]
        range = [Holiday]

    class dependsOnSector(ObjectProperty):
        domain = [CountryGroup]
        range = [EconomicSector]

    class bordersOcean(ObjectProperty, FunctionalProperty):
        domain = [CountryGroup]
        range = [Ocean]

    class usuallyAffects(ObjectProperty):
        domain = [ClimatePattern]
        range = [CountryGroup]

    class subgroupOf(ObjectProperty, TransitiveProperty):
        domain = [CountryGroup]
        range = [CountryGroup]

    class hasVulnerableSector(ObjectProperty):
        domain = [ClimatePattern]
        range = [EconomicSector]

    class hasTemperaturePattern(DataProperty, FunctionalProperty):
        domain = [ClimatePattern]
        range = [str]

    class hasSeaSurfaceTemperatureCondition(DataProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [str]

    class literalMeaning(DataProperty, FunctionalProperty):
        domain = [Term]
        range = [str]

    class namingReason(DataProperty, FunctionalProperty):
        domain = [Term]
        range = [str]

    class originDescription(DataProperty, FunctionalProperty):
        domain = [Term]
        range = [str]

    ElNinoSouthernOscillation = ClimatePattern("ElNinoSouthernOscillation")
    ElNinoSouthernOscillation.label = "El Niño Southern Oscillation"

    ElNino = WarmClimatePhase("ElNino")
    ElNino.label = "El Niño"

    LaNina = CoolClimatePhase("LaNina")
    LaNina.label = "La Niña"

    ENSO = Term("ENSO")
    ENSO.label = "ENSO"

    ElNinoTerm = Term("ElNinoTerm")
    ElNinoTerm.label = "El Niño"

    LaNinaTerm = Term("LaNinaTerm")
    LaNinaTerm.label = "La Niña"

    ElNinoDeNavidad = Term("ElNinoDeNavidad")
    ElNinoDeNavidad.label = "El Niño de Navidad"

    SeaSurfaceTemperature = MeasurementIndicator("SeaSurfaceTemperature")
    SeaSurfaceTemperature.label = ["sea surface temperature", "SST"]

    PacificOcean = Ocean("PacificOcean")
    PacificOcean.label = ["Pacific Ocean", "Pacific"]

    SouthAmerica = Continent("SouthAmerica")
    SouthAmerica.label = "South America"

    InternationalDateLine = BoundaryMarker("InternationalDateLine")
    InternationalDateLine.label = "International Date Line"

    Longitude120W = BoundaryMarker("Longitude120W")
    Longitude120W.label = "120 ° W"

    CentralAndEastCentralEquatorialPacific = OceanRegion("CentralAndEastCentralEquatorialPacific")
    CentralAndEastCentralEquatorialPacific.label = "central and east - central equatorial Pacific"

    TropicalCentralAndEasternPacificOcean = OceanRegion("TropicalCentralAndEasternPacificOcean")
    TropicalCentralAndEasternPacificOcean.label = "tropical central and eastern Pacific Ocean"

    WesternPacific = OceanRegion("WesternPacific")
    WesternPacific.label = "western Pacific"

    EasternPacific = OceanRegion("EasternPacific")
    EasternPacific.label = "eastern Pacific"

    PacificCoastOfSouthAmerica = CoastRegion("PacificCoastOfSouthAmerica")
    PacificCoastOfSouthAmerica.label = "Pacific coast of South America"

    WarmWaterPool = OceanWaterBody("WarmWaterPool")
    WarmWaterPool.label = ["band of warm ocean water", "pool of warm water in the Pacific near South America"]

    AmericanSpanish = LanguageVariety("AmericanSpanish")
    AmericanSpanish.label = "American Spanish"

    Christmas = Holiday("Christmas")
    Christmas.label = "Christmas"

    Christ = ReligiousFigure("Christ")
    Christ.label = "Christ"

    PeruvianFishermen = PersonGroup("PeruvianFishermen")
    PeruvianFishermen.label = "Peruvian fishermen"

    Temperatures = ClimateVariable("Temperatures")
    Temperatures.label = "temperatures"

    Rainfall = ClimateVariable("Rainfall")
    Rainfall.label = "rainfall"

    Agriculture = EconomicSector("Agriculture")
    Agriculture.label = "agriculture"

    Fishing = EconomicSector("Fishing")
    Fishing.label = "fishing"

    DevelopingCountries = CountryGroup("DevelopingCountries")
    DevelopingCountries.label = "Developing countries"

    AgricultureAndFishingDependentDevelopingCountries = CountryGroup("AgricultureAndFishingDependentDevelopingCountries")
    AgricultureAndFishingDependentDevelopingCountries.label = "Developing countries that are dependent upon agriculture and fishing"

    PacificOceanBorderingCountries = CountryGroup("PacificOceanBorderingCountries")
    PacificOceanBorderingCountries.label = "those bordering the Pacific Ocean"

    ElNino.phaseOf = ElNinoSouthernOscillation
    LaNina.phaseOf = ElNinoSouthernOscillation
    ElNinoSouthernOscillation.hasPhase = [ElNino, LaNina]
    ElNino.oppositeOf = [LaNina]
    ElNino.associatedWithWaterBody = WarmWaterPool
    ElNino.developsInRegion = CentralAndEastCentralEquatorialPacific
    ElNino.hasSeaSurfaceTemperatureCondition = "warm ocean water in the central and east - central equatorial Pacific"
    ElNino.accompaniedByHighAirPressureIn = [WesternPacific]
    ElNino.accompaniedByLowAirPressureIn = [EasternPacific]
    ElNino.causesGlobalChangeIn = [Temperatures, Rainfall]
    ElNino.hasOriginalName = ElNinoDeNavidad

    LaNina.hasSeaSurfaceTemperatureCondition = "SST in the eastern Pacific below average"
    LaNina.hasBelowAverageSeaSurfaceTemperatureIn = [EasternPacific]
    LaNina.accompaniedByHighAirPressureIn = [EasternPacific]
    LaNina.accompaniedByLowAirPressureIn = [WesternPacific]
    LaNina.causesGlobalChangeIn = [Temperatures, Rainfall]

    ENSO.alternativeNameFor = ElNinoSouthernOscillation

    ElNinoTerm.alternativeNameFor = ElNino
    ElNinoTerm.usedInLanguage = AmericanSpanish
    ElNinoTerm.literalMeaning = "the boy"
    ElNinoTerm.namingReason = "the pool of warm water in the Pacific near South America is often at its warmest around Christmas"

    LaNinaTerm.alternativeNameFor = LaNina
    LaNinaTerm.literalMeaning = "the girl"
    LaNinaTerm.namingReason = "chosen as the opposite of El Niño"
    LaNinaTerm.oppositeOf = [ElNinoTerm]

    ElNinoDeNavidad.alternativeNameFor = ElNino
    ElNinoDeNavidad.originDescription = "traces its origin centuries back to Peruvian fishermen"
    ElNinoDeNavidad.namedBy = PeruvianFishermen
    ElNinoDeNavidad.namedFor = Christ

    ElNinoSouthernOscillation.measuredBy = SeaSurfaceTemperature
    ElNinoSouthernOscillation.hasTemperaturePattern = "cycle of warm and cold temperatures"
    ElNinoSouthernOscillation.usuallyAffects = [
        AgricultureAndFishingDependentDevelopingCountries,
        PacificOceanBorderingCountries,
    ]
    ElNinoSouthernOscillation.hasVulnerableSector = [Agriculture, Fishing]

    SeaSurfaceTemperature.developsInRegion = TropicalCentralAndEasternPacificOcean

    CentralAndEastCentralEquatorialPacific.partOf = [PacificOcean]
    CentralAndEastCentralEquatorialPacific.westBoundary = InternationalDateLine
    CentralAndEastCentralEquatorialPacific.eastBoundary = Longitude120W
    CentralAndEastCentralEquatorialPacific.includesRegion = [PacificCoastOfSouthAmerica]

    TropicalCentralAndEasternPacificOcean.partOf = [PacificOcean]
    WesternPacific.partOf = [PacificOcean]
    EasternPacific.partOf = [PacificOcean]
    PacificCoastOfSouthAmerica.offCoastOf = SouthAmerica

    WarmWaterPool.developsInRegion = CentralAndEastCentralEquatorialPacific
    WarmWaterPool.offCoastOf = SouthAmerica
    WarmWaterPool.warmestAround = Christmas

    AgricultureAndFishingDependentDevelopingCountries.subgroupOf = [DevelopingCountries]
    AgricultureAndFishingDependentDevelopingCountries.dependsOnSector = [Agriculture, Fishing]
    PacificOceanBorderingCountries.subgroupOf = [AgricultureAndFishingDependentDevelopingCountries]
    PacificOceanBorderingCountries.bordersOcean = PacificOcean


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
