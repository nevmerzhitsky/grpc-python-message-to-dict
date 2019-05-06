from pprint import pprint

import test_pb2
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp

from converter import message_to_dict


def main():
    print('\n### empty_pb2.Empty')
    request = empty_pb2.Empty()
    dump_request(request)

    print('\n### ManyFields')
    ts = Timestamp()
    ts.GetCurrentTime()
    request = test_pb2.ManyFields(a_bool=True, int_32=1, int_64=112233, ts=ts, a_str='abc')
    dump_request(request)

    print('\n### FieldsWithEnum')
    ts = Timestamp()
    ts.GetCurrentTime()
    request = test_pb2.FieldsWithEnum(int_32=1, e_num=test_pb2.TestEnum.Value('IMAGES'))
    dump_request(request)

    print('\n### OneOfFields')
    request = test_pb2.OneOfFields(a_bool=True, a_str='abc100500')
    dump_request(request)

    print('\n### ManyFieldsList with data')
    request = test_pb2.ManyFieldsList()
    for i in range(2):
        ts = Timestamp()
        ts.GetCurrentTime()
        record = test_pb2.ManyFields(a_bool=True, int_32=i, int_64=112233, ts=ts, a_str='abc')
        request.records.extend([record])
    dump_request(request)

    print('\n### MapFields with data')
    request = test_pb2.MapFields()
    for i in range(2):
        request.records[i].a_bool = True
        request.records[i].int_32 = i
        request.records[i].int_64 = 112233
        request.records[i].a_str = 'abc'
    dump_request(request)

    print('\n### ManyFieldsList empty')
    request = test_pb2.ManyFieldsList()
    dump_request(request)

    print('\n### MapFields empty')
    request = test_pb2.MapFields()
    dump_request(request)


def dump_request(request):
    print('request:')
    pprint(request)
    print('json_format.MessageToDict:')
    pprint(MessageToDict(request, True, True, True))
    print('\nmessage_to_dict:')
    pprint(message_to_dict(request))


if __name__ == '__main__':
    print('CLIENT')
    main()
