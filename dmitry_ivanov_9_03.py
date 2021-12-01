###################################################################
### Program with Weeker (days of the week) class implementation ###
###################################################################

# custom weekday error exception
class WeekDayError(Exception):
    def __init__(self, day, message):
        Exception.__init__(self, message)
        self.day = day

class Weeker:
    __weekdays_dict = { # weekday codes dictionary
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat',
        6: 'Sun'
    }

    def __init__(self, day = 'Mon'):
        if day in self.__weekdays_dict.values():
            for i in self.__weekdays_dict.keys():
                if day == self.__weekdays_dict.get(i):
                    self.__day = i
                    break
        else:
            raise WeekDayError(day, 'invalid weekday code')

    def __str__(self):
        return self.__weekdays_dict.get(self.__day)

    # add days to a Weeker instance
    def add_days(self, n):
        res = self.__day + n
        self.__day = res % 7

    # subtract days from a Weeker instance
    def subtract_days(self, n):
        res = self.__day - n
        self.__day = res % 7

# Test logic
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError as wde:
    print(wde, ':', wde.day)
