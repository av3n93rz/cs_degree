from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1639986.xml'

xml = urlopen(url).read()
tree = ET.fromstring(xml)


""" long version: """
total = 0

for count in tree.findall('.//count'):
  total = total + int(count.text)

print(total)


""" short version: """
print(sum([int(count.text) for count in tree.findall('.//count')]))

