"""
=== TASK INPUT ===
Source text:
Milton is a town in the South Coast region of New South Wales , Australia , within the City of Shoalhaven . It was founded in 1860 , named after the property of post master George Knight and became an important regional centre during the 19th Century . Today , Milton remains one of the two main commercial centres of the Milton - Ulladulla district , with a population at the of 1,663 . It is a popular stopping place for travellers on the Princes Highway which runs through the centre of town . In recent years , Milton has undergone a resurgence largely influenced by the local tourism industry and an influx of residents to the district seeking a seachange . Several new housing estates are being developed on the fringes of the village and new boutique stores , cafes and bed and breakfast type businesses have located in the town .

1. What region is Milton located in?
2. In which state of Australia is Milton situated?
3. What local government area does Milton belong to?
4. When was Milton founded?
5. Who was Milton named after?
6. What was George Knight's occupation?
7. What was Milton's role during the 19th Century?
8. What is the population of Milton?
9. What are the two main commercial centres of the Milton-Ulladulla district?
10. Which highway runs through the centre of Milton?
11. What factors have contributed to Milton's recent resurgence?
12. What types of new businesses have been established in Milton?
13. What type of development is occurring on the fringes of Milton?
14. What is the primary industry influencing Milton's growth in recent years?
15. Why have new residents been moving to the Milton district?
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
    NonAgentiveSocialObject,
    AgentivePhysicalObject,
    NonAgentivePhysicalObject,
    Achievement,
    Process,
    TimeInterval,
    MentalObject,
)


with core:

    # ── Entity classes ────────────────────────────────────────────────────

    class GeographicArea(NonAgentiveSocialObject):
        """Any geographic or administrative area (region, town, state, …)."""

    class Town(GeographicArea):
        """A town or village."""

    class GeoRegion(GeographicArea):
        """A named geographic or administrative region."""

    class AustralianState(GeographicArea):
        """A state of Australia."""

    class Country(GeographicArea):
        """A sovereign country."""

    class LocalGovernmentArea(GeographicArea):
        """A local government area (city, shire, etc.)."""

    class District(GeographicArea):
        """A named district grouping one or more towns."""

    class Person(AgentivePhysicalObject):
        """A human individual."""

    class Occupation(NonAgentiveSocialObject):
        """A job title or profession."""

    class Highway(NonAgentivePhysicalObject):
        """A named road or highway."""

    class Industry(NonAgentiveSocialObject):
        """An industry sector."""

    class FoundingEvent(Achievement):
        """The (instantaneous) event of establishing a settlement."""

    class Business(NonAgentiveSocialObject):
        """A commercial business establishment."""

    class BoutiqueStore(Business):
        """A small, speciality retail store."""

    class Cafe(Business):
        """A café or coffee shop."""

    class BedAndBreakfast(Business):
        """A bed-and-breakfast accommodation business."""

    class HousingEstate(NonAgentivePhysicalObject):
        """A residential housing development."""

    class Resurgence(Process):
        """A revival or renewed growth of a town or area."""

    class InfluxOfResidents(Process):
        """A movement of new residents into an area."""

    class SeachangeSeeking(MentalObject):
        """The desire to leave city life for a quieter coastal lifestyle."""

    # ── Properties ───────────────────────────────────────────────────────

    class locatedIn(ObjectProperty, TransitiveProperty):
        """Geographic / administrative containment (transitive)."""
        domain = [GeographicArea]
        range  = [GeographicArea]

    class foundedIn(ObjectProperty, FunctionalProperty):
        """Links a town to the time interval of its founding."""
        domain = [Town]
        range  = [TimeInterval]

    class namedAfterPerson(ObjectProperty):
        """The person (or their estate) after whom a place was named."""
        domain = [Town]
        range  = [Person]

    class hadOccupation(ObjectProperty):
        """Links a person to their occupation."""
        domain = [Person]
        range  = [Occupation]

    class hasPopulation(DataProperty, FunctionalProperty):
        """Census / stated population count of an area."""
        domain = [GeographicArea]
        range  = [int]

    class traverses(ObjectProperty):
        """A highway runs through an area."""
        domain = [Highway]
        range  = [GeographicArea]

    class isCommercialCentreOf(ObjectProperty):
        """A town serves as a main commercial centre of a district."""
        domain = [Town]
        range  = [District]

    class influencedBy(ObjectProperty):
        """A resurgence is influenced by an industry or influx."""
        domain = [Resurgence]
        range  = [Industry, InfluxOfResidents]

    class hasResurgence(ObjectProperty):
        """Links a town to its resurgence process."""
        domain = [Town]
        range  = [Resurgence]

    class motivatedBy(ObjectProperty):
        """An influx of residents is motivated by a lifestyle desire."""
        domain = [InfluxOfResidents]
        range  = [SeachangeSeeking]

    class hasEstablishment(ObjectProperty):
        """A geographic area contains a business establishment."""
        domain = [GeographicArea]
        range  = [Business]

    class historicalRole(DataProperty):
        """A textual description of an area's historical function."""
        domain = [GeographicArea]
        range  = [str]

    # ── Named instances ───────────────────────────────────────────────────

    # Time intervals
    year_1860 = TimeInterval("Year_1860")
    year_1860.label = "1860"

    nineteenth_century = TimeInterval("Nineteenth_Century_interval")
    nineteenth_century.label = "19th Century"

    # Countries / states / regions
    australia = Country("Australia_inst")
    australia.label = "Australia"

    new_south_wales = AustralianState("New_South_Wales_inst")
    new_south_wales.label = "New South Wales"

    south_coast = GeoRegion("South_Coast_inst")
    south_coast.label = "South Coast"

    city_of_shoalhaven = LocalGovernmentArea("City_of_Shoalhaven_inst")
    city_of_shoalhaven.label = "City of Shoalhaven"

    milton_ulladulla_district = District("Milton_Ulladulla_District_inst")
    milton_ulladulla_district.label = "Milton-Ulladulla district"

    # Towns
    milton = Town("Milton_inst")
    milton.label = "Milton"

    ulladulla = Town("Ulladulla_inst")
    ulladulla.label = "Ulladulla"

    # People
    george_knight = Person("George_Knight_inst")
    george_knight.label = "George Knight"

    # Occupations
    post_master = Occupation("PostMaster_inst")
    post_master.label = "post master"

    # Highway
    princes_highway = Highway("Princes_Highway_inst")
    princes_highway.label = "Princes Highway"

    # Industry
    tourism_industry = Industry("Local_Tourism_Industry_inst")
    tourism_industry.label = "local tourism industry"

    # Resurgence
    milton_resurgence = Resurgence("Milton_Resurgence_inst")
    milton_resurgence.label = "Milton's resurgence"

    # ── Property assignments ──────────────────────────────────────────────

    # Geographic containment chain
    south_coast.locatedIn.append(new_south_wales)
    new_south_wales.locatedIn.append(australia)

    # Milton's geographic location (CQs 1–3)
    milton.locatedIn.append(south_coast)
    milton.locatedIn.append(city_of_shoalhaven)
    milton.locatedIn.append(milton_ulladulla_district)
    ulladulla.locatedIn.append(milton_ulladulla_district)

    # Founding year (CQ 4)
    milton.foundedIn = year_1860

    # Named after (CQ 5)
    milton.namedAfterPerson.append(george_knight)

    # George Knight's occupation (CQ 6)
    george_knight.hadOccupation.append(post_master)

    # Historical role during 19th Century (CQ 7)
    milton.historicalRole.append("important regional centre")

    # Population (CQ 8)
    milton.hasPopulation = 1663

    # Commercial centres of the district (CQ 9)
    milton.isCommercialCentreOf.append(milton_ulladulla_district)
    ulladulla.isCommercialCentreOf.append(milton_ulladulla_district)

    # Highway (CQ 10)
    princes_highway.traverses.append(milton)

    # Resurgence and influencing factors (CQs 11, 14)
    milton.hasResurgence.append(milton_resurgence)
    milton_resurgence.influencedBy.append(tourism_industry)


graph = default_world.as_rdflib_graph()
graph.serialize(destination="output.txt", format="turtle")
