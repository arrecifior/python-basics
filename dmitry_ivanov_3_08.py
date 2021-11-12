"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program exits infinite loop when user enters the keyword

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

keyword = "chupacabra"

while True:
    input_word = input("Enter the keyword: ")
    if input_word == keyword:
        break

print("You've successfully left the loop.")
