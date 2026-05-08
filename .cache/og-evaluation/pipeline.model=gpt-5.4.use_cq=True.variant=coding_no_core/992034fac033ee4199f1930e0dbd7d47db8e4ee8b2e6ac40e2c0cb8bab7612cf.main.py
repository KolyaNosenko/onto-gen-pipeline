"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

What is the full name of Joos van Cleve?
What alternative names was Joos van Cleve known by?
When was Joos van Cleve born and when did he die?
In which place was Joos van Cleve active as a painter?
During what years was Joos van Cleve active in Antwerp?
What profession did Joos van Cleve have?
What painting techniques and artistic styles did Joos van Cleve combine in his work?
Of which guild was Joos van Cleve a member?
What role did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
For what types of artworks is Joos van Cleve mostly known?
What artistic qualities characterize the work of Joos van Cleve?
Did Joos van Cleve introduce broad landscapes in the backgrounds of his paintings?
What painting technique introduced by Joos van Cleve became popular in sixteenth-century northern Renaissance paintings?
Who was the father of Cornelis van Cleve?
Who was Cornelis van Cleve?
When was Cornelis van Cleve born and when did he die?
What profession did Cornelis van Cleve have?
What familial relationship existed between Joos van Cleve and Cornelis van Cleve?
Where did Cornelis van Cleve reside when he became mentally ill?
Why was Cornelis van Cleve referred to as "Sotte Cleef"?
What does the nickname "Sotte Cleef" mean?
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

    class GuildMember(Person):
        pass

    class GuildCoDeacon(GuildMember):
        pass

    class Name(Thing):
        pass

    class AlternativeName(Name):
        pass

    class Nickname(Name):
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

    class Artwork(Thing):
        pass

    class Painting(Artwork):
        pass

    class ReligiousWork(Painting):
        pass

    class Portrait(Painting):
        pass

    class Royalty(Person):
        pass

    class PortraitOfRoyalty(Portrait):
        pass

    class ArtisticApproach(Thing):
        pass

    class PaintingTechnique(ArtisticApproach):
        pass

    class PaintingStyle(ArtisticApproach):
        pass

    class PaintingTradition(Thing):
        pass

    class TimeReference(Thing):
        pass

    class alsoKnownAs(ObjectProperty):
        domain = [Person]
        range = [AlternativeName]

    class referredToAs(ObjectProperty):
        domain = [Person]
        range = [Nickname]

    class bornAt(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeReference]

    class diedAt(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeReference]

    class activeInPlace(ObjectProperty):
        domain = [Painter]
        range = [Place]

    class activeFrom(ObjectProperty, FunctionalProperty):
        domain = [Painter]
        range = [TimeReference]

    class activeTo(ObjectProperty, FunctionalProperty):
        domain = [Painter]
        range = [TimeReference]

    class combinesTechnique(ObjectProperty):
        domain = [Painter]
        range = [PaintingTechnique]

    class combinesStyle(ObjectProperty):
        domain = [Painter]
        range = [PaintingStyle]

    class memberOf(ObjectProperty):
        domain = [GuildMember]
        range = [Guild]

    class coDeaconOf(ObjectProperty):
        domain = [GuildCoDeacon]
        range = [Guild]

    class locatedIn(ObjectProperty):
        domain = [Organization]
        range = [Place]

    class creates(ObjectProperty):
        domain = [Painter]
        range = [Painting]

    class depicts(ObjectProperty):
        domain = [Portrait]
        range = [Person]

    class hasChild(ObjectProperty):
        domain = [Person]
        range = [Person]

    class hasFather(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Person]

    class residesIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class becameMentallyIllDuringResidenceIn(ObjectProperty):
        domain = [Person]
        range = [Place]

    class techniqueBecamePopularIn(ObjectProperty):
        domain = [Painter]
        range = [PaintingTradition]

    class isApproximate(DataProperty, FunctionalProperty):
        domain = [TimeReference]
        range = [bool]

    class knownForArtworkDescription(DataProperty):
        domain = [Painter]
        range = [str]

    class hasArtisticQualityDescription(DataProperty):
        domain = [Painter]
        range = [str]

    class introducedBroadLandscapeBackgrounds(DataProperty, FunctionalProperty):
        domain = [Painter]
        range = [bool]

    class introducedTechniqueDescription(DataProperty):
        domain = [Painter]
        range = [str]

    class mentalStateDescription(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [str]

    class nicknameReasonDescription(DataProperty, FunctionalProperty):
        domain = [Nickname]
        range = [str]

    class nicknameMeaning(DataProperty, FunctionalProperty):
        domain = [Nickname]
        range = [str]

    Painter.is_a.append(creates.some(Painting))
    GuildMember.is_a.append(memberOf.some(Guild))
    GuildCoDeacon.is_a.append(coDeaconOf.some(Guild))
    PortraitOfRoyalty.is_a.append(depicts.some(Royalty))

    joos_van_cleve = Painter("JoosVanClevePerson")
    joos_van_cleave_alias = AlternativeName("JoosVanDerBekeName")
    cornelis_van_cleve = Painter("CornelisVanClevePerson")
    sotte_cleef = Nickname("SotteCleefNickname")
    antwerp = City("AntwerpCity")
    england = Country("EnglandCountry")
    guild_of_saint_luke_of_antwerp = Guild("GuildOfSaintLukeOfAntwerp")
    traditional_netherlandish_painting_techniques = PaintingTechnique("TraditionalNetherlandishPaintingTechniques")
    more_contemporary_renaissance_painting_styles = PaintingStyle("MoreContemporaryRenaissancePaintingStyles")
    sixteenth_century_northern_renaissance_paintings = PaintingTradition("SixteenthCenturyNorthernRenaissancePaintings")
    circa_1485 = TimeReference("Circa1485")
    year_1540_or_1541 = TimeReference("Year1540Or1541")
    year_1511 = TimeReference("Year1511")
    year_1540 = TimeReference("Year1540")
    year_1520 = TimeReference("Year1520")
    year_1567 = TimeReference("Year1567")

    joos_van_cleve.label = "Joos van Cleve"
    joos_van_cleave_alias.label = "Joos van der Beke"
    cornelis_van_cleve.label = "Cornelis van Cleve"
    sotte_cleef.label = "' Sotte Cleef '"
    antwerp.label = "Antwerp"
    england.label = "England"
    guild_of_saint_luke_of_antwerp.label = "Guild of Saint Luke of Antwerp"
    traditional_netherlandish_painting_techniques.label = "traditional Netherlandish painting techniques"
    more_contemporary_renaissance_painting_styles.label = "more contemporary Renaissance painting styles"
    sixteenth_century_northern_renaissance_paintings.label = "sixteenth century northern Renaissance paintings"
    circa_1485.label = "c. 1485"
    year_1540_or_1541.label = "1540/1541"
    year_1511.label = "1511"
    year_1540.label = "1540"
    year_1520.label = "1520"
    year_1567.label = "1567"

    joos_van_cleve.alsoKnownAs = [joos_van_cleave_alias]
    joos_van_cleve.bornAt = circa_1485
    joos_van_cleve.diedAt = year_1540_or_1541
    joos_van_cleve.activeInPlace = [antwerp]
    joos_van_cleve.activeFrom = year_1511
    joos_van_cleve.activeTo = year_1540
    joos_van_cleve.combinesTechnique = [traditional_netherlandish_painting_techniques]
    joos_van_cleve.combinesStyle = [more_contemporary_renaissance_painting_styles]
    joos_van_cleve.is_a.append(GuildCoDeacon)
    joos_van_cleve.memberOf = [guild_of_saint_luke_of_antwerp]
    joos_van_cleve.coDeaconOf = [guild_of_saint_luke_of_antwerp]
    joos_van_cleve.knownForArtworkDescription = ["religious works", "portraits of royalty"]
    joos_van_cleve.hasArtisticQualityDescription = ["sensitivity to color", "a unique solidarity of figures"]
    joos_van_cleve.introducedBroadLandscapeBackgrounds = True
    joos_van_cleve.introducedTechniqueDescription = ["broad landscapes in the backgrounds of his paintings"]
    joos_van_cleve.techniqueBecamePopularIn = [sixteenth_century_northern_renaissance_paintings]
    joos_van_cleve.hasChild = [cornelis_van_cleve]

    guild_of_saint_luke_of_antwerp.locatedIn = [antwerp]

    cornelis_van_cleve.bornAt = year_1520
    cornelis_van_cleve.diedAt = year_1567
    cornelis_van_cleve.hasFather = joos_van_cleve
    cornelis_van_cleve.residesIn = [england]
    cornelis_van_cleve.becameMentallyIllDuringResidenceIn = [england]
    cornelis_van_cleve.mentalStateDescription = "mentally ill"
    cornelis_van_cleve.referredToAs = [sotte_cleef]

    sotte_cleef.nicknameReasonDescription = "Cornelis became mentally ill during a residence in England"
    sotte_cleef.nicknameMeaning = "mad Cleef"

    circa_1485.isApproximate = True


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
