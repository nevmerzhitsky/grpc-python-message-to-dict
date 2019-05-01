import time
from concurrent import futures
from pprint import pprint

import grpc
import test_pb2
import test_pb2_grpc
from google.protobuf import struct_pb2

from tools import message_to_dict


def grpc_server_start() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestApiServicer_to_server(TestApiServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # since server.start() will not block,
    # a sleep-loop is added to keep alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


class TestApiServicer(test_pb2_grpc.TestApiServicer):
    def EmptyFunc(self, request, context):
        print('### EmptyFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()

    def ManyFieldsFunc(self, request: test_pb2.ManyFields, context):
        print('### ManyFieldsFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()

    def ManyFieldsListFunc(self, request: test_pb2.ManyFieldsList, context):
        print('### ManyFieldsListFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()

    def FieldsWithEnumFunc(self, request: test_pb2.FieldsWithEnum, context):
        print('### FieldsWithEnumFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()

    def OneofFieldsFunc(self, request: test_pb2.OneofFields, context):
        print('### OneofFieldsFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()

    def MapFieldsFunc(self, request: test_pb2.MapFields, context):
        print('### MapFieldsFunc')
        print('request:')
        pprint(request)
        params = message_to_dict(request)
        print('dict:')
        pprint(params)
        return struct_pb2.Value()


if __name__ == '__main__':
    print('SERVER')
    grpc_server_start()
