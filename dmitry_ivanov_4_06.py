#######################################################################################
###                                                                                 ### 
###   This programs converts liters per 100 km to miles per gallon and vise versa   ###
###                                                                                 ###
#######################################################################################

lpg = 3.785411784
kmpm = 1609.344

def lp100km_to_mpg(lp100km):
    return (100 * 1000 * lpg) / (lp100km * kmpm)

def mpg_to_lp100km(mpg):
    return (100 * 1000 * lpg) / (mpg * kmpm)

print(lp100km_to_mpg(3.9))
print(lp100km_to_mpg(7.5))
print(lp100km_to_mpg(10.))
print(mpg_to_lp100km(60.3))
print(mpg_to_lp100km(31.4))
print(mpg_to_lp100km(23.5))
