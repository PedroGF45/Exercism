from datetime import datetime, timedelta
import re
from dateutil.relativedelta import relativedelta

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def delivery_date(start, description):

    converted_time = format_starting_time(start)

    if description == "NOW":

        converted_time += timedelta(hours = 2)
    
    elif description == "ASAP":

        if converted_time.hour < 13:
            
            converted_time = converted_time.replace(hour = 17, minute = 0, second = 0)

        else:
            converted_time = converted_time + timedelta(days = 1)
            converted_time = converted_time.replace(hour = 13, minute = 0, second = 0)
    
    elif description == "EOW":

        # monday, tuesday or wednesday
        if converted_time.weekday() in [0, 1, 2]:
            converted_time = converted_time + timedelta( (4-converted_time.weekday()) % 7 )
            converted_time = converted_time.replace(hour = 17, minute = 0, second = 0)

        else:
            converted_time = converted_time + timedelta( (6-converted_time.weekday()) % 7 )
            converted_time = converted_time.replace(hour = 20, minute = 0, second = 0)
        
    elif re.search(r'([1-9]|1[0-2])(M)', description):

        month = re.search(r'([1-9]|1[0-2])(M)', description).group(1)
                          
        if converted_time.month >= int(month):
            converted_time = converted_time + relativedelta(years = 1)
        
        converted_time = converted_time.replace(month = int(month), day = 1, hour = 8, minute = 0, second = 0)

        while converted_time.weekday() in [5, 6]:
            converted_time = converted_time + timedelta(days = 1)

    elif re.search(r'(Q)([1-4])', description):

        quarter = re.search(r'(Q)([1-4])', description).group(2)

        month = converted_time.month

        if int(quarter) * 3 >= month + 1:
            converted_time = converted_time + relativedelta(months = int(quarter) * 3 - month + 1)
        else:
            converted_time = converted_time + relativedelta(years = 1, months = int(quarter) * 3 - month + 1)

        converted_time = converted_time.replace(day = 1, hour = 8, minute = 0, second = 0)

        converted_time = converted_time - timedelta(days = 1)
         
        while converted_time.weekday() in [5, 6]:
            converted_time = converted_time - timedelta(days = 1)
    else:

        raise ValueError("Wrong Description")

    return format_converted_time(converted_time)


def format_starting_time(starting_time) -> datetime:

    starting_time = starting_time.replace("T", " ")
    
    converted_time = datetime.strptime(starting_time, DATE_FORMAT)

    return converted_time


def format_converted_time(converted_time):

    return '{:%Y-%m-%dT%H:%M:%S}'.format(converted_time)
    
