# coding=utf-8
import log

"""处理函数都被绑定在此类里"""

class AppContext():

    uriMapFunc = {}

    """单例模式"""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst = super(AppContext, cls).__new__(cls, *args, **kwargs)
        return cls._inst

    """绑定函数,函数同一为一个参数"""
    def addEntry(self, uri, callBackFunc):
        self.uriMapFunc[uri] = callBackFunc  # 将uri和对应的处理函数插入字典

    def getEntryByUri(self, uri):
        if uri in self.uriMapFunc.keys():
            return self.uriMapFunc[uri]
        else:
            return 0

# def print_(context):
#     log.info(context)
# app = AppContext()
# app.addEntry(10, print_)
# app.getEntryByUri(10)("hello")
