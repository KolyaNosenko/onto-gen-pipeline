"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. What is Shadowrun: Hong Kong?
2. In which fictional universe is Shadowrun: Hong Kong set?
3. What genre of video game is Shadowrun: Hong Kong?
4. Who developed Shadowrun: Hong Kong?
5. Who published Shadowrun: Hong Kong?
6. Which previous games had Harebrained Schemes developed before Shadowrun: Hong Kong?
7. Does Shadowrun: Hong Kong include a single-player campaign?
8. Does Shadowrun: Hong Kong include a level editor?
9. What can players create using the level editor in Shadowrun: Hong Kong?
10. Can players share their custom Shadowrun campaigns with other players?
11. When was the Kickstarter campaign for Shadowrun: Hong Kong launched?
12. Why did Harebrained Schemes launch a Kickstarter campaign for Shadowrun: Hong Kong?
13. What was the initial funding goal of the Shadowrun: Hong Kong Kickstarter campaign?
14. How quickly was the initial Kickstarter funding goal met?
15. When did the Kickstarter campaign for Shadowrun: Hong Kong end?
16. How much money was pledged by the end of the Kickstarter campaign?
17. Which game engine was used to develop Shadowrun: Hong Kong?
18. Was the engine for Shadowrun: Hong Kong an improved version of the one used in Shadowrun Returns and Dragonfall?
19. On which platforms was Shadowrun: Hong Kong developed to be released?
20. Why did Harebrained Schemes choose not to develop Shadowrun: Hong Kong for tablets?
21. When was Shadowrun: Hong Kong released worldwide?
22. Was an extended edition of Shadowrun: Hong Kong released?
23. When was the extended edition of Shadowrun: Hong Kong released?
24. What additional content was included in the extended edition of Shadowrun: Hong Kong?
25. Did the extended edition include a new campaign?
26. Did the extended edition include developer commentary?
27. Did the extended edition include bug fixes for the original game?
28. Was the extended edition update free for owners of the original game?
29. Who was eligible to receive the extended edition update for free?
30. What relationship does Shadowrun: Hong Kong have to Shadowrun Returns and Dragonfall?
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
    class CreativeWork(Thing):
        pass

    class VideoGame(CreativeWork):
        pass

    class TurnBasedTacticalRolePlayingVideoGame(VideoGame):
        pass

    class FictionalUniverse(Thing):
        pass

    class Organization(Thing):
        pass

    class Campaign(CreativeWork):
        pass

    class SinglePlayerCampaign(Campaign):
        pass

    class ShadowrunCampaign(Campaign):
        pass

    class SoftwareTool(Thing):
        pass

    class LevelEditor(SoftwareTool):
        pass

    class FundraisingCampaign(Thing):
        pass

    class KickstarterCampaign(FundraisingCampaign):
        pass

    class CrowdfundingPlatform(Thing):
        pass

    class FeatureSet(Thing):
        pass

    class MonetaryAmount(Thing):
        pass

    class Duration(Thing):
        pass

    class TimePoint(Thing):
        pass

    class GameEngine(SoftwareTool):
        pass

    class Platform(Thing):
        pass

    class OperatingSystem(Platform):
        pass

    class DeviceCategory(Thing):
        pass

    class Tablet(DeviceCategory):
        pass

    class Constraint(Thing):
        pass

    class HardwareLimitation(Constraint):
        pass

    class SoftwareEdition(CreativeWork):
        pass

    class ExtendedEdition(SoftwareEdition):
        pass

    class Commentary(CreativeWork):
        pass

    class DeveloperCommentary(Commentary):
        pass

    class BugFixCollection(CreativeWork):
        pass

    class PlayerGroup(Thing):
        pass

    class setIn(ObjectProperty, FunctionalProperty):
        domain = [CreativeWork]
        range = [FictionalUniverse]

    class developedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class publishedBy(ObjectProperty):
        domain = [VideoGame]
        range = [Organization]

    class previouslyDeveloped(ObjectProperty):
        domain = [Organization]
        range = [VideoGame]

    class standaloneExpansionOf(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [VideoGame]

    class includesCampaign(ObjectProperty):
        domain = [CreativeWork]
        range = [Campaign]

    class shippedWith(ObjectProperty):
        domain = [VideoGame]
        range = [SoftwareTool]

    class allowsCreationOf(ObjectProperty):
        domain = [LevelEditor]
        range = [Campaign]

    class allowsSharingWith(ObjectProperty):
        domain = [LevelEditor]
        range = [PlayerGroup]

    class launchedBy(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [Organization]

    class hostedOn(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [CrowdfundingPlatform]

    class launchedIn(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [TimePoint]

    class fundedFor(ObjectProperty):
        domain = [FundraisingCampaign]
        range = [FeatureSet]

    class intendedForGame(ObjectProperty, FunctionalProperty):
        domain = [FeatureSet]
        range = [VideoGame]

    class limitedBy(ObjectProperty, FunctionalProperty):
        domain = [FeatureSet]
        range = [MonetaryAmount]

    class hasInitialFundingGoal(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [MonetaryAmount]

    class metWithin(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [Duration]

    class endedIn(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [TimePoint]

    class raisedAmount(ObjectProperty, FunctionalProperty):
        domain = [FundraisingCampaign]
        range = [MonetaryAmount]

    class developedWith(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [GameEngine]

    class improvedVersionOf(ObjectProperty, FunctionalProperty):
        domain = [GameEngine]
        range = [GameEngine]

    class previouslyUsedFor(ObjectProperty):
        domain = [GameEngine]
        range = [VideoGame]

    class developedForPlatform(ObjectProperty):
        domain = [VideoGame]
        range = [Platform]

    class notDevelopedFor(ObjectProperty):
        domain = [VideoGame]
        range = [DeviceCategory]

    class avoidedBecauseOf(ObjectProperty):
        domain = [VideoGame]
        range = [Constraint]

    class appliesTo(ObjectProperty, FunctionalProperty):
        domain = [Constraint]
        range = [Thing]

    class releasedWorldwideIn(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [TimePoint]

    class hasEdition(ObjectProperty):
        domain = [VideoGame]
        range = [SoftwareEdition]

    class editionOf(ObjectProperty, FunctionalProperty):
        domain = [SoftwareEdition]
        range = [VideoGame]

    class releasedIn(ObjectProperty, FunctionalProperty):
        domain = [SoftwareEdition]
        range = [TimePoint]

    class includesContent(ObjectProperty):
        domain = [SoftwareEdition]
        range = [CreativeWork]

    class hasBugFixesFor(ObjectProperty):
        domain = [BugFixCollection]
        range = [VideoGame]

    class releasedForFreeFor(ObjectProperty):
        domain = [SoftwareEdition]
        range = [PlayerGroup]

    class ownsGame(ObjectProperty):
        domain = [PlayerGroup]
        range = [VideoGame]

    class partOf(ObjectProperty, TransitiveProperty):
        domain = [Thing]
        range = [Thing]

    TurnBasedTacticalRolePlayingVideoGame.is_a.append(setIn.some(FictionalUniverse))
    TurnBasedTacticalRolePlayingVideoGame.is_a.append(developedBy.some(Organization))
    TurnBasedTacticalRolePlayingVideoGame.is_a.append(publishedBy.some(Organization))
    LevelEditor.is_a.append(allowsCreationOf.some(ShadowrunCampaign))
    KickstarterCampaign.is_a.append(hostedOn.some(CrowdfundingPlatform))
    KickstarterCampaign.is_a.append(hasInitialFundingGoal.some(MonetaryAmount))
    ExtendedEdition.is_a.append(editionOf.some(VideoGame))
    ExtendedEdition.is_a.append(includesCampaign.some(Campaign))
    ExtendedEdition.is_a.append(includesContent.some(CreativeWork))

    ShadowrunHongKong = TurnBasedTacticalRolePlayingVideoGame("ShadowrunHongKongInstance")
    ShadowrunHongKong.label = "Shadowrun : Hong Kong"

    ShadowrunUniverse = FictionalUniverse("ShadowrunUniverseInstance")
    ShadowrunUniverse.label = "Shadowrun universe"

    HarebrainedSchemes = Organization("HarebrainedSchemesInstance")
    HarebrainedSchemes.label = "Harebrained Schemes"

    ShadowrunReturns = VideoGame("ShadowrunReturnsInstance")
    ShadowrunReturns.label = "Shadowrun Returns"

    Dragonfall = VideoGame("DragonfallInstance")
    Dragonfall.label = "Dragonfall"

    SinglePlayerCampaignMention = SinglePlayerCampaign("SinglePlayerCampaignMention")
    SinglePlayerCampaignMention.label = "a new single - player campaign"

    LevelEditorMention = LevelEditor("LevelEditorMention")
    LevelEditorMention.label = "a level editor"

    TheirOwnShadowrunCampaigns = ShadowrunCampaign("TheirOwnShadowrunCampaigns")
    TheirOwnShadowrunCampaigns.label = "their own Shadowrun campaigns"

    OtherPlayers = PlayerGroup("OtherPlayersGroup")
    OtherPlayers.label = "other players"

    Kickstarter = CrowdfundingPlatform("KickstarterPlatform")
    Kickstarter.label = "Kickstarter"

    KickstarterCampaignMention = KickstarterCampaign("KickstarterCampaignMention")
    KickstarterCampaignMention.label = "a Kickstarter campaign"

    AdditionalFeaturesAndContent = FeatureSet("AdditionalFeaturesAndContentSet")
    AdditionalFeaturesAndContent.label = "additional features and content"

    CurrentBudget = MonetaryAmount("CurrentBudgetAmount")
    CurrentBudget.label = "their current budget"

    Us100000 = MonetaryAmount("Us100000Amount")
    Us100000.label = "US$ 100,000"

    OnlyAFewHours = Duration("OnlyAFewHoursDuration")
    OnlyAFewHours.label = "only a few hours"

    January2015 = TimePoint("January2015TimePoint")
    January2015.label = "January 2015"

    FollowingMonth = TimePoint("FollowingMonthTimePoint")
    FollowingMonth.label = "the following month"

    Over12Million = MonetaryAmount("Over12MillionAmount")
    Over12Million.label = "over $ 1.2 million"

    PreviousEngine = GameEngine("PreviousEngineInstance")
    PreviousEngine.label = "the engine used with Shadowrun Returns and Dragonfall"

    ImprovedEngine = GameEngine("ImprovedEngineInstance")
    ImprovedEngine.label = "an improved version of the engine used with Shadowrun Returns and Dragonfall"

    MicrosoftWindows = OperatingSystem("MicrosoftWindowsPlatform")
    MicrosoftWindows.label = "Microsoft Windows"

    OSX = OperatingSystem("OSXPlatform")
    OSX.label = "OS X"

    Linux = OperatingSystem("LinuxPlatform")
    Linux.label = "Linux"

    Tablets = Tablet("TabletsDeviceCategory")
    Tablets.label = "tablets"

    HardwareLimitationsOfTablets = HardwareLimitation("HardwareLimitationsOfTabletsConstraint")
    HardwareLimitationsOfTablets.label = "the hardware limitations of tablets"

    August2015 = TimePoint("August2015TimePoint")
    August2015.label = "August 2015"

    ExtendedEditionMention = ExtendedEdition("ExtendedEditionMention")
    ExtendedEditionMention.label = "An extended edition"

    NewCampaign = Campaign("NewCampaignMention")
    NewCampaign.label = "a new campaign"

    DeveloperCommentaryMention = DeveloperCommentary("DeveloperCommentaryMention")
    DeveloperCommentaryMention.label = "a developer commentary"

    BugFixesForTheOriginalGame = BugFixCollection("BugFixesForTheOriginalGameMention")
    BugFixesForTheOriginalGame.label = "bug fixes for the original game"

    February2016 = TimePoint("February2016TimePoint")
    February2016.label = "February 2016"

    EverybodyWhoOwnedTheOriginalGame = PlayerGroup("EverybodyWhoOwnedTheOriginalGameGroup")
    EverybodyWhoOwnedTheOriginalGame.label = "everybody who owned the original game"

    ShadowrunHongKong.setIn = ShadowrunUniverse
    ShadowrunHongKong.developedBy = [HarebrainedSchemes]
    ShadowrunHongKong.publishedBy = [HarebrainedSchemes]
    ShadowrunHongKong.includesCampaign = [SinglePlayerCampaignMention]
    ShadowrunHongKong.shippedWith = [LevelEditorMention]
    ShadowrunHongKong.developedWith = ImprovedEngine
    ShadowrunHongKong.developedForPlatform = [MicrosoftWindows, OSX, Linux]
    ShadowrunHongKong.notDevelopedFor = [Tablets]
    ShadowrunHongKong.avoidedBecauseOf = [HardwareLimitationsOfTablets]
    ShadowrunHongKong.releasedWorldwideIn = August2015
    ShadowrunHongKong.hasEdition = [ExtendedEditionMention]

    HarebrainedSchemes.previouslyDeveloped = [ShadowrunReturns, Dragonfall]
    Dragonfall.standaloneExpansionOf = ShadowrunReturns

    SinglePlayerCampaignMention.partOf = [ShadowrunHongKong]

    LevelEditorMention.allowsCreationOf = [TheirOwnShadowrunCampaigns]
    LevelEditorMention.allowsSharingWith = [OtherPlayers]
    LevelEditorMention.partOf = [ShadowrunHongKong]

    KickstarterCampaignMention.launchedBy = HarebrainedSchemes
    KickstarterCampaignMention.hostedOn = Kickstarter
    KickstarterCampaignMention.launchedIn = January2015
    KickstarterCampaignMention.fundedFor = [AdditionalFeaturesAndContent]
    KickstarterCampaignMention.hasInitialFundingGoal = Us100000
    KickstarterCampaignMention.metWithin = OnlyAFewHours
    KickstarterCampaignMention.endedIn = FollowingMonth
    KickstarterCampaignMention.raisedAmount = Over12Million

    AdditionalFeaturesAndContent.intendedForGame = ShadowrunHongKong
    AdditionalFeaturesAndContent.limitedBy = CurrentBudget

    ImprovedEngine.improvedVersionOf = PreviousEngine
    PreviousEngine.previouslyUsedFor = [ShadowrunReturns, Dragonfall]

    HardwareLimitationsOfTablets.appliesTo = Tablets

    ExtendedEditionMention.editionOf = ShadowrunHongKong
    ExtendedEditionMention.releasedIn = February2016
    ExtendedEditionMention.includesCampaign = [NewCampaign]
    ExtendedEditionMention.includesContent = [DeveloperCommentaryMention, BugFixesForTheOriginalGame]
    ExtendedEditionMention.releasedForFreeFor = [EverybodyWhoOwnedTheOriginalGame]

    NewCampaign.partOf = [ExtendedEditionMention]
    DeveloperCommentaryMention.partOf = [ExtendedEditionMention]
    BugFixesForTheOriginalGame.partOf = [ExtendedEditionMention]
    BugFixesForTheOriginalGame.hasBugFixesFor = [ShadowrunHongKong]

    EverybodyWhoOwnedTheOriginalGame.ownsGame = [ShadowrunHongKong]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
