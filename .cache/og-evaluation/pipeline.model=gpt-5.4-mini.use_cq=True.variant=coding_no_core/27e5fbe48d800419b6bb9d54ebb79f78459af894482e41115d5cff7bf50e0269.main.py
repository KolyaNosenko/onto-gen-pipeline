"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

1. Who was Joos van Cleve also known as?
2. When was Joos van Cleve born and when did he die?
3. What was Joos van Cleve’s profession?
4. Where was Joos van Cleve active?
5. During what period was Joos van Cleve active in Antwerp?
6. What artistic techniques or styles did Joos van Cleve combine in his paintings?
7. What guild was Joos van Cleve an active member of?
8. What role did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
9. What types of works is Joos van Cleve known mostly for?
10. What artistic qualities characterize Joos van Cleve’s work?
11. What innovation is Joos van Cleve known for introducing into his paintings?
12. What later painting tradition did Joos van Cleve’s use of broad landscapes influence?
13. Who was Joos van Cleve’s child?
14. What were the life dates of Cornelis van Cleve?
15. What profession did Cornelis van Cleve have?
16. Why was Cornelis van Cleve referred to as “Sotte Cleef”?
17. In which country did Cornelis van Cleve reside when he became mentally ill?
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
    class Person(Thing):
        pass

    class Painter(Person):
        pass

    class Place(Thing):
        pass

    class City(Place):
        pass

    class Country(Place):
        pass

    class Organization(Thing):
        pass

    class Guild(Organization):
        pass

    class Appellation(Thing):
        pass

    class Alias(Appellation):
        pass

    class Nickname(Appellation):
        pass

    class ArtisticConcept(Thing):
        pass

    class PaintingTechnique(ArtisticConcept):
        pass

    class PaintingStyle(ArtisticConcept):
        pass

    class ArtworkType(ArtisticConcept):
        pass

    class ArtisticQuality(ArtisticConcept):
        pass

    class Innovation(ArtisticConcept):
        pass

    class PaintingTradition(ArtisticConcept):
        pass

    class GuildRole(ArtisticConcept):
        pass

    class born(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class died(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class activeDuring(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class nicknameMeaning(DataProperty, FunctionalProperty):
        domain = [Nickname]
        range = [str]

    class nicknameReason(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class alsoKnownAs(ObjectProperty):
        domain = [Person]
        range = [Appellation]

    class activeIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class memberOf(ObjectProperty):
        domain = [Person]
        range = [Guild]

    class heldRole(ObjectProperty):
        domain = [Person]
        range = [GuildRole]

    class combinesTechnique(ObjectProperty):
        domain = [Person]
        range = [PaintingTechnique]

    class influencedByStyle(ObjectProperty):
        domain = [Person]
        range = [PaintingStyle]

    class knownFor(ObjectProperty):
        domain = [Person]
        range = [ArtworkType]

    class hasQuality(ObjectProperty):
        domain = [Person]
        range = [ArtisticQuality]

    class introducedInnovation(ObjectProperty):
        domain = [Person]
        range = [Innovation]

    class influencedTradition(ObjectProperty):
        domain = [Innovation]
        range = [PaintingTradition]

    class hasChild(ObjectProperty):
        domain = [Person]
        range = [Person]

    class residedIn(ObjectProperty):
        domain = [Person]
        range = [Country]

    JoosVanCleve = Painter("JoosVanCleve")
    JoosVanCleve.label = "Joos van Cleve"

    JoosVanDerBeke = Alias("JoosVanDerBeke")
    JoosVanDerBeke.label = "Joos van der Beke"

    Antwerp = City("Antwerp")
    Antwerp.label = "Antwerp"

    GuildOfSaintLukeOfAntwerp = Guild("GuildOfSaintLukeOfAntwerp")
    GuildOfSaintLukeOfAntwerp.label = "Guild of Saint Luke of Antwerp"

    CornelisVanCleve = Painter("CornelisVanCleve")
    CornelisVanCleve.label = "Cornelis van Cleve"

    England = Country("England")
    England.label = "England"

    SotteCleef = Nickname("SotteCleef")
    SotteCleef.label = "Sotte Cleef"
    SotteCleef.nicknameMeaning = "mad Cleef"

    TraditionalNetherlandishPaintingTechniques = PaintingTechnique("TraditionalNetherlandishPaintingTechniques")
    TraditionalNetherlandishPaintingTechniques.label = "traditional Netherlandish painting techniques"

    ContemporaryRenaissancePaintingStyles = PaintingStyle("ContemporaryRenaissancePaintingStyles")
    ContemporaryRenaissancePaintingStyles.label = "more contemporary Renaissance painting styles"

    ReligiousWorks = ArtworkType("ReligiousWorks")
    ReligiousWorks.label = "religious works"

    PortraitsOfRoyalty = ArtworkType("PortraitsOfRoyalty")
    PortraitsOfRoyalty.label = "portraits of royalty"

    SensitivityToColor = ArtisticQuality("SensitivityToColor")
    SensitivityToColor.label = "sensitivity to color"

    UniqueSolidarityOfFigures = ArtisticQuality("UniqueSolidarityOfFigures")
    UniqueSolidarityOfFigures.label = "unique solidarity of figures"

    BroadLandscapesInTheBackgroundsOfHisPaintings = Innovation("BroadLandscapesInTheBackgroundsOfHisPaintings")
    BroadLandscapesInTheBackgroundsOfHisPaintings.label = "broad landscapes in the backgrounds of his paintings"

    SixteenthCenturyNorthernRenaissancePaintings = PaintingTradition("SixteenthCenturyNorthernRenaissancePaintings")
    SixteenthCenturyNorthernRenaissancePaintings.label = "sixteenth century northern Renaissance paintings"

    CoDeaconRole = GuildRole("CoDeaconRole")
    CoDeaconRole.label = "co-deacon"

    JoosVanCleve.alsoKnownAs = [JoosVanDerBeke]
    JoosVanCleve.born = "c. 1485"
    JoosVanCleve.died = "1540/1541"
    JoosVanCleve.activeIn = [Antwerp]
    JoosVanCleve.activeDuring = "around 1511 to 1540"
    JoosVanCleve.combinesTechnique = [TraditionalNetherlandishPaintingTechniques]
    JoosVanCleve.influencedByStyle = [ContemporaryRenaissancePaintingStyles]
    JoosVanCleve.memberOf = [GuildOfSaintLukeOfAntwerp]
    JoosVanCleve.heldRole = [CoDeaconRole]
    JoosVanCleve.knownFor = [ReligiousWorks, PortraitsOfRoyalty]
    JoosVanCleve.hasQuality = [SensitivityToColor, UniqueSolidarityOfFigures]
    JoosVanCleve.introducedInnovation = [BroadLandscapesInTheBackgroundsOfHisPaintings]
    BroadLandscapesInTheBackgroundsOfHisPaintings.influencedTradition = [SixteenthCenturyNorthernRenaissancePaintings]
    JoosVanCleve.hasChild = [CornelisVanCleve]

    CornelisVanCleve.born = "1520"
    CornelisVanCleve.died = "1567"
    CornelisVanCleve.alsoKnownAs = [SotteCleef]
    CornelisVanCleve.nicknameReason = "became mentally ill during a residence in England"
    CornelisVanCleve.residedIn = [England]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
