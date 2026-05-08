"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

1. Who initiated the military reforms of the Florentine Republic?
2. During which republic and time period were the military reforms of the Florentine Republic initiated?
3. Under whose leadership did the short-lived Republic of Florence last from 1498 to 1512?
4. What political ideal motivated Machiavelli’s military reforms in Florence?
5. What kind of military establishment did Machiavelli seek to create for Florence?
6. Which ancient military force did Machiavelli use as a model for the Florentine army?
7. What specific military quality of the Roman legions did Machiavelli want the Florentine army to have?
8. What type of army did Machiavelli seek to establish to confront the Italian Condottieri?
9. Why did Machiavelli want to create a citizen-infantry for Florence?
10. In what year did Machiavelli institute reforms that created a citizen army?
11. How large was the citizen army created by Machiavelli’s reforms?
12. What system was established to keep the citizen army in a state of readiness?
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
    Accomplishment,
    Abstract,
    AbstractQuality,
    AgentivePhysicalObject,
    Event,
    SocialObject,
    State,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import (
    directQualityOf,
    partOf,
    temporallyLocatedAt,
)


with core:
    class PoliticalFigure(AgentivePhysicalObject):
        pass

    class Politician(PoliticalFigure):
        pass

    class PoliticalTheorist(PoliticalFigure):
        pass

    class Priest(PoliticalFigure):
        pass

    class City(SocialObject):
        pass

    class Republic(SocialObject):
        pass

    class MilitaryEstablishment(SocialObject):
        pass

    class MilitaryForce(MilitaryEstablishment):
        pass

    class Army(MilitaryForce):
        pass

    class CitizenArmy(Army):
        pass

    class CitizenInfantry(Army):
        pass

    class Legion(MilitaryForce):
        pass

    class Condottieri(MilitaryForce):
        pass

    class MilitaryReform(Accomplishment):
        pass

    class Invasion(Event):
        pass

    class PoliticalIdeal(AbstractQuality):
        pass

    class MilitaryDiscipline(AbstractQuality):
        pass

    class ReadinessSystem(SocialObject):
        pass

    class ReadinessState(State):
        pass

    class Quantity(Abstract):
        pass

    class CountQuantity(Quantity):
        pass

    class initiatedBy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [PoliticalFigure]

    class tookPlaceIn(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Republic]

    class ledBy(ObjectProperty, FunctionalProperty):
        domain = [Republic]
        range = [Priest]

    class motivatedBy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [PoliticalIdeal]

    class seeksToEstablish(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryEstablishment]

    class creates(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryEstablishment]

    class establishes(ObjectProperty):
        domain = [MilitaryReform]
        range = [ReadinessSystem]

    class modeledAfter(ObjectProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range = [MilitaryForce]

    class hasDesiredQuality(ObjectProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range = [MilitaryDiscipline]

    class intendedAgainst(ObjectProperty):
        domain = [CitizenInfantry]
        range = [MilitaryForce, Invasion]

    class belongsTo(ObjectProperty, FunctionalProperty):
        domain = [MilitaryForce]
        range = [City]

    class maintains(ObjectProperty, FunctionalProperty):
        domain = [ReadinessSystem]
        range = [CitizenArmy]

    class keepsInState(ObjectProperty, FunctionalProperty):
        domain = [ReadinessSystem]
        range = [ReadinessState]

    class quantityOf(ObjectProperty, FunctionalProperty):
        domain = [CountQuantity]
        range = [CitizenArmy]

    class quantityValue(DataProperty, FunctionalProperty):
        domain = [CountQuantity]
        range = [int]

    FlorentineRepublicPeriod = TimeInterval("FlorentineRepublicPeriod")
    FlorentineRepublicPeriod.label = "1498 to 1512"

    Year1498 = TimeInterval("Year1498")
    Year1498.label = "1498"
    Year1498.partOf.append(FlorentineRepublicPeriod)

    Year1512 = TimeInterval("Year1512")
    Year1512.label = "1512"
    Year1512.partOf.append(FlorentineRepublicPeriod)

    Year1506 = TimeInterval("Year1506")
    Year1506.label = "1506"
    Year1506.partOf.append(FlorentineRepublicPeriod)

    Florence = City("Florence")
    Florence.label = "Florence"

    AncientRome = City("AncientRome")
    AncientRome.label = "ancient Rome"

    FlorentineRepublic = Republic("FlorentineRepublic")
    FlorentineRepublic.label = ["Florentine Republic", "Republic of Florence"]
    FlorentineRepublic.temporallyLocatedAt = FlorentineRepublicPeriod

    NiccoloMachiavelli = PoliticalFigure("NiccoloMachiavelli")
    NiccoloMachiavelli.is_a.append(Politician)
    NiccoloMachiavelli.is_a.append(PoliticalTheorist)
    NiccoloMachiavelli.label = "Niccolò Machiavelli"

    GirolamoSavonarola = Priest("GirolamoSavonarola")
    GirolamoSavonarola.label = "Girolamo Savonarola"
    FlorentineRepublic.ledBy = GirolamoSavonarola

    RepublicanSpiritOfFlorence = PoliticalIdeal("RepublicanSpiritOfFlorence")
    RepublicanSpiritOfFlorence.label = "republican spirit"
    RepublicanSpiritOfFlorence.directQualityOf = Florence

    RomanLegions = Legion("RomanLegions")
    RomanLegions.label = "Roman legions"
    RomanLegions.belongsTo = AncientRome

    RomanLegionsDiscipline = MilitaryDiscipline("RomanLegionsDiscipline")
    RomanLegionsDiscipline.label = "discipline"
    RomanLegionsDiscipline.directQualityOf = RomanLegions

    ItalianCondottieri = Condottieri("ItalianCondottieri")
    ItalianCondottieri.label = "Italian Condottieri"

    ForeignInvasions = Invasion("ForeignInvasions")
    ForeignInvasions.label = "foreign invasions"

    CitizenInfantryOfFlorence = CitizenInfantry("CitizenInfantryOfFlorence")
    CitizenInfantryOfFlorence.label = "citizen - infantry"
    CitizenInfantryOfFlorence.intendedAgainst.append(ItalianCondottieri)
    CitizenInfantryOfFlorence.intendedAgainst.append(ForeignInvasions)

    CitizenArmyOfFlorence = CitizenArmy("CitizenArmyOfFlorence")
    CitizenArmyOfFlorence.label = ["military establishment", "citizen army"]
    CitizenArmyOfFlorence.modeledAfter = RomanLegions
    CitizenArmyOfFlorence.hasDesiredQuality = RomanLegionsDiscipline

    TwentyThousandMen = CountQuantity("TwentyThousandMen")
    TwentyThousandMen.label = "20,000 men"
    TwentyThousandMen.quantityValue = 20000
    TwentyThousandMen.quantityOf = CitizenArmyOfFlorence

    ReadinessStateOfCitizenArmy = ReadinessState("ReadinessStateOfCitizenArmy")
    ReadinessStateOfCitizenArmy.label = "state of readiness"

    ReadinessSystemOfCitizenArmy = ReadinessSystem("ReadinessSystemOfCitizenArmy")
    ReadinessSystemOfCitizenArmy.label = "readiness system"
    ReadinessSystemOfCitizenArmy.maintains = CitizenArmyOfFlorence
    ReadinessSystemOfCitizenArmy.keepsInState = ReadinessStateOfCitizenArmy

    MilitaryReformsOfFlorentineRepublic = MilitaryReform("MilitaryReformsOfFlorentineRepublic")
    MilitaryReformsOfFlorentineRepublic.label = "military reforms of the Florentine Republic"
    MilitaryReformsOfFlorentineRepublic.initiatedBy = NiccoloMachiavelli
    MilitaryReformsOfFlorentineRepublic.tookPlaceIn = FlorentineRepublic
    MilitaryReformsOfFlorentineRepublic.temporallyLocatedAt = Year1506
    MilitaryReformsOfFlorentineRepublic.motivatedBy = RepublicanSpiritOfFlorence
    MilitaryReformsOfFlorentineRepublic.seeksToEstablish.append(CitizenInfantryOfFlorence)
    MilitaryReformsOfFlorentineRepublic.seeksToEstablish.append(CitizenArmyOfFlorence)
    MilitaryReformsOfFlorentineRepublic.creates.append(CitizenArmyOfFlorence)
    MilitaryReformsOfFlorentineRepublic.establishes.append(ReadinessSystemOfCitizenArmy)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
