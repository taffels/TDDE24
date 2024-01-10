from cal_abstraction import *
from cal_ui import *


def remove(cal_name: str, d: int, m: str, start: str):
    """ Overwrites appointment if a new appointment/ no appointment is booked/removed at an already booked time"""
   
    # Skapa day och mon för att få rätt datatyp
    day = new_day(d)
    mon = new_month(m)

    # Ta fram rätt cal_day från cal_name mha. tidigare skapade datatyper
    old_cal_year = get_calendar(cal_name)
    old_cal_mon = cy_get_month(mon, old_cal_year)
    old_cal_day = cm_get_day(old_cal_mon, day)

    start_time = new_time_from_string(start)


    appointments_list = new_app_list(old_cal_day, start_time)       # En lista med appointments utan den med given start tid
   
    if not is_booked_from(old_cal_day, start_time):                 # Kollar om det finns någon appointment med given starttid under kalenderdagen
        print("No removed appointments")
        
    else:
        print("Removed appointment")
        new_cal_day = new_calendar_day(day, appointments_list)      # Skapar en calenderdag med alla givna appointments från listan
        new_cal_mon = cm_plus_cd(old_cal_mon, new_cal_day)          # Replaces dem gamla kalenderdagen i kalendermånaden eftersom den redan finns
        new_cal_year = cy_plus_cm(old_cal_year, new_cal_mon)        # Replaces den gamla kalendermånaden i kalenderåret

        insert_calendar(cal_name, new_cal_year)

        
def new_app_list(cal_day: CalendarDay, start_time: Time)-> List:
    """ Returns a list of appointmets without the appointments with the given start time """

    ensure_type(cal_day, CalendarDay)
    ensure_type(start_time, Time)

    appointments = []

    if cd_is_empty(cal_day):
        print("No appointments at given day")
        return appointments

    for app in cd_iter_appointments(cal_day):
        if start_time != ts_start(app_span(app)):
            appointments.append(app)
    return appointments


""" Tests """

# create("Tess")
# book("Tess", 13, "dec", "12:00", "14:00", "Plugga")
# book("Tess", 13, "dec", "15:00", "16:00", "Vila")
# show("Tess", 13, "dec")
# remove("Tess", 13, "dec", "15:00")
# book("Tess", 13, "dec", "15:00", "16:00", "Kröka")
# show("Tess", 13, "dec")


# create("Mats")
# book("Mats", 25, "dec", "14:00", "17:00", "Födelsedagsfirande")
# book("Mats", 25, "dec", "11:00", "14:00", "Sovmorgon")
# book("Mats", 25, "dec", "21:00", "23:00", "partaj")
# show("Mats", 25, "dec")
# remove("Mats", 25, "dec", "14:00")
# show("Mats", 25, "dec")