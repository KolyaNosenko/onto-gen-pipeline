"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

What is Shadowrun: Hong Kong?
In which fictional universe is Shadowrun: Hong Kong set?
What genre is Shadowrun: Hong Kong?
Who developed Shadowrun: Hong Kong?
Who published Shadowrun: Hong Kong?
Which previous games had Harebrained Schemes developed before Shadowrun: Hong Kong?
Is Shadowrun: Hong Kong a standalone game or an expansion?
What type of campaign does Shadowrun: Hong Kong include?
Does Shadowrun: Hong Kong include a level editor?
What can players create with the level editor in Shadowrun: Hong Kong?
Can players share their custom Shadowrun campaigns with other players?
When was the Kickstarter campaign for Shadowrun: Hong Kong launched?
Who launched the Kickstarter campaign for Shadowrun: Hong Kong?
Why was the Kickstarter campaign for Shadowrun: Hong Kong launched?
What was the initial funding goal of the Shadowrun: Hong Kong Kickstarter campaign?
How quickly was the initial funding goal reached?
When did the Kickstarter campaign end?
How much money did the Kickstarter campaign receive in total?
What engine was used to develop Shadowrun: Hong Kong?
Was Shadowrun: Hong Kong developed with an improved version of the engine used for earlier Shadowrun games?
Which games previously used the engine improved for Shadowrun: Hong Kong?
For which platforms was Shadowrun: Hong Kong developed?
Why was Shadowrun: Hong Kong developed only for Microsoft Windows, OS X, and Linux?
What hardware limitations did Harebrained Schemes avoid by not developing the game for tablets?
When was Shadowrun: Hong Kong released worldwide?
Was Shadowrun: Hong Kong released worldwide in August 2015?
Was an extended edition of Shadowrun: Hong Kong released?
When was the extended edition of Shadowrun: Hong Kong released?
What new content was included in the extended edition of Shadowrun: Hong Kong?
Did the extended edition include a new campaign?
Did the extended edition include developer commentary?
Did the extended edition include bug fixes for the original game?
Was the extended edition update free for owners of the original game?
Who was eligible to receive the extended edition update for free?
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
    Abstract,
    Accomplishment,
    NonAgentivePhysicalObject,
    NonAgentiveSocialObject,
    SocialObject,
    Society,
    TimeInterval,
)


with core:
    class FictionalUniverse(SocialObject):
        pass


    class GameStudio(Society):
        pass


    class VideoGame(NonAgentiveSocialObject):
        pass


    class StandaloneVideoGame(VideoGame):
        pass


    class VideoGameExpansion(VideoGame):
        pass


    class TurnBasedTacticalRolePlayingVideoGame(StandaloneVideoGame):
        pass


    class GameContent(NonAgentiveSocialObject):
        pass


    class GameCampaign(GameContent):
        pass


    class SinglePlayerCampaign(GameCampaign):
        pass


    class ShadowrunCampaign(GameCampaign):
        pass


    class PlayerCreatedShadowrunCampaign(ShadowrunCampaign):
        pass


    class LevelEditor(GameContent):
        pass


    class CrowdfundingPlatform(NonAgentiveSocialObject):
        pass


    class CrowdfundingCampaign(Accomplishment):
        pass


    class KickstarterCampaign(CrowdfundingCampaign):
        pass


    class FeatureContentSet(GameContent):
        pass


    class MonetaryAmount(Abstract):
        pass


    class DurationDescription(Abstract):
        pass


    class GameEngine(NonAgentiveSocialObject):
        pass


    class ImprovedGameEngine(GameEngine):
        pass


    class OperatingSystem(NonAgentiveSocialObject):
        pass


    class HardwareLimitation(Abstract):
        pass


    class TabletDevice(NonAgentivePhysicalObject):
        pass


    class VideoGameEdition(VideoGame):
        pass


    class ExtendedEdition(VideoGameEdition):
        pass


    class DeveloperCommentary(GameContent):
        pass


    class BugFixCollection(GameContent):
        pass


    class setIn(ObjectProperty):
        domain = [VideoGame]
        range = [FictionalUniverse]


    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [GameStudio]


    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [GameStudio]


    class previouslyDeveloped(ObjectProperty):
        domain = [GameStudio]
        range = [VideoGame]


    class includesContent(ObjectProperty):
        domain = [VideoGame]
        range = [GameContent]


    class shippedWith(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [LevelEditor]


    class allowsCreationOf(ObjectProperty):
        domain = [LevelEditor]
        range = [PlayerCreatedShadowrunCampaign]


    class allowsSharingOf(ObjectProperty):
        domain = [LevelEditor]
        range = [PlayerCreatedShadowrunCampaign]


    class launchedBy(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [GameStudio]


    class hostedOn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [CrowdfundingPlatform]


    class targetsGame(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [VideoGame]


    class fundsAdditionOf(ObjectProperty):
        domain = [KickstarterCampaign]
        range = [FeatureContentSet]


    class intendedForGame(ObjectProperty, FunctionalProperty):
        domain = [FeatureContentSet]
        range = [VideoGame]


    class hasFundingGoal(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [MonetaryAmount]


    class goalReachedWithin(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [DurationDescription]


    class endedIn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [TimeInterval]


    class launchedIn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [TimeInterval]


    class receivedTotalFunding(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [MonetaryAmount]


    class developedWith(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [GameEngine]


    class improvesOn(ObjectProperty, FunctionalProperty):
        domain = [ImprovedGameEngine]
        range = [GameEngine]


    class usedWith(ObjectProperty):
        domain = [GameEngine]
        range = [VideoGame]


    class developedForPlatform(ObjectProperty):
        domain = [VideoGame]
        range = [OperatingSystem]


    class avoidedHardwareLimitation(ObjectProperty):
        domain = [GameStudio]
        range = [HardwareLimitation]


    class avoidsHardwareLimitation(ObjectProperty):
        domain = [VideoGame]
        range = [HardwareLimitation]


    class ofDevice(ObjectProperty, FunctionalProperty):
        domain = [HardwareLimitation]
        range = [TabletDevice]


    class releasedWorldwideIn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimeInterval]


    class hasEdition(ObjectProperty):
        domain = [VideoGame]
        range = [VideoGameEdition]


    class editionOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGameEdition]
        range = [VideoGame]


    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [VideoGameEdition]
        range = [TimeInterval]


    class freeForOwnersOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGameEdition]
        range = [VideoGame]


    LevelEditor.is_a.append(allowsCreationOf.some(PlayerCreatedShadowrunCampaign))
    LevelEditor.is_a.append(allowsSharingOf.some(PlayerCreatedShadowrunCampaign))
    KickstarterCampaign.is_a.append(launchedBy.some(GameStudio))
    KickstarterCampaign.is_a.append(hasFundingGoal.some(MonetaryAmount))
    KickstarterCampaign.is_a.append(receivedTotalFunding.some(MonetaryAmount))
    ImprovedGameEngine.is_a.append(improvesOn.some(GameEngine))
    ExtendedEdition.is_a.append(editionOf.some(VideoGame))
    ExtendedEdition.is_a.append(includesContent.some(GameCampaign))
    ExtendedEdition.is_a.append(includesContent.some(DeveloperCommentary))
    ExtendedEdition.is_a.append(includesContent.some(BugFixCollection))

    shadowrun_hong_kong = TurnBasedTacticalRolePlayingVideoGame("ShadowrunHongKongGame")
    shadowrun_hong_kong.label = "Shadowrun : Hong Kong"

    shadowrun_universe = FictionalUniverse("ShadowrunUniverseSetting")
    shadowrun_universe.label = "Shadowrun universe"

    harebrained_schemes = GameStudio("HarebrainedSchemesStudio")
    harebrained_schemes.label = "Harebrained Schemes"

    shadowrun_returns = StandaloneVideoGame("ShadowrunReturnsGame")
    shadowrun_returns.label = "Shadowrun Returns"

    dragonfall = VideoGameExpansion("DragonfallExpansion")
    dragonfall.label = "Dragonfall"

    single_player_campaign = SinglePlayerCampaign("ShadowrunHongKongSinglePlayerCampaign")
    single_player_campaign.label = "a new single - player campaign"

    level_editor = LevelEditor("ShadowrunHongKongLevelEditor")
    level_editor.label = "a level editor"

    player_created_shadowrun_campaigns = PlayerCreatedShadowrunCampaign("PlayerCreatedShadowrunCampaigns")
    player_created_shadowrun_campaigns.label = "their own Shadowrun campaigns"

    kickstarter = CrowdfundingPlatform("KickstarterPlatform")
    kickstarter.label = "Kickstarter"

    kickstarter_campaign = KickstarterCampaign("ShadowrunHongKongKickstarterCampaign")
    kickstarter_campaign.label = "a Kickstarter campaign"

    january_2015 = TimeInterval("January2015Interval")
    january_2015.label = "January 2015"

    additional_features_and_content = FeatureContentSet("AdditionalFeaturesAndContentSet")
    additional_features_and_content.label = "additional features and content"

    initial_funding_goal = MonetaryAmount("USD100000Amount")
    initial_funding_goal.label = "US$ 100,000"

    few_hours = DurationDescription("FewHoursDuration")
    few_hours.label = "a few hours"

    following_month = TimeInterval("FollowingMonthInterval")
    following_month.label = "the following month"

    total_funding = MonetaryAmount("USD1200000Amount")
    total_funding.label = "$ 1.2 million"

    previous_engine = GameEngine("ShadowrunReturnsDragonfallEngine")
    previous_engine.label = "the engine used with Shadowrun Returns and Dragonfall"

    improved_engine = ImprovedGameEngine("ImprovedShadowrunEngine")
    improved_engine.label = "an improved version of the engine used with Shadowrun Returns and Dragonfall"

    microsoft_windows = OperatingSystem("MicrosoftWindowsPlatform")
    microsoft_windows.label = "Microsoft Windows"

    os_x = OperatingSystem("OSXPlatform")
    os_x.label = "OS X"

    linux = OperatingSystem("LinuxPlatform")
    linux.label = "Linux"

    hardware_limitations = HardwareLimitation("TabletHardwareLimitations")
    hardware_limitations.label = "hardware limitations"

    tablets = TabletDevice("TabletDevices")
    tablets.label = "tablets"

    august_2015 = TimeInterval("August2015Interval")
    august_2015.label = "August 2015"

    extended_edition = ExtendedEdition("ShadowrunHongKongExtendedEdition")
    extended_edition.label = "an extended edition"

    new_campaign = GameCampaign("ShadowrunHongKongExtendedEditionCampaign")
    new_campaign.label = "a new campaign"

    developer_commentary = DeveloperCommentary("ShadowrunHongKongDeveloperCommentary")
    developer_commentary.label = "a developer commentary"

    bug_fixes = BugFixCollection("ShadowrunHongKongBugFixes")
    bug_fixes.label = "bug fixes for the original game"

    february_2016 = TimeInterval("February2016Interval")
    february_2016.label = "February 2016"

    shadowrun_hong_kong.setIn.append(shadowrun_universe)
    shadowrun_hong_kong.developedBy.append(harebrained_schemes)
    shadowrun_hong_kong.publishedBy.append(harebrained_schemes)
    shadowrun_hong_kong.includesContent.append(single_player_campaign)
    shadowrun_hong_kong.shippedWith = level_editor
    shadowrun_hong_kong.developedWith = improved_engine
    shadowrun_hong_kong.developedForPlatform.append(microsoft_windows)
    shadowrun_hong_kong.developedForPlatform.append(os_x)
    shadowrun_hong_kong.developedForPlatform.append(linux)
    shadowrun_hong_kong.avoidsHardwareLimitation.append(hardware_limitations)
    shadowrun_hong_kong.releasedWorldwideIn = august_2015
    shadowrun_hong_kong.hasEdition.append(extended_edition)

    harebrained_schemes.previouslyDeveloped.append(shadowrun_returns)
    harebrained_schemes.previouslyDeveloped.append(dragonfall)
    harebrained_schemes.avoidedHardwareLimitation.append(hardware_limitations)

    level_editor.allowsCreationOf.append(player_created_shadowrun_campaigns)
    level_editor.allowsSharingOf.append(player_created_shadowrun_campaigns)

    kickstarter_campaign.launchedBy = harebrained_schemes
    kickstarter_campaign.hostedOn = kickstarter
    kickstarter_campaign.targetsGame = shadowrun_hong_kong
    kickstarter_campaign.fundsAdditionOf.append(additional_features_and_content)
    kickstarter_campaign.hasFundingGoal = initial_funding_goal
    kickstarter_campaign.goalReachedWithin = few_hours
    kickstarter_campaign.launchedIn = january_2015
    kickstarter_campaign.endedIn = following_month
    kickstarter_campaign.receivedTotalFunding = total_funding

    additional_features_and_content.intendedForGame = shadowrun_hong_kong

    previous_engine.usedWith.append(shadowrun_returns)
    previous_engine.usedWith.append(dragonfall)
    improved_engine.improvesOn = previous_engine

    hardware_limitations.ofDevice = tablets

    extended_edition.editionOf = shadowrun_hong_kong
    extended_edition.includesContent.append(new_campaign)
    extended_edition.includesContent.append(developer_commentary)
    extended_edition.includesContent.append(bug_fixes)
    extended_edition.releasedIn = february_2016
    extended_edition.freeForOwnersOf = shadowrun_hong_kong


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
