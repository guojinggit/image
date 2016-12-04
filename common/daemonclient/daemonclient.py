# coding=utf-8

from common.protocol.commonprotocol import *
from common.sock_connect.connect import *


class DaemonClient(Conn):

    def __init__(self, backLinkHander):
        self.backLinkHander = backLinkHander

    def getlist(self):
        task = TaskBase()
        task.setConn(self.getConn())
        msg = DaemonReq()
        msg.init("getlist", "127.0.0.1","8443","x","")
        pk = Pack(msg)
        task.setMessage(pk.get_data())
        SendQueue().getQueue(0).push(task)

    def on_getlist_rsp(self, msg, conn):
        print "daemon_list:"
        print msg.daemon_list

    def getConn(self,ip_port):
        if not self.conn:
            self.conn = ClientConn((ip_port), self.backLinkHander)
        return self.conn
        