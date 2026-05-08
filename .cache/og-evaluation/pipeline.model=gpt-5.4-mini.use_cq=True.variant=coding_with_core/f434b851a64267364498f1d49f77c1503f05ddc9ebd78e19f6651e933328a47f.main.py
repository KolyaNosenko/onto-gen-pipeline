"""
=== TASK INPUT ===
Source text:
Waterloo was the original name for the city of Austin , Texas , located in Travis County in the central part of the state . After Republic of Texas Vice President Mirabeau B. Lamar visited the area during a buffalo - hunting expedition between 1837 and 1838 , he proposed that the republic 's capital , then located in Houston , be relocated to an area situated on the north bank of the Colorado River near the present - day Ann W. Richards Congress Avenue Bridge in what is now central Austin . In 1839 , the site was officially chosen as the seventh and final location for the capital of the Republic of Texas . It was incorporated under the name " Waterloo " . Shortly thereafter , the name was changed to Austin in honor of Stephen F. Austin , the " Father of Texas " and the republic 's first secretary of state .

1. What was the original name of the city of Austin, Texas?
2. In which county is Austin, Texas located?
3. In what part of Texas is Austin located?
4. Who proposed relocating the capital of the Republic of Texas to the area that became Austin?
5. When did Mirabeau B. Lamar visit the area during the buffalo-hunting expedition?
6. From which city was the capital of the Republic of Texas proposed to be relocated?
7. On which riverbank was the proposed capital site located?
8. Near which landmark was the proposed capital site situated?
9. In what year was the site officially chosen as the capital of the Republic of Texas?
10. What position in the sequence of capital locations did the site hold?
11. Under what name was the city incorporated?
12. What was the city’s name changed to shortly after incorporation?
13. In honor of whom was Waterloo renamed Austin?
14. What title is Stephen F. Austin known by?
15. What role did Stephen F. Austin hold in the Republic of Texas?
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
    Abstract,
    Event,
    PhysicalObject,
    SocialAgent,
    SocialObject,
    Society,
    SpaceRegion,
    TimeInterval,
)


with core:
    class Person(SocialAgent):
        pass

    class City(SocialObject):
        pass

    class County(SocialObject):
        pass

    class State(SocialObject):
        pass

    class Republic(Society):
        pass

    class River(PhysicalObject):
        pass

    class Bridge(PhysicalObject):
        pass

    class Area(SpaceRegion):
        pass

    class Site(Area):
        pass

    class RiverBank(Area):
        pass

    class Year(TimeInterval):
        pass

    class Name(Abstract):
        pass

    class Title(Abstract):
        pass

    class PoliticalOffice(Abstract):
        pass

    class OrdinalPosition(Abstract):
        pass

    class BuffaloHuntingExpedition(Event):
        pass

    class CapitalRelocationProposal(Event):
        pass

    class locatedIn(ObjectProperty, TransitiveProperty):
        domain = [SocialObject, PhysicalObject, SpaceRegion]
        range = [SocialObject, PhysicalObject, SpaceRegion]

    class originalName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Name]

    class incorporatedUnderName(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Name]

    class visitedDuring(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [TimeInterval]

    class visitedArea(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Site]

    class proposedRelocationFrom(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [City]

    class proposedRelocationTo(ObjectProperty, FunctionalProperty):
        domain = [Person]
        range = [Site]

    class situatedOn(ObjectProperty, FunctionalProperty):
        domain = [Site]
        range = [RiverBank]

    class situatedNear(ObjectProperty, FunctionalProperty):
        domain = [Site]
        range = [Bridge]

    class officiallyChosenIn(ObjectProperty, FunctionalProperty):
        domain = [Site]
        range = [TimeInterval]

    class hasSequencePosition(ObjectProperty, FunctionalProperty):
        domain = [Site]
        range = [OrdinalPosition]

    class hasStartYear(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class hasEndYear(ObjectProperty, FunctionalProperty):
        domain = [TimeInterval]
        range = [Year]

    class renamedInHonorOf(ObjectProperty, FunctionalProperty):
        domain = [City]
        range = [Person]

    class hasHonorificTitle(ObjectProperty):
        domain = [Person]
        range = [Title]

    class heldOffice(ObjectProperty):
        domain = [Person]
        range = [PoliticalOffice]

    class officeOf(ObjectProperty, FunctionalProperty):
        domain = [PoliticalOffice]
        range = [Republic]

    class ofRiver(ObjectProperty, FunctionalProperty):
        domain = [RiverBank]
        range = [River]

    AustinCity = City("AustinCity")
    AustinCity.label = "Austin"

    WaterlooName = Name("WaterlooName")
    WaterlooName.label = "Waterloo"

    TravisCounty = County("TravisCounty")
    TravisCounty.label = "Travis County"

    TexasState = State("TexasState")
    TexasState.label = "Texas"

    CentralPartOfTexas = Area("CentralPartOfTexas")
    CentralPartOfTexas.label = "central part of the state"

    CentralAustin = Area("CentralAustin")
    CentralAustin.label = "what is now central Austin"

    RepublicOfTexas = Republic("RepublicOfTexas")
    RepublicOfTexas.label = "Republic of Texas"

    MirabeauBLamar = Person("MirabeauBLamar")
    MirabeauBLamar.label = "Mirabeau B. Lamar"

    RepublicOfTexasVicePresident = PoliticalOffice("RepublicOfTexasVicePresident")
    RepublicOfTexasVicePresident.label = "Republic of Texas Vice President"

    HoustonCity = City("HoustonCity")
    HoustonCity.label = "Houston"

    ColoradoRiver = River("ColoradoRiver")
    ColoradoRiver.label = "Colorado River"

    NorthBankOfColoradoRiver = RiverBank("NorthBankOfColoradoRiver")
    NorthBankOfColoradoRiver.label = "north bank of the Colorado River"

    AnnWRichardsCongressAvenueBridge = Bridge("AnnWRichardsCongressAvenueBridge")
    AnnWRichardsCongressAvenueBridge.label = "Ann W. Richards Congress Avenue Bridge"

    ProposedCapitalSite = Site("ProposedCapitalSite")
    ProposedCapitalSite.label = "the area situated on the north bank of the Colorado River near the present-day Ann W. Richards Congress Avenue Bridge in what is now central Austin"

    Year1837 = Year("Year1837")
    Year1837.label = "1837"

    Year1838 = Year("Year1838")
    Year1838.label = "1838"

    Between1837And1838 = TimeInterval("Between1837And1838")
    Between1837And1838.label = "between 1837 and 1838"
    Between1837And1838.hasStartYear = Year1837
    Between1837And1838.hasEndYear = Year1838

    Year1839 = Year("Year1839")
    Year1839.label = "1839"

    SeventhAndFinalLocation = OrdinalPosition("SeventhAndFinalLocation")
    SeventhAndFinalLocation.label = "the seventh and final location"

    StephenFAustin = Person("StephenFAustin")
    StephenFAustin.label = "Stephen F. Austin"

    FatherOfTexas = Title("FatherOfTexas")
    FatherOfTexas.label = "Father of Texas"

    FirstSecretaryOfStateOffice = PoliticalOffice("FirstSecretaryOfStateOffice")
    FirstSecretaryOfStateOffice.label = "first secretary of state"

    AustinCity.locatedIn.append(TravisCounty)
    AustinCity.locatedIn.append(CentralPartOfTexas)
    AustinCity.locatedIn.append(TexasState)
    TravisCounty.locatedIn.append(TexasState)
    CentralPartOfTexas.locatedIn.append(TexasState)
    CentralAustin.locatedIn.append(AustinCity)
    HoustonCity.locatedIn.append(TexasState)
    AnnWRichardsCongressAvenueBridge.locatedIn.append(CentralAustin)
    ProposedCapitalSite.locatedIn.append(CentralAustin)

    NorthBankOfColoradoRiver.ofRiver = ColoradoRiver
    ProposedCapitalSite.situatedOn = NorthBankOfColoradoRiver
    ProposedCapitalSite.situatedNear = AnnWRichardsCongressAvenueBridge
    ProposedCapitalSite.officiallyChosenIn = Year1839
    ProposedCapitalSite.hasSequencePosition = SeventhAndFinalLocation

    MirabeauBLamar.visitedDuring = Between1837And1838
    MirabeauBLamar.visitedArea = ProposedCapitalSite
    MirabeauBLamar.proposedRelocationFrom = HoustonCity
    MirabeauBLamar.proposedRelocationTo = ProposedCapitalSite
    MirabeauBLamar.heldOffice.append(RepublicOfTexasVicePresident)
    RepublicOfTexasVicePresident.officeOf = RepublicOfTexas

    AustinCity.originalName = WaterlooName
    AustinCity.incorporatedUnderName = WaterlooName
    AustinCity.renamedInHonorOf = StephenFAustin

    StephenFAustin.hasHonorificTitle.append(FatherOfTexas)
    StephenFAustin.heldOffice.append(FirstSecretaryOfStateOffice)
    FirstSecretaryOfStateOffice.officeOf = RepublicOfTexas


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
