###################################
### A simple calculator program ###
###################################

# Requesting number values
print("\nThis is a simple calculatior.\nPlease enter number values for x and y:")
x = float(input("x = "))
y = float(input("y = "))

# Requesting operation choice
print("\nPlease choose operation.")
print( "(1)", x, "+ ", y)
print( "(2)", x, "- ", y)
print( "(3)", x, "/ ", y)
print( "(4)", x, "* ", y)
print( "(5)", x, "**", y)
print( "(6)", x, "//", y)
print( "(7)", x, "%", y)
operation = int(input("Please enter operation value: "))

# Calculator logic
print()
if (operation==1):
    print(x, "+", y, "=", x+y)
elif (operation==2):
    print(x, "-", y, "=", x-y)
elif (operation==3):
    print(x, "/", y, "=", x/y)
elif (operation==4):
    print(x, "*", y, "=", x*y)
elif (operation==5):
    print(x, "**", y, "=", x**y)
elif (operation==6):
    print(x, "//", y, "=", x//y)
elif (operation==7):
    print(x, "%", y, "=", x%y)
else:
    print("No operation chosen. Exiting program...")