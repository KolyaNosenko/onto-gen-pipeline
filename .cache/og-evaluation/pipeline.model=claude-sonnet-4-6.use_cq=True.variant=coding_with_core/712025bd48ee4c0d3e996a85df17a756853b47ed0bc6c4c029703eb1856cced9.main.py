"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. What type of game is Shadowrun: Hong Kong?
2. Who developed and published Shadowrun: Hong Kong?
3. What previous games did Harebrained Schemes develop before Shadowrun: Hong Kong?
4. What features does Shadowrun: Hong Kong include?
5. When did Harebrained Schemes launch a Kickstarter campaign for Shadowrun: Hong Kong?
6. What was the initial funding goal of the Kickstarter campaign for Shadowrun: Hong Kong?
7. How long did it take to meet the initial funding goal of the Kickstarter campaign?
8. How much money did the Kickstarter campaign receive in total?
9. When did the Kickstarter campaign end?
10. What engine was used to develop Shadowrun: Hong Kong?
11. Which platforms was Shadowrun: Hong Kong developed for?
12. Why did Harebrained Schemes choose not to develop the game for tablets?
13. When was Shadowrun: Hong Kong released worldwide?
14. What does the extended edition of Shadowrun: Hong Kong include?
15. When was the extended edition of Shadowrun: Hong Kong released?
16. Who was eligible to receive the extended edition update for free?
17. What is the Shadowrun universe?
18. What tool was included with Shadowrun: Hong Kong that allows players to create their own campaigns?
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
    NonAgentiveSocialObject,
    Society,
    Accomplishment,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import presentAt


with core:
    # ── Entity Classes ────────────────────────────────────────────────────────

    class VideoGame(NonAgentiveSocialObject):
        """A video game: a non-agentive social object created and shared within a community."""

    class TurnBasedTacticalRPG(VideoGame):
        """A turn-based tactical role-playing video game."""

    class StandaloneExpansion(VideoGame):
        """A standalone expansion to another video game."""

    class GameEdition(VideoGame):
        """A specific edition of an existing video game."""

    class GameDeveloper(Society):
        """A company or organisation that develops and/or publishes video games."""

    class CrowdfundingCampaign(Accomplishment):
        """A crowdfunding campaign that raises funds via an online platform."""

    class FictionalUniverse(NonAgentiveSocialObject):
        """A fictional universe that is the setting for one or more creative works."""

    class SoftwarePlatform(NonAgentiveSocialObject):
        """An operating system or computing platform on which software runs."""

    class LevelEditor(NonAgentiveSocialObject):
        """A software tool that lets users build new game levels or campaigns."""

    # ── Properties ────────────────────────────────────────────────────────────

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [GameDeveloper]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [GameDeveloper]

    class setIn(ObjectProperty):
        domain = [VideoGame]
        range  = [FictionalUniverse]

    class availableOn(ObjectProperty):
        domain = [VideoGame]
        range  = [SoftwarePlatform]

    class isExpansionOf(ObjectProperty):
        domain = [StandaloneExpansion]
        range  = [VideoGame]

    class isEditionOf(ObjectProperty):
        domain = [GameEdition]
        range  = [VideoGame]

    class launchedBy(ObjectProperty):
        domain = [CrowdfundingCampaign]
        range  = [GameDeveloper]

    class fundsGame(ObjectProperty):
        domain = [CrowdfundingCampaign]
        range  = [VideoGame]

    class developedFromEngineOf(ObjectProperty):
        """Links a game to the earlier game(s) whose engine was adapted for its development."""
        domain = [VideoGame]
        range  = [VideoGame]

    class shippedWithLevelEditor(ObjectProperty):
        domain = [VideoGame]
        range  = [LevelEditor]

    class releasedDuring(presentAt):
        """The time interval during which a video game or edition was released."""
        domain = [VideoGame]
        range  = [TimeInterval]

    class launchedDuring(presentAt):
        """The time interval during which a crowdfunding campaign was launched."""
        domain = [CrowdfundingCampaign]
        range  = [TimeInterval]

    class initialFundingGoal(DataProperty, FunctionalProperty):
        domain = [CrowdfundingCampaign]
        range  = [float]

    class totalAmountRaised(DataProperty, FunctionalProperty):
        domain = [CrowdfundingCampaign]
        range  = [float]

    # ── Named Individuals ─────────────────────────────────────────────────────

    # Time intervals
    January2015 = TimeInterval("January2015")
    January2015.label = "January 2015"

    August2015 = TimeInterval("August2015")
    August2015.label = "August 2015"

    February2016 = TimeInterval("February2016")
    February2016.label = "February 2016"

    # Software platforms
    MicrosoftWindows = SoftwarePlatform("MicrosoftWindows")
    MicrosoftWindows.label = "Microsoft Windows"

    OSX = SoftwarePlatform("OSX")
    OSX.label = "OS X"

    Linux = SoftwarePlatform("Linux")
    Linux.label = "Linux"

    # Fictional universe
    ShadowrunUniverse = FictionalUniverse("ShadowrunUniverse")
    ShadowrunUniverse.label = "Shadowrun universe"

    # Game developer
    HarebrainedSchemes = GameDeveloper("HarebrainedSchemes")
    HarebrainedSchemes.label = "Harebrained Schemes"

    # Video games
    ShadowrunReturns = VideoGame("ShadowrunReturns")
    ShadowrunReturns.label = "Shadowrun Returns"
    ShadowrunReturns.developedBy.append(HarebrainedSchemes)
    ShadowrunReturns.publishedBy.append(HarebrainedSchemes)

    Dragonfall = StandaloneExpansion("Dragonfall")
    Dragonfall.label = "Dragonfall"
    Dragonfall.developedBy.append(HarebrainedSchemes)
    Dragonfall.publishedBy.append(HarebrainedSchemes)
    Dragonfall.isExpansionOf.append(ShadowrunReturns)

    ShadowrunHongKong = TurnBasedTacticalRPG("ShadowrunHongKong")
    ShadowrunHongKong.label = "Shadowrun : Hong Kong"
    ShadowrunHongKong.developedBy.append(HarebrainedSchemes)
    ShadowrunHongKong.publishedBy.append(HarebrainedSchemes)
    ShadowrunHongKong.setIn.append(ShadowrunUniverse)
    ShadowrunHongKong.availableOn.append(MicrosoftWindows)
    ShadowrunHongKong.availableOn.append(OSX)
    ShadowrunHongKong.availableOn.append(Linux)
    ShadowrunHongKong.releasedDuring.append(August2015)
    ShadowrunHongKong.developedFromEngineOf.append(ShadowrunReturns)
    ShadowrunHongKong.developedFromEngineOf.append(Dragonfall)

    # Extended edition
    ShadowrunHongKongExtendedEdition = GameEdition("ShadowrunHongKongExtendedEdition")
    ShadowrunHongKongExtendedEdition.label = "extended edition"
    ShadowrunHongKongExtendedEdition.isEditionOf.append(ShadowrunHongKong)
    ShadowrunHongKongExtendedEdition.releasedDuring.append(February2016)

    # Kickstarter campaign
    ShadowrunHongKongKickstarter = CrowdfundingCampaign("ShadowrunHongKongKickstarter")
    ShadowrunHongKongKickstarter.label = "Kickstarter campaign"
    ShadowrunHongKongKickstarter.launchedBy.append(HarebrainedSchemes)
    ShadowrunHongKongKickstarter.fundsGame.append(ShadowrunHongKong)
    ShadowrunHongKongKickstarter.launchedDuring.append(January2015)
    ShadowrunHongKongKickstarter.initialFundingGoal = 100000.0
    ShadowrunHongKongKickstarter.totalAmountRaised = 1200000.0


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
