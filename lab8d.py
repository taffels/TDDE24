# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

###SKALL EGENTLIGEN TAS BORT MOT SLUTET, ENBART HÄR NU:
from lab8b import *
from cal_ui import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """ Finds free timespans given a CalendarDay, start and end time """
    
    ensure_type(cal_day, CalendarDay)
    ensure_type(start, Time)
    ensure_type(end, Time)


    def add_free_spans(apps_list: List[Appointment], span_start, span_end):
        """ Adds the free spans between appointments """
       
        if not apps_list:
            return []
        
        app_start = ts_start(app_span(apps_list[0]))
        app_end = ts_end(app_span(apps_list[0]))
        

        if time_precedes_or_equals(span_start, app_start):
            if not time_equals(span_start, app_start):
                return [new_time_span(span_start, app_start)] + add_free_spans(apps_list, app_end, span_end)
            
            if time_equals(span_start, app_start):
                if time_precedes_or_equals(span_end, app_end): # kollar om appointment startar och slutar samtidigt som spannet
                    return []
                return add_free_spans(apps_list, app_end, span_end)
            
        elif time_precedes(app_start, span_start):
            if not time_precedes(app_end, span_start): # Om inte app end slutar innan spannet börjar
                span_start = app_end

            if apps_list[1:]:

                next_app_start = ts_start(app_span(apps_list[1]))
                next_app_end = ts_end(app_span(apps_list[1]))
                
                if time_equals(app_end, next_app_start):
                    return add_free_spans(apps_list[1:], next_app_end, span_end)
                    
                if time_precedes(span_end, next_app_start):
                    return [new_time_span(span_start, span_end)]

                if time_precedes_or_equals(span_end, next_app_end):
                    return [new_time_span(span_start, next_app_start)]

                return [new_time_span(span_start, next_app_start)] + add_free_spans(apps_list[1:], next_app_end, span_end)
        
            else:
                if time_precedes(span_end, app_end):
                    return []
                
                return [new_time_span(span_start, span_end)]


    if time_precedes_or_equals(end, start):
        return new_time_span_seq()
    
    if not is_booked_during(cal_day, new_time_span(start, end)):
        return new_time_span_seq([new_time_span(start, end)])
    

    return new_time_span_seq(add_free_spans(cal_day.appointments, start, end))

     
     
def show_free(cal_name: str, d: int, m: str, start: str, end: str):
    """ Prints free timespans on a given day with a set start and end time """
    
    day = new_day(d)
    mon = new_month(m)

    # Ta fram rätt cal_day från cal_name mha. tidigare skapade datatyper
    cal_year = get_calendar(cal_name)
    cal_mon = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_mon, day)

    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)

    if time_precedes_or_equals(end_time, start_time):
        return new_time_span_seq()
    
    else:
        show_time_spans(free_spans(cal_day, start_time, end_time))
