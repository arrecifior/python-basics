#############################
###   Building shop.xml   ###
#############################

import xml.etree.ElementTree as ET
from xml.dom import minidom

class XmlTreeHelper:
    def add_tags_with_text(self, parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return

root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

prod_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
prod_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Vaganiette'})
prod_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})

xth = XmlTreeHelper()

xth.add_tags_with_text(prod_1, {
    'type': 'cereals',
    'producer': 'Foods Ltd.',
    'price': '9.90',
    'currency': 'USD'
})

xth.add_tags_with_text(prod_2, {
    'type': 'pasta',
    'producer': 'Programmers Eat Pasta Gmbh',
    'price': '14.49',
    'currency': 'EUR'
})

xth.add_tags_with_text(prod_3, {
    'type': 'beverages',
    'producer': 'Drinks4Coders Inc.',
    'price': '19.75',
    'currency': 'USD'
})

#ET.dump(root)

#tree = ET.ElementTree(root)
#tree.write('shop.xml', 'UTF-8', True)

# writing pretty xml
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
with open('shop.xml', 'w') as f:
    f.write(xmlstr)
