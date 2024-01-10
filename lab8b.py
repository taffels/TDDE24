# =========================================================================
# Type definition
# =========================================================================
from cal_abstraction import *
from cal_output import *
# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple('TimeSpanSeq', [("spans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.


def new_time_span_seq(spans: List[TimeSpan] = None) -> TimeSpanSeq:
    """ Creates a new time span """
    
    if spans is None:
        spans = []
    else:
        ensure_type(spans, List[TimeSpan])
    return TimeSpanSeq(spans)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """ Checks if time span sequence is empty """

    ensure_type(tss, TimeSpanSeq)
    return not tss.spans


def tss_plus_span(tss: TimeSpanSeq, new_span: TimeSpan) -> TimeSpanSeq:
    """ Adds time span to TimeSpanSeq in the right order """

    ensure_type(new_span, TimeSpan)
    ensure_type(tss, TimeSpanSeq)

    def add_ts(tss_list: List[TimeSpan]):
        if not tss_list or time_precedes(ts_start(new_span), ts_start(tss_list[0])):
            return [new_span] + tss_list
        else:
            return [tss_list[0]] + add_ts(tss_list[1:])

    return new_time_span_seq(add_ts(tss.spans))
   

def tss_iter_spans(tss: TimeSpanSeq):
    """ Iterates through time spans """

    ensure_type(tss, TimeSpanSeq)
    for span in tss.spans:
        yield span


def show_time_spans(tss: TimeSpanSeq):
    """ Shows each time span in TimeSpanSeq """

    ensure_type(tss, TimeSpanSeq)
    for span in tss_iter_spans(tss):
        show_ts(span)
        print()


def tss_keep_spans(tss, pred):
    """ Keeps time spans that satisfy pred """

    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)
    return result



""" Tests """

min1 = 0            # 00:00
min2 = 420          # 07:00

min3 = 0            # 00:00
min4 = 70           # 01:10 

min5 = 1080         # 18:00
min6 = 1450         # 24:10 eller 00:10 ?


time = new_time_span(Time(Hour(min1 // 60), Minute(min1 % 60)), Time(Hour(min2 // 60), Minute(min2 % 60)))

time2 = new_time_span(Time(Hour(min3 // 60), Minute(min3 % 60)), Time(Hour(min4 // 60), Minute(min4 % 60)))

time3= new_time_span(Time(Hour(min5 // 60), Minute(min5 % 60)), Time(Hour(min6 // 60), Minute(min6 % 60)))


# timespanseq = new_time_span_seq()

# print(tss_is_empty(timespanseq))

# timespanseq = tss_plus_span(timespanseq, time2)

# timespanseq = tss_plus_span(timespanseq, time)

# timespanseq = tss_plus_span(timespanseq, time3)

# show_time_spans(timespanseq)

# print(tss_is_empty(timespanseq))