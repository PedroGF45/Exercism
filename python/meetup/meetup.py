from typing import List
from datetime import date
import calendar

WEEKDAYS = {"Monday": 0, "Tuesday": 1 , "Wednesday": 2 , "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
TEENTH_DAYS = [13, 14, 15, 16, 17, 18, 19]

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    
    month_calendar = calendar.monthcalendar(year, month)

    day = None

    if week == "first":

        day = _get_day(month_calendar, day_of_week, 0)

    elif week == "second":

        day = _get_day(month_calendar, day_of_week, 1)

    elif week == "third":

        day = _get_day(month_calendar, day_of_week, 2)

    elif week == "fourth":

        day = _get_day(month_calendar, day_of_week, 3)

    elif week == "fifth":

        day = _get_day(month_calendar, day_of_week, 4)

    elif week == "teenth":

        day = _get_teenth_day(month_calendar, day_of_week)

    elif week == "last":
    
        day = _get_last_day(month_calendar, day_of_week)

    else:
        raise MeetupDayException("Wrong week")

    return date(year, month, day)

def _get_day(month_calendar: List[list], day_of_week: str, count_times: int) -> int: # type: ignore

    counter = 0
    for month_week in month_calendar:

        if month_week[WEEKDAYS[day_of_week]] != 0:

            if counter < count_times:
                counter += 1
            else:
                day = month_week[WEEKDAYS[day_of_week]]
                return day
            
    raise MeetupDayException("That day does not exist.")

def _get_teenth_day(month_calendar: List[list], day_of_week: str) -> int:

    for month_week in month_calendar:

        if month_week[WEEKDAYS[day_of_week]] != 0 and month_week[WEEKDAYS[day_of_week]] in TEENTH_DAYS:

            day = month_week[WEEKDAYS[day_of_week]]
            return day
        
def _get_last_day(month_calendar: List[list], day_of_week: str) -> int:

    for week_index in range(len(month_calendar) - 1, 0, -1):

        if month_calendar[week_index][WEEKDAYS[day_of_week]] != 0:

            day = month_calendar[week_index][WEEKDAYS[day_of_week]]
            return day