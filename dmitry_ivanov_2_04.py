############################
### Practicing variables ###
############################

# creating vriables and assigning values
john, mary, adam = 10, 6, 4

# outputting values separated by comma
print(john, mary, adam, sep=", ")

# variable, containing total amount of values
total_apples = john + mary + adam

print("Total number of apples:", total_apples)

# adam's number of apples is lost!
adam = 0
print(john, mary, adam, sep=", ")

# recalculating... 
adam = total_apples - john - mary

print(john, mary, adam, sep=", ")