"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

1. What was the original name of the city of Austin, Texas?
2. In which county is Austin, Texas located?
3. Who proposed relocating the Republic of Texas capital to the area that became Austin?
4. What position did Mirabeau B. Lamar hold in the Republic of Texas?
5. Between which years did Mirabeau B. Lamar visit the area during a buffalo-hunting expedition?
6. Where was the Republic of Texas capital located before it was moved to Austin?
7. On which river's bank was the new capital site situated?
8. In what year was the site officially chosen as the capital of the Republic of Texas?
9. What was the sequence number of this location as the capital of the Republic of Texas?
10. Under what name was the city originally incorporated?
11. After whom was the city renamed Austin?
12. What was Stephen F. Austin's title or nickname?
13. What role did Stephen F. Austin hold in the Republic of Texas government?
14. What bridge is located near the original capital site in present-day Austin?
15. In which part of Texas is Austin located?
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
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    Accomplishment,
    Society,
    SocialAgent,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import (
    constantPartOf,
    temporallyLocatedAt,
)


with core:
    # ── Entity classes ──────────────────────────────────────────────────────
    class City(Society):
        """A city: a geopolitical settlement that can serve as a capital."""

    class County(Society):
        """An administrative county within a state."""

    class USState(Society):
        """A constituent state of the United States."""

    class Republic(Society):
        """An independent republic."""

    class Person(AgentivePhysicalObject):
        """A human individual."""

    class HuntingExpedition(Accomplishment):
        """An organised journey undertaken to hunt game."""

    class River(NonAgentivePhysicalObject):
        """A natural flowing watercourse."""

    class Bridge(NonAgentivePhysicalObject):
        """A structure spanning a waterway or gap."""

    class GovernmentPosition(SocialAgent):
        """An official position within a government."""

    class VicePresident(GovernmentPosition):
        """The vice-presidential office of a republic or state."""

    class SecretaryOfState(GovernmentPosition):
        """The secretary-of-state office of a republic or state."""

    # ── Properties ──────────────────────────────────────────────────────────
    class locatedIn(constantPartOf):
        """Administrative or geographic containment (transitive)."""
        domain = [Society]
        range  = [Society]

    class originalName(DataProperty, FunctionalProperty):
        """The name a city bore before being renamed."""
        domain = [City]
        range  = [str]

    class capitalOf(ObjectProperty):
        """Relates a city that serves (or served) as capital to its polity."""
        domain = [City]
        range  = [Society]

    class capitalSequenceNumber(DataProperty, FunctionalProperty):
        """Ordinal position of this city as the capital of its polity."""
        domain = [City]
        range  = [int]

    class holdsPosition(ObjectProperty):
        """Relates a person to the government position they hold."""
        domain = [Person]
        range  = [GovernmentPosition]

    class proposedRelocationTo(ObjectProperty):
        """Relates a person who proposed moving a capital to the destination city."""
        domain = [Person]
        range  = [City]

    class namedInHonorOf(ObjectProperty):
        """Relates a city to the person it was renamed to honour."""
        domain = [City]
        range  = [Person]

    class hasNickname(DataProperty, FunctionalProperty):
        """An informal title or honorific given to a person."""
        domain = [Person]
        range  = [str]

    class situatedOnBankOf(ObjectProperty):
        """Relates a city (or settlement site) to the river on whose bank it lies."""
        domain = [City]
        range  = [River]

    class locatedNear(ObjectProperty, SymmetricProperty):
        """Proximity relation between a city and a nearby landmark."""
        domain = [City]
        range  = [Bridge]

    class participatedIn(ObjectProperty):
        """Relates a person to an expedition they took part in."""
        domain = [Person]
        range  = [HuntingExpedition]

    class regionOfState(DataProperty, FunctionalProperty):
        """Informal descriptor of which region of the state the city is in."""
        domain = [City]
        range  = [str]

    # ── Named individuals ───────────────────────────────────────────────────
    republicOfTexas = Republic("Republic_of_Texas")
    republicOfTexas.label = "Republic of Texas"

    texas = USState("Texas")
    texas.label = "Texas"

    travisCounty = County("Travis_County")
    travisCounty.label = "Travis County"

    austinTX = City("Austin_Texas")
    austinTX.label = "Austin, Texas"

    houstonCity = City("Houston")
    houstonCity.label = "Houston"

    coloradoRiver = River("Colorado_River")
    coloradoRiver.label = "Colorado River"

    annRichardsBridge = Bridge("Ann_W_Richards_Congress_Avenue_Bridge")
    annRichardsBridge.label = "Ann W. Richards Congress Avenue Bridge"

    lamar = Person("Mirabeau_B_Lamar")
    lamar.label = "Mirabeau B. Lamar"

    stephenFAustin = Person("Stephen_F_Austin")
    stephenFAustin.label = "Stephen F. Austin"

    buffaloExpedition = HuntingExpedition("BuffaloHuntingExpedition_1837_1838")
    buffaloExpedition.label = "buffalo-hunting expedition"

    interval1837_1838 = TimeInterval("Interval_1837_1838")
    interval1837_1838.label = "1837–1838"

    year1839 = TimeInterval("Year_1839")
    year1839.label = "1839"

    vpPosition = VicePresident("VicePresident_of_Republic_of_Texas")
    vpPosition.label = "Vice President"

    sosPosition = SecretaryOfState("SecretaryOfState_of_Republic_of_Texas")
    sosPosition.label = "Secretary of State"

    # ── Assertions ──────────────────────────────────────────────────────────
    travisCounty.locatedIn = [texas]
    austinTX.locatedIn = [travisCounty]
    austinTX.originalName = "Waterloo"
    austinTX.capitalSequenceNumber = 7
    austinTX.capitalOf.append(republicOfTexas)
    austinTX.namedInHonorOf.append(stephenFAustin)
    austinTX.situatedOnBankOf.append(coloradoRiver)
    austinTX.locatedNear.append(annRichardsBridge)
    austinTX.regionOfState = "central"

    houstonCity.capitalOf.append(republicOfTexas)

    lamar.holdsPosition.append(vpPosition)
    lamar.proposedRelocationTo.append(austinTX)
    lamar.participatedIn.append(buffaloExpedition)
    buffaloExpedition.temporallyLocatedAt = interval1837_1838

    stephenFAustin.hasNickname = "Father of Texas"
    stephenFAustin.holdsPosition.append(sosPosition)

    austinTX.temporallyLocatedAt = year1839


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
