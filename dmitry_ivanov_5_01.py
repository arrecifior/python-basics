#################################################################
###                                                           ###
###   This program calculates factorial (without recursion)   ###
###                                                           ###
#################################################################

def factorial(num):
    if num < 0:
        return None
    else:
        fac = 1
        for i in range (num):
            fac *= i + 1
        return fac

for i in range(-1, 9):
    print(factorial(i))
