"""
=== TASK INPUT ===
Source text:
Collins Street is a major street in the centre of Melbourne , Victoria in Australia . It was laid out in the first survey of Melbourne , the original 1837 Hoddle Grid , and soon became the most desired address in the city . Collins Street was named after Lieutenant - Governor David Collins who led a group of settlers in establishing a short - lived settlement at Sorrento in 1803 . The eastern end of Collins Street has been known colloquially as the ' Paris End ' since the 1950s due to its numerous heritage buildings , old street trees , high - end shopping boutiques , and as the location for the first sidewalk cafes in the city . Blocks further west centred around Queen Street became the financial heart of Melbourne in the 19th century , the preferred home of major banks and insurance companies , a tradition which continues today with the most prestigious office blocks and skyscrapers found along its length .

1. What is the location of Collins Street?
2. When was Collins Street laid out?
3. What grid system was Collins Street part of?
4. After whom was Collins Street named?
5. What was the role of David Collins?
6. What settlement did David Collins help establish?
7. When was the settlement at Sorrento established?
8. What is the eastern end of Collins Street colloquially known as?
9. Since when has the eastern end of Collins Street been known as the 'Paris End'?
10. What features characterize the 'Paris End' of Collins Street?
11. Where were the first sidewalk cafes in Melbourne located?
12. Which street became the financial heart of Melbourne in the 19th century?
13. What types of businesses were historically located around Queen Street?
14. What types of buildings are found along Collins Street today?
15. What was the most desired address in Melbourne?
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
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    AgentivePhysicalObject,
    Society,
    SocialAgent,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import constantProperPartOf, presentAt


with core:
    # ── Base entity classes ─────────────────────────────────────────────

    class Street(NonAgentivePhysicalObject):
        """A street in an urban area."""

    class City(NonAgentivePhysicalObject):
        """A city."""

    class StateTerritory(NonAgentivePhysicalObject):
        """A state or territory within a country."""

    class Country(NonAgentivePhysicalObject):
        """A sovereign country."""

    class Settlement(NonAgentivePhysicalObject):
        """A settlement established by a group of people."""

    class UrbanPlanningGrid(NonAgentiveSocialObject):
        """A surveying and planning grid used to lay out streets in a city."""

    class Person(AgentivePhysicalObject):
        """A human individual."""

    class LieutenantGovernor(SocialAgent):
        """The social role of a lieutenant-governor."""

    class StreetSection(NonAgentivePhysicalObject):
        """A named or informally designated section of a street."""

    class HeritageBuilding(NonAgentivePhysicalObject):
        """A building listed or recognised for its heritage value."""

    class StreetTree(NonAgentivePhysicalObject):
        """A tree planted along a street."""

    class ShoppingBoutique(NonAgentivePhysicalObject):
        """A high-end specialty retail shop."""

    class SidewalkCafe(NonAgentivePhysicalObject):
        """A cafe with outdoor seating on the footpath."""

    class OfficeBlock(NonAgentivePhysicalObject):
        """A building primarily used for commercial office space."""

    class Skyscraper(NonAgentivePhysicalObject):
        """A very tall commercial building."""

    class Bank(Society):
        """A financial institution providing banking services."""

    class InsuranceCompany(Society):
        """A company providing insurance products."""

    # ── Properties ──────────────────────────────────────────────────────

    class locatedIn(ObjectProperty, TransitiveProperty):
        """Geographical containment: x is located within y."""
        domain = [NonAgentivePhysicalObject]
        range  = [NonAgentivePhysicalObject]

    class namedAfter(ObjectProperty, FunctionalProperty):
        """The street was named after this person."""
        domain = [Street]
        range  = [Person]

    class laidOutIn(ObjectProperty, FunctionalProperty):
        """The street was laid out as part of this planning grid."""
        domain = [Street]
        range  = [UrbanPlanningGrid]

    class sectionOf(constantProperPartOf):
        """A street section is a proper constant part of a street."""
        domain = [StreetSection]
        range  = [Street]

    class colloquiallyKnownAs(DataProperty, FunctionalProperty):
        """The informal colloquial name used for this street section."""
        domain = [StreetSection]
        range  = [str]

    class knownSince(presentAt, FunctionalProperty):
        """The time interval from which this street section has been known by its colloquial name."""
        domain = [StreetSection]
        range  = [TimeInterval]

    class ledEstablishmentOf(ObjectProperty):
        """This person led the establishment of the given settlement."""
        domain = [Person]
        range  = [Settlement]

    class establishedDuring(presentAt, FunctionalProperty):
        """The time interval during which the settlement was established."""
        domain = [Settlement]
        range  = [TimeInterval]

    class heldPosition(DataProperty, FunctionalProperty):
        """The official title or role held by this person."""
        domain = [Person]
        range  = [str]

    class createdDuring(presentAt, FunctionalProperty):
        """The time interval during which this planning grid was created."""
        domain = [UrbanPlanningGrid]
        range  = [TimeInterval]

    class financialCentreOf(ObjectProperty, FunctionalProperty):
        """This street is or was the financial centre of the given city."""
        domain = [Street]
        range  = [City]

    class becameFinancialCentreIn(presentAt, FunctionalProperty):
        """The time interval in which this street became the financial centre."""
        domain = [Street]
        range  = [TimeInterval]

    class hasAdjacentBuilding(ObjectProperty):
        """A type of building found adjacent to or along this street."""
        domain = [Street]
        range  = [NonAgentivePhysicalObject]

    class hostsBusiness(ObjectProperty):
        """A type of business organisation hosted along this street."""
        domain = [Street]
        range  = [Society]

    class hasCharacteristicFeature(ObjectProperty):
        """A type of physical feature that characterises this street section."""
        domain = [StreetSection]
        range  = [NonAgentivePhysicalObject]

    class mostDesiredAddressOf(ObjectProperty, FunctionalProperty):
        """This street is (or was) the most desired address in the given city."""
        domain = [Street]
        range  = [City]

    # ── Restricted sub-classes ───────────────────────────────────────────

    class HeritageShoppingDistrict(StreetSection):
        """A street section characterised by heritage buildings, street trees,
        high-end boutiques, and sidewalk cafes."""
        is_a = [
            hasCharacteristicFeature.some(HeritageBuilding),
            hasCharacteristicFeature.some(StreetTree),
            hasCharacteristicFeature.some(ShoppingBoutique),
            hasCharacteristicFeature.some(SidewalkCafe),
        ]

    class FinancialDistrict(Street):
        """A street that serves (or served) as a financial district,
        home to banks and insurance companies."""
        is_a = [
            hostsBusiness.some(Bank),
            hostsBusiness.some(InsuranceCompany),
        ]

    class PremiumCommercialStreet(Street):
        """A street lined with prestigious office blocks and skyscrapers."""
        is_a = [
            hasAdjacentBuilding.some(OfficeBlock),
            hasAdjacentBuilding.some(Skyscraper),
        ]

    # ── Named instances ──────────────────────────────────────────────────
    # Constructor argument = URI-safe local name; .label = exact text mention.

    # Time intervals
    Year1803 = TimeInterval("Year_1803")
    Year1803.label = "1803"

    Year1837 = TimeInterval("Year_1837")
    Year1837.label = "1837"

    Decade1950s = TimeInterval("Decade_1950s")
    Decade1950s.label = "1950s"

    Century19th = TimeInterval("Century_19th")
    Century19th.label = "19th century"

    # Geographical places
    AustraliaInst = Country("Australia")
    AustraliaInst.label = "Australia"

    VictoriaInst = StateTerritory("Victoria")
    VictoriaInst.label = "Victoria"
    VictoriaInst.locatedIn.append(AustraliaInst)

    MelbourneInst = City("Melbourne")
    MelbourneInst.label = "Melbourne"
    MelbourneInst.locatedIn.append(VictoriaInst)

    SorrentoInst = Settlement("Sorrento")
    SorrentoInst.label = "Sorrento"
    SorrentoInst.establishedDuring = Year1803

    # Urban planning grid
    HoddelGridInst = UrbanPlanningGrid("Hoddle_Grid")
    HoddelGridInst.label = "Hoddle Grid"
    HoddelGridInst.createdDuring = Year1837

    # Person
    DavidCollinsInst = Person("David_Collins")
    DavidCollinsInst.label = "David Collins"
    DavidCollinsInst.heldPosition = "Lieutenant-Governor"
    DavidCollinsInst.ledEstablishmentOf.append(SorrentoInst)

    # Streets
    CollinsStreetInst = PremiumCommercialStreet("Collins_Street")
    CollinsStreetInst.label = "Collins Street"
    CollinsStreetInst.locatedIn.append(MelbourneInst)
    CollinsStreetInst.laidOutIn = HoddelGridInst
    CollinsStreetInst.namedAfter = DavidCollinsInst
    CollinsStreetInst.mostDesiredAddressOf = MelbourneInst

    QueenStreetInst = FinancialDistrict("Queen_Street")
    QueenStreetInst.label = "Queen Street"
    QueenStreetInst.locatedIn.append(MelbourneInst)
    QueenStreetInst.financialCentreOf = MelbourneInst
    QueenStreetInst.becameFinancialCentreIn = Century19th

    # Street section
    ParisEndInst = HeritageShoppingDistrict("Paris_End")
    ParisEndInst.label = "Paris End"
    ParisEndInst.sectionOf.append(CollinsStreetInst)
    ParisEndInst.colloquiallyKnownAs = "Paris End"
    ParisEndInst.knownSince = Decade1950s


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
