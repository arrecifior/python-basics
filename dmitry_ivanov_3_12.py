"""""""""""""""""""""""""""

    Calculator v 2.0

"""""""""""""""""""""""""""

while True:
    
    # first value input request
    a = input("Enter first value: ")
    
    # converting input value to an appropriate data type
    if a.lower() == "true":
        a = True
    elif a.lower() == "false":
        a = False
    elif float(a) % 1 == 0:
        a = int(a)
    else:
        a = float(a)

    ##print(type(a)) #test
    
    # operation input request
    oper = input("Operations: '+', '-', '/', '*', '**', '//', '%', 'and', 'or',\n            'not', 'type', 'round', 'max', 'min'.\nYou can enter 'exit' to exit the program.\nInput your choice: ")
    
    # exit loop if the input is 'exit'
    if oper == "exit":
        break

    # performing unary operations without requesting second value
    if oper == "not":
        print("RESULT: not", a, "=", not a)
    elif oper == "type":
        print("RESULT:", a, "has", type(a), "type")
    elif oper == "round":
        print("RESULT: round(", a, ") = ", round(a))
    else:
        # requesting second value for binary operatios
        b = input("Enter second value: ")

        # converting input value to an appropriate data type
        if b.lower() == "true":
            b = True
        elif b.lower() == "false":
            b = False
        elif float(b) % 1 == 0:
            b = int(b)
        else:
            b = float(b)

        ##print(type(b)) # test

        # performing binary operations
        if oper == "and":
            print("RESULT:", a, "and", b, "=", a and b)
        elif oper == "or":
            print("RESULT:", a, "or", b, "=", a or b)
        elif oper == "max":
            print("RESULT: max(", a, ",", b, ") =", max(a, b))
        elif oper == "min":
            print("RESULT: min(", a, ",", b, ") =", min(a, b))
        elif oper == "+":
            print("RESULT:", a, "+", b, "=", a+b)
        elif oper == "-":
            print("RESULT:", a, "-", b, "=", a-b)
        elif oper == "/":
            print("RESULT:", a, "/", b, "=", a/b)
        elif oper == "*":
            print("RESULT:", a, "*", b, "=", a*b)
        elif oper == "**":
            print("RESULT:", a, "**", b, "=", a**b)
        elif oper == "//":
            print("RESULT:", a, "//", b, "=", a//b)
        elif oper == "%":
            print("RESULT:", a, "%", b, "=", a%b)
        else:
            print("Invalid operation, please try again")

print("Exiting the program ...")
