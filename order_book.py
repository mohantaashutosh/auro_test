import xml.etree.ElementTree as ET
from collections import OrderedDict
book=OrderedDict()
tree = ET.parse("orders.xml")
root = tree.getroot()
for child in root:
    print(child.attrib['book'])
