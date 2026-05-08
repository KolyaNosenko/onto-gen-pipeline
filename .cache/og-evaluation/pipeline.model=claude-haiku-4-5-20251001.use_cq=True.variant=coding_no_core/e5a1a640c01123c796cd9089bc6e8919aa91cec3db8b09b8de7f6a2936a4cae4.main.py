"""
=== TASK INPUT ===
Source text:
Shadowrun : Hong Kong is a turn - based tactical role - playing video game set in the Shadowrun universe . It was developed and published by Harebrained Schemes , who previously developed Shadowrun Returns and its standalone expansion , . It includes a new single - player campaign and also shipped with a level editor that lets players create their own Shadowrun campaigns and share them with other players . In January 2015 , Harebrained Schemes launched a Kickstarter campaign in order to fund additional features and content they wanted to add to the game , but determined would not have been possible with their current budget . The initial funding goal of US$ 100,000 was met in only a few hours . The campaign ended the following month , receiving over $ 1.2 million . The game was developed with an improved version of the engine used with Shadowrun Returns and Dragonfall . Harebrained Schemes decided to develop the game only for Microsoft Windows , OS X , and Linux , so that they did not have to factor in the hardware limitations of tablets , as they did with their previous Shadowrun games . The game was released worldwide in August 2015 . An extended edition , featuring a new campaign , a developer commentary , and bug fixes for the original game , was released in February 2016 . The update was released for free for everybody who owned the original game .

1. What is Shadowrun: Hong Kong and what type of game is it?
2. Who developed and published Shadowrun: Hong Kong?
3. What previous games did the developer of Shadowrun: Hong Kong create?
4. What features does Shadowrun: Hong Kong include?
5. When was the Kickstarter campaign for Shadowrun: Hong Kong launched?
6. What was the initial funding goal for the Shadowrun: Hong Kong Kickstarter campaign?
7. How much funding did the Shadowrun: Hong Kong Kickstarter campaign receive?
8. What game engine was used to develop Shadowrun: Hong Kong?
9. What platforms was Shadowrun: Hong Kong developed for?
10. Why did Harebrained Schemes choose to develop Shadowrun: Hong Kong only for specific platforms?
11. When was Shadowrun: Hong Kong released worldwide?
12. What is the extended edition of Shadowrun: Hong Kong and when was it released?
13. What features are included in the extended edition of Shadowrun: Hong Kong?
14. Who could access the extended edition update for free?
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
    # Domain entity classes
    class VideoGame(Thing):
        pass
    
    class Company(Thing):
        pass
    
    class Platform(Thing):
        pass
    
    class GameEngine(Thing):
        pass
    
    class KickstarterCampaign(Thing):
        pass
    
    class GameFeature(Thing):
        pass
    
    class Campaign(GameFeature):
        pass
    
    class LevelEditor(GameFeature):
        pass
    
    class GameEdition(Thing):
        pass
    
    # Object Properties
    class developedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Company]
    
    class publishedBy(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [Company]
    
    class hasFeature(ObjectProperty):
        domain = [VideoGame]
        range = [GameFeature]
    
    class usesGameEngine(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [GameEngine]
    
    class developedFor(ObjectProperty):
        domain = [VideoGame]
        range = [Platform]
    
    class hasExtendedEdition(ObjectProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [GameEdition]
    
    class fundingCampaignFor(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [VideoGame]
    
    class launchedBy(ObjectProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [Company]
    
    class previouslyDeveloped(ObjectProperty):
        domain = [Company]
        range = [VideoGame]
    
    # Data Properties
    class releaseDate(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class universeName(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class gameType(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class platformChoiceReason(DataProperty, FunctionalProperty):
        domain = [VideoGame]
        range = [str]
    
    class launchDate(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [str]
    
    class fundingGoal(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [str]
    
    class fundingReceived(DataProperty, FunctionalProperty):
        domain = [KickstarterCampaign]
        range = [str]
    
    class editionReleaseDate(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range = [str]
    
    class hasNewCampaign(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range = [bool]
    
    class hasDeveloperCommentary(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range = [bool]
    
    class hasBugFixes(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range = [bool]
    
    class isFreeUpdate(DataProperty, FunctionalProperty):
        domain = [GameEdition]
        range = [bool]
    
    # Concrete instances for named entities
    hbs = Company("HarebrainedSchemes")
    hbs.label = "Harebrained Schemes"
    
    shadowrun_hk = VideoGame("ShadowrunHongKong")
    shadowrun_hk.label = "Shadowrun : Hong Kong"
    shadowrun_hk.universeName = "Shadowrun"
    shadowrun_hk.releaseDate = "August 2015"
    shadowrun_hk.gameType = "turn-based tactical role-playing video game"
    shadowrun_hk.platformChoiceReason = "to avoid hardware limitations of tablets"
    shadowrun_hk.developedBy = hbs
    shadowrun_hk.publishedBy = hbs
    
    sr_returns = VideoGame("ShadowrunReturns")
    sr_returns.label = "Shadowrun Returns"
    
    dragonfall = VideoGame("Dragonfall")
    dragonfall.label = "Dragonfall"
    
    hbs.previouslyDeveloped = [sr_returns]
    
    engine = GameEngine("ShadowrunGameEngine")
    engine.label = "engine"
    shadowrun_hk.usesGameEngine = engine
    
    win = Platform("MicrosoftWindows")
    win.label = "Microsoft Windows"
    
    osx = Platform("OSX")
    osx.label = "OS X"
    
    linux = Platform("Linux")
    linux.label = "Linux"
    
    shadowrun_hk.developedFor = [win, osx, linux]
    
    campaign = Campaign("ShadowrunHongKongCampaign")
    campaign.label = "single-player campaign"
    
    editor = LevelEditor("ShadowrunHongKongLevelEditor")
    editor.label = "level editor"
    
    shadowrun_hk.hasFeature = [campaign, editor]
    
    edition = GameEdition("ShadowrunHongKongExtendedEdition")
    edition.label = "extended edition"
    edition.editionReleaseDate = "February 2016"
    edition.hasNewCampaign = True
    edition.hasDeveloperCommentary = True
    edition.hasBugFixes = True
    edition.isFreeUpdate = True
    
    shadowrun_hk.hasExtendedEdition = edition
    
    kickstarter = KickstarterCampaign("ShadowrunHongKongKickstarter")
    kickstarter.label = "Kickstarter campaign"
    kickstarter.launchDate = "January 2015"
    kickstarter.fundingGoal = "US$ 100,000"
    kickstarter.fundingReceived = "over $ 1.2 million"
    kickstarter.launchedBy = hbs
    kickstarter.fundingCampaignFor = shadowrun_hk


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
