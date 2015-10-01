#!/usr/bin/python2.7
import cgitb
cgitb.enable()

import cgi

form = cgi.FieldStorage()
argtn = form.getvalue('tablens')
argcu = form.getvalue('dColumns')

import sys
sys.path.append('/usr/lib/python2.7/site-packages/')

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('192.168.171.168', 9090);
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport);
client = Hbase.Client(protocol)
transport.open()

content = ColumnDescriptor(name=str(argcu), maxVersions=1)

try:
    client.createTable(str(argtn), [content])
    print("Location: google.com.tw")
    print 
except:
    print('error')
