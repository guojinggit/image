# coding=utf-8
import sys
sys.path.append("..")
sys.path.append(".")
from common.sock_connect.connect import *
from common.backLinkHandler.backLinkHandler import *
from common.protocol.tespprotocol import *
from common.task.taskbase import *
from common.config.config import *
from common.mysql.mysql import *
from common.thread.threads import *
from common.appContext.appContext import *
from common.env.env import *
from common.daemonclient.daemonclient import *
from common.manager.manager import *
from common.connectManager.connManager import *

class Framework(Singleton):

    def __init__(self, Config, Epoll, Server, ServerConn, ConnManager, AppContext, Entry,
                 BackLinkHander, Threads, Mysql, Manager):

        self.localVal = threading.local()
        Env.setThreadLocal(self.localVal)
        Env.setFramework(self)
        self.config = Config().init()
        self.Mysql = Mysql
        self.mysql = Mysql(self.config)
        self.epoll = Epoll()
        self.Entry = Entry
        self.appContext = AppContext()
        self.backLinkHandler = BackLinkHander()
        self.server = Server(self.config, ServerConn, self.backLinkHandler)
        self.epoll.register_with_handler(self.server)
        self.connManager = ConnManager()
        self.manager = Manager(self.config)
        self.epoll.add_handler(self.manager)
        self.threads = Threads(self.config)
        self.threads.start()

    def bind_uri(self, msg, callBackFunc):
        enrty = self.Entry().bind_uri(msg, callBackFunc)
        self.appContext.addEntry(enrty)

    def start(self):
        self.epoll.server_forever()

Framework_AN94 = Framework(Config, Epoll, TcpServer, ServerConn, ConnManager, AppContext, Entry,
                           BackLinkHandler, Threads, Mysql, Manager)
