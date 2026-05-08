"""
=== TASK INPUT ===
Source text:
El Niño (; ) is the warm phase of the El Niño Southern Oscillation ( commonly called ENSO ) and is associated with a band of warm ocean water that develops in the central and east - central equatorial Pacific ( between approximately the International Date Line and 120 ° W ) , including off the Pacific coast of South America . El Niño Southern Oscillation refers to the cycle of warm and cold temperatures , as measured by sea surface temperature , SST , of the tropical central and eastern Pacific Ocean . El Niño is accompanied by high air pressure in the western Pacific and low air pressure in the eastern Pacific . The cool phase of ENSO is called " La Niña " with SST in the eastern Pacific below average and air pressures high in the eastern and low in western Pacific . The ENSO cycle , both El Niño and La Niña , cause global changes of both temperatures and rainfall . Developing countries that are dependent upon agriculture and fishing , particularly those bordering the Pacific Ocean , are usually most affected . In American Spanish , the capitalized term " El Niño " refers to " the boy " , so named because the pool of warm water in the Pacific near South America is often at its warmest around Christmas . The original name , " El Niño de Navidad " , traces its origin centuries back to Peruvian fishermen , who named the weather phenomenon in reference to the newborn Christ . " La Niña " , chosen as the ' opposite ' of El Niño , literally translates to " the girl " .

1. What is El Niño and how is it defined?
2. What are the geographic characteristics of El Niño, specifically its location in the Pacific Ocean?
3. What is the relationship between El Niño and the El Niño Southern Oscillation (ENSO)?
4. What ocean and atmospheric conditions characterize El Niño?
5. What is the cool phase of ENSO called and how does it differ from El Niño?
6. What are the atmospheric pressure patterns associated with El Niño in the western and eastern Pacific?
7. What global impacts does the ENSO cycle have on temperatures and rainfall?
8. Which countries and regions are most affected by El Niño and La Niña?
9. What is the seasonal timing of El Niño warming in the Pacific?
10. What is the historical origin of the term "El Niño" and its cultural significance?
11. How does La Niña differ from El Niño in terms of sea surface temperature and air pressure patterns?
12. Which economic sectors are most vulnerable to the effects of ENSO cycles?
13. What role do sea surface temperatures (SST) play in measuring the ENSO cycle?
14. Why is El Niño typically warmest around Christmas?
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
    State, Process, PhysicalQuality, Quality,
    NonAgentivePhysicalObject, SpaceRegion, TimeInterval
)


with core:
    # Domain entity classes
    class ElNino(State):
        """The warm phase of the El Niño Southern Oscillation (ENSO) cycle."""
        pass

    class LaNina(State):
        """The cool phase of the El Niño Southern Oscillation (ENSO) cycle."""
        pass

    class ENSO(Process):
        """The El Niño Southern Oscillation cycle of warm and cold temperatures."""
        pass

    class SeaSurfaceTemperature(PhysicalQuality):
        """Sea surface temperature (SST) measurement of ocean waters."""
        pass

    class AirPressure(PhysicalQuality):
        """Atmospheric air pressure quality."""
        pass

    class GlobalTemperatureChange(Quality):
        """Global changes in temperature caused by ENSO."""
        pass

    class GlobalRainfallChange(Quality):
        """Global changes in rainfall caused by ENSO."""
        pass

    class PacificOcean(NonAgentivePhysicalObject):
        """The Pacific Ocean body of water."""
        pass

    class SouthAmerica(SpaceRegion):
        """The South America geographic region."""
        pass

    # Domain ObjectProperty classes
    class isPhaseOf(ObjectProperty):
        """Relating a phase (warm or cool) to the ENSO cycle."""
        domain = [State]
        range = [Process]

    class locatedIn(ObjectProperty):
        """Relating a phenomenon to its geographic/oceanic location."""
        domain = [State, Process]
        range = [NonAgentivePhysicalObject, SpaceRegion]

    class measuredBy(ObjectProperty):
        """Relating a phenomenon to its measurement metric."""
        domain = [Process, State]
        range = [PhysicalQuality]

    class causesGlobalChange(ObjectProperty):
        """Relating ENSO cycle to global changes in climate."""
        domain = [Process]
        range = [Quality]

    class accompaniedByPressurePattern(ObjectProperty):
        """Relating a phase to its characteristic air pressure patterns."""
        domain = [State]
        range = [AirPressure]

    class peakWarmthDuring(ObjectProperty):
        """Indicating when El Niño reaches peak warmth."""
        domain = [State]
        range = [TimeInterval]

    class affectsRegion(ObjectProperty):
        """Relating ENSO to regions and countries it affects."""
        domain = [Process]
        range = [SpaceRegion]

    # Named instances from the source text
    el_nino = ElNino("ElNino_instance")
    el_nino.label = "El Niño"

    la_nina = LaNina("LaNina_instance")
    la_nina.label = "La Niña"

    enso_cycle = ENSO("ENSO_instance")
    enso_cycle.label = "ENSO"

    pacific_ocean_instance = PacificOcean("PacificOcean_instance")
    pacific_ocean_instance.label = "Pacific Ocean"

    south_america_instance = SouthAmerica("SouthAmerica_instance")
    south_america_instance.label = "South America"

    # Define phase relationships
    el_nino.isPhaseOf.append(enso_cycle)
    la_nina.isPhaseOf.append(enso_cycle)

    # Define locations
    el_nino.locatedIn.append(pacific_ocean_instance)
    la_nina.locatedIn.append(pacific_ocean_instance)
    enso_cycle.locatedIn.append(pacific_ocean_instance)
    el_nino.locatedIn.append(south_america_instance)

    # Define measurement
    enso_cycle.measuredBy.append(SeaSurfaceTemperature("SST_measurement"))

    # Define global impacts
    global_temp_change = GlobalTemperatureChange("GlobalTempChange_instance")
    global_temp_change.label = "global temperature change"
    enso_cycle.causesGlobalChange.append(global_temp_change)

    global_rainfall_change = GlobalRainfallChange("GlobalRainfallChange_instance")
    global_rainfall_change.label = "global rainfall change"
    enso_cycle.causesGlobalChange.append(global_rainfall_change)

    # Define pressure patterns for El Niño
    high_pressure_west = AirPressure("HighPressure_WesternPacific")
    high_pressure_west.label = "high air pressure in the western Pacific"
    el_nino.accompaniedByPressurePattern.append(high_pressure_west)

    low_pressure_east = AirPressure("LowPressure_EasternPacific")
    low_pressure_east.label = "low air pressure in the eastern Pacific"
    el_nino.accompaniedByPressurePattern.append(low_pressure_east)

    # Define pressure patterns for La Niña (opposite)
    high_pressure_east_nina = AirPressure("HighPressure_EasternPacific_LaNina")
    high_pressure_east_nina.label = "high air pressure in the eastern Pacific"
    la_nina.accompaniedByPressurePattern.append(high_pressure_east_nina)

    low_pressure_west_nina = AirPressure("LowPressure_WesternPacific_LaNina")
    low_pressure_west_nina.label = "low air pressure in the western Pacific"
    la_nina.accompaniedByPressurePattern.append(low_pressure_west_nina)

    # Define seasonal timing
    christmas_interval = TimeInterval("Christmas")
    christmas_interval.label = "Christmas"
    el_nino.peakWarmthDuring.append(christmas_interval)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
