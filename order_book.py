import xml.etree.ElementTree as ET
from collections import OrderedDict
book=OrderedDict()
tree = ET.parse("orders.xml")
root = tree.getroot()
for child in root:
    print(child.attrib['book'])
    if not book[child.attrib['book']]:
        book[child.attrib['book']]=OrderedDict()
    book[child.attrib['book']].add()
