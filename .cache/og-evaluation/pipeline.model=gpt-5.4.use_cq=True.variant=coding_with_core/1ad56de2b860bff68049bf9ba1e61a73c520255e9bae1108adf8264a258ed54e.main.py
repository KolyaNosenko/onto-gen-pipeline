"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

What military reforms were initiated by Niccolò Machiavelli during the Florentine Republic?
When were Machiavelli’s military reforms initiated?
During which period did the short-lived Republic of Florence last?
Who ruled the Republic of Florence during the period in which the reforms were initiated?
What political roles did Niccolò Machiavelli hold in Florence?
What ideological objective motivated Machiavelli’s military reforms?
What ancient military model did Machiavelli seek to emulate?
What characteristics of the Roman legions did Machiavelli want the new army to possess?
What type of army did Machiavelli seek to establish in Florence?
What was the intended military capability of the citizen-infantry established by Machiavelli?
Against whom was Machiavelli’s citizen army intended to fight?
What threat did the Italian Condottieri pose to the Italian peninsula?
What additional military threat, besides the Condottieri, motivated Machiavelli’s reforms?
In what year did Machiavelli institute the series of military reforms?
How many men were included in the citizen army created by Machiavelli’s reforms?
What system was established to keep the Florentine citizen army in a state of readiness?
What was the relationship between the republican spirit in Florence and Machiavelli’s military reforms?
How did Machiavelli’s proposed military establishment differ from reliance on Condottieri?
What was the purpose of creating a disciplined citizen army in Florence?
Which political entity was responsible for initiating these military reforms?
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
    AbstractQuality,
    Accomplishment,
    NonAgentiveSocialObject,
    Process,
    SocialAgent,
    Society,
    SpaceRegion,
    TimeInterval,
)
from og_sandbox_with_core.core.properties import directQualityOf, presentAt, temporallyLocatedAt


with core:
    class Person(SocialAgent):
        pass


    class Politician(Person):
        pass


    class FlorentinePolitician(Politician):
        pass


    class PoliticalTheorist(Person):
        pass


    class Priest(Person):
        pass


    class PoliticalEntity(Society):
        pass


    class Republic(PoliticalEntity):
        pass


    class HistoricalPolity(PoliticalEntity):
        pass


    class Place(SpaceRegion):
        pass


    class City(Place):
        pass


    class Peninsula(Place):
        pass


    class MilitaryOrganization(Society):
        pass


    class MilitaryForce(MilitaryOrganization):
        pass


    class CitizenArmy(MilitaryForce):
        pass


    class CitizenInfantry(CitizenArmy):
        pass


    class CondottieriForce(MilitaryForce):
        pass


    class MilitaryInstitution(NonAgentiveSocialObject):
        pass


    class MilitaryReadinessSystem(NonAgentiveSocialObject):
        pass


    class IdeologicalObjective(NonAgentiveSocialObject):
        pass


    class RepublicanSpirit(IdeologicalObjective):
        pass


    class MilitaryReform(Accomplishment):
        pass


    class ForeignInvasion(Process):
        pass


    class TroopStrength(AbstractQuality):
        pass


    class initiatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [Person]


    class responsiblePoliticalEntity(ObjectProperty):
        domain = [MilitaryReform]
        range = [Republic]


    class ruledBy(ObjectProperty):
        domain = [Republic]
        range = [Person]


    class associatedWithPlace(ObjectProperty):
        domain = [Person]
        range = [Place]


    class motivatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [IdeologicalObjective]


    class pervaded(ObjectProperty):
        domain = [IdeologicalObjective]
        range = [Place]


    class soughtToEstablish(ObjectProperty):
        domain = [Person]
        range = [MilitaryInstitution, MilitaryForce, MilitaryReadinessSystem]


    class similarToMilitaryOf(ObjectProperty):
        domain = [MilitaryInstitution]
        range = [HistoricalPolity]


    class modeledDisciplineOn(ObjectProperty):
        domain = [MilitaryForce]
        range = [MilitaryForce]


    class capableOfTakingFieldAgainst(ObjectProperty):
        domain = [MilitaryForce]
        range = [MilitaryForce]


    class terrorized(ObjectProperty):
        domain = [MilitaryForce]
        range = [Place]


    class promptedByThreat(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryForce, Process]


    class createdForce(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryForce]


    class establishedSystem(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryReadinessSystem]


    class keptInStateOfReadiness(ObjectProperty):
        domain = [MilitaryReadinessSystem]
        range = [MilitaryForce]


    class startsAt(ObjectProperty):
        domain = [TimeInterval]
        range = [TimeInterval]


    class endsAt(ObjectProperty):
        domain = [TimeInterval]
        range = [TimeInterval]


    class hasNumericValue(DataProperty, FunctionalProperty):
        domain = [TroopStrength]
        range = [int]


    MilitaryReform.is_a.append(initiatedBy.some(Person))
    MilitaryReform.is_a.append(responsiblePoliticalEntity.some(Republic))
    MilitaryReform.is_a.append(motivatedBy.some(IdeologicalObjective))
    MilitaryReform.is_a.append(createdForce.some(CitizenArmy))
    MilitaryReform.is_a.append(establishedSystem.some(MilitaryReadinessSystem))
    Republic.is_a.append(ruledBy.some(Person))
    MilitaryInstitution.is_a.append(similarToMilitaryOf.some(HistoricalPolity))
    CitizenInfantry.is_a.append(capableOfTakingFieldAgainst.some(CondottieriForce))
    MilitaryReadinessSystem.is_a.append(keptInStateOfReadiness.some(CitizenArmy))
    RepublicanSpirit.is_a.append(pervaded.some(Place))

    florentineMilitaryReforms = MilitaryReform("FlorentineRepublicMilitaryReforms")
    florentineMilitaryReforms.label = "The military reforms of the Florentine Republic"

    niccoloMachiavelli = FlorentinePolitician("NiccoloMachiavelli")
    niccoloMachiavelli.label = ["Niccolò Machiavelli", "Machiavelli"]
    niccoloMachiavelli.is_a.append(PoliticalTheorist)

    republicOfFlorence = Republic("RepublicOfFlorence")
    republicOfFlorence.label = [
        "the Florentine Republic",
        "the short - lived Republic of Florence",
        "Republic of Florence",
    ]

    girolamoSavonarola = Priest("GirolamoSavonarola")
    girolamoSavonarola.label = "Girolamo Savonarola"

    florence = City("Florence")
    florence.label = "Florence"

    ancientRome = HistoricalPolity("AncientRome")
    ancientRome.label = "ancient Rome"

    romanLegions = MilitaryForce("RomanLegions")
    romanLegions.label = "Roman legions"

    italianCondottieri = CondottieriForce("ItalianCondottieri")
    italianCondottieri.label = "Italian Condottieri"

    italianPeninsula = Peninsula("ItalianPeninsula")
    italianPeninsula.label = "Italian peninsula"

    year1498 = TimeInterval("Year1498")
    year1498.label = "1498"

    year1512 = TimeInterval("Year1512")
    year1512.label = "1512"

    year1506 = TimeInterval("Year1506")
    year1506.label = "1506"

    republicOfFlorencePeriod = TimeInterval("RepublicOfFlorencePeriod")
    republicOfFlorencePeriod.label = "1498 to 1512"

    republicanSpirit = RepublicanSpirit("RepublicanSpiritAtTheTime")
    republicanSpirit.label = "the republican spirit"

    militaryEstablishment = MilitaryInstitution("FlorentineMilitaryEstablishment")
    militaryEstablishment.label = "a military establishment that was similar to that of ancient Rome"

    citizenArmy = CitizenArmy("FlorentineCitizenArmy")
    citizenArmy.label = [
        "an army possessed with the discipline of the Roman legions",
        "a citizen - infantry",
        "a citizen army of 20,000 men",
        "this citizen army",
    ]
    citizenArmy.is_a.append(CitizenInfantry)

    readinessSystem = MilitaryReadinessSystem("CitizenArmyReadinessSystem")
    readinessSystem.label = "a system that would keep this citizen army in a state of readiness"

    chronicForeignInvasions = ForeignInvasion("ChronicForeignInvasions")
    chronicForeignInvasions.label = "the chronic foreign invasions"

    twentyThousandMen = TroopStrength("TwentyThousandMen")
    twentyThousandMen.label = "20,000 men"

    florentineMilitaryReforms.initiatedBy.append(niccoloMachiavelli)
    florentineMilitaryReforms.responsiblePoliticalEntity.append(republicOfFlorence)
    florentineMilitaryReforms.motivatedBy.append(republicanSpirit)
    florentineMilitaryReforms.promptedByThreat.append(italianCondottieri)
    florentineMilitaryReforms.promptedByThreat.append(chronicForeignInvasions)
    florentineMilitaryReforms.createdForce.append(citizenArmy)
    florentineMilitaryReforms.establishedSystem.append(readinessSystem)
    florentineMilitaryReforms.temporallyLocatedAt = year1506
    florentineMilitaryReforms.presentAt.append(republicOfFlorencePeriod)

    republicOfFlorence.ruledBy.append(girolamoSavonarola)
    republicOfFlorence.temporallyLocatedAt = republicOfFlorencePeriod

    republicOfFlorencePeriod.startsAt.append(year1498)
    republicOfFlorencePeriod.endsAt.append(year1512)

    niccoloMachiavelli.associatedWithPlace.append(florence)
    niccoloMachiavelli.soughtToEstablish.append(militaryEstablishment)
    niccoloMachiavelli.soughtToEstablish.append(citizenArmy)
    niccoloMachiavelli.soughtToEstablish.append(readinessSystem)

    republicanSpirit.pervaded.append(florence)
    republicanSpirit.presentAt.append(republicOfFlorencePeriod)

    militaryEstablishment.similarToMilitaryOf.append(ancientRome)

    citizenArmy.modeledDisciplineOn.append(romanLegions)
    citizenArmy.capableOfTakingFieldAgainst.append(italianCondottieri)

    italianCondottieri.terrorized.append(italianPeninsula)

    readinessSystem.keptInStateOfReadiness.append(citizenArmy)

    twentyThousandMen.directQualityOf = citizenArmy
    twentyThousandMen.hasNumericValue = 20000


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
