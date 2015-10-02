#!/usr/bin/python2.7
import cgitb
cgitb.enable()

import cgi
print ('Content-Type: application/json\n\n')

import json
listtest = [2,5,9,10,11,113,117,118,144]
print(json.dumps(listtest,separators=(',', ': ')))

