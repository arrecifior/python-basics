##############################################################
###                                                        ###
###   AUTHOR : Dmitry Ivanov                               ###
###   DATE   : 2021-11-17                                  ###
###   TASK   : Create a basic calculator using functions   ###
###                                                        ###
##############################################################

# functions for math operations

def add(a, b):
    print(a, "+", b, "=", a + b)

def subtract(a, b):
    print(a, "-", b, "=", a - b)

def divide(a, b):
    print(a, "/", b, "=", a / b)

def multiply(a, b):
    print(a, "*", b, "=", a * b)

def modulus(a, b):
    print(a, "%", b, "=", a % b)

def floor(a, b):
    print(a, "//", b, "=", a // b)

def exponent(a, b):
    print(a, "**", b, "=", a ** b)

def max_min(a, b):
    print("max:", max(a, b), "min:", min(a, b))

def odd_even(a):
    if a % 2:
        print(a, "is odd")
    else:
        print(a, "is even")

def custom_type(a):
    print("type() of", a, "is", type(a))

oper_unary = ["odd_even", "type"]
oper_binary = ["add", "subtract", "divide", "multiply", "modulus", "floor", "exponent", "max_min"]

# main calculator logic
while True:
    
    print("Operations:", oper_binary, oper_unary, "\nEnter 'exit' to close the program")
    oper = input("Enter an operation: ")

    if oper in oper_unary:    # unary operations
        a = float(input("Enter a number: "))
        if oper == "odd_even":
            odd_even(a)
        if oper == "type":
            custom_type(a)

    elif oper in oper_binary: # binary operations
        a = float(input("Enter first number  : "))
        b = float(input("Enter second number : "))
        if oper == "add":
            add(a, b)
        if oper == "subtract":
            subtract(a, b)
        if oper == "divide":
            divide(a, b)
        if oper == "multiply":
            multiply(a, b)
        if oper == "modulus":
            modulus(a, b)
        if oper == "floor":
            floor(a, b)
        if oper == "exponent":
            exponent(a, b)
        if oper == "max_min":
            max_min(a, b)

    elif oper == "exit":      # exit condition
        break

    else:                     # invalid operation
        print("Invalid operation")

# on exit condition
print("Exiting the program ...")
