##################################
###                            ###
###   Bubble sorting machine   ###
###                            ###
##################################

# initialize list
my_list = []

# user preferences
n = int(input("Enter the number of numbers you want to sort: "))
sort_direction = input("Do you want an ascending or descending sorting? (a)scending / (d)escending: ")
sort_method = input("Do you want to use a custom bubble sorting or a built-in method? (c)ustom / (b)uilt-in: ")

# enter list data
for i in range(n):
    my_list.append(int(input("Enter a number: ")))

# fake data to enter a loop
swapped = True

# Main logic 
if sort_method.lower() == "c" or sort_method.lower() == "custom":
    if sort_direction.lower() == "a" or sort_direction.lower() == "ascending":

        # Custom bubble sorting with ascending order
        while swapped:
            swapped = False # no swaps
            for i in range(len(my_list) - 1):
                if my_list[i] > my_list [i + 1]:
                    swapped = True # there was a swap
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)

    elif sort_direction.lower() == "d" or sort_direction.lower() == "descending":

        # Custom bubble sorting with descending order
        while swapped:
            swapped = False # no swaps
            for i in range(len(my_list) - 1):
                if my_list[i] < my_list [i + 1]:
                    swapped = True # there was a swap
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)

    else:
        print("Invalid sorting order.")
elif sort_method.lower() == "b" or sort_method.lower() == "built-in":
    if sort_direction.lower() == "a" or sort_direction.lower() == "ascending":

        # Built-in sorting with ascending order
        my_list.sort()
        print(my_list)

    elif sort_direction.lower() == "d" or sort_direction.lower() == "descending":

        # Built-in sorting with descending order
        my_list.sort()
        my_list.reverse()
        print(my_list)

    else:
        print("Invalid sorting order.")
else:
    print("Invalid sorting method type.")
