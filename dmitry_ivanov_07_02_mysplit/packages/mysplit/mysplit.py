def split(string):

    # String converted into a list. Added space to the
    # end of the list to skip an edge case.
    string = list(string)
    string.append(' ')

    word = [] # words are stored here before they are appended to the main list
    split = [] # the main result list

    for i in range(len(string) - 1):
        if string[i] != ' ':
            word.append(string[i])
            if string[i + 1] == ' ':
                split.append(''.join(word))
                word.clear()
 
    return split

if __name__ == "__main__":
    print(split("To be or not to be, that is the question"))
