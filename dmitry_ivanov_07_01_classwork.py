##############################################################
###   AUTHOR      : Dmitry                                 ###
###   DATE        : 2021-11-24                             ###
###   DESCRIPTION : Class work for the lecture 7, part 1   ###
##############################################################

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('Oops! You entered something weird.')
except ZeroDivisionError:
    print('Yeah... Dividing by zero is not allowed, sorry :(')
except:
    print('I am not even sure how to describe what just happened.')


temperature = float(input('Enter current temperature: '))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero")
else:
    print("Zero")


while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")


while True:
    try:
        number = int(input("Enter an integer number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or attempt to divide by zero.")
    except:
        print("Sorry, something went wrong...")

while True:
    try:
        number = int(input("Enter an integer number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value or attempt to divide by zero.")
    except ZeroDivisionError:
        print("Division by zero is forbidden.")
    except:
        print("Sorry, something went wrong...")
