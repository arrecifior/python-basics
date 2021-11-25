"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    This program removes vowels from the word entered by user

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# user input
user_word = input("Please enter a word: ").upper()

# vowel skipping logic
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
