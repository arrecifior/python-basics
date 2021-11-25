"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program finds the largest of four numbers

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

# Checking data type
print("num1 has", type(num1), "data type.")

# Main logic
max = num1
if (num2 > max):
    max = num2
if (num3 > max):
    max = num3
if (num4 > max):
    max = num4

# Printing result
print(max, "is the largest number.")
