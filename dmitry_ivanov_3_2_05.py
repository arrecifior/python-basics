###########################################################################
###                                                                     ###
###   This program accepts numbers as one input and outputs their sum   ###
###                                                                     ###
###########################################################################

# Requesting user input
list_input = input("Enter numbers separated by space: ")
print("Your input:", list_input)

# Splitting input string
list_input = list_input.split()
print("Your input after split:", list_input)

# Converting strings to integers
numbers = []
for num in list_input:
    numbers.append(int(num))
print("Converting strings to integers:", numbers)

print("Sum:", sum(numbers))
