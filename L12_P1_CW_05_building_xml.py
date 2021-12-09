import xml.etree.ElementTree as et

root = et.Element('data')
et.dump(root)

root = et.Element('data')
movie_1 = et.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = et.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
et.dump(root)