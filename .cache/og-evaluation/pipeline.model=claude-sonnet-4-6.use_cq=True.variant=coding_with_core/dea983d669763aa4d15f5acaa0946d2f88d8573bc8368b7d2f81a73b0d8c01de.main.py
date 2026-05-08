"""
=== TASK INPUT ===
Source text:
The military reforms of the Florentine Republic were initiated by Florentine politician and political theorist Niccolò Machiavelli during the short - lived Republic of Florence that lasted from 1498 to 1512 under the priest Girolamo Savonarola . In the pursuit of the republican spirit which pervaded Florence at the time , Machiavelli sought to establish a military establishment that was similar to that of ancient Rome . He was specifically focused upon the establishment of an army possessed with the discipline of the Roman legions . He sought to establish a citizen - infantry capable of taking the field against the Italian Condottieri of the day , who largely terrorized the peninsula , in addition to the chronic foreign invasions which occurred on a regular basis at this time . Broadly speaking Machiavelli would institute a series of reforms in 1506 that would create a citizen army of 20,000 men , and establish a system that would keep this citizen army in a state of readiness .

1. Who initiated the military reforms of the Florentine Republic?
2. What political roles did Niccolò Machiavelli hold?
3. During which time period did the Republic of Florence last?
4. Who led the Republic of Florence?
5. What ancient civilization's military did Machiavelli seek to emulate?
6. What type of army did Machiavelli aim to establish?
7. What was the purpose of establishing a citizen-infantry in Florence?
8. Who were the Italian Condottieri?
9. What threats did Florence face that motivated the military reforms?
10. In what year did Machiavelli institute his series of military reforms?
11. How many men were planned to form the citizen army?
12. What was the goal of the system established alongside the citizen army?
13. What military unit served as the model for the discipline Machiavelli sought to instill?
14. What was the relationship between the military reforms and the republican spirit of Florence?
15. What was the duration of the Republic of Florence under Savonarola?
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
    AgentivePhysicalObject, Accomplishment, Society,
    NonAgentiveSocialObject, TimeInterval,
)
from og_sandbox_with_core.core.properties import temporallyLocatedAt


with core:
    # ── ENTITY CLASSES ──────────────────────────────────────────────────
    class Politician(AgentivePhysicalObject): pass
    class PoliticalTheorist(AgentivePhysicalObject): pass
    class Priest(AgentivePhysicalObject): pass
    class Republic(Society): pass
    class AncientCivilization(Society): pass
    class MilitaryForce(NonAgentiveSocialObject): pass
    class CitizenArmy(MilitaryForce): pass
    class CitizenInfantry(CitizenArmy): pass
    class MilitaryLegion(MilitaryForce): pass
    class MercenaryForce(MilitaryForce): pass
    class MilitaryReform(Accomplishment): pass
    class ForeignInvasion(Accomplishment): pass
    class RepublicanSpirit(NonAgentiveSocialObject): pass

    # ── PROPERTIES ──────────────────────────────────────────────────────
    class initiatedBy(ObjectProperty):
        domain = [MilitaryReform]
        range  = [AgentivePhysicalObject]

    class ledBy(ObjectProperty):
        domain = [Society]
        range  = [AgentivePhysicalObject]

    class aimedToEmulate(ObjectProperty):
        domain = [MilitaryReform]
        range  = [AncientCivilization]

    class servedAsModelFor(ObjectProperty):
        domain = [MilitaryForce]
        range  = [MilitaryReform]

    class aimedToEstablish(ObjectProperty):
        domain = [MilitaryReform]
        range  = [MilitaryForce]

    class aimedToCounter(ObjectProperty):
        domain = [MilitaryReform]
        range  = [Or([MercenaryForce, ForeignInvasion])]

    class inspiredBy(ObjectProperty):
        domain = [MilitaryReform]
        range  = [RepublicanSpirit]

    class pervades(ObjectProperty):
        domain = [RepublicanSpirit]
        range  = [Society]

    class citizenArmySize(DataProperty, FunctionalProperty):
        domain = [CitizenArmy]
        range  = [int]

    # ── NAMED INDIVIDUALS ────────────────────────────────────────────────
    machiavelli = Politician("NiccoloMachiavelli")
    machiavelli.label = "Niccolò Machiavelli"
    machiavelli.is_a.append(PoliticalTheorist)

    savonarola = Priest("GirolamoSavonarola")
    savonarola.label = "Girolamo Savonarola"

    republicOfFlorence = Republic("RepublicOfFlorence")
    republicOfFlorence.label = "Republic of Florence"

    ancientRome = AncientCivilization("AncientRome")
    ancientRome.label = "ancient Rome"

    romanLegions = MilitaryLegion("RomanLegions")
    romanLegions.label = "Roman legions"

    italianCondottieri = MercenaryForce("ItalianCondottieri")
    italianCondottieri.label = "Italian Condottieri"

    interval1498to1512 = TimeInterval("Interval1498to1512")
    interval1498to1512.label = "1498 to 1512"

    year1506 = TimeInterval("Year1506")
    year1506.label = "1506"

    militaryReforms = MilitaryReform("MilitaryReformsOfTheFlorentineRepublic")
    militaryReforms.label = "military reforms of the Florentine Republic"

    florentineCitizenArmy = CitizenArmy("FlorentineCitizenArmy")
    florentineCitizenArmy.label = "citizen army"
    florentineCitizenArmy.citizenArmySize = 20000

    florentineCitizenInfantry = CitizenInfantry("FlorentineCitizenInfantry")
    florentineCitizenInfantry.label = "citizen-infantry"

    foreignInvasions = ForeignInvasion("ChronicForeignInvasions")
    foreignInvasions.label = "chronic foreign invasions"

    republicanSpirit = RepublicanSpirit("RepublicanSpiritOfFlorence")
    republicanSpirit.label = "republican spirit"

    # ── PROPERTY ASSERTIONS ──────────────────────────────────────────────
    militaryReforms.initiatedBy.append(machiavelli)
    militaryReforms.temporallyLocatedAt = year1506
    militaryReforms.aimedToEmulate.append(ancientRome)
    militaryReforms.aimedToEstablish.append(florentineCitizenArmy)
    militaryReforms.aimedToEstablish.append(florentineCitizenInfantry)
    militaryReforms.aimedToCounter.append(italianCondottieri)
    militaryReforms.aimedToCounter.append(foreignInvasions)
    militaryReforms.inspiredBy.append(republicanSpirit)

    romanLegions.servedAsModelFor.append(militaryReforms)

    republicOfFlorence.temporallyLocatedAt = interval1498to1512
    republicOfFlorence.ledBy.append(savonarola)

    republicanSpirit.pervades.append(republicOfFlorence)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
