"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

1. What was the original name of Austin, Texas?

2. In which county and region of Texas is Austin located?

3. Who proposed relocating the Republic of Texas capital to the Austin area?

4. When did Mirabeau B. Lamar visit the area that would become Austin?

5. Where was the Republic of Texas capital located before it was moved to Austin?

6. In what year was Austin officially chosen as the capital of the Republic of Texas?

7. Was Austin the first capital location of the Republic of Texas?

8. On which bank of the Colorado River was Austin's capital site situated?

9. Why was the city renamed from Waterloo to Austin?

10. Who was Stephen F. Austin and what was his role in Texas?

11. What was the reason for relocating the capital to the Austin area?

12. What is the historical significance of the Ann W. Richards Congress Avenue Bridge in relation to Austin's founding?
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

# TODO: import the core entity classes you actually subclass.
# Example:
#     from og_sandbox_with_core.core.entities import SocialObject, NonAgentivePhysicalObject
from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    AmountOfMatter,
    Accomplishment,
    Society,
    TimeInterval,
    SpaceRegion,
)

# TODO (optional): import the core properties you actually subclass.
# Example:
#     from og_sandbox_with_core.core.properties import partOf


with core:
    # TODO: declare your domain entity classes here.
    # Each MUST be a subclass of a class from `og_sandbox_with_core.core.entities`
    # (or of another domain class that ultimately roots in one). Direct
    # subclassing of `Thing` is forbidden — pick the most specific core
    # ancestor that fits.

    class City(NonAgentivePhysicalObject):
        """A city."""
        pass

    class County(SpaceRegion):
        """A county or geographic region."""
        pass

    class River(AmountOfMatter):
        """A river."""
        pass

    class Bridge(NonAgentivePhysicalObject):
        """A bridge."""
        pass

    class Person(AgentivePhysicalObject):
        """A person."""
        pass

    class Organization(Society):
        """An organization or political entity."""
        pass

    class HistoricalEvent(Accomplishment):
        """A historical event."""
        pass

    # TODO: declare your domain ObjectProperty / DataProperty subclasses
    # here. If a core property matches the text's semantics, subclass it;
    # otherwise declare a fresh ObjectProperty / DataProperty with explicit
    # domain / range.

    class locatedIn(ObjectProperty):
        """A city is located in a county."""
        domain = [City]
        range = [County]

    class onNorthBankOf(ObjectProperty):
        """A city is situated on the north bank of a river."""
        domain = [City]
        range = [River]

    class wasNamedAfter(ObjectProperty):
        """A city was named after a person."""
        domain = [City]
        range = [Person]

    class hadOriginalName(DataProperty, FunctionalProperty):
        """A city had an original name."""
        domain = [City]
        range = [str]

    class capitalPosition(DataProperty, FunctionalProperty):
        """A city's position as a capital (ordinal number)."""
        domain = [City]
        range = [int]

    class hadRole(DataProperty):
        """A person had a role or position."""
        domain = [Person]
        range = [str]

    class hadTitle(DataProperty):
        """A person had a title or epithet."""
        domain = [Person]
        range = [str]

    class wasCapitalBefore(ObjectProperty):
        """A city was the capital before another city."""
        domain = [City]
        range = [City]

    class proposedRelocationTo(ObjectProperty):
        """A person proposed relocating the capital to a city."""
        domain = [Person]
        range = [City]

    # TODO: create concrete instances ONLY for named entities the source
    # text mentions by name. Format: name = SomeClass("name_from_text").

    # Create all instances
    austin = City("Austin_City")
    austin.label = "Austin, Texas"
    austin.locatedIn = [County("Travis_County")]
    austin.hadOriginalName = "Waterloo"
    austin.capitalPosition = 7
    austin.onNorthBankOf = [River("Colorado_River")]
    austin.wasNamedAfter = [Person("Stephen_Austin")]

    travisCounty = County("Travis_County")
    travisCounty.label = "Travis County"

    houston = City("Houston_City")
    houston.label = "Houston"
    houston.wasCapitalBefore = [austin]

    coloradoRiver = River("Colorado_River")
    coloradoRiver.label = "Colorado River"

    bridge = Bridge("Ann_Richards_Bridge")
    bridge.label = "Ann W. Richards Congress Avenue Bridge"

    republic = Organization("Republic_Texas")
    republic.label = "Republic of Texas"

    lamar = Person("Mirabeau_Lamar")
    lamar.label = "Mirabeau B. Lamar"

    stephenAustin = Person("Stephen_Austin")
    stephenAustin.label = "Stephen F. Austin"
    stephenAustin.hadTitle = ["Father of Texas"]
    stephenAustin.hadRole = ["first secretary of state"]

    timeInterval_1837_1838 = TimeInterval("TimeInterval_1837_1838")
    timeInterval_1837_1838.label = "1837-1838"

    timeInterval_1839 = TimeInterval("TimeInterval_1839")
    timeInterval_1839.label = "1839"

    expedition = HistoricalEvent("Buffalo_Hunting_Expedition")
    expedition.label = "buffalo-hunting expedition"
    expedition.temporallyLocatedAt = timeInterval_1837_1838

    lamar.constantParticipantOf = [expedition]
    lamar.proposedRelocationTo = [austin]

    choiceEvent = HistoricalEvent("Capital_Choice_1839")
    choiceEvent.label = "site officially chosen as capital"
    choiceEvent.temporallyLocatedAt = timeInterval_1839


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
