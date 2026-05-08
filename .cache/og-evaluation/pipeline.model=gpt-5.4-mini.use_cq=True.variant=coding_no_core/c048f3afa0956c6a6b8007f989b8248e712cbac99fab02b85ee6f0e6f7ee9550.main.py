"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the long-term impacts of climate change in Germany?
2. How does climate change affect agriculture in Germany?
3. What extreme weather events associated with climate change are impacting Germany?
4. How does climate change affect water availability in Germany?
5. What mitigation strategies has Germany adopted in response to climate change?
6. What changes have occurred in Germany’s energy sector due to climate change debates?
7. What is Germany’s Energiewende and why is it politically significant?
8. How has the Energiewende affected coalition talks in German politics?
9. What role has Germany played in renewable energy investment?
10. Has Germany been successful in reducing coal production and usage?
11. What is Germany’s position in coal imports within Europe?
12. How much coal does Germany produce relative to other EU countries?
13. What share of global coal production is associated with Germany?
14. Which climate conference did Germany host in Bonn?
15. How did the German delegation travel to COP23, and what commitment was this intended to demonstrate?
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
    class Country(Thing):
        pass

    class Region(Thing):
        pass

    class Continent(Region):
        pass

    class City(Thing):
        pass

    class Organization(Thing):
        pass

    class PoliticalParty(Organization):
        pass

    class Person(Thing):
        pass

    class Politics(Thing):
        pass

    class PoliticalIssue(Thing):
        pass

    class PoliticalProcess(Thing):
        pass

    class Conference(Thing):
        pass

    class Delegation(Thing):
        pass

    class Train(Thing):
        pass

    class ClimateChange(Thing):
        pass

    class AnthropogenicClimateChange(ClimateChange):
        pass

    class ClimateImpact(Thing):
        pass

    class Sector(Thing):
        pass

    class Agriculture(Sector):
        pass

    class EnergySector(Sector):
        pass

    class Strategy(Thing):
        pass

    class MitigationStrategy(Strategy):
        pass

    class EnergyTransition(PoliticalIssue):
        pass

    class WeatherEvent(ClimateImpact):
        pass

    class Heatwave(WeatherEvent):
        pass

    class Coldwave(WeatherEvent):
        pass

    class Flooding(WeatherEvent):
        pass

    class WaterAvailabilityIssue(ClimateImpact):
        pass

    class Coal(Thing):
        pass

    class CoalProduction(Thing):
        pass

    class CoalUsage(Thing):
        pass

    class RenewableEnergy(Thing):
        pass

    class CarbonNeutrality(Thing):
        pass

    class affects(ObjectProperty):
        domain = [ClimateChange]
        range = [Thing]

    class hasImpact(ObjectProperty):
        domain = [ClimateChange]
        range = [ClimateImpact]

    class sparksChangeIn(ObjectProperty):
        domain = [ClimateChange]
        range = [Thing]

    class isPoliticalIssueIn(ObjectProperty):
        domain = [PoliticalIssue]
        range = [Politics]

    class makesDifficultFor(ObjectProperty):
        domain = [PoliticalIssue]
        range = [Thing]

    class affiliatedWith(ObjectProperty):
        domain = [Organization]
        range = [Person]

    class investsIn(ObjectProperty):
        domain = [Country]
        range = [Thing]

    class strugglesToReduce(ObjectProperty):
        domain = [Country]
        range = [Thing]

    class importsCommodity(ObjectProperty):
        domain = [Country]
        range = [Thing]

    class producesCommodity(ObjectProperty):
        domain = [Country]
        range = [Thing]

    class ranksBehindInProductionOf(ObjectProperty):
        domain = [Country]
        range = [Country]

    class hosted(ObjectProperty):
        domain = [Country]
        range = [Conference]

    class heldIn(ObjectProperty, FunctionalProperty):
        domain = [Conference]
        range = [City]

    class travelledBy(ObjectProperty, FunctionalProperty):
        domain = [Delegation]
        range = [Train]

    class travelledTo(ObjectProperty):
        domain = [Delegation]
        range = [Conference]

    class demonstratesCommitmentTo(ObjectProperty, FunctionalProperty):
        domain = [Train]
        range = [Thing]

    class coalImportRankInEurope(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]

    class coalProductionRankInEU(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]

    class globalCoalProductionShare(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [float]

    ClimateChange.is_a.append(hasImpact.some(ClimateImpact))
    Conference.is_a.append(heldIn.some(City))
    Delegation.is_a.append(travelledBy.some(Train))
    EnergyTransition.is_a.append(isPoliticalIssueIn.some(Politics))

    germany = Country("GermanyCountry")
    germany.label = "Germany"

    europe = Continent("EuropeContinent")
    europe.label = "Europe"

    european_union = Organization("EuropeanUnionOrganization")
    european_union.label = "European Union"

    poland = Country("PolandCountry")
    poland.label = "Poland"

    angela_merkel = Person("AngelaMerkelPerson")
    angela_merkel.label = "Angela Merkel"

    cdu = PoliticalParty("CDUPoliticalParty")
    cdu.label = "CDU"

    german_politics = Politics("GermanPolitics")
    german_politics.label = "German politics"

    coalition_talks = PoliticalProcess("CoalitionTalksProcess")
    coalition_talks.label = "coalition talks"

    cop23 = Conference("Cop23Meeting")
    cop23.label = "COP23 meeting"

    bonn = City("BonnCity")
    bonn.label = "Bonn"

    german_delegation = Delegation("GermanDelegation")
    german_delegation.label = "German delegation"

    carbon_neutral_train = Train("CarbonNeutralTrain")
    carbon_neutral_train.label = "carbon-neutral train"

    climate_change = ClimateChange("ClimateChangeConcept")
    climate_change.label = "climate change"

    anthropogenic_climate_change = AnthropogenicClimateChange("AnthropogenicClimateChangeConcept")
    anthropogenic_climate_change.label = "anthropogenic climate change"

    agriculture = Agriculture("AgricultureConcept")
    agriculture.label = "agriculture"

    heatwaves = Heatwave("HeatwavesConcept")
    heatwaves.label = "heatwaves"

    coldwaves = Coldwave("ColdwavesConcept")
    coldwaves.label = "coldwaves"

    flash_flooding = Flooding("FlashFloodingConcept")
    flash_flooding.label = "flash flooding"

    coastal_flooding = Flooding("CoastalFloodingConcept")
    coastal_flooding.label = "coastal flooding"

    reduced_water_availability = WaterAvailabilityIssue("ReducedWaterAvailabilityConcept")
    reduced_water_availability.label = "reduced water availability"

    energy_sector = EnergySector("EnergySectorConcept")
    energy_sector.label = "energy sector"

    mitigation_strategies = MitigationStrategy("MitigationStrategiesConcept")
    mitigation_strategies.label = "mitigation strategies"

    energiewende = EnergyTransition("EnergiewendeConcept")
    energiewende.label = ["Germany 's energiewende", "energiewende", "energy transition"]

    renewable_energy = RenewableEnergy("RenewableEnergyConcept")
    renewable_energy.label = "renewable energy"

    coal = Coal("CoalConcept")
    coal.label = "coal"

    coal_production = CoalProduction("CoalProductionConcept")
    coal_production.label = "coal production"

    coal_usage = CoalUsage("CoalUsageConcept")
    coal_usage.label = "coal usage"

    carbon_neutrality = CarbonNeutrality("CarbonNeutralityConcept")
    carbon_neutrality.label = "carbon neutrality"

    climate_change.affects = [germany]
    climate_change.hasImpact = [agriculture, heatwaves, coldwaves, flash_flooding, coastal_flooding, reduced_water_availability]
    climate_change.sparksChangeIn = [energy_sector, mitigation_strategies]

    anthropogenic_climate_change.affects = [germany]
    anthropogenic_climate_change.hasImpact = [agriculture, heatwaves, coldwaves, flash_flooding, coastal_flooding, reduced_water_availability]

    germany.investsIn = [renewable_energy]
    germany.strugglesToReduce = [coal_production, coal_usage]
    germany.importsCommodity = [coal]
    germany.producesCommodity = [coal]
    germany.ranksBehindInProductionOf = [poland]
    germany.hosted = [cop23]
    germany.coalImportRankInEurope = 1
    germany.coalProductionRankInEU = 2
    germany.globalCoalProductionShare = 0.01

    european_union.label = "European Union"
    cop23.heldIn = bonn
    german_delegation.travelledBy = carbon_neutral_train
    german_delegation.travelledTo = [cop23]
    carbon_neutral_train.demonstratesCommitmentTo = carbon_neutrality

    energiewende.isPoliticalIssueIn = [german_politics]
    energiewende.makesDifficultFor = [coalition_talks]
    cdu.affiliatedWith = [angela_merkel]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
