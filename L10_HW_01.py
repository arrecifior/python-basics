#####################################################
###   This prigram counts letters in a file and   ###
###   prints the data into another file           ###
#####################################################

from os import strerror

# dictionary for counting letters
alpha = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# sorted key list
keys = [ch for ch in alpha.keys()]
keys.sort()

# reading a file an counting letters
filename = input("Enter file name: ") # asking user to specify file name
try:
    s = open(filename, "rt")

    for line in s:
        for ch in line:
            print(ch, end="")
            if ch.lower() in alpha.keys():
                ccnt = alpha.pop(ch.lower())
                alpha.update({ch.lower(): ccnt + 1})

    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))

# print counters to the console
for ch in keys:
    if alpha.get(ch) > 0:
        print(ch, '->', alpha.get(ch))

# printing data to a file
try:
    s = open("text_count.txt", "w")
    for ch in keys:
        if alpha.get(ch) > 0:
            s.write(ch + " -> " + str(alpha.get(ch)) + "\n")
    s.close()
    print("Data written to a file 'text_count.txt'")
except Exception as exc:
    print("File writing error:", strerror(exc.errno))
