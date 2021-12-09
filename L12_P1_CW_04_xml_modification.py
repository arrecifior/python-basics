import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

for child in root:
    child.tag = 'movie'
    print(child.tag, child.attrib)

    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)
    print()

# testing testing
tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
print(
)

# remove, set, write methods
tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'

    #remove
    child.remove(child.find('author'))
    child.remove(child.find('year'))

    #set
    child.set('rating', '5')

    print (child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)
print()
#write
tree.write('movies.xml', 'UTF-8', True)
