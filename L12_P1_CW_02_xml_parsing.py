import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print('My books:\n')
for book in root:
    print('Title: ', book.attrib['title'])
    for elem in book:
        print(elem.tag.title(), ': ', elem.text, sep='')
    print()