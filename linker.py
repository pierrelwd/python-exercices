#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request as urllib

url = "http://python-data.dr-chuck.net/known_by_Oonagh.html"
i = 0
regEx = '>(.+)<'

while i < 7 :
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	a = soup.find_all('a', href=True)[17]
	url = a['href']
	i += 1

finalResult = re.findall(regEx, str(a))
print (finalResult[0])