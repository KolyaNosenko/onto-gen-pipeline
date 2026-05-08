"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

1. Who was Joos van Cleve?
2. When was Joos van Cleve active as a painter?
3. Where was Joos van Cleve active as a painter?
4. What painting techniques did Joos van Cleve combine in his work?
5. Which guild was Joos van Cleve a member of?
6. What role did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
7. What types of works is Joos van Cleve known for?
8. What artistic characteristics are associated with Joos van Cleve's work?
9. What innovative technique did Joos van Cleve introduce in his paintings?
10. What influence did Joos van Cleve's technique have on later paintings?
11. Who was the father of Cornelis van Cleve?
12. When was Cornelis van Cleve born and when did he die?
13. What was Cornelis van Cleve's profession?
14. What happened to Cornelis van Cleve during his residence in England?
15. What nickname was given to Cornelis van Cleve and what does it mean?
16. What is the approximate birth and death year of Joos van Cleve?
17. What painting styles influenced Joos van Cleve's work?
18. In which century did broad landscapes in painting backgrounds become popular?
19. What is the relationship between Joos van Cleve and Cornelis van Cleve?
20. In which country did Cornelis van Cleve become mentally ill?
=== END TASK INPUT ===

Domain model entry point (with-core variant). Run with `python main.py`
from this directory. The script declares classes and relations inside
`with core:` and writes the resulting graph (core + domain) to
`output.txt` in this directory.
"""
from og_sandbox_with_core.engine import (
    ObjectProperty, DataProperty,
    FunctionalProperty, TransitiveProperty, SymmetricProperty,
    AsymmetricProperty, IrreflexiveProperty,
    Or, And, Not,
    default_world,
)
from og_sandbox_with_core.core import core

from og_sandbox_with_core.core.entities import (
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    State,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import (
    presentAt,
    constantParticipantOf,
)


with core:
    # ── Entity Classes ────────────────────────────────────────────────────────

    class Painter(AgentivePhysicalObject):
        """A person whose profession is painting."""

    class City(NonAgentivePhysicalObject):
        """A city or urban settlement."""

    class Country(NonAgentivePhysicalObject):
        """A sovereign country or nation."""

    class PaintingWork(NonAgentivePhysicalObject):
        """A physical painting artefact."""

    class ReligiousPainting(PaintingWork):
        """A painting with a religious subject."""

    class Portrait(PaintingWork):
        """A portrait painting."""

    class PaintingTechnique(NonAgentiveSocialObject):
        """A named painting technique or tradition."""

    class PaintingStyle(NonAgentiveSocialObject):
        """A named painting style or movement."""

    class Guild(Society):
        """An artisan or professional guild."""

    class MentalIllness(State):
        """A state of mental illness experienced by a person."""

    # ── Object & Data Properties ──────────────────────────────────────────────

    class activeIn(ObjectProperty):
        """City where a painter was professionally active."""
        domain = [Painter]
        range  = [City]

    class activeDuring(presentAt):
        """Time interval during which a painter was professionally active."""
        domain = [Painter]
        range  = [TimeInterval]

    class memberOf(ObjectProperty):
        """Guild to which a painter belonged."""
        domain = [Painter]
        range  = [Guild]

    class hasGuildRole(DataProperty, FunctionalProperty):
        """Role held by a painter within a guild."""
        domain = [Painter]
        range  = [str]

    class combinedTechnique(ObjectProperty):
        """Painting technique combined or employed by a painter."""
        domain = [Painter]
        range  = [PaintingTechnique]

    class influencedBy(ObjectProperty):
        """Painting style that influenced a painter's work."""
        domain = [Painter]
        range  = [PaintingStyle]

    class fatherOf(ObjectProperty, AsymmetricProperty, IrreflexiveProperty):
        """Parental relation: the subject is the father of the object."""
        domain = [Painter]
        range  = [Painter]

    class residedIn(ObjectProperty):
        """Country in which a painter resided at some point."""
        domain = [Painter]
        range  = [Country]

    class hasNickname(DataProperty, FunctionalProperty):
        """Nickname by which a painter was known."""
        domain = [Painter]
        range  = [str]

    class nicknameExplanation(DataProperty, FunctionalProperty):
        """Meaning or explanation of a painter's nickname."""
        domain = [Painter]
        range  = [str]

    class guildLocatedIn(ObjectProperty, FunctionalProperty):
        """City in which a guild is based."""
        domain = [Guild]
        range  = [City]

    class introducedTechnique(ObjectProperty):
        """Painting technique introduced or pioneered by a painter."""
        domain = [Painter]
        range  = [PaintingTechnique]

    class birthYear(DataProperty, FunctionalProperty):
        """Year of birth, as a string to accommodate approximate values."""
        domain = [Painter]
        range  = [str]

    class deathYear(DataProperty, FunctionalProperty):
        """Year of death, as a string to accommodate approximate values."""
        domain = [Painter]
        range  = [str]

    class worksKnownFor(DataProperty):
        """Type of works a painter is primarily known for."""
        domain = [Painter]
        range  = [str]

    class artisticCharacteristic(DataProperty):
        """Artistic quality or characteristic associated with a painter's work."""
        domain = [Painter]
        range  = [str]

    class popularIn(ObjectProperty):
        """Time interval during which a technique became popular."""
        domain = [PaintingTechnique]
        range  = [TimeInterval]

    class popularAmong(ObjectProperty):
        """Painting style or tradition in which a technique became popular."""
        domain = [PaintingTechnique]
        range  = [PaintingStyle]

    # ── Named Individuals ─────────────────────────────────────────────────────

    # Time intervals
    joos_life          = TimeInterval("JoosVanCleve_LifeSpan")
    joos_life.label    = "c. 1485 \u2013 1540/1541"

    joos_active_period       = TimeInterval("JoosVanCleve_ActivePeriod")
    joos_active_period.label = "around 1511 to 1540"

    cornelis_life       = TimeInterval("CornelisVanCleve_LifeSpan")
    cornelis_life.label = "1520 - 1567"

    sixteenth_century       = TimeInterval("SixteenthCentury")
    sixteenth_century.label = "sixteenth century"

    # Places
    antwerp       = City("Antwerp")
    antwerp.label = "Antwerp"

    england       = Country("England")
    england.label = "England"

    # Guild
    guild_saint_luke              = Guild("GuildOfSaintLukeOfAntwerp")
    guild_saint_luke.label        = "Guild of Saint Luke of Antwerp"
    guild_saint_luke.guildLocatedIn = antwerp

    # Painting styles
    northern_renaissance       = PaintingStyle("NorthernRenaissancePaintingStyle")
    northern_renaissance.label = "northern Renaissance"

    renaissance_style       = PaintingStyle("RenaissancePaintingStyle")
    renaissance_style.label = "Renaissance painting styles"

    # Painting techniques
    netherlandish_technique       = PaintingTechnique("NetherlandishPaintingTechnique")
    netherlandish_technique.label = "traditional Netherlandish painting techniques"

    broad_landscapes       = PaintingTechnique("BroadLandscapesTechnique")
    broad_landscapes.label = "broad landscapes in the backgrounds"
    broad_landscapes.popularIn.append(sixteenth_century)
    broad_landscapes.popularAmong.append(northern_renaissance)

    # Painters
    cornelis             = Painter("CornelisVanCleve")
    cornelis.label       = "Cornelis van Cleve"
    cornelis.birthYear   = "1520"
    cornelis.deathYear   = "1567"
    cornelis.presentAt.append(cornelis_life)
    cornelis.residedIn.append(england)
    cornelis.hasNickname         = "Sotte Cleef"
    cornelis.nicknameExplanation = "mad Cleef"

    cornelis_illness       = MentalIllness("CornelisVanCleve_MentalIllness")
    cornelis_illness.label = "mental illness of Cornelis van Cleve"
    cornelis.constantParticipantOf.append(cornelis_illness)

    joos       = Painter("JoosVanCleve")
    joos.label = ["Joos van Cleve", "Joos van der Beke"]
    joos.birthYear = "c. 1485"
    joos.deathYear = "1540/1541"
    joos.presentAt.append(joos_life)
    joos.activeIn.append(antwerp)
    joos.activeDuring.append(joos_active_period)
    joos.memberOf.append(guild_saint_luke)
    joos.hasGuildRole = "co-deacon"
    joos.combinedTechnique.append(netherlandish_technique)
    joos.influencedBy.append(renaissance_style)
    joos.introducedTechnique.append(broad_landscapes)
    joos.worksKnownFor.append("religious works")
    joos.worksKnownFor.append("portraits of royalty")
    joos.artisticCharacteristic.append("sensitivity to color")
    joos.artisticCharacteristic.append("unique solidarity of figures")
    joos.fatherOf.append(cornelis)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
