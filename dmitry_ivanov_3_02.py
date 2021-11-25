"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program finds maximum and minimum of ten numbers

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Input values
print("Enter number values:")
num01 = int(input("Enter num01: "))
num02 = int(input("Enter num02: "))
num03 = int(input("Enter num03: "))
num04 = int(input("Enter num04: "))
num05 = int(input("Enter num05: "))
num06 = int(input("Enter num06: "))
num07 = int(input("Enter num07: "))
num08 = int(input("Enter num08: "))
num09 = int(input("Enter num09: "))
num10 = int(input("Enter num10: "))

# Find maximum and minimum
max = max(num01, num02, num03, num04, num05, num06, num07, num08, num09, num10)
min = min(num01, num02, num03, num04, num05, num06, num07, num08, num09, num10)

# Checking max data type
print("Variable max has", type(max), "data type.")

# Printing max and min values
print(max, "is the largest number.", min, "is the smallest number.")
