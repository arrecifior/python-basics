##############################################################
###                                                        ###
###   This program uses a funtion to determine how many    ###
###   days are there in a month and tests the result       ###
###                                                        ###
##############################################################

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

# testing

test_year = [1900, 2000, 2016, 1987]
test_month = [2, 2, 6, 12]
test_results = [28, 29, 30, 31]
for i in range(len(test_year)):
    yr = test_year[i]
    mn = test_month[i]
    print(yr, mn, "->", end=" ")
    result = days_in_month(yr, mn)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
