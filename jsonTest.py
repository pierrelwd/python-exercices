#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request as urllib
import json

i = 0
url = 'http://python-data.dr-chuck.net/comments_310434.json'
result = 0

data = urllib.urlopen(url).read()
x = json.loads(data.decode('utf-8'))
a = len(x['comments']) 

while i < a :
	b = x['comments'][i]['count']
	result += b
	i += 1

print (result)