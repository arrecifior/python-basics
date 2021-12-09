######################################################
### Simple unit converter for miles and kilometers ###
######################################################

# storing amount of kilometers in miles
kilometers_in_miles = 1.61

# input values
kilometers = 12.25
miles = 7.38

# output
print(miles, "miles is", round(miles*kilometers_in_miles, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers/kilometers_in_miles, 2), "miles")