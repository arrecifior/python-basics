##################################################
### This program includes a custom Timer class ###
##################################################

class Timer:
    def __init__(self, hr = 0, mn = 0, sc = 0):
        self.__hr = hr
        self.__mn = mn
        self.__sc = sc

    def __str__(self):
        hr = str(self.__hr)
        mn = str(self.__mn)
        sc = str(self.__sc)
        
        if len(hr) == 1:
            hr_div = '0'
        else:
             hr_div = ""
        if len(mn) == 1:
            mn_div = ':0'
        else:
             mn_div = ":"
        if len(sc) == 1:
            sc_div = ':0'
        else:
             sc_div = ":"

        return hr_div + hr + mn_div + mn + sc_div + sc

    def next_second(self):
        if self.__sc < 59:
            self.__sc += 1
        else:
            self.__sc = 0
            if self.__mn < 59:
                self.__mn += 1
            else:
                self.__mn = 0
                if self.__hr < 23:
                    self.__hr += 1
                else:
                    self.__hr = 0

    def prev_second(self):
        if self.__sc > 0:
            self.__sc -= 1
        else:
            self.__sc = 59
            if self.__mn > 0:
                self.__mn -= 1
            else:
                self.__mn = 59
                if self.__hr > 0:
                    self.__hr -= 1
                else:
                    self.__hr = 23        

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)