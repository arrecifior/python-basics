###########################################
###                                     ###
###   Removing duplicates from a list   ###
###                                     ###
###########################################

# initial list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# setting this variable to true to enter while loop
duplicate_removed = True 

# main logic
my_list.sort()
while duplicate_removed:
    duplicate_removed = False # no duplicate removals
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[i + 1]:
            my_list.pop(i)
            duplicate_removed = True # duplicate removal occured
            break # breaking searching for duplicates loop after a duplicate is removed

print(my_list)
