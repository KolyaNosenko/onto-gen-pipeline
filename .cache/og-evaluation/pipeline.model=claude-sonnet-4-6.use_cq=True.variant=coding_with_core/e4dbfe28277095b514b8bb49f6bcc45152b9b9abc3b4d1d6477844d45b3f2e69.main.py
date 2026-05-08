"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

1. What is El Niño and which phase of the ENSO cycle does it represent?
2. Where does the band of warm ocean water associated with El Niño develop?
3. What does ENSO stand for and what does it measure?
4. What are the air pressure conditions associated with El Niño in the western and eastern Pacific?
5. What is the cool phase of ENSO called and what are its characteristics?
6. What global changes are caused by the ENSO cycle?
7. Which countries are most affected by El Niño and La Niña?
8. What is the literal meaning of the term "El Niño" in American Spanish?
9. Why was the weather phenomenon named "El Niño"?
10. What is the origin of the name "El Niño de Navidad"?
11. Who originally named the El Niño weather phenomenon?
12. What is the literal translation of "La Niña" and why was it chosen as a name?
13. What is the geographical range of the warm ocean water associated with El Niño?
14. How does La Niña differ from El Niño in terms of sea surface temperature?
15. What is the relationship between El Niño and the Pacific coast of South America?
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
    Process, State, AmountOfMatter, Feature,
    NonAgentivePhysicalObject, PhysicalQuality, TimeInterval,
    AgentivePhysicalObject,
)
from og_sandbox_with_core.core.properties import temporalPartOf


with core:
    # ── Entity Classes ─────────────────────────────────────────────────────────

    class WeatherPhenomenon(Process):
        """A recurring atmospheric or oceanic phenomenon."""

    class ClimateCycle(WeatherPhenomenon):
        """A cyclical climate process with alternating warm and cool phases."""

    class ClimatePhase(State):
        """A phase within a climate cycle characterised by consistent conditions."""

    class WarmClimatePhase(ClimatePhase):
        """A climate phase with above-average sea-surface temperatures."""

    class CoolClimatePhase(ClimatePhase):
        """A climate phase with below-average sea-surface temperatures."""

    class OceanWaterBand(AmountOfMatter):
        """A band of ocean water defined by its temperature and equatorial location."""

    class OceanBody(NonAgentivePhysicalObject):
        """A named body of ocean or sea water."""

    class Continent(NonAgentivePhysicalObject):
        """A large continuous landmass."""

    class GeographicLine(Feature):
        """A line-based geographic boundary or reference feature."""

    class SeaSurfaceTemperature(PhysicalQuality):
        """Temperature of the ocean surface; the primary ENSO measurement."""

    class AirPressure(PhysicalQuality):
        """Atmospheric pressure at or near sea level over an ocean region."""

    # ── Properties ─────────────────────────────────────────────────────────────

    class isPhaseOf(temporalPartOf):
        """Relates a climate phase to the climate cycle it is part of."""
        domain = [ClimatePhase]
        range  = [ClimateCycle]

    class associatedWith(ObjectProperty):
        """Relates a climate phase to its characteristic ocean-water band."""
        domain = [ClimatePhase]
        range  = [OceanWaterBand]

    class developsIn(ObjectProperty):
        """Relates an ocean-water band to the ocean body where it forms."""
        domain = [OceanWaterBand]
        range  = [OceanBody]

    class occursNear(ObjectProperty):
        """Relates an ocean-water band to a nearby continent."""
        domain = [OceanWaterBand]
        range  = [Continent]

    class measuredBy(ObjectProperty):
        """Relates a climate cycle to the quality used to measure it."""
        domain = [ClimateCycle]
        range  = [SeaSurfaceTemperature]

    class namedInReferenceToTime(ObjectProperty):
        """Relates a climate phase to the seasonal interval after which it was named."""
        domain = [ClimatePhase]
        range  = [TimeInterval]

    class namedInReferenceToEntity(ObjectProperty):
        """Relates a weather phenomenon to the entity whose name it references."""
        domain = [WeatherPhenomenon]
        range  = [AgentivePhysicalObject]

    class originalNameFor(ObjectProperty):
        """Relates an older name of a phenomenon to the phenomenon itself."""
        domain = [WeatherPhenomenon]
        range  = [WeatherPhenomenon]

    class literalMeaning(DataProperty, FunctionalProperty):
        """Literal English translation of a Spanish climate-phase name."""
        domain = [ClimatePhase]
        range  = [str]

    class abbreviatedAs(DataProperty, FunctionalProperty):
        """Standard abbreviation for a climate cycle name."""
        domain = [ClimateCycle]
        range  = [str]

    class causesGlobalChangeIn(DataProperty):
        """Names a global quantity (e.g. temperature, rainfall) the cycle alters."""
        domain = [ClimateCycle]
        range  = [str]

    class westernPacificAirPressure(DataProperty, FunctionalProperty):
        """High or low air pressure over the western Pacific during a climate phase."""
        domain = [ClimatePhase]
        range  = [str]

    class easternPacificAirPressure(DataProperty, FunctionalProperty):
        """High or low air pressure over the eastern Pacific during a climate phase."""
        domain = [ClimatePhase]
        range  = [str]

    class sstCondition(DataProperty, FunctionalProperty):
        """Describes the sea-surface temperature condition during a climate phase."""
        domain = [ClimatePhase]
        range  = [str]

    # ── Named Individuals ──────────────────────────────────────────────────────

    # El Niño Southern Oscillation (ENSO)
    enso = ClimateCycle("ElNinoSouthernOscillation")
    enso.label = "El Niño Southern Oscillation"
    enso.abbreviatedAs = "ENSO"
    enso.causesGlobalChangeIn.append("temperature")
    enso.causesGlobalChangeIn.append("rainfall")

    # Pacific Ocean
    pacific = OceanBody("PacificOcean")
    pacific.label = "Pacific Ocean"

    # South America
    south_america = Continent("SouthAmerica")
    south_america.label = "South America"

    # International Date Line
    idl = GeographicLine("InternationalDateLine")
    idl.label = "International Date Line"

    # Christmas (seasonal time interval after which El Niño is named)
    christmas = TimeInterval("Christmas")
    christmas.label = "Christmas"

    # Christ (the entity in reference to whom El Niño de Navidad was named)
    christ = AgentivePhysicalObject("Christ")
    christ.label = "Christ"

    # Band of warm ocean water associated with El Niño
    warm_water = OceanWaterBand("WarmOceanWaterBand")
    warm_water.label = "band of warm ocean water"
    warm_water.developsIn.append(pacific)
    warm_water.occursNear.append(south_america)

    # Sea-surface temperature quality of the tropical Pacific (ENSO measurement)
    pacific_sst = SeaSurfaceTemperature("TropicalPacificSST")
    pacific_sst.label = "SST"
    enso.measuredBy.append(pacific_sst)

    # El Niño (warm phase)
    elnino = WarmClimatePhase("ElNino")
    elnino.label = "El Niño"
    elnino.literalMeaning = "the boy"
    elnino.isPhaseOf.append(enso)
    elnino.associatedWith.append(warm_water)
    elnino.westernPacificAirPressure = "high"
    elnino.easternPacificAirPressure = "low"
    elnino.namedInReferenceToTime.append(christmas)

    # El Niño de Navidad (original name for El Niño)
    elnino_navidad = WarmClimatePhase("ElNinoDeNavidad")
    elnino_navidad.label = "El Niño de Navidad"
    elnino_navidad.isPhaseOf.append(enso)
    elnino_navidad.originalNameFor.append(elnino)
    elnino_navidad.namedInReferenceToEntity.append(christ)
    elnino_navidad.namedInReferenceToTime.append(christmas)

    # La Niña (cool phase)
    lanina = CoolClimatePhase("LaNina")
    lanina.label = "La Niña"
    lanina.literalMeaning = "the girl"
    lanina.isPhaseOf.append(enso)
    lanina.westernPacificAirPressure = "low"
    lanina.easternPacificAirPressure = "high"
    lanina.sstCondition = "below average in eastern Pacific"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
