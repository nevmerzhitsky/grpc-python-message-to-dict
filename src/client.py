from pprint import pprint

import grpc
import test_pb2
import test_pb2_grpc
from google.protobuf import empty_pb2
from google.protobuf.timestamp_pb2 import Timestamp

from tools import message_to_dict


def main():
    with grpc.insecure_channel('server:50051') as channel:
        stub = test_pb2_grpc.DatabaseToolsStub(channel)

        print('### EmptyFunc')
        stub.EmptyFunc(empty_pb2.Empty())

        print('### ManyFieldsFunc')
        ts = Timestamp()
        ts.GetCurrentTime()
        request = test_pb2.ManyFields(a_bool=True, int_32=1, int_64=112233, ts=ts, a_str='abc')
        pprint(request)
        stub.ManyFieldsFunc(request)

        print('### ManyFieldsListFunc')
        request = test_pb2.ManyFieldsList()
        for i in range(2):
            ts = Timestamp()
            ts.GetCurrentTime()
            record = test_pb2.ManyFields(a_bool=True, int_32=i, int_64=112233, ts=ts, a_str='abc')
            request.records.extend([record])
        pprint(request)
        stub.ManyFieldsListFunc(request)

        print('### ManyFieldsListFunc empty')
        request = test_pb2.ManyFieldsList()
        pprint(request)
        stub.ManyFieldsListFunc(request)

        print('### FieldsWithEnumFunc')
        ts = Timestamp()
        ts.GetCurrentTime()
        request = test_pb2.FieldsWithEnum(int_32=1, e_num=test_pb2.TestEnum.Value('IMAGES'))
        pprint(request)
        stub.FieldsWithEnumFunc(request)

        print('### OneofFieldsFunc')
        request = test_pb2.OneofFields(a_bool=True, a_str='abc100500')
        pprint(request)
        stub.OneofFieldsFunc(request)

        print('### MapFieldsFunc')
        request = test_pb2.MapFields()
        for i in range(2):
            request.records[i].a_bool = True
            request.records[i].int_32 = i
            request.records[i].int_64 = 112233
            request.records[i].a_str = 'abc'
        pprint(request)
        stub.MapFieldsFunc(request)

        print('### MapFieldsFunc empty')
        request = test_pb2.MapFields()
        pprint(request)
        stub.MapFieldsFunc(request)


if __name__ == '__main__':
    print('CLIENT')
    main()
