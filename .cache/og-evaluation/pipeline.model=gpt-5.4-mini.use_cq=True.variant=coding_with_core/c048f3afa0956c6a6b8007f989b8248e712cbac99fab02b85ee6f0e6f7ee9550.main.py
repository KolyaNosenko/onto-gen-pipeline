"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the long-term impacts of anthropogenic climate change on Germany?
2. How does climate change affect agriculture in Germany?
3. How does climate change influence the frequency or intensity of heatwaves in Germany?
4. How does climate change influence the frequency or intensity of coldwaves in Germany?
5. What types of flooding are linked to climate change impacts in Germany?
6. How does climate change affect water availability in Germany?
7. What debates have arisen in Germany about addressing long-term climate change challenges?
8. How have climate change challenges affected Germany’s energy sector?
9. What mitigation strategies has Germany adopted in response to climate change?
10. What is Germany’s Energiewende, and why is it politically significant?
11. How has the Energiewende affected coalition talks in German politics?
12. How much has Germany invested in renewable energy?
13. Has Germany reduced coal production and coal usage despite investments in renewable energy?
14. Is Germany the largest importer of coal in Europe?
15. How does Germany’s coal production compare with other European Union countries?
16. What share of global coal production or usage is associated with Germany?
17. Did Germany host COP23 in Bonn?
18. How did the German delegation travel to COP23?
19. What was the purpose of Germany’s use of a carbon-neutral train to COP23?
20. How does Germany demonstrate commitment to carbon neutrality in its climate actions?
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
    Abstract, AmountOfMatter, Event, NonAgentivePhysicalObject, Process,
    SocialAgent, SocialObject, Society, SpaceRegion, State,
)


with core:
    class Country(Society):
        pass

    class City(SpaceRegion):
        pass

    class Continent(SpaceRegion):
        pass

    class PoliticalUnion(Society):
        pass

    class PoliticalParty(Society):
        pass

    class Person(SocialAgent):
        pass

    class Delegation(SocialObject):
        pass

    class Meeting(Event):
        pass

    class Train(NonAgentivePhysicalObject):
        pass

    class ClimateChange(Process):
        pass

    class Challenge(Abstract):
        pass

    class ClimateImpact(Abstract):
        pass

    class PoliticalIssue(Abstract):
        pass

    class Sector(SocialObject):
        pass

    class Strategy(Abstract):
        pass

    class Debate(Event):
        pass

    class CoalitionTalk(Event):
        pass

    class EnergyResource(Abstract):
        pass

    class EconomicActivity(Process):
        pass

    class MatterSubstance(AmountOfMatter):
        pass

    class CarbonNeutralityState(State):
        pass

    class impactsOn(ObjectProperty):
        domain = [ClimateChange]
        range = [Abstract, SocialObject, Process]

    class addresses(ObjectProperty):
        domain = [Debate]
        range = [Challenge]

    class sparkedChangesIn(ObjectProperty):
        domain = [Debate]
        range = [Sector, Strategy]

    class madeDifficultFor(ObjectProperty):
        domain = [PoliticalIssue]
        range = [CoalitionTalk]

    class politicallySignificantIn(ObjectProperty):
        domain = [PoliticalIssue]
        range = [Country]

    class investsIn(ObjectProperty):
        domain = [Country]
        range = [EnergyResource]

    class struggledToReduce(ObjectProperty):
        domain = [Country]
        range = [EconomicActivity]

    class imports(ObjectProperty):
        domain = [Country]
        range = [MatterSubstance]

    class produces(ObjectProperty):
        domain = [Country]
        range = [MatterSubstance]

    class behindInCoalProductionInEU(ObjectProperty):
        domain = [Country]
        range = [Country]

    class hostedBy(ObjectProperty):
        domain = [Meeting]
        range = [Country]

    class heldIn(ObjectProperty):
        domain = [Meeting]
        range = [City]

    class traveledIn(ObjectProperty):
        domain = [Delegation]
        range = [Train]

    class traveledTo(ObjectProperty):
        domain = [Delegation]
        range = [Meeting]

    class delegationOf(ObjectProperty):
        domain = [Delegation]
        range = [Country]

    class demonstratesCommitmentTo(ObjectProperty):
        domain = [Delegation, Train, Country]
        range = [CarbonNeutralityState]

    class hasCoalProductionRankInEU(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]

    class hasGlobalCoalShare(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [float]

    class isLargestCoalImporterInEurope(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]

    class hasMadeMassiveInvestmentsInRenewableEnergy(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]

    class hasCoalProductionReductionDifficulty(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]

    class hasCoalUsageReductionDifficulty(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [bool]

    class isSignificantPoliticalIssueInGermanPolitics(DataProperty, FunctionalProperty):
        domain = [PoliticalIssue]
        range = [bool]

    Germany = Country("Germany")
    Germany.label = "Germany"

    Europe = Continent("Europe")
    Europe.label = "Europe"

    EuropeanUnion = PoliticalUnion("EuropeanUnion")
    EuropeanUnion.label = "European Union"

    Poland = Country("Poland")
    Poland.label = "Poland"

    AngelaMerkel = Person("AngelaMerkel")
    AngelaMerkel.label = "Angela Merkel"

    CDU = PoliticalParty("CDU")
    CDU.label = "CDU"

    Bonn = City("Bonn")
    Bonn.label = "Bonn"

    COP23 = Meeting("COP23")
    COP23.label = "COP23"

    GermanDelegation = Delegation("GermanDelegation")
    GermanDelegation.label = "German delegation"

    CarbonNeutralTrain = Train("CarbonNeutralTrain")
    CarbonNeutralTrain.label = "carbon-neutral train"

    AnthropogenicClimateChange = ClimateChange("AnthropogenicClimateChange")
    AnthropogenicClimateChange.label = "anthropogenic climate change"

    ClimateChangeDebates = Debate("ClimateChangeDebates")
    ClimateChangeDebates.label = "Debates over how to address these long-term challenges"

    LongTermChallenges = Challenge("LongTermChallenges")
    LongTermChallenges.label = "these long-term challenges"

    Agriculture = Sector("Agriculture")
    Agriculture.label = "agriculture"

    EnergySector = Sector("EnergySector")
    EnergySector.label = "energy sector"

    MitigationStrategies = Strategy("MitigationStrategies")
    MitigationStrategies.label = "mitigation strategies"

    Energiewende = PoliticalIssue("Energiewende")
    Energiewende.label = "energiewende"

    CoalitionTalks = CoalitionTalk("CoalitionTalks")
    CoalitionTalks.label = "coalition talks"

    RenewableEnergy = EnergyResource("RenewableEnergy")
    RenewableEnergy.label = "renewable energy"

    CoalProduction = EconomicActivity("CoalProduction")
    CoalProduction.label = "coal production"

    CoalUsage = EconomicActivity("CoalUsage")
    CoalUsage.label = "coal usage"

    Coal = MatterSubstance("Coal")
    Coal.label = "coal"

    CarbonNeutrality = CarbonNeutralityState("CarbonNeutrality")
    CarbonNeutrality.label = "carbon neutrality"

    Heatwaves = ClimateImpact("Heatwaves")
    Heatwaves.label = "more intense heatwaves"

    Coldwaves = ClimateImpact("Coldwaves")
    Coldwaves.label = "coldwaves"

    FlashFlooding = ClimateImpact("FlashFlooding")
    FlashFlooding.label = "flash flooding"

    CoastalFlooding = ClimateImpact("CoastalFlooding")
    CoastalFlooding.label = "coastal flooding"

    ReducedWaterAvailability = ClimateImpact("ReducedWaterAvailability")
    ReducedWaterAvailability.label = "reduced water availability"

    AnthropogenicClimateChange.impactsOn.extend(
        [
            Germany,
            Agriculture,
            Heatwaves,
            Coldwaves,
            FlashFlooding,
            CoastalFlooding,
            ReducedWaterAvailability,
        ]
    )
    ClimateChangeDebates.addresses.append(LongTermChallenges)
    ClimateChangeDebates.sparkedChangesIn.extend([EnergySector, MitigationStrategies])
    Energiewende.politicallySignificantIn.append(Germany)
    Energiewende.madeDifficultFor.append(CoalitionTalks)
    Energiewende.isSignificantPoliticalIssueInGermanPolitics = True

    Germany.investsIn.append(RenewableEnergy)
    Germany.struggledToReduce.extend([CoalProduction, CoalUsage])
    Germany.imports.append(Coal)
    Germany.produces.append(Coal)
    Germany.behindInCoalProductionInEU.append(Poland)
    Germany.hasCoalProductionRankInEU = 2
    Germany.hasGlobalCoalShare = 0.01
    Germany.isLargestCoalImporterInEurope = True
    Germany.hasMadeMassiveInvestmentsInRenewableEnergy = True
    Germany.hasCoalProductionReductionDifficulty = True
    Germany.hasCoalUsageReductionDifficulty = True

    COP23.hostedBy.append(Germany)
    COP23.heldIn.append(Bonn)

    GermanDelegation.traveledIn.append(CarbonNeutralTrain)
    GermanDelegation.traveledTo.append(COP23)
    GermanDelegation.delegationOf.append(Germany)
    GermanDelegation.demonstratesCommitmentTo.append(CarbonNeutrality)
    CarbonNeutralTrain.demonstratesCommitmentTo.append(CarbonNeutrality)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
