# This code violates abstraction layers, and should be reimplemented in lab 8A.
from cal_abstraction import *


def ts_equals(ts1: TimeSpan, ts2: TimeSpan):
    """Return true iff the two given TimeSpans are equal."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)

    return (time_equals(ts_start(ts1), ts_start(ts2)) and 
            time_equals(ts_end(ts1), ts_end(ts2)))


def ts_overlap(ts1: TimeSpan, ts2: TimeSpan) -> bool:
    """Return true iff the two given TimeSpans overlap."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)

    return (
            time_precedes(ts_start(ts1), ts_end(ts2)) and
            time_precedes(ts_start(ts2), ts_end(ts1))
    )


def ts_overlapping_part(ts1: TimeSpan, ts2: TimeSpan) -> TimeSpan:
    """Return the overlapping part of two overlapping time spans,
    under the assumption that they really *are* overlapping."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ensure((ts1, ts2), lambda tup: ts_overlap(tup[0], tup[1]))


    min1 = max(hour_number(time_hour(ts_start(ts1))) * 60 + minute_number(time_minute(ts_start(ts1))),
               hour_number(time_hour(ts_start(ts2))) * 60 + minute_number(time_minute(ts_start(ts2))),
    )
    
    min2 = min(hour_number(time_hour(ts_end(ts1))) * 60 + minute_number(time_minute(ts_end(ts1))),
               hour_number(time_hour(ts_end(ts2))) * 60 + minute_number(time_minute(ts_end(ts2))),
    )
    
    return new_time_span(new_time(new_hour(min1 // 60), new_minute(min1 % 60)),
            new_time(new_hour(min2 // 60), new_minute(min2 % 60)))



def ts_duration(ts: TimeSpan) -> "Duration":
    """Return the duration (length) of a TimeSpan"""
    ensure_type(ts, TimeSpan)


    mins = (hour_number(time_hour(ts_end(ts))) * 60 + minute_number(time_minute(ts_end(ts))) - 
            hour_number(time_hour(ts_start(ts))) * 60 - minute_number(time_minute(ts_start(ts)))
    )

    return new_duration(new_hour(mins // 60), new_minute(mins % 60))
    


def duration_is_longer_or_equal(d1: Duration, d2: Duration):
    """
    Return true iff the first duration is longer than, or equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = hour_number(duration_hour(d1))
    hours2 = hour_number(duration_hour(d2))
    mins1 = minute_number(duration_minute(d1)) 
    mins2 = minute_number(duration_minute(d2)) 

    return (hours1, mins1) >= (hours2, mins2)


def duration_equals(d1: Duration, d2: Duration):
    """
    Return true iff the first duration is equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = hour_number(duration_hour(d1))
    hours2 = hour_number(duration_hour(d2))
    mins1 = minute_number(duration_minute(d1))
    mins2 = minute_number(duration_minute(d2))

    return (hours1, mins1) == (hours2, mins2)


if __name__ == "__main__":
    test_timespan_duration()