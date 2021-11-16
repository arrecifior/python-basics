###############################
###                         ###
###    Working with lists   ###
###                         ###
###############################

# List of numbers hidden in the hat
hat_list = [1, 2, 3, 4, 5]

# Prints the length of the list
print("The length of the list is", len(hat_list))

# Prompting user to replace the middle number
hat_list[2] = int(input("Please enter a new middle number: "))

# Removing the last element of the list
del hat_list[-1]

# Prints the length of the list
print("The length of the list is", len(hat_list))

# Printing out the list
print(hat_list)
