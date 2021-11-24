#######################################################
###                                                 ###
###   This programs outputs list of numbers which   ###
###   appear more than once in the initial list     ###
###                                                 ###
#######################################################

# Requesting input
list_input = input("Please input integers separated by space: ")

# Splitting input string
list_input = list_input.split()

# Converting strings to integers
numbers = []
for num in list_input:
    numbers.append(int(num))

# Logic for more-than-one-appearance numbers
numbers.sort()
numbers_reapeat = [] # list of numbers which appear more than once in the original list
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1] and numbers[i] not in numbers_reapeat:
        numbers_reapeat.append(numbers[i])

# output and output formatting
for i in numbers_reapeat:
    print(i, end=" ")
