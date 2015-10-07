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

tableName = 'result'
rowKey = 's96113106'

result = client.getRow(tableName, rowKey, None)
print(result)
for r in result:
    print('ID:' , r.row ,'Student name is ' , r.columns.get('name:').value)
    print('His Chinese Score is ' , r.columns.get('scores:Chinese').value)
    print('His English Score is ' , r.columns.get('scores:english').value)
    print('His Math Score is ' , r.columns.get('scores:math').value)


