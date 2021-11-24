##############################################################
###                                                        ###
###   This program uses a funtion to determine if a year   ###
###   is a leap year and tests the result                  ###
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
    

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end=" ")
    result = if_leap_year(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
