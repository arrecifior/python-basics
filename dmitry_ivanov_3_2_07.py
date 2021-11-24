################################################################
###                                                          ###
###   This program calculates average from the number list   ###
###                                                          ###
################################################################

# Requesting input
list_input = input("Please input integers separated by space: ")

# Converting input to a list of integers
list_input = list_input.split()
numbers = []
for num in list_input:
    numbers.append(int(num))

# Calculating average
sum = 0
for i in numbers:
    sum += i
average = sum / len(numbers)

print("The average is", average)
