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

row = 's96113106'

mutation1 = [Mutation(column="name:", value="Ball")]
client.mutateRow('result', row, mutation1, None)

mutation2 = [Mutation(column="scores:Chinese",value="30")]
client.mutateRow('result',row,mutation2, None)

mutation3 = [Mutation(column='scores:english',value="50")]
client.mutateRow('result',row,mutation3, None)

mutation4 = [Mutation(column='scores:math', value="40")]
client.mutateRow('result',row,mutation4, None)

