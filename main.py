import time
from calendar import isleap

# Take leap year into consideration
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# This will return the number of days in every month
# Format (1 = January, etc.)
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28
