import time
from calendar import isleap

# Take leap year into consideration
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

#
