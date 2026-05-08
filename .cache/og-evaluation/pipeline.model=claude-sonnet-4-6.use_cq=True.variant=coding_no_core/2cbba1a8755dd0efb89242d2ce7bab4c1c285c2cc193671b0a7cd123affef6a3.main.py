"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What is the location of Collins Street?
2. When was Collins Street laid out?
3. What grid plan was Collins Street part of?
4. Who was Collins Street named after?
5. What role did David Collins hold?
6. What settlement did David Collins help establish?
7. When was the settlement at Sorrento established?
8. What is the colloquial name for the eastern end of Collins Street?
9. Since when has the eastern end of Collins Street been known by its colloquial name?
10. What features characterize the eastern end of Collins Street?
11. Where were the first sidewalk cafes in Melbourne located?
12. Which street intersects with Collins Street to form the financial district?
13. What types of businesses established themselves around Queen Street in the 19th century?
14. What types of buildings are found along Collins Street today?
15. What was the first survey of Melbourne?
16. When did Collins Street become the most desired address in the city?
17. What heritage features does the Paris End of Collins Street contain?
18. What financial institutions were historically located near Queen Street?
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
    # ── Entity Classes ────────────────────────────────────────────────────────

    # Geographic places
    class Place(Thing): pass
    class Street(Place): pass
    class City(Place): pass
    class State(Place): pass
    class Country(Place): pass
    class Settlement(Place): pass

    # People and roles
    class Person(Thing): pass
    class GovernmentRole(Thing): pass

    # Survey / cartography – a grid plan is itself a survey
    class Survey(Thing): pass
    class GridPlan(Survey): pass

    # Street subdivision
    class StreetSection(Thing): pass

    # Built-environment features referenced by the text
    class HeritageBuilding(Thing): pass
    class StreetTree(Thing): pass
    class ShoppingBoutique(Thing): pass
    class SidewalkCafe(Thing): pass

    # Office buildings
    class OfficeBuilding(Thing): pass
    class OfficeBlock(OfficeBuilding): pass
    class Skyscraper(OfficeBuilding): pass

    # Financial institutions
    class FinancialInstitution(Thing): pass
    class Bank(FinancialInstitution): pass
    class InsuranceCompany(FinancialInstitution): pass

    # Time periods
    class TimePeriod(Thing): pass
    class Decade(TimePeriod): pass
    class Century(TimePeriod): pass

    # ── Object Properties ─────────────────────────────────────────────────────

    # Transitive geographic containment (Melbourne in Victoria in Australia)
    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    # Collins Street named after David Collins
    class namedAfter(ObjectProperty):
        domain = [Street]
        range  = [Person]

    # Collins Street was laid out in the Hoddle Grid survey
    class laidOutIn(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range  = [Survey]

    # David Collins held the role of Lieutenant-Governor
    class hasRole(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range  = [GovernmentRole]

    # David Collins established a settlement
    class establishedSettlement(ObjectProperty):
        domain = [Person]
        range  = [Settlement]

    # The Sorrento settlement is at the place Sorrento
    class locatedAt(ObjectProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [Place]

    # Paris End is a section of Collins Street
    class isPartOf(ObjectProperty, TransitiveProperty):
        domain = [StreetSection]
        range  = [Street]

    # Paris End has been known as such since the 1950s
    class knownSince(ObjectProperty, FunctionalProperty):
        domain = [StreetSection]
        range  = [TimePeriod]

    # Features of the Paris End section
    class containsHeritageBuilding(ObjectProperty):
        domain = [StreetSection]
        range  = [HeritageBuilding]

    class containsStreetTree(ObjectProperty):
        domain = [StreetSection]
        range  = [StreetTree]

    class containsShoppingBoutique(ObjectProperty):
        domain = [StreetSection]
        range  = [ShoppingBoutique]

    class containsSidewalkCafe(ObjectProperty):
        domain = [StreetSection]
        range  = [SidewalkCafe]

    # Collins Street intersects Queen Street (symmetric)
    class intersectsWith(ObjectProperty, SymmetricProperty):
        domain = [Street]
        range  = [Street]

    # The area centred around Queen Street became the financial heart of Melbourne
    class financialHeartOf(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range  = [City]

    # Queen Street became the financial heart in the 19th century
    class becameFinancialHeartIn(ObjectProperty, FunctionalProperty):
        domain = [Street]
        range  = [Century]

    # Banks and insurance companies historically near Queen Street
    class historicallyLocatedNear(ObjectProperty):
        domain = [FinancialInstitution]
        range  = [Street]

    # Prestigious office blocks and skyscrapers along Collins Street today
    class locatedAlongStreet(ObjectProperty):
        domain = [OfficeBuilding]
        range  = [Street]

    # ── Data Properties ───────────────────────────────────────────────────────

    # Paris End colloquial name as a string
    class hasColloquialName(DataProperty, FunctionalProperty):
        domain = [StreetSection]
        range  = [str]

    # Year the Sorrento settlement was established (1803)
    class establishedYear(DataProperty, FunctionalProperty):
        domain = [Settlement]
        range  = [int]

    # Year the grid plan was produced (1837)
    class gridYear(DataProperty, FunctionalProperty):
        domain = [GridPlan]
        range  = [int]

    # ── Individuals ───────────────────────────────────────────────────────────

    # Geographic places
    australia = Country("Australia")
    australia.label = "Australia"

    victoria = State("Victoria")
    victoria.label = "Victoria"
    victoria.locatedIn = [australia]

    melbourne = City("Melbourne")
    melbourne.label = "Melbourne"
    melbourne.locatedIn = [victoria]

    sorrento = Place("Sorrento")
    sorrento.label = "Sorrento"
    sorrento.locatedIn = [victoria]

    # Streets  (spaces replaced by underscores in local IRI names)
    collins_street = Street("Collins_Street")
    collins_street.label = "Collins Street"
    collins_street.locatedIn = [melbourne]

    queen_street = Street("Queen_Street")
    queen_street.label = "Queen Street"
    queen_street.locatedIn = [melbourne]

    collins_street.intersectsWith = [queen_street]

    # Survey / grid plan
    hoddle_grid = GridPlan("Hoddle_Grid")
    hoddle_grid.label = "Hoddle Grid"
    hoddle_grid.gridYear = 1837

    collins_street.laidOutIn = hoddle_grid

    # Person: David Collins, Lieutenant-Governor
    david_collins = Person("David_Collins")
    david_collins.label = "David Collins"

    lt_governor = GovernmentRole("Lieutenant-Governor")
    lt_governor.label = "Lieutenant-Governor"

    david_collins.hasRole = lt_governor
    collins_street.namedAfter = [david_collins]

    # Settlement at Sorrento established in 1803
    sorrento_settlement = Settlement("Settlement_at_Sorrento")
    sorrento_settlement.label = "settlement at Sorrento"
    sorrento_settlement.locatedAt = sorrento
    sorrento_settlement.establishedYear = 1803

    david_collins.establishedSettlement = [sorrento_settlement]

    # Time periods
    the_1950s = Decade("The_1950s")
    the_1950s.label = "the 1950s"

    the_19th_century = Century("The_19th_Century")
    the_19th_century.label = "the 19th century"

    # Eastern end of Collins Street: the "Paris End"
    paris_end = StreetSection("Paris_End")
    paris_end.label = "Paris End"
    paris_end.hasColloquialName = "Paris End"
    paris_end.isPartOf = [collins_street]
    paris_end.knownSince = the_1950s

    # Financial area centred around Queen Street
    queen_street.financialHeartOf = melbourne
    queen_street.becameFinancialHeartIn = the_19th_century


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
