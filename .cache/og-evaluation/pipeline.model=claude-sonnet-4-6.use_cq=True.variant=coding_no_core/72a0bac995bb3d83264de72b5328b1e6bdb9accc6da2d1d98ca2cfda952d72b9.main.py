"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

1. Who was Joos van Cleve?
2. When was Joos van Cleve active as a painter?
3. Where was Joos van Cleve active as a painter?
4. What painting techniques did Joos van Cleve combine in his work?
5. What artistic styles influenced Joos van Cleve's paintings?
6. What guild was Joos van Cleve a member of?
7. What role did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
8. What types of works is Joos van Cleve known for?
9. What were the distinctive characteristics of Joos van Cleve's art?
10. What innovative technique did Joos van Cleve introduce in his paintings?
11. What influence did Joos van Cleve's technique have on later paintings?
12. Who was the father of Cornelis van Cleve?
13. When was Cornelis van Cleve born and when did he die?
14. What profession did Cornelis van Cleve pursue?
15. What happened to Cornelis van Cleve during his residence in England?
16. What was Cornelis van Cleve referred to as and why?
17. What was the relationship between Joos van Cleve and Cornelis van Cleve?
18. In which century did broad landscapes in painting backgrounds become a popular technique?
19. What was Joos van Cleve's approximate birth and death year?
20. What was the full name or alternative name used for Joos van Cleve?
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
    class Person(Thing): pass
    class Painter(Person): pass

    class Place(Thing): pass
    class City(Place): pass
    class Country(Place): pass

    class Guild(Thing): pass
    class GuildRole(Thing): pass

    class ArtisticWork(Thing): pass
    class Painting(ArtisticWork): pass
    class ReligiousWork(Painting): pass
    class Portrait(Painting): pass

    class PaintingTechnique(Thing): pass
    class PaintingStyle(Thing): pass
    class ArtisticMovement(Thing): pass

    # ── Object properties ─────────────────────────────────────────────────────
    class activeIn(ObjectProperty):
        domain = [Painter]
        range  = [Place]

    class memberOf(ObjectProperty):
        domain = [Person]
        range  = [Guild]

    class hasGuildRole(ObjectProperty):
        domain = [Person]
        range  = [GuildRole]

    class locatedIn(ObjectProperty):
        domain = [Guild]
        range  = [City]

    class combinesTechnique(ObjectProperty):
        domain = [Painter]
        range  = [PaintingTechnique]

    class influencedByStyle(ObjectProperty):
        domain = [Painter]
        range  = [PaintingStyle]

    class knownFor(ObjectProperty):
        domain = [Painter]
        range  = [ArtisticWork]

    class fatherOf(ObjectProperty):
        domain = [Person]
        range  = [Person]

    class introducedTechnique(ObjectProperty):
        domain = [Painter]
        range  = [PaintingTechnique]

    class becamePopularIn(ObjectProperty):
        domain = [PaintingTechnique]
        range  = [ArtisticMovement]

    class residedIn(ObjectProperty):
        domain = [Person]
        range  = [Place]

    # ── Data properties ───────────────────────────────────────────────────────
    class approximateBirthYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class approximateDeathYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class birthYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [int]

    class deathYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [int]

    class activeFromYear(DataProperty, FunctionalProperty):
        domain = [Painter]
        range  = [int]

    class activeToYear(DataProperty, FunctionalProperty):
        domain = [Painter]
        range  = [int]

    class alternativeName(DataProperty):
        domain = [Person]
        range  = [str]

    class nickname(DataProperty):
        domain = [Person]
        range  = [str]

    class hasArtisticCharacteristic(DataProperty):
        domain = [Painter]
        range  = [str]

    class becameMentallyIll(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [bool]

    # ── Individuals ───────────────────────────────────────────────────────────

    # Places
    antwerp = City("Antwerp")
    antwerp.label = "Antwerp"

    england = Country("England")
    england.label = "England"

    # Guild and role
    guildOfSaintLuke = Guild("GuildOfSaintLukeOfAntwerp")
    guildOfSaintLuke.label = "Guild of Saint Luke of Antwerp"
    guildOfSaintLuke.locatedIn = [antwerp]

    coDeacon = GuildRole("CoDeacon")
    coDeacon.label = "co-deacon"

    # Painting techniques
    netherlandishTechnique = PaintingTechnique("NetherlandishPaintingTechnique")
    netherlandishTechnique.label = "traditional Netherlandish painting techniques"

    broadLandscapesTechnique = PaintingTechnique("BroadLandscapesTechnique")
    broadLandscapesTechnique.label = "broad landscapes in the backgrounds"

    # Painting style and artistic movement
    renaissancePaintingStyle = PaintingStyle("RenaissancePaintingStyle")
    renaissancePaintingStyle.label = "Renaissance painting style"

    sixteenthCenturyNorthernRenaissance = ArtisticMovement("SixteenthCenturyNorthernRenaissance")
    sixteenthCenturyNorthernRenaissance.label = "sixteenth century northern Renaissance"

    broadLandscapesTechnique.becamePopularIn = [sixteenthCenturyNorthernRenaissance]

    # Work categories Joos is known for
    religiousWorks = ReligiousWork("ReligiousWorks")
    religiousWorks.label = "religious works"

    portraitsOfRoyalty = Portrait("PortraitsOfRoyalty")
    portraitsOfRoyalty.label = "portraits of royalty"

    # Painters
    joosVanCleve = Painter("JoosVanCleve")
    joosVanCleve.label = "Joos van Cleve"
    joosVanCleve.alternativeName = ["Joos van der Beke"]
    joosVanCleve.approximateBirthYear = "c. 1485"
    joosVanCleve.approximateDeathYear = "1540/1541"
    joosVanCleve.activeFromYear = 1511
    joosVanCleve.activeToYear = 1540
    joosVanCleve.activeIn = [antwerp]
    joosVanCleve.memberOf = [guildOfSaintLuke]
    joosVanCleve.hasGuildRole = [coDeacon]
    joosVanCleve.combinesTechnique = [netherlandishTechnique]
    joosVanCleve.influencedByStyle = [renaissancePaintingStyle]
    joosVanCleve.knownFor = [religiousWorks, portraitsOfRoyalty]
    joosVanCleve.introducedTechnique = [broadLandscapesTechnique]
    joosVanCleve.hasArtisticCharacteristic = ["sensitivity to color", "unique solidarity of figures"]

    cornelisVanCleve = Painter("CornelisVanCleve")
    cornelisVanCleve.label = "Cornelis van Cleve"
    cornelisVanCleve.birthYear = 1520
    cornelisVanCleve.deathYear = 1567
    cornelisVanCleve.nickname = ["Sotte Cleef"]
    cornelisVanCleve.becameMentallyIll = True
    cornelisVanCleve.residedIn = [england]

    joosVanCleve.fatherOf = [cornelisVanCleve]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
