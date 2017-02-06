# coding=utf-8


from common.env.env import *

class TaskBase():

    uri = 0



    def setUri(self, uri):
        self.uri = uri
    def getUri(self):
        return self.uri

    def setProcFunc(self, callBackFunc):
        self.procFunc = callBackFunc

    def getProcFunc(self):
        return self.procFunc

    def setMessage(self, data):
        self.data = data

    def getMessage(self):
        return self.data

    def setConn(self, conn):
        self.conn = conn

    def getConn(self):
        return self.conn


class SendMsgTask(TaskBase):

    def set_ip_port(self, ip_port):
        self.ip_port = ip_port

    def sendmsg(self):
        if self.sendtype == "sendById":
            self.conn.sendbin(self.getMessage())
        elif self.sendtype == "sendByIp":
            self.conn = Env.framework.connManager.getConn(self.ip_port)
            self.conn.sendbin(self.getMessage())





