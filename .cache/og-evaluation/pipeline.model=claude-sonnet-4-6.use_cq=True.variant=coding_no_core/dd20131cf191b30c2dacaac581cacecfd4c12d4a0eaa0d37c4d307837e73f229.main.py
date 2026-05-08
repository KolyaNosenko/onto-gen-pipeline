"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

Here are the competency questions derived from the document:

1. What was the original name of the city of Austin, Texas?
2. In which county is Austin, Texas located?
3. Who proposed relocating the capital of the Republic of Texas to the area that became Austin?
4. What position did Mirabeau B. Lamar hold in the Republic of Texas?
5. What activity was Mirabeau B. Lamar engaged in when he visited the area between 1837 and 1838?
6. Where was the capital of the Republic of Texas located before it was moved?
7. On which river bank was the proposed new capital site situated?
8. What is the present-day landmark near the original capital site on the Colorado River?
9. In what year was the site officially chosen as the capital of the Republic of Texas?
10. What number location was this in the sequence of capital sites for the Republic of Texas?
11. After whom was the city of Austin named?
12. What was Stephen F. Austin's title and role in the Republic of Texas?
13. What name was the city incorporated under before being renamed Austin?
14. Why was the name changed from Waterloo to Austin?
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
    # --- Entity classes ---
    class Place(Thing): pass
    class City(Place): pass
    class State(Place): pass
    class County(Place): pass
    class GeographicFeature(Place): pass
    class River(GeographicFeature): pass
    class Landmark(Place): pass
    class Bridge(Landmark): pass
    class PoliticalEntity(Thing): pass
    class Republic(PoliticalEntity): pass
    class Person(Thing): pass
    class GovernmentPosition(Thing): pass
    class Expedition(Thing): pass

    # --- Object properties ---
    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [Place]
        range  = [Place]

    class capitalOf(ObjectProperty):
        domain = [City]
        range  = [PoliticalEntity]

    class formerCapitalOf(ObjectProperty):
        domain = [City]
        range  = [PoliticalEntity]

    class heldPosition(ObjectProperty):
        domain = [Person]
        range  = [GovernmentPosition]

    class positionIn(ObjectProperty):
        domain = [GovernmentPosition]
        range  = [PoliticalEntity]

    class proposedRelocationOf(ObjectProperty):
        domain = [Person]
        range  = [City]

    class situatedOnBankOf(ObjectProperty):
        domain = [Place]
        range  = [River]

    class nearLandmark(ObjectProperty):
        domain = [Place]
        range  = [Landmark]

    class namedInHonorOf(ObjectProperty):
        domain = [City]
        range  = [Person]

    class conducedExpedition(ObjectProperty):
        domain = [Person]
        range  = [Expedition]

    # --- Data properties ---
    class originalName(DataProperty, FunctionalProperty):
        domain = [City]
        range  = [str]

    class honorificTitle(DataProperty, FunctionalProperty):
        domain = [Person]
        range  = [str]

    class expeditionStartYear(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range  = [int]

    class expeditionEndYear(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range  = [int]

    class expeditionType(DataProperty, FunctionalProperty):
        domain = [Expedition]
        range  = [str]

    class capitalSelectionYear(DataProperty, FunctionalProperty):
        domain = [City]
        range  = [int]

    class capitalSequenceNumber(DataProperty, FunctionalProperty):
        domain = [City]
        range  = [int]

    class bankSide(DataProperty, FunctionalProperty):
        domain = [Place]
        range  = [str]

    class geographicRegion(DataProperty, FunctionalProperty):
        domain = [Place]
        range  = [str]

    class positionTitle(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range  = [str]

    class positionOrder(DataProperty, FunctionalProperty):
        domain = [GovernmentPosition]
        range  = [int]

    # --- Individuals ---

    # Places
    TexasState = State("TexasState")
    TexasState.label = "Texas"

    TravisCounty = County("TravisCounty")
    TravisCounty.label = "Travis County"
    TravisCounty.geographicRegion = "central"
    TravisCounty.locatedIn = [TexasState]

    ColoradoRiver = River("ColoradoRiver")
    ColoradoRiver.label = "Colorado River"

    AnnWRichardsCongressAvenueBridge = Bridge("AnnWRichardsCongressAvenueBridge")
    AnnWRichardsCongressAvenueBridge.label = "Ann W. Richards Congress Avenue Bridge"

    HoustonCity = City("HoustonCity")
    HoustonCity.label = "Houston"

    AustinTexas = City("AustinTexas")
    AustinTexas.label = "Austin, Texas"
    AustinTexas.originalName = "Waterloo"
    AustinTexas.capitalSelectionYear = 1839
    AustinTexas.capitalSequenceNumber = 7
    AustinTexas.bankSide = "north"
    AustinTexas.locatedIn = [TravisCounty]
    AustinTexas.situatedOnBankOf = [ColoradoRiver]
    AustinTexas.nearLandmark = [AnnWRichardsCongressAvenueBridge]

    # Political entity
    RepublicOfTexas = Republic("RepublicOfTexas")
    RepublicOfTexas.label = "Republic of Texas"

    AustinTexas.capitalOf = [RepublicOfTexas]
    HoustonCity.formerCapitalOf = [RepublicOfTexas]

    # Government positions
    VicePresidentPosition = GovernmentPosition("VicePresidentPosition")
    VicePresidentPosition.label = "Vice President"
    VicePresidentPosition.positionTitle = "Vice President"
    VicePresidentPosition.positionIn = [RepublicOfTexas]

    SecretaryOfStatePosition = GovernmentPosition("SecretaryOfStatePosition")
    SecretaryOfStatePosition.label = "Secretary of State"
    SecretaryOfStatePosition.positionTitle = "Secretary of State"
    SecretaryOfStatePosition.positionOrder = 1
    SecretaryOfStatePosition.positionIn = [RepublicOfTexas]

    # Persons
    MirabeauBLamar = Person("MirabeauBLamar")
    MirabeauBLamar.label = "Mirabeau B. Lamar"
    MirabeauBLamar.heldPosition = [VicePresidentPosition]
    MirabeauBLamar.proposedRelocationOf = [AustinTexas]

    StephenFAustin = Person("StephenFAustin")
    StephenFAustin.label = "Stephen F. Austin"
    StephenFAustin.honorificTitle = "Father of Texas"
    StephenFAustin.heldPosition = [SecretaryOfStatePosition]

    AustinTexas.namedInHonorOf = [StephenFAustin]

    # Expedition
    BuffaloHuntingExpedition = Expedition("BuffaloHuntingExpedition")
    BuffaloHuntingExpedition.label = "buffalo-hunting expedition"
    BuffaloHuntingExpedition.expeditionType = "buffalo-hunting"
    BuffaloHuntingExpedition.expeditionStartYear = 1837
    BuffaloHuntingExpedition.expeditionEndYear = 1838

    MirabeauBLamar.conducedExpedition = [BuffaloHuntingExpedition]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
