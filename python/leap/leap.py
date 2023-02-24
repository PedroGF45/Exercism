def leap_year(year):
    return bool(( year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
