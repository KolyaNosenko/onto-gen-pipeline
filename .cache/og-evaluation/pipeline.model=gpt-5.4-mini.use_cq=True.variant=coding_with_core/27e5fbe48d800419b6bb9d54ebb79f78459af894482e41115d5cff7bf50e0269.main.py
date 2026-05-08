"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

Who was Joos van Cleve also known as?

When was Joos van Cleve born and when did he die?

Where was Joos van Cleve active as a painter?

What artistic traditions or styles did Joos van Cleve combine in his painting?

What role did Joos van Cleve have in the Guild of Saint Luke of Antwerp?

For what types of works is Joos van Cleve mostly known?

What artistic qualities characterize Joos van Cleve’s work?

What painting technique did Joos van Cleve help introduce into his works?

What later painting style or period did the use of broad landscapes in backgrounds become associated with?

Who was Joos van Cleve’s child?

What was the occupation of Cornelis van Cleve?

When was Cornelis van Cleve born and when did he die?

What happened to Cornelis van Cleve during his residence in England?

What nickname was Cornelis van Cleve given because of his mental illness?
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
    AgentivePhysicalObject,
    PhysicalQuality,
    Process,
    SocialObject,
    SpaceRegion,
    State,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    class Painter(AgentivePhysicalObject):
        label = ["Painter"]

    class Guild(SocialObject):
        label = ["Guild"]

    class Place(SpaceRegion):
        label = ["Place"]

    class PaintingTechnique(Abstract):
        label = ["Painting Technique"]

    class PaintingStyle(Abstract):
        label = ["Painting Style"]

    class PaintingPeriod(Abstract):
        label = ["Painting Period"]

    class WorkType(Abstract):
        label = ["Work Type"]

    class ArtisticQuality(PhysicalQuality):
        label = ["Artistic Quality"]

    class Appellation(Abstract):
        label = ["Appellation"]

    class Nickname(Appellation):
        label = ["Nickname"]

    class Residence(Process):
        label = ["Residence"]

    class MentalIllness(State):
        label = ["Mental Illness"]

    class alsoKnownAs(ObjectProperty):
        domain = [Painter]
        range = [Appellation]

    class activeIn(ObjectProperty):
        domain = [Painter]
        range = [Place]

    class activeDuring(ObjectProperty):
        domain = [Painter]
        range = [TimeInterval]

    class locatedIn(ObjectProperty):
        domain = [SocialObject]
        range = [Place]

    class memberOf(ObjectProperty):
        domain = [Painter]
        range = [Guild]

    class coDeaconOf(ObjectProperty):
        domain = [Painter]
        range = [Guild]

    class combinedTechnique(ObjectProperty):
        domain = [Painter]
        range = [PaintingTechnique]

    class influencedByStyle(ObjectProperty):
        domain = [Painter]
        range = [PaintingStyle]

    class knownFor(ObjectProperty):
        domain = [Painter]
        range = [WorkType]

    class hasArtisticQuality(ObjectProperty):
        domain = [Painter]
        range = [ArtisticQuality]

    class helpedIntroduceTechnique(ObjectProperty):
        domain = [Painter]
        range = [PaintingTechnique]

    class associatedWithPeriod(ObjectProperty):
        domain = [PaintingTechnique]
        range = [PaintingPeriod]

    class fatherOf(ObjectProperty):
        domain = [Painter]
        range = [Painter]

    class residedIn(ObjectProperty):
        domain = [Residence]
        range = [Place]

    class hadResident(ObjectProperty):
        domain = [Residence]
        range = [Painter]

    class sufferedFrom(ObjectProperty):
        domain = [Painter]
        range = [MentalIllness]

    class occurredDuring(ObjectProperty):
        domain = [MentalIllness]
        range = [Residence]

    JoosVanCleve = Painter("JoosVanCleveInd")
    JoosVanCleve.label = "Joos van Cleve"

    JoosVanDerBeke = Appellation("JoosVanDerBekeInd")
    JoosVanDerBeke.label = "Joos van der Beke"
    JoosVanCleve.alsoKnownAs.append(JoosVanDerBeke)

    JoosLifespan = TimeInterval("JoosVanCleveLifespanInd")
    JoosLifespan.label = "c. 1485 – 1540/1541"
    JoosVanCleve.temporallyLocatedAt = JoosLifespan

    JoosActivePeriod = TimeInterval("JoosActivePeriodInd")
    JoosActivePeriod.label = "around 1511 to 1540"
    JoosVanCleve.activeDuring.append(JoosActivePeriod)

    Antwerp = Place("AntwerpInd")
    Antwerp.label = "Antwerp"
    JoosVanCleve.activeIn.append(Antwerp)

    GuildOfSaintLukeOfAntwerp = Guild("GuildOfSaintLukeOfAntwerpInd")
    GuildOfSaintLukeOfAntwerp.label = "Guild of Saint Luke of Antwerp"
    GuildOfSaintLukeOfAntwerp.locatedIn.append(Antwerp)
    JoosVanCleve.memberOf.append(GuildOfSaintLukeOfAntwerp)
    JoosVanCleve.coDeaconOf.append(GuildOfSaintLukeOfAntwerp)

    TraditionalNetherlandishPaintingTechniques = PaintingTechnique(
        "TraditionalNetherlandishPaintingTechniquesInd"
    )
    TraditionalNetherlandishPaintingTechniques.label = (
        "traditional Netherlandish painting techniques"
    )
    JoosVanCleve.combinedTechnique.append(TraditionalNetherlandishPaintingTechniques)

    ContemporaryRenaissancePaintingStyles = PaintingStyle(
        "ContemporaryRenaissancePaintingStylesInd"
    )
    ContemporaryRenaissancePaintingStyles.label = (
        "more contemporary Renaissance painting styles"
    )
    JoosVanCleve.influencedByStyle.append(ContemporaryRenaissancePaintingStyles)

    ReligiousWorks = WorkType("ReligiousWorksInd")
    ReligiousWorks.label = "religious works"

    PortraitsOfRoyalty = WorkType("PortraitsOfRoyaltyInd")
    PortraitsOfRoyalty.label = "portraits of royalty"

    JoosVanCleve.knownFor.append(ReligiousWorks)
    JoosVanCleve.knownFor.append(PortraitsOfRoyalty)

    SensitivityToColor = ArtisticQuality("SensitivityToColorInd")
    SensitivityToColor.label = "sensitivity to color"

    UniqueSolidarityOfFigures = ArtisticQuality("UniqueSolidarityOfFiguresInd")
    UniqueSolidarityOfFigures.label = "a unique solidarity of figures"

    JoosVanCleve.hasArtisticQuality.append(SensitivityToColor)
    JoosVanCleve.hasArtisticQuality.append(UniqueSolidarityOfFigures)

    BroadLandscapesBackground = PaintingTechnique("BroadLandscapesBackgroundInd")
    BroadLandscapesBackground.label = "broad landscapes in the backgrounds of his paintings"
    JoosVanCleve.helpedIntroduceTechnique.append(BroadLandscapesBackground)

    SixteenthCenturyNorthernRenaissancePaintings = PaintingPeriod(
        "SixteenthCenturyNorthernRenaissancePaintingsInd"
    )
    SixteenthCenturyNorthernRenaissancePaintings.label = (
        "sixteenth century northern Renaissance paintings"
    )
    BroadLandscapesBackground.associatedWithPeriod.append(
        SixteenthCenturyNorthernRenaissancePaintings
    )

    CornelisVanCleve = Painter("CornelisVanCleveInd")
    CornelisVanCleve.label = "Cornelis van Cleve"
    JoosVanCleve.fatherOf.append(CornelisVanCleve)

    CornelisLifespan = TimeInterval("CornelisVanCleveLifespanInd")
    CornelisLifespan.label = "1520 - 1567"
    CornelisVanCleve.temporallyLocatedAt = CornelisLifespan

    England = Place("EnglandInd")
    England.label = "England"

    CornelisResidenceInEngland = Residence("CornelisResidenceInEnglandInd")
    CornelisResidenceInEngland.label = "a residence in England"
    CornelisResidenceInEngland.residedIn.append(England)
    CornelisResidenceInEngland.hadResident.append(CornelisVanCleve)

    CornelisMentalIllness = MentalIllness("CornelisMentalIllnessInd")
    CornelisMentalIllness.label = "mentally ill"
    CornelisMentalIllness.occurredDuring.append(CornelisResidenceInEngland)
    CornelisVanCleve.sufferedFrom.append(CornelisMentalIllness)

    SotteCleef = Nickname("SotteCleefInd")
    SotteCleef.label = "Sotte Cleef"

    MadCleef = Nickname("MadCleefInd")
    MadCleef.label = "mad Cleef"

    CornelisVanCleve.alsoKnownAs.append(SotteCleef)
    CornelisVanCleve.alsoKnownAs.append(MadCleef)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
