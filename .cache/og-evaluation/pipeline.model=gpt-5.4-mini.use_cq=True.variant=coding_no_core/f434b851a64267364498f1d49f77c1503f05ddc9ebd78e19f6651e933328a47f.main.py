"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

1. What was the original name of the city of Austin, Texas?
2. In which county is Austin located?
3. In which part of Texas is Austin located?
4. Who visited the area during the buffalo-hunting expedition between 1837 and 1838?
5. What proposal did Mirabeau B. Lamar make after visiting the area?
6. Where was the capital of the Republic of Texas located before it was proposed to be moved?
7. To what area was the capital of the Republic of Texas proposed to be relocated?
8. On what river is the proposed capital site situated?
9. Near what present-day landmark was the proposed capital site located?
10. In what year was the site officially chosen as the capital location?
11. What was the seventh and final location for the capital of the Republic of Texas?
12. Under what name was the city incorporated in 1839?
13. After whom was the name of Waterloo changed to Austin?
14. What was Stephen F. Austin known as?
15. What position did Stephen F. Austin hold in the Republic of Texas?
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
    class Entity(Thing):
        pass

    class Place(Entity):
        pass

    class City(Place):
        pass

    class County(Place):
        pass

    class State(Place):
        pass

    class Republic(Place):
        pass

    class River(Place):
        pass

    class Bridge(Place):
        pass

    class Site(Place):
        pass

    class Region(Place):
        pass

    class Person(Entity):
        pass

    class Event(Entity):
        pass

    class Expedition(Event):
        pass

    class Name(Entity):
        pass

    class Role(Entity):
        pass

    class Office(Role):
        pass

    class Title(Role):
        pass

    class locatedIn(ObjectProperty):
        domain = [Place]
        range = [Place]

    class partOf(ObjectProperty):
        domain = [Place]
        range = [Place]

    class originalName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Name]

    class incorporatedUnderName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Name]

    class namedAfter(ObjectProperty):
        domain = [City]
        range = [Person]

    class situatedOn(ObjectProperty):
        domain = [Place]
        range = [River]

    class nearLandmark(ObjectProperty):
        domain = [Place]
        range = [Bridge]

    class capitalLocationOf(ObjectProperty):
        domain = [Place]
        range = [Republic]

    class visitedDuring(ObjectProperty):
        domain = [Person]
        range = [Expedition]

    class visitedArea(ObjectProperty):
        domain = [Person]
        range = [Place]

    class proposedCapitalRelocationTo(ObjectProperty):
        domain = [Person]
        range = [Place]

    class holdsOffice(ObjectProperty):
        domain = [Person]
        range = [Office]

    class knownAs(ObjectProperty):
        domain = [Person]
        range = [Title]

    class officeOf(ObjectProperty, FunctionalProperty):
        domain = [Office]
        range = [Republic]

    class startYear(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range = [int]

    class endYear(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range = [int]

    class chosenInYear(DataProperty, FunctionalProperty):
        domain = [Place]
        range = [int]

    class locationOrder(DataProperty, FunctionalProperty):
        domain = [Place]
        range = [int]

    class isFinalLocation(DataProperty, FunctionalProperty):
        domain = [Place]
        range = [bool]

    AustinCity = City("AustinCity")
    AustinCity.label = "Austin"

    WaterlooName = Name("WaterlooName")
    WaterlooName.label = "Waterloo"

    TexasState = State("TexasState")
    TexasState.label = "Texas"

    TravisCounty = County("TravisCounty")
    TravisCounty.label = "Travis County"

    CentralPartOfTheState = Region("CentralPartOfTheState")
    CentralPartOfTheState.label = "the central part of the state"

    RepublicOfTexas = Republic("RepublicOfTexas")
    RepublicOfTexas.label = "Republic of Texas"

    MirabeauBLamar = Person("MirabeauBLamar")
    MirabeauBLamar.label = "Mirabeau B. Lamar"

    BuffaloHuntingExpedition = Expedition("BuffaloHuntingExpedition")
    BuffaloHuntingExpedition.label = "buffalo-hunting expedition between 1837 and 1838"
    BuffaloHuntingExpedition.startYear = 1837
    BuffaloHuntingExpedition.endYear = 1838

    HoustonCity = City("HoustonCity")
    HoustonCity.label = "Houston"
    HoustonCity.capitalLocationOf = [RepublicOfTexas]

    ColoradoRiver = River("ColoradoRiver")
    ColoradoRiver.label = "Colorado River"

    AnnWRichardsCongressAvenueBridge = Bridge("AnnWRichardsCongressAvenueBridge")
    AnnWRichardsCongressAvenueBridge.label = "Ann W. Richards Congress Avenue Bridge"

    StephenFAustin = Person("StephenFAustin")
    StephenFAustin.label = "Stephen F. Austin"

    FatherOfTexas = Title("FatherOfTexas")
    FatherOfTexas.label = "Father of Texas"

    VicePresidentOfRepublicOfTexas = Office("VicePresidentOfRepublicOfTexas")
    VicePresidentOfRepublicOfTexas.label = "Vice President"
    VicePresidentOfRepublicOfTexas.officeOf = RepublicOfTexas

    FirstSecretaryOfStateOfRepublicOfTexas = Office("FirstSecretaryOfStateOfRepublicOfTexas")
    FirstSecretaryOfStateOfRepublicOfTexas.label = "first secretary of state"
    FirstSecretaryOfStateOfRepublicOfTexas.officeOf = RepublicOfTexas

    AustinCity.locatedIn = [TravisCounty, CentralPartOfTheState, TexasState]
    CentralPartOfTheState.partOf = [TexasState]
    AustinCity.originalName = WaterlooName
    AustinCity.incorporatedUnderName = WaterlooName
    AustinCity.namedAfter = [StephenFAustin]
    AustinCity.situatedOn = [ColoradoRiver]
    AustinCity.nearLandmark = [AnnWRichardsCongressAvenueBridge]
    AustinCity.capitalLocationOf = [RepublicOfTexas]
    AustinCity.chosenInYear = 1839
    AustinCity.locationOrder = 7
    AustinCity.isFinalLocation = True

    MirabeauBLamar.visitedDuring = [BuffaloHuntingExpedition]
    MirabeauBLamar.visitedArea = [AustinCity]
    MirabeauBLamar.proposedCapitalRelocationTo = [AustinCity]
    MirabeauBLamar.holdsOffice = [VicePresidentOfRepublicOfTexas]

    StephenFAustin.knownAs = [FatherOfTexas]
    StephenFAustin.holdsOffice = [FirstSecretaryOfStateOfRepublicOfTexas]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
