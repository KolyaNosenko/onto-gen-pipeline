"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

What military reforms were initiated by Niccolò Machiavelli in the Florentine Republic?
When were the military reforms of the Florentine Republic initiated?
Who initiated the military reforms of the Florentine Republic?
What political roles did Niccolò Machiavelli hold during the Florentine Republic?
During which period did the short-lived Republic of Florence last?
Under whose leadership did the Republic of Florence last from 1498 to 1512?
What republican ideals influenced Machiavelli’s military reforms?
What ancient military model did Machiavelli seek to emulate in Florence?
What characteristics of the Roman legions did Machiavelli seek to reproduce in the Florentine army?
What type of army did Machiavelli seek to establish in Florence?
What was the intended composition of Machiavelli’s citizen-infantry?
Against whom was the citizen-infantry intended to take the field?
What threat did the Italian Condottieri pose at the time of Machiavelli’s reforms?
What recurring external threat did Machiavelli’s military reforms aim to address?
What series of reforms did Machiavelli institute in 1506?
How many men were included in the citizen army created by Machiavelli’s reforms?
What system was established to keep the Florentine citizen army in a state of readiness?
What was the purpose of establishing a citizen army in Florence?
How were Machiavelli’s military reforms related to the republican spirit in Florence?
How did Machiavelli’s military reforms differ from reliance on Italian Condottieri?
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
    class PoliticalEntity(Thing):
        pass

    class Republic(PoliticalEntity):
        pass

    class HistoricalPolity(PoliticalEntity):
        pass

    class City(Thing):
        pass

    class GeographicRegion(Thing):
        pass

    class Person(Thing):
        pass

    class Politician(Person):
        pass

    class PoliticalTheorist(Person):
        pass

    class Priest(Person):
        pass

    class MilitaryReform(Thing):
        pass

    class ReformSeries(MilitaryReform):
        pass

    class MilitaryOrganization(Thing):
        pass

    class Army(MilitaryOrganization):
        pass

    class CitizenArmy(Army):
        pass

    class CitizenInfantry(CitizenArmy):
        pass

    class Legion(MilitaryOrganization):
        pass

    class MercenaryForce(MilitaryOrganization):
        pass

    class Threat(Thing):
        pass

    class ForeignInvasion(Threat):
        pass

    class ReadinessSystem(Thing):
        pass

    class PoliticalIdeal(Thing):
        pass

    class MilitaryCharacteristic(Thing):
        pass

    class TimeInterval(Thing):
        pass

    class Year(Thing):
        pass

    class Quantity(Thing):
        pass

    class initiatedBy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Person]

    class implementedIn(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Republic]

    class centeredIn(ObjectProperty, FunctionalProperty):
        domain = [PoliticalEntity]
        range = [City]

    class lastedDuring(ObjectProperty, FunctionalProperty):
        domain = [PoliticalEntity]
        range = [TimeInterval]

    class underLeadershipOf(ObjectProperty, FunctionalProperty):
        domain = [PoliticalEntity]
        range = [Person]

    class influencedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [PoliticalIdeal]

    class pervaded(ObjectProperty):
        domain = [PoliticalIdeal]
        range = [City]

    class soughtToEstablish(ObjectProperty):
        domain = [Person]
        range = [MilitaryOrganization, ReadinessSystem]

    class modeledOn(ObjectProperty):
        domain = [MilitaryReform, MilitaryOrganization]
        range = [HistoricalPolity, Legion]

    class hasCharacteristic(ObjectProperty):
        domain = [MilitaryOrganization]
        range = [MilitaryCharacteristic]

    class intendedOpponent(ObjectProperty):
        domain = [MilitaryOrganization]
        range = [MercenaryForce, Threat]

    class terrorized(ObjectProperty):
        domain = [MercenaryForce]
        range = [GeographicRegion]

    class addressedThreat(ObjectProperty):
        domain = [MilitaryReform]
        range = [MercenaryForce, Threat]

    class createdForce(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [CitizenArmy]

    class establishedSystem(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [ReadinessSystem]

    class keepsReady(ObjectProperty, FunctionalProperty):
        domain = [ReadinessSystem]
        range = [CitizenArmy]

    class hasSize(ObjectProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range = [Quantity]

    class institutedIn(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Year]

    class startsAt(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class endsAt(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class numericValue(DataProperty, FunctionalProperty):
        domain = [Year, Quantity]
        range = [int]

    MilitaryReform.is_a.append(initiatedBy.some(Person))
    MilitaryReform.is_a.append(implementedIn.some(Republic))
    Republic.is_a.append(lastedDuring.some(TimeInterval))
    ReadinessSystem.is_a.append(keepsReady.some(CitizenArmy))
    CitizenArmy.is_a.append(hasSize.some(Quantity))
    CitizenInfantry.is_a.append(intendedOpponent.some(MercenaryForce))

    FlorentineRepublic = Republic("FlorentineRepublicEntity")
    FlorentineRepublic.label = [
        "Florentine Republic",
        "Republic of Florence",
        "short - lived Republic of Florence",
    ]

    Florence = City("FlorenceCity")
    Florence.label = "Florence"

    NiccoloMachiavelli = Politician("NiccoloMachiavelliPerson")
    NiccoloMachiavelli.label = "Niccolò Machiavelli"
    NiccoloMachiavelli.is_a.append(PoliticalTheorist)

    GirolamoSavonarola = Priest("GirolamoSavonarolaPerson")
    GirolamoSavonarola.label = "Girolamo Savonarola"

    AncientRome = HistoricalPolity("AncientRomePolity")
    AncientRome.label = "ancient Rome"

    RomanLegions = Legion("RomanLegionsForce")
    RomanLegions.label = "Roman legions"

    ItalianCondottieri = MercenaryForce("ItalianCondottieriForce")
    ItalianCondottieri.label = "Italian Condottieri"

    Peninsula = GeographicRegion("PeninsulaRegion")
    Peninsula.label = "the peninsula"

    ChronicForeignInvasions = ForeignInvasion("ChronicForeignInvasionsThreat")
    ChronicForeignInvasions.label = "chronic foreign invasions"

    RepublicanSpirit = PoliticalIdeal("RepublicanSpiritIdeal")
    RepublicanSpirit.label = "republican spirit"

    Discipline = MilitaryCharacteristic("DisciplineCharacteristic")
    Discipline.label = "discipline"

    Years1498To1512 = TimeInterval("Years1498To1512Interval")
    Years1498To1512.label = "1498 to 1512"

    Year1498 = Year("Year1498Point")
    Year1498.label = "1498"
    Year1498.numericValue = 1498

    Year1512 = Year("Year1512Point")
    Year1512.label = "1512"
    Year1512.numericValue = 1512

    Year1506 = Year("Year1506Point")
    Year1506.label = "1506"
    Year1506.numericValue = 1506

    TwentyThousandMen = Quantity("TwentyThousandMenQuantity")
    TwentyThousandMen.label = "20,000 men"
    TwentyThousandMen.numericValue = 20000

    MilitaryReformsOfTheFlorentineRepublic = ReformSeries(
        "FlorentineRepublicMilitaryReforms"
    )
    MilitaryReformsOfTheFlorentineRepublic.label = (
        "The military reforms of the Florentine Republic"
    )

    FlorentineCitizenArmy = CitizenInfantry("FlorentineCitizenArmyForce")
    FlorentineCitizenArmy.label = ["citizen army", "citizen - infantry"]

    CitizenArmyReadinessSystem = ReadinessSystem(
        "CitizenArmyReadinessSystemEntity"
    )
    CitizenArmyReadinessSystem.label = (
        "a system that would keep this citizen army in a state of readiness"
    )

    FlorentineRepublic.centeredIn = Florence
    FlorentineRepublic.lastedDuring = Years1498To1512
    FlorentineRepublic.underLeadershipOf = GirolamoSavonarola

    Years1498To1512.startsAt = Year1498
    Years1498To1512.endsAt = Year1512

    RepublicanSpirit.pervaded = [Florence]

    NiccoloMachiavelli.soughtToEstablish = [FlorentineCitizenArmy]

    MilitaryReformsOfTheFlorentineRepublic.initiatedBy = NiccoloMachiavelli
    MilitaryReformsOfTheFlorentineRepublic.implementedIn = FlorentineRepublic
    MilitaryReformsOfTheFlorentineRepublic.influencedBy = [RepublicanSpirit]
    MilitaryReformsOfTheFlorentineRepublic.modeledOn = [AncientRome]
    MilitaryReformsOfTheFlorentineRepublic.addressedThreat = [
        ItalianCondottieri,
        ChronicForeignInvasions,
    ]
    MilitaryReformsOfTheFlorentineRepublic.createdForce = FlorentineCitizenArmy
    MilitaryReformsOfTheFlorentineRepublic.establishedSystem = CitizenArmyReadinessSystem
    MilitaryReformsOfTheFlorentineRepublic.institutedIn = Year1506

    FlorentineCitizenArmy.modeledOn = [RomanLegions]
    FlorentineCitizenArmy.hasCharacteristic = [Discipline]
    FlorentineCitizenArmy.intendedOpponent = [
        ItalianCondottieri,
        ChronicForeignInvasions,
    ]
    FlorentineCitizenArmy.hasSize = TwentyThousandMen

    ItalianCondottieri.terrorized = [Peninsula]

    CitizenArmyReadinessSystem.keepsReady = FlorentineCitizenArmy


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
