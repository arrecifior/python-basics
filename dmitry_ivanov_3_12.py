"""""""""""""""""""""""""""

    Calculator v 2.0

"""""""""""""""""""""""""""

# input request
result = float(input("Please enter a number: "))

while True:
    # operation input request
    print("Please enter an opetation")
    print("'+' '-' '/' '*' '**' '//' '%' ; enter 'exit' to stop the program.")
    operation = input("Operation: ")
    
    # exit loop if the input is 'exit'
    if operation == "exit":
        break

    # next number request
    number = float(input("Enter next number: " + str(result) + " " + operation + " "))

    if (operation == "+"):
        result = result + number
    elif (operation == "-"):
        result = result - number
    elif (operation == "/"):
        result = result / number
    elif (operation == "*"):
        result = result * number
    elif (operation == "**"):
        result = result ** number
    elif (operation == "//"):
        result = result // number
    elif (operation == "%"):
        result = result % number
    else:
        print("Invalid operation, please try again")
    print("The result is", result)

print("Exit command received. The program is stopped.")
