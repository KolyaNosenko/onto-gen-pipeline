"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

1. Who initiated the military reforms of the Florentine Republic?
2. During which time period did the Republic of Florence exist?
3. What was the primary goal of Machiavelli's military reforms?
4. Which ancient military system did Machiavelli use as a model for his reforms?
5. What specific military characteristics did Machiavelli seek to establish?
6. Who was the leader under whose rule the military reforms took place?
7. What were the main threats that prompted Machiavelli's military reforms?
8. How many soldiers comprised the citizen army established by Machiavelli?
9. In what year were the military reforms instituted?
10. What system did Machiavelli establish to maintain the citizen army's readiness?
11. What type of military unit did Machiavelli seek to create as part of his reforms?
12. Against whom was the citizen-infantry specifically intended to fight?
13. What political ideology motivated Machiavelli's military establishment?
14. What were the chronic threats faced by Florence during this period?
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
    # Entity classes
    class Person(Thing): pass
    class Politician(Person): pass
    class Priest(Person): pass
    
    class Place(Thing): pass
    class City(Place): pass
    
    class State(Thing): pass
    class Republic(State): pass
    
    class MilitaryReform(Thing): pass
    
    class MilitaryUnit(Thing): pass
    class Army(MilitaryUnit): pass
    class Infantry(MilitaryUnit): pass
    class Legions(MilitaryUnit): pass
    class MilitaryGroup(MilitaryUnit): pass
    
    class MilitarySystem(Thing): pass
    
    class Threat(Thing): pass
    class Invasion(Threat): pass
    
    class Ideology(Thing): pass
    
    class TimeInterval(Thing): pass
    
    class System(Thing): pass
    class ReadinessSystem(System): pass
    
    # Object Properties
    class initiatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [Person]
    
    class occurredDuring(ObjectProperty):
        domain = [MilitaryReform]
        range = [TimeInterval]
    
    class existedDuring(ObjectProperty):
        domain = [State]
        range = [TimeInterval]
    
    class ledBy(ObjectProperty):
        domain = [State]
        range = [Person]
    
    class modeledAfter(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitarySystem]
    
    class emulates(ObjectProperty):
        domain = [MilitaryReform]
        range = [MilitaryUnit]
    
    class targetedAgainst(ObjectProperty):
        domain = [MilitaryUnit]
        range = [Threat]
    
    class motivatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range = [Ideology]
    
    class establishedSystem(ObjectProperty):
        domain = [MilitaryReform]
        range = [System]
    
    class maintainsReadinessOf(ObjectProperty):
        domain = [ReadinessSystem]
        range = [MilitaryUnit]
    
    # Data Properties
    class year(DataProperty, FunctionalProperty):
        domain = [MilitaryReform]
        range = [int]
    
    class startYear(DataProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [int]
    
    class endYear(DataProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [int]
    
    class size(DataProperty, FunctionalProperty):
        domain = [Army]
        range = [int]
    
    # Instances: People
    niccoloMachiavelli = Politician("NiccoloMachiavelli")
    niccoloMachiavelli.label = "Niccolò Machiavelli"
    
    girolamoSavonarola = Priest("GirolamoSavonarola")
    girolamoSavonarola.label = "Girolamo Savonarola"
    
    # Instances: Places
    florence = City("Florence")
    florence.label = "Florence"
    
    rome = City("Rome")
    rome.label = "Rome"
    
    # Instances: States
    republicOfFlorence = Republic("RepublicOfFlorence")
    republicOfFlorence.label = "Republic of Florence"
    
    # Instances: Military Units and Systems
    romanLegions = Legions("RomanLegions")
    romanLegions.label = "Roman legions"
    
    romanMilitarySystem = MilitarySystem("RomanMilitarySystem")
    romanMilitarySystem.label = "Roman military system"
    
    italianCondottieri = MilitaryGroup("ItalianCondottieri")
    italianCondottieri.label = "Italian Condottieri"
    
    foreignInvasions = Invasion("ForeignInvasions")
    foreignInvasions.label = "foreign invasions"
    
    citizenArmy = Army("CitizenArmy")
    citizenArmy.label = "citizen army"
    
    citizenInfantry = Infantry("CitizenInfantry")
    citizenInfantry.label = "citizen-infantry"
    
    # Instances: Concepts and Time
    republicanSpirit = Ideology("RepublicanSpirit")
    republicanSpirit.label = "republican spirit"
    
    timeInterval1498_1512 = TimeInterval("TimeInterval14981512")
    timeInterval1498_1512.label = "1498-1512"
    timeInterval1498_1512.startYear = 1498
    timeInterval1498_1512.endYear = 1512
    
    readinessSystem = ReadinessSystem("ReadinessSystemForCitizenArmy")
    readinessSystem.label = "readiness system for citizen army"
    
    # Main event: Military reforms
    militaryReforms = MilitaryReform("MilitaryReformsOfFlorentineRepublic")
    militaryReforms.label = "military reforms of the Florentine Republic"
    militaryReforms.initiatedBy = [niccoloMachiavelli]
    militaryReforms.occurredDuring = [timeInterval1498_1512]
    militaryReforms.year = 1506
    militaryReforms.motivatedBy = [republicanSpirit]
    militaryReforms.modeledAfter = [romanMilitarySystem]
    militaryReforms.emulates = [romanLegions]
    militaryReforms.establishedSystem = [readinessSystem]
    
    # State and governance
    republicOfFlorence.existedDuring = [timeInterval1498_1512]
    republicOfFlorence.ledBy = [girolamoSavonarola]
    
    # Military units and threats
    citizenArmy.size = 20000
    citizenArmy.targetedAgainst = [italianCondottieri, foreignInvasions]
    
    citizenInfantry.targetedAgainst = [italianCondottieri, foreignInvasions]
    
    readinessSystem.maintainsReadinessOf = [citizenArmy]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
