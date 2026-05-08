"""
=== TASK INPUT ===
Source text:
Climate change in Germany describes the impacts of anthropogenic climate change on Germany . This includes long - term impacts on agriculture , more intense heatwaves and coldwaves , flash and coastal flooding , and reduced water availability . Debates over how to address these long - term challenges have also sparked changes in the energy sector and in mitigation strategies . Germany 's energiewende ( " energy transition " ) has been a significant political issue in German politics that has made coalition talks difficult for Angela Merkel 's CDU . Despite massive investments in renewable energy , Germany has struggled to reduce coal production and usage . The country remains Europe 's largest importer of coal and produces the 2nd most amount of coal in the European Union behind Poland , about 1 % of the global total . Germany hosted the COP23 meeting in Bonn to which the German delegation traveled in a carbon - neutral train to demonstrate commitment to carbon neutrality .

1. What are the long-term impacts of anthropogenic climate change on Germany?
2. How does climate change affect agriculture in Germany?
3. What types of extreme weather events are intensified by climate change in Germany?
4. How has climate change influenced Germany's energy sector?
5. What is Germany's Energiewende and what political significance does it hold?
6. How has the Energiewende affected coalition negotiations in German politics?
7. What role did Angela Merkel's CDU play in Germany's energy transition debates?
8. What investments has Germany made in renewable energy?
9. Why has Germany struggled to reduce coal production and usage despite investments in renewable energy?
10. What is Germany's ranking in coal importation within Europe?
11. How much coal does Germany produce relative to other European Union countries?
12. What percentage of global coal production does Germany account for?
13. Which country produces the most coal in the European Union?
14. What international climate conference did Germany host and in which city?
15. How did the German delegation demonstrate commitment to carbon neutrality at COP23?
16. What mitigation strategies has Germany adopted in response to climate change?
17. How does climate change affect water availability in Germany?
18. What types of flooding are associated with climate change impacts in Germany?
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
    # ── CLASSES ──────────────────────────────────────────────────────────────

    class ClimateChange(Thing): pass
    class AnthropogenicClimateChange(ClimateChange): pass

    class GeographicEntity(Thing): pass
    class Country(GeographicEntity): pass
    class Continent(GeographicEntity): pass

    class PoliticalUnion(Thing): pass

    class ClimateImpact(Thing): pass
    class AgriculturalImpact(ClimateImpact): pass
    class WaterAvailabilityImpact(ClimateImpact): pass
    class ExtremeWeatherEvent(ClimateImpact): pass
    class Heatwave(ExtremeWeatherEvent): pass
    class Coldwave(ExtremeWeatherEvent): pass
    class Flooding(ExtremeWeatherEvent): pass
    class FlashFlooding(Flooding): pass
    class CoastalFlooding(Flooding): pass

    class EnergySector(Thing): pass
    class EnergySource(Thing): pass
    class Coal(EnergySource): pass
    class RenewableEnergy(EnergySource): pass
    class EnergyPolicy(Thing): pass
    class PoliticalIssue(Thing): pass
    class EnergyTransition(EnergyPolicy, PoliticalIssue): pass

    class MitigationStrategy(Thing): pass
    class CoalitionNegotiation(Thing): pass
    class PoliticalParty(Thing): pass
    class Politician(Thing): pass

    class ClimateConference(Thing): pass
    class City(Thing): pass
    class Delegation(Thing): pass
    class CarbonNeutrality(Thing): pass

    # ── OBJECT PROPERTIES ────────────────────────────────────────────────────

    class hasImpactOn(ObjectProperty):
        domain = [AnthropogenicClimateChange]
        range  = [GeographicEntity]

    class hasImpact(ObjectProperty):
        domain = [AnthropogenicClimateChange]
        range  = [ClimateImpact]

    class sparkedChangeIn(ObjectProperty):
        domain = [ClimateChange]
        range  = [EnergySector]

    class influencedMitigationStrategy(ObjectProperty):
        domain = [ClimateChange]
        range  = [MitigationStrategy]

    class isEnergyTransitionOf(ObjectProperty, FunctionalProperty):
        domain = [EnergyTransition]
        range  = [Country]

    class isPoliticalIssueIn(ObjectProperty):
        domain = [EnergyTransition]
        range  = [Country]

    class madeCoalitionTalksDifficultFor(ObjectProperty):
        domain = [EnergyTransition]
        range  = [PoliticalParty]

    class ledBy(ObjectProperty):
        domain = [PoliticalParty]
        range  = [Politician]

    class investedIn(ObjectProperty):
        domain = [Country]
        range  = [EnergySource]

    class struggledToReduce(ObjectProperty):
        domain = [Country]
        range  = [EnergySource]

    class isLargestCoalImporterIn(ObjectProperty):
        domain = [Country]
        range  = [GeographicEntity]

    class ranksInCoalProductionIn(ObjectProperty):
        domain = [Country]
        range  = [PoliticalUnion]

    class memberOf(ObjectProperty):
        domain = [Country]
        range  = [PoliticalUnion]

    class hosted(ObjectProperty):
        domain = [Country]
        range  = [ClimateConference]

    class heldIn(ObjectProperty, FunctionalProperty):
        domain = [ClimateConference]
        range  = [City]

    class representedBy(ObjectProperty):
        domain = [Country]
        range  = [Delegation]

    class attendedConference(ObjectProperty):
        domain = [Delegation]
        range  = [ClimateConference]

    class demonstratedCommitmentTo(ObjectProperty):
        domain = [Delegation]
        range  = [CarbonNeutrality]

    # ── DATA PROPERTIES ──────────────────────────────────────────────────────

    class coalProductionRankInEU(DataProperty, FunctionalProperty):
        domain = [Country]
        range  = [int]

    class coalShareOfGlobalTotal(DataProperty, FunctionalProperty):
        domain = [Country]
        range  = [float]

    class usedCarbonNeutralTransport(DataProperty, FunctionalProperty):
        domain = [Delegation]
        range  = [bool]

    # ── CLASS RESTRICTIONS ───────────────────────────────────────────────────

    AnthropogenicClimateChange.is_a += [
        hasImpact.some(AgriculturalImpact),
        hasImpact.some(Heatwave),
        hasImpact.some(Coldwave),
        hasImpact.some(FlashFlooding),
        hasImpact.some(CoastalFlooding),
        hasImpact.some(WaterAvailabilityImpact),
    ]

    # ── NAMED INDIVIDUALS ────────────────────────────────────────────────────

    Germany = Country("Germany")
    Germany.label = "Germany"

    Poland = Country("Poland")
    Poland.label = "Poland"

    Europe_i = Continent("Europe")
    Europe_i.label = "Europe"

    EuropeanUnion_i = PoliticalUnion("EuropeanUnion")
    EuropeanUnion_i.label = "European Union"

    AngelaMerkel = Politician("AngelaMerkel")
    AngelaMerkel.label = "Angela Merkel"

    CDU_i = PoliticalParty("CDU")
    CDU_i.label = "CDU"

    Energiewende_i = EnergyTransition("GermanyEnergyTransition")
    Energiewende_i.label = "energiewende"

    COP23_i = ClimateConference("COP23")
    COP23_i.label = "COP23"

    Bonn_i = City("Bonn")
    Bonn_i.label = "Bonn"

    GermanDelegation_i = Delegation("GermanDelegation")
    GermanDelegation_i.label = "German delegation"

    CarbonNeutrality_i = CarbonNeutrality("CarbonNeutralityConcept")
    CarbonNeutrality_i.label = "carbon neutrality"

    Coal_i = Coal("CoalResource")
    Coal_i.label = "coal"

    RenewableEnergy_i = RenewableEnergy("RenewableEnergyResource")
    RenewableEnergy_i.label = "renewable energy"

    GermanyEnergySector_i = EnergySector("GermanyEnergySector")
    GermanyEnergySector_i.label = "Germany energy sector"

    ClimateChangeInGermany_i = AnthropogenicClimateChange("ClimateChangeInGermany")
    ClimateChangeInGermany_i.label = "climate change in Germany"

    # ── ASSERTIONS ───────────────────────────────────────────────────────────

    # Anthropogenic climate change impacts on Germany
    ClimateChangeInGermany_i.hasImpactOn = [Germany]
    ClimateChangeInGermany_i.sparkedChangeIn = [GermanyEnergySector_i]

    # Country memberships in the EU
    Germany.memberOf = [EuropeanUnion_i]
    Poland.memberOf = [EuropeanUnion_i]

    # CDU led by Angela Merkel
    CDU_i.ledBy = [AngelaMerkel]

    # Energiewende
    Energiewende_i.isEnergyTransitionOf = Germany
    Energiewende_i.isPoliticalIssueIn = [Germany]
    Energiewende_i.madeCoalitionTalksDifficultFor = [CDU_i]

    # Germany's energy and coal facts
    Germany.investedIn = [RenewableEnergy_i]
    Germany.struggledToReduce = [Coal_i]
    Germany.isLargestCoalImporterIn = [Europe_i]
    Germany.ranksInCoalProductionIn = [EuropeanUnion_i]
    Poland.ranksInCoalProductionIn = [EuropeanUnion_i]
    Germany.coalProductionRankInEU = 2
    Poland.coalProductionRankInEU = 1
    Germany.coalShareOfGlobalTotal = 0.01

    # COP23 in Bonn hosted by Germany
    Germany.hosted = [COP23_i]
    COP23_i.heldIn = Bonn_i

    # German delegation at COP23
    Germany.representedBy = [GermanDelegation_i]
    GermanDelegation_i.attendedConference = [COP23_i]
    GermanDelegation_i.usedCarbonNeutralTransport = True
    GermanDelegation_i.demonstratedCommitmentTo = [CarbonNeutrality_i]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
