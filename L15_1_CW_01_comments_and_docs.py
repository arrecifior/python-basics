# TODO: add a function that takes the val and prc arguments.

# Step 1: Ask the user for the value
# Step 2: Change the value to an int and handle possible exceptions.
# Step 3: Print the value multiplied by 0.7.

def fun(val):
    return val * 2

user_value = int(input("Enter the value: "))
# fun(user_value)
# user_value = user_value + "foo"

print(fun(user_value))

# Type information added:
def hello(name: str) -> str:
    return "Hello, " + name

def my_fun(a, b):
    """This function returns the result of a*b. That's it."""

    return a*b

print(my_fun.__doc__)
