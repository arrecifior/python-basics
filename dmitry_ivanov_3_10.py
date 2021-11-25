"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Vowel remover v2.0

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# user input
user_word = input("Please enter a word: ").upper()
word_without_vowels = ""

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
        word_without_vowels = word_without_vowels + letter

# printing the result
print(word_without_vowels)
