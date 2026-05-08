"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the impacts of anthropogenic climate change on Germany?
2. Which long-term impacts of climate change affect agriculture in Germany?
3. How does climate change influence the frequency or intensity of heatwaves in Germany?
4. How does climate change influence the frequency or intensity of coldwaves in Germany?
5. What types of flooding associated with climate change occur in Germany?
6. How does climate change affect water availability in Germany?
7. What long-term challenges related to climate change are discussed in Germany?
8. How have debates about addressing climate change affected the energy sector in Germany?
9. How have mitigation strategies in Germany changed in response to climate change?
10. What is the Energiewende in the context of Germany?
11. Why has the Energiewende been a significant political issue in German politics?
12. How has the Energiewende affected coalition talks involving Angela Merkel’s CDU?
13. What investments has Germany made in renewable energy?
14. Has Germany succeeded in reducing coal production and usage despite investments in renewable energy?
15. What is Germany’s role in coal imports within Europe?
16. How much coal does Germany produce relative to other European Union countries?
17. Which country produces more coal than Germany in the European Union?
18. What share of global coal production is attributed to Germany?
19. Which international climate meeting was hosted by Germany in Bonn?
20. How did the German delegation travel to COP23?
21. Why did the German delegation travel to COP23 in a carbon-neutral train?
22. What actions has Germany taken to demonstrate commitment to carbon neutrality?
23. What is the relationship between climate change impacts and political responses in Germany?
24. What is the relationship between climate change mitigation efforts and coal dependence in Germany?
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
    Accomplishment,
    AgentivePhysicalObject,
    AmountOfMatter,
    Event,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Perdurant,
    Process,
    Society,
    SpaceRegion,
    State,
)
from og_sandbox_with_core.core.properties import partOf


with core:
    class Person(AgentivePhysicalObject):
        pass


    class Politician(Person):
        pass


    class Country(Society):
        pass


    class SupranationalOrganization(Society):
        pass


    class PoliticalParty(Society):
        pass


    class Delegation(Society):
        pass


    class GeographicRegion(SpaceRegion):
        pass


    class City(GeographicRegion):
        pass


    class Sector(NonAgentiveSocialObject):
        pass


    class Strategy(NonAgentiveSocialObject):
        pass


    class Policy(NonAgentiveSocialObject):
        pass


    class PoliticalContext(NonAgentiveSocialObject):
        pass


    class ClimatePolicyGoal(NonAgentiveSocialObject):
        pass


    class EnergyResource(NonAgentiveSocialObject):
        pass


    class CoalMaterial(AmountOfMatter):
        pass


    class Vehicle(NonAgentivePhysicalObject):
        pass


    class Train(Vehicle):
        pass


    class ClimatePhenomenon(Process):
        pass


    class ClimateChange(ClimatePhenomenon):
        pass


    class AnthropogenicClimateChange(ClimateChange):
        pass


    class ClimateImpact(Perdurant):
        pass


    class LongTermClimateImpact(ClimateImpact):
        pass


    class AgriculturalClimateImpact(LongTermClimateImpact, State):
        pass


    class HeatwaveImpact(LongTermClimateImpact, Event):
        pass


    class ColdwaveImpact(LongTermClimateImpact, Event):
        pass


    class FloodingImpact(LongTermClimateImpact, Event):
        pass


    class FlashFloodingImpact(FloodingImpact):
        pass


    class CoastalFloodingImpact(FloodingImpact):
        pass


    class WaterAvailabilityReduction(LongTermClimateImpact, State):
        pass


    class ClimateChallenge(NonAgentiveSocialObject):
        pass


    class ClimateChangeDebate(Accomplishment):
        pass


    class PoliticalNegotiation(Accomplishment):
        pass


    class CoalitionTalks(PoliticalNegotiation):
        pass


    class Investment(Accomplishment):
        pass


    class RenewableEnergyInvestment(Investment):
        pass


    class CoalActivity(Process):
        pass


    class ClimateConference(Accomplishment):
        pass


    class EnergyTransition(Policy):
        pass


    class hasImpact(ObjectProperty):
        domain = [ClimateChange]
        range = [ClimateImpact]


    class resultsFrom(ObjectProperty):
        domain = [ClimateImpact]
        range = [ClimateChange]


    class affects(ObjectProperty):
        domain = [ClimateImpact]
        range = [Country, Sector]


    class addresses(ObjectProperty):
        domain = [ClimateChangeDebate]
        range = [ClimateChallenge]


    class sparksChangeIn(ObjectProperty):
        domain = [ClimateChangeDebate]
        range = [Sector, Strategy]


    class significantIn(ObjectProperty):
        domain = [EnergyTransition]
        range = [PoliticalContext]


    class affectsPoliticalProcess(ObjectProperty):
        domain = [EnergyTransition]
        range = [PoliticalNegotiation]


    class madeDifficultFor(ObjectProperty):
        domain = [EnergyTransition]
        range = [PoliticalParty]


    class involvesParty(ObjectProperty):
        domain = [PoliticalNegotiation]
        range = [PoliticalParty]


    class ledBy(ObjectProperty):
        domain = [PoliticalParty]
        range = [Person]


    class represents(ObjectProperty):
        domain = [Delegation]
        range = [Country]


    class madeInvestment(ObjectProperty):
        domain = [Country]
        range = [Investment]


    class investmentTarget(ObjectProperty):
        domain = [Investment]
        range = [EnergyResource]


    class struggledToReduce(ObjectProperty):
        domain = [Country]
        range = [CoalActivity]


    class isLargestImporterOf(ObjectProperty):
        domain = [Country]
        range = [CoalMaterial]


    class producesMoreCoalThan(ObjectProperty):
        domain = [Country]
        range = [Country]


    class hosted(ObjectProperty):
        domain = [Country]
        range = [ClimateConference]


    class takesPlaceIn(ObjectProperty):
        domain = [ClimateConference]
        range = [City]


    class traveledTo(ObjectProperty):
        domain = [Delegation]
        range = [ClimateConference]


    class traveledBy(ObjectProperty):
        domain = [Delegation]
        range = [Train]


    class demonstratedCommitmentTo(ObjectProperty):
        domain = [Delegation]
        range = [ClimatePolicyGoal]


    class hasInvestmentScale(DataProperty, FunctionalProperty):
        domain = [Investment]
        range = [str]


    class hasSucceededInReducingCoalProductionAndUsage(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]


    class coalProductionRankInEuropeanUnion(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]


    class globalCoalProductionSharePercent(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [float]


    LongTermClimateImpact.is_a.append(resultsFrom.some(AnthropogenicClimateChange))
    AgriculturalClimateImpact.is_a.append(affects.some(Sector))
    ClimateChangeDebate.is_a.append(addresses.some(ClimateChallenge))
    ClimateChangeDebate.is_a.append(sparksChangeIn.some(Sector))
    ClimateChangeDebate.is_a.append(sparksChangeIn.some(Strategy))
    RenewableEnergyInvestment.is_a.append(investmentTarget.some(EnergyResource))
    ClimateConference.is_a.append(takesPlaceIn.some(City))

    Germany = Country("Germany")
    Germany.label = "Germany"

    Europe = GeographicRegion("Europe")
    Europe.label = "Europe"

    EuropeanUnion = SupranationalOrganization("EuropeanUnion")
    EuropeanUnion.label = "European Union"

    Poland = Country("Poland")
    Poland.label = "Poland"

    Bonn = City("Bonn")
    Bonn.label = "Bonn"

    AngelaMerkel = Politician("AngelaMerkel")
    AngelaMerkel.label = "Angela Merkel"

    CDU = PoliticalParty("CDU")
    CDU.label = "CDU"

    GermanPolitics = PoliticalContext("GermanPolitics")
    GermanPolitics.label = "German politics"

    Agriculture = Sector("agriculture")
    Agriculture.label = "agriculture"

    EnergySector = Sector("EnergySector")
    EnergySector.label = "energy sector"

    MitigationStrategies = Strategy("MitigationStrategies")
    MitigationStrategies.label = "mitigation strategies"

    RenewableEnergy = EnergyResource("RenewableEnergy")
    RenewableEnergy.label = "renewable energy"

    Coal = CoalMaterial("coal")
    Coal.label = "coal"

    CarbonNeutrality = ClimatePolicyGoal("CarbonNeutrality")
    CarbonNeutrality.label = "carbon neutrality"

    AnthropogenicClimateChangeInstance = AnthropogenicClimateChange("AnthropogenicClimateChangeInstance")
    AnthropogenicClimateChangeInstance.label = "anthropogenic climate change"

    LongTermImpactOnAgriculture = AgriculturalClimateImpact("LongTermImpactOnAgriculture")
    LongTermImpactOnAgriculture.label = "long - term impacts on agriculture"

    MoreIntenseHeatwaves = HeatwaveImpact("MoreIntenseHeatwaves")
    MoreIntenseHeatwaves.label = "more intense heatwaves"

    MoreIntenseColdwaves = ColdwaveImpact("MoreIntenseColdwaves")
    MoreIntenseColdwaves.label = "more intense coldwaves"

    FlashFlooding = FlashFloodingImpact("FlashFlooding")
    FlashFlooding.label = ["flash flooding", "flash and coastal flooding"]

    CoastalFlooding = CoastalFloodingImpact("CoastalFlooding")
    CoastalFlooding.label = "coastal flooding"

    ReducedWaterAvailability = WaterAvailabilityReduction("ReducedWaterAvailability")
    ReducedWaterAvailability.label = "reduced water availability"

    LongTermChallenges = ClimateChallenge("LongTermChallenges")
    LongTermChallenges.label = "long - term challenges"

    DebatesOverAddressingLongTermChallenges = ClimateChangeDebate(
        "DebatesOverAddressingLongTermChallenges"
    )
    DebatesOverAddressingLongTermChallenges.label = (
        "Debates over how to address these long - term challenges"
    )

    Energiewende = EnergyTransition("energiewende")
    Energiewende.label = ["energiewende", "energy transition"]

    CoalitionTalksInstance = CoalitionTalks("CoalitionTalksInstance")
    CoalitionTalksInstance.label = "coalition talks"

    MassiveInvestmentsInRenewableEnergy = RenewableEnergyInvestment(
        "MassiveInvestmentsInRenewableEnergy"
    )
    MassiveInvestmentsInRenewableEnergy.label = "massive investments in renewable energy"

    CoalProductionAndUsage = CoalActivity("CoalProductionAndUsage")
    CoalProductionAndUsage.label = "coal production and usage"

    COP23 = ClimateConference("COP23")
    COP23.label = "COP23"

    GermanDelegation = Delegation("GermanDelegation")
    GermanDelegation.label = "German delegation"

    CarbonNeutralTrain = Train("CarbonNeutralTrain")
    CarbonNeutralTrain.label = "carbon - neutral train"

    Germany.partOf = [Europe, EuropeanUnion]
    Bonn.partOf = [Germany]
    CDU.ledBy = [AngelaMerkel]
    GermanDelegation.represents = [Germany]

    AnthropogenicClimateChangeInstance.hasImpact = [
        LongTermImpactOnAgriculture,
        MoreIntenseHeatwaves,
        MoreIntenseColdwaves,
        FlashFlooding,
        CoastalFlooding,
        ReducedWaterAvailability,
    ]

    LongTermImpactOnAgriculture.resultsFrom = [AnthropogenicClimateChangeInstance]
    LongTermImpactOnAgriculture.affects = [Germany, Agriculture]
    MoreIntenseHeatwaves.resultsFrom = [AnthropogenicClimateChangeInstance]
    MoreIntenseHeatwaves.affects = [Germany]
    MoreIntenseColdwaves.resultsFrom = [AnthropogenicClimateChangeInstance]
    MoreIntenseColdwaves.affects = [Germany]
    FlashFlooding.resultsFrom = [AnthropogenicClimateChangeInstance]
    FlashFlooding.affects = [Germany]
    CoastalFlooding.resultsFrom = [AnthropogenicClimateChangeInstance]
    CoastalFlooding.affects = [Germany]
    ReducedWaterAvailability.resultsFrom = [AnthropogenicClimateChangeInstance]
    ReducedWaterAvailability.affects = [Germany]

    DebatesOverAddressingLongTermChallenges.addresses = [LongTermChallenges]
    DebatesOverAddressingLongTermChallenges.sparksChangeIn = [
        EnergySector,
        MitigationStrategies,
    ]

    Energiewende.significantIn = [GermanPolitics]
    Energiewende.affectsPoliticalProcess = [CoalitionTalksInstance]
    Energiewende.madeDifficultFor = [CDU]
    CoalitionTalksInstance.involvesParty = [CDU]

    Germany.madeInvestment = [MassiveInvestmentsInRenewableEnergy]
    MassiveInvestmentsInRenewableEnergy.investmentTarget = [RenewableEnergy]
    MassiveInvestmentsInRenewableEnergy.hasInvestmentScale = "massive"

    Germany.struggledToReduce = [CoalProductionAndUsage]
    Germany.hasSucceededInReducingCoalProductionAndUsage = False
    Germany.isLargestImporterOf = [Coal]
    Germany.coalProductionRankInEuropeanUnion = 2
    Germany.globalCoalProductionSharePercent = 1.0
    Poland.producesMoreCoalThan = [Germany]

    Germany.hosted = [COP23]
    COP23.takesPlaceIn = [Bonn]
    GermanDelegation.traveledTo = [COP23]
    GermanDelegation.traveledBy = [CarbonNeutralTrain]
    GermanDelegation.demonstratedCommitmentTo = [CarbonNeutrality]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
