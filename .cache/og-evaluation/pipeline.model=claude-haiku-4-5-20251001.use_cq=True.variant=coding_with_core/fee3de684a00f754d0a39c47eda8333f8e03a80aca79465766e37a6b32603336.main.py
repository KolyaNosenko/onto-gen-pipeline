"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the main impacts of climate change on Germany?
2. How does climate change affect agriculture in Germany?
3. What types of extreme weather events is Germany experiencing due to climate change?
4. What is Germany's energiewende and what role does it play in addressing climate change?
5. What challenges has Germany faced in implementing its energy transition?
6. How much renewable energy has Germany invested in?
7. What is Germany's current coal production and consumption compared to other European countries?
8. Why has Germany's energy transition been a political issue in German politics?
9. How much coal does Germany produce relative to global coal production?
10. What mitigation strategies has Germany adopted to address climate change?
11. What role did Germany play in hosting COP23?
12. How did Germany demonstrate its commitment to carbon neutrality at COP23?
13. What are the long-term challenges Germany faces related to climate change?
14. How has the energy sector in Germany changed in response to climate change debates?
15. What is Germany's ranking in coal importation in Europe?
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
    Society, AgentivePhysicalObject, NonAgentiveSocialObject,
    Accomplishment, NonAgentivePhysicalObject,
    AmountOfMatter, PhysicalQuality, AbstractQuality, Endurant
)
from og_sandbox_with_core.core.properties import constantParticipantOf

with core:
    # Entity classes
    
    class Heatwave(Accomplishment):
        """An event involving abnormally high temperatures"""
        pass
    
    class Coldwave(Accomplishment):
        """An event involving abnormally low temperatures"""
        pass
    
    class Flooding(Accomplishment):
        """An event involving water flooding"""
        pass
    
    class FlashFlooding(Flooding):
        """Flooding that occurs suddenly"""
        pass
    
    class CoastalFlooding(Flooding):
        """Flooding that occurs on coasts"""
        pass
    
    class ClimateChange(Accomplishment):
        """The phenomenon of climate change with impacts"""
        pass
    
    class Energiewende(Accomplishment):
        """Germany's energy transition"""
        pass
    
    # ObjectProperties
    
    class causes(ObjectProperty):
        """Causation relation between events or processes"""
        domain = [Accomplishment]
        range = [Accomplishment]
    
    class affects(ObjectProperty):
        """Affectation relation between entities"""
        domain = [Accomplishment]
        range = [Accomplishment, Society, NonAgentiveSocialObject, PhysicalQuality]
    
    class reduces(ObjectProperty):
        """Reduction relation between entity and quality"""
        domain = [Accomplishment]
        range = [PhysicalQuality]
    
    class isLocatedAt(ObjectProperty):
        """Spatial location relation"""
        domain = [Accomplishment]
        range = [NonAgentiveSocialObject, Society]
    
    class hosts(ObjectProperty):
        """Hosting/organizing relation"""
        domain = [Society]
        range = [Accomplishment]
    
    class usesTransport(ObjectProperty):
        """Use of transport means"""
        domain = [Endurant]
        range = [NonAgentivePhysicalObject]
    
    class produces(ObjectProperty):
        """Production relation"""
        domain = [Society]
        range = [AmountOfMatter]
    
    class imports(ObjectProperty):
        """Importation relation"""
        domain = [Society]
        range = [AmountOfMatter]
    
    class invests(ObjectProperty):
        """Investment in resources or activities"""
        domain = [Society]
        range = [AmountOfMatter, Accomplishment]
    
    class demonstrates(ObjectProperty):
        """Demonstration of commitment or quality"""
        domain = [Endurant]
        range = [AbstractQuality]
    
    class producesMore(ObjectProperty):
        """Comparative production relation"""
        domain = [Society]
        range = [Society]
    
    # DataProperties
    
    class hasProductionRankInEU(DataProperty, FunctionalProperty):
        """Coal production ranking in EU"""
        domain = [Society]
        range = [int]
    
    class hasProductionPercentageOfGlobal(DataProperty, FunctionalProperty):
        """Production as percentage of global total"""
        domain = [Society]
        range = [float]
    
    class isLargestImporterInEurope(DataProperty, FunctionalProperty):
        """Boolean indicating largest importer status in Europe"""
        domain = [Society]
        range = [bool]
    
    # Named instances
    
    germany = Society("Germany")
    germany.label = "Germany"
    
    angela_merkel = AgentivePhysicalObject("AngelaMerkel")
    angela_merkel.label = "Angela Merkel"
    
    cdu = Society("CDU")
    cdu.label = "CDU"
    
    eu = Society("EuropeanUnion")
    eu.label = "European Union"
    
    poland = Society("Poland")
    poland.label = "Poland"
    
    bonn = NonAgentiveSocialObject("Bonn")
    bonn.label = "Bonn"
    
    german_delegation = Society("GermanDelegation")
    german_delegation.label = "German delegation"
    
    cop23 = Accomplishment("COP23")
    cop23.label = "COP23"
    
    coal = AmountOfMatter("Coal")
    coal.label = "coal"
    
    renewable_energy = AmountOfMatter("RenewableEnergy")
    renewable_energy.label = "renewable energy"
    
    carbon_neutral_train = NonAgentivePhysicalObject("CarbonNeutralTrain")
    carbon_neutral_train.label = "carbon-neutral train"
    
    climate_change = ClimateChange("ClimateChangeInGermany")
    climate_change.label = "climate change in Germany"
    
    water_availability = PhysicalQuality("WaterAvailability")
    water_availability.label = "water availability"
    
    heatwaves = Heatwave("HeatwaveEvent")
    heatwaves.label = "heatwaves"
    
    coldwaves = Coldwave("ColdwaveEvent")
    coldwaves.label = "coldwaves"
    
    flooding = Flooding("FloodingEvent")
    flooding.label = "flooding"
    
    agriculture = NonAgentiveSocialObject("Agriculture")
    agriculture.label = "agriculture in Germany"
    
    carbon_neutrality = AbstractQuality("CarbonNeutrality")
    carbon_neutrality.label = "carbon neutrality"
    
    energiewende = Energiewende("GermanyEnergiewende")
    energiewende.label = "Germany's energiewende"
    
    # Facts about climate change and its impacts
    
    climate_change.causes.append(heatwaves)
    climate_change.causes.append(coldwaves)
    climate_change.causes.append(flooding)
    climate_change.reduces.append(water_availability)
    climate_change.affects.append(agriculture)
    climate_change.affects.append(germany)
    
    # Facts about energiewende and politics
    
    energiewende.affects.append(cdu)
    
    # Facts about Germany's coal and energy production
    
    germany.produces.append(coal)
    germany.imports.append(coal)
    germany.invests.append(renewable_energy)
    poland.producesMore.append(germany)
    germany.hasProductionRankInEU = 2
    germany.hasProductionPercentageOfGlobal = 1.0
    germany.isLargestImporterInEurope = True
    
    # Facts about COP23
    
    cop23.isLocatedAt.append(bonn)
    germany.hosts.append(cop23)
    
    # Facts about German delegation at COP23
    
    german_delegation.constantParticipantOf.append(cop23)
    german_delegation.usesTransport.append(carbon_neutral_train)
    german_delegation.demonstrates.append(carbon_neutrality)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
