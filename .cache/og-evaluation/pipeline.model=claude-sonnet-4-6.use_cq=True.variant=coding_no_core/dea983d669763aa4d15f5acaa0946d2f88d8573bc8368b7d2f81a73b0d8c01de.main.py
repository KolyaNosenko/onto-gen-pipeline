"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

1. Who initiated the military reforms of the Florentine Republic?
2. What political roles did Niccolò Machiavelli hold?
3. During what time period did the Republic of Florence last?
4. Who led the Republic of Florence during its existence?
5. What ancient military model did Machiavelli seek to emulate in his reforms?
6. What type of army did Machiavelli aim to establish?
7. What military threats was the citizen army intended to counter?
8. Who were the Italian Condottieri?
9. In what year did Machiavelli institute his series of military reforms?
10. How many men were intended to compose the citizen army created by Machiavelli's reforms?
11. What was the purpose of the system established alongside the citizen army?
12. What military qualities did Machiavelli seek to instill in his proposed army?
13. What foreign threats were regularly occurring in Italy at the time of the reforms?
14. What was the relationship between the republican spirit of Florence and Machiavelli's military reforms?
15. What specific type of infantry did Machiavelli seek to establish through his reforms?
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
    # ── Classes ────────────────────────────────────────────────────────────

    class Person(Thing): pass
    class Politician(Person): pass
    class PoliticalTheorist(Person): pass
    class Priest(Person): pass

    class PoliticalEntity(Thing): pass
    class Republic(PoliticalEntity): pass

    class GeographicalEntity(Thing): pass
    class City(GeographicalEntity): pass
    class State(GeographicalEntity): pass
    class AncientState(State): pass

    class MilitaryForce(Thing): pass
    class CitizenArmy(MilitaryForce): pass
    class CitizenInfantry(CitizenArmy): pass
    class MercenaryForce(MilitaryForce): pass
    class MilitaryLegion(MilitaryForce): pass

    class MilitaryThreat(Thing): pass
    class ForeignInvasion(MilitaryThreat): pass
    class MercenaryThreat(MercenaryForce, MilitaryThreat): pass

    class MilitaryReform(Thing): pass
    class ReadinessSystem(Thing): pass
    class PoliticalIdeology(Thing): pass

    # ── Object Properties ──────────────────────────────────────────────────

    class initiatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [Person]

    class ledBy(ObjectProperty):
        domain = [Republic]
        range = [Person]

    class locatedIn(ObjectProperty):
        domain = [Republic]
        range = [City]

    class soughtToEmulate(ObjectProperty):
        domain = [Person]
        range = [MilitaryForce]

    class aimedToEstablish(ObjectProperty):
        domain = [Person]
        range = [MilitaryForce]

    class intendedToCounter(ObjectProperty):
        domain = [CitizenArmy]
        range = [MilitaryThreat]

    class createdBy(ObjectProperty):
        domain = [MilitaryForce]
        range = [MilitaryReform]

    class maintainedBy(ObjectProperty):
        domain = [CitizenArmy]
        range = [ReadinessSystem]

    class establishedBy(ObjectProperty, FunctionalProperty):
        domain = [ReadinessSystem]
        range = [Person]

    class occurredDuring(ObjectProperty):
        domain = [MilitaryReform]
        range = [Republic]

    class motivatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [PoliticalIdeology]

    class inspiredByDisciplineOf(ObjectProperty):
        domain = [CitizenArmy]
        range = [MilitaryLegion]

    class terrorizedBy(ObjectProperty):
        domain = [GeographicalEntity]
        range = [MercenaryForce]

    # ── Data Properties ────────────────────────────────────────────────────

    class startYear(DataProperty, FunctionalProperty):
        domain = [Republic]
        range = [int]

    class endYear(DataProperty, FunctionalProperty):
        domain = [Republic]
        range = [int]

    class reformYear(DataProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [int]

    class armySize(DataProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range = [int]

    # ── Individuals ────────────────────────────────────────────────────────

    # Persons
    NiccoloMachiavelli = Politician("NiccoloMachiavelli")
    NiccoloMachiavelli.label = "Niccolò Machiavelli"
    NiccoloMachiavelli.is_a.append(PoliticalTheorist)

    GirolamoSavonarola = Priest("GirolamoSavonarola")
    GirolamoSavonarola.label = "Girolamo Savonarola"

    # Geographical entities
    FlorenceCity = City("FlorenceCity")
    FlorenceCity.label = "Florence"

    ItalianPeninsula = GeographicalEntity("ItalianPeninsula")
    ItalianPeninsula.label = "Italian peninsula"

    AncientRome = AncientState("AncientRome")
    AncientRome.label = "ancient Rome"

    # Political entity
    RepublicOfFlorence = Republic("RepublicOfFlorence")
    RepublicOfFlorence.label = "Republic of Florence"
    RepublicOfFlorence.startYear = 1498
    RepublicOfFlorence.endYear = 1512
    RepublicOfFlorence.ledBy = [GirolamoSavonarola]
    RepublicOfFlorence.locatedIn = [FlorenceCity]

    # Political ideology
    RepublicanSpiritInst = PoliticalIdeology("RepublicanSpiritInst")
    RepublicanSpiritInst.label = "republican spirit"

    # Military forces
    RomanLegions = MilitaryLegion("RomanLegions")
    RomanLegions.label = "Roman legions"

    ItalianCondottieri = MercenaryThreat("ItalianCondottieri")
    ItalianCondottieri.label = "Italian Condottieri"
    ItalianPeninsula.terrorizedBy = [ItalianCondottieri]

    # Military threats
    ChronicForeignInvasions = ForeignInvasion("ChronicForeignInvasions")
    ChronicForeignInvasions.label = "foreign invasions"

    # Military reforms
    FlorentineRepublicMilitaryReforms = MilitaryReform("FlorentineRepublicMilitaryReforms")
    FlorentineRepublicMilitaryReforms.label = "military reforms of the Florentine Republic"
    FlorentineRepublicMilitaryReforms.initiatedBy = [NiccoloMachiavelli]
    FlorentineRepublicMilitaryReforms.reformYear = 1506
    FlorentineRepublicMilitaryReforms.occurredDuring = [RepublicOfFlorence]
    FlorentineRepublicMilitaryReforms.motivatedBy = [RepublicanSpiritInst]

    # Citizen army
    FlorentineCitizenArmy = CitizenArmy("FlorentineCitizenArmy")
    FlorentineCitizenArmy.label = "citizen army"
    FlorentineCitizenArmy.armySize = 20000
    FlorentineCitizenArmy.createdBy = [FlorentineRepublicMilitaryReforms]
    FlorentineCitizenArmy.inspiredByDisciplineOf = [RomanLegions]
    FlorentineCitizenArmy.intendedToCounter = [ItalianCondottieri, ChronicForeignInvasions]

    # Citizen infantry
    FlorentineCitizenInfantry = CitizenInfantry("FlorentineCitizenInfantry")
    FlorentineCitizenInfantry.label = "citizen-infantry"
    FlorentineCitizenInfantry.createdBy = [FlorentineRepublicMilitaryReforms]

    # Readiness system
    ReadinessSystemInst = ReadinessSystem("ReadinessSystemInst")
    ReadinessSystemInst.label = "system of readiness"
    ReadinessSystemInst.establishedBy = NiccoloMachiavelli

    FlorentineCitizenArmy.maintainedBy = [ReadinessSystemInst]

    # Machiavelli's aims
    NiccoloMachiavelli.soughtToEmulate = [RomanLegions]
    NiccoloMachiavelli.aimedToEstablish = [FlorentineCitizenArmy, FlorentineCitizenInfantry]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
