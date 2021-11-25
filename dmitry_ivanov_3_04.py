"""""""""""""""""""""""""""""""""

    This is a tax calculator

"""""""""""""""""""""""""""""""""

# setting tax amount
tax_rate = 0.15

# main logic
print("This is a tax calculator.")
income = float(input("Please enter your income amount: ")) # 1st input

if income <= 0:
    print("Invalid number.")
    income = float(input("Please enter your income amount: ")) # 2nd input
    if income <= 0:
        print("Invalid number.")
        income = float(input("Please enter your income amount: ")) # 3rd input
        if income <= 0:
            print("Invalid number.")
            income = float(input("Please enter your income amount: ")) # 4th input
            if income <= 0:
                print("Invalid number.")
                income = float(input("Please enter your income amount: ")) # 5th input
                if income <= 0:
                    print("You entered an invalid income amout 5 times. Please try again later.")
                else:
                    print("Your tax is ", round(income*tax_rate, 2), " at tax rate ", int(tax_rate*100), "%", sep="")
            else:
                print("Your tax is ", round(income*tax_rate, 2), " at tax rate ", int(tax_rate*100), "%", sep="")
        else:
            print("Your tax is ", round(income*tax_rate, 2), " at tax rate ", int(tax_rate*100), "%", sep="")
    else:
        print("Your tax is ", round(income*tax_rate, 2), " at tax rate ", int(tax_rate*100), "%", sep="")
else:
    print("Your tax is ", round(income*tax_rate, 2), " at tax rate ", int(tax_rate*100), "%", sep="")
