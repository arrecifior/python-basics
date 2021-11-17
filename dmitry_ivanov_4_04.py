############################################################################
###                                                                      ###
###   This program uses funtions to determines day of the year by date   ###
###                                                                      ###
############################################################################

def if_leap_year(year):
    if year < 1582:
        leap_year = False
    else:
        if year % 4 != 0:
            leap_year = False
        elif year % 100 != 0:
            leap_year = True
        elif year % 400 != 0:
            leap_year = False
        else:
            leap_year = True
    return leap_year

def days_in_month(year, month):
    month_length = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if if_leap_year(year):
            days = 29
        else:
            days = 28
    else:
        days = month_length[month - 1]
    return days

def day_of_year(year, month, day):
    if year >= 1582 and 0 < month <= 12 and 0 < day <= days_in_month(year, month): # input data validation
        day_count = 0
        for month_count in range(month - 1):
            day_count += days_in_month(year, month_count + 1)
        day_count += day
        return day_count
    else:
        return None         

test_year = [2000, 2007, 2013]
test_month = [12, 11, 5]
test_day = [31, 12, 6]
test_results = [366, 316, 126]
for i in range(len(test_year)):
    yr = test_year[i]
    mn = test_month[i]
    dy = test_day[i]
    print(yr, mn, dy, "->", end=" ")
    result = day_of_year(yr, mn, dy)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
