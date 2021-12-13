import xml.etree.cElementTree

cars_for_sale = xml.etree.cElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, '=', prop.text, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
            print(' =', prop.text)
        print()
