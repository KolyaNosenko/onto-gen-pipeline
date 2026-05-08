"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

What is El Niño?
What larger climate phenomenon is El Niño a phase of?
What is ENSO?
What is the warm phase of the El Niño Southern Oscillation?
What is the cool phase of the El Niño Southern Oscillation?
What is La Niña?
With what oceanic condition is El Niño associated?
Where does the band of warm ocean water associated with El Niño develop?
Which parts of the Pacific Ocean are affected during El Niño?
Between which approximate longitudes does the warm water band of El Niño develop?
Does El Niño include waters off the Pacific coast of South America?
How are warm and cold phases in ENSO measured?
What role does sea surface temperature play in defining ENSO?
Which ocean region’s sea surface temperature is used to characterize ENSO?
What air pressure pattern accompanies El Niño?
Is air pressure high in the western Pacific during El Niño?
Is air pressure low in the eastern Pacific during El Niño?
What sea surface temperature condition characterizes La Niña?
Are sea surface temperatures in the eastern Pacific below average during La Niña?
What air pressure pattern accompanies La Niña?
Is air pressure high in the eastern Pacific during La Niña?
Is air pressure low in the western Pacific during La Niña?
What global effects do El Niño and La Niña cause?
How does the ENSO cycle affect global temperatures?
How does the ENSO cycle affect global rainfall?
Which countries are usually most affected by ENSO events?
Why are developing countries particularly affected by ENSO?
Which economic sectors are especially impacted by El Niño and La Niña?
Are countries dependent on agriculture and fishing especially vulnerable to ENSO?
Are countries bordering the Pacific Ocean usually most affected by ENSO?
What does the term “El Niño” mean in American Spanish?
Why is the phenomenon called “El Niño”?
When is the warm water near South America often at its warmest?
What is the origin of the name “El Niño de Navidad”?
Who originally named El Niño de Navidad?
To whom does the name “El Niño de Navidad” refer?
What does “La Niña” literally translate to?
How is the name “La Niña” related to El Niño?
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
    AbstractRegion,
    NonAgentiveSocialObject,
    PhysicalQuality,
    Process,
    SocialAgent,
    Society,
    SpaceRegion,
    State,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporalPartOf


with core:
    class ClimatePhenomenon(State):
        pass


    class ClimateOscillation(Process):
        pass


    class ClimatePhase(ClimatePhenomenon):
        pass


    class WarmClimatePhase(ClimatePhase):
        pass


    class CoolClimatePhase(ClimatePhase):
        pass


    class GeographicRegion(SpaceRegion):
        pass


    class OceanRegion(GeographicRegion):
        pass


    class CoastalRegion(GeographicRegion):
        pass


    class GeographicMarker(AbstractRegion):
        pass


    class ClimateMeasurement(PhysicalQuality):
        pass


    class SeaSurfaceTemperature(ClimateMeasurement):
        pass


    class EconomicSector(NonAgentiveSocialObject):
        pass


    class AgricultureSector(EconomicSector):
        pass


    class FishingSector(EconomicSector):
        pass


    class Country(Society):
        pass


    class DevelopingCountry(Country):
        pass


    class AgricultureAndFishingDependentDevelopingCountry(DevelopingCountry):
        pass


    class PacificBorderingAgricultureAndFishingDependentDevelopingCountry(
        AgricultureAndFishingDependentDevelopingCountry
    ):
        pass


    class LanguageVariant(NonAgentiveSocialObject):
        pass


    class HumanCommunity(Society):
        pass


    class ReligiousFigure(SocialAgent):
        pass


    class phaseOf(temporalPartOf):
        domain = [ClimatePhase]
        range = [ClimateOscillation]


    class associatedWithWarmWaterIn(ObjectProperty):
        domain = [WarmClimatePhase]
        range = [GeographicRegion]


    class developsIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]


    class includesWatersOff(ObjectProperty):
        domain = [ClimatePhase]
        range = [CoastalRegion]


    class boundedApproximatelyBy(ObjectProperty):
        domain = [ClimatePhase]
        range = [GeographicMarker]


    class measuredBy(ObjectProperty):
        domain = [ClimateOscillation]
        range = [ClimateMeasurement]


    class measuredInRegion(ObjectProperty):
        domain = [ClimateMeasurement]
        range = [OceanRegion]


    class hasHighAirPressureIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]


    class hasLowAirPressureIn(ObjectProperty):
        domain = [ClimatePhase]
        range = [OceanRegion]


    class hasBelowAverageSeaSurfaceTemperatureIn(ObjectProperty):
        domain = [CoolClimatePhase]
        range = [OceanRegion]


    class describedAs(DataProperty, FunctionalProperty):
        domain = [ClimateOscillation, ClimatePhase]
        range = [str]


    class associatedOceanicCondition(DataProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [str]


    class affectsGlobalTemperatures(DataProperty, FunctionalProperty):
        domain = [ClimateOscillation, ClimatePhase]
        range = [str]


    class affectsGlobalRainfall(DataProperty, FunctionalProperty):
        domain = [ClimateOscillation, ClimatePhase]
        range = [str]


    class dependsOnSector(ObjectProperty):
        domain = [Country]
        range = [EconomicSector]


    class borders(ObjectProperty):
        domain = [Country]
        range = [OceanRegion]


    class usuallyMostAffects(ObjectProperty):
        domain = [ClimateOscillation]
        range = [DevelopingCountry]


    class literalTranslation(DataProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [str]


    class namedInLanguage(ObjectProperty):
        domain = [ClimatePhase]
        range = [LanguageVariant]


    class originallyNamedAs(DataProperty, FunctionalProperty):
        domain = [ClimatePhase]
        range = [str]


    class namedBy(ObjectProperty):
        domain = [ClimatePhase]
        range = [HumanCommunity]


    class namedFor(ObjectProperty):
        domain = [ClimatePhase]
        range = [ReligiousFigure]


    class warmestAround(ObjectProperty):
        domain = [ClimatePhase]
        range = [TimeInterval]


    class oppositeOf(ObjectProperty):
        domain = [ClimatePhase]
        range = [ClimatePhase]


    ClimatePhase.is_a.append(phaseOf.some(ClimateOscillation))
    ClimateOscillation.is_a.append(measuredBy.some(ClimateMeasurement))
    AgricultureAndFishingDependentDevelopingCountry.is_a.append(
        dependsOnSector.some(AgricultureSector)
    )
    AgricultureAndFishingDependentDevelopingCountry.is_a.append(
        dependsOnSector.some(FishingSector)
    )
    PacificBorderingAgricultureAndFishingDependentDevelopingCountry.is_a.append(
        borders.some(OceanRegion)
    )
    ClimateOscillation.is_a.append(
        usuallyMostAffects.some(AgricultureAndFishingDependentDevelopingCountry)
    )
    ClimateOscillation.is_a.append(
        usuallyMostAffects.some(
            PacificBorderingAgricultureAndFishingDependentDevelopingCountry
        )
    )

    enso = ClimateOscillation("ElNinoSouthernOscillation")
    enso.label = ["El Niño Southern Oscillation", "ENSO"]

    el_nino = WarmClimatePhase("ElNino")
    el_nino.label = ["El Niño", "El Niño de Navidad"]

    la_nina = CoolClimatePhase("LaNina")
    la_nina.label = "La Niña"

    sea_surface_temperature = SeaSurfaceTemperature("SeaSurfaceTemperatureMeasure")
    sea_surface_temperature.label = ["sea surface temperature", "SST"]

    pacific_ocean = OceanRegion("PacificOcean")
    pacific_ocean.label = "Pacific Ocean"

    central_and_east_central_equatorial_pacific = OceanRegion(
        "CentralAndEastCentralEquatorialPacific"
    )
    central_and_east_central_equatorial_pacific.label = (
        "central and east-central equatorial Pacific"
    )

    tropical_central_and_eastern_pacific_ocean = OceanRegion(
        "TropicalCentralAndEasternPacificOcean"
    )
    tropical_central_and_eastern_pacific_ocean.label = (
        "tropical central and eastern Pacific Ocean"
    )

    western_pacific = OceanRegion("WesternPacific")
    western_pacific.label = "western Pacific"

    eastern_pacific = OceanRegion("EasternPacific")
    eastern_pacific.label = "eastern Pacific"

    south_america = GeographicRegion("SouthAmerica")
    south_america.label = "South America"

    pacific_coast_of_south_america = CoastalRegion("PacificCoastOfSouthAmerica")
    pacific_coast_of_south_america.label = "Pacific coast of South America"

    international_date_line = GeographicMarker("InternationalDateLine")
    international_date_line.label = "International Date Line"

    longitude_120_w = GeographicMarker("Longitude120W")
    longitude_120_w.label = "120 ° W"

    american_spanish = LanguageVariant("AmericanSpanish")
    american_spanish.label = "American Spanish"

    christmas = TimeInterval("Christmas")
    christmas.label = "Christmas"

    peruvian_fishermen = HumanCommunity("PeruvianFishermen")
    peruvian_fishermen.label = "Peruvian fishermen"

    christ = ReligiousFigure("Christ")
    christ.label = "Christ"

    enso.describedAs = "cycle of warm and cold temperatures"
    enso.measuredBy.append(sea_surface_temperature)
    enso.affectsGlobalTemperatures = "causes global changes"
    enso.affectsGlobalRainfall = "causes global changes"

    el_nino.describedAs = "warm phase"
    el_nino.phaseOf.append(enso)
    el_nino.associatedOceanicCondition = "band of warm ocean water"
    el_nino.literalTranslation = "the boy"
    el_nino.namedInLanguage.append(american_spanish)
    el_nino.originallyNamedAs = "El Niño de Navidad"
    el_nino.namedBy.append(peruvian_fishermen)
    el_nino.namedFor.append(christ)
    el_nino.warmestAround.append(christmas)
    el_nino.affectsGlobalTemperatures = "causes global changes"
    el_nino.affectsGlobalRainfall = "causes global changes"
    el_nino.associatedWithWarmWaterIn.append(
        central_and_east_central_equatorial_pacific
    )
    el_nino.associatedWithWarmWaterIn.append(pacific_coast_of_south_america)
    el_nino.developsIn.append(central_and_east_central_equatorial_pacific)
    el_nino.includesWatersOff.append(pacific_coast_of_south_america)
    el_nino.boundedApproximatelyBy.append(international_date_line)
    el_nino.boundedApproximatelyBy.append(longitude_120_w)
    el_nino.hasHighAirPressureIn.append(western_pacific)
    el_nino.hasLowAirPressureIn.append(eastern_pacific)

    la_nina.describedAs = "cool phase"
    la_nina.phaseOf.append(enso)
    la_nina.hasBelowAverageSeaSurfaceTemperatureIn.append(eastern_pacific)
    la_nina.hasHighAirPressureIn.append(eastern_pacific)
    la_nina.hasLowAirPressureIn.append(western_pacific)
    la_nina.literalTranslation = "the girl"
    la_nina.oppositeOf.append(el_nino)
    la_nina.affectsGlobalTemperatures = "causes global changes"
    la_nina.affectsGlobalRainfall = "causes global changes"

    sea_surface_temperature.measuredInRegion.append(
        tropical_central_and_eastern_pacific_ocean
    )

    central_and_east_central_equatorial_pacific.partOf.append(pacific_ocean)
    tropical_central_and_eastern_pacific_ocean.partOf.append(pacific_ocean)
    western_pacific.partOf.append(pacific_ocean)
    eastern_pacific.partOf.append(pacific_ocean)
    pacific_coast_of_south_america.partOf.append(south_america)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
