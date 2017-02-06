from common.sock_pack.pack import *
from common.sock_pack.data_top import *


class TestMessage(Data_top):

    uri = 10
    testdata1 = ""
    testdata2 = ""
    testdata3 = ""

    def get_uri(self):
        return self.uri

    def pack_me(self,pk):
        pk.pack(self.testdata1)
        pk.pack(self.testdata2)
        pk.pack(self.testdata3)

    def unpack_me(self, upk):
        self.testdata1 = upk.unpack()
        self.testdata2 = upk.unpack()
        self.testdata3 = upk.unpack()

class TestMessageRsp(Data_top):

    uri = 11

    def pack_me(self,pk):
        pk.pack("hello")

    def unpack_me(self,upk):
        self.testdata1 = upk.unpack()

