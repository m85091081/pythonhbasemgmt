import sys
sys.path.append('/usr/lib/python2.7/site-packages/')


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('192.168.171.154', 9090);

transport = TTransport.TBufferedTransport(transport)

protocol = TBinaryProtocol.TBinaryProtocol(transport);

client = Hbase.Client(protocol)
transport.open()


content1 = ColumnDescriptor(name='name:', maxVersions=1)

content2 = ColumnDescriptor(name='scores:', maxVersions=1)


client.createTable('result', [content1,content2])

print client.getTableNames()
