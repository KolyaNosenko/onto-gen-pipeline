"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

Competency questions — natural-language queries the ontology should
support; your output must contain enough classes, properties, and
individuals to answer every one of them:
Who is Joos van Cleve?
What alternative names is Joos van Cleve known by?
When was Joos van Cleve born?
When did Joos van Cleve die?
In which city was Joos van Cleve active?
During which years was Joos van Cleve active in Antwerp?
What profession did Joos van Cleve have?
What painting traditions and styles did Joos van Cleve combine in his work?
Of which guild was Joos van Cleve a member?
What role did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
For what types of artworks is Joos van Cleve mostly known?
What artistic qualities characterize Joos van Cleve’s work?
Did Joos van Cleve’s art show sensitivity to color?
Did Joos van Cleve’s art show a unique solidarity of figures?
What compositional technique was Joos van Cleve among the first to introduce?
In what part of his paintings did Joos van Cleve introduce broad landscapes?
What later artistic trend did Joos van Cleve’s use of broad landscape backgrounds influence?
Who was the father of Cornelis van Cleve?
Who was Cornelis van Cleve?
When was Cornelis van Cleve born?
When did Cornelis van Cleve die?
Did Cornelis van Cleve also become a painter?
What familial relationship existed between Joos van Cleve and Cornelis van Cleve?
Where did Cornelis van Cleve reside when he became mentally ill?
Why was Cornelis van Cleve referred to as “Sotte Cleef”?
What does the nickname “Sotte Cleef” mean?
Which royal subjects are associated with Joos van Cleve’s portrait works?
Was Joos van Cleve active during the northern Renaissance?
How did Joos van Cleve contribute to sixteenth-century northern Renaissance painting techniques?
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
    AgentivePhysicalObject,
    NonAgentiveSocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class Person(AgentivePhysicalObject):
        pass


    class Painter(Person):
        pass


    class Place(SpaceRegion):
        pass


    class City(Place):
        pass


    class Country(Place):
        pass


    class Guild(Society):
        pass


    class GuildRole(NonAgentiveSocialObject):
        pass


    class PersonalName(NonAgentiveSocialObject):
        pass


    class AlternativeName(PersonalName):
        pass


    class Nickname(PersonalName):
        pass


    class ArtworkGenre(NonAgentiveSocialObject):
        pass


    class PaintingTechnique(NonAgentiveSocialObject):
        pass


    class PaintingStyle(NonAgentiveSocialObject):
        pass


    class ArtisticQuality(NonAgentiveSocialObject):
        pass


    class ProfessionalAttribute(NonAgentiveSocialObject):
        pass


    class CompositionalTechnique(NonAgentiveSocialObject):
        pass


    class PaintingPart(NonAgentiveSocialObject):
        pass


    class ArtisticTrend(NonAgentiveSocialObject):
        pass


    class MentalHealthCondition(NonAgentiveSocialObject):
        pass


    class ApproximateDate(TimeInterval):
        pass


    class DateRange(TimeInterval):
        pass


    class alsoKnownAs(ObjectProperty):
        domain = [Person]
        range = [PersonalName]


    class bornDuring(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]


    class diedDuring(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]


    class activeIn(ObjectProperty):
        domain = [Person]
        range = [Place]


    class activeDuring(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]


    class combinesTechnique(ObjectProperty):
        domain = [Painter]
        range = [PaintingTechnique]


    class influencedByStyle(ObjectProperty):
        domain = [Painter]
        range = [PaintingStyle]


    class memberOfGuild(ObjectProperty):
        domain = [Person]
        range = [Guild]


    class heldGuildRole(ObjectProperty):
        domain = [Person]
        range = [GuildRole]


    class roleInGuild(ObjectProperty):
        domain = [GuildRole]
        range = [Guild]


    class knownForArtworkGenre(ObjectProperty):
        domain = [Painter]
        range = [ArtworkGenre]


    class hasProfessionalAttribute(ObjectProperty):
        domain = [Painter]
        range = [ProfessionalAttribute]


    class characterizedBy(ObjectProperty):
        domain = [Painter]
        range = [ArtisticQuality]


    class amongFirstToIntroduce(ObjectProperty):
        domain = [Painter]
        range = [CompositionalTechnique]


    class usedInPaintingPart(ObjectProperty):
        domain = [CompositionalTechnique]
        range = [PaintingPart]


    class becamePopularTechniqueIn(ObjectProperty):
        domain = [CompositionalTechnique]
        range = [ArtisticTrend]


    class activeDuringTrend(ObjectProperty):
        domain = [Painter]
        range = [ArtisticTrend]


    class fatherOf(ObjectProperty):
        domain = [Person]
        range = [Person]


    class residedIn(ObjectProperty):
        domain = [Person]
        range = [Place]


    class hasMentalHealthCondition(ObjectProperty):
        domain = [Person]
        range = [MentalHealthCondition]


    class referredToAs(ObjectProperty):
        domain = [Person]
        range = [Nickname]


    class becameMentallyIllDuringResidenceIn(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Place]


    class reasonForNickname(ObjectProperty):
        domain = [Nickname]
        range = [MentalHealthCondition]


    class nicknameMeaning(DataProperty, FunctionalProperty):
        domain = [Nickname]
        range = [str]


    JoosVanCleve = Painter("JoosVanCleve_Individual")
    JoosVanCleve.label = "Joos van Cleve"

    JoosVanDerBeke = AlternativeName("JoosVanDerBeke_Name")
    JoosVanDerBeke.label = "Joos van der Beke"

    Circa1485 = ApproximateDate("Circa1485")
    Circa1485.label = "c. 1485"

    Death1540Or1541 = DateRange("Death1540Or1541")
    Death1540Or1541.label = "1540/1541"

    Antwerp = City("Antwerp_City")
    Antwerp.label = "Antwerp"

    Around1511To1540 = DateRange("Around1511To1540")
    Around1511To1540.label = "around 1511 to 1540"

    TraditionalNetherlandishPaintingTechniques = PaintingTechnique(
        "TraditionalNetherlandishPaintingTechniques"
    )
    TraditionalNetherlandishPaintingTechniques.label = (
        "traditional Netherlandish painting techniques"
    )

    MoreContemporaryRenaissancePaintingStyles = PaintingStyle(
        "MoreContemporaryRenaissancePaintingStyles"
    )
    MoreContemporaryRenaissancePaintingStyles.label = (
        "more contemporary Renaissance painting styles"
    )

    GuildOfSaintLukeOfAntwerp = Guild("GuildOfSaintLukeOfAntwerp")
    GuildOfSaintLukeOfAntwerp.label = "Guild of Saint Luke of Antwerp"

    CoDeacon = GuildRole("CoDeaconRole")
    CoDeacon.label = "co - deacon"

    ReligiousWorks = ArtworkGenre("ReligiousWorks")
    ReligiousWorks.label = "religious works"

    PortraitsOfRoyalty = ArtworkGenre("PortraitsOfRoyalty")
    PortraitsOfRoyalty.label = "portraits of royalty"

    SkilledTechnician = ProfessionalAttribute("SkilledTechnician")
    SkilledTechnician.label = "skilled technician"

    SensitivityToColor = ArtisticQuality("SensitivityToColor")
    SensitivityToColor.label = "sensitivity to color"

    UniqueSolidarityOfFigures = ArtisticQuality("UniqueSolidarityOfFigures")
    UniqueSolidarityOfFigures.label = "unique solidarity of figures"

    BroadLandscapes = CompositionalTechnique("BroadLandscapes")
    BroadLandscapes.label = "broad landscapes"

    BackgroundsOfHisPaintings = PaintingPart("BackgroundsOfHisPaintings")
    BackgroundsOfHisPaintings.label = "backgrounds of his paintings"

    SixteenthCenturyNorthernRenaissancePaintings = ArtisticTrend(
        "SixteenthCenturyNorthernRenaissancePaintings"
    )
    SixteenthCenturyNorthernRenaissancePaintings.label = (
        "sixteenth century northern Renaissance paintings"
    )

    CornelisVanCleve = Painter("CornelisVanCleve_Individual")
    CornelisVanCleve.label = "Cornelis van Cleve"

    Year1520 = ApproximateDate("Year1520")
    Year1520.label = "1520"

    Year1567 = ApproximateDate("Year1567")
    Year1567.label = "1567"

    England = Country("England_Country")
    England.label = "England"

    MentallyIll = MentalHealthCondition("MentallyIll")
    MentallyIll.label = "mentally ill"

    SotteCleef = Nickname("SotteCleef_Nickname")
    SotteCleef.label = "Sotte Cleef"

    JoosVanCleve.alsoKnownAs.append(JoosVanDerBeke)
    JoosVanCleve.bornDuring = Circa1485
    JoosVanCleve.diedDuring = Death1540Or1541
    JoosVanCleve.activeIn.append(Antwerp)
    JoosVanCleve.activeDuring = Around1511To1540
    JoosVanCleve.combinesTechnique.append(TraditionalNetherlandishPaintingTechniques)
    JoosVanCleve.influencedByStyle.append(MoreContemporaryRenaissancePaintingStyles)
    JoosVanCleve.memberOfGuild.append(GuildOfSaintLukeOfAntwerp)
    JoosVanCleve.heldGuildRole.append(CoDeacon)
    JoosVanCleve.knownForArtworkGenre.append(ReligiousWorks)
    JoosVanCleve.knownForArtworkGenre.append(PortraitsOfRoyalty)
    JoosVanCleve.hasProfessionalAttribute.append(SkilledTechnician)
    JoosVanCleve.characterizedBy.append(SensitivityToColor)
    JoosVanCleve.characterizedBy.append(UniqueSolidarityOfFigures)
    JoosVanCleve.amongFirstToIntroduce.append(BroadLandscapes)
    JoosVanCleve.activeDuringTrend.append(SixteenthCenturyNorthernRenaissancePaintings)
    JoosVanCleve.fatherOf.append(CornelisVanCleve)

    CoDeacon.roleInGuild.append(GuildOfSaintLukeOfAntwerp)

    BroadLandscapes.usedInPaintingPart.append(BackgroundsOfHisPaintings)
    BroadLandscapes.becamePopularTechniqueIn.append(
        SixteenthCenturyNorthernRenaissancePaintings
    )

    CornelisVanCleve.bornDuring = Year1520
    CornelisVanCleve.diedDuring = Year1567
    CornelisVanCleve.residedIn.append(England)
    CornelisVanCleve.hasMentalHealthCondition.append(MentallyIll)
    CornelisVanCleve.referredToAs.append(SotteCleef)
    CornelisVanCleve.becameMentallyIllDuringResidenceIn = England

    SotteCleef.nicknameMeaning = "mad Cleef"
    SotteCleef.reasonForNickname.append(MentallyIll)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
