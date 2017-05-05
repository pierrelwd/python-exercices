#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request as urllib
import xml.etree.ElementTree as ET

result = []
url = 'http://python-data.dr-chuck.net/comments_310430.xml'

data = urllib.urlopen(url).read()

e = ET.fromstring(data)
x = e.findall('comments/comment')

for item in x :
	z = item.find('count').text
	result.append(z)

finalResult = list(map(int, result))
print (sum(finalResult))