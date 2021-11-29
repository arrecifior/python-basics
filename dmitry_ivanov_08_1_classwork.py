#########################################
###   Classwork for lecture 8 pt. 1   ###
#########################################

# I am to lazy to format the output manually
count = 0
def ex():
    global count
    count += 1

    if len(str(count)) == 2:
        padding = ''
    else:
        padding = ' '

    print("╒═══════════════════════╕")
    print("│  Example ", padding, count, "           │", sep="")
    print("└───────────────────────┘")

# Examples

ex()

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oops...")

print("FIN.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Oops... (again)")

print("FIN pt.2: Electric Boogaloo")


ex()

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero division!")

print("THE END.")


ex()

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic problem!")
    return None

bad_fun(0)
print("THE END.")

def bad_fun1(n):
    return 1 / n

try:
    bad_fun1(0)
except ArithmeticError:
    print("An exception was raised!")

print("THE END.")


ex()

def more_bad_fun(n):
    raise ZeroDivisionError

try:
    more_bad_fun(0)
except ArithmeticError:
    print("What happened? Some error.")

print("THE END.")


ex()

def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it! And I'll do it again!")
        raise

try:
    bad_fun(0)
except ArithmeticError:
    print("Good for you!")

print("THE END.")


ex()

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)


ex()

#Ex1
try:
    print(1/0)
except ZeroDivisionError:
    print("zero")
except ArithmeticError:
    print("arith")
except:
    print("some")

#Ex2
try:
    print(1/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

#Ex3
def foo(x):
    assert x
    return 1/x

try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")


ex()

from math import tan, radians
angle = int(input("Enter integral angle in degrees: "))

assert angle % 180 != 90, "Angle must not be == 90 + k * 180"
print(tan(radians(angle)))


ex()
from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 0.1
        seconds = round(seconds, 1)
        sleep(0.1)
    except KeyboardInterrupt:
        print("Don't do that! Or do. It is your computer and your life, who am I to judge?")
        break


ex()

string = 'x'

try:
    while True:
        string = string + string
        print(len(string))
        if len(string) > 4294967296:
            print('That is enough for 16 gigs of ram')
            break
except MemoryError:
    print('This is not funny!')


ex()

from math import exp

exx = 1

try:
    while True:
        print(exp(exx))
        exx *= 2
except OverflowError:
    print("The number is too big")


ex()
try:
    import time
    import math
    import supermath
except:
    print("Python is wrong, there is definetely a supermath, somwhere...")
