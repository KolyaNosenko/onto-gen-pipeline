"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. What type of video game is Shadowrun: Hong Kong?
2. Who developed and published Shadowrun: Hong Kong?
3. What previous games did Harebrained Schemes develop before Shadowrun: Hong Kong?
4. What features does Shadowrun: Hong Kong include?
5. When did Harebrained Schemes launch the Kickstarter campaign for Shadowrun: Hong Kong?
6. What was the initial funding goal of the Kickstarter campaign?
7. How long did it take to meet the initial funding goal?
8. How much money did the Kickstarter campaign receive in total?
9. When did the Kickstarter campaign end?
10. What engine was used to develop Shadowrun: Hong Kong?
11. Which platforms was Shadowrun: Hong Kong developed for?
12. Why did Harebrained Schemes choose not to develop the game for tablets?
13. When was Shadowrun: Hong Kong released worldwide?
14. What does the extended edition of Shadowrun: Hong Kong include?
15. When was the extended edition of Shadowrun: Hong Kong released?
16. Who was eligible to receive the extended edition update for free?
17. What universe is Shadowrun: Hong Kong set in?
18. What is the relationship between Shadowrun: Hong Kong and Dragonfall?
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
    # ── Entity classes ────────────────────────────────────────────────────────

    class VideoGame(Thing): pass
    class TurnBasedTacticalRPG(VideoGame): pass
    class StandaloneExpansion(VideoGame): pass
    class GameEdition(Thing): pass

    class GameDeveloper(Thing): pass
    class GameUniverse(Thing): pass
    class SinglePlayerCampaign(Thing): pass
    class LevelEditor(Thing): pass
    class KickstarterCampaign(Thing): pass
    class GameEngine(Thing): pass
    class Platform(Thing): pass
    class MoneyAmount(Thing): pass

    # ── Object properties ─────────────────────────────────────────────────────

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [GameDeveloper]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range  = [GameDeveloper]

    class setInUniverse(ObjectProperty):
        domain = [VideoGame]
        range  = [GameUniverse]

    class isStandaloneExpansionOf(ObjectProperty):
        domain = [StandaloneExpansion]
        range  = [VideoGame]

    class includesCampaign(ObjectProperty):
        domain = [VideoGame]
        range  = [SinglePlayerCampaign]

    class hasLevelEditor(ObjectProperty):
        domain = [VideoGame]
        range  = [LevelEditor]

    class launchedBy(ObjectProperty):
        domain = [KickstarterCampaign]
        range  = [GameDeveloper]

    class fundsGame(ObjectProperty):
        domain = [KickstarterCampaign]
        range  = [VideoGame]

    class hasInitialFundingGoal(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range  = [MoneyAmount]

    class receivedTotalFunding(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range  = [MoneyAmount]

    class builtWithEngine(ObjectProperty):
        domain = [VideoGame]
        range  = [GameEngine]

    class availableOnPlatform(ObjectProperty):
        domain = [VideoGame]
        range  = [Platform]

    class hasEdition(ObjectProperty):
        domain = [VideoGame]
        range  = [GameEdition]

    class isEditionOf(ObjectProperty, FunctionalProperty):
        domain = [GameEdition]
        range  = [VideoGame]

    # ── Data properties ───────────────────────────────────────────────────────

    class releaseDate(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class gameGenre(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range  = [str]

    class kickstarterLaunchDate(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range  = [str]

    class kickstarterEndDate(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range  = [str]

    class goalMetIn(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range  = [str]

    class monetaryValue(DataProperty, FunctionalProperty):
        domain = [MoneyAmount]
        range  = [str]

    class editionReleaseDate(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range  = [str]

    class isFreeUpdate(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range  = [bool]

    # ── Named individuals ─────────────────────────────────────────────────────

    # Developer
    harebrained_schemes = GameDeveloper("HarebrainedSchemes")
    harebrained_schemes.label = "Harebrained Schemes"

    # Universe
    shadowrun_universe = GameUniverse("ShadowrunUniverse")
    shadowrun_universe.label = "Shadowrun universe"

    # Games
    shadowrun_hk = TurnBasedTacticalRPG("ShadowrunHongKong")
    shadowrun_hk.label = "Shadowrun : Hong Kong"
    shadowrun_hk.gameGenre = "turn-based tactical role-playing video game"

    shadowrun_returns = VideoGame("ShadowrunReturns")
    shadowrun_returns.label = "Shadowrun Returns"

    dragonfall = StandaloneExpansion("DragonfallGame")
    dragonfall.label = "Dragonfall"

    # Game engine (improved version used across all three games)
    hk_engine = GameEngine("HKGameEngine")
    hk_engine.label = "improved version of the engine"

    # In-game features
    hk_campaign = SinglePlayerCampaign("HKSinglePlayerCampaign")
    hk_campaign.label = "single-player campaign"

    hk_editor = LevelEditor("HKLevelEditor")
    hk_editor.label = "level editor"

    # Platforms
    windows = Platform("MicrosoftWindows")
    windows.label = "Microsoft Windows"

    osx = Platform("OSX")
    osx.label = "OS X"

    linux = Platform("LinuxPlatform")
    linux.label = "Linux"

    # Kickstarter campaign
    hk_kickstarter = KickstarterCampaign("HKKickstarterCampaign")
    hk_kickstarter.label = "Kickstarter campaign"

    # Money amounts
    initial_goal = MoneyAmount("InitialFundingGoal")
    initial_goal.label = "US$ 100,000"
    initial_goal.monetaryValue = "US$ 100,000"

    total_funding = MoneyAmount("TotalCampaignFunding")
    total_funding.label = "$ 1.2 million"
    total_funding.monetaryValue = "$ 1.2 million"

    # Extended edition
    hk_extended = GameEdition("HKExtendedEdition")
    hk_extended.label = "extended edition"

    # ── Property assertions ───────────────────────────────────────────────────

    # Shadowrun: Hong Kong
    shadowrun_hk.developedBy      = [harebrained_schemes]
    shadowrun_hk.publishedBy      = [harebrained_schemes]
    shadowrun_hk.setInUniverse    = [shadowrun_universe]
    shadowrun_hk.includesCampaign = [hk_campaign]
    shadowrun_hk.hasLevelEditor   = [hk_editor]
    shadowrun_hk.builtWithEngine  = [hk_engine]
    shadowrun_hk.availableOnPlatform = [windows, osx, linux]
    shadowrun_hk.hasEdition       = [hk_extended]
    shadowrun_hk.releaseDate      = "August 2015"

    # Shadowrun Returns
    shadowrun_returns.developedBy     = [harebrained_schemes]
    shadowrun_returns.publishedBy     = [harebrained_schemes]
    shadowrun_returns.builtWithEngine = [hk_engine]

    # Dragonfall (standalone expansion of Shadowrun Returns)
    dragonfall.developedBy            = [harebrained_schemes]
    dragonfall.publishedBy            = [harebrained_schemes]
    dragonfall.isStandaloneExpansionOf = [shadowrun_returns]
    dragonfall.builtWithEngine        = [hk_engine]

    # Kickstarter campaign
    hk_kickstarter.launchedBy            = [harebrained_schemes]
    hk_kickstarter.fundsGame             = [shadowrun_hk]
    hk_kickstarter.kickstarterLaunchDate = "January 2015"
    hk_kickstarter.kickstarterEndDate    = "February 2015"
    hk_kickstarter.goalMetIn             = "a few hours"
    hk_kickstarter.hasInitialFundingGoal = initial_goal
    hk_kickstarter.receivedTotalFunding  = total_funding

    # Extended edition
    hk_extended.isEditionOf       = shadowrun_hk
    hk_extended.editionReleaseDate = "February 2016"
    hk_extended.isFreeUpdate      = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
