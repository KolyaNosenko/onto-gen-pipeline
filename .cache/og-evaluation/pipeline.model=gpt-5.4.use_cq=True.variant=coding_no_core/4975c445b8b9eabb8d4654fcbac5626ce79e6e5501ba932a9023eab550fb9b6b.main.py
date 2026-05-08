"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

What was the original name of the city of Austin, Texas?
What is the current name of the city originally called Waterloo?
In which county is Austin, Texas located?
In which part of the state is Austin, Texas located?
Who was the Vice President of the Republic of Texas who visited the Austin area between 1837 and 1838?
When did Mirabeau B. Lamar visit the area that became Austin?
What was the purpose of Mirabeau B. Lamar’s visit to the area?
Which city served as the capital of the Republic of Texas before its proposed relocation?
Who proposed relocating the capital of the Republic of Texas to the area that became Austin?
To what geographic area was the capital of the Republic of Texas proposed to be relocated?
On which bank of the Colorado River was the proposed capital site located?
Near what present-day landmark was the proposed capital site situated?
When was the site officially chosen as the capital of the Republic of Texas?
What number capital location of the Republic of Texas was the Austin site?
Under what name was the city incorporated when it became the capital site?
What name replaced Waterloo?
Why was the name Waterloo changed to Austin?
In whose honor was Austin named?
Who was known as the “Father of Texas”?
What office did Stephen F. Austin hold in the Republic of Texas?
What is the relationship between Waterloo and Austin?
Which historical events led to the renaming of Waterloo to Austin?
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
    class Place(Thing):
        pass

    class AdministrativeRegion(Place):
        pass

    class City(AdministrativeRegion):
        pass

    class County(AdministrativeRegion):
        pass

    class State(AdministrativeRegion):
        pass

    class UrbanArea(Place):
        pass

    class NaturalFeature(Place):
        pass

    class River(NaturalFeature):
        pass

    class RiverBank(Place):
        pass

    class Bridge(Place):
        pass

    class PoliticalEntity(Thing):
        pass

    class Republic(PoliticalEntity):
        pass

    class Name(Thing):
        pass

    class PlaceName(Name):
        pass

    class Person(Thing):
        pass

    class GovernmentOffice(Thing):
        pass

    class HonorificTitle(Thing):
        pass

    class Event(Thing):
        pass

    class Visit(Event):
        pass

    class Expedition(Event):
        pass

    class RelocationProposal(Event):
        pass

    class CapitalSelection(Event):
        pass

    class Incorporation(Event):
        pass

    class Renaming(Event):
        pass

    class TimeInterval(Thing):
        pass

    class Year(TimeInterval):
        pass

    class OrdinalQuantity(Thing):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range = [Place]

    class hasOriginalName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [PlaceName]

    class hasCurrentName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [PlaceName]

    class replacedBy(ObjectProperty, FunctionalProperty):
        domain = [PlaceName]
        range = [PlaceName]

    class namedInHonorOf(ObjectProperty, FunctionalProperty):
        domain = [City, PlaceName, Renaming]
        range = [Person]

    class hasTitle(ObjectProperty):
        domain = [Person]
        range = [HonorificTitle]

    class holdsOffice(ObjectProperty):
        domain = [Person]
        range = [GovernmentOffice]

    class officeOf(ObjectProperty, FunctionalProperty):
        domain = [GovernmentOffice]
        range = [PoliticalEntity]

    class carriedOutBy(ObjectProperty, FunctionalProperty):
        domain = [Event]
        range = [Person]

    class visitedPlace(ObjectProperty):
        domain = [Visit]
        range = [Place]

    class duringExpedition(ObjectProperty, FunctionalProperty):
        domain = [Visit]
        range = [Expedition]

    class hasTimeInterval(ObjectProperty, FunctionalProperty):
        domain = [Event]
        range = [TimeInterval]

    class hasStartYear(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class hasEndYear(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class relocatesCapitalOf(ObjectProperty, FunctionalProperty):
        domain = [RelocationProposal, CapitalSelection]
        range = [PoliticalEntity]

    class fromCapital(ObjectProperty, FunctionalProperty):
        domain = [RelocationProposal]
        range = [City]

    class toPlace(ObjectProperty):
        domain = [Event]
        range = [Place]

    class nearLandmark(ObjectProperty):
        domain = [Place]
        range = [Place]

    class bankOfRiver(ObjectProperty, FunctionalProperty):
        domain = [RiverBank]
        range = [River]

    class resultedInName(ObjectProperty, FunctionalProperty):
        domain = [Incorporation, Renaming]
        range = [PlaceName]

    class hasCapitalLocationOrdinal(ObjectProperty, FunctionalProperty):
        domain = [CapitalSelection]
        range = [OrdinalQuantity]

    class ledTo(ObjectProperty):
        domain = [Event]
        range = [Event]

    class yearValue(DataProperty, FunctionalProperty):
        domain = [Year]
        range = [int]

    class textValue(DataProperty, FunctionalProperty):
        domain = [TimeInterval, OrdinalQuantity]
        range = [str]

    class ordinalValue(DataProperty, FunctionalProperty):
        domain = [OrdinalQuantity]
        range = [int]

    class isFinal(DataProperty, FunctionalProperty):
        domain = [CapitalSelection]
        range = [bool]

    Visit.is_a.append(visitedPlace.some(Place))
    Visit.is_a.append(duringExpedition.some(Expedition))
    RelocationProposal.is_a.append(relocatesCapitalOf.some(PoliticalEntity))
    RelocationProposal.is_a.append(toPlace.some(Place))
    CapitalSelection.is_a.append(hasCapitalLocationOrdinal.some(OrdinalQuantity))
    Renaming.is_a.append(resultedInName.some(PlaceName))

    austin = City("AustinTexas")
    austin.label = ["Austin , Texas", "Austin"]
    waterlooName = PlaceName("WaterlooName")
    waterlooName.label = ["Waterloo", '" Waterloo "']
    austinName = PlaceName("AustinName")
    austinName.label = "Austin"
    travisCounty = County("TravisCounty")
    travisCounty.label = "Travis County"
    texas = State("Texas")
    texas.label = "Texas"
    centralPartOfTheState = UrbanArea("CentralPartOfTheState")
    centralPartOfTheState.label = "central part of the state"
    republicOfTexas = Republic("RepublicOfTexas")
    republicOfTexas.label = "Republic of Texas"
    mirabeauBLamar = Person("MirabeauBLamar")
    mirabeauBLamar.label = "Mirabeau B. Lamar"
    houston = City("Houston")
    houston.label = "Houston"
    northBankOfTheColoradoRiver = RiverBank("NorthBankOfTheColoradoRiver")
    northBankOfTheColoradoRiver.label = "north bank of the Colorado River"
    coloradoRiver = River("ColoradoRiver")
    coloradoRiver.label = "Colorado River"
    annWRichardsCongressAvenueBridge = Bridge("AnnWRichardsCongressAvenueBridge")
    annWRichardsCongressAvenueBridge.label = "Ann W. Richards Congress Avenue Bridge"
    centralAustin = UrbanArea("CentralAustin")
    centralAustin.label = "central Austin"
    stephenFAustin = Person("StephenFAustin")
    stephenFAustin.label = "Stephen F. Austin"
    fatherOfTexas = HonorificTitle("FatherOfTexas")
    fatherOfTexas.label = "Father of Texas"
    vicePresident = GovernmentOffice("VicePresidentOfRepublicOfTexas")
    vicePresident.label = "Republic of Texas Vice President"
    firstSecretaryOfState = GovernmentOffice("FirstSecretaryOfState")
    firstSecretaryOfState.label = "first secretary of state"
    year1837 = Year("Year1837")
    year1837.label = "1837"
    year1837.yearValue = 1837
    year1838 = Year("Year1838")
    year1838.label = "1838"
    year1838.yearValue = 1838
    between1837And1838 = TimeInterval("Between1837And1838")
    between1837And1838.label = "between 1837 and 1838"
    between1837And1838.textValue = "between 1837 and 1838"
    between1837And1838.hasStartYear = year1837
    between1837And1838.hasEndYear = year1838
    year1839 = Year("Year1839")
    year1839.label = "1839"
    year1839.yearValue = 1839
    buffaloHuntingExpedition = Expedition("BuffaloHuntingExpedition")
    buffaloHuntingExpedition.label = "buffalo - hunting expedition"
    seventhAndFinalLocation = OrdinalQuantity("SeventhAndFinalLocation")
    seventhAndFinalLocation.label = "seventh and final location"
    seventhAndFinalLocation.textValue = "seventh and final location"
    seventhAndFinalLocation.ordinalValue = 7
    lamarVisit = Visit("LamarVisit")
    lamarVisit.label = "visited the area during a buffalo - hunting expedition between 1837 and 1838"
    capitalRelocationProposal = RelocationProposal("CapitalRelocationProposal")
    capitalRelocationProposal.label = "he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin"
    capitalSelection1839 = CapitalSelection("CapitalSelection1839")
    capitalSelection1839.label = "the site was officially chosen as the seventh and final location for the capital of the Republic of Texas"
    waterlooIncorporation = Incorporation("WaterlooIncorporation")
    waterlooIncorporation.label = 'It was incorporated under the name " Waterloo "'
    austinRenaming = Renaming("AustinRenaming")
    austinRenaming.label = "the name was changed to Austin in honor of Stephen F. Austin"

    austin.locatedIn = [travisCounty, centralPartOfTheState, texas]
    travisCounty.locatedIn = [texas]
    centralPartOfTheState.locatedIn = [texas]
    centralAustin.locatedIn = [austin]
    northBankOfTheColoradoRiver.locatedIn = [centralAustin]
    northBankOfTheColoradoRiver.bankOfRiver = coloradoRiver
    northBankOfTheColoradoRiver.nearLandmark = [annWRichardsCongressAvenueBridge]
    austin.hasOriginalName = waterlooName
    austin.hasCurrentName = austinName
    austin.namedInHonorOf = stephenFAustin
    waterlooName.replacedBy = austinName
    mirabeauBLamar.holdsOffice = [vicePresident]
    vicePresident.officeOf = republicOfTexas
    stephenFAustin.hasTitle = [fatherOfTexas]
    stephenFAustin.holdsOffice = [firstSecretaryOfState]
    firstSecretaryOfState.officeOf = republicOfTexas

    lamarVisit.carriedOutBy = mirabeauBLamar
    lamarVisit.visitedPlace = [austin]
    lamarVisit.duringExpedition = buffaloHuntingExpedition
    lamarVisit.hasTimeInterval = between1837And1838
    capitalRelocationProposal.carriedOutBy = mirabeauBLamar
    capitalRelocationProposal.relocatesCapitalOf = republicOfTexas
    capitalRelocationProposal.fromCapital = houston
    capitalRelocationProposal.toPlace = [northBankOfTheColoradoRiver]
    capitalSelection1839.relocatesCapitalOf = republicOfTexas
    capitalSelection1839.toPlace = [austin]
    capitalSelection1839.hasTimeInterval = year1839
    capitalSelection1839.hasCapitalLocationOrdinal = seventhAndFinalLocation
    capitalSelection1839.isFinal = True
    waterlooIncorporation.toPlace = [austin]
    waterlooIncorporation.resultedInName = waterlooName
    austinRenaming.toPlace = [austin]
    austinRenaming.resultedInName = austinName
    austinRenaming.namedInHonorOf = stephenFAustin

    lamarVisit.ledTo = [capitalRelocationProposal]
    capitalRelocationProposal.ledTo = [capitalSelection1839]
    capitalSelection1839.ledTo = [waterlooIncorporation, austinRenaming]
    waterlooIncorporation.ledTo = [austinRenaming]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
