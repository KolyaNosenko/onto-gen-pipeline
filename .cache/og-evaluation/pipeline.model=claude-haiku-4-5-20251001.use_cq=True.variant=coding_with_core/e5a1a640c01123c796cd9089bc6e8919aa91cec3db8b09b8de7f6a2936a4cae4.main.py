"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. Who developed and published Shadowrun: Hong Kong?
2. What type of game is Shadowrun: Hong Kong?
3. What previous Shadowrun games did Harebrained Schemes develop?
4. What features does Shadowrun: Hong Kong include?
5. When was the Kickstarter campaign for Shadowrun: Hong Kong launched?
6. What was the initial funding goal for the Kickstarter campaign?
7. How much money did the Shadowrun: Hong Kong Kickstarter campaign raise?
8. What game engine was used to develop Shadowrun: Hong Kong?
9. Which operating systems was Shadowrun: Hong Kong developed for?
10. When was Shadowrun: Hong Kong released?
11. What is included in the extended edition of Shadowrun: Hong Kong?
12. When was the extended edition of Shadowrun: Hong Kong released?
13. Was the extended edition update free for original game owners?
14. Why did Harebrained Schemes exclude tablet platforms from Shadowrun: Hong Kong development?
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
    NonAgentivePhysicalObject, Society, Accomplishment
)


with core:
    # Domain entity classes
    class VideoGame(NonAgentivePhysicalObject):
        pass

    class GameEngine(NonAgentivePhysicalObject):
        pass

    class OperatingSystem(NonAgentivePhysicalObject):
        pass

    class GameComponent(NonAgentivePhysicalObject):
        pass

    class LevelEditor(GameComponent):
        pass

    class Campaign(GameComponent):
        pass

    class KickstarterCampaign(Accomplishment):
        pass

    # Domain properties
    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Society]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Society]

    class developed(ObjectProperty):
        domain = [Society]
        range = [VideoGame]

    class includes(ObjectProperty):
        domain = [VideoGame]
        range = [GameComponent]

    class usesEngine(ObjectProperty):
        domain = [VideoGame]
        range = [GameEngine]

    class targetsPlatform(ObjectProperty):
        domain = [VideoGame]
        range = [OperatingSystem]

    class initiatedCampaign(ObjectProperty):
        domain = [Society]
        range = [KickstarterCampaign]

    class isExtendedEditionOf(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class initialFundingGoal(DataProperty):
        domain = [KickstarterCampaign]
        range = [str]

    class fundingRaised(DataProperty):
        domain = [KickstarterCampaign]
        range = [str]

    class launchDate(DataProperty):
        domain = [KickstarterCampaign]
        range = [str]

    class endDate(DataProperty):
        domain = [KickstarterCampaign]
        range = [str]

    class releaseDate(DataProperty):
        domain = [VideoGame]
        range = [str]

    class hasDeveloperCommentary(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class hasBugFixes(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    class isFreeUpdateFor(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [bool]

    # Named instances
    shadowrun_hk = VideoGame("ShadowrunHongKong")
    shadowrun_hk.label = "Shadowrun: Hong Kong"

    harebrained = Society("HarebrainedSchemes")
    harebrained.label = "Harebrained Schemes"

    shadowrun_returns = VideoGame("ShadowrunReturns")
    shadowrun_returns.label = "Shadowrun Returns"

    dragonfall = VideoGame("Dragonfall")
    dragonfall.label = "Dragonfall"

    windows = OperatingSystem("MicrosoftWindows")
    windows.label = "Microsoft Windows"

    osx = OperatingSystem("OSX")
    osx.label = "OS X"

    linux = OperatingSystem("Linux")
    linux.label = "Linux"

    engine = GameEngine("ImprovedShadowrunEngine")
    engine.label = "Improved Shadowrun Engine"

    level_editor = LevelEditor("LevelEditorShadowrunHongKong")
    level_editor.label = "Level Editor"

    campaign = Campaign("SinglePlayerCampaignShadowrunHongKong")
    campaign.label = "Single-player campaign"

    kickstarter = KickstarterCampaign("KickstarterCampaignShadowrunHongKong")
    kickstarter.label = "Kickstarter campaign for Shadowrun: Hong Kong"

    extended_edition = VideoGame("ExtendedEditionShadowrunHongKong")
    extended_edition.label = "Extended Edition"

    new_campaign = Campaign("NewCampaignExtendedEdition")
    new_campaign.label = "New campaign in Extended Edition"

    # Property assignments for Shadowrun: Hong Kong
    shadowrun_hk.developedBy = [harebrained]
    shadowrun_hk.publishedBy = [harebrained]
    shadowrun_hk.includes = [level_editor, campaign]
    shadowrun_hk.usesEngine = [engine]
    shadowrun_hk.targetsPlatform = [windows, osx, linux]
    shadowrun_hk.releaseDate = ["August 2015"]

    # Property assignments for Harebrained Schemes
    harebrained.developed = [shadowrun_returns, dragonfall, shadowrun_hk]
    harebrained.initiatedCampaign = [kickstarter]

    # Property assignments for Kickstarter campaign
    kickstarter.initialFundingGoal = ["US$ 100,000"]
    kickstarter.fundingRaised = ["over $ 1.2 million"]
    kickstarter.launchDate = ["January 2015"]
    kickstarter.endDate = ["February 2015"]

    # Property assignments for Extended Edition
    extended_edition.isExtendedEditionOf = [shadowrun_hk]
    extended_edition.includes = [new_campaign]
    extended_edition.releaseDate = ["February 2016"]
    extended_edition.hasDeveloperCommentary = True
    extended_edition.hasBugFixes = True
    extended_edition.isFreeUpdateFor = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
