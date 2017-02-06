# coding=utf-8
import log
from common.singleton.singleton import *
from common.sock_pack.pack import Unpack
"""处理函数都被绑定在此类里"""

class AppContext(Singleton):

    uriMapFunc = {}

    """绑定函数,函数同一为一个参数"""
    def addEntry(self, entry):
        self.uriMapFunc[entry.uri] = entry  # 将uri和对应的处理函数插入字典

    def getEntryByUri(self, uri):
        if uri in self.uriMapFunc.keys():
            return self.uriMapFunc[uri]
        else:
            return 0


class Entry():

    def bind_uri(self, messageClass, callBackFunc):
        self.uri = messageClass.get_uri()
        self.messageClass = messageClass
        self.callBackFunc = callBackFunc
        return self


    def handle_unpack(self, context, len):
        upk = Unpack(context, len)
        upk.load(self.messageClass)


