"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

Here are the competency questions derived from the document:

1. What are the impacts of anthropogenic climate change on Germany?
2. What long-term effects does climate change have on agriculture in Germany?
3. What types of extreme weather events are intensified by climate change in Germany?
4. What flooding risks are associated with climate change in Germany?
5. How does climate change affect water availability in Germany?
6. What changes has climate change debate sparked in Germany's energy sector?
7. What is Germany's "Energiewende" and why is it politically significant?
8. How has the Energiewende affected coalition talks in German politics?
9. Which political party has been associated with the Energiewende debate?
10. What challenges has Germany faced in reducing coal production despite investments in renewable energy?
11. What is Germany's rank as a coal importer in Europe?
12. What is Germany's rank as a coal producer within the European Union?
13. Which country produces more coal than Germany within the European Union?
14. What percentage of global coal production does Germany account for?
15. What climate-related international event did Germany host in Bonn?
16. How did the German delegation demonstrate commitment to carbon neutrality at COP23?
17. What mitigation strategies has Germany adopted in response to climate change?
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
    Process, Event, Accomplishment,
    PhysicalObject, Society, AgentiveSocialObject,
    NonAgentiveSocialObject, SocialAgent, AmountOfMatter,
)


with core:
    # ── Entity Classes ──────────────────────────────────────────────────────

    # Nation-states, political bodies, delegations
    class NationState(Society): pass
    class PoliticalUnion(Society): pass
    class Delegation(Society): pass

    # Climate-related processes
    class ClimateChange(Process): pass

    # Extreme weather events
    class ExtremeWeatherEvent(Event): pass
    class Heatwave(ExtremeWeatherEvent): pass
    class Coldwave(ExtremeWeatherEvent): pass

    # Flooding events
    class FloodingEvent(Event): pass
    class FlashFlooding(FloodingEvent): pass
    class CoastalFlooding(FloodingEvent): pass

    # Social objects: sectors, policies, strategies, parties, conferences
    class EconomicSector(NonAgentiveSocialObject): pass
    class RenewableEnergySector(EconomicSector): pass
    class EnergyPolicy(NonAgentiveSocialObject): pass
    class MitigationStrategy(NonAgentiveSocialObject): pass
    class PoliticalParty(AgentiveSocialObject): pass
    class CoalitionTalk(Accomplishment): pass
    class InternationalConference(Accomplishment): pass

    # People
    class Politician(SocialAgent): pass

    # Physical places
    class City(PhysicalObject): pass

    # Natural resources (AmountOfMatter — no unity criterion)
    class NaturalResource(AmountOfMatter): pass
    class Coal(NaturalResource): pass
    class WaterResource(NaturalResource): pass

    # ── Object Properties ───────────────────────────────────────────────────

    class hasImpactOn(ObjectProperty):
        domain = [ClimateChange]
        range  = [NationState, EconomicSector]

    class intensifies(ObjectProperty):
        domain = [ClimateChange]
        range  = [ExtremeWeatherEvent]

    class causesFlooding(ObjectProperty):
        domain = [ClimateChange]
        range  = [FloodingEvent]

    class reducesAvailabilityOf(ObjectProperty):
        domain = [ClimateChange]
        range  = [NaturalResource]

    class sparksChangeIn(ObjectProperty):
        domain = [ClimateChange]
        range  = [EconomicSector]

    class isPoliticalIssueIn(ObjectProperty):
        domain = [EnergyPolicy]
        range  = [NationState]

    class complicates(ObjectProperty):
        domain = [EnergyPolicy]
        range  = [CoalitionTalk]

    class associatedWithParty(ObjectProperty):
        domain = [EnergyPolicy]
        range  = [PoliticalParty]

    class leaderOf(ObjectProperty):
        domain = [Politician]
        range  = [PoliticalParty]

    class producesResource(ObjectProperty):
        domain = [NationState]
        range  = [NaturalResource]

    class importsResource(ObjectProperty):
        domain = [NationState]
        range  = [NaturalResource]

    class hasInvestmentIn(ObjectProperty):
        domain = [NationState]
        range  = [EconomicSector]

    class hosts(ObjectProperty):
        domain = [NationState]
        range  = [InternationalConference]

    class hostedIn(ObjectProperty):
        domain = [InternationalConference]
        range  = [City]

    class representsNation(ObjectProperty):
        domain = [Delegation]
        range  = [NationState]

    class participatesIn(ObjectProperty):
        domain = [Delegation]
        range  = [InternationalConference]

    class demonstratesCommitmentTo(ObjectProperty):
        domain = [Delegation]
        range  = [MitigationStrategy]

    # ── Data Properties ─────────────────────────────────────────────────────

    class coalImporterRankInEurope(DataProperty, FunctionalProperty):
        domain = [NationState]
        range  = [int]

    class coalProducerRankInEU(DataProperty, FunctionalProperty):
        domain = [NationState]
        range  = [int]

    class coalShareOfGlobalTotal(DataProperty, FunctionalProperty):
        domain = [NationState]
        range  = [float]

    # ── Named Individuals ───────────────────────────────────────────────────

    germany = NationState("Germany")
    germany.label = "Germany"

    poland = NationState("Poland")
    poland.label = "Poland"

    europeanUnion = PoliticalUnion("EuropeanUnion")
    europeanUnion.label = "European Union"

    angelaMerkel = Politician("AngelaMerkel")
    angelaMerkel.label = "Angela Merkel"

    cdu = PoliticalParty("CDU")
    cdu.label = "CDU"

    energiewende = EnergyPolicy("Energiewende")
    energiewende.label = "Energiewende"

    cop23 = InternationalConference("COP23")
    cop23.label = "COP23"

    bonn = City("Bonn")
    bonn.label = "Bonn"

    germanDelegation = Delegation("GermanDelegation")
    germanDelegation.label = "German delegation"

    germanCoalitionTalks = CoalitionTalk("GermanCoalitionTalks")
    germanCoalitionTalks.label = "coalition talks"

    agricultureSector = EconomicSector("AgricultureSector")
    agricultureSector.label = "agriculture"

    energySectorInst = EconomicSector("EnergySectorInst")
    energySectorInst.label = "energy sector"

    renewableEnergySectorInst = RenewableEnergySector("RenewableEnergySectorInst")
    renewableEnergySectorInst.label = "renewable energy"

    heatwaveInst = Heatwave("HeatwaveInst")
    heatwaveInst.label = "heatwave"

    coldwaveInst = Coldwave("ColdwaveInst")
    coldwaveInst.label = "coldwave"

    flashFloodingInst = FlashFlooding("FlashFloodingInst")
    flashFloodingInst.label = "flash flooding"

    coastalFloodingInst = CoastalFlooding("CoastalFloodingInst")
    coastalFloodingInst.label = "coastal flooding"

    waterResourceInst = WaterResource("WaterResourceInst")
    waterResourceInst.label = "water availability"

    coalResource = Coal("CoalResource")
    coalResource.label = "coal"

    carbonNeutrality = MitigationStrategy("CarbonNeutrality")
    carbonNeutrality.label = "carbon neutrality"

    climateChangeInGermany = ClimateChange("ClimateChangeInGermany")
    climateChangeInGermany.label = "climate change in Germany"

    # ── Property Assertions ─────────────────────────────────────────────────

    # Climate change impacts on Germany and its sectors
    climateChangeInGermany.hasImpactOn.append(germany)
    climateChangeInGermany.hasImpactOn.append(agricultureSector)
    climateChangeInGermany.hasImpactOn.append(energySectorInst)

    # Extreme weather intensification
    climateChangeInGermany.intensifies.append(heatwaveInst)
    climateChangeInGermany.intensifies.append(coldwaveInst)

    # Flooding risks
    climateChangeInGermany.causesFlooding.append(flashFloodingInst)
    climateChangeInGermany.causesFlooding.append(coastalFloodingInst)

    # Reduced water availability
    climateChangeInGermany.reducesAvailabilityOf.append(waterResourceInst)

    # Debate sparks change in energy sector
    climateChangeInGermany.sparksChangeIn.append(energySectorInst)

    # Energiewende as political issue and its effects
    energiewende.isPoliticalIssueIn.append(germany)
    energiewende.complicates.append(germanCoalitionTalks)
    energiewende.associatedWithParty.append(cdu)

    # Angela Merkel leads CDU
    angelaMerkel.leaderOf.append(cdu)

    # Germany coal and investment facts
    germany.producesResource.append(coalResource)
    germany.importsResource.append(coalResource)
    germany.hasInvestmentIn.append(renewableEnergySectorInst)
    germany.coalImporterRankInEurope = 1
    germany.coalProducerRankInEU = 2
    germany.coalShareOfGlobalTotal = 0.01

    # Poland is 1st coal producer in the EU
    poland.producesResource.append(coalResource)
    poland.coalProducerRankInEU = 1

    # COP23 hosted by Germany in Bonn
    germany.hosts.append(cop23)
    cop23.hostedIn.append(bonn)

    # German delegation at COP23 demonstrates carbon-neutrality commitment
    germanDelegation.representsNation.append(germany)
    germanDelegation.participatesIn.append(cop23)
    germanDelegation.demonstratesCommitmentTo.append(carbonNeutrality)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
