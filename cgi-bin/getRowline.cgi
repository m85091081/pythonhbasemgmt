#!/usr/bin/python2.7
import cgitb
cgitb.enable()

import cgi

form = cgi.FieldStorage()
argtn = form.getvalue('tablen')


import sys
sys.path.append('/usr/lib/python2.7/site-packages/')


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('192.168.171.168', 9090)
transport = TTransport.TBufferedTransport(transport)

protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

scan = TScan()
tableName = str(argtn)
id = client.scannerOpenWithScan(tableName, scan, None)

result2 = client.scannerGet(id)
sum_r=0
while result2:
    sum_r +=  1
    result2 = client.scannerGet(id)

print("Content-Type: text/html\n\n")
print
print(sum_r)
