"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

What was the original name of the city of Austin, Texas?
What is the current name of the city that was originally called Waterloo?
In which state is Austin located?
In which county is Austin located?
In what part of the state is Austin located?
Who visited the Waterloo/Austin area during a buffalo-hunting expedition between 1837 and 1838?
When did Mirabeau B. Lamar visit the area near present-day Austin?
What office did Mirabeau B. Lamar hold in the Republic of Texas?
What did Mirabeau B. Lamar propose after visiting the area?
Where was the capital of the Republic of Texas located before the proposed relocation?
To what geographic area did Lamar propose relocating the capital of the Republic of Texas?
On which river bank was the proposed capital site situated?
Which river was associated with the proposed capital site?
What present-day landmark was near the proposed capital site?
When was the site officially chosen as the capital of the Republic of Texas?
What numbered capital location was this site for the Republic of Texas?
Was this site the final location of the capital of the Republic of Texas?
Under what name was the site incorporated in 1839?
Why was the name changed from Waterloo to Austin?
After whom was Austin named?
Who was known as the “Father of Texas”?
What position did Stephen F. Austin hold in the Republic of Texas?
What is the relationship between Waterloo and Austin?
Which historical entity selected the site as its capital in 1839?
How are Stephen F. Austin and the naming of Austin connected?
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
    NonAgentivePhysicalObject,
    SocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import partOf, temporallyLocatedAt


with core:
    class GeographicalEntity(SpaceRegion):
        pass


    class AdministrativeArea(GeographicalEntity):
        pass


    class City(AdministrativeArea):
        pass


    class County(AdministrativeArea):
        pass


    class State(AdministrativeArea):
        pass


    class StateSubregion(GeographicalEntity):
        pass


    class UrbanRegion(GeographicalEntity):
        pass


    class SiteArea(GeographicalEntity):
        pass


    class RiverBank(GeographicalEntity):
        pass


    class NaturalFeature(NonAgentivePhysicalObject):
        pass


    class River(NaturalFeature):
        pass


    class Landmark(NonAgentivePhysicalObject):
        pass


    class Bridge(Landmark):
        pass


    class PoliticalEntity(Society):
        pass


    class Republic(PoliticalEntity):
        pass


    class Person(AgentivePhysicalObject):
        pass


    class GovernmentOffice(SocialObject):
        pass


    class HonorificTitle(SocialObject):
        pass


    class PlaceName(SocialObject):
        pass


    class HistoricalTimeInterval(TimeInterval):
        pass


    class Expedition(Accomplishment):
        pass


    class BuffaloHuntingExpedition(Expedition):
        pass


    class locatedIn(partOf):
        domain = [GeographicalEntity]
        range = [GeographicalEntity]


    class onRiverBank(ObjectProperty):
        domain = [GeographicalEntity]
        range = [RiverBank]


    class bankOfRiver(ObjectProperty, FunctionalProperty):
        domain = [RiverBank]
        range = [River]


    class nearLandmark(ObjectProperty):
        domain = [GeographicalEntity]
        range = [Landmark]


    class becameCity(ObjectProperty, FunctionalProperty):
        domain = [SiteArea]
        range = [City]


    class currentName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [PlaceName]


    class originalName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [PlaceName]


    class incorporatedUnderName(ObjectProperty, FunctionalProperty):
        domain = [SiteArea]
        range = [PlaceName]


    class renamedTo(ObjectProperty, FunctionalProperty):
        domain = [PlaceName]
        range = [PlaceName]


    class honorsPerson(ObjectProperty):
        domain = [PlaceName]
        range = [Person]


    class visitedArea(ObjectProperty):
        domain = [Person]
        range = [GeographicalEntity]


    class visitTime(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [HistoricalTimeInterval]


    class visitedDuringExpedition(ObjectProperty):
        domain = [Person]
        range = [Expedition]


    class heldOffice(ObjectProperty):
        domain = [Person]
        range = [GovernmentOffice]


    class officeOfPolity(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [PoliticalEntity]


    class proposedCapitalRelocationTarget(ObjectProperty):
        domain = [Person]
        range = [GeographicalEntity]


    class proposedCapitalRelocationFor(ObjectProperty):
        domain = [Person]
        range = [PoliticalEntity]


    class capitalLocatedIn(ObjectProperty):
        domain = [PoliticalEntity]
        range = [GeographicalEntity]


    class officiallyChosenAsCapitalOf(ObjectProperty):
        domain = [SiteArea]
        range = [PoliticalEntity]


    class officialCapitalSelectionTime(ObjectProperty, FunctionalProperty):
        domain = [SiteArea]
        range = [HistoricalTimeInterval]


    class capitalLocationOrdinal(DataProperty, FunctionalProperty):
        domain = [SiteArea]
        range = [int]


    class finalCapitalLocation(DataProperty, FunctionalProperty):
        domain = [SiteArea]
        range = [bool]


    class hasHonorificTitle(ObjectProperty):
        domain = [Person]
        range = [HonorificTitle]


    GovernmentOffice.is_a.append(officeOfPolity.some(PoliticalEntity))
    RiverBank.is_a.append(bankOfRiver.some(River))

    austin_texas_city = City("AustinTexasCity")
    austin_texas_city.label = ["Austin , Texas", "Austin"]

    waterloo_name = PlaceName("WaterlooName")
    waterloo_name.label = "Waterloo"

    austin_name = PlaceName("AustinName")
    austin_name.label = "Austin"

    texas_state = State("TexasState")
    texas_state.label = "Texas"

    travis_county = County("TravisCounty")
    travis_county.label = "Travis County"

    central_part_of_state = StateSubregion("CentralPartOfTexasState")
    central_part_of_state.label = "the central part of the state"

    republic_of_texas = Republic("RepublicOfTexas")
    republic_of_texas.label = "Republic of Texas"

    mirabeau_b_lamar = Person("MirabeauBLamar")
    mirabeau_b_lamar.label = "Mirabeau B. Lamar"

    visit_1837_1838 = HistoricalTimeInterval("Visit1837To1838")
    visit_1837_1838.label = "between 1837 and 1838"

    buffalo_hunting_expedition = BuffaloHuntingExpedition("BuffaloHuntingExpedition1837To1838")
    buffalo_hunting_expedition.label = "a buffalo - hunting expedition"

    houston_city = City("HoustonCity")
    houston_city.label = "Houston"

    proposed_capital_site = SiteArea("ProposedCapitalSite")
    proposed_capital_site.label = (
        "an area situated on the north bank of the Colorado River near the "
        "present - day Ann W. Richards Congress Avenue Bridge in what is now "
        "central Austin"
    )

    north_bank_of_colorado = RiverBank("NorthBankOfColoradoRiver")
    north_bank_of_colorado.label = "the north bank of the Colorado River"

    colorado_river = River("ColoradoRiver")
    colorado_river.label = "Colorado River"

    ann_w_richards_bridge = Bridge("AnnWRichardsCongressAvenueBridge")
    ann_w_richards_bridge.label = "Ann W. Richards Congress Avenue Bridge"

    central_austin = UrbanRegion("CentralAustin")
    central_austin.label = "central Austin"

    year_1839 = HistoricalTimeInterval("Year1839")
    year_1839.label = "1839"

    stephen_f_austin = Person("StephenFAustin")
    stephen_f_austin.label = "Stephen F. Austin"

    father_of_texas = HonorificTitle("FatherOfTexas")
    father_of_texas.label = "Father of Texas"

    republic_of_texas_vice_president = GovernmentOffice("RepublicOfTexasVicePresident")
    republic_of_texas_vice_president.label = "Republic of Texas Vice President"

    republic_first_secretary_of_state = GovernmentOffice("RepublicFirstSecretaryOfState")
    republic_first_secretary_of_state.label = "the republic 's first secretary of state"

    austin_texas_city.currentName = austin_name
    austin_texas_city.originalName = waterloo_name
    austin_texas_city.locatedIn.append(travis_county)
    austin_texas_city.locatedIn.append(texas_state)
    austin_texas_city.locatedIn.append(central_part_of_state)

    travis_county.locatedIn.append(texas_state)
    central_part_of_state.locatedIn.append(texas_state)

    waterloo_name.renamedTo = austin_name
    austin_name.honorsPerson.append(stephen_f_austin)

    republic_of_texas.capitalLocatedIn.append(houston_city)

    republic_of_texas_vice_president.officeOfPolity = republic_of_texas
    republic_first_secretary_of_state.officeOfPolity = republic_of_texas

    mirabeau_b_lamar.visitedArea.append(proposed_capital_site)
    mirabeau_b_lamar.visitTime = visit_1837_1838
    mirabeau_b_lamar.visitedDuringExpedition.append(buffalo_hunting_expedition)
    mirabeau_b_lamar.heldOffice.append(republic_of_texas_vice_president)
    mirabeau_b_lamar.proposedCapitalRelocationTarget.append(proposed_capital_site)
    mirabeau_b_lamar.proposedCapitalRelocationFor.append(republic_of_texas)

    buffalo_hunting_expedition.temporallyLocatedAt = visit_1837_1838

    proposed_capital_site.locatedIn.append(central_austin)
    proposed_capital_site.onRiverBank.append(north_bank_of_colorado)
    proposed_capital_site.nearLandmark.append(ann_w_richards_bridge)
    proposed_capital_site.becameCity = austin_texas_city
    proposed_capital_site.incorporatedUnderName = waterloo_name
    proposed_capital_site.officiallyChosenAsCapitalOf.append(republic_of_texas)
    proposed_capital_site.officialCapitalSelectionTime = year_1839
    proposed_capital_site.capitalLocationOrdinal = 7
    proposed_capital_site.finalCapitalLocation = True

    north_bank_of_colorado.bankOfRiver = colorado_river
    central_austin.locatedIn.append(austin_texas_city)

    stephen_f_austin.heldOffice.append(republic_first_secretary_of_state)
    stephen_f_austin.hasHonorificTitle.append(father_of_texas)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
