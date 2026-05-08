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
7. What long-term challenges related to climate change are identified for Germany?
8. How have debates about addressing climate change challenges influenced the energy sector in Germany?
9. How have climate change debates affected mitigation strategies in Germany?
10. What is the Energiewende in the context of Germany?
11. Why has the Energiewende been a significant political issue in German politics?
12. How has the Energiewende affected coalition talks involving Angela Merkel’s CDU?
13. What investments has Germany made in renewable energy?
14. Has Germany succeeded in reducing coal production despite investments in renewable energy?
15. Has Germany succeeded in reducing coal usage despite investments in renewable energy?
16. What is Germany’s status as a coal importer in Europe?
17. How does Germany rank in coal production within the European Union?
18. Which country produces more coal than Germany in the European Union?
19. What proportion of global coal production is produced by Germany?
20. Which COP meeting did Germany host in Bonn?
21. Where was COP23 hosted?
22. How did the German delegation travel to the COP23 meeting?
23. Why did the German delegation travel to COP23 in a carbon-neutral train?
24. What actions has Germany taken to demonstrate commitment to carbon neutrality?
25. What is the relationship between climate change impacts and political responses in Germany?
26. What is the relationship between renewable energy investment and continued coal usage in Germany?
27. What sectors in Germany have changed in response to climate change debates?
28. Which climate-related extreme events mentioned in the document affect Germany?
29. What evidence is given of Germany’s commitment to climate mitigation?
30. What tensions exist between Germany’s climate goals and its coal dependency?
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
    class GeographicEntity(Thing):
        pass

    class Region(GeographicEntity):
        pass

    class Continent(Region):
        pass

    class PoliticalUnion(Region):
        pass

    class Country(GeographicEntity):
        pass

    class City(GeographicEntity):
        pass

    class ClimatePhenomenon(Thing):
        pass

    class ClimateChange(ClimatePhenomenon):
        pass

    class AnthropogenicClimateChange(ClimateChange):
        pass

    class NationalClimateChange(ClimateChange):
        pass

    class LongTermChallenge(Thing):
        pass

    class ClimateImpact(LongTermChallenge):
        pass

    class AgriculturalImpact(ClimateImpact):
        pass

    class ExtremeWeatherImpact(ClimateImpact):
        pass

    class HeatwaveImpact(ExtremeWeatherImpact):
        pass

    class ColdwaveImpact(ExtremeWeatherImpact):
        pass

    class Flooding(ExtremeWeatherImpact):
        pass

    class FlashFlooding(Flooding):
        pass

    class CoastalFlooding(Flooding):
        pass

    class WaterAvailabilityImpact(ClimateImpact):
        pass

    class Sector(Thing):
        pass

    class AgricultureSector(Sector):
        pass

    class EnergySector(Sector):
        pass

    class PoliticalContext(Thing):
        pass

    class Politics(PoliticalContext):
        pass

    class PoliticalIssue(PoliticalContext):
        pass

    class PoliticalProcess(PoliticalContext):
        pass

    class CoalitionTalk(PoliticalProcess):
        pass

    class Debate(PoliticalProcess):
        pass

    class Politician(PoliticalContext):
        pass

    class PoliticalParty(PoliticalContext):
        pass

    class Strategy(Thing):
        pass

    class MitigationStrategy(Strategy):
        pass

    class EnergyTransition(PoliticalIssue):
        pass

    class EnergyResource(Thing):
        pass

    class RenewableEnergy(EnergyResource):
        pass

    class Coal(EnergyResource):
        pass

    class ProductionActivity(Thing):
        pass

    class CoalProduction(ProductionActivity):
        pass

    class UsageActivity(Thing):
        pass

    class CoalUsage(UsageActivity):
        pass

    class ConferenceMeeting(Thing):
        pass

    class Delegation(Thing):
        pass

    class Vehicle(Thing):
        pass

    class Train(Vehicle):
        pass

    class Goal(Thing):
        pass

    class CarbonNeutralityGoal(Goal):
        pass

    class affectsCountry(ObjectProperty, FunctionalProperty):
        domain = [ClimateChange, ClimateImpact]
        range = [Country]

    class causedBy(ObjectProperty, FunctionalProperty):
        domain = [ClimateChange]
        range = [ClimateChange]

    class hasImpact(ObjectProperty):
        domain = [ClimateChange]
        range = [ClimateImpact]

    class affectsSector(ObjectProperty):
        domain = [ClimateImpact, Debate]
        range = [Sector]

    class addressesChallenge(ObjectProperty):
        domain = [Debate]
        range = [LongTermChallenge]

    class sparkedChangeIn(ObjectProperty):
        domain = [Debate]
        range = [Thing]

    class isPoliticalIssueIn(ObjectProperty, FunctionalProperty):
        domain = [EnergyTransition]
        range = [Politics]

    class madeDifficult(ObjectProperty, FunctionalProperty):
        domain = [EnergyTransition]
        range = [CoalitionTalk]

    class difficultFor(ObjectProperty, FunctionalProperty):
        domain = [CoalitionTalk]
        range = [PoliticalParty]

    class associatedWithPolitician(ObjectProperty, FunctionalProperty):
        domain = [PoliticalParty]
        range = [Politician]

    class investedIn(ObjectProperty):
        domain = [Country]
        range = [EnergyResource]

    class struggledToReduceProduction(ObjectProperty, FunctionalProperty):
        domain = [Country]
        range = [CoalProduction]

    class struggledToReduceUsage(ObjectProperty, FunctionalProperty):
        domain = [Country]
        range = [CoalUsage]

    class importsResource(ObjectProperty):
        domain = [Country]
        range = [EnergyResource]

    class producesResource(ObjectProperty):
        domain = [Country]
        range = [EnergyResource]

    class involvesResource(ObjectProperty, FunctionalProperty):
        domain = [ProductionActivity, UsageActivity]
        range = [EnergyResource]

    class memberOfUnion(ObjectProperty, FunctionalProperty):
        domain = [Country]
        range = [PoliticalUnion]

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [GeographicEntity, PoliticalUnion]
        range = [GeographicEntity]

    class hosted(ObjectProperty):
        domain = [Country]
        range = [ConferenceMeeting]

    class hostedIn(ObjectProperty, FunctionalProperty):
        domain = [ConferenceMeeting]
        range = [City]

    class traveledTo(ObjectProperty, FunctionalProperty):
        domain = [Delegation]
        range = [ConferenceMeeting]

    class traveledBy(ObjectProperty, FunctionalProperty):
        domain = [Delegation]
        range = [Vehicle]

    class demonstratedCommitmentTo(ObjectProperty):
        domain = [Delegation, Country]
        range = [Goal]

    class producesMoreCoalThan(ObjectProperty):
        domain = [Country]
        range = [Country]

    class coalImporterStatusInEurope(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [str]

    class coalProductionRankInEuropeanUnion(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [int]

    class shareOfGlobalCoalProductionPercent(DataProperty, FunctionalProperty):
        domain = [Country]
        range = [float]

    NationalClimateChange.is_a.append(affectsCountry.some(Country))
    NationalClimateChange.is_a.append(hasImpact.some(ClimateImpact))
    ClimateImpact.is_a.append(affectsCountry.some(Country))
    AgriculturalImpact.is_a.append(affectsSector.some(AgricultureSector))
    Debate.is_a.append(addressesChallenge.some(LongTermChallenge))
    EnergyTransition.is_a.append(isPoliticalIssueIn.some(Politics))
    CoalProduction.is_a.append(involvesResource.some(Coal))
    CoalUsage.is_a.append(involvesResource.some(Coal))
    ConferenceMeeting.is_a.append(hostedIn.some(City))
    Delegation.is_a.append(traveledBy.some(Vehicle))

    Europe = Continent("Europe")
    Europe.label = "Europe"

    EuropeanUnion = PoliticalUnion("EuropeanUnion")
    EuropeanUnion.label = "European Union"
    EuropeanUnion.locatedIn = [Europe]

    Germany = Country("Germany")
    Germany.label = "Germany"
    Germany.locatedIn = [Europe]
    Germany.memberOfUnion = EuropeanUnion
    Germany.coalImporterStatusInEurope = "largest importer"
    Germany.coalProductionRankInEuropeanUnion = 2
    Germany.shareOfGlobalCoalProductionPercent = 1.0

    Poland = Country("Poland")
    Poland.label = "Poland"
    Poland.locatedIn = [Europe]
    Poland.memberOfUnion = EuropeanUnion
    Poland.producesMoreCoalThan = [Germany]

    Bonn = City("Bonn")
    Bonn.label = "Bonn"
    Bonn.locatedIn = [Germany]

    AngelaMerkel = Politician("AngelaMerkel")
    AngelaMerkel.label = "Angela Merkel"

    CDU = PoliticalParty("CDU")
    CDU.label = "CDU"
    CDU.associatedWithPolitician = AngelaMerkel

    GermanPolitics = Politics("GermanPolitics")
    GermanPolitics.label = "German politics"

    AgricultureInGermany = AgricultureSector("AgricultureInGermany")
    AgricultureInGermany.label = "agriculture"

    EnergySectorInGermany = EnergySector("EnergySectorInGermany")
    EnergySectorInGermany.label = "the energy sector"

    MitigationStrategiesInGermany = MitigationStrategy("MitigationStrategiesInGermany")
    MitigationStrategiesInGermany.label = "mitigation strategies"

    RenewableEnergyResource = RenewableEnergy("RenewableEnergyResource")
    RenewableEnergyResource.label = "renewable energy"

    CoalResource = Coal("CoalResource")
    CoalResource.label = "coal"

    CarbonNeutrality = CarbonNeutralityGoal("CarbonNeutrality")
    CarbonNeutrality.label = "carbon neutrality"

    CoalitionTalks = CoalitionTalk("CoalitionTalks")
    CoalitionTalks.label = "coalition talks"
    CoalitionTalks.difficultFor = CDU

    Energiewende = EnergyTransition("Energiewende")
    Energiewende.label = "energiewende"
    Energiewende.isPoliticalIssueIn = GermanPolitics
    Energiewende.madeDifficult = CoalitionTalks

    GermanyClimateChange = NationalClimateChange("GermanyClimateChange")
    GermanyClimateChange.label = "Climate change in Germany"
    GermanyClimateChange.affectsCountry = Germany

    AnthropogenicClimateChangeProcess = AnthropogenicClimateChange("AnthropogenicClimateChangeProcess")
    AnthropogenicClimateChangeProcess.label = "anthropogenic climate change"

    GermanyClimateChange.causedBy = AnthropogenicClimateChangeProcess

    ImpactOnAgriculture = AgriculturalImpact("ImpactOnAgriculture")
    ImpactOnAgriculture.label = "long-term impacts on agriculture"
    ImpactOnAgriculture.affectsCountry = Germany
    ImpactOnAgriculture.affectsSector = [AgricultureInGermany]

    MoreIntenseHeatwaves = HeatwaveImpact("MoreIntenseHeatwaves")
    MoreIntenseHeatwaves.label = "more intense heatwaves"
    MoreIntenseHeatwaves.affectsCountry = Germany

    MoreIntenseColdwaves = ColdwaveImpact("MoreIntenseColdwaves")
    MoreIntenseColdwaves.label = "more intense coldwaves"
    MoreIntenseColdwaves.affectsCountry = Germany

    FlashFloodingInGermany = FlashFlooding("FlashFloodingInGermany")
    FlashFloodingInGermany.label = "flash flooding"
    FlashFloodingInGermany.affectsCountry = Germany

    CoastalFloodingInGermany = CoastalFlooding("CoastalFloodingInGermany")
    CoastalFloodingInGermany.label = "coastal flooding"
    CoastalFloodingInGermany.affectsCountry = Germany

    ReducedWaterAvailability = WaterAvailabilityImpact("ReducedWaterAvailability")
    ReducedWaterAvailability.label = "reduced water availability"
    ReducedWaterAvailability.affectsCountry = Germany

    GermanyClimateChange.hasImpact = [
        ImpactOnAgriculture,
        MoreIntenseHeatwaves,
        MoreIntenseColdwaves,
        FlashFloodingInGermany,
        CoastalFloodingInGermany,
        ReducedWaterAvailability,
    ]

    ClimateChangeDebates = Debate("ClimateChangeDebates")
    ClimateChangeDebates.label = "Debates over how to address these long-term challenges"
    ClimateChangeDebates.addressesChallenge = [
        ImpactOnAgriculture,
        MoreIntenseHeatwaves,
        MoreIntenseColdwaves,
        FlashFloodingInGermany,
        CoastalFloodingInGermany,
        ReducedWaterAvailability,
    ]
    ClimateChangeDebates.sparkedChangeIn = [
        EnergySectorInGermany,
        MitigationStrategiesInGermany,
    ]
    ClimateChangeDebates.affectsSector = [EnergySectorInGermany]

    Germany.investedIn = [RenewableEnergyResource]
    Germany.importsResource = [CoalResource]
    Germany.producesResource = [CoalResource]
    Germany.demonstratedCommitmentTo = [CarbonNeutrality]

    GermanyCoalProduction = CoalProduction("GermanyCoalProduction")
    GermanyCoalProduction.label = "coal production"
    GermanyCoalProduction.involvesResource = CoalResource

    GermanyCoalUsage = CoalUsage("GermanyCoalUsage")
    GermanyCoalUsage.label = "coal usage"
    GermanyCoalUsage.involvesResource = CoalResource

    Germany.struggledToReduceProduction = GermanyCoalProduction
    Germany.struggledToReduceUsage = GermanyCoalUsage

    COP23Meeting = ConferenceMeeting("COP23Meeting")
    COP23Meeting.label = ["COP23 meeting", "COP23"]
    COP23Meeting.hostedIn = Bonn

    Germany.hosted = [COP23Meeting]

    GermanDelegation = Delegation("GermanDelegation")
    GermanDelegation.label = "the German delegation"
    GermanDelegation.traveledTo = COP23Meeting

    CarbonNeutralTrain = Train("CarbonNeutralTrain")
    CarbonNeutralTrain.label = "a carbon-neutral train"

    GermanDelegation.traveledBy = CarbonNeutralTrain
    GermanDelegation.demonstratedCommitmentTo = [CarbonNeutrality]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
