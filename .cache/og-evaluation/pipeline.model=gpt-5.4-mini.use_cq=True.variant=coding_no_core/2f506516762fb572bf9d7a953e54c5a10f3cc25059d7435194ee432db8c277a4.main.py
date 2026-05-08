"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

What type of video game is Shadowrun: Hong Kong?

In what universe is Shadowrun: Hong Kong set?

Who developed and published Shadowrun: Hong Kong?

What previous Shadowrun games had Harebrained Schemes developed before Shadowrun: Hong Kong?

What new content did Shadowrun: Hong Kong include at release?

What tool was shipped with Shadowrun: Hong Kong for player-created campaigns?

What did the level editor in Shadowrun: Hong Kong allow players to do?

When did Harebrained Schemes launch the Kickstarter campaign for Shadowrun: Hong Kong?

Why did Harebrained Schemes launch the Kickstarter campaign for Shadowrun: Hong Kong?

What was the initial funding goal of the Kickstarter campaign for Shadowrun: Hong Kong?

How quickly was the initial funding goal of the Kickstarter campaign met?

How much money did the Kickstarter campaign for Shadowrun: Hong Kong raise in total?

What engine was Shadowrun: Hong Kong developed with?

For which operating systems was Shadowrun: Hong Kong developed?

Why did Harebrained Schemes limit Shadowrun: Hong Kong to Microsoft Windows, OS X, and Linux?

When was Shadowrun: Hong Kong released worldwide?

When was the extended edition of Shadowrun: Hong Kong released?

What features did the extended edition of Shadowrun: Hong Kong add?

Was the extended edition update free for owners of the original game?
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
    class VideoGame(Thing):
        pass

    class TurnBasedTacticalRolePlayingVideoGame(VideoGame):
        pass

    class Universe(Thing):
        pass

    class Organization(Thing):
        pass

    class GameDeveloper(Organization):
        pass

    class GamePublisher(Organization):
        pass

    class Player(Thing):
        pass

    class Campaign(Thing):
        pass

    class KickstarterCampaign(Campaign):
        pass

    class SinglePlayerCampaign(Campaign):
        pass

    class LevelEditor(Thing):
        pass

    class Feature(Thing):
        pass

    class Commentary(Feature):
        pass

    class BugFix(Feature):
        pass

    class Content(Thing):
        pass

    class Engine(Thing):
        pass

    class OperatingSystem(Thing):
        pass

    class HardwarePlatform(Thing):
        pass

    class Tablet(HardwarePlatform):
        pass

    class Edition(Thing):
        pass

    class Budget(Thing):
        pass

    class MonetaryAmount(Thing):
        pass

    class TimePoint(Thing):
        pass

    class Duration(Thing):
        pass

    class setInUniverse(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Universe]

    class developedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Organization]

    class publishedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Organization]

    class previouslyDeveloped(ObjectProperty):
        domain = [Organization]
        range = [VideoGame]

    class includes(ObjectProperty):
        domain = [VideoGame]
        range = [Thing]

    class shippedWith(ObjectProperty):
        domain = [VideoGame]
        range = [Thing]

    class allowsCreationOf(ObjectProperty):
        domain = [LevelEditor]
        range = [Campaign]

    class allowsSharingWith(ObjectProperty):
        domain = [LevelEditor]
        range = [Player]

    class launchedBy(ObjectProperty, FunctionalProperty):
        domain = [Campaign]
        range = [Organization]

    class launchedIn(ObjectProperty, FunctionalProperty):
        domain = [Campaign]
        range = [TimePoint]

    class funds(ObjectProperty):
        domain = [Campaign]
        range = [Thing]

    class hasFundingGoal(ObjectProperty, FunctionalProperty):
        domain = [Campaign]
        range = [MonetaryAmount]

    class metInDuration(ObjectProperty, FunctionalProperty):
        domain = [Campaign]
        range = [Duration]

    class raisedAmount(ObjectProperty, FunctionalProperty):
        domain = [Campaign]
        range = [MonetaryAmount]

    class developedWithEngine(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Engine]

    class usedFor(ObjectProperty):
        domain = [Engine]
        range = [VideoGame]

    class limitedToOperatingSystem(ObjectProperty):
        domain = [VideoGame]
        range = [OperatingSystem]

    class avoidsHardwareLimitationsOf(ObjectProperty):
        domain = [VideoGame]
        range = [HardwarePlatform]

    class releasedWorldwideIn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimePoint]

    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [Edition]
        range = [TimePoint]

    class featuresAdded(ObjectProperty):
        domain = [Edition]
        range = [Feature]

    class freeForOwnersOf(ObjectProperty, FunctionalProperty):
        domain = [Edition]
        range = [VideoGame]

    class improvedVersionOf(ObjectProperty, FunctionalProperty):
        domain = [Engine]
        range = [Engine]

    class wantedToAddTo(ObjectProperty):
        domain = [Thing]
        range = [VideoGame]

    class notPossibleWithBudget(ObjectProperty):
        domain = [Thing]
        range = [Budget]

    ShadowrunHongKong = TurnBasedTacticalRolePlayingVideoGame("ShadowrunHongKong")
    ShadowrunHongKong.label = "Shadowrun : Hong Kong"

    ShadowrunUniverse = Universe("ShadowrunUniverse")
    ShadowrunUniverse.label = "Shadowrun universe"

    HarebrainedSchemes = GameDeveloper("HarebrainedSchemes")
    HarebrainedSchemes.label = "Harebrained Schemes"
    HarebrainedSchemes.is_a.append(GamePublisher)

    ShadowrunReturns = TurnBasedTacticalRolePlayingVideoGame("ShadowrunReturns")
    ShadowrunReturns.label = "Shadowrun Returns"

    Dragonfall = TurnBasedTacticalRolePlayingVideoGame("Dragonfall")
    Dragonfall.label = "Dragonfall"

    NewSinglePlayerCampaign = SinglePlayerCampaign("NewSinglePlayerCampaign")
    NewSinglePlayerCampaign.label = "new single-player campaign"

    ShadowrunHongKongLevelEditor = LevelEditor("ShadowrunHongKongLevelEditor")
    ShadowrunHongKongLevelEditor.label = "level editor"

    PlayerCreatedShadowrunCampaigns = Campaign("PlayerCreatedShadowrunCampaigns")
    PlayerCreatedShadowrunCampaigns.label = "their own Shadowrun campaigns"

    OtherPlayers = Player("OtherPlayers")
    OtherPlayers.label = "other players"

    January2015 = TimePoint("January2015")
    January2015.label = "January 2015"

    KickstarterCampaignHK = KickstarterCampaign("KickstarterCampaignHK")
    KickstarterCampaignHK.label = "Kickstarter campaign"

    AdditionalFeatures = Feature("AdditionalFeatures")
    AdditionalFeatures.label = "additional features"

    AdditionalContent = Content("AdditionalContent")
    AdditionalContent.label = "content"

    CurrentBudget = Budget("CurrentBudget")
    CurrentBudget.label = "current budget"

    US100000 = MonetaryAmount("US100000")
    US100000.label = "US$ 100,000"

    FewHours = Duration("FewHours")
    FewHours.label = "a few hours"

    Over1_2Million = MonetaryAmount("Over1_2Million")
    Over1_2Million.label = "over $ 1.2 million"

    OriginalShadowrunEngine = Engine("OriginalShadowrunEngine")
    OriginalShadowrunEngine.label = "the engine used with Shadowrun Returns and Dragonfall"

    ImprovedEngine = Engine("ImprovedEngine")
    ImprovedEngine.label = "improved version of the engine"
    ImprovedEngine.improvedVersionOf = OriginalShadowrunEngine

    MicrosoftWindows = OperatingSystem("MicrosoftWindows")
    MicrosoftWindows.label = "Microsoft Windows"

    OSX = OperatingSystem("OSX")
    OSX.label = "OS X"

    Linux = OperatingSystem("Linux")
    Linux.label = "Linux"

    Tablets = Tablet("Tablets")
    Tablets.label = "tablets"

    August2015 = TimePoint("August2015")
    August2015.label = "August 2015"

    ExtendedEdition = Edition("ShadowrunHongKongExtendedEdition")
    ExtendedEdition.label = "extended edition"

    February2016 = TimePoint("February2016")
    February2016.label = "February 2016"

    ExtendedEditionNewCampaign = Campaign("ExtendedEditionNewCampaign")
    ExtendedEditionNewCampaign.label = "new campaign"

    DeveloperCommentary = Commentary("DeveloperCommentary")
    DeveloperCommentary.label = "developer commentary"

    BugFixes = BugFix("BugFixes")
    BugFixes.label = "bug fixes"

    ShadowrunHongKong.setInUniverse = ShadowrunUniverse
    ShadowrunHongKong.developedBy = HarebrainedSchemes
    ShadowrunHongKong.publishedBy = HarebrainedSchemes
    HarebrainedSchemes.previouslyDeveloped = [ShadowrunReturns, Dragonfall]
    ShadowrunHongKong.includes = [NewSinglePlayerCampaign]
    ShadowrunHongKong.shippedWith = [ShadowrunHongKongLevelEditor]
    ShadowrunHongKong.developedWithEngine = ImprovedEngine
    OriginalShadowrunEngine.usedFor = [ShadowrunReturns, Dragonfall]
    ShadowrunHongKong.limitedToOperatingSystem = [MicrosoftWindows, OSX, Linux]
    ShadowrunHongKong.avoidsHardwareLimitationsOf = [Tablets]
    ShadowrunHongKong.releasedWorldwideIn = August2015

    ShadowrunHongKongLevelEditor.allowsCreationOf = [PlayerCreatedShadowrunCampaigns]
    ShadowrunHongKongLevelEditor.allowsSharingWith = [OtherPlayers]

    KickstarterCampaignHK.launchedBy = HarebrainedSchemes
    KickstarterCampaignHK.launchedIn = January2015
    KickstarterCampaignHK.hasFundingGoal = US100000
    KickstarterCampaignHK.metInDuration = FewHours
    KickstarterCampaignHK.raisedAmount = Over1_2Million
    KickstarterCampaignHK.funds = [AdditionalFeatures, AdditionalContent]
    AdditionalFeatures.wantedToAddTo = [ShadowrunHongKong]
    AdditionalContent.wantedToAddTo = [ShadowrunHongKong]
    AdditionalFeatures.notPossibleWithBudget = [CurrentBudget]
    AdditionalContent.notPossibleWithBudget = [CurrentBudget]

    ExtendedEdition.releasedIn = February2016
    ExtendedEdition.featuresAdded = [ExtendedEditionNewCampaign, DeveloperCommentary, BugFixes]
    ExtendedEdition.freeForOwnersOf = ShadowrunHongKong


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
