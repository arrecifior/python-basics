"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program wants you to type "Cinnamomum camphora"

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# correct spelling + input
tree_name = "Cinnamomum camphora"
input_tree_name = input("Please enter a tree name: ")

# main logic
if tree_name.lower() == input_tree_name.lower():
    if tree_name == input_tree_name:
        print("Yes!", tree_name, "is great!")
    else:
        print("Check your spelling! It is supposed to be", tree_name, end="!\n")
else:
    print(tree_name, "! Not ", input_tree_name, "!", sep="")
