#########################################################
###                                                   ###
###   This program finds arithmetic mean of numbers   ###
###   which are multiples of 3 in range [a;b]         ###
###                                                   ###
#########################################################

# user input
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# obtaining a set from the range
value_set = []
for i in range(a, b + 1):
    if i % 3 == 0:
        value_set.append(i)

# calculating arithmetic mean
sum = 0
for i in value_set:
    sum += i
arithmetic_mean = sum / len(value_set)

# output
print(round(arithmetic_mean, 1))
