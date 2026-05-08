"""
=== TASK INPUT ===
Source text:
Joos van Cleve (; also Joos van der Beke ; c. 1485 – 1540/1541 ) was a painter active in Antwerp around 1511 to 1540 . He is known for combining traditional Netherlandish painting techniques with influences of more contemporary Renaissance painting styles . An active member and co - deacon of the Guild of Saint Luke of Antwerp , he is known mostly for his religious works and portraits of royalty . As a skilled technician , his art shows sensitivity to color and a unique solidarity of figures . He was one of the first to introduce broad landscapes in the backgrounds of his paintings , which would become a popular technique of sixteenth century northern Renaissance paintings . He was the father of Cornelis van Cleve ( 1520 - 1567 ) who also became a painter . Cornelis became mentally ill during a residence in England and was therefore referred to as ' Sotte Cleef ' ( mad Cleef ) .

1. Who was Joos van Cleve and what were his primary artistic contributions?
2. What painting techniques did Joos van Cleve combine in his work?
3. In which city was Joos van Cleve active as a painter, and during what time period?
4. What roles did Joos van Cleve hold in the Guild of Saint Luke of Antwerp?
5. What types of subjects did Joos van Cleve primarily paint?
6. What artistic innovation did Joos van Cleve introduce regarding landscape backgrounds?
7. Who was Joos van Cleve's son and what was his profession?
8. Why was Cornelis van Cleve referred to as "Sotte Cleef"?
9. What distinguishes Joos van Cleve's artistic style from his contemporaries?
10. How did Joos van Cleve influence sixteenth century northern Renaissance painting?
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
    class Painter(Person): pass
    class Place(Thing): pass
    class City(Place): pass
    class Guild(Thing): pass
    class PaintingTechnique(Thing): pass
    class PaintingStyle(Thing): pass
    class Subject(Thing): pass
    class Role(Thing): pass
    
    # Role specializations
    class CoDeacon(Role): pass
    
    # Properties for people
    class birthYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [int]
    
    class deathYear(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [int]
    
    class residedIn(ObjectProperty):
        domain = [Person]
        range = [Place]
    
    class becameMentallyIll(DataProperty, FunctionalProperty):
        domain = [Person]
        range = [bool]
    
    # Properties for painters
    class activeIn(ObjectProperty):
        domain = [Painter]
        range = [Place]
    
    class activeFrom(DataProperty, FunctionalProperty):
        domain = [Painter]
        range = [int]
    
    class activeTo(DataProperty, FunctionalProperty):
        domain = [Painter]
        range = [int]
    
    class memberOf(ObjectProperty):
        domain = [Painter]
        range = [Guild]
    
    class hasRoleIn(ObjectProperty):
        domain = [Painter]
        range = [Role]
    
    class combinedTechniques(ObjectProperty):
        domain = [Painter]
        range = [PaintingTechnique]
    
    class combinedStyles(ObjectProperty):
        domain = [Painter]
        range = [PaintingStyle]
    
    class paintsPrimaryly(ObjectProperty):
        domain = [Painter]
        range = [Subject]
    
    class introduced(DataProperty):
        domain = [Painter]
        range = [str]
    
    class hasArtisticQuality(DataProperty):
        domain = [Painter]
        range = [str]
    
    class hasChild(ObjectProperty):
        domain = [Painter]
        range = [Painter]
    
    # Instances - Painters
    joos = Painter("JoosVanCleve")
    joos.label = ["Joos van Cleve", "Joos van der Beke"]
    joos.activeFrom = 1511
    joos.activeTo = 1540
    joos.birthYear = 1485
    
    cornelis = Painter("CornelisVanCleve")
    cornelis.label = ["Cornelis van Cleve", "Sotte Cleef"]
    cornelis.birthYear = 1520
    cornelis.deathYear = 1567
    cornelis.becameMentallyIll = True
    
    # Instances - Places
    antwerp = City("Antwerp")
    antwerp.label = "Antwerp"
    
    england = Place("England")
    england.label = "England"
    
    # Instances - Guild
    guild = Guild("GuildOfSaintLukeOfAntwerp")
    guild.label = "Guild of Saint Luke of Antwerp"
    
    # Instances - Techniques and Styles
    netherlandish_tech = PaintingTechnique("NetherlandishTechnique")
    netherlandish_tech.label = "Netherlandish painting techniques"
    
    renaissance_style = PaintingStyle("RenaissancePainting")
    renaissance_style.label = "Renaissance painting styles"
    
    # Instances - Subjects
    religious = Subject("ReligiousWorks")
    religious.label = "Religious works"
    
    royalty_portraits = Subject("RoyaltyPortraits")
    royalty_portraits.label = "Portraits of royalty"
    
    # Instances - Roles
    co_deacon = CoDeacon("CoDeaconRole")
    co_deacon.label = "Co-Deacon"
    
    # Relationships for Joos
    joos.activeIn = [antwerp]
    joos.memberOf = [guild]
    joos.hasRoleIn = [co_deacon]
    joos.combinedTechniques = [netherlandish_tech]
    joos.combinedStyles = [renaissance_style]
    joos.paintsPrimaryly = [religious, royalty_portraits]
    joos.introduced = ["broad landscapes in backgrounds of paintings"]
    joos.hasArtisticQuality = ["sensitivity to color", "unique solidarity of figures"]
    joos.hasChild = [cornelis]
    
    # Relationships for Cornelis
    cornelis.activeIn = [antwerp]
    cornelis.residedIn = [england]


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
