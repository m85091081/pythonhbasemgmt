import cgi


import sys
sys.path.append('/usr/lib/python2.7/site-packages/')


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('192.168.171.154', 9090)
transport = TTransport.TBufferedTransport(transport)

protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

scan = TScan()
tableName = 'result'
id = client.scannerOpenWithScan(tableName, scan, None)

result2 = client.scannerGet(id)
sum_r=0
while result2:
    sum_r +=  1


print(sum_r)
