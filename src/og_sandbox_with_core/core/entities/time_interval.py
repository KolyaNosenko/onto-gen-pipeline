"""TimeInterval — direct subclass of TemporalRegion."""

from og_sandbox_with_core.core.ontology import core
from og_sandbox_with_core.core.entities.temporal_region import TemporalRegion


with core:

    class TimeInterval(TemporalRegion):
        """
        A Time Interval is a temporal region which is an interval or a
        sum of intervals. A Time Interval can be atomic, i.e.,
        instantaneous. (examples: the first second of your life,  the
        Cretaceous time period, the time interval of all winters of the
        third millennium).
        """

    TimeInterval.label = ["Time Interval"]


__all__ = ["TimeInterval"]
