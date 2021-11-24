##############################################################
###   AUTHOR      : Dmitry                                 ###
###   DATE        : 2021-11-24                             ###
###   DESCRIPTION : Class work for the lecture 7, part 2   ###
##############################################################

count = 0
# I am too lazy to count manually
def cnt():
    global count
    count +=1
    return "#" + str(count)

# Example 1
print(cnt(), "string length")

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 1

i_am = 'I\'m'
print(len(i_am))


# Multiline strings
print(cnt(), "multiline string length")

multiline = '''Line #1
Line #2'''

print(len(multiline))


multiline1 = """Line #1
Line #2"""

print(len(multiline1))


# String operations
print(cnt(), "string operations")

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * str1)
print(str2 * 4)



print(cnt(), "ord() demos")

# #1 ord() demo

char_1 = 'a'
char_2 = ' '

print(char_1, ord(char_1))
print(char_2, ord(char_2))

# #2 ord demo

char_greek = 'α'
char_polish = 'ę'
char_emoji = '🐍'

print(char_greek, ord(char_greek))
print(char_polish, ord(char_polish))
print(char_emoji, ord(char_emoji))


# chr() demo
print(cnt(), "chr() demo")

x = "a"
x1 = 97

print(type(x))
print(type(ord(x)))
print(type(chr(x1)))

print(chr(ord(x)), x)
print(chr(ord(x)) == x)

print(ord(chr(x1)), x1)
print(ord(chr(x1)) == x1)


# Indexing strings
print(cnt(), "indexing strings")

the_string = 'the ministry of silly walks'

for char in range(len(the_string)):
    print(the_string[char], end=' ')
print()

for char in range(len(the_string) - 1, -1, -1):
    print(the_string[char], end=' ')
print()

for i in range(len(the_string)):
    print(the_string[i], end='\n')
print()


# Slices
print(cnt(), "slices")

alpha = 'abdefg'
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


# in / not in
print(cnt(), "in / not in")

alphabet = "abcdefghjklmnopqrstuvwxyz"

print("f" in alphabet)
print("FF" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


# More operations on strings
print(cnt(), "more operations on strings")

alphabet = "bcdefghjklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"

# min()
print(min("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']', sep='')

space = min(t)
print("is space:", "\"", space, "\"", sep="")
print(ord(space))
print()

t = [0, 1, 2]
print(min(t))

# max()
print(max("aAbByYzZ"))

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']', sep='')

t = [0, 1, 2]
print(max(t))


# index()
print(cnt(), "index() method")

print("aAbByYzZ".index("b"))
print("aAbByYzZ".index("Z"))
print("aAbByYzZ".index("A"))


# list()
print(cnt(), "list() method")

st = "abcabc"
print(st, type(st), list(st))
print()

di = {1: "1", 2: "2"}
print(di, type(di), list(di))
print()

tupl = ("1", "2")
print(tupl, type(tupl), list(tupl))
print

# count()
print(cnt(), "count() method")

print("abcabc".count("b"))
print('abcabc'.count("d"))
print()

# Excercises
print("### Excerxises ###")

len("\"")

s='yesteryears'
the_list = list(s)
print(the_list[3:6])

for ch in "abc":
    print(chr(ord(ch) + 1), end="")

# capitalize()
print(cnt(), "capitalize() method")

print('aBcD'.capitalize())

print('Alpha'.capitalize())
print('ALPHA'.capitalize())
print(' Aplha'.capitalize())
print('123'.capitalize())
print('αβγδ'.capitalize())

# center()
print(cnt(), "center() method")

print('[' + 'alpha'.center(10) + ']')

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '-') + ']')


# endswith()
print(cnt(), "endswith() method")

if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# find()
print(cnt(), "find() method")

print("Eta".find("ta"))
print("Eta".find("mma"))
print()

print("kappa".find('a', 2))
print()

t= 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print()

the_text = """The raccoon (/rəˈkuːn/ or US: /ræˈkuːn/ (About this soundlisten), Procyon lotor),
sometimes called the common raccoon to distinguish it from other species, is a medium-sized
mammal native to North America. It is the largest of the procyonid family, having a body
length of 40 to 70 cm (16 to 28 in), and a body weight of 5 to 26 kg (11 to 57 lb). Its
grayish coat mostly consists of dense underfur, which insulates it against cold weather.
Three of the raccoon's most distinctive features are its extremely dexterous front paws,
its facial mask, and its ringed tail, which are themes in the mythologies of the indigenous
peoples of the Americas relating to the animal. The raccoon is noted for its intelligence,
as studies show that it is able to remember the solution to tasks for at least three years.
It is usually nocturnal and omnivorous, eating about 40% invertebrates, 33% plants, and 27%
vertebrates.
"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
print

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
print()


# isalnum()
print(cnt(), "isalnum() method")

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = 'αβγδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())


# isalpha(), isdigit()
print(cnt(), "isalpha(), isdigit() methods")

print("Moooo".isalpha())
print("Mu40".isalpha())

print('2018'.isdigit())
print('Year2019'.isdigit())


# join()
print(cnt(), "join() method")

print(" ".join(["Omicron", "Persei", "8"]))


# replace() and rfind()
print(cnt(), "replace() and rfind() methods")

print('www.vk.com'.replace('vk.com', 'python.org'))
print('This are it!'.replace('are', 'is'))
print('Apple juice'.replace('juice', ''))

print('This is it!'.replace('is', 'are', 1))
print('This is it!'.replace('is', 'are', 2))

print('tau tau tau'.rfind("ta"))
print('tau tau tau'.rfind("ta", 9))
print('tau tau tau'.rfind("ta", 3, 9))

# split()
print(cnt(), "split() method")
print("phi        chi\npsi".split())
