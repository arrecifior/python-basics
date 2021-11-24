###################################################################
###                                                             ###
###   AUTHOR      : Dmitry Ivanov                               ###
###   DATE        : 2021-11-24                                  ###
###   DESCRIPTION : This program uses custom split() function   ###
###                                                             ###
###################################################################

from packages.mysplit import mysplit

print(mysplit.split("To be or not to be, that is the question"))
print(mysplit.split("To be or not to be,that is the question"))
print(mysplit.split("   "))
print(mysplit.split("abc"))
print(mysplit.split(""))
