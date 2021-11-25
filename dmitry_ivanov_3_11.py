"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program computes sequences for Collatz conjuncture

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# user input request
c0 = int(input("Enter any natural number: "))
steps = 0

# check if the input is correct
if c0 <= 0:
    print("Input must be a natural number (non-negative and non-zero).")
else:
    print(c0)
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        print(int(c0))
        steps += 1

# printing amount of steps
print("steps =", steps)
