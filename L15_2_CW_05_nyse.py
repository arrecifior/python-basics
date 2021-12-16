import xml.etree.ElementTree

try:
    NYSE = xml.etree.ElementTree.parse('nyse.xml')
except FileNotFoundError:
    print("Stock data file not found")
    exit(1)
except xml.etree.ElementTree.ParseError:
    print("Stock data file contains invalid data")
    exit(2)

quotes = NYSE.getroot()
print('COMPANY'.ljust(40), end='')
print('LAST'.ljust(10), end='')
print('CHANGE'.ljust(10), end='')
print('MIN'.ljust(10), end='')
print('MAX'.ljust(10), end='')
print()
print('-' * 80)

for quote in quotes.findall('quote'):
    print(quote.text.ljust(40), end='')
    print(quote.attrib['last'].ljust(10), end='')
    print(quote.attrib['change'].ljust(10), end='')
    print(quote.attrib['min'].ljust(10), end='')
    print(quote.attrib['max'].ljust(10), end='')
    print()
