from common.sock_pack.pack import *
from common.sock_pack.data_top import *

class DaemonReq(Data_top):
    uri = 20

    def get_uri(self):
        return self.uri

    def init(self, reqtype, name, ip, port, group, remark=""):
        self.reqtype = reqtype
        self.name = name
        self.ip = ip
        self.port = port
        self.group = group
        self.remark = remark

    def pack_me(self,pk):
        pk.pack(self.reqtype)
        pk.pack(self.name)
        pk.pack(self.ip)
        pk.pack(self.port)
        pk.pack(self.group)
        pk.pack(self.remark)

    def unpack_me(self, upk):
        self.reqtype = upk.unpack()
        self.name = upk.unpack()
        self.ip = upk.unpack()
        self.port = upk.unpack()
        self.group = upk.unpack()
        self.remark = upk.unpack()


class DaemonRsp(Data_top):
    uri = 21

    def get_uri(self):
        return self.uri

    def init(self, rsp, daemon_list):
        self.rsp = rsp
        self.daemon_list = daemon_list

    def pack_me(self, pk):
        pk.pack(self.rsp)
        pk.pack(self.daemon_list)

    def unpack_me(self,upk):
        self.rsp = upk.unpack()
        self.daemon_list = upk.unpack()
# req = DaemonReq()
# req.init("getlist","127.0.0.1","8444","x","")
# pk = Pack(req)
# print pk.get_data()