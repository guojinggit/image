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

class Framework(Singleton):

    def __init__(self, Config, Epoll, Server, Conn, BackLinkHander, Threads, Mysql, TaskQueue, SendQueue):
        self.localVal = threading.local()
        Env.setThreadLocal(self.localVal)
        Env.setFramework(self)

        self.config = Config().init()

        self.Mysql = Mysql
        self.mysql = Mysql(self.config)

        self.epoll = Epoll()

        self.backLinkHandler = BackLinkHander()

        self.server = Server(self.config, Conn, self.backLinkHandler)
        self.epoll.register_with_handler(self.server)

        self.taskQueue = TaskQueue(self.config)

        self.sendQueue = SendQueue(self.config)

        self.threads = Threads(self.config)
        self.threads.start()

    def start(self):
        self.epoll.server_forever()

Framework_AN94 = Framework(Config, Epoll, TcpServer, Conn, BackLinkHandler, Threads, Mysql, TaskQueue, SendQueue)
