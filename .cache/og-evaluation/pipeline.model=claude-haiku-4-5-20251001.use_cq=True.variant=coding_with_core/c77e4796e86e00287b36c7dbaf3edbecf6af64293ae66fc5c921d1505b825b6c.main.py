"""
=== TASK INPUT ===
Source text:
The American Association for Nude Recreation ( AANR ) is a naturist organization based in the United States . The AANR is the largest , longest - established organization of its kind in North America . It was founded in 1931 under its previous name American Sunbathing Association . Approximately 200 nudist resorts , clubs , and businesses choose to affiliate with AANR , and AANR serves over 30,000 members in the United States , Canada , Mexico , French West Indies , Virgin Islands , and St. Martin . The AANR promotes the benefits of wholesome nude family recreation and works to protect the rights of nudists in appropriate settings , such as sanctioned nude beaches and public lands set aside for that use ; as well as homes , private backyards , plus AANR - affiliated clubs , campgrounds and resorts . The AANR uses a portion of its collected membership fees to be politically active by campaigning and lobbying governments fighting to allow nudism in the US and Canada .

1. What is the American Association for Nude Recreation (AANR)?

2. When was the AANR founded and under what previous name?

3. How many members does the AANR serve and in which geographic regions?

4. How many nudist resorts, clubs, and businesses are affiliated with the AANR?

5. What are the primary objectives and missions of the AANR?

6. What types of settings does the AANR promote for nude recreation?

7. How does the AANR use its membership fees?

8. What political activities does the AANR engage in?

9. Which countries and territories does the AANR serve its members in?

10. What is the historical significance of the AANR in North America?

11. What rights does the AANR work to protect and in which contexts?

12. What benefits of nude recreation does the AANR promote?
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

from og_sandbox_with_core.core.entities import AgentiveSocialObject, Event, SpaceRegion


with core:
    # Domain entity classes
    class NaturistOrganization(AgentiveSocialObject):
        """An organization that promotes naturism and nudism"""
        pass
    
    class PoliticalActivity(Event):
        """Campaigning, lobbying, and other political activities"""
        pass
    
    # Domain ObjectProperty / DataProperty subclasses
    class previousName(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class foundedYear(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [int]
    
    class memberCount(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [int]
    
    class affiliatedFacilityCount(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [int]
    
    class basedIn(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class servesCountry(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class mission(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class recreationSettings(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class promotedBenefits(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class protectsRights(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class protectionContexts(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class largestLongestEstablishedIn(DataProperty, FunctionalProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class politicalActivities(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class usesMembershipFeesFor(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    class fightsTolegalizeIn(DataProperty):
        domain = [NaturistOrganization]
        range = [str]
    
    # Concrete instances for named entities
    aanr = NaturistOrganization("AANR")
    aanr.label = "American Association for Nude Recreation (AANR)"
    aanr.previousName = "American Sunbathing Association"
    aanr.foundedYear = 1931
    aanr.memberCount = 30000
    aanr.affiliatedFacilityCount = 200
    aanr.basedIn = "United States"
    aanr.servesCountry.append("United States")
    aanr.servesCountry.append("Canada")
    aanr.servesCountry.append("Mexico")
    aanr.servesCountry.append("French West Indies")
    aanr.servesCountry.append("Virgin Islands")
    aanr.servesCountry.append("St. Martin")
    aanr.mission.append("Promote wholesome nude family recreation")
    aanr.mission.append("Protect the rights of nudists in appropriate settings")
    aanr.recreationSettings.append("Sanctioned nude beaches")
    aanr.recreationSettings.append("Public lands set aside for that use")
    aanr.recreationSettings.append("Homes")
    aanr.recreationSettings.append("Private backyards")
    aanr.recreationSettings.append("AANR-affiliated clubs")
    aanr.recreationSettings.append("Campgrounds")
    aanr.recreationSettings.append("Resorts")
    aanr.promotedBenefits.append("Wholesome nude family recreation")
    aanr.protectsRights.append("Rights of nudists")
    aanr.protectionContexts.append("Sanctioned nude beaches")
    aanr.protectionContexts.append("Public lands set aside for that use")
    aanr.protectionContexts.append("Homes")
    aanr.protectionContexts.append("Private backyards")
    aanr.protectionContexts.append("AANR-affiliated clubs")
    aanr.protectionContexts.append("Campgrounds")
    aanr.protectionContexts.append("Resorts")
    aanr.largestLongestEstablishedIn = "North America"
    aanr.politicalActivities.append("Campaigning")
    aanr.politicalActivities.append("Lobbying")
    aanr.usesMembershipFeesFor.append("Political activities")
    aanr.fightsTolegalizeIn.append("United States")
    aanr.fightsTolegalizeIn.append("Canada")
    
    # Geographic regions
    united_states = SpaceRegion("UnitedStates")
    united_states.label = "United States"
    
    north_america = SpaceRegion("NorthAmerica")
    north_america.label = "North America"
    
    canada = SpaceRegion("Canada")
    canada.label = "Canada"
    
    mexico = SpaceRegion("Mexico")
    mexico.label = "Mexico"
    
    french_west_indies = SpaceRegion("FrenchWestIndies")
    french_west_indies.label = "French West Indies"
    
    virgin_islands = SpaceRegion("VirginIslands")
    virgin_islands.label = "Virgin Islands"
    
    st_martin = SpaceRegion("StMartin")
    st_martin.label = "St. Martin"


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
