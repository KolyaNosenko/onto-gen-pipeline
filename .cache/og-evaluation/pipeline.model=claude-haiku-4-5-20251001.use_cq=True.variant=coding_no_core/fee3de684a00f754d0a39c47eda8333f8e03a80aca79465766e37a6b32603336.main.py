"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the main impacts of climate change on Germany?
2. How does climate change affect agriculture in Germany?
3. What changes in extreme weather events (heatwaves, coldwaves, flooding) are occurring in Germany due to climate change?
4. What is Germany's energy transition (Energiewende) and what are its goals?
5. What challenges has Germany faced in reducing coal production and usage?
6. How much coal does Germany currently produce compared to other European Union countries?
7. What is Germany's global share of coal production?
8. What mitigation strategies has Germany implemented to address climate change?
9. How have climate change debates influenced German politics and coalition negotiations?
10. What renewable energy investments has Germany made as part of its energy transition?
11. Where did Germany host COP23 and how did it demonstrate commitment to carbon neutrality?
12. What is the relationship between Germany's energy sector changes and climate change response?
13. What long-term environmental challenges is Germany facing due to climate change?
14. What is Germany's status as a coal importer in Europe?
15. How has Germany's political landscape been affected by climate change policies?
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
    # Domain entity classes
    class Country(Thing): pass
    class Person(Thing): pass
    class PoliticalParty(Thing): pass
    
    # Climate and environmental impacts
    class ClimateChange(Thing): pass
    class ClimateImpact(Thing): pass
    class AgriculturalImpact(ClimateImpact): pass
    class WeatherImpact(ClimateImpact): pass
    class HeatWaveImpact(WeatherImpact): pass
    class ColdWaveImpact(WeatherImpact): pass
    class FloodingImpact(WeatherImpact): pass
    class FlashFloodingImpact(FloodingImpact): pass
    class CoastalFloodingImpact(FloodingImpact): pass
    class WaterAvailabilityImpact(ClimateImpact): pass
    
    # Energy and policy
    class EnergyTransition(Thing): pass
    class RenewableEnergyInvestment(Thing): pass
    class CoalImport(Thing): pass
    
    # Conferences and locations
    class Conference(Thing): pass
    class Location(Thing): pass
    
    # Delegations and transport
    class Delegation(Thing): pass
    class Transport(Thing): pass
    class CarbonNeutralTransport(Transport): pass
    
    # Commitment/initiative
    class CommitmentToCarbonNeutrality(Thing): pass
    
    # Object properties
    class affects(ObjectProperty):
        domain = [ClimateChange]
        range = [Country]
    
    class causes(ObjectProperty):
        domain = [ClimateChange]
        range = [ClimateImpact]
    
    class sparksEnergyTransition(ObjectProperty):
        domain = [ClimateChange]
        range = [EnergyTransition]
    
    class isPoliticalIssueFor(ObjectProperty):
        domain = [EnergyTransition]
        range = [Country]
    
    class makesCoalitionTalksDifficult(ObjectProperty):
        domain = [EnergyTransition]
        range = [PoliticalParty]
    
    class hasLeader(ObjectProperty):
        domain = [PoliticalParty]
        range = [Person]
    
    class investedIn(ObjectProperty):
        domain = [Country]
        range = [RenewableEnergyInvestment]
    
    class importsCoal(ObjectProperty):
        domain = [Country]
        range = [CoalImport]
    
    class hosted(ObjectProperty):
        domain = [Country]
        range = [Conference]
    
    class locatedIn(ObjectProperty):
        domain = [Conference]
        range = [Location]
    
    class involves(ObjectProperty):
        domain = [Conference]
        range = [Delegation]
    
    class traveledUsing(ObjectProperty):
        domain = [Delegation]
        range = [Transport]
    
    class demonstrates(ObjectProperty):
        domain = [Delegation]
        range = [CommitmentToCarbonNeutrality]
    
    # Data properties
    class coalProductionRankInEU(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]
    
    class coalProductionGlobalPercentage(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [float]
    
    # Instances for named entities
    
    # Countries
    germany = Country("Germany")
    germany.label = "Germany"
    
    poland = Country("Poland")
    poland.label = "Poland"
    
    # People
    angelaMerkel = Person("AngelaMerkel")
    angelaMerkel.label = "Angela Merkel"
    
    # Political parties
    cdu = PoliticalParty("CDU")
    cdu.label = "CDU"
    cdu.hasLeader = [angelaMerkel]
    
    # Climate change phenomenon
    climateChange = ClimateChange("ClimateChange_instance")
    climateChange.label = "climate change"
    
    # Climate impacts
    agriculturalImpact = AgriculturalImpact("AgriculturalImpact_instance")
    heatWaveImpact = HeatWaveImpact("HeatWaveImpact_instance")
    coldWaveImpact = ColdWaveImpact("ColdWaveImpact_instance")
    flashFloodingImpact = FlashFloodingImpact("FlashFloodingImpact_instance")
    coastalFloodingImpact = CoastalFloodingImpact("CoastalFloodingImpact_instance")
    waterAvailabilityImpact = WaterAvailabilityImpact("WaterAvailabilityImpact_instance")
    
    # Relate climate change to impacts and country
    climateChange.affects = [germany]
    climateChange.causes = [agriculturalImpact, heatWaveImpact, coldWaveImpact, 
                            flashFloodingImpact, coastalFloodingImpact, waterAvailabilityImpact]
    
    # Energy transition
    energiewende = EnergyTransition("Energiewende")
    energiewende.label = "energiewende"
    energiewende.isPoliticalIssueFor = [germany]
    energiewende.makesCoalitionTalksDifficult = [cdu]
    
    # Climate change sparks energy transition
    climateChange.sparksEnergyTransition = [energiewende]
    
    # Renewable energy investment
    renewableInvestment = RenewableEnergyInvestment("RenewableEnergyInvestment_instance")
    germany.investedIn = [renewableInvestment]
    
    # Coal import
    coalImport = CoalImport("CoalImport_instance")
    germany.importsCoal = [coalImport]
    
    # Coal production data
    germany.coalProductionRankInEU = 2
    germany.coalProductionGlobalPercentage = 1.0
    
    # Conference
    cop23 = Conference("COP23")
    cop23.label = "COP23"
    
    # Location
    bonn = Location("Bonn")
    bonn.label = "Bonn"
    
    # Relate conference to location
    cop23.locatedIn = [bonn]
    
    # Germany hosted COP23
    germany.hosted = [cop23]
    
    # Delegation
    germanDelegation = Delegation("GermanDelegation")
    germanDelegation.label = "German delegation"
    
    # Relate conference to delegation
    cop23.involves = [germanDelegation]
    
    # Carbon-neutral train
    carbonNeutralTrain = CarbonNeutralTransport("CarbonNeutralTrain")
    carbonNeutralTrain.label = "carbon-neutral train"
    
    # Delegation traveled using carbon-neutral train
    germanDelegation.traveledUsing = [carbonNeutralTrain]
    
    # Commitment to carbon neutrality
    commitment = CommitmentToCarbonNeutrality("CommitmentToCarbonNeutrality_instance")
    commitment.label = "commitment to carbon neutrality"
    
    # Delegation demonstrates commitment
    germanDelegation.demonstrates = [commitment]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
