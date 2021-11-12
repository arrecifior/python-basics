"""""""""""""""""""""""""""""""""""""""""""""""""""

    The simplest text adventure game possible!

"""""""""""""""""""""""""""""""""""""""""""""""""""

# secret number
number_required = 182

# first user input
number_input = int(input("Choose a number: "))

# wizards' trap!
while number_input != number_required:
    print("Ha ha! You're stuck in my loop!")
    number_input = int(input("Choose your number wisely: "))

# out of the loop
print("Well done, muggle! You are free now.")
