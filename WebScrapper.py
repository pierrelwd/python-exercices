#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import urllib.request as urllib
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_310433.html"
regEx = '"comments">(.+)</span'
i = 0
result = []

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

x = (soup.find_all('span'))

while i < len(x) :
	y = str(x[i])
	z = re.findall(regEx, y)
	result.append(z[0])
	i += 1

final = list(map(int, result))
print (sum(final))


