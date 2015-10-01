#!/usr/local/bin/python3
import cgitb
cgitb.enable()

import cgi

print("Content-type: text/html\n\n")
print()

form = cgi.FieldStorage()
argtn = form.getvalue('tablens')
argcu = form.getvalue('dColumns')
#$content = ColumnDescriptor(name=str(argcu), maxVersions=1)

#client.createTable(str(argtn), [content])
#print(client.getTableNames())

print(str(argtn))
print(str(argcu))
