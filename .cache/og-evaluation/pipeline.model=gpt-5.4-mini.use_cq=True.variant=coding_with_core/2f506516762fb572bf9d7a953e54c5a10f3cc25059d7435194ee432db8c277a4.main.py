"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. What type of video game is Shadowrun: Hong Kong?
2. In which universe is Shadowrun: Hong Kong set?
3. Who developed and published Shadowrun: Hong Kong?
4. What previous Shadowrun games had Harebrained Schemes developed before Shadowrun: Hong Kong?
5. What content does the game include besides the main campaign?
6. What does the included level editor allow players to do?
7. When did Harebrained Schemes launch the Kickstarter campaign for Shadowrun: Hong Kong?
8. Why did Harebrained Schemes launch the Kickstarter campaign for the game?
9. What was the initial funding goal of the Kickstarter campaign?
10. How quickly was the initial funding goal met?
11. How much money did the campaign receive in total?
12. What engine was Shadowrun: Hong Kong developed with?
13. For which operating systems was Shadowrun: Hong Kong developed?
14. Why did Harebrained Schemes decide not to develop the game for tablets?
15. When was Shadowrun: Hong Kong released worldwide?
16. When was the extended edition released?
17. What additional features does the extended edition include?
18. Who could obtain the free update to the extended edition?
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
    Event,
    NonAgentivePhysicalObject,
    NonPhysicalObject,
    Society,
    SocialAgent,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import constantConstituentOf


with core:
    class GameContent(NonPhysicalObject):
        pass


    class VideoGame(GameContent):
        pass


    class TurnBasedTacticalRolePlayingVideoGame(VideoGame):
        pass


    class GameCampaign(GameContent):
        pass


    class SinglePlayerCampaign(GameCampaign):
        pass


    class ShadowrunCampaign(GameCampaign):
        pass


    class LevelEditor(GameContent):
        pass


    class GameEdition(GameContent):
        pass


    class StandaloneExpansion(GameEdition):
        pass


    class ExtendedEdition(GameEdition):
        pass


    class DeveloperCommentary(GameContent):
        pass


    class BugFix(GameContent):
        pass


    class GameAdditions(GameContent):
        pass


    class GameEngine(NonPhysicalObject):
        pass


    class OperatingSystem(NonPhysicalObject):
        pass


    class Tablet(NonAgentivePhysicalObject):
        pass


    class Universe(Abstract):
        pass


    class Company(Society):
        pass


    class Player(SocialAgent):
        pass


    class KickstarterCampaign(Event):
        pass


    class MonetaryAmount(Abstract):
        pass


    class Budget(Abstract):
        pass


    class setInUniverse(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Universe]


    class developedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Company]


    class publishedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Company]


    class previouslyDeveloped(ObjectProperty):
        domain = [Company]
        range = [GameContent]


    class developedWithEngine(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [GameEngine]


    class usedWithGame(ObjectProperty):
        domain = [GameEngine]
        range = [VideoGame]


    class developedForOperatingSystem(ObjectProperty):
        domain = [VideoGame]
        range = [OperatingSystem]


    class avoidsHardwareLimitationsOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Tablet]


    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [GameContent]
        range = [TimeInterval]


    class launchedIn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [TimeInterval]


    class endedIn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [TimeInterval]


    class metIn(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [TimeInterval]


    class hasFundingGoal(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [MonetaryAmount]


    class receivedTotalFunding(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [MonetaryAmount]


    class raisesFundsFor(ObjectProperty):
        domain = [KickstarterCampaign]
        range = [GameAdditions]


    class wouldNotBePossibleWith(ObjectProperty, FunctionalProperty):
        domain = [GameAdditions]
        range = [Budget]


    class canObtainFreeUpdate(ObjectProperty, FunctionalProperty):
        domain = [ExtendedEdition]
        range = [Player]


    class allowsCreationOf(ObjectProperty):
        domain = [LevelEditor]
        range = [ShadowrunCampaign]


    class allowsSharingWith(ObjectProperty):
        domain = [LevelEditor]
        range = [Player]


    LevelEditor.is_a.append(allowsCreationOf.some(ShadowrunCampaign))
    LevelEditor.is_a.append(allowsSharingWith.some(Player))
    KickstarterCampaign.is_a.append(raisesFundsFor.some(GameAdditions))

    shadowrunHongKong = TurnBasedTacticalRolePlayingVideoGame("ShadowrunHongKong")
    shadowrunHongKong.label = "Shadowrun: Hong Kong"

    shadowrunUniverse = Universe("ShadowrunUniverse")
    shadowrunUniverse.label = "Shadowrun universe"

    harebrainedSchemes = Company("HarebrainedSchemes")
    harebrainedSchemes.label = "Harebrained Schemes"

    shadowrunReturns = VideoGame("ShadowrunReturns")
    shadowrunReturns.label = "Shadowrun Returns"

    dragonfall = StandaloneExpansion("Dragonfall")
    dragonfall.label = "Dragonfall"

    newSinglePlayerCampaign = SinglePlayerCampaign("NewSinglePlayerCampaign")
    newSinglePlayerCampaign.label = "a new single-player campaign"

    includedLevelEditor = LevelEditor("IncludedLevelEditor")
    includedLevelEditor.label = "a level editor"

    playerCreatedShadowrunCampaigns = ShadowrunCampaign("PlayerCreatedShadowrunCampaigns")
    playerCreatedShadowrunCampaigns.label = "their own Shadowrun campaigns"

    otherPlayers = Player("OtherPlayers")
    otherPlayers.label = "other players"

    kickstarterCampaign = KickstarterCampaign("ShadowrunHongKongKickstarterCampaign")
    kickstarterCampaign.label = "a Kickstarter campaign"

    additionalFeaturesAndContent = GameAdditions("AdditionalFeaturesAndContent")
    additionalFeaturesAndContent.label = "additional features and content"

    currentBudget = Budget("CurrentBudget")
    currentBudget.label = "their current budget"

    fundingGoal = MonetaryAmount("FundingGoal100000")
    fundingGoal.label = "US$ 100,000"

    onlyAFewHours = TimeInterval("OnlyAFewHours")
    onlyAFewHours.label = "only a few hours"

    totalFunding = MonetaryAmount("TotalFundingReceived")
    totalFunding.label = "over $ 1.2 million"

    improvedEngine = GameEngine("ImprovedEngineUsedWithShadowrunReturnsAndDragonfall")
    improvedEngine.label = "an improved version of the engine used with Shadowrun Returns and Dragonfall"

    microsoftWindows = OperatingSystem("MicrosoftWindows")
    microsoftWindows.label = "Microsoft Windows"

    osX = OperatingSystem("OSX")
    osX.label = "OS X"

    linux = OperatingSystem("Linux")
    linux.label = "Linux"

    tablets = Tablet("Tablets")
    tablets.label = "tablets"

    january2015 = TimeInterval("January2015")
    january2015.label = "January 2015"

    followingMonth = TimeInterval("FollowingMonth")
    followingMonth.label = "the following month"

    august2015 = TimeInterval("August2015")
    august2015.label = "August 2015"

    february2016 = TimeInterval("February2016")
    february2016.label = "February 2016"

    newCampaign = GameCampaign("NewCampaign")
    newCampaign.label = "a new campaign"

    developerCommentary = DeveloperCommentary("DeveloperCommentaryItem")
    developerCommentary.label = "a developer commentary"

    bugFixesForOriginalGame = BugFix("BugFixesForOriginalGame")
    bugFixesForOriginalGame.label = "bug fixes for the original game"

    shadowrunHongKongExtendedEdition = ExtendedEdition("ShadowrunHongKongExtendedEdition")
    shadowrunHongKongExtendedEdition.label = "an extended edition"

    originalGameOwners = Player("OriginalGameOwners")
    originalGameOwners.label = "everybody who owned the original game"

    shadowrunHongKong.setInUniverse = shadowrunUniverse
    shadowrunHongKong.developedBy = harebrainedSchemes
    shadowrunHongKong.publishedBy = harebrainedSchemes
    harebrainedSchemes.previouslyDeveloped.append(shadowrunReturns)
    harebrainedSchemes.previouslyDeveloped.append(dragonfall)
    shadowrunHongKong.developedWithEngine = improvedEngine
    improvedEngine.usedWithGame.append(shadowrunReturns)
    improvedEngine.usedWithGame.append(dragonfall)
    shadowrunHongKong.developedForOperatingSystem.append(microsoftWindows)
    shadowrunHongKong.developedForOperatingSystem.append(osX)
    shadowrunHongKong.developedForOperatingSystem.append(linux)
    shadowrunHongKong.avoidsHardwareLimitationsOf = tablets
    shadowrunHongKong.releasedIn = august2015
    newSinglePlayerCampaign.constantConstituentOf.append(shadowrunHongKong)
    includedLevelEditor.constantConstituentOf.append(shadowrunHongKong)
    includedLevelEditor.allowsCreationOf.append(playerCreatedShadowrunCampaigns)
    includedLevelEditor.allowsSharingWith.append(otherPlayers)
    kickstarterCampaign.launchedIn = january2015
    kickstarterCampaign.raisesFundsFor.append(additionalFeaturesAndContent)
    additionalFeaturesAndContent.wouldNotBePossibleWith = currentBudget
    kickstarterCampaign.hasFundingGoal = fundingGoal
    kickstarterCampaign.metIn = onlyAFewHours
    kickstarterCampaign.endedIn = followingMonth
    kickstarterCampaign.receivedTotalFunding = totalFunding
    shadowrunHongKongExtendedEdition.releasedIn = february2016
    newCampaign.constantConstituentOf.append(shadowrunHongKongExtendedEdition)
    developerCommentary.constantConstituentOf.append(shadowrunHongKongExtendedEdition)
    bugFixesForOriginalGame.constantConstituentOf.append(shadowrunHongKongExtendedEdition)
    shadowrunHongKongExtendedEdition.canObtainFreeUpdate = originalGameOwners


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
