#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request as urllib
import urllib.parse as parse
import json

serviceUrl = 'http://python-data.dr-chuck.net/geojson?'
address = 'Ecole centrale de PARIS'

url = serviceUrl + parse.urlencode({'sensor':'false', 'address':address})
data = urllib.urlopen(url).read()
x = json.loads(data.decode('utf-8'))

print(x["results"][0]["place_id"])
