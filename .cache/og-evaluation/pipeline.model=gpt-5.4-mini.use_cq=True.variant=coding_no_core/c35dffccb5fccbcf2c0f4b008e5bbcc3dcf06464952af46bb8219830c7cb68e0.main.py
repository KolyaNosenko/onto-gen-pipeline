"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

Competency questions — natural-language queries the ontology should
support; your output must contain enough classes, properties, and
individuals to answer every one of them:
1. Who initiated the military reforms of the Florentine Republic?
2. During which republic and under which leader were the military reforms of the Florentine Republic initiated?
3. What political ideas motivated Machiavelli’s military reforms in Florence?
4. Which ancient military model did Machiavelli seek to emulate?
5. What kind of discipline did Machiavelli want the new army to have?
6. What type of army did Machiavelli aim to establish in Florence?
7. Against whom was the citizen-infantry intended to fight?
8. What external threats influenced the need for military reforms in Florence?
9. In what year did Machiavelli institute reforms to create the citizen army?
10. How large was the citizen army created by Machiavelli’s reforms?
11. What system was established to keep the citizen army ready for service?
12. What was the purpose of creating a standing state of readiness for the citizen army?
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
    class Person(Thing): pass
    class Politician(Person): pass
    class PoliticalTheorist(Person): pass
    class Priest(Person): pass

    class PoliticalEntity(Thing): pass
    class Republic(PoliticalEntity): pass
    class City(PoliticalEntity): pass

    class HistoricalEvent(Thing): pass
    class MilitaryReform(HistoricalEvent): pass

    class MilitaryModel(Thing): pass
    class MilitaryEstablishment(Thing): pass
    class PoliticalIdea(Thing): pass
    class Discipline(Thing): pass
    class System(Thing): pass
    class ReadinessState(Thing): pass

    class MilitaryForce(Thing): pass
    class Army(MilitaryForce): pass
    class Infantry(MilitaryForce): pass
    class CitizenArmy(Army): pass
    class CitizenInfantry(Infantry): pass
    class Legion(MilitaryForce): pass
    class Condottieri(MilitaryForce): pass

    class ExternalThreat(Thing): pass
    class ForeignInvasion(ExternalThreat): pass

    class Quantity(Thing): pass
    class Headcount(Quantity): pass
    class TimePoint(Thing): pass
    class Year(TimePoint): pass

    class initiatedBy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Person]

    class occurredDuring(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Republic]

    class occurredIn(ObjectProperty, FunctionalProperty):
        domain = [HistoricalEvent]
        range = [City]

    class ledBy(ObjectProperty, FunctionalProperty):
        domain = [Republic]
        range = [Person]

    class motivatedBy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [PoliticalIdea]

    class emulatedMilitaryModel(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [MilitaryModel]

    class establishedMilitaryEstablishment(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [MilitaryEstablishment]

    class establishedArmy(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Army]

    class establishedSystem(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [System]

    class hasDiscipline(ObjectProperty, FunctionalProperty):
        domain = [Army]
        range = [Discipline]

    class intendedToFightAgainst(ObjectProperty):
        domain = [CitizenInfantry]
        range = [ExternalThreat]

    class influencedByThreat(ObjectProperty):
        domain = [MilitaryReform]
        range = [ExternalThreat]

    class institutedInYear(ObjectProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [Year]

    class hasSize(ObjectProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range = [Headcount]

    class locatedIn(ObjectProperty, FunctionalProperty):
        domain = [Republic]
        range = [City]

    class keepsInStateOfReadiness(ObjectProperty, FunctionalProperty):
        domain = [System]
        range = [Army]

    class aimsAtState(ObjectProperty, FunctionalProperty):
        domain = [System]
        range = [ReadinessState]

    class startYear(ObjectProperty, FunctionalProperty):
        domain = [Republic]
        range = [Year]

    class endYear(ObjectProperty, FunctionalProperty):
        domain = [Republic]
        range = [Year]

    class countValue(DataProperty, FunctionalProperty):
        domain = [Headcount]
        range = [int]

    class yearValue(DataProperty, FunctionalProperty):
        domain = [Year]
        range = [int]

    NiccoloMachiavelli = PoliticalTheorist("NiccoloMachiavelli")
    NiccoloMachiavelli.is_a.append(Politician)
    NiccoloMachiavelli.label = "Niccolò Machiavelli"

    GirolamoSavonarola = Priest("GirolamoSavonarola")
    GirolamoSavonarola.label = "Girolamo Savonarola"

    RepublicOfFlorence = Republic("RepublicOfFlorence")
    RepublicOfFlorence.label = ["Florentine Republic", "Republic of Florence", "short - lived Republic of Florence"]

    Florence = City("Florence")
    Florence.label = "Florence"

    AncientRome = City("AncientRome")
    AncientRome.is_a.append(MilitaryModel)
    AncientRome.label = "ancient Rome"

    RomanLegions = Legion("RomanLegions")
    RomanLegions.label = "Roman legions"

    RomanLegionsDiscipline = Discipline("RomanLegionsDiscipline")
    RomanLegionsDiscipline.label = "discipline of the Roman legions"

    ItalianCondottieri = Condottieri("ItalianCondottieri")
    ItalianCondottieri.label = "Italian Condottieri"

    ChronicForeignInvasions = ForeignInvasion("ChronicForeignInvasions")
    ChronicForeignInvasions.label = "chronic foreign invasions"

    RepublicanSpirit = PoliticalIdea("RepublicanSpirit")
    RepublicanSpirit.label = "republican spirit"

    MilitaryReformsOfFlorentineRepublic = MilitaryReform("MilitaryReformsOfFlorentineRepublic")
    MilitaryReformsOfFlorentineRepublic.label = ["The military reforms of the Florentine Republic", "military reforms of the Florentine Republic", "series of reforms"]

    MilitaryEstablishmentOfFlorence = MilitaryEstablishment("MilitaryEstablishmentOfFlorence")
    MilitaryEstablishmentOfFlorence.label = "military establishment"

    CitizenArmyEntity = CitizenArmy("CitizenArmyEntity")
    CitizenArmyEntity.label = "citizen army"

    CitizenInfantryEntity = CitizenInfantry("CitizenInfantryEntity")
    CitizenInfantryEntity.label = "citizen-infantry"

    ReadinessSystem = System("ReadinessSystem")
    ReadinessSystem.label = "system"

    StateOfReadiness = ReadinessState("StateOfReadiness")
    StateOfReadiness.label = "state of readiness"

    Year1498 = Year("Year1498")
    Year1498.label = "1498"
    Year1498.yearValue = 1498

    Year1512 = Year("Year1512")
    Year1512.label = "1512"
    Year1512.yearValue = 1512

    Year1506 = Year("Year1506")
    Year1506.label = "1506"
    Year1506.yearValue = 1506

    TwentyThousandMen = Headcount("TwentyThousandMen")
    TwentyThousandMen.label = "20,000 men"
    TwentyThousandMen.countValue = 20000

    RepublicOfFlorence.ledBy = GirolamoSavonarola
    RepublicOfFlorence.locatedIn = Florence
    RepublicOfFlorence.startYear = Year1498
    RepublicOfFlorence.endYear = Year1512

    MilitaryReformsOfFlorentineRepublic.initiatedBy = NiccoloMachiavelli
    MilitaryReformsOfFlorentineRepublic.occurredDuring = RepublicOfFlorence
    MilitaryReformsOfFlorentineRepublic.occurredIn = Florence
    MilitaryReformsOfFlorentineRepublic.motivatedBy = RepublicanSpirit
    MilitaryReformsOfFlorentineRepublic.emulatedMilitaryModel = AncientRome
    MilitaryReformsOfFlorentineRepublic.establishedMilitaryEstablishment = MilitaryEstablishmentOfFlorence
    MilitaryReformsOfFlorentineRepublic.establishedArmy = CitizenArmyEntity
    MilitaryReformsOfFlorentineRepublic.establishedSystem = ReadinessSystem
    MilitaryReformsOfFlorentineRepublic.influencedByThreat = [ItalianCondottieri, ChronicForeignInvasions]
    MilitaryReformsOfFlorentineRepublic.institutedInYear = Year1506

    MilitaryEstablishmentOfFlorence.similarTo = AncientRome

    CitizenArmyEntity.hasDiscipline = RomanLegionsDiscipline
    CitizenArmyEntity.hasSize = TwentyThousandMen

    CitizenInfantryEntity.intendedToFightAgainst = [ItalianCondottieri, ChronicForeignInvasions]

    ReadinessSystem.keepsInStateOfReadiness = CitizenArmyEntity
    ReadinessSystem.aimsAtState = StateOfReadiness


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
