"""
=== TASK INPUT ===
Source text:
Georgy Fotev ( ) ( born August 24 , 1941 ) is a Bulgarian sociologist . His scientific works are in the areas of theory and history of sociology and the disciplinary fields of modern sociology . The focus of the research interests of G.Fotev is the nature of sociology as a multiple paradigm science . Another major theme in the works of Georgy Fotev is the dialogue as a base and horizon of multiple paradigm sociology . Georgy Fotev has publications in the fields of historical sociology , sociology of politics , ethnosociology , the crisis of legitimacy , sociology of values , etc . His books " The long night of communism in Bulgaria " and " Bulgarian melancholy " throw light on the dramatic fate of the Bulgarian national society . Georgy Fotev was Minister of Education and Science ( 1991 - 1992 ) . He is professor emeritus of New Bulgarian University . In 2003 he was awarded the Distinguished Service Award from the American University in Bulgaria .

1. What is Georgy Fotev's birth date and nationality?
2. What are the main areas of scientific research for Georgy Fotev?
3. What is Georgy Fotev's perspective on sociology as a discipline?
4. What role does dialogue play in Georgy Fotev's sociological work?
5. What specific fields of sociology has Georgy Fotev published work in?
6. What are the titles and themes of Georgy Fotev's notable books?
7. What government position did Georgy Fotev hold and during what period?
8. What is Georgy Fotev's current academic affiliation?
9. What awards has Georgy Fotev received and when?
10. Which institution awarded Georgy Fotev the Distinguished Service Award and in what year?
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

from datetime import date
from og_sandbox_with_core.core.entities import SocialAgent, NonAgentivePhysicalObject, Society


with core:
    # Entity Classes
    class Sociologist(SocialAgent):
        """A scholar and professional in the field of sociology."""
        pass
    
    class Book(NonAgentivePhysicalObject):
        """A published written work in book form."""
        pass
    
    class University(Society):
        """An academic institution for higher learning."""
        pass
    
    # Data Properties
    class birthDate(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [date]
    
    class birthNationality(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [str]
    
    class bookTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]
    
    class governmentPosition(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [str]
    
    class positionStartYear(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [int]
    
    class positionEndYear(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [int]
    
    class academicStatus(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [str]
    
    class awardName(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [str]
    
    class awardYear(DataProperty, FunctionalProperty):
        domain = [SocialAgent]
        range = [int]
    
    class researchField(DataProperty):
        domain = [SocialAgent]
        range = [str]
    
    class publicationField(DataProperty):
        domain = [SocialAgent]
        range = [str]
    
    # Object Properties
    class affiliatedWith(ObjectProperty):
        domain = [SocialAgent]
        range = [University]
    
    class awardedBy(ObjectProperty):
        domain = [SocialAgent]
        range = [University]
    
    class authored(ObjectProperty):
        domain = [SocialAgent]
        range = [Book]
    
    # Named Instances
    georgeFotev = Sociologist("GeorgyFotev")
    georgeFotev.label = "Georgy Fotev"
    georgeFotev.birthDate = date(1941, 8, 24)
    georgeFotev.birthNationality = "Bulgarian"
    georgeFotev.governmentPosition = "Minister of Education and Science"
    georgeFotev.positionStartYear = 1991
    georgeFotev.positionEndYear = 1992
    georgeFotev.academicStatus = "professor emeritus"
    georgeFotev.awardName = "Distinguished Service Award"
    georgeFotev.awardYear = 2003
    georgeFotev.researchField = [
        "theory and history of sociology",
        "modern sociology",
        "the nature of sociology as a multiple paradigm science",
        "dialogue as a base and horizon of multiple paradigm sociology"
    ]
    georgeFotev.publicationField = [
        "historical sociology",
        "sociology of politics",
        "ethnosociology",
        "crisis of legitimacy",
        "sociology of values"
    ]
    
    newBulgarianUniversity = University("NewBulgarianUniversity")
    newBulgarianUniversity.label = "New Bulgarian University"
    
    americanUniversityInBulgaria = University("AmericanUniversityInBulgaria")
    americanUniversityInBulgaria.label = "American University in Bulgaria"
    
    longNightOfCommunism = Book("LongNightOfCommunismInBulgaria")
    longNightOfCommunism.label = "The long night of communism in Bulgaria"
    longNightOfCommunism.bookTitle = "The long night of communism in Bulgaria"
    
    bulgarianMelancholy = Book("BulgarianMelancholy")
    bulgarianMelancholy.label = "Bulgarian melancholy"
    bulgarianMelancholy.bookTitle = "Bulgarian melancholy"
    
    # Relationships
    georgeFotev.affiliatedWith.append(newBulgarianUniversity)
    georgeFotev.awardedBy.append(americanUniversityInBulgaria)
    georgeFotev.authored.append(longNightOfCommunism)
    georgeFotev.authored.append(bulgarianMelancholy)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
